#!/usr/bin/env python3
"""Resolve CTA URLs from env for Writer/GEO QA (no secrets printed by default)."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def load_dotenv_local(root: Path) -> None:
    local = root / "memory" / "site.env.local"
    if not local.is_file():
        return
    for line in local.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def resolve_cta() -> dict[str, str]:
    root = Path(__file__).resolve().parents[1]
    load_dotenv_local(root)
    catalog = (os.environ.get("CATALOG_URL") or os.environ.get("PUBLIC_SITE_URL") or "").rstrip("/")
    telegram = (os.environ.get("TELEGRAM_URL") or "").rstrip("/")
    if catalog and not catalog.startswith("http"):
        catalog = ""
    if telegram and not telegram.startswith("http"):
        telegram = ""
    return {
        "catalog_url": catalog,
        "telegram_url": telegram,
        "catalog_ok": bool(catalog),
        "telegram_ok": bool(telegram),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Excalibur BLOG CTA URL resolver")
    ap.add_argument("--json", action="store_true", help="Print JSON with URLs")
    ap.add_argument("--check", action="store_true", help="Exit 1 if CTA missing")
    args = ap.parse_args()
    data = resolve_cta()
    if args.json:
        print(json.dumps(data, ensure_ascii=False))
    else:
        print(f"CATALOG_OK={data['catalog_ok']}")
        print(f"TELEGRAM_OK={data['telegram_ok']}")
        if args.json is False:
            # Do not print raw URLs unless --json (writer/automation needs values)
            pass
    if args.json:
        pass
    elif data["catalog_ok"] and data["telegram_ok"]:
        # For writer convenience: print URLs only when both OK and --json not set? Keep safe default.
        print("Use --json to emit catalog_url/telegram_url for HTML injection.")
    if args.check and (not data["catalog_ok"] or not data["telegram_ok"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
