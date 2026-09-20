#!/usr/bin/env python3
"""Regression checks for AS|B topic ids and research tech-marker false positives."""
from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from excalibur_blog_topic_ids import (  # noqa: E402
    TOPIC_ID_RE,
    iter_topic_cards,
    topic_id_from_article_dirname,
)
from excalibur_blog_research_notes_gate import (  # noqa: E402
    count_accessed_at,
    is_technical_topic,
)
from excalibur_blog_link_verify import is_literal_redacted_href  # noqa: E402


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def test_topic_ids() -> None:
    assert_true(topic_id_from_article_dirname("AS10-aukcionnyj-list") == "AS10", "AS10 dirname")
    assert_true(topic_id_from_article_dirname("B09-llms") == "B09", "B09 dirname")
    assert_true(topic_id_from_article_dirname("notes") is None, "non-topic dirname")
    assert_true(bool(TOPIC_ID_RE.fullmatch("AS01")), "AS01 fullmatch")
    assert_true(bool(TOPIC_ID_RE.fullmatch("B12")), "B12 fullmatch")
    assert_true(not TOPIC_ID_RE.fullmatch("C01"), "C01 rejected")

    sample = "## AS10 — Тема\n\n- **priority:** P0\n\n---\n## B01 — Legacy\n\n- **priority:** P1\n"
    cards = list(iter_topic_cards(sample))
    assert_true([c[0] for c in cards] == ["AS10", "B01"], f"cards={cards}")


def test_tech_markers_false_positive() -> None:
    auto_ctx = {
        "topic": {
            "topic_id": "AS10",
            "h1": "Как читать аукционный лист Японии",
            "primary_query": "аукционный лист японии как читать",
            "secondary_queries": ["оценки uss", "auction sheet"],
            "search_intent": "how_to",
            "slug": "aukcionnyj-list-yaponii-kak-chitat",
        }
    }
    notes = (
        "research_date: 2026-07-20\n"
        "reader_pain: не понимаю оценки\n"
        "reader_outcome: читаю лист до ставки\n"
        "## github_evidence\n\nn/a — не tech-тема, scrapers не равны USS sheet\n"
    )
    assert_true(
        is_technical_topic(auto_ctx, notes) is False,
        "AS10 + Японии/reader_pain must not be technical_topic",
    )

    tech_ctx = {
        "topic": {
            "topic_id": "B01",
            "h1": "Как подключить MCP агент в Cursor",
            "primary_query": "cursor mcp agent",
            "secondary_queries": ["n8n workflow"],
            "search_intent": "how_to",
            "slug": "cursor-mcp-agent",
        }
    }
    assert_true(is_technical_topic(tech_ctx, "notes") is True, "MCP/Cursor topic is technical")


def test_accessed_at_iso_rows() -> None:
    table = """
| source | url | accessed |
| a | https://example.com/a | 2026-07-20 |
| b | https://example.com/b | 2026-07-20 |
| c | https://example.com/c | 2026-07-20 |
| d | https://example.com/d | 2026-07-20 |
| e | https://example.com/e | 2026-07-20 |
"""
    assert_true(count_accessed_at(table) >= 5, "ISO dates on source rows count as accessed_at")


def test_redacted_href() -> None:
    assert_true(is_literal_redacted_href("https://[REDACTED]/"), "redacted host")
    assert_true(is_literal_redacted_href("[REDACTED]"), "bare redacted")
    assert_true(not is_literal_redacted_href("https://example.com/catalog"), "live url ok")


def main() -> int:
    test_topic_ids()
    test_tech_markers_false_positive()
    test_accessed_at_iso_rows()
    test_redacted_href()
    print("OK: excalibur_blog_topic_id_regression")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
