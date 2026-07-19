#!/usr/bin/env python3
"""Helpers for shared/published-articles.md markdown table upserts."""
from __future__ import annotations

import re
from pathlib import Path


LEDGER_HEADER = (
    "# Excalibur BLOG — журнал опубликованных статей\n\n"
    "| date | topic_id | slug | url | status |\n"
    "|------|----------|------|-----|--------|\n"
)


def ensure_ledger_file(ledger_path: Path) -> None:
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    if not ledger_path.is_file():
        ledger_path.write_text(LEDGER_HEADER, encoding="utf-8")


def first_markdown_table_range(lines: list[str]) -> tuple[int, int] | None:
    """Return (start, end_exclusive) of the first contiguous markdown table."""
    start: int | None = None
    for index, line in enumerate(lines):
        if line.startswith("|"):
            if start is None:
                start = index
            continue
        if start is not None:
            return start, index
    if start is not None:
        return start, len(lines)
    return None


def topic_row_in_table(lines: list[str], topic_id: str, table_range: tuple[int, int]) -> int | None:
    topic_id = topic_id.upper()
    start, end = table_range
    for index in range(start, end):
        line = lines[index]
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[1].upper() == topic_id:
            # Skip header / separator rows
            if cells[0].lower() == "date" or set(cells[0]) <= {"-", ":"}:
                continue
            return index
    return None


def upsert_ledger_row(ledger_path: Path, row: str, topic_id: str) -> str:
    """Insert or replace a topic row inside the first markdown table only.

    Returns: 'replaced' | 'inserted' | 'created'
    """
    ensure_ledger_file(ledger_path)
    topic_id = topic_id.upper()
    row = row.rstrip("\n")
    lines = ledger_path.read_text(encoding="utf-8").splitlines()
    table_range = first_markdown_table_range(lines)

    if table_range is None:
        # No table yet — write canonical header + row.
        ledger_path.write_text(LEDGER_HEADER + row + "\n", encoding="utf-8")
        return "created"

    existing = topic_row_in_table(lines, topic_id, table_range)
    if existing is not None:
        lines[existing] = row
        ledger_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        return "replaced"

    # Insert before the first non-table line after the table (end of table).
    _, end = table_range
    lines.insert(end, row)
    ledger_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return "inserted"


def ledger_topic_inside_table(ledger_path: Path, topic_id: str) -> bool:
    """True when topic_id has a data row inside the first markdown table."""
    if not ledger_path.is_file():
        return False
    lines = ledger_path.read_text(encoding="utf-8").splitlines()
    table_range = first_markdown_table_range(lines)
    if table_range is None:
        return False
    return topic_row_in_table(lines, topic_id, table_range) is not None


def find_topic_rows_outside_table(ledger_path: Path) -> list[str]:
    """Return topic_ids that appear as table-looking rows outside the first table."""
    if not ledger_path.is_file():
        return []
    lines = ledger_path.read_text(encoding="utf-8").splitlines()
    table_range = first_markdown_table_range(lines)
    if table_range is None:
        return []
    start, end = table_range
    outside: list[str] = []
    row_re = re.compile(r"^\|\s*20\d{2}-\d{2}-\d{2}\s*\|\s*([A-Za-z]+\d+)\s*\|")
    for index, line in enumerate(lines):
        if start <= index < end:
            continue
        match = row_re.match(line)
        if match:
            outside.append(match.group(1).upper())
    return outside
