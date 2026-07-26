#!/usr/bin/env python3
"""Smoke checks for research-notes technical-topic marker matching.

Short tokens (ai/ии/api/mcp/rag) must use non-letter boundaries so ordinary
Russian words like «регистрации» do not flip technical_topic=true.
"""
from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from excalibur_blog_research_notes_gate import is_technical_topic  # noqa: E402


def main() -> int:
    auto_ctx = {
        "topic": {
            "h1": "Как поставить авто на учёт после ЭПТС: чек-лист документов и шагов 2026",
            "primary_query": "документы для постановки авто на учет",
            "secondary_queries": "постановка авто на учет в гибдд 2026",
            "search_intent": "checklist",
            "slug": "postanovka-na-uchet-avto-posle-epts-2026",
        }
    }
    auto_notes = (
        "reader_pain: непонятно с чего начать регистрацию после ЭПТС.\n"
        "В регистрации часто путают ОСАГО и техосмотр.\n"
    )
    if is_technical_topic(auto_ctx, auto_notes):
        print("FAIL: auto-registration topic must not be technical_topic")
        return 1

    it_ctx = {
        "topic": {
            "h1": "Как настроить MCP сервер в Cursor",
            "primary_query": "mcp cursor настройка",
            "secondary_queries": "api rag агент",
            "search_intent": "how_to",
            "slug": "nastroit-mcp-cursor",
        }
    }
    it_notes = "Нужен MCP и API ключ для RAG workflow.\n"
    if not is_technical_topic(it_ctx, it_notes):
        print("FAIL: MCP/API topic must be technical_topic")
        return 1

    # Bare «ии» as a word should still match; substring inside регистрации must not.
    ii_only = {
        "topic": {
            "h1": "Что такое ИИ для новичка",
            "primary_query": "ии для бизнеса",
            "secondary_queries": "",
            "search_intent": "how_to",
            "slug": "ii-dlya-novichka",
        }
    }
    if not is_technical_topic(ii_only, "кратко про ии\n"):
        print("FAIL: whole-word «ии» must still mark technical topic")
        return 1

    print("PASS: research-notes tech marker smoke checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
