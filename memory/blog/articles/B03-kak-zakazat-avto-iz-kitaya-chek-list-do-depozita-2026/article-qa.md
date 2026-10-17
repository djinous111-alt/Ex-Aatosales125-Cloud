# Article QA — B03 (re-run after Writer FIX1)

**topic_id:** B03  
**slug:** kak-zakazat-avto-iz-kitaya-chek-list-do-depozita-2026  
**article_dir:** memory/blog/articles/B03-kak-zakazat-avto-iz-kitaya-chek-list-do-depozita-2026  
**date:** 2026-10-17  
**verdict:** FAIL  
**score:** 78  
**qa_cycle:** 2 (after FIX1)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-17 |
| utility gate | **PASS** | action_markers **33** ≥ 8 |
| human-voice-gate | **BLOCK** | Fact Check Box: нет фразы «Материал проверен» |
| fact-check | PASS | 2 stats; unverified «37 дней» |
| link-verify | PASS | 3/3 OK |
| html-linter | PASS | whitelist OK |
| slop-detector | WARNING | 0 cliches; 6 over-long; Flesch RU 55.1 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; нет blog internal |
| GEO / citability | 23/25 | insight «Коротко», таблица, чеклист 12, FAQ×7 |
| CORE-EEAT lite | 17/20 | ≥16 ✓ |
| Human voice | 8/15 | gate **BLOCK** — сломан Fact Check anchor |
| Fact safety | 12/15 | «37 дней» не в fact-bank |
| Contract HTML | 10/10 | whitelist PASS |
| Utility gate | 10/10 | PASS (33 markers) |
| **Итого** | **78/100** | veto human-voice BLOCK |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01–C04 | ✓ | Primary + lead pain + новичок + термины |
| O01–O04 | ✓ | Outline до депозита, FAQ 7, mode B |
| R01–R04 | ✓ | insight + критерий готово + FAQ |
| E01–E03 | ✓ | Угол + Сделайте/Не делайте + CTA |
| Exp01–Exp03 | ✓ | Mode B, тон Авто-Сейлс, slop=0 |
| Ept01 | ✓ | Лимиты пошлин / возврат в договоре |
| Ept02 | ✗ | Нет internal blog links |

**Target:** ≥16/20 ✓ · veto: human-voice BLOCK

## Pain / solution / beginner-fit

| Критерий | Статус |
|----------|--------|
| Боль в lead | ✓ |
| Решение в H2 | ✓ |
| Результат до FAQ | ✓ критерий «готово» |
| Beginner-fit | ✓ |
| Utility markers | ✓ 33 |

## Blockers

1. **human-voice BLOCK:** Fact Check Box must contain exact phrase **«Материал проверен»** inside a `<blockquote>` before FAQ.  
   Сейчас: `<b>Проверка редакции:</b>…` — gate не находит блок (`extract_fact_check_block` ищет substring `материал проверен`).  
   Также в блоке должно фигурировать имя из registry: **«Редакция Авто-Сейлс»** (`author_id=avtosales-editorial`).

## FIX cycle (QA) — вернуть writer (цикл 2)

1. **Обязательно:** в blockquote перед FAQ вернуть якорь `Материал проверен:` (можно варьировать остальной текст «Достоверность данных» / источники, но **не** убирать эту фразу). Пример каркаса:
   - `Материал проверен: Редакция Авто-Сейлс (…)`  
   - вторая строка про источники/дату — свободная формулировка (не копия generic Wordstat).
2. **Не ломать:** utility markers (Сделайте/Не делайте/чеклист/избегайте), insight без TL;DR, списки ≠5 где уже поправлено.
3. После правки: `human_voice_gate` → PASS, затем GEO QA re-score.

## Gate checklist

- score ≥ 80 → **78** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- research-notes PASS ✓  
- utility PASS ✓  
- human-voice PASS ✗  
- link-verify PASS ✓  

**Итог:** FAIL — **cover \|\| schema не запускать**; writer FIX cycle 2 (Fact Check phrase).
