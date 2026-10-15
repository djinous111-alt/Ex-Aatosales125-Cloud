#!/usr/bin/env python3
"""Helpers for markdown ledger tables in shared/published-articles.md."""

from __future__ import annotations

import re
from pathlib import Path


TABLE_SEP_RE = re.compile(r"^\|\s*-+")


def find_markdown_table_bounds(lines: list[str]) -> tuple[int, int] | None:
    """Return (header_idx, last_data_row_idx) for the first markdown table.

    last_data_row_idx is the last `| ... |` row that belongs to the table
    (header or separator or data). Insertion should happen after that index.
    """
    header_idx: int | None = None
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("|"):
            if header_idx is not None:
                break
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if header_idx is None:
            # Prefer the published-articles header shape, else first pipe row.
            if len(cells) >= 2 and (
                cells[0].lower() == "date" or cells[1].lower() in {"topic_id", "id"}
            ):
                header_idx = idx
            elif len(cells) >= 2:
                header_idx = idx
            continue
        # Still inside table while lines start with |
        continue

    if header_idx is None:
        return None

    last_idx = header_idx
    for idx in range(header_idx + 1, len(lines)):
        stripped = lines[idx].strip()
        if not stripped.startswith("|"):
            break
        last_idx = idx
    return header_idx, last_idx


def insert_row_into_markdown_table(text: str, row: str) -> str:
    """Insert a table row after the last existing table row (not file EOF).

    If no table exists, appends a minimal header + row.
    """
    row = row.rstrip("\n")
    if not row.startswith("|"):
        row = "| " + row
    lines = text.splitlines()
    bounds = find_markdown_table_bounds(lines)
    if bounds is None:
        block = [
            "| date | topic_id | slug | url | status |",
            "|------|----------|------|-----|--------|",
            row,
        ]
        base = text.rstrip("\n")
        return (base + "\n\n" if base else "") + "\n".join(block) + "\n"

    _, last_idx = bounds
    lines.insert(last_idx + 1, row)
    return "\n".join(lines).rstrip() + "\n"


def replace_or_insert_topic_row(text: str, topic_id: str, row: str) -> str:
    """Replace an existing topic_id row inside the table, else insert into table."""
    topic_id = topic_id.upper()
    row = row.rstrip("\n")
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[1].upper() == topic_id:
            lines[idx] = row
            return "\n".join(lines).rstrip() + "\n"
    return insert_row_into_markdown_table(text, row)
