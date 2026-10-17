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
    """Load memory/topics/live-reserved.json (live WP B* + denylist_slugs)."""
    path = root / "memory" / "topics" / "live-reserved.json"
    if not path.is_file():
        return {
            "reserved_ids": set(),
            "denylist_slugs": set(),
            "next_forced_topic_id": "",
            "max_live_b_num": 0,
            "path": str(path),
            "loaded": False,
        }
    data = json.loads(path.read_text(encoding="utf-8"))
    reserved_ids: set[str] = set()
    max_live_b = 0
    for row in data.get("reserved") or []:
        tid = str(row.get("topic_id") or "").strip().upper()
        if tid:
            reserved_ids.add(tid)
            m = re.match(r"B(\d+)$", tid)
            if m:
                max_live_b = max(max_live_b, int(m.group(1)))
    denylist = {str(s).strip().lower() for s in (data.get("denylist_slugs") or []) if str(s).strip()}
    forced = str(data.get("next_forced_topic_id") or "").strip().upper()
    return {
        "reserved_ids": reserved_ids,
        "denylist_slugs": denylist,
        "next_forced_topic_id": forced,
        "max_live_b_num": max_live_b,
        "path": str(path),
        "loaded": True,
    }


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
                        f"High overlap ({round(similarity * 100)}%) with topic "
                        f"{t['topic_id']} ({status}). Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def check_slug(slug: str, existing: list[dict[str, str]], denylist: set[str], reserved_ids: set[str]) -> list[str]:
    slug_norm = slug.strip().lower().strip("/")
    errors: list[str] = []
    if not slug_norm:
        errors.append("empty slug")
        return errors
    if slug_norm in denylist:
        errors.append(f"slug is on live-reserved denylist: {slug_norm}")
    for t in existing:
        ext = (t.get("slug") or "").strip().lower().strip("/")
        if not ext:
            continue
        if ext == slug_norm:
            status = "reserved" if t["topic_id"] in reserved_ids else "in_pool"
            errors.append(f"exact slug match with {t['topic_id']} ({status})")
    return errors


def suggest_next_id(
    existing: list[dict[str, str]],
    reserved: set[str],
    live: dict[str, Any],
) -> str:
    """Prefer next_forced_topic_id, else next free B* after max(pool, live, reserved)."""
    forced = live.get("next_forced_topic_id") or ""
    if forced and forced not in reserved:
        return forced

    max_num = int(live.get("max_live_b_num") or 0)
    for t in existing:
        m = re.match(r"B(\d+)$", t["topic_id"])
        if m:
            max_num = max(max_num, int(m.group(1)))
    for tid in reserved:
        m = re.match(r"B(\d+)$", tid)
        if m:
            max_num = max(max_num, int(m.group(1)))

    candidate_num = max_num + 1
    while True:
        candidate = f"B{candidate_num:02d}"
        if candidate not in reserved:
            return candidate
        candidate_num += 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument("--check-slug", type=str, default="", help="Check slug against live-reserved denylist + pool")
    ap.add_argument(
        "--skip-live-reserved",
        action="store_true",
        help="Ignore memory/topics/live-reserved.json (local-only debug)",
    )
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    live = (
        {
            "reserved_ids": set(),
            "denylist_slugs": set(),
            "next_forced_topic_id": "",
            "max_live_b_num": 0,
            "loaded": False,
        }
        if args.skip_live_reserved
        else load_live_reserved(root)
    )
    reserved = published | active | set(live.get("reserved_ids") or set())
    existing = load_existing_topics(root)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = suggest_next_id(existing, reserved, live)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress/live-reserved: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Live-reserved loaded: {bool(live.get('loaded'))}")
        print(f"Live-reserved topic IDs: {sorted(live.get('reserved_ids') or [])}")
        if live.get("next_forced_topic_id"):
            print(f"next_forced_topic_id: {live['next_forced_topic_id']}")
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_slug:
        errors = check_slug(
            args.check_slug,
            existing,
            set(live.get("denylist_slugs") or set()),
            reserved,
        )
        if errors:
            print("❌ SLUG BLOCKED:")
            for err in errors:
                print(f"  - {err}")
            return 1
        print("✅ SLUG OK: not on denylist and no exact pool collision.")
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
