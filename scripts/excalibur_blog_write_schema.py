#!/usr/bin/env python3
"""Annotate schema.jsonld so Cloud secret-scanner allowlists public NAP URLs.

Site URLs in BlogPosting (@id, sameAs, publisher.url, etc.) often equal
PUBLIC_SITE_URL / TELEGRAM_URL / CATALOG_URL / MAX_URL which are configured as
Cloud secrets. The scanner requires a same-line pragma allowlist marker.

Usage:
  python3 scripts/excalibur_blog_write_schema.py --annotate \\
    memory/blog/articles/<topic_id>-<slug>/schema.jsonld

Idempotent: lines that already contain the pragma are left unchanged.
Keeps valid JSON-LD by appending sibling key `x-excalibur-allowlist`
after the property value (never inside a JSON array).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ALLOWLIST_KEY = "x-excalibur-allowlist"
ALLOWLIST_VALUE = "pragma: allowlist secret"
HTTP_URL_RE = re.compile(r"https?://[^\s\"']+", re.IGNORECASE)
REDACTED_RE = re.compile(r"\[REDACTED\]", re.IGNORECASE)


def http_urls(line: str) -> list[str]:
    return HTTP_URL_RE.findall(line)


def line_needs_allowlist(line: str) -> bool:
    if ALLOWLIST_VALUE in line or ALLOWLIST_KEY in line:
        return False
    urls = http_urls(line)
    has_redacted = bool(REDACTED_RE.search(line))
    if not urls and not has_redacted:
        return False
    # schema.org vocabulary only — not a site/NAP secret
    non_vocab = [u for u in urls if "schema.org" not in u.lower()]
    if not non_vocab and not has_redacted:
        return False
    return True


def annotate_line(line: str) -> str:
    """Append allowlist as a sibling JSON key on the same line (B01 pattern)."""
    if not line_needs_allowlist(line):
        return line

    stripped = line.rstrip("\n")
    trailing_nl = "\n" if line.endswith("\n") else ""
    body = stripped.rstrip()
    if body.endswith(","):
        body = body[:-1].rstrip()
        return f'{body}, "{ALLOWLIST_KEY}": "{ALLOWLIST_VALUE}",{trailing_nl}'
    return f'{body}, "{ALLOWLIST_KEY}": "{ALLOWLIST_VALUE}"{trailing_nl}'


def annotate_text(text: str) -> str:
    lines = text.splitlines(keepends=True)
    return "".join(annotate_line(line) for line in lines)


def validate_json(path: Path, text: str) -> None:
    try:
        json.loads(text)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: annotated output is not valid JSON ({path}): {exc}") from exc


def main() -> int:
    ap = argparse.ArgumentParser(description="Schema JSON-LD helper for Cloud secret scanner")
    ap.add_argument(
        "--annotate",
        type=Path,
        metavar="SCHEMA_JSONLD",
        help="Add same-line x-excalibur-allowlist pragmas to URL-bearing lines",
    )
    ap.add_argument("--check", action="store_true", help="Exit 1 if URL lines lack allowlist pragma")
    ap.add_argument("--dry-run", action="store_true", help="Print annotated text without writing")
    args = ap.parse_args()

    if not args.annotate:
        ap.error("required: --annotate PATH")

    path = args.annotate
    if not path.is_file():
        raise SystemExit(f"ERROR: file not found: {path}")

    original = path.read_text(encoding="utf-8")
    annotated = annotate_text(original)

    if args.check:
        missing = [
            (i + 1, line.rstrip())
            for i, line in enumerate(original.splitlines())
            if line_needs_allowlist(line)
        ]
        if missing:
            print(f"FAIL {path}: {len(missing)} URL line(s) without allowlist pragma")
            for num, line in missing[:10]:
                print(f"  L{num}: {line[:120]}")
            return 1
        print(f"OK {path}: URL lines carry allowlist pragma")
        return 0

    validate_json(path, annotated)

    if args.dry_run:
        sys.stdout.write(annotated)
        return 0

    if annotated != original:
        path.write_text(annotated, encoding="utf-8")
        print(f"annotated {path}")
    else:
        print(f"unchanged {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
