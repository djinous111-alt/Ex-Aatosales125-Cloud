#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

# Topic cards use AS* (legacy / niche pool) and B* (current blog series).
TOPIC_CARD_RE = re.compile(
    r"##\s+((?:AS|B)\d+)\s+[—\-][^\n]*\n(.*?)(?=\n---|\n##\s+(?:AS|B)\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)
ARTICLE_DIR_RE = re.compile(r"^((?:AS|B)\d+)-", re.IGNORECASE)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_published_rows(root: Path) -> list[dict[str, str]]:
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
        status = cells[4].lower()
        if status not in {"published", "in_progress", "draft_ready"}:
            continue
        rows.append(
            {
                "topic_id": cells[1].upper(),
                "slug": cells[2],
                "url": cells[3],
                "status": status,
            }
        )
    return rows


def load_published_topics(root: Path) -> set[str]:
    return {r["topic_id"] for r in load_published_rows(root)}


def load_active_article_topics(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = ARTICLE_DIR_RE.match(path.name)
        if match:
            active.add(match.group(1).upper())
    return active


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics: list[dict[str, str]] = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in TOPIC_CARD_RE.finditer(text):
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
                "source": "pool",
            }
        )
    return topics


def ledger_overlap_targets(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Synthetic topics from ledger slugs for --check-query (even if card removed)."""
    out: list[dict[str, str]] = []
    for row in rows:
        slug = (row.get("slug") or "").strip()
        if not slug or slug.startswith("memory/"):
            continue
        query_from_slug = slug.replace("-", " ").strip()
        out.append(
            {
                "topic_id": row["topic_id"],
                "primary_query": query_from_slug,
                "slug": slug,
                "priority": "",
                "source": f"ledger:{row.get('status') or 'unknown'}",
            }
        )
    return out


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
    warnings: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str]] = set()

    for t in existing_topics:
        key = (t["topic_id"], (t.get("primary_query") or "").lower())
        if key in seen_keys:
            continue
        seen_keys.add(key)

        ext_tokens = normalize_and_tokenize(t.get("primary_query") or "")
        slug_tokens = normalize_and_tokenize((t.get("slug") or "").replace("-", " "))
        pool_tokens = ext_tokens | slug_tokens
        if not new_tokens or not pool_tokens:
            continue
        intersection = len(new_tokens.intersection(pool_tokens))
        union = len(new_tokens.union(pool_tokens))
        similarity = intersection / union if union else 0.0

        status = "reserved" if t["topic_id"] in reserved_ids else "in_pool"
        source = t.get("source") or "pool"

        pq = (t.get("primary_query") or "").strip().lower()
        if pq and pq == new_query.strip().lower():
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "source": source,
                    "message": (
                        f"EXACT MATCH found with topic {t['topic_id']} ({status}/{source})! "
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
                    "source": source,
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with topic {t['topic_id']} "
                        f"({status}/{source}). Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def next_b_series_id(existing: list[dict[str, str]], reserved: set[str]) -> str:
    """Next Bxx id from pool + ledger + article dirs (AS* counted separately)."""
    max_num = 0
    for t in existing:
        m = re.match(r"B(\d+)$", t["topic_id"], flags=re.I)
        if m:
            max_num = max(max_num, int(m.group(1)))
    for topic_id in reserved:
        m = re.match(r"B(\d+)$", topic_id, flags=re.I)
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
    ledger_rows = load_published_rows(root)
    published = {r["topic_id"] for r in ledger_rows}
    active = load_active_article_topics(root)
    reserved = published | active
    existing = load_existing_topics(root)
    as_topics = [t for t in existing if t["topic_id"].startswith("AS")]
    b_topics = [t for t in existing if t["topic_id"].startswith("B")]

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = next_b_series_id(existing, reserved)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)} (AS={len(as_topics)}, B={len(b_topics)})")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Ledger reserved IDs: {sorted(published)}")
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        print(
            "NOTE: Cross-check Next ID against EXCALIBUR_RECENT_WP_POSTS from "
            "excalibur_blog_today.py. If WP already has a prior B01 (or same slug), "
            "start at B02+ even when the pool looks empty."
        )
        return 0

    if args.check_query:
        overlap_pool = existing + ledger_overlap_targets(ledger_rows)
        warnings = check_overlap(args.check_query, overlap_pool, reserved)
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(
                    f"  [{w['severity']}] Similarity: {w['similarity']} | "
                    f"Topic: {w['topic_id']} ({w['status']}/{w.get('source', 'pool')})"
                )
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
