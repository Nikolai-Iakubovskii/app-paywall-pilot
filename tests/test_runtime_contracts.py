from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class RuntimeContractTests(unittest.TestCase):
    def test_skill_core_stays_thin(self) -> None:
        line_count = len((REPO / "SKILL.md").read_text().splitlines())
        self.assertLessEqual(line_count, 400)

    def test_runtime_docs_exist(self) -> None:
        for rel in (
            "runtime/data-inventory.md",
            "runtime/input-contracts.md",
            "runtime/reference-routing.md",
            "runtime/golden-prompts.json",
        ):
            self.assertTrue((REPO / rel).exists(), rel)

    def test_golden_prompts_have_required_fields(self) -> None:
        data = json.loads((REPO / "runtime/golden-prompts.json").read_text())
        self.assertEqual(data["version"], 1)
        self.assertGreaterEqual(len(data["prompts"]), 5)

        required = {"id", "prompt", "expected_mode", "max_references", "must_include", "must_not_include"}
        for prompt in data["prompts"]:
            self.assertTrue(required.issubset(prompt.keys()), prompt)


if __name__ == "__main__":
    unittest.main()
