#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def public_site_base() -> str:
    """Authoritative Avto-Sales site for WP inventory (not MCP-KV WordPress host)."""
    for key in ("PUBLIC_SITE_URL", "WP_HOME", "WP_SITE_URL"):
        value = (os.environ.get(key) or "").strip().rstrip("/")
        if value.startswith(("http://", "https://")):
            return value
    return ""


def fetch_live_wp_slugs(site_base: str, *, per_page: int = 100, max_pages: int = 20) -> list[str]:
    """List published post slugs via PUBLIC_SITE_URL/wp-json (prefer over MCP WP tools)."""
    base = site_base.rstrip("/")
    slugs: list[str] = []
    for page in range(1, max_pages + 1):
        url = f"{base}/wp-json/wp/v2/posts?per_page={per_page}&page={page}&status=publish&_fields=slug"
        req = urllib.request.Request(url, headers={"User-Agent": "ExcaliburBlogScoutHelper/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 400:
                break
            raise
        if not isinstance(payload, list) or not payload:
            break
        for item in payload:
            slug = str((item or {}).get("slug") or "").strip()
            if slug:
                slugs.append(slug)
        if len(payload) < per_page:
            break
    return slugs

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
            
        topics.append({
            "topic_id": topic_id,
            "primary_query": field("primary_query"),
            "slug": field("slug"),
            "priority": field("priority"),
        })
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
            warnings.append({
                "severity": "CRITICAL",
                "topic_id": t["topic_id"],
                "similarity": 1.0,
                "status": status,
                "message": f"EXACT MATCH found with topic {t['topic_id']} ({status})! Primary query: '{t['primary_query']}'"
            })
        elif similarity >= 0.35:
            warnings.append({
                "severity": "WARNING",
                "topic_id": t["topic_id"],
                "similarity": round(similarity, 2),
                "status": status,
                "message": f"High overlap ({round(similarity*100)}%) with topic {t['topic_id']} ({status}). Query: '{t['primary_query']}'"
            })
    return warnings

def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--live-wp-slugs",
        action="store_true",
        help="List published slugs from PUBLIC_SITE_URL/wp-json (authoritative; ignore MCP WP host)",
    )
    ap.add_argument("--check-slug", type=str, default="", help="Exit 1 if slug already exists on live WP")
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

    if args.live_wp_slugs or args.check_slug:
        site = public_site_base()
        if not site:
            print("❌ PUBLIC_SITE_URL (or WP_HOME/WP_SITE_URL) required for live WP inventory", file=sys.stderr)
            return 2
        print("=== EXCALIBUR SCOUT LIVE WP ===")
        print("source: PUBLIC_SITE_URL/wp-json (do not trust MCP-KV wordpress_* for Avto-Sales dedupe)")
        try:
            slugs = fetch_live_wp_slugs(site)
        except Exception as exc:  # noqa: BLE001
            print(f"❌ live WP inventory failed: {exc}", file=sys.stderr)
            return 1
        print(f"published_posts={len(slugs)}")
        if args.live_wp_slugs:
            for slug in slugs:
                print(slug)
        if args.check_slug:
            needle = args.check_slug.strip().lower()
            if needle in {s.lower() for s in slugs}:
                print(f"❌ SLUG EXISTS on live WP: {args.check_slug}")
                return 1
            print(f"✅ slug available on live WP: {args.check_slug}")
        return 0
    
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

    ap.print_help()
    return 0

if __name__ == "__main__":
    sys.exit(main())
