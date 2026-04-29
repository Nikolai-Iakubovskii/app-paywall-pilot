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
FIELD_WEIGHTS = {
    "id": 5,
    "claim": 4,
    "tags": 4,
    "source": 2,
    "scope": 2,
    "evidence_class": 1,
    "date": 1,
}
ALIASES = {
    "ab": ["a/b", "experiment", "test"],
    "abtest": ["a/b", "experiment", "test"],
    "apple": ["app store", "ios", "storekit"],
    "complaint": ["complaints", "refund", "billing"],
    "conversion": ["convert", "paid", "purchase"],
    "design": ["paywall", "screen", "visual", "copy"],
    "geo": ["region", "market", "localization", "pricing"],
    "localize": ["localization", "locale", "market"],
    "plan": ["plans", "product", "products"],
    "plans": ["plan", "product", "products"],
    "product": ["plan", "plans", "products"],
    "products": ["plan", "plans", "product"],
    "refund": ["billing", "failure", "failures", "cancellations", "complaint", "complaints"],
    "rejection": ["reject", "rejected", "guideline", "3.1.2"],
    "trial": ["free trial", "trial-to-paid", "trial paid"],
    "weekly": ["week", "7-day"],
}


def load_sources(path: Path = SOURCES) -> list[dict[str, Any]]:
    data = json.loads(path.read_text())
    return list(data.get("benchmarks", []))


def normalize_entry(entry: dict[str, Any]) -> dict[str, Any]:
    return {field: entry.get(field) for field in OUTPUT_FIELDS}


def expand_terms(query: str) -> list[str]:
    raw_terms = [term.lower() for term in query.replace("-", " ").split() if term.strip()]
    terms: list[str] = []
    for term in raw_terms:
        terms.append(term)
        terms.extend(ALIASES.get(term, []))
    if len(raw_terms) > 1:
        terms.append(" ".join(raw_terms))
    return list(dict.fromkeys(terms))


def score_entry(entry: dict[str, Any], terms: list[str]) -> int:
    score = 0
    for field, weight in FIELD_WEIGHTS.items():
        value = entry.get(field, "")
        if isinstance(value, list):
            haystack = " ".join(str(item) for item in value).lower()
        else:
            haystack = str(value).lower()
        for term in terms:
            if term in haystack:
                score += weight
    return score


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
        terms = expand_terms(query)
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
