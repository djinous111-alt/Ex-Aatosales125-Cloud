#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from excalibur_topic_ids import (
    iter_topic_cards,
    load_live_slug_dump,
    next_topic_id,
    prefer_topic_prefix,
    topic_id_from_article_dirname,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_published_topics(root: Path) -> set[str]:
    ledger_path = root / "shared/published-articles.md"
    published = set()
    if not ledger_path.is_file():
        return published
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| 20"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 5 and cells[4].lower() in {"published", "in_progress", "draft_ready"}:
                published.add(cells[1].upper())
    return published


def load_active_article_topics(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        topic_id = topic_id_from_article_dirname(path.name)
        if topic_id:
            active.add(topic_id)
    return active


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for topic_id, block in iter_topic_cards(text):

        def field(name: str) -> str:
            m = re.search(rf"(?:-|\*)\s*\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            if not m:
                m = re.search(rf"\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            return m.group(1).strip() if m else ""

        topics.append(
            {
                "topic_id": topic_id,
                "primary_query": field("primary_query"),
                "slug": field("slug"),
                "priority": field("priority"),
            }
        )
    return topics


def normalize_and_tokenize(text: str) -> set[str]:
    text = text.lower()
    text = re.sub(r"[^\w\s\-]", " ", text)
    words = text.split()
    tokens = set()
    for w in words:
        w_clean = w.strip()
        if not w_clean or w_clean in {"в", "на", "и", "или", "с", "по", "для", "как", "что", "это"}:
            continue
        tokens.add(w_clean[:5] if len(w_clean) > 4 else w_clean)
    return tokens


def check_overlap(
    new_query: str,
    existing_topics: list[dict[str, str]],
    reserved_ids: set[str],
    live_posts: list[dict[str, str]] | None = None,
) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    warnings: list[dict[str, Any]] = []
    new_norm = new_query.strip().lower().replace(" ", "-")

    for t in existing_topics:
        ext_tokens = normalize_and_tokenize(t["primary_query"])
        if not new_tokens or not ext_tokens:
            continue
        intersection = len(new_tokens.intersection(ext_tokens))
        union = len(new_tokens.union(ext_tokens))
        similarity = intersection / union

        status = "reserved" if t["topic_id"] in reserved_ids else "in_pool"

        if t["primary_query"].strip().lower() == new_query.strip().lower():
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "message": (
                        f"EXACT MATCH found with topic {t['topic_id']} ({status})! "
                        f"Primary query: '{t['primary_query']}'"
                    ),
                }
            )
        elif similarity >= 0.35:
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": t["topic_id"],
                    "similarity": round(similarity, 2),
                    "status": status,
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with topic "
                        f"{t['topic_id']} ({status}). Query: '{t['primary_query']}'"
                    ),
                }
            )

        slug = (t.get("slug") or "").strip().lower()
        if slug and (slug == new_norm or new_norm in slug or slug in new_norm):
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": t["topic_id"],
                    "similarity": 0.9,
                    "status": status,
                    "message": f"Slug overlap with topic {t['topic_id']}: '{slug}' vs query tokens '{new_norm}'",
                }
            )

    for post in live_posts or []:
        slug = (post.get("slug") or "").strip().lower()
        title_tokens = normalize_and_tokenize(post.get("title") or "")
        if not slug and not title_tokens:
            continue
        if slug and (slug == new_norm or new_norm.replace("-", "") in slug.replace("-", "")):
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": "live-wp",
                    "similarity": 0.85,
                    "status": "published_live",
                    "message": (
                        f"Live WP slug overlap: '{slug}' "
                        f"(source={post.get('source', 'live-dump')})"
                    ),
                }
            )
            continue
        if new_tokens and title_tokens:
            intersection = len(new_tokens.intersection(title_tokens))
            union = len(new_tokens.union(title_tokens))
            similarity = intersection / union if union else 0.0
            if similarity >= 0.45:
                warnings.append(
                    {
                        "severity": "WARNING",
                        "topic_id": "live-wp",
                        "similarity": round(similarity, 2),
                        "status": "published_live",
                        "message": (
                            f"Live WP title overlap ({round(similarity * 100)}%) "
                            f"with '{post.get('title', '')[:80]}' (slug={slug})"
                        ),
                    }
                )

    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    reserved = published | active
    existing = load_existing_topics(root)
    existing_ids = [t["topic_id"] for t in existing]

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        prefix = prefer_topic_prefix(existing_ids)
        next_id = next_topic_id(existing_ids, prefix=prefix)
        print(f"Topic ID series: {prefix}* (regex (?:AS|B)\\d+)")
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        live_posts = load_live_slug_dump(root)
        warnings = check_overlap(args.check_query, existing, reserved, live_posts=live_posts)
        if live_posts:
            print(f"(also checked {len(live_posts)} live WP slugs from dump)")
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | Topic: {w['topic_id']} ({w['status']})")
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
