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

TOPIC_HEADING_RE = re.compile(
    r"##\s+([A-Z]+\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+[A-Z]+\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)
TOPIC_ID_RE = re.compile(r"\b([A-Z]+)(\d+)\b", re.IGNORECASE)
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


def load_ledger_slugs(root: Path) -> set[str]:
    ledger_path = root / "shared/published-articles.md"
    slugs: set[str] = set()
    if not ledger_path.is_file():
        return slugs
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[2]:
            slugs.add(cells[2].lower())
    return slugs


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


def extract_topic_ids(text: str) -> set[str]:
    """Extract canonical Bxx / ASn topic IDs from free text."""
    canonical: set[str] = set()
    for match in TOPIC_ID_RE.finditer(text or ""):
        prefix = match.group(1).upper()
        if prefix not in {"B", "AS"}:
            continue
        num = int(match.group(2))
        if prefix == "B":
            canonical.add(f"B{num:02d}")
        else:
            canonical.add(f"AS{num}")
    return canonical


def env_floor_ids() -> set[str]:
    ids: set[str] = set()
    for key in ("EXCALIBUR_TOPIC_ID_FLOOR", "EXCALIBUR_B_ID_FLOOR", "EXCALIBUR_AS_ID_FLOOR", "EXCALIBUR_MIN_TOPIC_ID"):
        raw = os.environ.get(key, "").strip().upper()
        if raw:
            ids |= extract_topic_ids(raw)
    return ids


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
                "title": title.strip(),
                "link": str(item.get("link", "")),
            }
        )
    return pages, None


def load_wp_posts_from_env() -> list[dict[str, str]]:
    raw = os.environ.get("EXCALIBUR_RECENT_WP_POSTS", "").strip()
    if not raw:
        return []
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return []
    posts: list[dict[str, str]] = []
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, str) and "|" in item:
                date, slug, title = (item.split("|", 2) + ["", ""])[:3]
                posts.append({"date": date, "slug": slug, "title": title, "link": ""})
            elif isinstance(item, dict):
                posts.append(
                    {
                        "date": str(item.get("date", ""))[:10],
                        "slug": str(item.get("slug", "")),
                        "title": str(item.get("title", "")),
                        "link": str(item.get("link", "")),
                    }
                )
    return posts


def collect_wp_signals(root: Path) -> tuple[list[dict[str, str]], set[str], set[str], str | None]:
    posts = load_wp_posts_from_env()
    error: str | None = None
    if not posts:
        site_url = os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or ""
        if site_url:
            posts, error = fetch_recent_wp_posts(site_url)
    ids: set[str] = set()
    slugs: set[str] = set()
    for post in posts:
        blob = " ".join([post.get("slug", ""), post.get("title", ""), post.get("link", "")])
        ids |= extract_topic_ids(blob)
        slug = (post.get("slug") or "").strip().lower()
        if slug:
            slugs.add(slug)
    return posts, ids, slugs, error


def max_num_for_prefix(topic_ids: set[str], prefix: str) -> int:
    max_num = 0
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)$", re.IGNORECASE)
    for tid in topic_ids:
        match = pattern.match(tid)
        if match:
            max_num = max(max_num, int(match.group(1)))
    return max_num


