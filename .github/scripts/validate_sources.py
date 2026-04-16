#!/usr/bin/env python3
"""Validate sources.json structure: required fields, allowed evidence classes."""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "sources.json"

REQUIRED_FIELDS = ["claim", "source", "url", "date", "scope", "evidence_class"]


def main() -> int:
    data = json.loads(SOURCES.read_text())
    if "_meta" not in data or "evidence_classes" not in data["_meta"]:
        print("ERROR: _meta.evidence_classes missing")
        return 1
    if "benchmarks" not in data:
        print("ERROR: benchmarks key missing")
        return 1

    allowed = set(data["_meta"]["evidence_classes"].keys())
    errors: list[str] = []

    for i, entry in enumerate(data["benchmarks"]):
        for field in REQUIRED_FIELDS:
            if field not in entry:
                errors.append(f"entry {i}: missing field '{field}'")
        cls = entry.get("evidence_class")
        if cls and cls not in allowed:
            errors.append(f"entry {i}: unknown evidence_class '{cls}'")

    if errors:
        for e in errors:
            print(e)
        return 1

    print(
        f"sources.json valid: {len(data['benchmarks'])} entries, {len(allowed)} evidence classes"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
