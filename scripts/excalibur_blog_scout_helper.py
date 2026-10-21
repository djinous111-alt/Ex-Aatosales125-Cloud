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


def load_wp_slug_denylist(root: Path) -> dict[str, Any]:
    path = root / "shared/wp-slug-denylist.json"
    if not path.is_file():
        return {"slugs": [], "path": str(path), "missing": True}
    data = json.loads(path.read_text(encoding="utf-8"))
    slugs = [str(s).strip() for s in (data.get("slugs") or []) if str(s).strip()]
    return {
        "slugs": slugs,
        "slug_set": {s.lower() for s in slugs},
        "updated_at": data.get("updated_at"),
        "recent_wp": data.get("recent_wp") or [],
        "do_not_rewrite_post_ids": data.get("do_not_rewrite_post_ids") or [],
        "path": "shared/wp-slug-denylist.json",
        "missing": False,
    }


def slug_denied(slug: str, denylist: dict[str, Any]) -> bool:
    return bool(slug) and slug.strip().lower() in (denylist.get("slug_set") or set())


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
    ap.add_argument("--check-slug", type=str, default="", help="Check candidate slug against shared/wp-slug-denylist.json")
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
    denylist = load_wp_slug_denylist(root)
    
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
        if denylist.get("missing"):
            print("❌ DENYLIST MISSING: shared/wp-slug-denylist.json — create/update before Scout picks a topic")
        else:
            recent = denylist.get("recent_wp") or []
            print(f"WP slug denylist: {len(denylist.get('slugs') or [])} slugs (updated_at={denylist.get('updated_at')})")
            print(f"Recent WP slugs (must avoid): {[r.get('slug') for r in recent[:12]]}")
            print(f"Do-not-rewrite post ids: {denylist.get('do_not_rewrite_post_ids')}")
        return 0 if not denylist.get("missing") else 1

    if args.check_slug:
        slug = args.check_slug.strip()
        if denylist.get("missing"):
            print("❌ DENYLIST MISSING: shared/wp-slug-denylist.json")
            return 1
        if slug_denied(slug, denylist):
            print(f"❌ SLUG DENYLIST HIT: '{slug}' is already on live/recent WP or ledger")
            return 1
        print(f"✅ SLUG FREE: '{slug}' not in wp-slug-denylist.json")
        return 0
        
    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | Topic: {w['topic_id']} ({w['status']})")
                print(f"  Message: {w['message']}")
            return 1
        # Also flag if query tokens clearly match a denylisted slug stem
        q_tokens = normalize_and_tokenize(args.check_query)
        for slug in denylist.get("slugs") or []:
            slug_tokens = normalize_and_tokenize(slug.replace("-", " "))
            if q_tokens and slug_tokens and len(q_tokens.intersection(slug_tokens)) >= max(3, len(slug_tokens) // 3):
                print(f"❌ DENYLIST OVERLAP: query looks close to live slug '{slug}'")
                return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        return 0

    ap.print_help()
    return 0

if __name__ == "__main__":
    sys.exit(main())
