"""Offline structural checks; explicitly does not validate RTL or FPGA behavior."""
import csv
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = '''README.md AGENTS.md Makefile .gitignore .gitattributes .editorconfig
WORKSPACE_HANDOFF_REPORT.md
planning/README.md planning/roadmap.md planning/phase1-plan.md
planning/backlog.md planning/milestones.md planning/weekly/week-01.md
knowledge/README.md research/README.md research/research-questions.md
research/hypotheses.md research/research-gaps.md
research/literature/references.bib research/literature/literature-matrix.csv
docs/architecture/system-context.md docs/design/phase1-scope.md
docs/guides/local-setup.md docs/guides/simulation.md docs/guides/fpga-bringup.md
docs/guides/vivado-workflow.md docs/guides/debugging.md
docs/verification/verification-matrix.md tools/tool-versions.md
datasets/catalog.md datasets/manifests/dataset-template.yaml
experiments/README.md third_party/upstream.lock.json
ai/README.md ai/project-context.md ai/current-state.md ai/next-actions.md
.github/workflows/workspace.yml .github/pull_request_template.md'''.split()
EXCLUDED = {'.git', '.venv', '__pycache__', 'checkouts', 'build', 'local', 'raw'}
IGNORED_CASES = ['.venv/bin/python', 'build/x', 'project.runs/x', '.Xil/x',
                 'project.cache/x', 'project.gen/x', 'wave.vcd', 'wave.fst',
                 'a.bit', 'a.elf', 'a.dcp', 'a.log', 'a.jou', 'Xilinx.lic',
                 'license.dat', '.env', '.env.local', 'private.key',
                 'datasets/raw/x.csv', 'data.mat', 'paper.pdf',
                 'third_party/checkouts/ibex/rtl/ibex_core.sv', 'tools/local/bin/tool']
SOURCE_CASES = ['hardware/rtl/top.sv', 'hardware/rtl/block.v',
                'firmware/apps/main.c', 'scripts/test/test_example.py',
                'hardware/constraints/board.xdc', 'fpga/scripts/report.tcl',
                'docs/reports/timing-summary.md', 'experiments/results/run.json',
                'experiments/results/metrics.csv', 'third_party/LICENSE',
                'datasets/manifests/example.yaml']


def files(root=ROOT):
    found = []
    for directory, subdirs, names in os.walk(str(root)):
        subdirs[:] = [name for name in subdirs if name not in EXCLUDED]
        found.extend(Path(directory) / name for name in names)
    return sorted(found)


def markdown_errors(path, root=ROOT):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'(?ms)^```.*?^```[^\n]*', '', text)
    errors = []
    for raw in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
        target = raw.strip().split(' "', 1)[0].strip('<>')
        url = urlsplit(target)
        if url.scheme or target.startswith('#'):
            continue
        if not url.path:
            continue
        dest = (path.parent / unquote(url.path)).resolve()
        if root.resolve() not in (dest, *dest.parents):
            errors.append('{}: link escapes repository: {}'.format(path.relative_to(root), target))
        elif not dest.exists():
            errors.append('{}: broken local link: {}'.format(path.relative_to(root), target))
    return errors


