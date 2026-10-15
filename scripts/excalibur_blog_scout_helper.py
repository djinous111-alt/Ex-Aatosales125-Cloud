#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

# Topic IDs: B01, AS08, etc. (prefix letters + digits)
TOPIC_ID_RE = re.compile(r"([A-Z]+\d+)", re.IGNORECASE)
TOPIC_HEADING_RE = re.compile(
    r"##\s+([A-Z]+\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+[A-Z]+\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)
ARTICLE_DIR_RE = re.compile(r"^([A-Z]+\d+)-", re.IGNORECASE)


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


def load_published_slugs_and_queries(root: Path) -> list[dict[str, str]]:
    """Extra cannibalization signals from the publish ledger (slug column)."""
    ledger_path = root / "shared/published-articles.md"
    rows: list[dict[str, str]] = []
    if not ledger_path.is_file():
        return rows
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[4].lower() not in {"published", "in_progress", "draft_ready"}:
            continue
        topic_id = cells[1].upper()
        slug = cells[2]
        rows.append(
            {
                "topic_id": topic_id,
                "primary_query": slug.replace("-", " "),
                "slug": slug,
                "priority": "ledger",
            }
        )
    return rows


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
    text = re.sub(r"[^\w\s\-]", " ", text, flags=re.UNICODE)
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
    warnings = []

    for t in existing_topics:
        candidates = [t.get("primary_query") or ""]
        slug = t.get("slug") or ""
        if slug:
            candidates.append(slug.replace("-", " "))
        best_sim = 0.0
        best_label = candidates[0]
        for cand in candidates:
            ext_tokens = normalize_and_tokenize(cand)
            if not new_tokens or not ext_tokens:
                continue
            intersection = len(new_tokens.intersection(ext_tokens))
            union = len(new_tokens.union(ext_tokens))
            similarity = intersection / union if union else 0.0
            if similarity > best_sim:
                best_sim = similarity
                best_label = cand

        status = "reserved" if t["topic_id"] in reserved_ids else "in_pool"
        exact = any(
            (cand or "").strip().lower() == new_query.strip().lower()
            for cand in candidates
            if cand
        )

        if exact:
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "message": (
                        f"EXACT MATCH found with topic {t['topic_id']} ({status})! "
                        f"Primary query/slug: '{best_label}'"
                    ),
                }
            )
        elif best_sim >= 0.35:
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": t["topic_id"],
                    "similarity": round(best_sim, 2),
                    "status": status,
                    "message": (
                        f"High overlap ({round(best_sim * 100)}%) with topic "
                        f"{t['topic_id']} ({status}). Query/slug: '{best_label}'"
                    ),
                }
            )
    return warnings


def _next_b_id(existing: list[dict[str, str]]) -> str:
    max_num = 0
    for t in existing:
        m = re.match(r"B(\d+)$", t["topic_id"], flags=re.IGNORECASE)
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
    active = load_active_article_topics(root)
    reserved = published | active
    existing = load_existing_topics(root)
    ledger_extra = load_published_slugs_and_queries(root)

    # Deduplicate ledger rows already present as pool cards
    pool_ids = {t["topic_id"] for t in existing}
    for row in ledger_extra:
        if row["topic_id"] not in pool_ids:
            existing.append(row)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = _next_b_id(existing)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md + ledger extras): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        as_ids = sorted(t["topic_id"] for t in existing if t["topic_id"].startswith("AS"))
        b_ids = sorted(t["topic_id"] for t in existing if t["topic_id"].startswith("B"))
        print(f"AS* topic IDs visible: {as_ids}")
        print(f"B* topic IDs visible: {b_ids}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
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
