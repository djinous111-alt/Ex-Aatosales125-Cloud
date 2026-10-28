#!/usr/bin/env python3
"""Expand / redact secret CTA hrefs for Excalibur BLOG articles.

Authoring contract (conversion-map.md):
  - Write href="${CATALOG_URL}" / href="${TELEGRAM_URL}" / href="${MAX_URL}"
  - Never invent hosts; public 2GIS/Instagram stay as literal public URLs
  - Never commit live secret URL values (secret-scan)
  - Legacy href="[REDACTED]" is accepted; expand via env + anchor heuristics

Modes:
  --expand  : placeholders/[REDACTED] → env values (QA / publish payload)
  --redact  : env values → ${CATALOG_URL}/… placeholders (pre-commit hygiene)
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


CTA_ENV_KEYS = ("CATALOG_URL", "TELEGRAM_URL", "MAX_URL")
PLACEHOLDER_RE = re.compile(r"\$\{(CATALOG_URL|TELEGRAM_URL|MAX_URL)\}")
HREF_RE = re.compile(
    r'(<a\b[^>]*\bhref=["\'])([^"\']+)(["\'][^>]*>)(.*?)(</a>)',
    flags=re.IGNORECASE | re.DOTALL,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_cta_env() -> dict[str, str]:
    env: dict[str, str] = {}
    local = project_root() / "memory" / "site.env.local"
    if local.is_file():
        for line in local.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                key = key.strip()
                if key in CTA_ENV_KEYS:
                    env[key] = value.strip().strip('"').strip("'")
    for key in CTA_ENV_KEYS:
        value = (os.environ.get(key) or "").strip()
        if value and value not in {"[REDACTED]", "${" + key + "}"}:
            env[key] = value
    return env


def guess_cta_key(anchor_html: str, href: str) -> str | None:
    text = re.sub(r"<[^>]+>", " ", anchor_html).lower()
    href_l = href.lower()
    if "telegram" in text or "t.me/" in href_l or "avtosales125" in text and "telegram" in text:
        return "TELEGRAM_URL"
    if "max" in text.split() or "max.ru" in href_l or href_l.endswith("/max"):
        # Prefer MAX only when clearly messenger CTA, not "максимум".
        if "max" in text or "мессенджер" in text:
            return "MAX_URL"
    if any(tok in text for tok in ("каталог", "catalog", "avto-sales", "авто-сейлс", "подбор")):
        return "CATALOG_URL"
    if href in {"[REDACTED]", "${CATALOG_URL}"}:
        return "CATALOG_URL"
    return None


def expand_html(html: str, env: dict[str, str]) -> tuple[str, int]:
    replacements = 0

    def repl_placeholder(match: re.Match[str]) -> str:
        nonlocal replacements
        key = match.group(1)
        value = env.get(key)
        if not value:
            return match.group(0)
        replacements += 1
        return value

    html = PLACEHOLDER_RE.sub(repl_placeholder, html)

    def repl_anchor(match: re.Match[str]) -> str:
        nonlocal replacements
        prefix, href, mid, inner, suffix = match.groups()
        if href.startswith(("http://", "https://")) and href not in env.values():
            return match.group(0)
        key = None
        ph = PLACEHOLDER_RE.fullmatch(href)
        if ph:
            key = ph.group(1)
        elif href == "[REDACTED]":
            key = guess_cta_key(inner, href)
        if not key:
            return match.group(0)
        value = env.get(key)
        if not value:
            return match.group(0)
        if href == value:
            return match.group(0)
        replacements += 1
        return f"{prefix}{value}{mid}{inner}{suffix}"

    return HREF_RE.sub(repl_anchor, html), replacements


def redact_html(html: str, env: dict[str, str]) -> tuple[str, int]:
    # Longest values first to avoid partial overlaps outside anchors.
    items = sorted(((k, v) for k, v in env.items() if v), key=lambda kv: len(kv[1]), reverse=True)
    value_to_key = {v: k for k, v in items}

    out_parts: list[str] = []
    last = 0
    count = 0
    for match in HREF_RE.finditer(html):
        out_parts.append(html[last : match.start()])
        prefix, href, mid, inner, suffix = match.groups()
        new_href = href
        if href in value_to_key:
            new_href = f"${{{value_to_key[href]}}}"
        elif href == "[REDACTED]":
            key = guess_cta_key(inner, href)
            if key:
                new_href = f"${{{key}}}"
        if new_href != href:
            count += 1
        out_parts.append(f"{prefix}{new_href}{mid}{inner}{suffix}")
        last = match.end()
    out_parts.append(html[last:])
    # Also redact bare secret URLs that appear outside <a href> (rare).
    result = "".join(out_parts)
    for key, value in items:
        placeholder = f"${{{key}}}"
        if value in result:
            result = result.replace(value, placeholder)
            count += 1
    return result, count


def main() -> int:
    ap = argparse.ArgumentParser(description="Expand/redact Excalibur CTA hrefs")
    ap.add_argument("--article-html", type=Path, required=True)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--expand", action="store_true", help="Placeholders → env URLs")
    mode.add_argument("--redact", action="store_true", help="Env URLs → ${CATALOG_URL}/…")
    ap.add_argument("--write", action="store_true", help="Write file in place")
    args = ap.parse_args()

    path = args.article_html
    if not path.is_absolute():
        path = project_root() / path
    if not path.is_file():
        print(f"missing file: {path}", file=sys.stderr)
        return 2

    html = path.read_text(encoding="utf-8")
    env = load_cta_env()
    missing = [k for k in CTA_ENV_KEYS if k not in env]
    if args.expand and missing:
        print(f"WARN missing CTA env (expand partial): {', '.join(missing)}", file=sys.stderr)

    if args.expand:
        new_html, n = expand_html(html, env)
        action = "expand"
    else:
        new_html, n = redact_html(html, env)
        action = "redact"

    if args.write and new_html != html:
        path.write_text(new_html, encoding="utf-8")
    print(f"OK cta_{action} replacements={n} write={bool(args.write and new_html != html)}")
    if not args.write:
        # Dry-run: show whether content would change, without dumping URLs.
        print(f"changed={new_html != html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
