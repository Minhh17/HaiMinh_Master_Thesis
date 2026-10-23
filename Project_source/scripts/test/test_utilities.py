"""Regression tests for diagnostics and validation failure modes, no hardware fiction."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


validator = module('validator', 'scripts/maintenance/validate_workspace.py')
doctor = module('doctor', 'scripts/setup/doctor.py')
builder = module('builder', 'scripts/build/run.py')
upstream = module('upstream_test', 'scripts/setup/upstream.py')


class Diagnostics(unittest.TestCase):
    def test_missing_tool_does_not_pass(self):
        self.assertEqual(doctor.probe('fake-tool', [], finder=lambda _: None)['status'], 'BLOCKED')

    def test_nonzero_version_is_failure(self):
        result = subprocess.CompletedProcess(['tool'], 1, '', 'failed')
        row = doctor.probe('fake-tool', [], finder=lambda _: '/tool', runner=lambda *a, **k: result)
        self.assertEqual(row['status'], 'FAIL')

    def test_timeout_is_blocked(self):
        def timeout(*args, **kwargs):
            raise subprocess.TimeoutExpired('tool', 30)
        self.assertEqual(doctor.probe('fake-tool', [], finder=lambda _: '/tool', runner=timeout)['status'], 'BLOCKED')

    def test_relative_links_and_missing_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'exists.md').write_text('ok')
            note = root / 'README.md'
            note.write_text('[ok](exists.md) [bad](absent.md)\n```sh\n[example](not-a-file)\n```\n')
            errors = validator.markdown_errors(note, root)
            self.assertEqual(len(errors), 1)
            self.assertIn('absent.md', errors[0])

    def test_documentation_cannot_link_outside_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            note = root / 'README.md'
            note.write_text('[bad](../outside.md)')
            self.assertIn('escapes repository', validator.markdown_errors(note, root)[0])

    def test_real_gitignore_protects_artifacts_and_keeps_sources(self):
        self.assertEqual(validator.check_ignore(), [])

    def test_tbd_board_never_builds(self):
        with self.assertRaisesRegex(ValueError, 'board TBD'):
            builder.board_target('board', {'status': 'TBD'}, {'candidates': []})

    def test_board_target_and_adr_must_match(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'docs/decisions').mkdir(parents=True)
            (root / 'docs/decisions/choice.md').write_text('approved test fixture')
            candidates = {'candidates': [{'board': 'example', 'target': 'synth_example'}]}
            selected = {'status': 'approved', 'board': 'example', 'target': 'synth_example',
                        'adr': 'docs/decisions/choice.md'}
            self.assertEqual(builder.board_target('example', selected, candidates, root), 'synth_example')
            selected['target'] = 'synth_other'
            with self.assertRaisesRegex(ValueError, 'mapping'):
                builder.board_target('example', selected, candidates, root)
            selected['target'] = 'synth_example'
            selected['adr'] = '../unreviewed.md'
            with self.assertRaisesRegex(ValueError, 'ADR'):
                builder.board_target('example', selected, candidates, root)

    def test_upstream_rejects_changed_remote_or_revision(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.git').mkdir()
            entry = {'url': 'https://github.com/lowRISC/ibex-demo-system.git', 'commit': 'a' * 40}
            with patch.object(upstream, 'git', return_value='https://example.invalid/other'):
                with self.assertRaisesRegex(ValueError, 'origin differs'):
                    upstream.verify(root, entry)
            with patch.object(upstream, 'git', side_effect=[entry['url'], 'b' * 40]):
                with self.assertRaisesRegex(ValueError, 'HEAD differs'):
                    upstream.verify(root, entry)

    def test_upstream_preserves_dirty_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.git').mkdir()
            entry = {'url': 'https://github.com/lowRISC/ibex-demo-system.git', 'commit': 'a' * 40}
            with patch.object(upstream, 'git', side_effect=[entry['url'], entry['commit'], ' M source.sv']):
                with self.assertRaisesRegex(ValueError, 'modified'):
                    upstream.verify(root, entry)

    def test_upstream_rejects_untracked_core_injection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.git').mkdir()
            entry = {'url': 'https://github.com/lowRISC/ibex-demo-system.git', 'commit': 'a' * 40}
            with patch.object(upstream, 'git', side_effect=[entry['url'], entry['commit'], '?? injected.core']) as mocked:
                with self.assertRaisesRegex(ValueError, 'untracked'):
                    upstream.verify(root, entry)
                self.assertEqual(mocked.call_args[0][-1], '--untracked-files=all')


    def test_malformed_lock_is_diagnostic_not_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'third_party').mkdir()
            lock = root / 'third_party/upstream.lock.json'
            lock.write_text('{invalid')
            errors = validator.check_configs([lock], root)
            self.assertTrue(any('invalid config' in error for error in errors))

    def test_mutable_python_pin_and_incomplete_template_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'third_party').mkdir()
            lock = root / 'third_party/upstream.lock.json'
            lock.write_text(json.dumps({'schema_version': 1, 'dependencies': [],
                                        'python_vcs_dependencies': [{'url': 'https://github.com/lowRISC/fusesoc.git', 'commit': 'main'}]}))
            errors = validator.check_configs([lock], root)
            self.assertTrue(any('40-hex' in error for error in errors))
            self.assertTrue(any('missing field dataset_id' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
