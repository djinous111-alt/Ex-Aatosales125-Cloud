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
                "source": "blog-topics",
            }
        )
    return topics


def load_live_published_topics(root: Path) -> list[dict[str, str]]:
    """Load slugs/titles from memory/blog/published-live-*.json (WP mirror)."""
    blog_dir = root / "memory" / "blog"
    if not blog_dir.is_dir():
        return []
    topics: list[dict[str, str]] = []
    for path in sorted(blog_dir.glob("published-live-*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        posts = data.get("posts") or []
        for idx, post in enumerate(posts):
            if not isinstance(post, dict):
                continue
            slug = str(post.get("slug") or "").strip()
            title = str(post.get("title") or "").strip()
            if not slug and not title:
                continue
            # primary_query ≈ title for token overlap; slug for exact/near slug match
            topics.append(
                {
                    "topic_id": f"LIVE:{slug or idx}",
                    "primary_query": title or slug.replace("-", " "),
                    "slug": slug,
                    "priority": "live",
                    "source": path.name,
                }
            )
    return topics


def load_denylist_topics(root: Path, denylist_path: Path | None) -> list[dict[str, str]]:
    """Optional denylist: JSON list of {slug,title,primary_query} or plain slug lines."""
    path = denylist_path
    if path is None:
        candidates = [
            root / "memory" / "blog" / "scout-denylist.json",
            root / "memory" / "topics" / "scout-denylist.json",
        ]
        path = next((p for p in candidates if p.is_file()), None)
    if path is None or not path.is_file():
        return []
    if not path.is_absolute():
        path = root / path
    text = path.read_text(encoding="utf-8").strip()
    topics: list[dict[str, str]] = []
    if not text:
        return topics
    if path.suffix.lower() == ".json":
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            return topics
        items = data if isinstance(data, list) else data.get("slugs") or data.get("items") or []
        for idx, item in enumerate(items):
            if isinstance(item, str):
                slug = item.strip()
                title = slug.replace("-", " ")
            elif isinstance(item, dict):
                slug = str(item.get("slug") or "").strip()
                title = str(item.get("title") or item.get("primary_query") or slug).strip()
            else:
                continue
            if not slug and not title:
                continue
            topics.append(
                {
                    "topic_id": f"DENY:{slug or idx}",
                    "primary_query": title or slug.replace("-", " "),
                    "slug": slug,
                    "priority": "deny",
                    "source": "denylist",
                }
            )
        return topics

    for idx, line in enumerate(text.splitlines()):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        slug = line.split()[0]
        topics.append(
            {
                "topic_id": f"DENY:{slug}",
                "primary_query": slug.replace("-", " "),
                "slug": slug,
                "priority": "deny",
                "source": "denylist",
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


def slugify_query(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return text.strip("-")


def check_overlap(
    new_query: str,
    existing_topics: list[dict[str, str]],
    reserved_ids: set[str],
    *,
    proposed_slug: str = "",
) -> list[dict[str, Any]]:
    new_tokens = normalize_and_tokenize(new_query)
    proposed = (proposed_slug or slugify_query(new_query)).lower().strip("-")
    warnings: list[dict[str, Any]] = []

    for t in existing_topics:
        source = t.get("source") or "blog-topics"
        status = "reserved" if t["topic_id"] in reserved_ids else source
        ext_slug = (t.get("slug") or "").lower().strip("-")

        # Exact / near-exact slug collision (critical for live WP denylist)
        if proposed and ext_slug:
            if proposed == ext_slug:
                warnings.append(
                    {
                        "severity": "CRITICAL",
                        "topic_id": t["topic_id"],
                        "similarity": 1.0,
                        "status": status,
                        "message": (
                            f"EXACT SLUG MATCH with {t['topic_id']} ({status}). "
                            f"slug='{ext_slug}' source={source}"
                        ),
                    }
                )
                continue
            # High slug token overlap (e.g. same long live slug stem)
            prop_parts = set(proposed.split("-")) - {"2026", "i", "v", "na", "po", "dlya"}
            ext_parts = set(ext_slug.split("-")) - {"2026", "i", "v", "na", "po", "dlya"}
            if prop_parts and ext_parts:
                inter = len(prop_parts & ext_parts)
                union = len(prop_parts | ext_parts)
                slug_sim = inter / union if union else 0.0
                if slug_sim >= 0.55 and inter >= 3:
                    warnings.append(
                        {
                            "severity": "WARNING",
                            "topic_id": t["topic_id"],
                            "similarity": round(slug_sim, 2),
                            "status": status,
                            "message": (
                                f"High slug overlap ({round(slug_sim * 100)}%) with "
                                f"{t['topic_id']} ({status}). live/deny slug='{ext_slug}'"
                            ),
                        }
                    )

        ext_tokens = normalize_and_tokenize(t.get("primary_query") or "")
        if not new_tokens or not ext_tokens:
            continue
        intersection = len(new_tokens.intersection(ext_tokens))
        union = len(new_tokens.union(ext_tokens))
        similarity = intersection / union if union else 0.0

        if (t.get("primary_query") or "").strip().lower() == new_query.strip().lower():
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "topic_id": t["topic_id"],
                    "similarity": 1.0,
                    "status": status,
                    "message": (
                        f"EXACT MATCH found with topic {t['topic_id']} ({status})! "
                        f"Primary query: '{t['primary_query']}' source={source}"
                    ),
                }
            )
        elif similarity >= 0.35:
            # Live/deny: slightly lower threshold already covered via slug; keep query overlap
            warnings.append(
                {
                    "severity": "WARNING",
                    "topic_id": t["topic_id"],
                    "similarity": round(similarity, 2),
                    "status": status,
                    "message": (
                        f"High overlap ({round(similarity * 100)}%) with topic "
                        f"{t['topic_id']} ({status}). Query: '{t['primary_query']}' "
                        f"source={source}"
                    ),
                }
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument("--slug", type=str, default="", help="Optional proposed slug for live/denylist match")
    ap.add_argument(
        "--denylist",
        type=Path,
        default=None,
        help="Optional denylist JSON/txt (default: memory/blog/scout-denylist.json if present)",
    )
    ap.add_argument(
        "--skip-live",
        action="store_true",
        help="Do not load memory/blog/published-live-*.json",
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
    live = [] if args.skip_live else load_live_published_topics(root)
    deny = load_denylist_topics(root, args.denylist)
    pool = existing + live + deny

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
        print(f"Live WP posts indexed: {len(live)}")
        print(f"Denylist entries: {len(deny)}")
        print(f"Total articles written/in_progress: {len(reserved)}")
        print(f"Active article dirs: {sorted(active)}")

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        warnings = check_overlap(args.check_query, pool, reserved, proposed_slug=args.slug)
        if warnings:
            print("❌ OVERLAP DETECTED:")
            for w in warnings:
                print(
                    f"  [{w['severity']}] Similarity: {w['similarity']} | "
                    f"Topic: {w['topic_id']} ({w['status']})"
                )
                print(f"  Message: {w['message']}")
            return 1
        print("✅ NO CANNIBALIZATION RISK: Query is clean and unique (pool+live+denylist).")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
