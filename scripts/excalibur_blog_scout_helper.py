#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from urllib.request import Request, urlopen

TOPIC_DIR_RE = re.compile(r"^((?:AS|B)\d+)-", flags=re.IGNORECASE)
TOPIC_CARD_RE = re.compile(
    r"##\s+((?:AS|B)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:AS|B)\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)
WP_LOG_TOPIC_RE = re.compile(r"##\s+\d{4}-\d{2}-\d{2}\s+[—-]\s*((?:AS|B)\d+)\b", re.I)
TOPIC_ID_RE = re.compile(r"^((?:AS|B)\d+)$", re.I)


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


def load_ledger_slug_map(root: Path) -> dict[str, str]:
    """slug → topic_id from published-articles.md (any status)."""
    ledger_path = root / "shared/published-articles.md"
    mapping: dict[str, str] = {}
    if not ledger_path.is_file():
        return mapping
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3:
            mapping[cells[2]] = cells[1].upper()
    return mapping


def load_active_article_topics(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = TOPIC_DIR_RE.match(path.name)
        if match:
            active.add(match.group(1).upper())
    return active


def load_article_dir_slug_map(root: Path) -> dict[str, str]:
    articles_dir = root / "memory" / "blog" / "articles"
    mapping: dict[str, str] = {}
    if not articles_dir.is_dir():
        return mapping
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = TOPIC_DIR_RE.match(path.name)
        if not match:
            continue
        topic_id = match.group(1).upper()
        slug = path.name.split("-", 1)[1] if "-" in path.name else ""
        if slug:
            mapping[slug] = topic_id
    return mapping


def load_wp_log_topics(root: Path) -> set[str]:
    path = root / "memory/blog/wp-publish-log.md"
    if not path.is_file():
        return set()
    return {m.group(1).upper() for m in WP_LOG_TOPIC_RE.finditer(path.read_text(encoding="utf-8"))}


def load_slug_topic_hints(root: Path) -> dict[str, str]:
    path = root / "memory/topics/slug-topic-hints.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    slugs = data.get("slugs") or {}
    return {str(k): str(v).upper() for k, v in slugs.items() if TOPIC_ID_RE.match(str(v))}


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
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
            }
        )
    return topics


def parse_recent_wp_slugs() -> list[str]:
    """Parse EXCALIBUR_RECENT_WP_POSTS env (JSON list of date|slug|title or id|date|slug|title)."""
    raw = os.environ.get("EXCALIBUR_RECENT_WP_POSTS", "").strip()
    if not raw:
        return []
    try:
        items = json.loads(raw)
    except json.JSONDecodeError:
        return []
    slugs: list[str] = []
    for item in items:
        if isinstance(item, dict):
            slug = str(item.get("slug") or "").strip()
        else:
            parts = str(item).split("|")
            # formats: date|slug|title OR id|date|slug|title
            if len(parts) >= 4 and re.fullmatch(r"\d+", parts[0] or ""):
                slug = parts[2].strip()
            elif len(parts) >= 2:
                slug = parts[1].strip()
            else:
                slug = ""
        if slug:
            slugs.append(slug)
    return slugs


def fetch_live_wp_slugs(limit: int = 20) -> list[str]:
    site_url = (os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or "").strip()
    if not site_url:
        return []
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=slug",
    )
    request = Request(endpoint, headers={"User-Agent": "ExcaliburBlogScoutHelper/1.0"})
    try:
        with urlopen(request, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception:  # noqa: BLE001
        return []
    return [str(item.get("slug") or "").strip() for item in payload if item.get("slug")]


def live_used_topic_ids(root: Path, slug_maps: list[dict[str, str]]) -> set[str]:
    slugs = parse_recent_wp_slugs() or fetch_live_wp_slugs()
    if not slugs:
        return set()
    merged: dict[str, str] = {}
    for mapping in slug_maps:
        merged.update(mapping)
    used: set[str] = set()
    for slug in slugs:
        tid = merged.get(slug)
        if tid:
            used.add(tid.upper())
    return used


def max_b_number(topic_ids: set[str] | list[str]) -> int:
    max_num = 0
    for tid in topic_ids:
        m = re.match(r"B(\d+)$", str(tid).upper())
        if m:
            max_num = max(max_num, int(m.group(1)))
    return max_num


def suggest_next_b_id(reserved: set[str], pool_ids: set[str]) -> str:
    """Next B## = max(pool, reserved B nums) + 1, skipping any still-reserved IDs."""
    start = max_b_number(reserved | pool_ids) + 1
    # Empty history → B01, but never return an ID already reserved.
    n = max(start, 1)
    while f"B{n:02d}" in reserved:
        n += 1
    return f"B{n:02d}"


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
                    "message": f"EXACT MATCH found with topic {t['topic_id']} ({status})! Primary query: '{t['primary_query']}'",
                }
            )
        elif similarity >= 0.35:
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": t["topic_id"],
                    "similarity": round(similarity, 2),
                    "status": status,
                    "message": f"High overlap ({round(similarity * 100)}%) with topic {t['topic_id']} ({status}). Query: '{t['primary_query']}'",
                }
            )
    return warnings


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
    wp_log = load_wp_log_topics(root)
    slug_maps = [
        load_ledger_slug_map(root),
        load_article_dir_slug_map(root),
        load_slug_topic_hints(root),
    ]
    live_used = live_used_topic_ids(root, slug_maps)
    reserved = published | active | wp_log | live_used
    existing = load_existing_topics(root)
    pool_ids = {t["topic_id"] for t in existing}

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = suggest_next_b_id(reserved, pool_ids)
        print(f"Next available topic ID: {next_id}")
        print("Note: new scout cards use B## series; AS## legacy cards are counted in pool/overlap.")
        print("Seed sources: blog-topics pool + published-articles + article dirs + wp-publish-log + LIVE WP slug hints.")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Reserved topic IDs: {sorted(reserved)}")
        print(f"Live-used topic IDs (slug match): {sorted(live_used)}")
        print(f"Active article dirs: {sorted(active)}")
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
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
