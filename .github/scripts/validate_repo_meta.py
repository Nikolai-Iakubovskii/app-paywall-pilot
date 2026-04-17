#!/usr/bin/env python3
"""Validate framework metadata against repo state."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
META = json.loads((REPO / "framework-meta.json").read_text())
SOURCES = json.loads((REPO / "sources.json").read_text())


def main() -> int:
    errors: list[str] = []

    module_count = len(list((REPO / "modules").glob("*.md")))
    if META["module_count"] != module_count:
        errors.append(
            f"framework-meta.json module_count={META['module_count']} but found {module_count} modules/"
        )

    source_count = len(SOURCES["benchmarks"])
    if META["source_count"] != source_count:
        errors.append(
            f"framework-meta.json source_count={META['source_count']} but found {source_count} sources"
        )

    for key in ("canonical_research_brief", "tool_cli_path", "tool_module_path"):
        target = REPO / META[key]
        if not target.exists():
            errors.append(f"framework-meta.json {key} points to missing file: {META[key]}")

    for brief in META.get("legacy_research_briefs", []):
        target = REPO / brief
        if not target.exists():
            errors.append(f"Missing legacy research brief: {brief}")

    if errors:
        for error in errors:
            print(error)
        return 1

    print(
        "framework-meta.json valid: "
        f"{module_count} modules, {source_count} sources, "
        f"canonical brief {META['canonical_research_brief']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
