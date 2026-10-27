#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
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
            # Flexible matching for bullet points with different formats
            m = re.search(rf"(?:-|\*)\s*\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
            if not m:
                # Fallback for plain bold key matching without lists
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


def public_site_base() -> str:
    for key in ("PUBLIC_SITE_URL", "WP_HOME", "WP_SITE_URL"):
        value = (os.environ.get(key) or "").strip().rstrip("/")
        if value and value not in {"[REDACTED]", "https://[REDACTED]", "http://[REDACTED]"}:
            return value
    return ""


def wp_rest_get(base: str, path: str, params: dict[str, str], timeout: float = 20.0) -> list[dict[str, Any]]:
    query = urllib.parse.urlencode(params)
    url = f"{base.rstrip('/')}{path}?{query}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ExcaliburBlogScout/1.0", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        raise RuntimeError(f"WP REST HTTP {exc.code} for {url}: {body[:200]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"WP REST network error for {url}: {exc}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"WP REST non-JSON response for {url}: {raw[:200]}") from exc
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        return [data]
    return []


def check_live_slugs(slugs: list[str], base: str) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    collisions = 0
    for slug in slugs:
        slug = slug.strip().strip("/")
        if not slug:
            continue
        posts = wp_rest_get(base, "/wp-json/wp/v2/posts", {"slug": slug, "per_page": "5", "_fields": "id,slug,link,status"})
        if posts:
            collisions += 1
            for post in posts:
                rows.append(
                    {
                        "check": "slug",
                        "query": slug,
                        "status": "TAKEN",
                        "id": post.get("id"),
                        "slug": post.get("slug"),
                        "link": post.get("link"),
                    }
                )
        else:
            rows.append({"check": "slug", "query": slug, "status": "FREE", "id": None, "slug": None, "link": None})
    return rows, collisions


def check_live_search(terms: list[str], base: str) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    collisions = 0
    for term in terms:
        term = term.strip()
        if not term:
            continue
        posts = wp_rest_get(
            base,
            "/wp-json/wp/v2/posts",
            {"search": term, "per_page": "10", "_fields": "id,slug,link,status,title"},
        )
        relevant = []
        term_l = term.lower()
        for post in posts:
            title = ""
            title_obj = post.get("title")
            if isinstance(title_obj, dict):
                title = str(title_obj.get("rendered") or "")
            slug = str(post.get("slug") or "")
            hay = f"{title} {slug}".lower()
            # Prefer dedicated hits (slug/title contains the term tokens), not broad blog noise.
            tokens = [t for t in re.split(r"\s+", term_l) if len(t) >= 3]
            if tokens and all(tok in hay for tok in tokens):
                relevant.append(post)
        if relevant:
            collisions += 1
            for post in relevant:
                title_obj = post.get("title") if isinstance(post.get("title"), dict) else {}
                rows.append(
                    {
                        "check": "search",
                        "query": term,
                        "status": "TAKEN",
                        "id": post.get("id"),
                        "slug": post.get("slug"),
                        "title": (title_obj or {}).get("rendered"),
                        "link": post.get("link"),
                    }
                )
        else:
            rows.append(
                {
                    "check": "search",
                    "query": term,
                    "status": "FREE",
                    "id": None,
                    "slug": None,
                    "title": None,
                    "link": None,
                    "raw_hits": len(posts),
                }
            )
    return rows, collisions


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--live-slugs",
        nargs="+",
        default=[],
        help="Check candidate slugs against LIVE WP REST /wp/v2/posts?slug=",
    )
    ap.add_argument(
        "--live-search",
        nargs="+",
        default=[],
        help="Search LIVE WP REST /wp/v2/posts?search= for model/topic collisions",
    )
    ap.add_argument(
        "--site-base",
        type=str,
        default="",
        help="Override PUBLIC_SITE_URL for LIVE WP checks",
    )
    args = ap.parse_args()

    # Reconfigure stdout for utf-8 on Windows
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    reserved = published | active
    existing = load_existing_topics(root)

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

    if args.live_slugs or args.live_search:
        base = (args.site_base or "").strip().rstrip("/") or public_site_base()
        if not base:
            print(
                "❌ LIVE DEDUP BLOCKER: PUBLIC_SITE_URL/WP_SITE_URL missing "
                "(or pass --site-base https://example.com)",
                file=sys.stderr,
            )
            return 2
        print("=== EXCALIBUR SCOUT LIVE DEDUP ===")
        print(f"site_base_configured: yes")
        rows: list[dict[str, Any]] = []
        collisions = 0
        if args.live_slugs:
            slug_rows, slug_hits = check_live_slugs(args.live_slugs, base)
            rows.extend(slug_rows)
            collisions += slug_hits
        if args.live_search:
            search_rows, search_hits = check_live_search(args.live_search, base)
            rows.extend(search_rows)
            collisions += search_hits
        for row in rows:
            status = row["status"]
            extra = ""
            if row.get("slug"):
                extra += f" slug={row['slug']}"
            if row.get("id") is not None:
                extra += f" id={row['id']}"
            if row.get("raw_hits") is not None and status == "FREE":
                extra += f" raw_hits={row['raw_hits']}"
            print(f"[{status}] {row['check']}={row['query']}{extra}")
        if collisions:
            print(f"❌ LIVE COLLISION: {collisions} taken check(s)")
            return 1
        print("✅ LIVE FREE: no slug/search collisions")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
