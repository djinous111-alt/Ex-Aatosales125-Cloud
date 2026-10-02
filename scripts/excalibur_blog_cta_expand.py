#!/usr/bin/env python3
"""Expand or re-redact CTA href placeholders for link-verify / publish / git.

Repo convention: committed article.html may keep href="[REDACTED]" for catalog/Telegram.
Before link-verify or publish, expand from env; after checks, re-redact for git.

Usage:
  python3 scripts/excalibur_blog_cta_expand.py --article-dir <dir> --mode expand
  python3 scripts/excalibur_blog_cta_expand.py --article-dir <dir> --mode redact
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


PLACEHOLDER = "[REDACTED]"


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def merged_cta_env(root: Path) -> dict[str, str]:
    env = read_env_file(root / "memory/site.env.local")
    for key in ("CATALOG_URL", "TELEGRAM_URL", "PUBLIC_SITE_URL", "MAX_URL"):
        value = os.environ.get(key)
        if value:
            env[key] = value
    return env


def expand_html(html: str, catalog: str, telegram: str) -> tuple[str, int]:
    count = 0
    if not catalog and not telegram:
        return html, 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        full = match.group(0)
        text = (match.group(1) or "").lower()
        if catalog and any(tok in text for tok in ("каталог", "catalog", "подобрать", "расчёт", "расчет")):
            count += 1
            return full.replace(f'href="{PLACEHOLDER}"', f'href="{catalog}"', 1)
        if telegram and any(tok in text for tok in ("telegram", "телеграм", "tg", "@avtosales")):
            count += 1
            return full.replace(f'href="{PLACEHOLDER}"', f'href="{telegram}"', 1)
        # Fallback: first REDACTED → catalog, second → telegram when both set.
        return full

    pattern = re.compile(
        r'<a\b[^>]*href="' + re.escape(PLACEHOLDER) + r'"[^>]*>.*?</a>',
        flags=re.I | re.S,
    )
    # Two-pass deterministic fallback when anchor text is ambiguous.
    anchors = list(pattern.finditer(html))
    if not anchors:
        return html, 0
    out = html
    # Prefer text-based replace first.
    out2, n = "", 0
    last = 0
    catalog_used = False
    telegram_used = False
    for match in pattern.finditer(html):
        out2 += html[last : match.start()]
        full = match.group(0)
        text = re.sub(r"<[^>]+>", " ", full).lower()
        href_new = None
        if catalog and any(tok in text for tok in ("каталог", "catalog", "подобрать", "расчёт", "расчет", "калькулятор")):
            href_new = catalog
            catalog_used = True
        elif telegram and any(tok in text for tok in ("telegram", "телеграм", "tg", "напиш", "связать")):
            href_new = telegram
            telegram_used = True
        elif catalog and not catalog_used:
            href_new = catalog
            catalog_used = True
        elif telegram and not telegram_used:
            href_new = telegram
            telegram_used = True
        if href_new:
            full = full.replace(f'href="{PLACEHOLDER}"', f'href="{href_new}"', 1)
            n += 1
        out2 += full
        last = match.end()
    out2 += html[last:]
    return out2, n


def redact_html(html: str, catalog: str, telegram: str) -> tuple[str, int]:
    count = 0
    out = html
    for url in (catalog, telegram):
        if not url:
            continue
        replaced = out.replace(f'href="{url}"', f'href="{PLACEHOLDER}"')
        if replaced != out:
            count += replaced.count(f'href="{PLACEHOLDER}"') - out.count(f'href="{PLACEHOLDER}"')
            out = replaced
    return out, count


def main() -> int:
    ap = argparse.ArgumentParser(description="Expand/redact CTA href placeholders")
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("--mode", choices=("expand", "redact"), required=True)
    ap.add_argument("--html", default="article.html", help="HTML file relative to article-dir")
    args = ap.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    html_path = article_dir / args.html
    if not html_path.is_file():
        print(f"ERROR: {html_path} not found", file=sys.stderr)
        return 1

    env = merged_cta_env(root)
    catalog = (env.get("CATALOG_URL") or "").strip()
    telegram = (env.get("TELEGRAM_URL") or "").strip()
    html = html_path.read_text(encoding="utf-8")

    if args.mode == "expand":
        if not catalog and not telegram:
            print("ERROR: CATALOG_URL / TELEGRAM_URL missing in env or memory/site.env.local", file=sys.stderr)
            return 2
        new_html, n = expand_html(html, catalog, telegram)
        action = "expanded"
    else:
        new_html, n = redact_html(html, catalog, telegram)
        action = "redacted"

    if new_html != html:
        html_path.write_text(new_html, encoding="utf-8")
    print(f"OK CTA {action}: {n} href(s) in {html_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
