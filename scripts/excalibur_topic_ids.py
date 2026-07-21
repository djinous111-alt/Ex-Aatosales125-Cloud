"""Shared topic-id parsing for AS* (Авто-Сейлс) and B* series."""

from __future__ import annotations

import re
from collections import Counter

# Canonical topic id: AS18, B09, … (case-insensitive).
TOPIC_ID_BODY = r"(?:AS|B)\d+"
TOPIC_ID_RE = re.compile(rf"^({TOPIC_ID_BODY})$", re.IGNORECASE)
DIR_TOPIC_RE = re.compile(rf"^({TOPIC_ID_BODY})-", re.IGNORECASE)
# Heading cards in memory/topics/blog-topics.md
CARD_TOPIC_RE = re.compile(
    rf"##\s+({TOPIC_ID_BODY})\s+[—\-–][^\n]*\n(.*?)(?=\n---|\n##\s+(?:AS|B)|\Z)",
    re.DOTALL | re.IGNORECASE,
)
NUM_RE = re.compile(rf"^({TOPIC_ID_BODY})", re.IGNORECASE)


def normalize_topic_id(raw: str) -> str:
    return raw.strip().upper()


def topic_id_from_dirname(name: str) -> str | None:
    match = DIR_TOPIC_RE.match(name)
    return normalize_topic_id(match.group(1)) if match else None


def split_prefix_num(topic_id: str) -> tuple[str, int] | None:
    match = re.match(r"^(AS|B)(\d+)$", normalize_topic_id(topic_id))
    if not match:
        return None
    return match.group(1), int(match.group(2))


def preferred_prefix(topic_ids: list[str] | set[str], default: str = "AS") -> str:
    """Pick series with most evidence; Авто-Сейлс niches default to AS."""
    counts: Counter[str] = Counter()
    for tid in topic_ids:
        parts = split_prefix_num(tid)
        if parts:
            counts[parts[0]] += 1
    if not counts:
        return default
    # Prefer AS on ties (Авто-Сейлс niche).
    if counts.get("AS", 0) >= counts.get("B", 0) and counts.get("AS", 0) > 0:
        return "AS"
    if counts.get("B", 0) > 0:
        return "B"
    return default


def next_id_for_prefix(topic_ids: list[str] | set[str], prefix: str) -> str:
    max_num = 0
    prefix = prefix.upper()
    for tid in topic_ids:
        parts = split_prefix_num(tid)
        if parts and parts[0] == prefix:
            max_num = max(max_num, parts[1])
    return f"{prefix}{max_num + 1:02d}"


def suggest_next_topic_id(
    pool_ids: list[str] | set[str],
    reserved_ids: list[str] | set[str] | None = None,
    default_prefix: str = "AS",
) -> str:
    """Next free id in the dominant series across pool + reserved (ledger/dirs)."""
    combined = {normalize_topic_id(t) for t in pool_ids}
    if reserved_ids:
        combined.update(normalize_topic_id(t) for t in reserved_ids)
    prefix = preferred_prefix(combined, default=default_prefix)
    return next_id_for_prefix(combined, prefix)
