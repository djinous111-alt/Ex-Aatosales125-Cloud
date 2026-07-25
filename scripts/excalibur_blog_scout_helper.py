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

def project_root() -> Path:
    return Path(__file__).resolve().parents[1]

TOPIC_ID_RE = re.compile(r"\bB(\d+)\b", flags=re.IGNORECASE)


def parse_b_num(topic_id: str) -> int | None:
    match = re.fullmatch(r"B(\d+)", topic_id.strip().upper())
    if not match:
        return None
    return int(match.group(1))


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
        # Accept Bxx-* and AS-era dirs that embed a B watermark in name only when B-prefixed.
        match = re.match(r"(B\d+)-", path.name, flags=re.IGNORECASE)
        if match:
            active.add(match.group(1).upper())
    return active


def load_floor_watermark(root: Path) -> int:
    """Highest known B-number from floor config + optional env (live WP hint)."""
    floor = 0
    floor_path = root / "memory" / "scout-topic-id-floor.json"
    if floor_path.is_file():
        try:
            data = json.loads(floor_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
        for key in ("watermark_b_num", "min_used_b_num", "floor_b_num"):
            raw = data.get(key)
            if isinstance(raw, int) and raw > floor:
                floor = raw
        recent = data.get("recent_wp_topic_ids") or data.get("topic_ids") or []
        if isinstance(recent, list):
            for item in recent:
                num = parse_b_num(str(item))
                if num is not None and num > floor:
                    floor = num
    env_floor = (os.environ.get("EXCALIBUR_TOPIC_ID_FLOOR") or "").strip()
    if env_floor.isdigit():
        floor = max(floor, int(env_floor))
    elif parse_b_num(env_floor) is not None:
        floor = max(floor, int(parse_b_num(env_floor) or 0))
    recent_env = (os.environ.get("EXCALIBUR_RECENT_WP_TOPIC_IDS") or "").strip()
    if recent_env:
        for token in re.split(r"[\s,;]+", recent_env):
            num = parse_b_num(token)
            if num is not None and num > floor:
                floor = num
    return floor


def max_b_num_from_ids(ids: set[str] | list[str]) -> int:
    max_num = 0
    for topic_id in ids:
        num = parse_b_num(str(topic_id))
        if num is not None:
            max_num = max(max_num, num)
    return max_num


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
        pool_max = max_b_num_from_ids([t["topic_id"] for t in existing])
        reserved_max = max_b_num_from_ids(reserved)
        ledger_ids = set(published)
        ledger_path = root / "shared/published-articles.md"
        if ledger_path.is_file():
            for match in TOPIC_ID_RE.finditer(ledger_path.read_text(encoding="utf-8")):
                ledger_ids.add(f"B{int(match.group(1))}")
        ledger_max = max_b_num_from_ids(ledger_ids)
        floor_max = load_floor_watermark(root)
        max_num = max(pool_max, reserved_max, ledger_max, floor_max)

        next_id = f"B{max_num + 1:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"ID floor sources: pool={pool_max} articles={reserved_max} ledger={ledger_max} floor_cfg/env={floor_max}")
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
