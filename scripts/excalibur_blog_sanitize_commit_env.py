#!/usr/bin/env python3
"""Sanitize Cloud Agent commit env for secret-scan pre-commit hooks.

Cloud may inject non-identifiers (raw URLs) into CLOUD_AGENT_INJECTED_SECRET_NAMES.
Hooks that expand `${!SECRET_NAME}` then abort with `invalid variable name`.

Also supports excluding public brand URL secret names when committing artifacts
that must embed them (schema.jsonld / authors-registry sameAs).

Usage:
  eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export --empty-ok)"
  EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS=1 \\
    eval "$(python3 scripts/excalibur_blog_sanitize_commit_env.py --export --empty-ok)"
"""
from __future__ import annotations

import argparse
import os
import re
import sys

VALID_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

PUBLIC_URL_SECRET_NAMES = frozenset(
    {
        "PUBLIC_SITE_URL",
        "WP_HOME",
        "WP_SITE_URL",
        "CATALOG_URL",
        "TELEGRAM_URL",
        "MAX_URL",
        "SITE_URL",
    }
)


def _truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "yes", "true", "on"}


def split_names(raw: str) -> list[str]:
    normalized = raw.replace(",", " ")
    return [part for part in normalized.split() if part]


def sanitize_names(
    raw: str,
    *,
    exclude_public_urls: bool = False,
) -> list[str]:
    kept: list[str] = []
    for name in split_names(raw):
        if not VALID_IDENT.match(name):
            continue
        if exclude_public_urls and name in PUBLIC_URL_SECRET_NAMES:
            continue
        kept.append(name)
    # de-dupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for name in kept:
        if name not in seen:
            seen.add(name)
            out.append(name)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Sanitize CLOUD_AGENT_INJECTED_SECRET_NAMES for git commit")
    ap.add_argument(
        "--export",
        action="store_true",
        help="Print bash export lines suitable for eval",
    )
    ap.add_argument(
        "--empty-ok",
        action="store_true",
        help="Allow empty result (unset the variable) instead of exiting non-zero",
    )
    ap.add_argument(
        "--exclude-public-url-secrets",
        action="store_true",
        help="Drop PUBLIC_SITE_URL/TELEGRAM_URL/CATALOG_URL/MAX_URL from the scan list",
    )
    args = ap.parse_args()

    raw = os.environ.get("CLOUD_AGENT_INJECTED_SECRET_NAMES", "")
    exclude = args.exclude_public_url_secrets or _truthy(
        os.environ.get("EXCALIBUR_EXCLUDE_PUBLIC_URL_SECRETS")
    )
    cleaned = sanitize_names(raw, exclude_public_urls=exclude)

    if args.export:
        if cleaned:
            # Comma-separated — matches Cloud pre-commit IFS=','
            joined = ",".join(cleaned)
            # Escape for single-quoted bash string
            safe = joined.replace("'", "'\"'\"'")
            print(f"export CLOUD_AGENT_INJECTED_SECRET_NAMES='{safe}'")
        else:
            print("unset CLOUD_AGENT_INJECTED_SECRET_NAMES || true")
        return 0

    if not cleaned and raw and not args.empty_ok:
        print("ERROR: no valid secret names remain after sanitize", file=sys.stderr)
        return 1

    print(",".join(cleaned))
    return 0


if __name__ == "__main__":
    sys.exit(main())
