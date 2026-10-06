#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


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


def load_published_slugs(root: Path) -> set[str]:
    ledger_path = root / "shared/published-articles.md"
    slugs: set[str] = set()
    if not ledger_path.is_file():
        return slugs
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| 20"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 5 and cells[4].lower() in {"published", "in_progress", "draft_ready"}:
                slug = cells[2].strip().lower()
                if slug:
                    slugs.add(slug)
    return slugs


def load_active_article_topics(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = re.match(r"((?:B|AS)\d+)-", path.name, flags=re.IGNORECASE)
        if match:
            active.add(match.group(1).upper())
    return active


def load_live_wp_slugs(root: Path) -> set[str]:
    """Live WP slugs from today.py env and optional inventory JSON (ledger may be incomplete)."""
    slugs: set[str] = set()

    env_raw = os.environ.get("EXCALIBUR_RECENT_WP_POSTS", "").strip()
    if env_raw:
        try:
            items = json.loads(env_raw)
        except json.JSONDecodeError:
            items = []
        if isinstance(items, list):
            for item in items:
                if isinstance(item, str):
                    # today.py compact: date|slug|title
                    parts = item.split("|", 2)
                    if len(parts) >= 2 and parts[1].strip():
                        slugs.add(parts[1].strip().lower())
                elif isinstance(item, dict):
                    slug = str(item.get("slug") or "").strip().lower()
                    if slug:
                        slugs.add(slug)

    for candidate in (
        root / "memory/blog/published-live-avtosales125.json",
        root / "memory/blog/published-live.json",
    ):
        if not candidate.is_file():
            continue
        try:
            payload = json.loads(candidate.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        posts = payload.get("posts") if isinstance(payload, dict) else None
        if not isinstance(posts, list):
            continue
        for post in posts:
            if not isinstance(post, dict):
                continue
            slug = str(post.get("slug") or "").strip().lower()
            if slug:
                slugs.add(slug)
    return slugs


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in re.finditer(r"##\s+((?:B|AS)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)|\Z)", text, re.DOTALL):
        topic_id = match.group(1).upper()
        block = match.group(2)

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
    live_slugs: set[str] | None = None,
) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    warnings = []
    live_slugs = live_slugs or set()

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
                        f"High overlap ({round(similarity*100)}%) with topic {t['topic_id']} ({status}). "
                        f"Query: '{t['primary_query']}'"
                    ),
                }
            )

    # Slug-ish collision against live WP (hyphenate query tokens roughly)
    candidate_slug = re.sub(r"[^\w\s-]", "", new_query.lower())
    candidate_slug = re.sub(r"\s+", "-", candidate_slug.strip())
    if candidate_slug and candidate_slug in live_slugs:
        warnings.append(
            {
                "severity": "CRITICAL",
                "topic_id": "live-wp",
                "similarity": 1.0,
                "status": "live_wp",
                "message": f"Slug already on live WordPress: '{candidate_slug}'",
            }
        )
    return warnings


def next_b_topic_id(existing: list[dict[str, str]], reserved: set[str]) -> str:
    max_num = 0
    for t in existing:
        m = re.match(r"B(\d+)", t["topic_id"])
        if m:
            max_num = max(max_num, int(m.group(1)))
    for tid in reserved:
        m = re.match(r"B(\d+)", tid)
        if m:
            max_num = max(max_num, int(m.group(1)))
    return f"B{max_num + 1:02d}"


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
    published_slugs = load_published_slugs(root)
    active = load_active_article_topics(root)
    live_slugs = load_live_wp_slugs(root)
    reserved = published | active
    existing = load_existing_topics(root)

    # Topics whose slug already exists on live WP or ledger are treated as taken.
    slug_taken = published_slugs | live_slugs
    for t in existing:
        slug = (t.get("slug") or "").strip().lower()
        if slug and slug in slug_taken:
            reserved.add(t["topic_id"])

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = next_b_topic_id(existing, reserved)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Ledger topic IDs: {sorted(published)}")
        print(f"Live/ledger slug count (dedupe): {len(slug_taken)}")
        if live_slugs:
            sample = sorted(live_slugs)[:12]
            print(f"Live WP slug sample: {sample}")
        else:
            print(
                "Live WP slug sample: [] "
                "(set EXCALIBUR_RECENT_WP_POSTS from today.py or refresh published-live JSON)"
            )

        unwritten = []
        for t in existing:
            if t["topic_id"] in reserved:
                continue
            slug = (t.get("slug") or "").strip().lower()
            if slug and slug in slug_taken:
                continue
            unwritten.append(t["topic_id"])
        print(f"Unwritten topic IDs in pool: {unwritten}")
        print(
            "NOTE: ledger may be incomplete — always cross-check EXCALIBUR_RECENT_WP_POSTS "
            "and wordpress_search_posts before locking topic_id/slug."
        )
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved, live_slugs=slug_taken)
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
