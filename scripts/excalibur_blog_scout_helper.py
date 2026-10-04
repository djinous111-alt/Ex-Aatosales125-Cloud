#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
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


def load_known_wp_rows(root: Path) -> list[dict[str, str]]:
    """Parse shared/known-wp-slugs.md table rows."""
    path = root / "shared/known-wp-slugs.md"
    rows: list[dict[str, str]] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0].lower() in {"post_id", "---"} or set(cells[0]) <= {"-"}:
            continue
        if not cells[0].isdigit():
            continue
        rows.append(
            {
                "post_id": cells[0],
                "slug": cells[1].strip().strip("`"),
                "topic_id": cells[2].upper() if cells[2] else "",
                "date": cells[3] if len(cells) > 3 else "",
            }
        )
    return rows


def load_known_wp_topic_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    for row in load_known_wp_rows(root):
        tid = row.get("topic_id") or ""
        if re.match(r"^(?:B|AS)\d+$", tid, flags=re.IGNORECASE):
            ids.add(tid.upper())
    return ids


def load_known_wp_slugs(root: Path) -> set[str]:
    return {row["slug"].lower() for row in load_known_wp_rows(root) if row.get("slug")}


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in re.finditer(
        r"##\s+((?:B|AS)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)|\Z)",
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


def check_slug_against_known(slug: str, known_slugs: set[str]) -> list[dict[str, Any]]:
    slug_l = slug.strip().lower().strip("/")
    if not slug_l:
        return []
    if slug_l in known_slugs:
        return [
            {
                "severity": "CRITICAL",
                "topic_id": "known-wp",
                "similarity": 1.0,
                "status": "published_wp",
                "message": f"Slug already live on WordPress (shared/known-wp-slugs.md): '{slug_l}'",
            }
        ]
    return []


def next_b_topic_id(existing: list[dict[str, str]], reserved: set[str]) -> str:
    max_num = 0
    for tid in reserved | {t["topic_id"] for t in existing}:
        m = re.match(r"B(\d+)$", tid.upper())
        if m:
            max_num = max(max_num, int(m.group(1)))
    candidate = max_num + 1
    while True:
        next_id = f"B{candidate:02d}"
        if next_id not in reserved:
            return next_id
        candidate += 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument("--check-slug", type=str, default="", help="Check slug against shared/known-wp-slugs.md")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    known_topics = load_known_wp_topic_ids(root)
    known_slugs = load_known_wp_slugs(root)
    reserved = published | active | known_topics
    existing = load_existing_topics(root)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = next_b_topic_id(existing, reserved)
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total reserved (ledger+dirs+known-wp): {len(reserved)}")
        print(f"Known WP slugs: {len(known_slugs)} (shared/known-wp-slugs.md)")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Known WP topic_ids: {sorted(known_topics)}")
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        if not (root / "shared/known-wp-slugs.md").is_file():
            print("WARN: shared/known-wp-slugs.md missing — slug reuse risk")
        return 0

    if args.check_slug:
        hits = check_slug_against_known(args.check_slug, known_slugs)
        if hits:
            print("❌ SLUG COLLISION:")
            for w in hits:
                print(f"  [{w['severity']}] {w['message']}")
            return 1
        print("✅ SLUG OK: not in shared/known-wp-slugs.md")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
        if args.check_slug:
            warnings.extend(check_slug_against_known(args.check_slug, known_slugs))
        # Also treat query that equals a known slug fragment as soft signal
        q_tokens = normalize_and_tokenize(args.check_query)
        for slug in known_slugs:
            slug_tokens = normalize_and_tokenize(slug.replace("-", " "))
            if not q_tokens or not slug_tokens:
                continue
            sim = len(q_tokens & slug_tokens) / len(q_tokens | slug_tokens)
            if sim >= 0.5:
                warnings.append(
                    {
                        "severity": "WARNING",
                        "topic_id": "known-wp",
                        "similarity": round(sim, 2),
                        "status": "published_wp",
                        "message": f"Query overlaps live WP slug '{slug}' ({round(sim * 100)}%)",
                    }
                )
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
