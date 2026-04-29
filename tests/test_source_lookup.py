from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from tools.source_lookup import lookup_sources


class SourceLookupTests(unittest.TestCase):
    def test_lookup_by_id_returns_required_fields(self) -> None:
        results = lookup_sources(source_id="trial-paid-global-25-6-27-8")

        self.assertEqual(len(results), 1)
        entry = results[0]
        for field in ("id", "claim", "evidence_class", "source", "date", "url", "scope"):
            self.assertIn(field, entry)
            self.assertTrue(entry[field])

    def test_query_ranks_matching_claim(self) -> None:
        results = lookup_sources(query="trial paid global", limit=3)

        ids = [entry["id"] for entry in results]
        self.assertIn("trial-paid-global-25-6-27-8", ids)

    def test_alias_query_finds_refund_related_source(self) -> None:
        results = lookup_sources(query="refund rate annual", limit=3)

        ids = [entry["id"] for entry in results]
        self.assertIn("google-play-involuntary-billing-failures-31-of-cancellations-vs-app-stor", ids)

    def test_alias_query_finds_toggle_rejection_source(self) -> None:
        results = lookup_sources(query="toggle rejection", limit=3)

        ids = [entry["id"] for entry in results]
        self.assertIn("toggle-paywall-rejections-started-mid-january-2026", ids)

    def test_cli_outputs_json(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(REPO / "tools/source_lookup.py"),
                "--id",
                "trial-paid-global-25-6-27-8",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        payload = json.loads(result.stdout)
        self.assertEqual(payload[0]["id"], "trial-paid-global-25-6-27-8")
        self.assertEqual(payload[0]["evidence_class"], "large_scale_report")


if __name__ == "__main__":
    unittest.main()
