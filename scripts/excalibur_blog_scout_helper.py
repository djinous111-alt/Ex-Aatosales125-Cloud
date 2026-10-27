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
                    "message": f"High overlap ({round(similarity*100)}%) with topic {t['topic_id']} ({status}). Query: '{t['primary_query']}'",
                }
            )
    return warnings


def site_base_from_env() -> str:
    return (
        os.environ.get("PUBLIC_SITE_URL")
        or os.environ.get("WP_HOME")
        or os.environ.get("WP_SITE_URL")
        or ""
    ).rstrip("/")


def _wp_get_json(url: str, *, timeout: float = 20.0) -> Any:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ExcaliburBlogScout/1.0", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def check_live_slugs(site_base: str, slugs: list[str]) -> dict[str, Any]:
    """Check WP REST for exact slug availability. Prefer LIVE over ledger after reset."""
    base = site_base.rstrip("/")
    results: list[dict[str, Any]] = []
    for slug in slugs:
        slug = slug.strip().strip("/")
        if not slug:
            continue
        api = f"{base}/wp-json/wp/v2/posts?slug={urllib.parse.quote(slug)}&per_page=5&_fields=id,slug,link,status"
        entry: dict[str, Any] = {"slug": slug, "busy": False, "posts": [], "error": None}
        try:
            posts = _wp_get_json(api)
            if not isinstance(posts, list):
                posts = []
            entry["posts"] = [
                {"id": p.get("id"), "slug": p.get("slug"), "status": p.get("status"), "link": p.get("link")}
                for p in posts
                if isinstance(p, dict)
            ]
            entry["busy"] = bool(entry["posts"])
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            entry["error"] = f"{type(exc).__name__}: {exc}"
        results.append(entry)

    busy = [r["slug"] for r in results if r.get("busy")]
    free = [r["slug"] for r in results if not r.get("busy") and not r.get("error")]
    errored = [r["slug"] for r in results if r.get("error")]
    return {
        "site_base_configured": bool(base),
        "checked": len(results),
        "busy_slugs": busy,
        "free_slugs": free,
        "error_slugs": errored,
        "results": results,
    }


def live_search(site_base: str, query: str, *, per_page: int = 10) -> dict[str, Any]:
    """WP REST search by title/content keywords (Cyrillic/Latin)."""
    base = site_base.rstrip("/")
    api = (
        f"{base}/wp-json/wp/v2/posts?"
        f"search={urllib.parse.quote(query)}&per_page={per_page}&_fields=id,slug,title,link,status"
    )
    try:
        posts = _wp_get_json(api)
        if not isinstance(posts, list):
            posts = []
        rows = []
        for p in posts:
            if not isinstance(p, dict):
                continue
            title = p.get("title") or {}
            rendered = title.get("rendered") if isinstance(title, dict) else str(title or "")
            rows.append(
                {
                    "id": p.get("id"),
                    "slug": p.get("slug"),
                    "title": rendered,
                    "status": p.get("status"),
                    "link": p.get("link"),
                }
            )
        return {"query": query, "count": len(rows), "posts": rows, "error": None}
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        return {"query": query, "count": 0, "posts": [], "error": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--live-slugs",
        type=str,
        default="",
        help="Comma-separated slugs to check against PUBLIC_SITE_URL WP REST (exact slug)",
    )
    ap.add_argument(
        "--live-search",
        type=str,
        default="",
        help="Search LIVE WP posts by keyword (title/content) via REST",
    )
    ap.add_argument(
        "--site-base",
        type=str,
        default="",
        help="Override PUBLIC_SITE_URL for LIVE checks",
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
    site_base = (args.site_base or site_base_from_env()).rstrip("/")

    if args.live_slugs:
        if not site_base:
            print("BLOCKER: PUBLIC_SITE_URL / --site-base required for --live-slugs", file=sys.stderr)
            return 2
        slugs = [s.strip() for s in args.live_slugs.split(",") if s.strip()]
        report = check_live_slugs(site_base, slugs)
        print("=== EXCALIBUR SCOUT LIVE SLUGS ===")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["busy_slugs"]:
            print(f"BUSY: {', '.join(report['busy_slugs'])}")
        if report["free_slugs"]:
            print(f"FREE: {', '.join(report['free_slugs'])}")
        if report["error_slugs"]:
            print(f"ERROR: {', '.join(report['error_slugs'])}", file=sys.stderr)
            return 2
        # Exit 1 if any requested slug is already LIVE (denylist hit)
        return 1 if report["busy_slugs"] else 0

    if args.live_search:
        if not site_base:
            print("BLOCKER: PUBLIC_SITE_URL / --site-base required for --live-search", file=sys.stderr)
            return 2
        report = live_search(site_base, args.live_search)
        print("=== EXCALIBUR SCOUT LIVE SEARCH ===")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report.get("error"):
            print(f"ERROR: {report['error']}", file=sys.stderr)
            return 2
        return 0 if report["count"] == 0 else 1

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
        print("NOTE: After ledger reset prefer --live-slugs / --live-search against PUBLIC_SITE_URL over ledger-only dedupe.")
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