def check_ignore(root=ROOT):
    errors = []
    with tempfile.TemporaryDirectory(prefix='ibex-ignore-') as directory:
        temp = Path(directory)
        shutil.copyfile(str(root / '.gitignore'), str(temp / '.gitignore'))
        subprocess.run(['git', 'init', '-q', str(temp)], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for ignored, paths in [(True, IGNORED_CASES), (False, SOURCE_CASES)]:
            for path in paths:
                result = subprocess.run(['git', '-C', str(temp), 'check-ignore', '--no-index', '-q', path])
                if result.returncode not in (0, 1) or (result.returncode == 0) != ignored:
                    errors.append('gitignore: {} should be {}'.format(path, 'ignored' if ignored else 'trackable'))
    return errors


def check_configs(paths, root=ROOT):
    errors = []
    parsed = {}
    try:
        import yaml
    except ImportError:
        return ['PyYAML unavailable: install tools/requirements-check.txt in a local venv']
    for path in paths:
        if path.suffix not in {'.json', '.yaml', '.yml'}:
            continue
        try:
            data = json.loads(path.read_text()) if path.suffix == '.json' else yaml.safe_load(path.read_text())
            if not isinstance(data, dict):
                errors.append('{}: expected top-level mapping'.format(path.relative_to(root)))
            else:
                parsed[str(path.relative_to(root))] = data
        except (ValueError, yaml.YAMLError) as exc:
            errors.append('{}: invalid config: {}'.format(path.relative_to(root), exc))
    lock = parsed.get('third_party/upstream.lock.json', {})
    if lock.get('schema_version') != 1 or not lock.get('dependencies'):
        errors.append('upstream lock: invalid schema or empty dependencies')
    entries = []
    for field in ['dependencies', 'python_vcs_dependencies']:
        group = lock.get(field, [])
        if not isinstance(group, list):
            errors.append('upstream lock: {} must be a list'.format(field))
        else:
            entries.extend(group)
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append('upstream lock: dependency must be a mapping')
            continue
        if not re.fullmatch(r'[0-9a-f]{40}', entry.get('commit', '')):
            errors.append('upstream lock: immutable 40-hex commit required')
        if not entry.get('url', '').startswith('https://github.com/lowRISC/'):
            errors.append('upstream lock: expected inspected lowRISC HTTPS remote')
    workflow = parsed.get('.github/workflows/workspace.yml', {})
    # PyYAML's YAML 1.1 loader reads GitHub's `on` key as True.
    if 'on' not in workflow and True not in workflow:
        errors.append('CI: event triggers missing')
    if not workflow.get('jobs'):
        errors.append('CI: jobs missing')
    required_fields = {
        'datasets/manifests/dataset-template.yaml': [
            'dataset_id', 'name', 'version', 'source.url', 'source.doi',
            'license.identifier', 'license.restrictions', 'capture.device',
            'sample.format', 'sample.dimensions', 'sample.bit_width', 'sample.sample_rate_hz',
            'storage.local_path', 'checksums.files', 'extraction.commands', 'processing.steps',
            'split.strategy', 'contributor.recorded_by', 'citation.preferred_text', 'validation.state'],
        'experiments/configurations/experiment-template.yaml': [
            'experiment_id', 'run_id', 'question_or_requirement_ids', 'work_item_ids', 'adr_paths', 'test_ids',
            'plan.acceptance_rule', 'plan.correctness_oracle', 'source.repository_commit',
            'source.upstream_revisions', 'source.firmware_revision', 'source.config_sha256',
            'environment.tools', 'environment.board', 'execution.commands',
            'measurements.state', 'measurements.records', 'artifacts.files'],
    }
    for name, fields in required_fields.items():
        data = parsed.get(name, {})
        if data.get('schema_version') != 1 or data.get('record_type') != 'template':
            errors.append(name + ': template marker/schema missing')
        for field in fields:
            node = data
            for key in field.split('.'):
                if not isinstance(node, dict) or key not in node:
                    errors.append(name + ': missing field ' + field)
                    break
                node = node[key]
        state = data.get('validation', data.get('measurements', {}))
        if not isinstance(state, dict) or state.get('state') != 'NOT_RUN':
            errors.append(name + ': unused template state must be NOT_RUN')
    selected = parsed.get('fpga/boards/selected-board.json', {})
    if selected.get('status') == 'TBD':
        if any(selected.get(field) is not None for field in ['board', 'target', 'adr']):
            errors.append('board TBD must not silently select board/target/ADR')
    elif selected.get('status') == 'approved':
        if not all(selected.get(field) for field in ['board', 'target', 'adr']):
            errors.append('approved board requires board, target and ADR')
    else:
        errors.append('board record requires status TBD or approved')
    return errors


def check_hygiene(paths):
    errors = []
    private_key = re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
    for path in paths:
        rel = str(path.relative_to(ROOT))
        if path.stat().st_size > 1024 * 1024:
            errors.append('{}: exceeds 1 MiB review threshold'.format(rel))
        if path.suffix.lower() in {'.lic', '.pem', '.key', '.bit', '.pdf', '.mat', '.npy'}:
            errors.append('{}: restricted asset in source tree'.format(rel))
        try:
            content = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        if private_key.search(content):
            errors.append('{}: private key marker'.format(rel))
    result = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-ci', '--exclude-standard'],
                            text=True, capture_output=True)
    if result.returncode != 0:
        errors.append('Git index unavailable; initialize local repository first')
    elif result.stdout.strip():
        errors.append('ignored files are tracked: ' + result.stdout.strip())
    return errors


def main():
    errors = ['missing required file: ' + name for name in REQUIRED if not (ROOT / name).is_file()]
    paths = files()
    for path in paths:
        if path.suffix == '.md':
            errors.extend(markdown_errors(path))
    if not errors:
        errors.extend(check_configs(paths))
    matrix = ROOT / 'research/literature/literature-matrix.csv'
    if matrix.exists():
        with matrix.open(newline='', encoding='utf-8') as stream:
            reader = csv.DictReader(stream)
            required = {'paper_id', 'authors', 'year', 'evidence_status', 'source_url', 'notes_path'}
            if not required.issubset(reader.fieldnames or []):
                errors.append('literature CSV: missing required provenance columns')
            for row in reader:
                if None in row:
                    errors.append('literature CSV: unexpected extra values')
    errors.extend(check_ignore())
    errors.extend(check_hygiene(paths))
    if errors:
        for error in errors:
            print('FAIL: ' + error)
        return 1
    print('PASS: {} required files; {} source files; local Markdown file links; JSON/YAML;'.format(len(REQUIRED), len(paths)))
    print('      literature CSV; {} ignore/track cases; size/key/index hygiene.'.format(len(IGNORED_CASES) + len(SOURCE_CASES)))
    print('Scope: offline workspace checks; no external URL, citation, RTL, FPGA or CI-service execution claim.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
