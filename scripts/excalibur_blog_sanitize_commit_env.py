#!/usr/bin/env python3
"""Sanitize CLOUD_AGENT_INJECTED_SECRET_NAMES for bash pre-commit hooks.

Cloud redaction may inject the literal `[REDACTED]` (or other non-identifiers)
into CLOUD_AGENT_INJECTED_SECRET_NAMES. Pre-commit then crashes on
`${!SECRET_NAME}` with `invalid variable name`.

Usage (before git commit in redacted Cloud sandbox):

  eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export)"
  git commit ...

Or print filtered CSV only:

  python3 scripts/excalibur_blog_sanitize_commit_env.py
"""
from __future__ import annotations

import argparse
import os
import re
import sys

# Bash name: start with letter/underscore, then alnum/underscore.
_BASH_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def filter_secret_names(raw: str) -> list[str]:
    names: list[str] = []
    for part in (raw or "").replace(";", ",").split(","):
        name = part.strip()
        if not name:
            continue
        if _BASH_IDENT.fullmatch(name):
            names.append(name)
    return names


def main() -> int:
    ap = argparse.ArgumentParser(description="Filter invalid bash identifiers from Cloud secret-name env")
    ap.add_argument(
        "--export",
        action="store_true",
        help="Print `export CLOUD_AGENT_INJECTED_SECRET_NAMES=...` for eval",
    )
    ap.add_argument(
        "--empty-ok",
        action="store_true",
        help="If all names are invalid, export empty string (Cloud redacted sandbox workaround)",
    )
    args = ap.parse_args()

    raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
    filtered = filter_secret_names(raw)
    dropped = [
        p.strip()
        for p in (raw or "").replace(";", ",").split(",")
        if p.strip() and p.strip() not in filtered
    ]

    if dropped:
        print(
            f"# dropped non-bash secret name(s): {', '.join(dropped)}",
            file=sys.stderr,
        )

    value = ",".join(filtered)
    if not filtered and raw.strip() and args.empty_ok:
        value = ""

    if args.export:
        # Safe for eval: only filtered bash identifiers or empty.
        print(f'export CLOUD_AGENT_INJECTED_SECRET_NAMES="{value}"')
    else:
        print(value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
