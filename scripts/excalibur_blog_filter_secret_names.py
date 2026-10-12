#!/usr/bin/env python3
"""Filter CLOUD_AGENT_*_SECRET_NAMES to valid bash identifiers.

Cloud sometimes injects raw URL values into secret-name lists; bash `${!name}`
then crashes pre-commit with "invalid variable name".

Usage:
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(python3 scripts/excalibur_blog_filter_secret_names.py)"
  eval "$(python3 scripts/excalibur_blog_filter_secret_names.py --export)"
"""
from __future__ import annotations

import argparse
import os
import re
import sys

IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def filter_names(raw: str) -> str:
    kept: list[str] = []
    for token in re.split(r"[\s,]+", raw or ""):
        name = token.strip()
        if name and IDENT_RE.match(name):
            kept.append(name)
    return ",".join(kept)


def main() -> int:
    ap = argparse.ArgumentParser(description="Sanitize Cloud secret-name env lists")
    ap.add_argument(
        "--export",
        action="store_true",
        help="Print export statements for CLOUD_AGENT_*_SECRET_NAMES",
    )
    ap.add_argument(
        "--env",
        default="CLOUD_AGENT_INJECTED_SECRET_NAMES",
        help="Env var to filter when not using --export (default: INJECTED)",
    )
    args = ap.parse_args()

    if args.export:
        injected = filter_names(os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", ""))
        all_names = filter_names(os.environ.get("CLOUD_AGENT_ALL_SECRET_NAMES", ""))
        # Safe for eval: values are comma-separated identifiers only.
        print(f'export CLOUD_AGENT_INJECTED_SECRET_NAMES="{injected}"')
        print(f'export CLOUD_AGENT_ALL_SECRET_NAMES="{all_names}"')
        return 0

    filtered = filter_names(os.environ.get(args.env, ""))
    sys.stdout.write(filtered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
