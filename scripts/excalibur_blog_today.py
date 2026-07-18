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
        match = re.match(r"([A-Z]{1,3}\d+)-", path.name, flags=re.IGNORECASE)
        if match:
            active.add(match.group(1).upper())
    return active


def _topic_fields_from_block(topic_id: str, block: str) -> dict[str, str]:
    def field(name: str, default: str = "") -> str:
        m = re.search(rf"-\s*\*\*{re.escape(name)}:\*\*\s*(.+)", block, re.IGNORECASE)
        return m.group(1).strip() if m else default

    return {
        "topic_id": topic_id.upper(),
        "priority": field("priority"),
        "slug": field("slug"),
        "h1": field("h1"),
        "primary_query": field("primary_query"),
        "search_intent": field("search_intent"),
        "article_mode": field("article_mode"),
        "h2_outline": field("h2_outline"),
    }


def _topic_utility_pass(root: Path, topic: dict[str, str]) -> bool:
    """Skip P0 cards that would fail utility topic gate (optional soft-skip)."""
    try:
        scripts_dir = Path(__file__).resolve().parent
        if str(scripts_dir) not in sys.path:
            sys.path.insert(0, str(scripts_dir))
        from excalibur_blog_utility_gate import gate_topic, load_json

        policy_path = root / "memory/brief/editorial-policy.json"
        if not policy_path.is_file():
            return True
        report = gate_topic(topic, load_json(policy_path))
        return report.get("status") == "PASS"
    except Exception as exc:  # noqa: BLE001
        print(f"EXCALIBUR_TOPIC_UTILITY_CHECK_ERROR={type(exc).__name__}: {exc}", file=sys.stderr)
        return True


def next_p0_topic(root: Path, published: list[dict[str, str]]) -> str:
    topics_path = root / "memory/topics/blog-topics.md"
    if not topics_path.is_file():
        return ""

    used = {
        r["topic_id"].upper()
        for r in published
        if r["status"] in {"published", "in_progress", "draft_ready"}
    }
    used.update(active_article_topic_ids(root))
    text = topics_path.read_text(encoding="utf-8")
    # Support Autosalеs AS## and legacy B## topic cards.
    skipped: list[str] = []
    for match in re.finditer(
        r"##\s+([A-Z]{1,3}\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+[A-Z]{1,3}\d+|\Z)",
        text,
        re.DOTALL,
    ):
        topic_id = match.group(1).upper()
        block = match.group(2)
        if "priority:** P0" not in block and "**priority:** P0" not in block:
            pri = re.search(r"-\s*\*\*priority:\*\*\s*(\S+)", block)
            if not pri or pri.group(1).upper() != "P0":
                continue
        if topic_id in used:
            continue
        topic = _topic_fields_from_block(topic_id, block)
        if not _topic_utility_pass(root, topic):
            skipped.append(topic_id)
            continue
        if skipped:
            print(
                "EXCALIBUR_TOPIC_SKIPPED_UTILITY_FAIL="
                + json.dumps(skipped, ensure_ascii=False),
                file=sys.stderr,
            )
        return topic_id
    if skipped:
        print(
            "EXCALIBUR_TOPIC_SKIPPED_UTILITY_FAIL="
            + json.dumps(skipped, ensure_ascii=False),
            file=sys.stderr,
        )
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
    topic_id = os.environ.get("EXCALIBUR_TOPIC_ID", "").strip().upper() or next_p0_topic(root, published)

    print(f"EXCALIBUR_RUN_DATE={now:%Y-%m-%d}")
    print(f"EXCALIBUR_RUN_DATETIME={now:%Y-%m-%d %H:%M:%S %Z}")
    print(f"EXCALIBUR_RUN_YEAR={now.year}")
    print(f"EXCALIBUR_FRESHNESS_WINDOW=prefer_sources_after_{(now.date().replace(day=1)).isoformat()}")
    print(f"EXCALIBUR_SUGGESTED_TOPIC_ID={topic_id}")
    print(f"EXCALIBUR_TOPIC_SELECTION={'ready' if topic_id else 'needs_scout'}")
    print(
        "EXCALIBUR_PUBLISHED_ARTICLES="
        + json.dumps(published[-10:], ensure_ascii=False)
    )

    site_url = os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or DEFAULT_SITE_URL
    if site_url:
        posts, error = fetch_recent_wp_posts(site_url)
        if error:
            print(f"EXCALIBUR_RECENT_WP_POSTS_ERROR={error}")
        else:
            compact = [f"{p['date']}|{p['slug']}|{p['title']}" for p in posts]
            print("EXCALIBUR_RECENT_WP_POSTS=" + json.dumps(compact, ensure_ascii=False))
    else:
        print("EXCALIBUR_RECENT_WP_POSTS=")
        print("EXCALIBUR_RECENT_WP_POSTS_NOTE=set PUBLIC_SITE_URL for live dedupe")


if __name__ == "__main__":
    main()
