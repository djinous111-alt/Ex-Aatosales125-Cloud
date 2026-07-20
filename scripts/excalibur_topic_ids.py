"""Shared topic_id parsing for Excalibur BLOG (AS* customs niche + legacy B*)."""

from __future__ import annotations

import re
from pathlib import Path

# Авто-Сейлс uses AS01…; legacy Excalibur SEO niche used B01…
TOPIC_ID_RE = re.compile(r"(?:AS|B)\d+", re.IGNORECASE)
TOPIC_ID_PREFIX_NUM_RE = re.compile(r"^((?:AS|B))(\d+)$", re.IGNORECASE)

# Heading card: ## AS11 — Title  /  ## B09 — Title
TOPIC_CARD_HEADING_RE = re.compile(
    r"##\s+((?:AS|B)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:AS|B)\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)

# Article dir: AS11-slug / B09-slug
ARTICLE_DIR_TOPIC_RE = re.compile(r"^((?:AS|B)\d+)-", re.IGNORECASE)

LIVE_SLUG_DUMP_CANDIDATES = (
    Path("memory/blog/published-live-avtosales125.json"),
    Path("memory/blog/published-live.json"),
)


def normalize_topic_id(value: str) -> str:
    return (value or "").strip().upper()


def parse_topic_id(value: str) -> tuple[str, int] | None:
    match = TOPIC_ID_PREFIX_NUM_RE.match(normalize_topic_id(value))
    if not match:
        return None
    return match.group(1).upper(), int(match.group(2))


def topic_id_from_article_dirname(name: str) -> str | None:
    match = ARTICLE_DIR_TOPIC_RE.match(name)
    return match.group(1).upper() if match else None


def iter_topic_cards(text: str) -> list[tuple[str, str]]:
    """Return list of (topic_id, block) from blog-topics.md body."""
    return [(m.group(1).upper(), m.group(2)) for m in TOPIC_CARD_HEADING_RE.finditer(text)]


def prefer_topic_prefix(existing_ids: list[str], *, default: str = "AS") -> str:
    """Pick ID series from pool majority; Авто-Сейлс defaults to AS."""
    counts: dict[str, int] = {}
    for raw in existing_ids:
        parsed = parse_topic_id(raw)
        if not parsed:
            continue
        prefix, _ = parsed
        counts[prefix] = counts.get(prefix, 0) + 1
    if not counts:
        return default.upper()
    # Prefer AS over B when tied (current niche).
    return sorted(counts.items(), key=lambda item: (-item[1], 0 if item[0] == "AS" else 1))[0][0]


def next_topic_id(existing_ids: list[str], *, prefix: str | None = None) -> str:
    chosen = (prefix or prefer_topic_prefix(existing_ids)).upper()
    max_num = 0
    for raw in existing_ids:
        parsed = parse_topic_id(raw)
        if not parsed:
            continue
        pfx, num = parsed
        if pfx == chosen:
            max_num = max(max_num, num)
    return f"{chosen}{max_num + 1:02d}"


def load_live_slug_dump(root: Path) -> list[dict[str, str]]:
    """Optional WP slug dump for scout cannibalization when MCP points at wrong site."""
    import json

    for rel in LIVE_SLUG_DUMP_CANDIDATES:
        path = root / rel
        if not path.is_file():
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        posts = payload.get("posts") if isinstance(payload, dict) else None
        if not isinstance(posts, list):
            continue
        rows: list[dict[str, str]] = []
        for item in posts:
            if not isinstance(item, dict):
                continue
            slug = str(item.get("slug") or "").strip()
            title = str(item.get("title") or "").strip()
            if slug:
                rows.append({"slug": slug, "title": title, "source": rel.as_posix()})
        return rows
    return []
