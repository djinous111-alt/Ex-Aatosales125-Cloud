#!/usr/bin/env python3
"""Build or validate shared/wp-slug-denylist.json from WordPress REST (public)."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def public_base_from_env(root: Path) -> str:
    env_path = root / "memory/site.env.local"
    if env_path.is_file():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("PUBLIC_SITE_URL=") or line.startswith("WP_SITE_URL=") or line.startswith("WP_HOME="):
                value = line.split("=", 1)[1].strip().rstrip("/")
                if value:
                    return value
    for key in ("PUBLIC_SITE_URL", "WP_SITE_URL", "WP_HOME"):
        value = (os.environ.get(key) or "").strip().rstrip("/")
        if value:
            return value
    return ""


def fetch_json(url: str) -> list | dict:
    req = urllib.request.Request(url, headers={"User-Agent": "excalibur-blog-denylist/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def collect_slugs(base: str, resource: str) -> list[str]:
    slugs: list[str] = []
    page = 1
    while True:
        url = (
            f"{base.rstrip('/')}/wp-json/wp/v2/{resource}"
            f"?per_page=100&page={page}&_fields=slug,status"
        )
        try:
            data = fetch_json(url)
        except urllib.error.HTTPError as exc:
            if exc.code == 400 and page > 1:
                break
            raise
        if not isinstance(data, list) or not data:
            break
        for item in data:
            slug = str(item.get("slug") or "").strip()
            if slug:
                slugs.append(slug)
        if len(data) < 100:
            break
        page += 1
    return slugs


def validate_denylist(path: Path) -> dict:
    if not path.is_file():
        return {"ok": False, "error": "missing", "path": str(path)}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"ok": False, "error": f"invalid_json:{exc}", "path": str(path)}
    slugs = data.get("slugs")
    if not isinstance(slugs, list) or not slugs:
        return {"ok": False, "error": "empty_slugs", "path": str(path)}
    return {
        "ok": True,
        "path": str(path),
        "count": len(slugs),
        "generated_at": data.get("generated_at"),
        "source": data.get("source"),
    }


def rebuild(path: Path, base: str) -> dict:
    post_slugs = collect_slugs(base, "posts")
    page_slugs = collect_slugs(base, "pages")
    unique = sorted(set(post_slugs) | set(page_slugs))
    payload = {
        "generated_at": date.today().isoformat(),
        "source": "wp-rest-posts-pages",
        "posts_count": len(set(post_slugs)),
        "pages_count": len(set(page_slugs)),
        "slugs": unique,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "ok": True,
        "path": str(path),
        "posts_count": payload["posts_count"],
        "pages_count": payload["pages_count"],
        "unique_slugs": len(unique),
        # Do not echo PUBLIC_SITE_URL / host into stdout (secrets scanner).
        "base_configured": bool(base),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate or rebuild WP slug denylist")
    ap.add_argument("--check", action="store_true", help="Validate existing denylist JSON")
    ap.add_argument("--rebuild", action="store_true", help="Rebuild denylist from WP REST")
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path (default: shared/wp-slug-denylist.json)",
    )
    ap.add_argument(
        "--site-base",
        type=str,
        default="",
        help="Public site origin (default: PUBLIC_SITE_URL / WP_* from env)",
    )
    args = ap.parse_args()
    root = project_root()
    out = args.out or (root / "shared/wp-slug-denylist.json")
    if not out.is_absolute():
        out = root / out

    if args.check and not args.rebuild:
        report = validate_denylist(out)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report.get("ok") else 1

    if args.rebuild:
        base = (args.site_base or public_base_from_env(root)).strip().rstrip("/")
        if not base:
            print(
                json.dumps(
                    {
                        "ok": False,
                        "error": "PUBLIC_SITE_URL/WP_SITE_URL/WP_HOME required for --rebuild",
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 2
        report = rebuild(out, base)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report.get("ok") else 1

    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
