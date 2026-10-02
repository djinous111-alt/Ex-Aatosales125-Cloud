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
from html import unescape

# Legacy AS* pool + current B* series.
TOPIC_ID_RE = r"(?:AS|B)\d+"
TOPIC_CARD_RE = re.compile(
    rf"##\s+({TOPIC_ID_RE})\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:AS|B)\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)
ARTICLE_DIR_TOPIC_RE = re.compile(rf"^({TOPIC_ID_RE})-", re.IGNORECASE)


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
        match = ARTICLE_DIR_TOPIC_RE.match(path.name)
        if match:
            active.add(match.group(1).upper())
    return active


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
                "h1": field("h1"),
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


def slugify_guess(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-]", " ", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text


def fetch_recent_wp_posts(site_url: str, limit: int = 20) -> tuple[list[dict[str, str]], str | None]:
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=date,link,slug,title",
    )
    request = Request(endpoint, headers={"User-Agent": "ExcaliburBlogAutomation/1.0"})
    try:
        with urlopen(request, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [], f"{type(exc).__name__}: {exc}"

    pages: list[dict[str, str]] = []
    for item in payload:
        title = item.get("title", {}).get("rendered", "") if isinstance(item.get("title"), dict) else ""
        title = re.sub(r"<[^>]+>", "", title)
        pages.append(
            {
                "date": str(item.get("date", ""))[:10],
                "slug": str(item.get("slug", "")),
                "title": unescape(title).strip(),
                "link": str(item.get("link", "")),
            }
        )
    return pages, None


def parse_recent_wp_env(raw: str) -> list[dict[str, str]]:
    """Parse EXCALIBUR_RECENT_WP_POSTS compact lines: date|slug|title."""
    raw = (raw or "").strip()
    if not raw:
        return []
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return []
    posts: list[dict[str, str]] = []
    if not isinstance(payload, list):
        return posts
    for item in payload:
        if isinstance(item, str) and "|" in item:
            parts = item.split("|", 2)
            posts.append(
                {
                    "date": parts[0].strip(),
                    "slug": parts[1].strip(),
                    "title": parts[2].strip() if len(parts) > 2 else "",
                }
            )
        elif isinstance(item, dict):
            posts.append(
                {
                    "date": str(item.get("date") or "")[:10],
                    "slug": str(item.get("slug") or ""),
                    "title": str(item.get("title") or ""),
                }
            )
    return posts


def load_recent_wp_posts(explicit_json: str = "") -> tuple[list[dict[str, str]], str]:
    """Load recent WP posts from CLI JSON, env compact list, or live REST."""
    if explicit_json.strip():
        posts = parse_recent_wp_env(explicit_json)
        return posts, "cli-json"
    env_compact = os.environ.get("EXCALIBUR_RECENT_WP_POSTS", "").strip()
    if env_compact:
        return parse_recent_wp_env(env_compact), "env:EXCALIBUR_RECENT_WP_POSTS"
    site_url = (
        os.environ.get("PUBLIC_SITE_URL")
        or os.environ.get("WP_SITE_URL")
        or os.environ.get("WP_HOME")
        or ""
    ).strip()
    if site_url:
        posts, error = fetch_recent_wp_posts(site_url)
        if error:
            return [], f"live-error:{error}"
        return posts, "live-rest"
    return [], "unavailable"


def occupied_b_numbers(reserved_ids: set[str], wp_posts: list[dict[str, str]]) -> set[int]:
    """B-series numbers taken by ledger/dirs or live WP slugs like b03-... / topic markers."""
    nums: set[int] = set()
    for topic_id in reserved_ids:
        m = re.match(r"B(\d+)$", topic_id.upper())
        if m:
            nums.add(int(m.group(1)))
    for post in wp_posts:
        slug = (post.get("slug") or "").lower()
        m = re.match(r"b(\d+)(?:-|$)", slug)
        if m:
            nums.add(int(m.group(1)))
        # Also catch titles that embed B0x markers occasionally left in drafts.
        title = post.get("title") or ""
        for tm in re.finditer(r"\bB(\d+)\b", title, flags=re.I):
            nums.add(int(tm.group(1)))
    return nums


def check_overlap(new_query: str, existing_topics: list[dict[str, str]], reserved_ids: set[str]) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    warnings = []

    for t in existing_topics:
        ext_tokens = normalize_and_tokenize(t["primary_query"])
        if not new_tokens or not ext_tokens:
            continue
        intersection = len(new_tokens.intersection(ext_tokens))
        union = len(new_tokens.union(ext_tokens))
        similarity = intersection / union if union else 0.0

        status = "reserved" if t["topic_id"] in reserved_ids else "in_pool"

        if t["primary_query"].strip().lower() == new_query.strip().lower():
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "source": "blog-topics",
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
                    "source": "blog-topics",
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with topic "
                        f"{t['topic_id']} ({status}). Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def check_wp_overlap(
    new_query: str,
    proposed_slug: str,
    wp_posts: list[dict[str, str]],
) -> list[dict[str, Any]]:
    """Fail on near-duplicate slug/title against live/recent WordPress posts."""
    warnings: list[dict[str, Any]] = []
    if not wp_posts:
        return warnings

    query_tokens = normalize_and_tokenize(new_query)
    slug_norm = (proposed_slug or slugify_guess(new_query)).lower().strip()

    for post in wp_posts:
        live_slug = (post.get("slug") or "").lower().strip()
        live_title = post.get("title") or ""
        title_tokens = normalize_and_tokenize(live_title)
        source_id = f"WP:{live_slug or post.get('date') or 'unknown'}"

        if slug_norm and live_slug and (slug_norm == live_slug or slug_norm in live_slug or live_slug in slug_norm):
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": source_id,
                    "similarity": 1.0,
                    "status": "live_wp",
                    "source": "wordpress",
                    "message": (
                        f"SLUG near-duplicate vs live WP post '{live_slug}' "
                        f"({post.get('date')}: {live_title})"
                    ),
                }
            )
            continue

        if not query_tokens or not title_tokens:
            continue
        intersection = len(query_tokens.intersection(title_tokens))
        union = len(query_tokens.union(title_tokens))
        similarity = intersection / union if union else 0.0
        if similarity >= 0.35:
            warnings.append(
                {
                    "severity": "CRITICAL" if similarity >= 0.5 else "WARNING",
                    "topic_id": source_id,
                    "similarity": round(similarity, 2),
                    "status": "live_wp",
                    "source": "wordpress",
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with live WP "
                        f"'{live_slug}' title: '{live_title}'"
                    ),
                }
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--proposed-slug",
        type=str,
        default="",
        help="Optional kebab slug to compare against live WP slugs during --check-query",
    )
    ap.add_argument(
        "--recent-wp-json",
        type=str,
        default="",
        help="Optional JSON list of recent WP posts (compact date|slug|title or objects)",
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
    wp_posts, wp_source = load_recent_wp_posts(args.recent_wp_json)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        occupied = occupied_b_numbers(reserved, wp_posts)
        # Prefer continuing after max known B card, but never reuse occupied numbers
        # (ledger reset / live WP B01–B03 near-miss).
        max_num = max(occupied) if occupied else 0
        for t in existing:
            m = re.match(r"B(\d+)$", t["topic_id"].upper())
            if m:
                max_num = max(max_num, int(m.group(1)))
        next_num = max_num + 1
        while next_num in occupied:
            next_num += 1
        next_id = f"B{next_num:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"AS* cards in pool: {sum(1 for t in existing if t['topic_id'].startswith('AS'))}")
        print(f"B* cards in pool: {sum(1 for t in existing if t['topic_id'].startswith('B'))}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Occupied B numbers (ledger/dirs/WP): {sorted(occupied)}")
        print(f"Recent WP posts source: {wp_source} count={len(wp_posts)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
        warnings.extend(check_wp_overlap(args.check_query, args.proposed_slug, wp_posts))
        print(f"Recent WP posts source: {wp_source} count={len(wp_posts)}")
        if wp_source == "unavailable":
            print(
                "⚠️ WP dedupe unavailable: set PUBLIC_SITE_URL or EXCALIBUR_RECENT_WP_POSTS "
                "(from today.py) before appending a topic card."
            )
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(
                    f"  [{w['severity']}] Similarity: {w['similarity']} | "
                    f"Topic: {w['topic_id']} ({w['status']}) source={w.get('source')}"
                )
                print(f"  Message: {w['message']}")
            # Any CRITICAL (exact / live WP) fails hard; WARNING-only still fails to
            # keep Scout from appending near-duplicates without human review.
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
