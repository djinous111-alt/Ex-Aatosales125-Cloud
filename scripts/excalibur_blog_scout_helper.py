#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


TOPIC_HEADING_RE = re.compile(
    r"##\s+((?:B|AS)\d+)\s+[—\-][^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)
TOPIC_ID_RE = re.compile(r"^(B|AS)(\d+)$", re.IGNORECASE)


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


def load_live_wp_occupied(root: Path) -> dict[str, Any]:
    path = root / "memory/topics/live-wp-occupied-ids.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in TOPIC_HEADING_RE.finditer(text):
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
                        f"High overlap ({round(similarity * 100)}%) with topic {t['topic_id']} "
                        f"({status}). Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def _max_numeric_id(ids: set[str], prefix: str) -> int:
    max_num = 0
    for topic_id in ids:
        m = TOPIC_ID_RE.match(topic_id)
        if not m:
            continue
        if m.group(1).upper() != prefix.upper():
            continue
        max_num = max(max_num, int(m.group(2)))
    return max_num


def suggest_next_topic_id(reserved: set[str], occupied_meta: dict[str, Any]) -> str:
    suggested = str(occupied_meta.get("next_suggested_topic_id") or "").strip().upper()
    if suggested and TOPIC_ID_RE.match(suggested) and suggested not in reserved:
        return suggested

    # Prefer next free Bxx after the highest known B id among reserved/pool.
    max_b = _max_numeric_id(reserved, "B")
    candidate_num = max_b + 1 if max_b else 1
    while True:
        candidate = f"B{candidate_num:02d}"
        if candidate not in reserved:
            return candidate
        candidate_num += 1


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
    occupied_meta = load_live_wp_occupied(root)
    occupied_ids = {
        str(x).strip().upper()
        for x in (occupied_meta.get("occupied_topic_ids") or [])
        if str(x).strip()
    }
    reserved = published | active | occupied_ids
    existing = load_existing_topics(root)
    for t in existing:
        reserved.add(t["topic_id"])

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        # Pool cards, ledger, article dirs and live-wp occupied IDs all reserve topic_ids.
        next_id = suggest_next_topic_id(reserved, occupied_meta)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(published | active)}")
        print(f"Live WP occupied IDs: {sorted(occupied_ids)}")
        print(f"Active article dirs: {sorted(active)}")
        if occupied_meta.get("next_suggested_topic_id"):
            print(f"live-wp next_suggested_topic_id: {occupied_meta.get('next_suggested_topic_id')}")

        unwritten = [
            t["topic_id"]
            for t in existing
            if t["topic_id"] not in (published | active | occupied_ids)
        ]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
        occupied_slugs = {
            str(x).strip().lower()
            for x in (occupied_meta.get("occupied_slugs") or []) + (occupied_meta.get("recent_wp_slugs") or [])
            if str(x).strip()
        }
        # Slug-level collision hint when query normalizes near an occupied slug token set.
        query_tokens = normalize_and_tokenize(args.check_query)
        for slug in sorted(occupied_slugs):
            slug_tokens = normalize_and_tokenize(slug.replace("-", " "))
            if not query_tokens or not slug_tokens:
                continue
            similarity = len(query_tokens & slug_tokens) / len(query_tokens | slug_tokens)
            if similarity >= 0.55:
                warnings.append(
                    {
                        "severity": "WARNING",
                        "topic_id": "live-wp",
                        "similarity": round(similarity, 2),
                        "status": "occupied_slug",
                        "message": f"High overlap ({round(similarity * 100)}%) with occupied WP slug '{slug}'",
                    }
                )
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
