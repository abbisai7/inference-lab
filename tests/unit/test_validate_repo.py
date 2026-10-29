"""Behavioral tests for foundation validation using isolated temporary records."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[2] / "scripts/validate_repo.py"
spec = importlib.util.spec_from_file_location("validate_repo", SOURCE)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

RECORD = """# Change: Example
Status: Complete
## Summary
A small fixture.
## Requirements and acceptance criteria
- R1 — Preserve behavior: requests retain their expected result.
## Implementation plan
- [x] Implement and check.
## Validation and coverage
| Named requirement | Implementation | Evidence | Status |
| --- | --- | --- | --- |
| R1 — Preserve behavior | src/example.py | Executed focused test; passed | Verified |
## Operational impact
No deployment.
## Results and learning
Verified fixture.
"""


class RecordTests(unittest.TestCase):
    def check(self, content):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "record.md"
            path.write_text(content)
            return validator.check_record(path)

    def test_complete_with_evidence_passes(self):
        self.assertEqual([], self.check(RECORD))

    def test_unfinished_complete_fails(self):
        self.assertTrue(any("unfinished" in e for e in self.check(RECORD.replace("[x]", "[ ]"))))

    def test_pending_complete_fails(self):
        self.assertTrue(any("unverified" in e for e in self.check(RECORD.replace("| Verified |", "| Pending |"))))

    def test_missing_requirement_coverage_fails(self):
        self.assertTrue(any("must match" in e for e in self.check(RECORD.replace("- R1 —", "- R2 —"))))

    def test_duplicate_requirement_fails(self):
        content = RECORD.replace("## Implementation plan", "- R1 — Duplicate name: duplicate behavior.\n## Implementation plan")
        self.assertTrue(any("duplicate requirement" in e for e in self.check(content)))

    def test_placeholder_evidence_fails(self):
        self.assertTrue(any("lacks" in e for e in self.check(RECORD.replace("Executed focused test; passed", "Pending"))))

    def test_in_progress_can_have_pending_work(self):
        content = RECORD.replace("Status: Complete", "Status: In progress").replace("[x]", "[ ]").replace("| Verified |", "| Pending |")
        self.assertEqual([], self.check(content))

    def test_examples_do_not_create_unfinished_work(self):
        self.assertEqual([], self.check(RECORD + "\n```markdown\n- [ ] Example only\n```\n"))

    def test_markdown_list_markers_cannot_hide_unfinished_work(self):
        for marker in ["-", "*", "+", "1.", "2)"]:
            with self.subTest(marker=marker):
                errors = self.check(RECORD + "\n" + marker + " [ ] Verify cancellation.\n")
                self.assertTrue(any("unfinished" in e for e in errors))

    def test_markdown_list_markers_cannot_hide_uncovered_requirements(self):
        for marker in ["-", "*", "+", "1.", "2)"]:
            with self.subTest(marker=marker):
                content = RECORD.replace("## Implementation plan", marker + " R2 — Stop work: cancellation stops execution.\n## Implementation plan")
                self.assertTrue(any("must match" in e for e in self.check(content)))

    def test_missing_required_section_fails(self):
        self.assertTrue(any("missing section" in e for e in self.check(RECORD.replace("## Operational impact", "## Other"))))


class RepositoryTests(unittest.TestCase):
    def fixture(self, root):
        for name in validator.REQUIRED:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Fixture\n")
        for name in validator.SKILLS:
            folder = root / ".agents/skills" / name
            (folder / "agents").mkdir(parents=True)
            (folder / "SKILL.md").write_text("# Fixture\n")
            (folder / "agents/openai.yaml").write_text("interface: {}\n")
        (root / "harness/build/change-0001-example.md").write_text(RECORD)

    def test_links_missing_files_and_removed_prompts(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            self.assertTrue(validator.validate(root)["ok"])
            (root / "docs/workflow.md").write_text("[Broken](missing.md)\n")
            self.assertTrue(any("broken link" in e for e in validator.validate(root)["errors"]))
            (root / "docs/workflow.md").write_text("[OK](../README.md)\n")
            self.assertTrue(validator.validate(root)["ok"])
            (root / "PROMPTS.md").touch()
            self.assertFalse(validator.validate(root)["ok"])

    def test_escaping_links_are_rejected_without_reading_external_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            (root / "docs/workflow.md").write_text("[Outside](../../outside.md)\n")
            self.assertTrue(any("escapes" in e for e in validator.validate(root)["errors"]))

    def test_missing_skill_and_required_file_fail(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            (root / "AGENTS.md").unlink()
            (root / ".agents/skills/change-delivery/SKILL.md").unlink()
            errors = validator.validate(root)["errors"]
            self.assertTrue(any("required file" in e for e in errors))
            self.assertTrue(any("skill files" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
