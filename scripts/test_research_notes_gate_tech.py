#!/usr/bin/env python3
"""Regression: automotive notes with reader_pain must not flip technical_topic=true."""
from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from excalibur_blog_research_notes_gate import is_technical_topic  # noqa: E402


def main() -> int:
    auto_context = {
        "topic": {
            "h1": "Перегон авто из Владивостока своим ходом",
            "primary_query": "перегон авто из владивостока своим ходом",
            "secondary_queries": ["сколько стоит перегон", "документы для перегона"],
            "search_intent": "how_to",
            "slug": "peregon-avto-iz-vladivostoka-svoim-hodom-2026",
        }
    }
    # Intentionally contains substrings that used to false-positive:
    # "ai" inside reader_pain, "страховой агент", field name reader_pain.
    notes = """
## reader_pain
reader_pain: боюсь, что без ОСАГО и диагностической карты меня остановят на трассе.
Страховой агент обещал помочь, но я не уверен.

## reader_outcome
reader_outcome: понятный чек-лист до выезда
"""
    tech = is_technical_topic(auto_context, notes)
    if tech:
        print("FAIL: automotive topic marked technical_topic=true (false positive)", file=sys.stderr)
        return 1

    tech_context = {
        "topic": {
            "h1": "Как подключить MCP к Cursor AI",
            "primary_query": "cursor ai mcp setup",
            "secondary_queries": ["make.com automation"],
            "search_intent": "how_to",
            "slug": "cursor-ai-mcp-setup-2026",
        }
    }
    tech_notes = "github.com evidence for cursor ai and make.com workflow"
    if not is_technical_topic(tech_context, tech_notes):
        print("FAIL: clear tech topic should be technical_topic=true", file=sys.stderr)
        return 1

    # reader_pain alone must not make a neutral topic technical via substring "ai"
    neutral = {
        "topic": {
            "h1": "Как оформить документы",
            "primary_query": "оформить документы",
            "secondary_queries": [],
            "search_intent": "how_to",
            "slug": "oformit-dokumenty-2026",
        }
    }
    pain_only = "reader_pain: страх ошибки в бумагах; не про ai-инструменты"
    # "ai-" might still match \bai\b depending on boundaries — ensure auto short-circuit
    # isn't needed; bounded \bai\b should not match inside "ошибки" / "reader_pain"
    if is_technical_topic(neutral, "reader_pain: боюсь штрафа на посту"):
        print("FAIL: plain pain notes marked technical", file=sys.stderr)
        return 1

    print("PASS: research_notes_gate technical_topic regression")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
