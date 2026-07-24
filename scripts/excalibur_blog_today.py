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
            if re.match(r"^(?:B|AS)\d+$", topic_id, flags=re.IGNORECASE):
                active.add(topic_id)
    return active


def env_used_topic_ids() -> set[str]:
    raw = os.environ.get("EXCALIBUR_USED_TOPIC_IDS", "").strip()
    if not raw:
        return set()
    out: set[str] = set()
    for part in re.split(r"[,;\s]+", raw):
        token = part.strip().upper()
        if re.match(r"^(?:B|AS)\d+$", token):
            out.add(token)
    return out


def topic_slug_to_id(root: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for row in parse_published_slugs(root):
        slug = (row.get("slug") or "").strip().lower()
        topic_id = (row.get("topic_id") or "").strip().upper()
        if slug and re.match(r"^(?:B|AS)\d+$", topic_id):
            mapping[slug] = topic_id
    topics_path = root / "memory/topics/blog-topics.md"
    if topics_path.is_file():
        text = topics_path.read_text(encoding="utf-8")
        for match in re.finditer(
            r"##\s+((?:B|AS)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)|\Z)",
            text,
            re.DOTALL | re.IGNORECASE,
        ):
            topic_id = match.group(1).upper()
            block = match.group(2)
            slug_m = re.search(r"(?:-|\*)\s*\*\*slug:\*\*\s*(\S+)", block, re.IGNORECASE)
            if slug_m:
                mapping[slug_m.group(1).strip().lower()] = topic_id
    return mapping


def match_wp_topic_ids(posts: list[dict[str, str]], slug_map: dict[str, str]) -> set[str]:
    matched: set[str] = set()
    for post in posts:
        slug = (post.get("slug") or "").strip().lower()
        if not slug:
            continue
        if slug in slug_map:
            matched.add(slug_map[slug])
            continue
        m = re.match(r"((?:b|as)\d+)[-_]", slug, flags=re.IGNORECASE)
        if m:
            matched.add(m.group(1).upper())
    return matched


def max_b_floor(used: set[str], root: Path) -> int:
    max_num = 0
    for topic_id in used:
        m = re.match(r"^B(\d+)$", topic_id, flags=re.IGNORECASE)
        if m:
            max_num = max(max_num, int(m.group(1)))
    topics_path = root / "memory/topics/blog-topics.md"
    if topics_path.is_file():
        for m in re.finditer(r"##\s+B(\d+)\b", topics_path.read_text(encoding="utf-8"), re.IGNORECASE):
            max_num = max(max_num, int(m.group(1)))
    return max_num


def next_p0_topic(root: Path, published: list[dict[str, str]], extra_used: set[str] | None = None) -> str:
    topics_path = root / "memory/topics/blog-topics.md"
    if not topics_path.is_file():
        return ""

    used = {
        r["topic_id"].upper()
        for r in published
        if r["status"] in {"published", "in_progress", "draft_ready"}
    }
    used.update(active_article_topic_ids(root))
    used.update(env_used_topic_ids())
    if extra_used:
        used.update(extra_used)
    text = topics_path.read_text(encoding="utf-8")
    for match in re.finditer(
        r"##\s+(B\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:B|AS)|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    ):
        topic_id = match.group(1).upper()
        block = match.group(2)
        if "priority:** P0" not in block and "**priority:** P0" not in block:
            pri = re.search(r"-\s*\*\*priority:\*\*\s*(\S+)", block)
            if not pri or pri.group(1).upper() != "P0":
                continue
        if topic_id not in used:
            return topic_id
    return ""


def fetch_recent_wp_posts(site_url: str, limit: int = 30) -> tuple[list[dict[str, str]], str | None]:
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

    site_url = os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or DEFAULT_SITE_URL
    wp_matched: set[str] = set()
    posts: list[dict[str, str]] = []
    wp_error: str | None = None
    if site_url:
        posts, wp_error = fetch_recent_wp_posts(site_url)
        if not wp_error:
            wp_matched = match_wp_topic_ids(posts, topic_slug_to_id(root))

    topic_id = os.environ.get("EXCALIBUR_TOPIC_ID", "").strip().upper() or next_p0_topic(
        root, published, extra_used=wp_matched
    )
    used_for_floor = {
        r["topic_id"].upper()
        for r in published
        if r["status"] in {"published", "in_progress", "draft_ready"}
    }
    used_for_floor.update(active_article_topic_ids(root))
    used_for_floor.update(env_used_topic_ids())
    used_for_floor.update(wp_matched)
    b_floor = max_b_floor(used_for_floor, root)

    print(f"EXCALIBUR_RUN_DATE={now:%Y-%m-%d}")
    print(f"EXCALIBUR_RUN_DATETIME={now:%Y-%m-%d %H:%M:%S %Z}")
    print(f"EXCALIBUR_RUN_YEAR={now.year}")
    print(f"EXCALIBUR_FRESHNESS_WINDOW=prefer_sources_after_{(now.date().replace(day=1)).isoformat()}")
    print(f"EXCALIBUR_SUGGESTED_TOPIC_ID={topic_id}")
    print(f"EXCALIBUR_TOPIC_SELECTION={'ready' if topic_id else 'needs_scout'}")
    print(f"EXCALIBUR_BXX_FLOOR={b_floor}")
    print(f"EXCALIBUR_NEXT_B_IF_SCOUT=B{b_floor + 1:02d}")
    print(
        "EXCALIBUR_PUBLISHED_ARTICLES="
        + json.dumps(published[-10:], ensure_ascii=False)
    )
    if wp_matched:
        print("EXCALIBUR_WP_MATCHED_TOPIC_IDS=" + json.dumps(sorted(wp_matched), ensure_ascii=False))

    if site_url:
        if wp_error:
            print(f"EXCALIBUR_RECENT_WP_POSTS_ERROR={wp_error}")
        else:
            compact = [f"{p['date']}|{p['slug']}|{p['title']}" for p in posts]
            print("EXCALIBUR_RECENT_WP_POSTS=" + json.dumps(compact, ensure_ascii=False))
    else:
        print("EXCALIBUR_RECENT_WP_POSTS=")
        print("EXCALIBUR_RECENT_WP_POSTS_NOTE=set PUBLIC_SITE_URL for live dedupe")


if __name__ == "__main__":
    main()
