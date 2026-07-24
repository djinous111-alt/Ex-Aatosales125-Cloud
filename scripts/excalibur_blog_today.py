#!/usr/bin/env python3
"""Print Excalibur BLOG automation date context and recent published articles."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime
from html import unescape
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Moscow")
LEDGER_PATHS = (
    Path("shared/published-articles.md"),
)
DEFAULT_SITE_URL = ""
TOPIC_HEADING_RE = re.compile(
    r"##\s+([A-Z]+\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+[A-Z]+\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)
ARTICLE_DIR_RE = re.compile(r"^([A-Z]+\d+)-", re.IGNORECASE)
TOPIC_ID_RE = re.compile(r"\b(AS|B)(\d+)\b", re.IGNORECASE)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def parse_published_slugs(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for rel in LEDGER_PATHS:
        path = root / rel
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| 20"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            rows.append(
                {
                    "date": cells[0],
                    "topic_id": cells[1],
                    "slug": cells[2],
                    "url": cells[3],
                    "status": cells[4].lower(),
                }
            )
    return rows


def active_article_topic_ids(root: Path) -> set[str]:
    articles_dir = root / "memory" / "blog" / "articles"
    if not articles_dir.is_dir():
        return set()
    active: set[str] = set()
    for path in articles_dir.iterdir():
        if not path.is_dir():
            continue
        match = ARTICLE_DIR_RE.match(path.name)
        if match:
            active.add(match.group(1).upper())
    return active


def extract_topic_ids(text: str) -> set[str]:
    found: set[str] = set()
    for match in TOPIC_ID_RE.finditer(text or ""):
        prefix = match.group(1).upper()
        num = int(match.group(2))
        if prefix == "B":
            found.add(f"B{num:02d}")
        else:
            found.add(f"AS{num}")
    return found


def max_num_for_prefix(topic_ids: set[str], prefix: str) -> int:
    max_num = 0
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)$", re.IGNORECASE)
    for tid in topic_ids:
        match = pattern.match(tid)
        if match:
            max_num = max(max_num, int(match.group(1)))
    return max_num


def format_next_id(prefix: str, max_num: int) -> str:
    nxt = max_num + 1
    if prefix.upper() == "B":
        return f"B{nxt:02d}"
    return f"{prefix.upper()}{nxt}"


def env_floor_ids() -> set[str]:
    ids: set[str] = set()
    for key in ("EXCALIBUR_TOPIC_ID_FLOOR", "EXCALIBUR_B_ID_FLOOR", "EXCALIBUR_AS_ID_FLOOR", "EXCALIBUR_MIN_TOPIC_ID"):
        raw = os.environ.get(key, "").strip().upper()
        if raw:
            ids |= extract_topic_ids(raw)
    return ids


def pool_topic_ids(root: Path) -> set[str]:
    topics_path = root / "memory/topics/blog-topics.md"
    if not topics_path.is_file():
        return set()
    return {m.group(1).upper() for m in TOPIC_HEADING_RE.finditer(topics_path.read_text(encoding="utf-8"))}


def next_p0_topic(root: Path, published: list[dict[str, str]], known_ids: set[str]) -> str:
    topics_path = root / "memory/topics/blog-topics.md"
    if not topics_path.is_file():
        return ""

    used = {
        r["topic_id"].upper()
        for r in published
        if r["status"] in {"published", "in_progress", "draft_ready"}
    }
    used.update(active_article_topic_ids(root))
    used.update(known_ids)
    text = topics_path.read_text(encoding="utf-8")
    for match in TOPIC_HEADING_RE.finditer(text):
        topic_id = match.group(1).upper()
        block = match.group(2)
        if "priority:** P0" not in block and "**priority:** P0" not in block:
            pri = re.search(r"-\s*\*\*priority:\*\*\s*(\S+)", block)
            if not pri or pri.group(1).upper() != "P0":
                continue
        if topic_id not in used:
            return topic_id
    return ""


def fetch_recent_wp_posts(site_url: str, limit: int = 12) -> tuple[list[dict[str, str]], str | None]:
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=date,link,slug,title",
    )
    request = Request(endpoint, headers={"User-Agent": "ExcaliburBlogAutomation/1.0"})
    try:
        with urlopen(request, timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [], f"{type(exc).__name__}: {exc}"

    pages: list[dict[str, str]] = []
    for item in payload:
        title = item.get("title", {}).get("rendered", "") if isinstance(item.get("title"), dict) else ""
        title = re.sub(r"<[^>]+>", "", title)
        pages.append(
            {
                "date": str(item.get("date", ""))[:10],
                "slug": str(item.get("slug", "")),
                "title": unescape(title).strip(),
                "link": str(item.get("link", "")),
            }
        )
    return pages, None


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    root = project_root()
    now = datetime.now(TZ)
    published = parse_published_slugs(root)
    active = active_article_topic_ids(root)
    pool_ids = pool_topic_ids(root)
    floor_ids = env_floor_ids()
    ledger_ids = {
        r["topic_id"].upper()
        for r in published
        if r["status"] in {"published", "in_progress", "draft_ready"}
    }

    site_url = os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or DEFAULT_SITE_URL
    wp_posts: list[dict[str, str]] = []
    wp_error: str | None = None
    wp_ids: set[str] = set()
    if site_url:
        wp_posts, wp_error = fetch_recent_wp_posts(site_url)
        for post in wp_posts:
            blob = " ".join([post.get("slug", ""), post.get("title", ""), post.get("link", "")])
            wp_ids |= extract_topic_ids(blob)

    known_ids = pool_ids | ledger_ids | active | wp_ids | floor_ids
    max_b = max_num_for_prefix(known_ids, "B")
    max_as = max_num_for_prefix(known_ids, "AS")
    next_b = format_next_id("B", max_b)
    next_as = format_next_id("AS", max_as)

    if max_b == 0 and (wp_posts or any(tid.startswith("AS") for tid in known_ids)):
        if not floor_ids:
            next_b = "NEEDS_MANUAL_OR_FLOOR"

    topic_id = os.environ.get("EXCALIBUR_TOPIC_ID", "").strip().upper()
    if not topic_id:
        topic_id = next_p0_topic(root, published, known_ids)
    if not topic_id and next_b != "NEEDS_MANUAL_OR_FLOOR":
        # Suggest next free B* only when floor is known; else leave needs_scout.
        if max_b > 0 or floor_ids:
            topic_id = next_b

    print(f"EXCALIBUR_RUN_DATE={now:%Y-%m-%d}")
    print(f"EXCALIBUR_RUN_DATETIME={now:%Y-%m-%d %H:%M:%S %Z}")
    print(f"EXCALIBUR_RUN_YEAR={now.year}")
    print(f"EXCALIBUR_FRESHNESS_WINDOW=prefer_sources_after_{(now.date().replace(day=1)).isoformat()}")
    print(f"EXCALIBUR_SUGGESTED_TOPIC_ID={topic_id}")
    print(f"EXCALIBUR_TOPIC_SELECTION={'ready' if topic_id else 'needs_scout'}")
    print(f"EXCALIBUR_NEXT_B_ID={next_b}")
    print(f"EXCALIBUR_NEXT_AS_ID={next_as}")
    print(f"EXCALIBUR_MAX_B_SEEN={max_b}")
    print(f"EXCALIBUR_MAX_AS_SEEN={max_as}")
    print(
        "EXCALIBUR_PUBLISHED_ARTICLES="
        + json.dumps(published[-10:], ensure_ascii=False)
    )

    if site_url:
        if wp_error:
            print(f"EXCALIBUR_RECENT_WP_POSTS_ERROR={wp_error}")
        else:
            compact = [f"{p['date']}|{p['slug']}|{p['title']}" for p in wp_posts]
            print("EXCALIBUR_RECENT_WP_POSTS=" + json.dumps(compact, ensure_ascii=False))
            print(f"EXCALIBUR_WP_TOPIC_IDS={json.dumps(sorted(wp_ids), ensure_ascii=False)}")
    else:
        print("EXCALIBUR_RECENT_WP_POSTS=")
        print("EXCALIBUR_RECENT_WP_POSTS_NOTE=set PUBLIC_SITE_URL for live dedupe")

    if next_b == "NEEDS_MANUAL_OR_FLOOR":
        print(
            "EXCALIBUR_TOPIC_ID_FLOOR_NOTE="
            "live WP/AS* history present but no B* IDs found; "
            "set EXCALIBUR_TOPIC_ID_FLOOR=B0N before suggesting B01/B02"
        )


if __name__ == "__main__":
    main()
