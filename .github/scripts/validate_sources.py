#!/usr/bin/env python3
"""Validate sources.json structure: required fields, ids, and allowed values."""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "sources.json"

REQUIRED_FIELDS = [
    "id",
    "claim",
    "source",
    "url",
    "date",
    "scope",
    "domain",
    "status",
    "updated_at",
    "evidence_class",
]


def main() -> int:
    data = json.loads(SOURCES.read_text())
    if "_meta" not in data or "evidence_classes" not in data["_meta"]:
        print("ERROR: _meta.evidence_classes missing")
        return 1
    if "domains" not in data["_meta"]:
        print("ERROR: _meta.domains missing")
        return 1
    if "status_values" not in data["_meta"]:
        print("ERROR: _meta.status_values missing")
        return 1
    if "benchmarks" not in data:
        print("ERROR: benchmarks key missing")
        return 1

    allowed = set(data["_meta"]["evidence_classes"].keys())
    allowed_domains = set(data["_meta"]["domains"].keys())
    allowed_statuses = set(data["_meta"]["status_values"].keys())
    errors: list[str] = []
    seen_ids: set[str] = set()

    for i, entry in enumerate(data["benchmarks"]):
        for field in REQUIRED_FIELDS:
            if field not in entry:
                errors.append(f"entry {i}: missing field '{field}'")
        entry_id = entry.get("id")
        if entry_id:
            if entry_id in seen_ids:
                errors.append(f"entry {i}: duplicate id '{entry_id}'")
            seen_ids.add(entry_id)
        cls = entry.get("evidence_class")
        if cls and cls not in allowed:
            errors.append(f"entry {i}: unknown evidence_class '{cls}'")
        domain = entry.get("domain")
        if domain and domain not in allowed_domains:
            errors.append(f"entry {i}: unknown domain '{domain}'")
        status = entry.get("status")
        if status and status not in allowed_statuses:
            errors.append(f"entry {i}: unknown status '{status}'")
        tags = entry.get("tags")
        if tags is not None and not isinstance(tags, list):
            errors.append(f"entry {i}: tags must be a list")

    if errors:
        for e in errors:
            print(e)
        return 1

    print(
        "sources.json valid: "
        f"{len(data['benchmarks'])} entries, "
        f"{len(allowed)} evidence classes, "
        f"{len(seen_ids)} stable ids"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
