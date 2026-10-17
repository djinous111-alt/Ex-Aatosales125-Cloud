#!/usr/bin/env python3
"""Regression: tech-marker detection must use word boundaries, not substrings.

Auto/logistics notes that contain ``reader_pain`` / Russian morphology like
``ожидании`` must NOT be classified as technical (no GitHub evidence required).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from excalibur_blog_research_notes_gate import is_technical_topic  # noqa: E402


def main() -> int:
    auto_context = {
        "topic": {
            "h1": "Сроки доставки авто из Кореи во Владивосток",
            "primary_query": "доставка авто из кореи",
            "secondary_queries": ["сроки доставки авто из кореи"],
            "search_intent": "checklist",
            "slug": "sroki-dostavki-avto-iz-korei-vladivostok-2026",
        }
    }
    # Contains required field name reader_pain and Russian «ожидании» (has «ии»).
    auto_notes = (
        "## reader_pain\n"
        "Новичок в ожидании машины путает море с полным циклом.\n"
        "reader_pain: страх депозита под обещание ровно N дней.\n"
        "## reader_outcome\n"
        "Таймлайн по этапам до Владивостока.\n"
    )
    if is_technical_topic(auto_context, auto_notes):
        print("FAIL: auto niche falsely flagged as technical (substring match?)")
        return 1

    tech_context = {
        "topic": {
            "h1": "Как настроить MCP agent в Cursor",
            "primary_query": "cursor mcp agent",
            "secondary_queries": ["github docker rag"],
            "search_intent": "how_to",
            "slug": "cursor-mcp-agent-setup",
        }
    }
    tech_notes = "Нужен GitHub evidence и API workflow для агента.\n"
    if not is_technical_topic(tech_context, tech_notes):
        print("FAIL: obvious tech niche not detected")
        return 1

    # Short marker inside a longer Latin token must not match.
    if is_technical_topic(
        {"topic": {"h1": "plain logistics", "primary_query": "wait", "slug": "x"}},
        "waiting for shipment details only\n",
    ):
        print("FAIL: 'ai' matched inside 'waiting'")
        return 1

    print("OK research_notes_gate tech word-boundary")
    return 0


if __name__ == "__main__":
    sys.exit(main())
