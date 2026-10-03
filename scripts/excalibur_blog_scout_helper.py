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


def load_ledger_slugs(root: Path) -> set[str]:
    ledger_path = root / "shared/published-articles.md"
    slugs: set[str] = set()
    if not ledger_path.is_file():
        return slugs
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[2] and cells[2] != "slug":
            slugs.add(cells[2].lower())
    return slugs


def load_known_wp_slugs(root: Path) -> set[str]:
    """Durable blocklist that survives ledger resets (shared/known-wp-slugs.md)."""
    path = root / "shared/known-wp-slugs.md"
    slugs: set[str] = set()
    if not path.is_file():
        return slugs
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells:
            continue
        slug = cells[0].lower()
        if not slug or slug in {"slug", "---"} or slug.startswith("-"):
            continue
        if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            slugs.add(slug)
    return slugs


def load_article_dir_slugs(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    slugs: set[str] = set()
    if not articles_dir.is_dir():
        return slugs
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        meta = path / "article.meta.json"
        if meta.is_file():
            try:
                data = json.loads(meta.read_text(encoding="utf-8"))
                slug = str(data.get("slug") or "").strip().lower()
                if slug:
                    slugs.add(slug)
                    continue
            except (json.JSONDecodeError, OSError):
                pass
        # Fallback: B01-some-slug → some-slug
        match = re.match(r"(?:B|AS)\d+-(.+)$", path.name, flags=re.I)
        if match:
            slugs.add(match.group(1).lower())
    return slugs


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


def slug_to_queryish(slug: str) -> str:
    return slug.replace("-", " ")


def check_overlap(
    new_query: str,
    existing_topics: list[dict[str, str]],
    reserved_ids: set[str],
    *,
    known_slugs: set[str] | None = None,
    candidate_slug: str = "",
) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    warnings: list[dict[str, Any]] = []
    known_slugs = known_slugs or set()
    candidate_slug = (candidate_slug or "").strip().lower()

    if candidate_slug and candidate_slug in known_slugs:
        warnings.append(
            {
                "severity": "CRITICAL",
                "topic_id": "known-wp",
                "similarity": 1.0,
                "status": "published_wp",
                "message": (
                    f"EXACT SLUG MATCH with known WP/ledger slug '{candidate_slug}'. "
                    "Pick a fresh angle; do not republish."
                ),
            }
        )

    for slug in sorted(known_slugs):
        slug_tokens = normalize_and_tokenize(slug_to_queryish(slug))
        if not new_tokens or not slug_tokens:
            continue
        intersection = len(new_tokens.intersection(slug_tokens))
        union = len(new_tokens.union(slug_tokens))
        similarity = intersection / union if union else 0.0
        if similarity >= 0.45:
            warnings.append(
                {
                    "severity": "CRITICAL" if similarity >= 0.7 else "WARNING",
                    "topic_id": "known-wp",
                    "similarity": round(similarity, 2),
                    "status": "published_wp",
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with known published slug "
                        f"'{slug}' (ledger/known-wp-slugs). Query: '{new_query}'"
                    ),
                }
            )

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
        topic_slug = (t.get("slug") or "").strip().lower()
        if candidate_slug and topic_slug and candidate_slug == topic_slug:
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "message": f"EXACT SLUG MATCH with topic {t['topic_id']} slug '{topic_slug}'",
                }
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--slug",
        type=str,
        default="",
        help="Optional candidate slug to check against known WP/ledger slugs",
    )
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
    known_slugs = load_ledger_slugs(root) | load_known_wp_slugs(root) | load_article_dir_slugs(root)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        max_num = 0
        for t in existing:
            m = re.match(r"B(\d+)", t["topic_id"])
            if m:
                max_num = max(max_num, int(m.group(1)))

        next_id = f"B{max_num + 1:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Known published/WP slugs: {len(known_slugs)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(
            args.check_query,
            existing,
            reserved,
            known_slugs=known_slugs,
            candidate_slug=args.slug,
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
