#!/usr/bin/env python3
"""Restore CTA hrefs in article.html from env / conversion-map.

Cloud tool redaction may turn brand URLs into the literal [REDACTED] when agents
read briefs. Writers must not copy that placeholder into HTML. This helper
repairs article.html using:

1) env CATALOG_URL / TELEGRAM_URL / MAX_URL (preferred)
2) absolute https URLs parsed from memory/brief/conversion-map.md on disk

It never prints full URLs.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


REDACTED_RE = re.compile(r"\[REDACTED\]", re.I)
PLACEHOLDER_RE = re.compile(r"\[(CATALOG_URL|TELEGRAM_URL|MAX_URL|PUBLIC_SITE_URL)\]")
HREF_RE = re.compile(r'href="([^"]*)"', re.I)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def _safe_label(url: str) -> str:
    if not url:
        return "empty"
    if url.startswith("http"):
        return f"https(len={len(url)})"
    if REDACTED_RE.fullmatch(url.strip()):
        return "REDACTED"
    if PLACEHOLDER_RE.fullmatch(url.strip()):
        return url.strip()
    return f"other(len={len(url)})"


def load_conversion_urls(root: Path) -> dict[str, str]:
    path = root / "memory/brief/conversion-map.md"
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        label, url = cells[0], cells[1]
        if not url.startswith("http"):
            continue
        low = label.lower()
        if "каталог" in low or "catalog" in low:
            out.setdefault("catalog", url)
        elif "telegram" in low or "телеграм" in low:
            out.setdefault("telegram", url)
        elif low.strip() == "max" or low.startswith("max "):
            out.setdefault("max", url)
    return out


def resolve_cta_urls(root: Path) -> dict[str, str]:
    from_map = load_conversion_urls(root)
    catalog = (os.environ.get("CATALOG_URL") or os.environ.get("PUBLIC_CATALOG_URL") or "").strip() or from_map.get("catalog", "")
    telegram = (os.environ.get("TELEGRAM_URL") or os.environ.get("PUBLIC_TELEGRAM_URL") or "").strip() or from_map.get("telegram", "")
    max_url = (os.environ.get("MAX_URL") or os.environ.get("PUBLIC_MAX_URL") or "").strip() or from_map.get("max", "")
    return {"catalog": catalog, "telegram": telegram, "max": max_url}


def classify_anchor(anchor_html: str) -> str | None:
    text = re.sub(r"<[^>]+>", " ", anchor_html).lower()
    if "telegram" in text or "телеграм" in text or "@avtosales" in text or "t.me" in text:
        return "telegram"
    if "max" in text and ("мессенджер" in text or "написать" in text or "связ" in text):
        return "max"
    if "каталог" in text or "подобрать" in text or "расчёт" in text or "расчет" in text or "подбор" in text:
        return "catalog"
    return None


def restore_html(html: str, urls: dict[str, str]) -> tuple[str, list[str]]:
    notes: list[str] = []

    def replace_token(token: str) -> str:
        key = {
            "CATALOG_URL": "catalog",
            "TELEGRAM_URL": "telegram",
            "MAX_URL": "max",
        }.get(token)
        if not key:
            notes.append(f"left token [{token}] (no mapping)")
            return f"[{token}]"
        value = urls.get(key) or ""
        if not value.startswith("http"):
            notes.append(f"missing URL for [{token}]")
            return f"[{token}]"
        notes.append(f"expanded [{token}] -> {key}")
        return value

    # 1) Explicit env-style placeholders
    def token_sub(match: re.Match[str]) -> str:
        return replace_token(match.group(1))

    html = PLACEHOLDER_RE.sub(token_sub, html)

    # 2) href="[REDACTED]" — resolve by surrounding anchor text / position
    pieces: list[str] = []
    last = 0
    for match in HREF_RE.finditer(html):
        href = match.group(1).strip()
        if not REDACTED_RE.fullmatch(href):
            continue
        # look ahead a bit for </a> content
        window = html[match.end() : match.end() + 240]
        kind = classify_anchor(window)
        if kind is None:
            # default catalog for unresolved brand CTA
            kind = "catalog"
            notes.append("REDACTED href without clear anchor → catalog default")
        value = urls.get(kind) or ""
        if not value.startswith("http"):
            notes.append(f"cannot restore REDACTED href as {kind}: URL missing")
            continue
        pieces.append(html[last : match.start(1)])
        pieces.append(value)
        last = match.end(1)
        notes.append(f"restored REDACTED href as {kind}")
    if pieces:
        pieces.append(html[last:])
        html = "".join(pieces)

    return html, notes


def count_bad_hrefs(html: str) -> int:
    bad = 0
    for match in HREF_RE.finditer(html):
        href = match.group(1).strip()
        if REDACTED_RE.fullmatch(href) or PLACEHOLDER_RE.fullmatch(href):
            bad += 1
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description="Restore CTA hrefs from env/conversion-map")
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    html_path = article_dir / "article.html"
    if not html_path.is_file():
        print(f"ERROR: missing {html_path}", file=sys.stderr)
        return 1

    urls = resolve_cta_urls(root)
    print(
        "CTA sources:",
        f"catalog={_safe_label(urls['catalog'])}",
        f"telegram={_safe_label(urls['telegram'])}",
        f"max={_safe_label(urls['max'])}",
    )

    original = html_path.read_text(encoding="utf-8")
    updated, notes = restore_html(original, urls)
    before = count_bad_hrefs(original)
    after = count_bad_hrefs(updated)
    for note in notes:
        print(f"NOTE: {note}")
    print(f"bad_hrefs_before={before} bad_hrefs_after={after}")

    if before and after:
        print("ERROR: some CTA placeholders remain", file=sys.stderr)
        return 1
    if original == updated:
        print("OK no CTA changes needed")
        return 0
    if args.dry_run:
        print("OK dry-run (not written)")
        return 0

    html_path.write_text(updated, encoding="utf-8")
    print(f"OK wrote {html_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
