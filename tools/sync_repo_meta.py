#!/usr/bin/env python3
"""Sync small metadata-driven blocks in top-level docs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
META = json.loads((REPO / "framework-meta.json").read_text())
BLOCK_PATTERN = re.compile(
    r"<!-- meta:block (?P<name>[a-z0-9_]+) -->\n(?P<body>.*?)\n<!-- /meta:block -->",
    re.DOTALL,
)


def render_block(name: str) -> str:
    version = META["version"]
    source_count = META["source_count"]
    module_count = META["module_count"]
    academic_count = META["academic_concept_count"]
    flagship = META["flagship_domain"]
    canonical_brief = META["canonical_research_brief"]
    legacy_brief = META["legacy_research_briefs"][0]

    blocks = {
        "readme_hero": (
            f"<sub>AI skill + knowledge base + executable tool. For iOS + Android. "
            f"Built on {source_count} sourced 2026 benchmarks (Adapty 16K apps · "
            "RevenueCat 115K apps · AppsFlyer 1.7B installs · Superwall 32M paywall views) "
            f"and a {academic_count}-concept academic foundation (Kahneman + Layer 2). "
            f"Flagship domain is **{flagship}**; expansion to Onboarding / Retention / Growth / "
            "Pricing on the [roadmap](ROADMAP.md).</sub>\n\n"
            "<br>\n\n"
            f"[![Version](https://img.shields.io/badge/Version-{version}-brightgreen?style=for-the-badge)]"
            "(https://github.com/Nikolai-Iakubovskii/app-paywall-pilot/releases)\n"
            "[![Platform](https://img.shields.io/badge/Platform-iOS_%7C_Android-blue?style=for-the-badge)](#)\n"
            f"[![Framework](https://img.shields.io/badge/Framework-{flagship}-black?style=for-the-badge)](ROADMAP.md)\n"
            f"[![Modules](https://img.shields.io/badge/Modules-{module_count}-purple?style=for-the-badge)](modules/)\n"
            f"[![Sources](https://img.shields.io/badge/Sources-{source_count}-orange?style=for-the-badge)](sources.json)\n"
            f"[![Academic](https://img.shields.io/badge/Academic-{academic_count}_concepts-darkblue?style=for-the-badge)]"
            "(modules/pricing-psychology.md)\n"
            "[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)"
        ),
        "readme_research_outputs": (
            f"- [{canonical_brief}]({canonical_brief}) -- canonical research brief with current methodology, "
            "sample sizes, and evidence class for every benchmark used\n"
            f"- [{legacy_brief}]({legacy_brief}) -- legacy v1 research brief retained for historical references and changelog continuity\n"
            f"- [{canonical_brief.replace('.md', '.provenance.md')}]({canonical_brief.replace('.md', '.provenance.md')}) "
            "-- provenance ledger: sources consulted vs accepted vs rejected, cross-references, weak-signal flags"
        ),
        "roadmap_header": (
            f"**Version:** {version} (framework)\n"
            f"**Last updated:** {META['last_updated']}"
        ),
    }

    if name not in blocks:
        raise KeyError(f"Unknown metadata block '{name}'")
    return blocks[name]


def sync_file(path: Path, *, check: bool) -> bool:
    original = path.read_text()
    changed = False

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        name = match.group("name")
        rendered = render_block(name)
        if match.group("body") != rendered:
            changed = True
        return f"<!-- meta:block {name} -->\n{rendered}\n<!-- /meta:block -->"

    updated = BLOCK_PATTERN.sub(replace, original)

    if check:
        if changed:
            print(f"{path.relative_to(REPO)} is out of sync with framework-meta.json")
        return not changed

    if updated != original:
        path.write_text(updated)
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Sync metadata-driven doc blocks")
    parser.add_argument("--check", action="store_true", help="Fail if docs are out of sync")
    args = parser.parse_args(argv)

    targets = [REPO / "README.md", REPO / "ROADMAP.md"]
    ok = all(sync_file(path, check=args.check) for path in targets)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
