#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from html import unescape
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from urllib.request import Request, urlopen


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


def fetch_live_wp_posts(site_url: str, limit: int = 40) -> tuple[list[dict[str, str]], str | None]:
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=date,link,slug,title",
    )
    request = Request(endpoint, headers={"User-Agent": "ExcaliburBlogScout/1.0"})
    try:
        with urlopen(request, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [], f"{type(exc).__name__}: {exc}"

    posts: list[dict[str, str]] = []
    for item in payload:
        title = item.get("title", {}).get("rendered", "") if isinstance(item.get("title"), dict) else ""
        title = re.sub(r"<[^>]+>", "", title)
        posts.append(
            {
                "date": str(item.get("date", ""))[:10],
                "slug": str(item.get("slug", "")),
                "title": unescape(title).strip(),
                "link": str(item.get("link", "")),
            }
        )
    return posts, None


def check_live_wp_overlap(query: str, posts: list[dict[str, str]], threshold: float = 0.35) -> list[dict[str, Any]]:
    """Compare query tokens against live WP titles/slugs (not only local memory).

    Uses title-focused Jaccard (slug tokens are Latin and dilute RU queries) plus
    a significant-stem overlap rule: ≥2 stems of length≥4 shared with the title
    counts as near-duplicate for how-to topics.
    """
    query_tokens = normalize_and_tokenize(query)
    if not query_tokens:
        return []
    # Generic niche tokens match almost every post title — exclude from stem rule.
    weak_stems = {
        "авто",
        "машин",
        "год",
        "2026",
        "2025",
        "чекли",
        "чек-л",
        "под",
        "заказ",
        "из",
        "при",
        "для",
    }
    significant = {t for t in query_tokens if len(t) >= 4 and t not in weak_stems}
    warnings: list[dict[str, Any]] = []
    for post in posts:
        title = post.get("title", "")
        slug = post.get("slug", "")
        title_tokens = normalize_and_tokenize(title)
        slug_tokens = normalize_and_tokenize(slug.replace("-", " "))
        if not title_tokens and not slug_tokens:
            continue

        # Title-only Jaccard — primary signal for RU how-to queries.
        inter_title = query_tokens.intersection(title_tokens)
        union_title = query_tokens.union(title_tokens) if title_tokens else set()
        similarity = (len(inter_title) / len(union_title)) if union_title else 0.0

        stem_hits = significant.intersection(title_tokens)
        stem_hit = len(stem_hits) >= 2

        slug_l = slug.lower()
        query_l = query.lower()
        # Paired RU-intent ↔ latin-slug signals (avoid single-token false positives).
        latin_pairs = (
            (("читать", "аукцион"), ("chitat", "aukcion")),
            (("читать", "аукцион"), ("chitat", "auktsion")),
            (("аукционн", "лист"), ("aukcion", "list")),
            (("аукционн", "лист"), ("auktsion", "list")),
            (("encar",), ("encar",)),
            (("растамож",), ("rastamozh",)),
            (("утильсбор",), ("utilsbor",)),
        )
        latin_hit = False
        for ru_parts, lat_parts in latin_pairs:
            if all(part in query_l for part in ru_parts) and all(part in slug_l for part in lat_parts):
                latin_hit = True
                break

        if similarity >= threshold or stem_hit or latin_hit:
            severity = "CRITICAL" if similarity >= 0.5 or stem_hit or latin_hit else "WARNING"
            warnings.append(
                {
                    "severity": severity,
                    "similarity": round(similarity, 2),
                    "slug": slug,
                    "title": title,
                    "link": post.get("link", ""),
                    "message": (
                        f"Live WP near-duplicate: slug={slug!r} title={title!r} "
                        f"(title_jaccard={round(similarity * 100)}%, stem_hits={sorted(stem_hits)}). "
                        "Prefer update/refresh, not a new gap claim."
                    ),
                }
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--check-live-wp",
        type=str,
        default="",
        help="Check query against live WP REST titles/slugs (requires PUBLIC_SITE_URL)",
    )
    ap.add_argument("--site-base", type=str, default="", help="Override PUBLIC_SITE_URL for --check-live-wp")
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

    if args.check_live_wp:
        site = (
            args.site_base.strip()
            or os.environ.get("PUBLIC_SITE_URL", "").strip()
            or os.environ.get("WP_SITE_URL", "").strip()
        )
        if not site:
            print("WARN: PUBLIC_SITE_URL/WP_SITE_URL missing — cannot check live WP", file=sys.stderr)
            return 2
        posts, error = fetch_live_wp_posts(site)
        if error:
            print(f"WARN: live WP fetch failed: {error}", file=sys.stderr)
            return 2
        warnings = check_live_wp_overlap(args.check_live_wp, posts)
        if warnings:
            print("❌ LIVE WP NEAR-DUPLICATE DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | slug={w['slug']}")
                print(f"  Message: {w['message']}")
            return 1
        print(f"✅ LIVE WP CLEAN: no near-duplicate among {len(posts)} recent posts.")
        return 0

    ap.print_help()
    return 0

if __name__ == "__main__":
    sys.exit(main())
