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
    """Topic IDs with status published / in_progress / draft_ready in the ledger."""
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
    """Slugs already claimed in the ledger (any non-empty status row)."""
    ledger_path = root / "shared/published-articles.md"
    slugs: set[str] = set()
    if not ledger_path.is_file():
        return slugs
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[2] and cells[2].lower() not in {"slug", "---"}:
            slugs.add(cells[2].strip().lower())
    return slugs


def load_live_reserved(root: Path) -> tuple[set[str], set[str]]:
    """Optional live WP reservations not yet mirrored in the ledger.

    File: memory/topics/live-reserved.json
    {
      "topic_ids": ["B01"],
      "slugs": ["some-live-slug"]
    }
    """
    path = root / "memory" / "topics" / "live-reserved.json"
    if not path.is_file():
        return set(), set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set(), set()
    ids = {str(x).upper() for x in (data.get("topic_ids") or []) if str(x).strip()}
    slugs = {str(x).strip().lower() for x in (data.get("slugs") or []) if str(x).strip()}
    return ids, slugs


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


def max_b_number(*id_sets: set[str] | list[dict[str, str]]) -> int:
    max_num = 0
    for group in id_sets:
        if isinstance(group, set):
            for tid in group:
                m = re.match(r"B(\d+)$", tid.upper())
                if m:
                    max_num = max(max_num, int(m.group(1)))
        else:
            for t in group:
                m = re.match(r"B(\d+)$", str(t.get("topic_id", "")).upper())
                if m:
                    max_num = max(max_num, int(m.group(1)))
    return max_num


def next_free_topic_id(reserved: set[str], existing: list[dict[str, str]]) -> str:
    """Next Bxx that is free in ledger + live-reserved + article dirs + topic pool max."""
    max_num = max_b_number(reserved, existing)
    # Prefer first free slot after the highest known reserved/pool id.
    # If pool is empty but B01 is live-reserved, this yields B02 — not B01.
    candidate_num = max_num + 1 if max_num > 0 else 1
    # Also skip any holes that are still reserved (defensive).
    while True:
        candidate = f"B{candidate_num:02d}"
        if candidate not in reserved:
            return candidate
        candidate_num += 1


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


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument("--check-slug", type=str, default="", help="Check slug against ledger + live-reserved")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    live_ids, live_slugs = load_live_reserved(root)
    ledger_slugs = load_published_slugs(root)
    reserved = published | active | live_ids
    reserved_slugs = ledger_slugs | live_slugs
    existing = load_existing_topics(root)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = next_free_topic_id(reserved, existing)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Ledger reserved IDs: {sorted(published)}")
        print(f"Live-reserved IDs: {sorted(live_ids)}")
        print(f"Reserved slugs (ledger+live): {sorted(reserved_slugs)}")

        unwritten = [
            t["topic_id"]
            for t in existing
            if t["topic_id"] not in reserved
            and (not t.get("slug") or t["slug"].strip().lower() not in reserved_slugs)
        ]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        if unwritten:
            print(f"Prefer pool card first: {unwritten[0]} (else new {next_id})")
        return 0

    if args.check_slug:
        slug = args.check_slug.strip().lower()
        if slug in reserved_slugs:
            print(f"❌ SLUG RESERVED: {slug} is in ledger or live-reserved.json")
            return 1
        print(f"✅ SLUG FREE: {slug}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
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
