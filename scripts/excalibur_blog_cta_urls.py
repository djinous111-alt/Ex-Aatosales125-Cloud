#!/usr/bin/env python3
"""Reinject or re-redact CTA URLs in article.html before link-verify / publish.

Writer often leaves href="[REDACTED]" placeholders for catalog/Telegram CTAs.
GEO QA and Publish must reinject live URLs from env (never commit live secrets).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

PLACEHOLDER = "[REDACTED]"
DEFAULT_CATALOG_KEYS = ("CATALOG_URL", "PUBLIC_CATALOG_URL", "SITE_CATALOG_URL")
DEFAULT_TELEGRAM_KEYS = ("TELEGRAM_URL", "PUBLIC_TELEGRAM_URL", "TG_URL")


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def first_env(*keys: str) -> str:
    for key in keys:
        value = os.environ.get(key, "").strip()
        if value:
            return value
    return ""


def resolve_article_html(article_dir: Path) -> Path:
    html = article_dir / "article.html"
    if not html.is_file():
        raise FileNotFoundError(f"article.html not found in {article_dir}")
    return html


def reinject(html: str, catalog_url: str, telegram_url: str) -> tuple[str, dict[str, int]]:
    stats = {"catalog": 0, "telegram": 0, "placeholders_left": 0}
    if not catalog_url and not telegram_url:
        raise RuntimeError(
            "CTA reinject needs CATALOG_URL and/or TELEGRAM_URL (or PUBLIC_* aliases) in env"
        )

    def replace_href(match: re.Match[str]) -> str:
        full = match.group(0)
        ctx_before = match.string[max(0, match.start() - 180) : match.start()].lower()
        ctx_after = match.string[match.end() : match.end() + 180].lower()
        blob = ctx_before + " " + ctx_after
        is_tg = any(
            token in blob
            for token in ("telegram", "t.me/", "@avtosales", "телеграм", "tg://")
        )
        is_catalog = any(
            token in blob
            for token in ("каталог", "catalog", "avto-sales", "подобрать", "подбор")
        )
        if is_tg and telegram_url:
            stats["telegram"] += 1
            return full.replace(PLACEHOLDER, telegram_url, 1)
        if (is_catalog or not is_tg) and catalog_url:
            stats["catalog"] += 1
            return full.replace(PLACEHOLDER, catalog_url, 1)
        if telegram_url and not catalog_url:
            stats["telegram"] += 1
            return full.replace(PLACEHOLDER, telegram_url, 1)
        return full

    pattern = re.compile(
        rf'href\s*=\s*([\'"]){re.escape(PLACEHOLDER)}\1',
        flags=re.I,
    )
    out = pattern.sub(replace_href, html)
    stats["placeholders_left"] = out.lower().count(f'href="{PLACEHOLDER.lower()}"') + out.lower().count(
        f"href='{PLACEHOLDER.lower()}'"
    )
    return out, stats


def redact(html: str, catalog_url: str, telegram_url: str) -> tuple[str, int]:
    count = 0
    out = html
    for url in (catalog_url, telegram_url):
        if not url:
            continue
        if url in out:
            occurrences = out.count(url)
            out = out.replace(url, PLACEHOLDER)
            count += occurrences
    return out, count


def main() -> int:
    ap = argparse.ArgumentParser(description="Reinject or redact CTA URLs in article.html")
    ap.add_argument("--article-dir", required=True, help="Article directory with article.html")
    ap.add_argument(
        "--mode",
        choices=("reinject", "redact"),
        default="reinject",
        help="reinject live URLs from env, or redact them back to [REDACTED]",
    )
    ap.add_argument("--dry-run", action="store_true", help="Print stats without writing")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    html_path = resolve_article_html(article_dir)
    original = html_path.read_text(encoding="utf-8")
    catalog_url = first_env(*DEFAULT_CATALOG_KEYS)
    telegram_url = first_env(*DEFAULT_TELEGRAM_KEYS)

    if args.mode == "reinject":
        updated, stats = reinject(original, catalog_url, telegram_url)
        print(
            "OK mode=reinject "
            f"catalog={stats['catalog']} telegram={stats['telegram']} "
            f"placeholders_left={stats['placeholders_left']}"
        )
        if stats["placeholders_left"] > 0:
            print(
                "WARN some href=[REDACTED] remain; check surrounding CTA context or env URLs",
                file=sys.stderr,
            )
    else:
        updated, count = redact(original, catalog_url, telegram_url)
        print(f"OK mode=redact replaced={count}")

    if not args.dry_run and updated != original:
        html_path.write_text(updated, encoding="utf-8")
        print(f"OK wrote={html_path}")
    elif args.dry_run:
        print("OK dry-run (no write)")
    else:
        print("OK no changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
