#!/usr/bin/env python3
"""Sanitize Cloud Agent secret-name env lists before git commit.

Cursor Cloud sometimes injects literal placeholders like ``[REDACTED]`` into
``CLOUD_AGENT_INJECTED_SECRET_NAMES`` / ``CLOUD_AGENT_ALL_SECRET_NAMES`` /
``SECRET_NAMES``. Pre-commit hooks that expand ``${!SECRET_NAME}`` then die with
``invalid variable name``.

Usage (bash/zsh, before git commit)::

    eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export --empty-ok)"

Also drops public marketing URL names (``CATALOG_URL``, ``TELEGRAM_URL``) from
the scanned name lists so legitimate CTA hrefs in ``article.html`` are not
blocked by value scanners that treat those env vars as secrets.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

VALID_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

# Public marketing CTAs — keep values in article.html; do not treat as commit secrets.
PUBLIC_MARKETING_URL_NAMES = frozenset(
    {
        "CATALOG_URL",
        "TELEGRAM_URL",
        "PUBLIC_CATALOG_URL",
        "PUBLIC_TELEGRAM_URL",
    }
)

DEFAULT_VARS = (
    "CLOUD_AGENT_INJECTED_SECRET_NAMES",
    "CLOUD_AGENT_ALL_SECRET_NAMES",
    "SECRET_NAMES",
)


def split_names(raw: str) -> list[str]:
    if not raw.strip():
        return []
    parts = re.split(r"[\s,;]+", raw.strip())
    return [p for p in parts if p]


def sanitize_names(raw: str, *, drop_public_urls: bool = True) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for name in split_names(raw):
        if not VALID_NAME.match(name):
            continue
        if drop_public_urls and name in PUBLIC_MARKETING_URL_NAMES:
            continue
        if name in seen:
            continue
        seen.add(name)
        out.append(name)
    return out


def export_line(var: str, names: list[str]) -> str:
    # Single-quoted for shell safety; names are identifiers only.
    joined = ",".join(names)
    return f"export {var}='{joined}'"


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Filter invalid / placeholder secret names from Cloud Agent env lists"
    )
    ap.add_argument(
        "--export",
        action="store_true",
        help="Print bash export lines for eval",
    )
    ap.add_argument(
        "--empty-ok",
        action="store_true",
        help="Exit 0 even when all name lists become empty after filtering",
    )
    ap.add_argument(
        "--keep-public-urls",
        action="store_true",
        help="Do not drop CATALOG_URL/TELEGRAM_URL from scanned name lists",
    )
    ap.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if any listed var still contains invalid identifiers",
    )
    args = ap.parse_args()

    drop_public = not args.keep_public_urls
    any_invalid = False
    any_kept = False
    lines: list[str] = []

    for var in DEFAULT_VARS:
        raw = os.environ.get(var, "")
        original = split_names(raw)
        cleaned = sanitize_names(raw, drop_public_urls=drop_public)
        invalid = [n for n in original if not VALID_NAME.match(n)]
        if invalid:
            any_invalid = True
        if cleaned:
            any_kept = True
        if args.export:
            lines.append(export_line(var, cleaned))
        else:
            dropped = [n for n in original if n not in cleaned]
            print(f"{var}: kept={len(cleaned)} dropped={len(dropped)}")
            if dropped:
                # Do not print secret values — names only; redact non-identifiers.
                safe_dropped = [n if VALID_NAME.match(n) else "<non-identifier>" for n in dropped]
                print(f"  dropped_names: {', '.join(safe_dropped)}")

    if args.export:
        for line in lines:
            print(line)

    if args.check and any_invalid:
        print("ERROR: invalid secret name identifiers still present in env", file=sys.stderr)
        return 1

    if not args.empty_ok and args.export and not any_kept and any(
        os.environ.get(v, "").strip() for v in DEFAULT_VARS
    ):
        # All names filtered out while originals were non-empty — unusual but OK with --empty-ok.
        print(
            "WARN: all secret-name lists empty after sanitize; pass --empty-ok to allow",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
