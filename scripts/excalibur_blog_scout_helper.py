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


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def b_num(topic_id: str) -> int | None:
    match = re.match(r"B(\d+)$", topic_id.strip().upper())
    return int(match.group(1)) if match else None


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


def load_ledger_slug_map(root: Path) -> dict[str, str]:
    """slug -> topic_id from published-articles.md."""
    ledger_path = root / "shared/published-articles.md"
    mapping: dict[str, str] = {}
    if not ledger_path.is_file():
        return mapping
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[4].lower() in {"published", "in_progress", "draft_ready"}:
            mapping[cells[2].strip().lower()] = cells[1].upper()
    return mapping


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
            continue
        meta = path / "article.meta.json"
        if meta.is_file():
            try:
                data = json.loads(meta.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            tid = str(data.get("topic_id") or "").upper()
            if b_num(tid) is not None:
                active.add(tid)
    return active


def load_slug_to_topic_from_articles(root: Path) -> dict[str, str]:
    articles_dir = root / "memory" / "blog" / "articles"
    mapping: dict[str, str] = {}
    if not articles_dir.is_dir():
        return mapping
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = re.match(r"(B\d+)-(.+)$", path.name, flags=re.IGNORECASE)
        if match:
            mapping[match.group(2).lower()] = match.group(1).upper()
    return mapping


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


def fetch_wp_slugs(site_url: str, limit: int = 40) -> tuple[list[dict[str, str]], str | None]:
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=slug,title",
    )
    request = Request(endpoint, headers={"User-Agent": "ExcaliburBlogAutomation/1.0"})
    try:
        with urlopen(request, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [], f"{type(exc).__name__}: {exc}"

    posts: list[dict[str, str]] = []
    for item in payload:
        title = item.get("title", {}).get("rendered", "") if isinstance(item.get("title"), dict) else ""
        title = re.sub(r"<[^>]+>", "", str(title))
        posts.append({"slug": str(item.get("slug", "")).lower(), "title": title})
    return posts, None


def collect_wp_topic_ids(
    posts: list[dict[str, str]],
    slug_to_topic: dict[str, str],
) -> tuple[set[str], list[str]]:
    """Resolve WP posts to B* topic ids; return (ids, untracked_slugs)."""
    found: set[str] = set()
    untracked: list[str] = []
    for post in posts:
        slug = post.get("slug", "").strip().lower()
        title = post.get("title", "")
        if slug and slug in slug_to_topic:
            found.add(slug_to_topic[slug])
            continue
        title_hit = re.search(r"\b(B\d{2,})\b", title, flags=re.IGNORECASE)
        if title_hit:
            found.add(title_hit.group(1).upper())
            continue
        if slug:
            untracked.append(slug)
    return found, untracked


def max_b_across(*id_sets: set[str] | list[str]) -> int:
    max_num = 0
    for group in id_sets:
        for tid in group:
            num = b_num(str(tid))
            if num is not None:
                max_num = max(max_num, num)
    return max_num


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
                        f"High overlap ({round(similarity * 100)}%) with topic {t['topic_id']} ({status}). "
                        f"Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--skip-wp",
        action="store_true",
        help="Do not fetch live WP posts for B* high-water (default: fetch when PUBLIC_SITE_URL set)",
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
    existing_ids = {t["topic_id"] for t in existing}

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")

        slug_map = load_ledger_slug_map(root)
        slug_map.update(load_slug_to_topic_from_articles(root))

        wp_ids: set[str] = set()
        untracked: list[str] = []
        wp_note = ""
        site_url = (
            os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or ""
        ).strip()
        if not args.skip_wp and site_url:
            posts, error = fetch_wp_slugs(site_url)
            if error:
                wp_note = f"WP fetch failed: {error}"
            else:
                wp_ids, untracked = collect_wp_topic_ids(posts, slug_map)
                if untracked:
                    wp_note = (
                        f"WP has {len(untracked)} slug(s) not mapped to local B* "
                        f"(ledger incomplete?). Do not trust suggest-next alone; "
                        f"sync shared/published-articles.md. sample={untracked[:5]}"
                    )
        elif not site_url:
            wp_note = "set PUBLIC_SITE_URL for live WP B* high-water / dedupe"

        floor_env = os.environ.get("EXCALIBUR_B_ID_FLOOR", "").strip()
        floor = int(floor_env) if floor_env.isdigit() else 0

        max_num = max_b_across(existing_ids, reserved, wp_ids)
        max_num = max(max_num, floor)

        # If WP has untracked posts and local B* history is empty/low, bump conservatively
        # by untracked count so we do not restart at B01 after a ledger reset.
        if untracked and max_num == 0:
            max_num = len(untracked)
            wp_note = (
                (wp_note + " | ") if wp_note else ""
            ) + f"empty local B* + {len(untracked)} untracked WP → floor={max_num}"

        next_id = f"B{max_num + 1:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"B* high-water (topics+ledger+articles+wp+floor): {max_num}")
        if floor:
            print(f"EXCALIBUR_B_ID_FLOOR={floor}")
        print(f"Total topics in pool (blog-topics.md): {len(existing)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")
        print(f"Ledger B*/status reserved: {sorted(published)}")
        if wp_ids:
            print(f"WP-mapped B* ids: {sorted(tid for tid in wp_ids if b_num(tid) is not None)}")
            other = sorted(tid for tid in wp_ids if b_num(tid) is None)
            if other:
                print(f"WP-mapped non-B ids (ignored for high-water): {other}")
        if wp_note:
            print(f"WP_NOTE: {wp_note}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved)
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(
                    f"  [{w['severity']}] Similarity: {w['similarity']} | "
                    f"Topic: {w['topic_id']} ({w['status']})"
                )
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
