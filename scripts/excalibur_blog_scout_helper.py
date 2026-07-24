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
    r"##\s+((?:B|AS)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)\d+\s+—|\Z)",
    re.DOTALL | re.IGNORECASE,
)


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


def load_published_slugs(root: Path) -> set[str]:
    ledger_path = root / "shared/published-articles.md"
    slugs: set[str] = set()
    if not ledger_path.is_file():
        return slugs
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[4].lower() in {"published", "in_progress", "draft_ready"}:
            slug = cells[2].strip().lower()
            if slug:
                slugs.add(slug)
    return slugs


def load_active_article_topics(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = re.match(r"((?:B|AS)\d+)-", path.name, flags=re.IGNORECASE)
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


def fetch_recent_wp_slugs(site_url: str, limit: int = 30) -> tuple[set[str], str | None]:
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=slug,title",
    )
    request = Request(endpoint, headers={"User-Agent": "ExcaliburBlogAutomation/1.0"})
    try:
        with urlopen(request, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return set(), f"{type(exc).__name__}: {exc}"
    slugs = {str(item.get("slug") or "").strip().lower() for item in payload}
    return {s for s in slugs if s}, None


def max_b_number(*topic_id_sets: set[str] | list[str]) -> int:
    max_num = 0
    for group in topic_id_sets:
        for topic_id in group:
            m = re.match(r"B(\d+)$", str(topic_id).upper())
            if m:
                max_num = max(max_num, int(m.group(1)))
    return max_num


def next_b_topic_id(reserved: set[str], existing_ids: set[str]) -> str:
    max_num = max_b_number(reserved, existing_ids)
    candidate_num = max_num + 1
    while True:
        candidate = f"B{candidate_num:02d}"
        if candidate not in reserved:
            return candidate
        candidate_num += 1


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
    published_slugs = load_published_slugs(root)
    active = load_active_article_topics(root)
    reserved = set(published) | set(active)
    existing = load_existing_topics(root)
    existing_ids = {t["topic_id"] for t in existing}

    wp_note = ""
    site_url = (os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or "").strip()
    live_slugs: set[str] = set()
    if site_url:
        live_slugs, wp_error = fetch_recent_wp_slugs(site_url)
        if wp_error:
            wp_note = f"WP slug check skipped: {wp_error}"
        else:
            slug_to_topic = {t["slug"].lower(): t["topic_id"] for t in existing if t.get("slug")}
            for slug in live_slugs:
                if slug in slug_to_topic:
                    reserved.add(slug_to_topic[slug])
                if slug in published_slugs or slug in slug_to_topic:
                    continue
            # Live WP slug that matches a known published ledger slug reserves nothing extra;
            # orphan live posts still force B-series floor via max(B) from ledger/dirs.
            wp_note = f"WP recent slugs checked: {len(live_slugs)}"
            # If live site has a slug already in ledger under a B-id, reserved already has it.
            # If live has B01-era content not in topics pool, ledger must list it — see pitfalls.
    else:
        wp_note = "set PUBLIC_SITE_URL for live slug dedupe"

    # Any live slug that equals a topic slug marks that topic reserved (already done).
    # Also reserve topic_ids whose slug appears on live WP even if ledger missed them.
    for t in existing:
        slug = (t.get("slug") or "").lower()
        if slug and slug in live_slugs:
            reserved.add(t["topic_id"])

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        next_id = next_b_topic_id(reserved, existing_ids)
        as_topics = [t for t in existing if t["topic_id"].startswith("AS")]
        b_topics = [t for t in existing if t["topic_id"].startswith("B")]
        print(f"Next available topic ID: {next_id}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)} (B={len(b_topics)}, AS={len(as_topics)})")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Reserved topic IDs: {sorted(reserved)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        unwritten_as = [tid for tid in unwritten if tid.startswith("AS")]
        unwritten_b = [tid for tid in unwritten if tid.startswith("B")]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        print(f"Unwritten AS pool: {unwritten_as}")
        print(f"Unwritten B pool: {unwritten_b}")
        print(
            "NOTE: After AS→B migration / ledger reset, next B ID = max(B in topics+ledger+dirs)+1; "
            "never restart at B01 if live WP or ledger already used a B-series ID. "
            f"({wp_note})"
        )
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
