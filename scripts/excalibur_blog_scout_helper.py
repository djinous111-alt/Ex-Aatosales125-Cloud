#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


OCCUPIED_IDS_PATH = Path("memory/topics/live-wp-occupied-ids.json")


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


def load_occupied_ids(root: Path) -> dict[str, Any]:
    path = root / OCCUPIED_IDS_PATH
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return data if isinstance(data, dict) else {}


def occupied_mapped_topic_ids(occupied: dict[str, Any]) -> set[str]:
    mapped = occupied.get("mapped_topic_ids") or {}
    if not isinstance(mapped, dict):
        return set()
    return {str(k).upper() for k in mapped.keys() if re.match(r"^B\d+$", str(k), flags=re.I)}


def occupied_avoid_fragments(occupied: dict[str, Any]) -> list[str]:
    fragments: list[str] = []
    for key in ("avoid_query_fragments", "avoid_queries", "denylist_fragments"):
        raw = occupied.get(key) or []
        if isinstance(raw, list):
            fragments.extend(str(x).strip().lower() for x in raw if str(x).strip())
    # de-dupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for frag in fragments:
        if frag not in seen:
            seen.add(frag)
            out.append(frag)
    return out


def occupied_slugs(occupied: dict[str, Any]) -> set[str]:
    raw = occupied.get("occupied_slugs") or []
    if not isinstance(raw, list):
        return set()
    return {str(x).strip().lower() for x in raw if str(x).strip()}


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


def check_occupied_denylist(new_query: str, occupied: dict[str, Any]) -> list[dict[str, Any]]:
    """Block queries that hit live-WP / automation denylist fragments or occupied slugs."""
    warnings: list[dict[str, Any]] = []
    q = (new_query or "").strip().lower()
    if not q:
        return warnings

    for frag in occupied_avoid_fragments(occupied):
        if frag and frag in q:
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": "live-wp-occupied",
                    "similarity": 1.0,
                    "status": "denylist",
                    "message": (
                        f"Query hits avoid_query_fragments from {OCCUPIED_IDS_PATH}: '{frag}'. "
                        "Pick another angle (MCP WordPress search is NOT the AVTO SALES denylist source)."
                    ),
                }
            )

    slugish = re.sub(r"[^\w\s\-]", " ", q)
    slugish = re.sub(r"\s+", "-", slugish.strip())
    for slug in occupied_slugs(occupied):
        # fragment match against slug tokens
        slug_tokens = [t for t in slug.split("-") if len(t) >= 4]
        hits = sum(1 for t in slug_tokens if t in q.replace(" ", "-") or t in q)
        if slug in slugish or hits >= max(3, len(slug_tokens) // 2):
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": "live-wp-occupied",
                    "similarity": 1.0,
                    "status": "occupied_slug",
                    "message": f"Query overlaps occupied_slug '{slug}' from {OCCUPIED_IDS_PATH}.",
                }
            )
    return warnings


def suggest_next_id(
    existing: list[dict[str, str]],
    reserved: set[str],
    occupied: dict[str, Any],
) -> str:
    """Next free Bxx: max(pool, reserved, mapped occupied) + 1, preferring next_suggested if free."""
    mapped = occupied_mapped_topic_ids(occupied)
    max_num = 0
    for tid in list(reserved) + list(mapped) + [t["topic_id"] for t in existing]:
        m = re.match(r"B(\d+)$", tid.upper())
        if m:
            max_num = max(max_num, int(m.group(1)))

    preferred = str(occupied.get("next_suggested_topic_id") or "").strip().upper()
    if preferred and re.match(r"^B\d+$", preferred):
        pref_num = int(preferred[1:])
        if preferred not in reserved and preferred not in mapped:
            return preferred
        max_num = max(max_num, pref_num)

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
    active = load_active_article_topics(root)
    occupied = load_occupied_ids(root)
    mapped = occupied_mapped_topic_ids(occupied)
    reserved = published | active | mapped
    existing = load_existing_topics(root)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = suggest_next_id(existing, reserved, occupied)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(published | active)}")
        print(f"Occupied mapped topic IDs (live-wp): {sorted(mapped)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Occupied-ids file: {OCCUPIED_IDS_PATH} {'OK' if occupied else 'MISSING'}")
        print(f"Avoid fragments loaded: {len(occupied_avoid_fragments(occupied))}")
        print(f"Occupied slugs loaded: {len(occupied_slugs(occupied))}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
        warnings.extend(check_occupied_denylist(args.check_query, occupied))
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
