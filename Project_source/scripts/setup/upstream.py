"""Verify immutable upstream checkouts, or explicitly acquire one (network action)."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
ALLOWED = {
    'ibex-demo-system': 'https://github.com/lowRISC/ibex-demo-system.git',
    'ibex-demo-system-labs': 'https://github.com/lowRISC/ibex-demo-system-labs.git',
    'ibex': 'https://github.com/lowRISC/ibex.git',
}


def entry_for(name):
    entries = json.loads((ROOT / 'third_party/upstream.lock.json').read_text())['dependencies']
    entry = next((item for item in entries if item['name'] == name), None)
    if not entry or entry.get('url') != ALLOWED.get(name):
        raise ValueError('dependency name/remote differs from reviewed allowlist')
    if not re.fullmatch(r'[0-9a-f]{40}', entry.get('commit', '')):
        raise ValueError('immutable 40-character commit required')
    return entry


def git(path, *args):
    result = subprocess.run(['git', '-C', str(path)] + list(args), check=True,
                            capture_output=True, text=True, timeout=180)
    return result.stdout.strip()


def verify(path, entry):
    if not (path / '.git').exists():
        raise ValueError('upstream checkout absent: review third_party/README.md, then make upstream with download approval')
    if git(path, 'remote', 'get-url', 'origin') != entry['url']:
        raise ValueError('origin differs from locked HTTPS URL; checkout left unchanged')
    if git(path, 'rev-parse', 'HEAD') != entry['commit']:
        raise ValueError('HEAD differs from immutable lock; checkout left unchanged')
    if git(path, 'status', '--porcelain', '--untracked-files=all'):
        raise ValueError('upstream files modified or untracked; preserve changes and review manually')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fetch', action='store_true', help='explicit network acquisition; approval required for agent use')
    parser.add_argument('--name', choices=['ibex-demo-system', 'ibex-demo-system-labs'], default='ibex-demo-system')
    args = parser.parse_args()
    try:
        entry = entry_for(args.name)
        path = ROOT / 'third_party/checkouts' / args.name
        if not path.exists() and args.fetch:
            path.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(['git', 'init', '-q', str(path)], check=True)
            git(path, 'remote', 'add', 'origin', entry['url'])
            git(path, 'fetch', '--depth', '1', 'origin', entry['commit'])
            git(path, 'checkout', '--detach', entry['commit'])
        verify(path, entry)
        print('PASS: immutable remote/HEAD/clean source tree: ' + args.name)
        print('Not a build or nested dependency execution result.')
        return 0
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print('BLOCKED: {}'.format(exc))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
