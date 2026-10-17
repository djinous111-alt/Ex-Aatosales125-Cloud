#!/usr/bin/env python3
"""Smoke: empty pain/outcome marker lists fail-fast with policy error, not weak-copy wording."""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from excalibur_blog_utility_gate import gate_article  # noqa: E402


SAMPLE_HTML = """
<article>
<p>Проблема: долго ждать и страшно платить депозит без таймлайна.</p>
<h2>Что сделать</h2>
<ol>
<li>Шаг 1 проверьте сроки моря</li>
<li>Шаг 2 проверьте СВХ</li>
<li>Шаг 3 проверьте ПТБ</li>
<li>Шаг 4 проверьте выдачу</li>
<li>Шаг 5 сравните обещания</li>
</ol>
<ul><li>чеклист</li><li>ориентир</li></ul>
<blockquote><p>результат: сможете заполнить чеклист до оплаты</p></blockquote>
<h2>Частые вопросы</h2>
<h3>Сколько идет море?</h3>
<p>2–3 суток ориентир.</p>
<h3>Что спросить до депозита?</h3>
<p>Проверьте диапазон этапов.</p>
<h3>До Москвы то же?</h3>
<p>Нет, это отдельный срок.</p>
<h3>Ровно N дней?</h3>
<p>Красный флаг — избегайте.</p>
<h3>Что в итоге получите?</h3>
<p>Сможете выбрать офер без магии сроков.</p>
</article>
"""


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        article_dir = Path(tmp)
        (article_dir / "article.html").write_text(SAMPLE_HTML, encoding="utf-8")
        (article_dir / "article.meta.json").write_text(
            json.dumps({"article_mode": "B", "char_count": 9000}, ensure_ascii=False),
            encoding="utf-8",
        )
        empty_policy = {
            "policy_id": "test_empty_markers",
            "allowed_article_mode": ["B"],
            "article_required_signals": {
                "min_numbered_steps": 5,
                "min_actionable_h2": 1,
                "min_faq_pairs": 5,
                "min_recommendation_markers": 1,
                "min_pain_markers": 2,
                "min_outcome_markers": 3,
                "requires_workflow_or_table_or_checklist": True,
            },
            "recommendation_markers_ru": ["проверьте", "чеклист", "ориентир", "избегайте", "сделайте"],
            "pain_markers_ru": [],
            "outcome_markers_ru": [],
            "water_phrases_ru": [],
        }
        report = gate_article(article_dir, empty_policy)
        errors = " ".join(report.get("errors") or [])
        if report.get("status") != "BLOCK":
            print("FAIL: expected BLOCK for empty marker lists")
            return 1
        if "pain_markers_ru пуст" not in errors and "editorial-policy.json: pain_markers_ru" not in errors:
            print(f"FAIL: expected policy empty-list error, got: {report.get('errors')}")
            return 1
        if "слабо раскрыта боль" in errors:
            print("FAIL: should fail-fast on policy, not blame article copy")
            return 1
        print("OK utility_gate empty markers fail-fast")
        return 0


if __name__ == "__main__":
    sys.exit(main())
