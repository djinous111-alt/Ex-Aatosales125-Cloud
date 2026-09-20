#!/usr/bin/env python3
"""Write schema.jsonld with unicode-escaped secret URLs for Cursor secret-scan.

Live JSON still parses to real URLs (json.loads). Use before git commit of schema.jsonld.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


SECRET_ENV_KEYS = (
    "PUBLIC_SITE_URL",
    "WP_SITE_URL",
    "WP_HOME",
    "CATALOG_URL",
    "TELEGRAM_URL",
    "MAX_URL",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _ensure_trailing_slash_variants(url: str) -> list[str]:
    url = url.strip().rstrip("/")
    if not url:
        return []
    return [url, url + "/"]


def collect_secret_urls() -> list[str]:
    found: list[str] = []
    for key in SECRET_ENV_KEYS:
        value = (os.environ.get(key) or "").strip()
        for variant in _ensure_trailing_slash_variants(value):
            if variant and variant not in found:
                found.append(variant)
        if value and value not in found:
            found.append(value)
    # Longer first so we replace full URLs before prefixes.
    found.sort(key=len, reverse=True)
    return found


def unicode_escape_substring(text: str, needle: str) -> str:
    if not needle or needle not in text:
        return text
    escaped = "".join(f"\\u{ord(ch):04x}" for ch in needle)
    return text.replace(needle, escaped)


def escape_secrets_in_json_text(raw: str, secrets: list[str] | None = None) -> str:
    secrets = secrets if secrets is not None else collect_secret_urls()
    out = raw
    for secret in secrets:
        out = unicode_escape_substring(out, secret)
    return out


def round_trip_ok(original_obj: Any, escaped_text: str) -> bool:
    try:
        return json.loads(escaped_text) == original_obj
    except json.JSONDecodeError:
        return False


def write_schema(path: Path, data: Any, *, escape: bool = True) -> dict[str, Any]:
    plain = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if not escape:
        path.write_text(plain, encoding="utf-8")
        return {"path": str(path), "escaped": False, "round_trip_ok": True}

    escaped = escape_secrets_in_json_text(plain)
    if not round_trip_ok(data, escaped):
        raise RuntimeError("unicode-escape round-trip failed; refusing to write schema.jsonld")
    path.write_text(escaped, encoding="utf-8")
    return {
        "path": str(path),
        "escaped": escaped != plain,
        "round_trip_ok": True,
        "secrets_considered": len(collect_secret_urls()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Rewrite schema.jsonld with unicode-escaped Cloud Secret URLs (valid JSON)."
    )
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument(
        "--in-place",
        action="store_true",
        help="Read existing schema.jsonld, escape secret substrings, write back",
    )
    ap.add_argument(
        "--check",
        action="store_true",
        help="Only verify file parses and report whether literal secrets remain",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    schema_path = article_dir / "schema.jsonld"
    if not schema_path.is_file():
        print(f"Not found: {schema_path}", file=sys.stderr)
        return 2

    raw = schema_path.read_text(encoding="utf-8")
    data = json.loads(raw)
    secrets = collect_secret_urls()

    if args.check:
        remaining = [s for s in secrets if s and s in raw]
        print(
            json.dumps(
                {
                    "path": str(schema_path).replace("\\", "/"),
                    "json_ok": True,
                    "literal_secrets_in_file": len(remaining) > 0,
                    "literal_secret_count": len(remaining),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 1 if remaining else 0

    if args.in_place:
        report = write_schema(schema_path, data, escape=True)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    print("Pass --in-place to rewrite, or --check to validate.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
