#!/usr/bin/env python3
"""Regression tests for research-notes gate (false technical topic)."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from excalibur_blog_research_notes_gate import (  # noqa: E402
    _marker_in_blob,
    is_technical_topic,
    validate_research_notes,
)


class TechMarkerTests(unittest.TestCase):
    def test_short_marker_word_boundary(self) -> None:
        self.assertFalse(_marker_in_blob("авто из кореи или китая", "ai"))
        self.assertFalse(_marker_in_blob("боль: сложно выбрать в азии", "ии"))
        self.assertTrue(_marker_in_blob("настройка ai агента", "ai"))
        self.assertTrue(_marker_in_blob("локальный ии помощник", "ии"))

    def test_auto_niche_not_technical(self) -> None:
        context = {
            "topic": {
                "h1": "Авто из Кореи или Китая 2026: что выбрать",
                "primary_query": "авто из кореи или китая",
                "secondary_queries": "корея или китай авто",
                "search_intent": "comparison",
                "slug": "avto-iz-korei-ili-kitaya-2026",
            }
        }
        notes = (
            "reader_pain: сложно выбрать страну и не потерять деньги на растаможке\n"
            "reader_outcome: сравните корейский и китайский вариант по чеклисту\n"
            "## github_evidence\n"
            "- n/a for auto niche\n"
            "## action_outline\n"
            "1. шаг\n"
        )
        self.assertFalse(is_technical_topic(context, notes))
        # Required heading must not force technical_topic=true.
        self.assertFalse(
            is_technical_topic(
                context,
                "reader_pain: боль\n## github_evidence\n- https://github.com/x/y\n",
            )
        )


class AccessedAtTests(unittest.TestCase):
    def test_iso_dates_in_source_table_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            article = Path(tmp)
            (article / "research-context.json").write_text(
                '{"date_context":{"today_iso":"2026-10-12","year":2026,'
                '"freshness_window":{"prefer_sources_after":"2026-07-14"}}}',
                encoding="utf-8",
            )
            rows = "\n".join(
                f"| src{i} | https://example{i}.com/a | 2026-10-12 |" for i in range(1, 6)
            )
            notes = f"""# research
research_date: 2026-10-12
reader_pain: сложно выбрать
reader_outcome: выберите по чеклисту
success_criteria: понятный выбор
voice_angle: сравнение без воды
reader_story: покупатель впервые
surprising_fact: пошлина отличается
## pain_solution_map
| боль | решение | результат |
| a | b | c |
| d | e | f |
| g | h | i |
## github_evidence
- n/a
## action_outline
1. шаг один
2. шаг два
3. шаг три
4. шаг четыре
5. шаг пять
utility_verdict: PASS
## wordstat
показы: 100
## source_table
| name | url | accessed |
{rows}
https://docs.example.com/help
https://a.com https://b.com https://c.com https://d.com https://e.com https://f.com https://g.com https://h.com
"""
            (article / "research-notes.md").write_text(notes, encoding="utf-8")
            report = validate_research_notes(article)
            self.assertGreaterEqual(report["metrics"]["accessed_at"], 5)
            self.assertFalse(report["metrics"]["technical_topic"])


if __name__ == "__main__":
    raise SystemExit(unittest.main())