def format_next_id(prefix: str, max_num: int) -> str:
    nxt = max_num + 1
    if prefix.upper() == "B":
        return f"B{nxt:02d}"
    return f"{prefix.upper()}{nxt}"


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
    wp_posts: list[dict[str, str]] | None = None,
    ledger_slugs: set[str] | None = None,
) -> list[dict[str, Any]]:
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

    query_slug_guess = re.sub(r"[^\w\s-]", "", new_query.lower())
    query_slug_guess = re.sub(r"\s+", "-", query_slug_guess.strip())
    for slug in ledger_slugs or set():
        if slug and (slug == query_slug_guess or slug in query_slug_guess or query_slug_guess in slug):
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": "ledger",
                    "similarity": 1.0,
                    "status": "published_ledger",
                    "message": f"Slug/query overlaps published ledger slug '{slug}'",
                }
            )

    for post in wp_posts or []:
        slug = (post.get("slug") or "").lower()
        title = post.get("title") or ""
        title_tokens = normalize_and_tokenize(title)
        if slug and (slug == query_slug_guess or slug in query_slug_guess or query_slug_guess in slug):
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": "live_wp",
                    "similarity": 1.0,
                    "status": "live_wp",
                    "message": f"Slug/query overlaps live WP slug '{slug}' ({title})",
                }
            )
            continue
        if new_tokens and title_tokens:
            intersection = len(new_tokens.intersection(title_tokens))
            union = len(new_tokens.union(title_tokens))
            similarity = intersection / union if union else 0.0
            if similarity >= 0.45:
                warnings.append(
                    {
                        "severity": "CRITICAL",
                        "topic_id": "live_wp",
                        "similarity": round(similarity, 2),
                        "status": "live_wp",
                        "message": f"High overlap ({round(similarity * 100)}%) with live WP title '{title}' (slug={slug})",
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
    reserved = published | active
    existing = load_existing_topics(root)
    pool_ids = {t["topic_id"] for t in existing}
    ledger_slugs = load_ledger_slugs(root)
    wp_posts, wp_ids, wp_slugs, wp_error = collect_wp_signals(root)
    floor_ids = env_floor_ids()

    all_known_ids = pool_ids | reserved | wp_ids | floor_ids

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        max_b = max_num_for_prefix(all_known_ids, "B")
        max_as = max_num_for_prefix(all_known_ids, "AS")
        next_b = format_next_id("B", max_b)
        next_as = format_next_id("AS", max_as)

        # Live site already has content but no B* IDs discovered → do not silently restart B01.
        if max_b == 0 and (wp_posts or any(tid.startswith("AS") for tid in reserved)):
            floor = os.environ.get("EXCALIBUR_TOPIC_ID_FLOOR") or os.environ.get("EXCALIBUR_B_ID_FLOOR") or ""
            if floor.strip():
                floor_ids |= extract_topic_ids(floor)
                max_b = max_num_for_prefix(all_known_ids | floor_ids, "B")
                next_b = format_next_id("B", max_b)
            else:
                print(
                    "WARN: no B* IDs in topics/ledger/articles/WP text, but live WP or AS* history exists. "
                    "Do not assume B01/B02. Set EXCALIBUR_TOPIC_ID_FLOOR=B0N after verifying WP, "
                    f"or use next AS id {next_as}."
                )
                next_b = "NEEDS_MANUAL_OR_FLOOR"

        # Prefer unwritten P0 in the active series; if B* already used and no free B P0 → next B*.
        preferred = ""
        prefer_prefix = "B" if max_b > 0 else ("AS" if max_as > 0 else "")
        for t in existing:
            if t["topic_id"] in reserved:
                continue
            if t.get("priority", "").upper() != "P0":
                continue
            if prefer_prefix and not t["topic_id"].upper().startswith(prefer_prefix):
                continue
            preferred = t["topic_id"]
            break
        if preferred:
            suggested = preferred
        elif prefer_prefix == "B" and next_b != "NEEDS_MANUAL_OR_FLOOR":
            suggested = next_b
        elif prefer_prefix == "AS":
            suggested = next_as
        elif next_b != "NEEDS_MANUAL_OR_FLOOR":
            suggested = next_b
        else:
            # Any remaining unwritten P0, else next AS
            for t in existing:
                if t["topic_id"] not in reserved and t.get("priority", "").upper() == "P0":
                    suggested = t["topic_id"]
                    break
            else:
                suggested = next_as

        print(f"Next available topic ID: {suggested}")
        print(f"Next B* ID (max known B={max_b}): {next_b}")
        print(f"Next AS* ID (max known AS={max_as}): {next_as}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Ledger reserved IDs: {sorted(published)}")
        print(f"WP topic IDs detected: {sorted(wp_ids)}")
        print(f"WP recent posts: {len(wp_posts)}")
        if wp_error:
            print(f"WP fetch note: {wp_error}")
        if floor_ids:
            print(f"Floor IDs from env: {sorted(floor_ids)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(
            args.check_query,
            existing,
            reserved,
            wp_posts=wp_posts,
            ledger_slugs=ledger_slugs | wp_slugs,
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
