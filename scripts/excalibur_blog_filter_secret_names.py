#!/usr/bin/env python3
"""Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.

Cursor Cloud pre-commit expands `${!SECRET_NAME}`. A URL-like or otherwise
non-identifier token in CLOUD_AGENT_INJECTED_SECRET_NAMES aborts the hook with
`invalid variable name` before scanning. This helper drops bad tokens.

Usage:
  eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"
  python3 scripts/excalibur_blog_filter_secret_names.py --print
"""
from __future__ import annotations

import argparse
import os
import re
import sys

IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def filter_names(raw: str) -> list[str]:
    # pre-commit.cursor splits on commas: IFS=',' read -ra SECRET_NAMES
    parts = re.split(r"[\s,]+", raw.strip()) if raw.strip() else []
    return [p for p in parts if p and IDENT_RE.match(p)]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--export", action="store_true", help="Print export statement for eval")
    ap.add_argument("--print", action="store_true", help="Print filtered names one per line")
    args = ap.parse_args()
    raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
    filtered = filter_names(raw)
    dropped = sorted(set(re.split(r"[\s,]+", raw.strip()) if raw.strip() else []) - set(filtered) - {""})
    if args.export:
        # Comma-separated — matches pre-commit.cursor IFS=',' parsing.
        # Empty value → hook early-exit (no scan).
        print(f'export CLOUD_AGENT_INJECTED_SECRET_NAMES="{",".join(filtered)}"')
        if dropped:
            print(
                f"# dropped non-identifier secret name tokens: {', '.join(dropped)}",
                file=sys.stderr,
            )
        return 0
    if args.print or not args.export:
        for name in filtered:
            print(name)
        if dropped:
            print(f"# dropped: {', '.join(dropped)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
