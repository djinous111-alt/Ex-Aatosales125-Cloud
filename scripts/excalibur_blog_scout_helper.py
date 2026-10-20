#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
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


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    """Load Bxx and ASxx topic cards from blog-topics.md."""
    topics_path = root / "memory/topics/blog-topics.md"
    topics: list[dict[str, str]] = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in re.finditer(
        r"##\s+((?:B|AS)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)\d+|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    ):
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
                "source": "blog-topics",
            }
        )
    return topics


def load_live_published_posts(root: Path) -> list[dict[str, str]]:
    """Load live WP slugs/titles from memory/blog/published-live-*.json (cannibal denylist)."""
    posts: list[dict[str, str]] = []
    blog_dir = root / "memory" / "blog"
    if not blog_dir.is_dir():
        return posts
    for path in sorted(blog_dir.glob("published-live-*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for item in data.get("posts") or []:
            slug = str(item.get("slug") or "").strip()
            title = str(item.get("title") or "").strip()
            if not slug and not title:
                continue
            posts.append(
                {
                    "topic_id": f"LIVE:{slug or title[:40]}",
                    "primary_query": title or slug.replace("-", " "),
                    "slug": slug,
                    "priority": "live",
                    "source": path.name,
                }
            )
    return posts


def load_ledger_slugs(root: Path) -> list[dict[str, str]]:
    """Treat published ledger rows as cannibal sources (ASxx + Bxx)."""
    ledger_path = root / "shared/published-articles.md"
    rows: list[dict[str, str]] = []
    if not ledger_path.is_file():
        return rows
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        if cells[4].lower() not in {"published", "in_progress", "draft_ready"}:
            continue
        topic_id = cells[1].upper()
        slug = cells[2]
        rows.append(
            {
                "topic_id": topic_id,
                "primary_query": slug.replace("-", " "),
                "slug": slug,
                "priority": cells[4],
                "source": "ledger",
            }
        )
    return rows


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
) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    new_slugish = re.sub(r"[^\w]+", "-", new_query.lower()).strip("-")
    warnings: list[dict[str, Any]] = []

    for t in existing_topics:
        ext_query = t.get("primary_query") or ""
        ext_slug = (t.get("slug") or "").lower()
        ext_tokens = normalize_and_tokenize(ext_query)
        if not new_tokens or not ext_tokens:
            # Still catch exact slug collisions from live/ledger
            if ext_slug and (ext_slug == new_slugish or ext_slug in new_slugish or new_slugish in ext_slug):
                warnings.append(
                    {
                        "severity": "CRITICAL",
                        "topic_id": t["topic_id"],
                        "similarity": 1.0,
                        "status": t.get("source") or "live",
                        "message": (
                            f"SLUG/TITLE overlap with {t['topic_id']} ({t.get('source')}). "
                            f"slug='{ext_slug}' query='{ext_query}'"
                        ),
                    }
                )
            continue
        intersection = len(new_tokens.intersection(ext_tokens))
        union = len(new_tokens.union(ext_tokens))
        similarity = intersection / union if union else 0.0

        status = "reserved" if t["topic_id"] in reserved_ids else (t.get("source") or "in_pool")

        if ext_query.strip().lower() == new_query.strip().lower():
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
        elif ext_slug and ext_slug == new_slugish:
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "message": f"EXACT SLUG match with {t['topic_id']} ({status}): '{ext_slug}'",
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
                        f"High overlap ({round(similarity * 100)}%) with topic {t['topic_id']} "
                        f"({status}). Query: '{t['primary_query']}'"
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
    pool_topics = load_existing_topics(root)
    live_posts = load_live_published_posts(root)
    ledger_rows = load_ledger_slugs(root)

    # Deduplicate cannibal corpus: pool + ledger + live WP snapshot
    seen_keys: set[str] = set()
    cannibal_corpus: list[dict[str, str]] = []
    for item in pool_topics + ledger_rows + live_posts:
        key = f"{item.get('topic_id')}|{item.get('slug')}|{item.get('primary_query')}"
        if key in seen_keys:
            continue
        seen_keys.add(key)
        cannibal_corpus.append(item)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        max_num = 0
        for t in pool_topics:
            m = re.match(r"B(\d+)", t["topic_id"])
            if m:
                max_num = max(max_num, int(m.group(1)))

        next_id = f"B{max_num + 1:02d}" if max_num or any(t["topic_id"].startswith("B") for t in pool_topics) else "B01"
        # Empty B-pool → still suggest B01 (ASxx do not consume B-series)
        if max_num == 0 and not any(t["topic_id"].startswith("B") for t in pool_topics):
            next_id = "B01"

        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md Bxx+ASxx): {len(pool_topics)}")
        print(f"Total articles written/in_progress (ledger+dirs): {len(reserved)}")
        print(f"Live published posts (published-live-*.json): {len(live_posts)}")
        print(f"Active article dirs: {sorted(active)}")

        unwritten = [t["topic_id"] for t in pool_topics if t["topic_id"].startswith("B") and t["topic_id"] not in reserved]
        print(f"Unwritten B-topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, cannibal_corpus, reserved)
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(
                    f"  [{w['severity']}] Similarity: {w['similarity']} | "
                    f"Topic: {w['topic_id']} ({w['status']})"
                )
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        print(
            f"(checked pool={len(pool_topics)} ledger={len(ledger_rows)} "
            f"live={len(live_posts)} corpus={len(cannibal_corpus)})"
        )
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
