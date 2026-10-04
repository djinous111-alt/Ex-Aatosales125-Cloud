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


def load_live_wp_posts(root: Path) -> list[dict[str, str]]:
    """Load live WP slug/title snapshots so Scout sees posts after ledger reset."""
    blog_dir = root / "memory" / "blog"
    if not blog_dir.is_dir():
        return []
    posts: list[dict[str, str]] = []
    seen_slugs: set[str] = set()
    for path in sorted(blog_dir.glob("published-live-*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for item in data.get("posts") or []:
            slug = str(item.get("slug") or "").strip().lower()
            title = str(item.get("title") or "").strip()
            if not slug or slug in seen_slugs:
                continue
            seen_slugs.add(slug)
            posts.append({
                "slug": slug,
                "title": title,
                "source": path.name,
                "topic_id": f"LIVE:{slug[:24]}",
                "primary_query": title or slug,
            })
    return posts

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
        if str(t.get("topic_id", "")).startswith("LIVE:"):
            status = "live_wp"
        
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


def check_live_slug(slug: str, live_posts: list[dict[str, str]]) -> list[dict[str, Any]]:
    slug_norm = slug.strip().lower().strip("/")
    if not slug_norm:
        return []
    warnings: list[dict[str, Any]] = []
    for post in live_posts:
        live_slug = post["slug"]
        if live_slug == slug_norm:
            warnings.append({
                "severity": "CRITICAL",
                "topic_id": post["topic_id"],
                "similarity": 1.0,
                "status": "live_wp",
                "message": (
                    f"EXACT live WP slug match: '{live_slug}' "
                    f"(source={post.get('source')}, title='{post.get('title')}')"
                ),
            })
            continue
        # Token overlap on slug fragments (sbkts-i-epts vs sbkts epts ...)
        sim_tokens_a = normalize_and_tokenize(slug_norm.replace("-", " "))
        sim_tokens_b = normalize_and_tokenize(live_slug.replace("-", " "))
        if not sim_tokens_a or not sim_tokens_b:
            continue
        intersection = len(sim_tokens_a.intersection(sim_tokens_b))
        union = len(sim_tokens_a.union(sim_tokens_b))
        similarity = intersection / union if union else 0.0
        if similarity >= 0.55:
            warnings.append({
                "severity": "WARNING",
                "topic_id": post["topic_id"],
                "similarity": round(similarity, 2),
                "status": "live_wp",
                "message": (
                    f"High slug overlap ({round(similarity * 100)}%) with live WP "
                    f"'{live_slug}' (source={post.get('source')})"
                ),
            })
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--check-slug",
        type=str,
        default="",
        help="Check proposed slug against memory/blog/published-live-*.json",
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
    live_posts = load_live_wp_posts(root)
    # Treat live titles as extra overlap targets for --check-query
    existing_with_live = existing + [
        {
            "topic_id": p["topic_id"],
            "primary_query": p["title"] or p["slug"],
            "slug": p["slug"],
            "priority": "live",
        }
        for p in live_posts
    ]
    
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
        print(f"Live WP slugs loaded: {len(live_posts)} (memory/blog/published-live-*.json)")
        print(f"Active article dirs: {sorted(active)}")
        
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0
        
    if args.check_query or args.check_slug:
        warnings: list[dict[str, Any]] = []
        if args.check_query:
            warnings.extend(check_overlap(args.check_query, existing_with_live, reserved))
        if args.check_slug:
            warnings.extend(check_live_slug(args.check_slug, live_posts))
        elif args.check_query:
            # Derive a slug-ish form from the query for live slug audit when --check-slug omitted
            approx_slug = re.sub(r"[^\w\s-]", "", args.check_query.lower())
            approx_slug = re.sub(r"[\s_]+", "-", approx_slug).strip("-")
            if approx_slug:
                warnings.extend(check_live_slug(approx_slug, live_posts))
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | Topic: {w['topic_id']} ({w['status']})")
                print(f"  Message: {w['message']}")
            return 1
        print(
            f"✅ NO CANNIBALIZATION RISK: Query/slug is clean "
            f"(checked pool + {len(live_posts)} live WP slugs)."
        )
        return 0

    ap.print_help()
    return 0

if __name__ == "__main__":
    sys.exit(main())
