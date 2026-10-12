#!/usr/bin/env python3
"""Normalize CLOUD_AGENT_INJECTED_SECRET_NAMES for pre-commit secret scanners.

Cursor Cloud may inject space-separated names and/or URL-shaped junk that is not a
valid bash identifier. Hooks that split on commas and expand ${!NAME} then die.

Usage:
  eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"
  # or print comma-separated names only:
  python3 scripts/excalibur_blog_filter_secret_names.py
"""
from __future__ import annotations

import argparse
import os
import re
import sys

VALID_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def split_raw_names(raw: str) -> list[str]:
    if not raw or not raw.strip():
        return []
    # Accept comma- and/or whitespace-separated lists.
    parts = re.split(r"[\s,]+", raw.strip())
    return [p for p in parts if p]


def filter_secret_names(raw: str | None = None) -> list[str]:
    if raw is None:
        raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
    seen: set[str] = set()
    out: list[str] = []
    for name in split_raw_names(raw):
        if not VALID_NAME.match(name):
            continue
        if name in seen:
            continue
        seen.add(name)
        out.append(name)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers"
    )
    ap.add_argument(
        "--export",
        action="store_true",
        help="Print export CLOUD_AGENT_INJECTED_SECRET_NAMES='a,b,c' for eval",
    )
    ap.add_argument(
        "--raw",
        type=str,
        default=None,
        help="Override env value (for tests)",
    )
    args = ap.parse_args()

    names = filter_secret_names(args.raw)
    joined = ",".join(names)
    if args.export:
        # Safe for eval: only filtered identifiers joined by commas.
        print(f"export CLOUD_AGENT_INJECTED_SECRET_NAMES='{joined}'")
    else:
        print(joined)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
