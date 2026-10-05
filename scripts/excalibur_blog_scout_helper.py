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


def load_ledger_slug_to_topic(root: Path) -> dict[str, str]:
    """Map ledger slug -> topic_id for LIVE/ledger collision checks."""
    ledger_path = root / "shared/published-articles.md"
    mapping: dict[str, str] = {}
    if not ledger_path.is_file():
        return mapping
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        topic_id = cells[1].upper()
        slug = cells[2].strip().lower()
        if topic_id and slug:
            mapping[slug] = topic_id
    return mapping


def load_active_article_topics(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = re.match(r"(B\d+)-", path.name, flags=re.IGNORECASE)
        if match:
            active.add(match.group(1).upper())
    return active


def load_live_slugs(root: Path) -> set[str]:
    """Load LIVE WordPress slugs from stable memory/blog/published-live-*.json snapshots."""
    live: set[str] = set()
    blog_dir = root / "memory" / "blog"
    if not blog_dir.is_dir():
        return live
    for path in sorted(blog_dir.glob("published-live-*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for post in data.get("posts") or []:
            slug = str(post.get("slug") or "").strip().lower()
            if slug:
                live.add(slug)
    return live


def load_topic_ids_for_slugs(root: Path, slugs: set[str]) -> set[str]:
    """Resolve topic_ids for known LIVE slugs via ledger + article directories."""
    ids: set[str] = set()
    if not slugs:
        return ids
    for slug, topic_id in load_ledger_slug_to_topic(root).items():
        if slug in slugs:
            ids.add(topic_id.upper())
    articles_dir = root / "memory" / "blog" / "articles"
    if articles_dir.is_dir():
        for path in articles_dir.iterdir():
            if not path.is_dir():
                continue
            match = re.match(r"(B\d+)-(.+)$", path.name, flags=re.IGNORECASE)
            if match and match.group(2).lower() in slugs:
                ids.add(match.group(1).upper())
    return ids


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in re.finditer(r"##\s+(B\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+B|\Z)", text, re.DOTALL):
        topic_id = match.group(1).upper()
        block = match.group(2)

        def field(name: str) -> str:
            # Flexible matching for bullet points with different formats
            m = re.search(rf"(?:-|\*)\s*\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            if not m:
                # Fallback for plain bold key matching without lists
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
        slug = (t.get("slug") or "").strip().lower()
        if slug and slug in live_slugs:
            status = "live_wp"

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
    ap.add_argument("--check-slug", type=str, default="", help="Check new slug against LIVE WP + ledger")
    args = ap.parse_args()

    # Reconfigure stdout for utf-8 on Windows
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    live_slugs = load_live_slugs(root)
    live_topic_ids = load_topic_ids_for_slugs(root, live_slugs)
    reserved = published | active | live_topic_ids
    existing = load_existing_topics(root)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        max_num = 0
        for t in existing:
            m = re.match(r"B(\d+)", t["topic_id"])
            if m:
                max_num = max(max_num, int(m.group(1)))
        # Advance past reserved/published/active/LIVE-mapped Bxx even if missing from pool
        # (ledger gap / LIVE publish without local topic card).
        for rid in reserved:
            m = re.match(r"B(\d+)$", rid.upper())
            if m:
                max_num = max(max_num, int(m.group(1)))

        next_id = f"B{max_num + 1:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"LIVE WP slugs loaded: {len(live_slugs)}")
        print(f"LIVE-mapped topic IDs: {sorted(live_topic_ids)}")
        print(f"Reserved topic IDs: {sorted(reserved)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        live_pool_collisions = [
            f"{t['topic_id']}:{t.get('slug')}"
            for t in existing
            if (t.get("slug") or "").strip().lower() in live_slugs
        ]
        if live_pool_collisions:
            print(f"WARN pool slugs already LIVE: {live_pool_collisions}")
        return 0

    if args.check_slug:
        slug = args.check_slug.strip().lower()
        if slug in live_slugs:
            print(f"❌ LIVE SLUG COLLISION: '{slug}' already published on LIVE WP snapshot.")
            return 1
        ledger = load_ledger_slug_to_topic(root)
        if slug in ledger:
            print(f"❌ LEDGER SLUG COLLISION: '{slug}' reserved as {ledger[slug]} in published-articles.md")
            return 1
        print(f"✅ SLUG OK: '{slug}' not in LIVE snapshot or ledger.")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved, live_slugs=live_slugs)
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
