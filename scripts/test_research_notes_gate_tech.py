#!/usr/bin/env python3
"""Smoke tests for research-notes technical_topic detection (INC-20261017-1714)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_research_notes_gate import (  # noqa: E402
    _tech_marker_hit,
    is_technical_topic,
)


def test_short_ascii_marker_needs_boundary() -> None:
    assert _tech_marker_hit("ai", "ai agent workflow") is True
    assert _tech_marker_hit("ai", "reader_pain: новичок боится депозита") is False
    assert _tech_marker_hit("api", "rest api docs") is True
    assert _tech_marker_hit("api", "capibara") is False


def test_reader_pain_field_name_not_technical() -> None:
    notes = """
research_date: 2026-10-17
reader_pain: новичок не знает, что проверить до депозита
reader_outcome: чеклист из 12 пунктов
success_criteria: решение ставлю / жду / отказываюсь
voice_angle: спокойный практик
reader_story: заказ из Китая через Владивосток
surprising_fact: договор без ИНН
accessed_at: 2026-10-17
"""
    context = {
        "topic": {
            "h1": "Как заказать авто из Китая: чеклист до депозита",
            "primary_query": "как заказать авто из китая",
            "slug": "kak-zakazat-avto-iz-kitaya-chek-list-do-depozita-2026",
            "search_intent": "checklist",
            "secondary_queries": [],
        }
    }
    assert is_technical_topic(context, notes) is False


def test_explicit_ai_topic_is_technical() -> None:
    notes = "reader_pain: не умею подключить AI agent к MCP"
    context = {
        "topic": {
            "h1": "Как подключить AI agent к MCP",
            "primary_query": "ai agent mcp",
            "slug": "ai-agent-mcp",
            "search_intent": "how_to",
            "secondary_queries": ["cursor mcp"],
        }
    }
    assert is_technical_topic(context, notes) is True


def main() -> int:
    test_short_ascii_marker_needs_boundary()
    test_reader_pain_field_name_not_technical()
    test_explicit_ai_topic_is_technical()
    print("PASS test_research_notes_gate_tech")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
