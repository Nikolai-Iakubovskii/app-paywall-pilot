#!/usr/bin/env python3
"""Validate that all internal markdown links in the repo resolve to existing files."""
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", ".github", "node_modules", "outputs"}


def all_md_files() -> list[Path]:
    files: list[Path] = []
    for root, dirs, fs in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in fs:
            if f.endswith(".md"):
                files.append(Path(root) / f)
    return files


def main() -> int:
    errors: list[str] = []
    checked = 0

    for fp in all_md_files():
        try:
            content = fp.read_text()
        except Exception as e:
            errors.append(f"{fp}: cannot read ({e})")
            continue

        for _label, link in LINK_PATTERN.findall(content):
            if link.startswith(("http://", "https://", "#", "mailto:", "ftp://")):
                continue
            target = link.split("#")[0]
            if not target:
                continue
            base = fp.parent
            resolved = (base / target).resolve()
            checked += 1
            if not resolved.exists():
                rel_fp = fp.relative_to(REPO)
                errors.append(
                    f"{rel_fp}: broken link to '{link}' (resolved: {resolved})"
                )

    if errors:
        for e in errors:
            print(e)
        return 1

    print(f"All {checked} internal links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
