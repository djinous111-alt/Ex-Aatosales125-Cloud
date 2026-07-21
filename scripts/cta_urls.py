#!/usr/bin/env python3
"""Resolve Writer CTA URLs from env (never print secrets to handoff/logs beyond needed hrefs).

Usage:
  python3 scripts/cta_urls.py
  python3 scripts/cta_urls.py --json

Writer must inject live CATALOG_URL / TELEGRAM_URL into article.html CTA anchors.
If Cursor secret-scan blocks the commit, keep live hrefs and add an HTML comment
immediately after the CTA paragraph:

  <!-- pragma: allowlist secret -->

Do not replace live hrefs with the literal string [REDACTED] in body HTML.
"""
from __future__ import annotations

import argparse
import json
import os
import sys


def resolve() -> dict[str, str]:
    catalog = (os.environ.get("CATALOG_URL") or os.environ.get("EXCALIBUR_CATALOG_URL") or "").strip()
    telegram = (os.environ.get("TELEGRAM_URL") or os.environ.get("EXCALIBUR_TELEGRAM_URL") or "").strip()
    return {
        "catalog_url": catalog,
        "telegram_url": telegram,
        "ready": bool(catalog and telegram),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Resolve CTA URLs for Excalibur BLOG Writer")
    ap.add_argument("--json", action="store_true", help="Print JSON only")
    args = ap.parse_args()
    data = resolve()
    if args.json:
        print(json.dumps(data, ensure_ascii=False))
    else:
        print(f"CATALOG_URL_SET={'yes' if data['catalog_url'] else 'no'}")
        print(f"TELEGRAM_URL_SET={'yes' if data['telegram_url'] else 'no'}")
        print(f"CTA_READY={'yes' if data['ready'] else 'no'}")
        if data["catalog_url"]:
            print(f"CATALOG_URL={data['catalog_url']}")
        if data["telegram_url"]:
            print(f"TELEGRAM_URL={data['telegram_url']}")
    return 0 if data["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
