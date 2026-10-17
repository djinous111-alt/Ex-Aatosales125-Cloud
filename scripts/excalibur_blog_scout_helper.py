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
        match = re.match(r"(B\d+)-", path.name, flags=re.IGNORECASE)
        if match:
            active.add(match.group(1).upper())
    return active


def load_live_reserved(root: Path) -> dict[str, Any]:
    """Honor memory/topics/live-reserved.json (WP-live + forced next topic)."""
    path = root / "memory" / "topics" / "live-reserved.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def live_reserved_topic_ids(live: dict[str, Any]) -> set[str]:
    ids: set[str] = set()
    for item in live.get("reserved") or []:
        if isinstance(item, dict):
            tid = str(item.get("topic_id") or "").strip().upper()
            if tid:
                ids.add(tid)
        elif isinstance(item, str) and item.strip():
            ids.add(item.strip().upper())
    return ids


def live_denylist_slugs(live: dict[str, Any]) -> set[str]:
    return {str(s).strip().lower() for s in (live.get("denylist_slugs") or []) if str(s).strip()}


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


def check_overlap(new_query: str, existing_topics: list[dict[str, str]], reserved_ids: set[str]) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    warnings = []

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
                        f"High overlap ({round(similarity * 100)}%) with topic {t['topic_id']} ({status}). "
                        f"Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def suggest_next_topic_id(
    existing: list[dict[str, str]],
    reserved: set[str],
    live: dict[str, Any],
) -> tuple[str, str]:
    """Return (topic_id, reason). Prefer live-reserved next_forced_topic_id."""
    forced = str(live.get("next_forced_topic_id") or "").strip().upper()
    if forced:
        if forced not in reserved:
            return forced, "live-reserved.next_forced_topic_id"
        # Forced id already reserved — fall through to next free Bxx

    max_num = 0
    for t in existing:
        m = re.match(r"B(\d+)", t["topic_id"])
        if m:
            max_num = max(max_num, int(m.group(1)))
        if t["topic_id"] not in reserved:
            return t["topic_id"], "first_unwritten_in_pool"

    # Also scan live reserved max so we don't reuse B01 after live WP posts
    for tid in reserved:
        m = re.match(r"B(\d+)", tid)
        if m:
            max_num = max(max_num, int(m.group(1)))

    next_id = f"B{max_num + 1:02d}"
    return next_id, "next_after_max_reserved"


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument("--check-slug", type=str, default="", help="Check slug against live-reserved denylist")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    live = load_live_reserved(root)
    live_ids = live_reserved_topic_ids(live)
    reserved = published | active | live_ids
    existing = load_existing_topics(root)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id, reason = suggest_next_topic_id(existing, reserved, live)
        print(f"Next available topic ID: {next_id}")
        print(f"Suggestion reason: {reason}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress/live-reserved: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Live-reserved topic IDs: {sorted(live_ids)}")
        forced = str(live.get("next_forced_topic_id") or "").strip().upper()
        if forced:
            print(f"live-reserved.next_forced_topic_id: {forced}")
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_slug:
        slug = args.check_slug.strip().lower()
        denied = live_denylist_slugs(live)
        if slug in denied:
            print(f"❌ SLUG DENYLIST: '{slug}' is in live-reserved.denylist_slugs")
            return 1
        print(f"✅ SLUG OK: '{slug}' not in live denylist")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
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
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
