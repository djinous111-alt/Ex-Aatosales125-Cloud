"""Shared topic-id parsing for Excalibur BLOG (B01, AS02, …)."""

from __future__ import annotations

import re

# Letter prefix + digits: B01, AS02, AS18, …
TOPIC_ID_TOKEN = r"[A-Za-z]+\d+"
TOPIC_ID_RE = re.compile(rf"^({TOPIC_ID_TOKEN})$", re.IGNORECASE)
ARTICLE_DIR_TOPIC_RE = re.compile(rf"^({TOPIC_ID_TOKEN})-", re.IGNORECASE)
TOPIC_CARD_RE = re.compile(
    rf"##\s+({TOPIC_ID_TOKEN})\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+{TOPIC_ID_TOKEN}|\Z)",
    re.DOTALL | re.IGNORECASE,
)


def normalize_topic_id(raw: str) -> str:
    return raw.strip().upper()


def topic_id_from_article_dirname(name: str) -> str | None:
    match = ARTICLE_DIR_TOPIC_RE.match(name)
    if not match:
        return None
    return normalize_topic_id(match.group(1))


def iter_topic_cards(text: str) -> list[tuple[str, str]]:
    """Return list of (topic_id, block_body) from blog-topics.md."""
    return [
        (normalize_topic_id(match.group(1)), match.group(2))
        for match in TOPIC_CARD_RE.finditer(text)
    ]
