#!/usr/bin/env python3
"""Shared topic-id parsing for Scout / today / research_start (AS*, B*, …)."""

from __future__ import annotations

import os
import re
from collections import Counter

# Default site series first (AVTO SALES), then legacy B-series.
DEFAULT_TOPIC_PREFIXES = ("AS", "B")

# Full topic id: letters + digits, e.g. AS19, B09
TOPIC_ID_TOKEN_RE = re.compile(r"^[A-Za-z]+\d+$")
TOPIC_ID_PARSE_RE = re.compile(r"^([A-Za-z]+)(\d+)$")

# Article dir: AS19-slug or B09-slug
ARTICLE_DIR_TOPIC_RE = re.compile(r"^([A-Za-z]+\d+)-", re.IGNORECASE)

# blog-topics.md headings: ## AS19 — Title
TOPIC_HEADING_RE = re.compile(
    r"##\s+([A-Za-z]+\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+[A-Za-z]|\Z)",
    re.DOTALL,
)


def topic_id_prefixes() -> tuple[str, ...]:
    raw = os.environ.get("EXCALIBUR_TOPIC_ID_PREFIXES", "").strip()
    if raw:
        parts = tuple(p.strip().upper() for p in re.split(r"[,;\s]+", raw) if p.strip())
        if parts:
            return parts
    return DEFAULT_TOPIC_PREFIXES


def normalize_topic_id(topic_id: str) -> str:
    return (topic_id or "").strip().upper()


def parse_topic_id(topic_id: str) -> tuple[str, int] | None:
    m = TOPIC_ID_PARSE_RE.match(normalize_topic_id(topic_id))
    if not m:
        return None
    return m.group(1).upper(), int(m.group(2))


def is_known_series(topic_id: str, prefixes: tuple[str, ...] | None = None) -> bool:
    parsed = parse_topic_id(topic_id)
    if not parsed:
        return False
    prefix, _ = parsed
    allowed = prefixes or topic_id_prefixes()
    return prefix in {p.upper() for p in allowed}


def topic_id_from_article_dirname(name: str) -> str | None:
    m = ARTICLE_DIR_TOPIC_RE.match(name)
    if not m:
        return None
    topic_id = normalize_topic_id(m.group(1))
    return topic_id if TOPIC_ID_TOKEN_RE.match(topic_id) else None


def format_topic_id(prefix: str, number: int) -> str:
    return f"{prefix.upper()}{number:02d}"


def choose_series_prefix(topic_ids: list[str], prefixes: tuple[str, ...] | None = None) -> str:
    """Pick active series: env override, else most common known prefix, else first default."""
    env_series = os.environ.get("EXCALIBUR_TOPIC_SERIES", "").strip().upper()
    allowed = prefixes or topic_id_prefixes()
    if env_series and env_series in {p.upper() for p in allowed}:
        return env_series

    counts: Counter[str] = Counter()
    for tid in topic_ids:
        parsed = parse_topic_id(tid)
        if not parsed:
            continue
        prefix, _ = parsed
        if prefix in {p.upper() for p in allowed}:
            counts[prefix] += 1
    if counts:
        return counts.most_common(1)[0][0]
    return allowed[0].upper()


def next_topic_id(existing_ids: list[str], prefixes: tuple[str, ...] | None = None) -> str:
    allowed = prefixes or topic_id_prefixes()
    series = choose_series_prefix(existing_ids, allowed)
    max_num = 0
    for tid in existing_ids:
        parsed = parse_topic_id(tid)
        if not parsed:
            continue
        prefix, num = parsed
        if prefix == series:
            max_num = max(max_num, num)
    return format_topic_id(series, max_num + 1)
