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

TOPIC_CARD_RE = re.compile(
    r"##\s+((?:B|AS)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)|\Z)",
    re.DOTALL | re.IGNORECASE,
)
TOPIC_ID_RE = re.compile(r"^(B|AS)(\d+)$", re.IGNORECASE)
B_TOPIC_ID_RE = re.compile(r"^B(\d+)$", re.IGNORECASE)


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
        if len(cells) < 5:
            continue
        topic_id = cells[1].upper()
        slug = cells[2].strip().lower()
        if TOPIC_ID_RE.match(topic_id) and slug:
            mapping[slug] = topic_id
    return mapping


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
            continue
        meta_path = path / "article.meta.json"
        if meta_path.is_file():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            topic_id = str(meta.get("topic_id") or "").strip().upper()
            if TOPIC_ID_RE.match(topic_id):
                active.add(topic_id)
    return active


def env_used_topic_ids() -> set[str]:
    raw = os.environ.get("EXCALIBUR_USED_TOPIC_IDS", "").strip()
    if not raw:
        return set()
    out: set[str] = set()
    for part in re.split(r"[,;\s]+", raw):
        token = part.strip().upper()
        if TOPIC_ID_RE.match(token):
            out.add(token)
    return out


def load_existing_topics(root: Path) -> list[dict[str, str]]:
    """Load Bxx and ASxx cards from blog-topics.md."""
    topics_path = root / "memory/topics/blog-topics.md"
    topics = []
    if not topics_path.is_file():
        return topics
    text = topics_path.read_text(encoding="utf-8")
    for match in TOPIC_CARD_RE.finditer(text):
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


def topic_slug_map(topics: list[dict[str, str]]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for t in topics:
        slug = (t.get("slug") or "").strip().lower()
        if slug:
            mapping[slug] = t["topic_id"].upper()
    return mapping


def fetch_recent_wp_slugs(site_url: str, limit: int = 30) -> tuple[list[str], str | None]:
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=slug",
    )
    request = Request(endpoint, headers={"User-Agent": "ExcaliburBlogAutomation/1.0"})
    try:
        with urlopen(request, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [], f"{type(exc).__name__}: {exc}"
    slugs: list[str] = []
    for item in payload:
        slug = str(item.get("slug") or "").strip().lower()
        if slug:
            slugs.append(slug)
    return slugs, None


def match_wp_topic_ids(
    wp_slugs: list[str],
    slug_to_topic: dict[str, str],
) -> set[str]:
    matched: set[str] = set()
    for slug in wp_slugs:
        topic_id = slug_to_topic.get(slug)
        if topic_id:
            matched.add(topic_id.upper())
            continue
        # Fallback: slug starts with b01- / as08-
        m = re.match(r"((?:b|as)\d+)[-_]", slug, flags=re.IGNORECASE)
        if m:
            matched.add(m.group(1).upper())
    return matched


def collect_used_topic_ids(
    root: Path,
    existing: list[dict[str, str]] | None = None,
) -> tuple[set[str], dict[str, Any]]:
    existing = existing if existing is not None else load_existing_topics(root)
    published = load_published_topics(root)
    active = load_active_article_topics(root)
    env_ids = env_used_topic_ids()
    slug_map = topic_slug_map(existing)
    slug_map.update(load_ledger_slug_map(root))

    wp_ids: set[str] = set()
    wp_error: str | None = None
    wp_slugs: list[str] = []
    site_url = (
        os.environ.get("PUBLIC_SITE_URL")
        or os.environ.get("WP_SITE_URL")
        or os.environ.get("WP_HOME")
        or ""
    ).strip()
    if site_url:
        wp_slugs, wp_error = fetch_recent_wp_slugs(site_url)
        if not wp_error:
            wp_ids = match_wp_topic_ids(wp_slugs, slug_map)

    used = published | active | env_ids | wp_ids
    meta = {
        "published": sorted(published),
        "active_dirs": sorted(active),
        "env_used": sorted(env_ids),
        "wp_matched": sorted(wp_ids),
        "wp_slug_count": len(wp_slugs),
        "wp_error": wp_error,
        "site_url_configured": bool(site_url),
    }
    return used, meta


def max_b_floor(existing: list[dict[str, str]], used: set[str]) -> int:
    """Highest Bxx number seen in cards or used IDs (WP/ledger/dirs/env)."""
    max_num = 0
    for t in existing:
        m = B_TOPIC_ID_RE.match(t["topic_id"])
        if m:
            max_num = max(max_num, int(m.group(1)))
    for topic_id in used:
        m = B_TOPIC_ID_RE.match(topic_id)
        if m:
            max_num = max(max_num, int(m.group(1)))
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
                        f"High overlap ({round(similarity * 100)}%) with topic "
                        f"{t['topic_id']} ({status}). Query: '{t['primary_query']}'"
                    ),
                }
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Helper for Excalibur BLOG Scout Agent")
    ap.add_argument("--suggest-next", action="store_true", help="Print next available Topic ID and summary")
    ap.add_argument("--check-query", type=str, default="", help="Check new primary query for overlaps")
    ap.add_argument(
        "--used-ids",
        type=str,
        default="",
        help="Comma-separated extra used topic IDs (same as EXCALIBUR_USED_TOPIC_IDS)",
    )
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    root = project_root()
    if args.used_ids.strip():
        os.environ["EXCALIBUR_USED_TOPIC_IDS"] = (
            (os.environ.get("EXCALIBUR_USED_TOPIC_IDS", "").strip() + "," + args.used_ids.strip()).strip(",")
        )

    existing = load_existing_topics(root)
    reserved, meta = collect_used_topic_ids(root, existing)

    if args.suggest_next:
        print("=== EXCALIBUR SCOUT HELPER ===")
        floor = max_b_floor(existing, reserved)
        next_id = f"B{floor + 1:02d}"
        print(f"Next available topic ID: {next_id}")
        print(f"Bxx floor (max seen): B{floor:02d}" if floor else "Bxx floor (max seen): none")
        print(f"Total topics in pool (blog-topics.md B+AS): {len(existing)}")
        print(f"Total articles written/in_progress/used: {len(reserved)}")
        print(f"Active article dirs: {meta['active_dirs']}")
        print(f"Ledger reserved: {meta['published']}")
        print(f"WP matched topic IDs: {meta['wp_matched']}")
        if meta["env_used"]:
            print(f"Env/CLI used IDs: {meta['env_used']}")
        if not meta["site_url_configured"]:
            print("WP floor note: set PUBLIC_SITE_URL for live slug→topic matching")
        elif meta["wp_error"]:
            print(f"WP floor warning: {meta['wp_error']}")
        else:
            print(f"WP recent slugs scanned: {meta['wp_slug_count']}")
        print(
            "NOTE: never trust suggest-next alone when ledger lags WP; "
            "pass --used-ids / EXCALIBUR_USED_TOPIC_IDS for known Bxx not in repo."
        )

        unwritten = [t["topic_id"] for t in existing if t["topic_id"] not in reserved]
        print(f"Unwritten topic IDs in pool: {unwritten}")
        return 0

    if args.check_query:
        # Overlap against Bxx + ASxx cards; reserved includes WP/ledger/dirs/env.
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
