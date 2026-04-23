#!/usr/bin/env python3
"""Validate runtime docs and context-budget guardrails."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MAX_SKILL_LINES = 400
REQUIRED_FILES = [
    "runtime/data-inventory.md",
    "runtime/input-contracts.md",
    "runtime/reference-routing.md",
    "runtime/golden-prompts.json",
    "tools/source_lookup.py",
]
REQUIRED_MODES = ["quick", "audit", "calculator", "compliance", "pattern", "implementation"]


def main() -> int:
    errors: list[str] = []

    skill_lines = len((REPO / "SKILL.md").read_text().splitlines())
    if skill_lines > MAX_SKILL_LINES:
        errors.append(f"SKILL.md is {skill_lines} lines (> {MAX_SKILL_LINES})")

    for rel in REQUIRED_FILES:
        if not (REPO / rel).exists():
            errors.append(f"Missing runtime file: {rel}")

    contracts = (REPO / "runtime/input-contracts.md").read_text()
    routing = (REPO / "runtime/reference-routing.md").read_text()
    for mode in REQUIRED_MODES:
        if f"`{mode}`" not in contracts:
            errors.append(f"input-contracts.md missing mode `{mode}`")
        if f"`{mode}`" not in routing:
            errors.append(f"reference-routing.md missing mode `{mode}`")

    prompts = json.loads((REPO / "runtime/golden-prompts.json").read_text())
    required_prompt_fields = {"id", "prompt", "expected_mode", "max_references", "must_include", "must_not_include"}
    for index, prompt in enumerate(prompts.get("prompts", [])):
        missing = required_prompt_fields - set(prompt)
        if missing:
            errors.append(f"golden prompt {index} missing fields: {sorted(missing)}")
        if prompt.get("expected_mode") not in REQUIRED_MODES:
            errors.append(f"golden prompt {prompt.get('id')} has unknown expected_mode")

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"runtime contracts valid: SKILL.md {skill_lines} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
