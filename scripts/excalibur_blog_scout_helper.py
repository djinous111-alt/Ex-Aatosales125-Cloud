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
        match = re.match(r"([A-Z]+\d+)-", path.name, flags=re.IGNORECASE)
        if match:
            active.add(match.group(1).upper())
    return active


def load_live_posts(root: Path) -> list[dict[str, str]]:
    """Load live WP slug/title snapshot(s) under memory/blog/published-live*.json."""
    blog_dir = root / "memory" / "blog"
    if not blog_dir.is_dir():
        return []
    posts: list[dict[str, str]] = []
    for path in sorted(blog_dir.glob("published-live*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for item in data.get("posts") or []:
            slug = str(item.get("slug") or "").strip()
            title = str(item.get("title") or "").strip()
            if not slug and not title:
                continue
            posts.append(
                {
                    "slug": slug,
                    "title": title,
                    "source": path.name,
                }
            )
    return posts


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    """Load AS*/B* (and similar) topic cards from blog-topics.md."""
    topics_path = root / "memory/topics/blog-topics.md"
    topics: list[dict[str, str]] = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    pattern = r"##\s+([A-Z]+\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+[A-Z]+\d+|\Z)"
    for match in re.finditer(pattern, text, re.DOTALL):
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
                "h1": field("h1"),
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
        if not w_clean or w_clean in {"в", "на", "и", "или", "с", "по", "для", "как", "что", "это", "из", "а", "к", "до"}:
            continue
        tokens.add(w_clean[:5] if len(w_clean) > 4 else w_clean)
    return tokens


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a.intersection(b)) / len(a.union(b))


_SLUG_STOP = {
    "na",
    "iz",
    "i",
    "dlya",
    "do",
    "pod",
    "bez",
    "kak",
    "chto",
    "ili",
    "v",
    "s",
    "po",
    "ot",
    "the",
    "a",
    "and",
}


def slug_core_parts(slug: str) -> list[str]:
    parts = []
    for part in (slug or "").lower().strip("/").split("-"):
        if not part or part in _SLUG_STOP or part.isdigit():
            continue
        parts.append(part)
    return parts


def slug_similarity(a: str, b: str) -> float:
    """Exact / prefix / distinctive-token overlap for WP slugs (live often longer)."""
    a = (a or "").strip().lower().strip("/")
    b = (b or "").strip().lower().strip("/")
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    shorter, longer = (a, b) if len(a) <= len(b) else (b, a)
    if len(shorter) >= 12 and longer.startswith(shorter):
        return 0.92
    if len(shorter) >= 16 and shorter in longer:
        return 0.85
    a_core = slug_core_parts(a)
    b_core = slug_core_parts(b)
    prefix = 0
    for left, right in zip(a_core, b_core):
        if left != right:
            break
        prefix += 1
    # Require 3 distinctive tokens (avto+korei alone is too generic).
    if prefix >= 3:
        return 0.9
    shorter_c, longer_c = (a_core, b_core) if len(a_core) <= len(b_core) else (b_core, a_core)
    if len(shorter_c) >= 3 and set(shorter_c).issubset(set(longer_c)):
        return 0.88
    if prefix >= 2 and a_core and a_core[0] not in {"avto", "mashiny", "mashina", "kitajskie", "yaponskie"}:
        return 0.85
    # Weak geographic-year overlap alone must not look like the same article.
    return jaccard(set(a_core), set(b_core))


def topic_live_status(topic: dict[str, str], live_posts: list[dict[str, str]]) -> dict[str, Any] | None:
    """Return best live overlap for a topic card, if any."""
    best: dict[str, Any] | None = None
    topic_blob = " ".join(
        [
            topic.get("primary_query") or "",
            topic.get("h1") or "",
            (topic.get("slug") or "").replace("-", " "),
        ]
    )
    topic_tokens = normalize_and_tokenize(topic_blob)
    topic_head = slug_core_parts(topic.get("slug") or "")[:2]
    for post in live_posts:
        slug_sim = slug_similarity(topic.get("slug") or "", post.get("slug") or "")
        title_sim = jaccard(
            topic_tokens,
            normalize_and_tokenize(f"{post.get('title', '')} {post.get('slug', '').replace('-', ' ')}"),
        )
        # Prefer strong slug signal; title-only needs higher bar.
        if slug_sim >= 0.8:
            score = slug_sim
        elif slug_sim >= 0.55 and title_sim >= 0.25:
            score = max(slug_sim, (slug_sim + title_sim) / 2)
        elif title_sim >= 0.5 and (not topic_head or set(topic_head) & set(slug_core_parts(post.get("slug") or ""))):
            score = title_sim
        else:
            score = 0.0
        if score < 0.55:
            continue
        candidate = {
            "score": round(score, 2),
            "slug_sim": round(slug_sim, 2),
            "title_sim": round(title_sim, 2),
            "live_slug": post.get("slug") or "",
            "live_title": post.get("title") or "",
            "source": post.get("source") or "",
        }
        if best is None or candidate["score"] > best["score"]:
            best = candidate
    return best


def check_overlap(
    new_query: str,
    existing_topics: list[dict[str, str]],
    reserved_ids: set[str],
    live_posts: list[dict[str, str]] | None = None,
) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    warnings: list[dict[str, Any]] = []
    live_posts = live_posts or []

    for t in existing_topics:
        ext_tokens = normalize_and_tokenize(t["primary_query"] or t.get("h1") or "")
        if not new_tokens or not ext_tokens:
            continue
        similarity = jaccard(new_tokens, ext_tokens)
        live_hit = topic_live_status(t, live_posts)
        if t["topic_id"] in reserved_ids:
            status = "reserved"
        elif live_hit:
            status = "live_published"
        else:
            status = "in_pool"

        if (t["primary_query"] or "").strip().lower() == new_query.strip().lower():
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "message": (
                        f"EXACT MATCH found with topic {t['topic_id']} ({status})! "
                        f"Primary query: '{t['primary_query']}'"
                        + (f" | live slug: {live_hit['live_slug']}" if live_hit else "")
                    ),
                }
            )
        elif similarity >= 0.35:
            sev = "CRITICAL" if status in {"reserved", "live_published"} and similarity >= 0.45 else "WARNING"
            warnings.append(
                {
                    "severity": sev,
                    "topic_id": t["topic_id"],
                    "similarity": round(similarity, 2),
                    "status": status,
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with topic {t['topic_id']} ({status}). "
                        f"Query: '{t['primary_query']}'"
                        + (
                            f" | live≈{live_hit['live_slug']} (score={live_hit['score']})"
                            if live_hit
                            else ""
                        )
                    ),
                }
            )

    # Direct compare against live WP titles/slugs even when no topic card exists.
    for post in live_posts:
        live_tokens = normalize_and_tokenize(f"{post.get('title', '')} {post.get('slug', '').replace('-', ' ')}")
        similarity = jaccard(new_tokens, live_tokens)
        slug_bits = set((post.get("slug") or "").split("-"))
        slug_hit = jaccard(new_tokens, slug_bits)
        score = max(similarity, slug_hit)
        if score < 0.4:
            continue
        warnings.append(
            {
                "severity": "CRITICAL" if score >= 0.55 else "WARNING",
                "topic_id": "LIVE",
                "similarity": round(score, 2),
                "status": "live_published",
                "message": (
                    f"Overlap with live WP post slug='{post.get('slug')}' "
                    f"title='{(post.get('title') or '')[:80]}' (source={post.get('source')})"
                ),
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
    active = load_active_article_topics(root)
    reserved = published | active
    existing = load_existing_topics(root)
    live_posts = load_live_posts(root)
    live_topic_ids = set()
    for t in existing:
        hit = topic_live_status(t, live_posts)
        if hit and hit["score"] >= 0.55:
            live_topic_ids.add(t["topic_id"])

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
        print(f"Live WP snapshot posts: {len(live_posts)}")
        if live_topic_ids:
            print(f"Pool topics overlapping live WP (do not treat as free): {sorted(live_topic_ids)}")

        unwritten = [
            t["topic_id"]
            for t in existing
            if t["topic_id"] not in reserved and t["topic_id"] not in live_topic_ids
        ]
        print(f"Unwritten topic IDs in pool (ledger+live clean): {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, existing, reserved, live_posts)
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(f"  [{w['severity']}] Similarity: {w['similarity']} | Topic: {w['topic_id']} ({w['status']})")
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique.")
        if not live_posts:
            print("WARN: no memory/blog/published-live*.json loaded; live WP overlap was not checked.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
