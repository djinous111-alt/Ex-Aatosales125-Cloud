#!/usr/bin/env python3
"""Helper script for Excalibur BLOG Scout Agent to find next IDs and avoid keyword cannibalization."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# AVTO SALES uses AS##; Cursor/Make niche uses B##. Both must parse.
TOPIC_ID_PREFIX_RE = r"(?:AS|B)"
TOPIC_ID_RE = rf"{TOPIC_ID_PREFIX_RE}\d+"
TOPIC_DIR_RE = re.compile(rf"^({TOPIC_ID_RE})-", re.IGNORECASE)
TOPIC_CARD_RE = re.compile(
    rf"##\s+({TOPIC_ID_RE})\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+{TOPIC_ID_PREFIX_RE}|\Z)",
    re.DOTALL | re.IGNORECASE,
)
TOPIC_NUM_RE = re.compile(rf"^({TOPIC_ID_PREFIX_RE})(\d+)$", re.IGNORECASE)


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
        match = TOPIC_DIR_RE.match(path.name)
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


def load_denylist_slugs(root: Path) -> tuple[set[str], str | None]:
    """Load LIVE slug denylist. Returns (slugs, error) where error is missing|empty|invalid."""
    path = root / "shared/wp-slug-denylist.json"
    if not path.is_file():
        return set(), "missing"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set(), "invalid"
    raw = data.get("slugs") if isinstance(data, dict) else data
    if not isinstance(raw, list):
        return set(), "invalid"
    slugs = {str(s).strip().lower() for s in raw if str(s).strip()}
    if not slugs:
        return set(), "empty"
    return slugs, None


def slugify_candidate(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text


def check_denylist_slug(slug: str, denylist: set[str]) -> list[dict[str, Any]]:
    needle = slug.strip().lower()
    if not needle:
        return []
    if needle in denylist:
        return [
            {
                "severity": "CRITICAL",
                "topic_id": "denylist",
                "similarity": 1.0,
                "status": "wp_live",
                "message": f"EXACT denylist slug collision: '{needle}'",
            }
        ]
    return []


def check_denylist_query(query: str, denylist: set[str]) -> list[dict[str, Any]]:
    """Exact match when query is already a kebab slug; also slugified form."""
    q = query.strip().lower()
    hits = check_denylist_slug(q, denylist)
    if hits:
        return hits
    slugified = slugify_candidate(q)
    if slugified and slugified != q:
        return check_denylist_slug(slugified, denylist)
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--check-slug",
        type=str,
        default="",
        help="Check proposed article slug against shared/wp-slug-denylist.json",
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
        max_by_prefix: dict[str, int] = {}
        for t in existing:
            m = TOPIC_NUM_RE.match(t["topic_id"])
            if m:
                prefix = m.group(1).upper()
                max_by_prefix[prefix] = max(max_by_prefix.get(prefix, 0), int(m.group(2)))
        # Prefer AS when the pool has AVTO SALES cards; otherwise B (legacy niche).
        if "AS" in max_by_prefix:
            next_id = f"AS{max_by_prefix['AS'] + 1:02d}"
        elif "B" in max_by_prefix:
            next_id = f"B{max_by_prefix['B'] + 1:02d}"
        else:
            next_id = "AS01"
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        
        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        denylist, denylist_err = load_denylist_slugs(root)
        if denylist_err:
            print(f"Denylist: {denylist_err} (restore shared/wp-slug-denylist.json before append)")
        else:
            print(f"Denylist slugs loaded: {len(denylist)}")
        return 0
        
    if args.check_query or args.check_slug:
        denylist, denylist_err = load_denylist_slugs(root)
        if denylist_err:
            print(
                f"❌ DENYLIST BLOCKER: shared/wp-slug-denylist.json is {denylist_err}. "
                "Restore/rebuild from published-live + ledger before scout append "
                "(WP REST SSL timeout is expected; do not invent slugs)."
            )
            return 2

        warnings: list[dict[str, Any]] = []
        if args.check_query:
            warnings.extend(check_overlap(args.check_query, existing, reserved))
            warnings.extend(check_denylist_query(args.check_query, denylist))
        if args.check_slug:
            warnings.extend(check_denylist_slug(args.check_slug, denylist))
            # Also flag pool slug collisions.
            needle = args.check_slug.strip().lower()
            for t in existing:
                if (t.get("slug") or "").strip().lower() == needle:
                    warnings.append(
                        {
                            "severity": "CRITICAL",
                            "topic_id": t["topic_id"],
                            "similarity": 1.0,
                            "status": "in_pool",
                            "message": f"EXACT pool slug collision with {t['topic_id']}: '{needle}'",
                        }
                    )

        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | Topic: {w['topic_id']} ({w['status']})")
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query/slug is clean vs pool + denylist.")
        return 0

    ap.print_help()
    return 0

if __name__ == "__main__":
    sys.exit(main())
