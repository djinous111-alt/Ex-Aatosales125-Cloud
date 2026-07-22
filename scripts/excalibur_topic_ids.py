#!/usr/bin/env python3
"""Shared topic_id patterns for Excalibur BLOG (AS* Avto-Sales + legacy B*)."""

from __future__ import annotations

import re

# Avto-Sales primary prefix AS; legacy template prefix B.
TOPIC_ID_RE = re.compile(r"^(AS|B)(\d+)$", re.IGNORECASE)
TOPIC_ID_IN_HEADING_RE = re.compile(r"##\s+((?:AS|B)\d+)\s+—", re.IGNORECASE)
ARTICLE_DIR_TOPIC_RE = re.compile(r"^((?:AS|B)\d+)-", re.IGNORECASE)
TOPIC_BLOCK_RE = re.compile(
    r"##\s+((?:AS|B)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:AS|B)\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)


def normalize_topic_id(topic_id: str) -> str:
    return topic_id.strip().upper()


def parse_topic_id(topic_id: str) -> tuple[str, int] | None:
    match = TOPIC_ID_RE.match(normalize_topic_id(topic_id))
    if not match:
        return None
    return match.group(1).upper(), int(match.group(2))


def format_topic_id(prefix: str, number: int) -> str:
    return f"{prefix.upper()}{number:02d}"


def next_topic_id(existing_ids: list[str], preferred_prefix: str = "AS") -> str:
    """Return next free id for preferred_prefix, based on max number of that prefix."""
    max_num = 0
    for topic_id in existing_ids:
        parsed = parse_topic_id(topic_id)
        if not parsed:
            continue
        prefix, num = parsed
        if prefix == preferred_prefix.upper():
            max_num = max(max_num, num)
    return format_topic_id(preferred_prefix, max_num + 1)
