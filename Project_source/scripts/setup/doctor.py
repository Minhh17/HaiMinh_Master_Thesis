"""Read-only, bounded tool probes. No license values or host identifiers logged."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess

TOOLS = {
    'git': ['--version'], 'python3': ['--version'], 'make': ['--version'],
    'cmake': ['--version'], 'gcc': ['--version'], 'g++': ['--version'],
    'fusesoc': ['--version'], 'verilator': ['--version'],
    'riscv32-unknown-elf-gcc': ['--version'],
    'riscv64-unknown-elf-gcc': ['--version'],
    'openocd': ['--version'], 'gdb-multiarch': ['--version'],
    'riscv32-unknown-elf-gdb': ['--version'], 'gtkwave': ['--version'],
    'vivado': ['-version'],
}


def probe(name, flags, finder=shutil.which, runner=subprocess.run):
    executable = os.environ.get('VIVADO_BIN') if name == 'vivado' else None
    executable = executable or finder(name)
    if not executable:
        return {'tool': name, 'status': 'BLOCKED', 'detail': (
            'USER-AVAILABLE / AGENT-NOT-VERIFIED; not found on PATH'
            if name == 'vivado' else 'not found on PATH')}
    try:
        result = runner([executable] + flags, capture_output=True, text=True,
                        timeout=30, errors='replace')
        output = (result.stdout + result.stderr).strip().splitlines()
        return {'tool': name, 'status': 'PASS' if result.returncode == 0 else 'FAIL',
                'path': executable, 'exit_code': result.returncode,
                'detail': output[0][:250] if output else '(no version output)'}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {'tool': name, 'status': 'BLOCKED', 'detail': type(exc).__name__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vivado-only', action='store_true')
    parser.add_argument('--json', type=Path, help='save report to a chosen path')
    args = parser.parse_args()
    names = ['vivado'] if args.vivado_only else list(TOOLS)
    rows = [probe(name, TOOLS[name]) for name in names]
    for row in rows:
        print('{status}: {tool}: {detail}'.format(**row))
    print('Version detection does not verify tool compatibility, license, build or hardware.')
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({'scope': 'version-probes-only', 'tools': rows},
                                        indent=2) + '\n', encoding='utf-8')
    # General inventory may complete with optional tools absent; Vivado gate may not.
    return 0 if not args.vivado_only or rows[0]['status'] == 'PASS' else 2


if __name__ == '__main__':
    raise SystemExit(main())
