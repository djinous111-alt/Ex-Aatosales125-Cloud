#!/usr/bin/env python3
"""Shared topic-id helpers for AS* (Авто-Сейлс) and legacy B* pools."""
from __future__ import annotations

import re

# Canonical topic id: AS01… or B01…
TOPIC_ID_RE = re.compile(r"(?:AS|B)\d+", re.IGNORECASE)
TOPIC_ID_PREFIX_RE = re.compile(r"^((?:AS|B)\d+)-", re.IGNORECASE)
TOPIC_CARD_RE = re.compile(
    r"##\s+((?:AS|B)\d+)\s+—[^\n]*\n(.*?)(?=\n---|\n##\s+(?:AS|B)\d+|\Z)",
    re.DOTALL | re.IGNORECASE,
)


def normalize_topic_id(value: str) -> str:
    return str(value or "").strip().upper()


def topic_id_from_article_dirname(name: str) -> str | None:
    match = TOPIC_ID_PREFIX_RE.match(name)
    return match.group(1).upper() if match else None


def iter_topic_cards(text: str):
    for match in TOPIC_CARD_RE.finditer(text):
        yield match.group(1).upper(), match.group(2)
