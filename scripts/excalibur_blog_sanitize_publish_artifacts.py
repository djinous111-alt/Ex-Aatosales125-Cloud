#!/usr/bin/env python3
"""Sanitize publish/indexer artifacts for Cloud secret-scan before commit.

Replaces absolute PUBLIC_SITE_URL / WP_* hosts with [PUBLIC_SITE_URL].
Does not print secret values.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from excalibur_blog_wp_publish import PUBLIC_SITE_PLACEHOLDER, load_env, sanitize_public_urls


DEFAULT_PATHS = (
    "shared/published-articles.md",
    "memory/blog/wp-publish-log.md",
    "memory/blog/interlink-suggestions.json",
    "memory/blog/llms.txt",
    "memory/blog/llms-full.txt",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def collect_bases(root: Path, extra: list[str]) -> list[str]:
    env = load_env(root)
    bases = [
        env.get("PUBLIC_SITE_URL", ""),
        env.get("WP_HOME", ""),
        env.get("WP_SITE_URL", ""),
        os.environ.get("PUBLIC_SITE_URL", ""),
        os.environ.get("WP_HOME", ""),
        os.environ.get("WP_SITE_URL", ""),
        *extra,
    ]
    return [b for b in bases if (b or "").strip()]


def main() -> int:
    ap = argparse.ArgumentParser(description="Sanitize absolute site URLs in publish artifacts")
    ap.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Files to sanitize (default: ledger/log/llms/interlink + article publish artifacts)",
    )
    ap.add_argument("--article-dir", type=Path, default=None, help="Also sanitize article publish artifacts")
    ap.add_argument("--public-base", action="append", default=[], help="Extra base URL to redact (repeatable)")
    ap.add_argument("--dry-run", action="store_true", help="Report files that would change without writing")
    args = ap.parse_args()

    root = project_root()
    bases = collect_bases(root, args.public_base)
    if not bases:
        print("No PUBLIC_SITE_URL/WP_* bases configured; nothing to sanitize", file=sys.stderr)
        return 0

    paths: list[Path] = []
    if args.paths:
        paths.extend(args.paths)
    else:
        paths.extend(root / rel for rel in DEFAULT_PATHS)

    if args.article_dir is not None:
        article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
        for name in (
            "wp-publish-result.json",
            "promotion-checklist.md",
            "schema.jsonld",
        ):
            candidate = article_dir / name
            if candidate.is_file():
                paths.append(candidate)

    changed = 0
    for path in paths:
        target = path if path.is_absolute() else root / path
        if not target.is_file():
            continue
        original = target.read_text(encoding="utf-8")
        sanitized = sanitize_public_urls(original, *bases)
        if sanitized == original:
            continue
        rel = target.relative_to(root) if target.is_relative_to(root) else target
        if args.dry_run:
            print(f"WOULD_SANITIZE {rel}")
        else:
            target.write_text(sanitized, encoding="utf-8")
            print(f"SANITIZED {rel} -> {PUBLIC_SITE_PLACEHOLDER}")
        changed += 1

    print(f"SUMMARY changed={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
