#!/usr/bin/env python3
"""Lookup source-backed benchmark claims from sources.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
SOURCES = REPO / "sources.json"
OUTPUT_FIELDS = ("id", "claim", "evidence_class", "source", "date", "url", "scope", "status", "tags")


def load_sources(path: Path = SOURCES) -> list[dict[str, Any]]:
    data = json.loads(path.read_text())
    return list(data.get("benchmarks", []))


def normalize_entry(entry: dict[str, Any]) -> dict[str, Any]:
    return {field: entry.get(field) for field in OUTPUT_FIELDS}


def score_entry(entry: dict[str, Any], terms: list[str]) -> int:
    haystack = " ".join(
        str(entry.get(field, ""))
        for field in ("id", "claim", "source", "scope", "evidence_class", "date")
    ).lower()
    tags = " ".join(str(tag) for tag in entry.get("tags", [])).lower()
    haystack = f"{haystack} {tags}"
    return sum(1 for term in terms if term in haystack)


def lookup_sources(
    *,
    source_id: str | None = None,
    query: str | None = None,
    evidence_class: str | None = None,
    status: str | None = "active",
    limit: int = 10,
    path: Path = SOURCES,
) -> list[dict[str, Any]]:
    entries = load_sources(path)

    if status:
        entries = [entry for entry in entries if entry.get("status") == status]
    if evidence_class:
        entries = [entry for entry in entries if entry.get("evidence_class") == evidence_class]
    if source_id:
        entries = [entry for entry in entries if entry.get("id") == source_id]
    if query:
        terms = [term.lower() for term in query.split() if term.strip()]
        scored = [(score_entry(entry, terms), entry) for entry in entries]
        entries = [entry for score, entry in sorted(scored, key=lambda item: item[0], reverse=True) if score > 0]

    return [normalize_entry(entry) for entry in entries[:limit]]


def render_text(results: list[dict[str, Any]]) -> str:
    if not results:
        return "No matching sources found."

    blocks = []
    for entry in results:
        blocks.append(
            "\n".join(
                [
                    f"id: {entry['id']}",
                    f"claim: {entry['claim']}",
                    f"evidence_class: {entry['evidence_class']}",
                    f"source: {entry['source']}",
                    f"date: {entry['date']}",
                    f"url: {entry['url']}",
                    f"scope: {entry['scope']}",
                ]
            )
        )
    return "\n\n".join(blocks)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lookup source-backed benchmark claims.")
    parser.add_argument("--id", dest="source_id", help="Exact source id.")
    parser.add_argument("--query", help="Search terms for claim/source/scope/id.")
    parser.add_argument("--evidence-class", help="Filter by evidence_class.")
    parser.add_argument("--status", default="active", help="Filter by status. Use empty string for all.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum results.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args(argv)

    if not args.source_id and not args.query and not args.evidence_class:
        parser.error("provide --id, --query, or --evidence-class")

    status = args.status or None
    results = lookup_sources(
        source_id=args.source_id,
        query=args.query,
        evidence_class=args.evidence_class,
        status=status,
        limit=args.limit,
    )

    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
    else:
        print(render_text(results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
