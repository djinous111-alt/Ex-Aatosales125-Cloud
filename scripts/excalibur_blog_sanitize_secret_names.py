#!/usr/bin/env python3
"""Sanitize CLOUD_AGENT_*_SECRET_NAMES to comma-separated bash identifiers.

Cloud sometimes injects a URL into the secret-*names* list. Cursor pre-commit
then does `${!SECRET_NAME}` and fails with `invalid variable name`.

Usage:
  python3 scripts/excalibur_blog_sanitize_secret_names.py --check
  python3 scripts/excalibur_blog_sanitize_secret_names.py --print-export
  eval "$(python3 scripts/excalibur_blog_sanitize_secret_names.py --print-export)"
"""

from __future__ import annotations

import argparse
import os
import re
import sys

BASH_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
ENV_KEYS = (
    "CLOUD_AGENT_INJECTED_SECRET_NAMES",
    "CLOUD_AGENT_ALL_SECRET_NAMES",
)


def split_names(raw: str) -> list[str]:
    if not raw:
        return []
    # Prefer comma; also split on whitespace for broken space-separated lists.
    parts: list[str] = []
    for chunk in raw.replace("\n", ",").split(","):
        for tok in chunk.split():
            tok = tok.strip()
            if tok:
                parts.append(tok)
    return parts


def sanitize_list(raw: str) -> tuple[str, list[str]]:
    kept: list[str] = []
    dropped: list[str] = []
    for tok in split_names(raw):
        if BASH_IDENT.match(tok):
            kept.append(tok)
        else:
            dropped.append(tok)
    return ",".join(kept), dropped


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanitize Cloud secret-name env lists")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if any non-identifier tokens are present (doctor/preflight)",
    )
    parser.add_argument(
        "--print-export",
        action="store_true",
        help="Print bash export lines with sanitized lists",
    )
    args = parser.parse_args()

    dirty = False
    for key in ENV_KEYS:
        raw = os.environ.get(key, "")
        cleaned, dropped = sanitize_list(raw)
        if dropped:
            dirty = True
            preview = ", ".join(t[:48] for t in dropped[:5])
            print(
                f"WARN {key}: dropped {len(dropped)} non-identifier token(s): {preview}",
                file=sys.stderr,
            )
        if args.print_export:
            # Safe for eval: values are comma-separated identifiers only.
            print(f'export {key}="{cleaned}"')
        elif args.check:
            status = "dirty" if dropped else "ok"
            print(f"{key}: {status} kept={len(split_names(cleaned))} dropped={len(dropped)}")
        else:
            print(f"{key}={cleaned}")

    if args.check and dirty:
        print(
            "FAIL: sanitize CLOUD_AGENT_*_SECRET_NAMES before git commit "
            "(source scripts/sanitize_cloud_secret_names.sh or "
            "bash scripts/excalibur_git.sh commit ...)",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
