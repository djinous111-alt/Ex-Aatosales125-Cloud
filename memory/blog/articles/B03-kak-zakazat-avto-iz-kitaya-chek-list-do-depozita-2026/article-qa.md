# Article QA — B03

**topic_id:** B03  
**slug:** kak-zakazat-avto-iz-kitaya-chek-list-do-depozita-2026  
**article_dir:** memory/blog/articles/B03-kak-zakazat-avto-iz-kitaya-chek-list-do-depozita-2026  
**date:** 2026-10-17  
**verdict:** FAIL  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-17; errors=[] |
| utility gate | **BLOCK** | action_markers 5 < 8 (см. FIX) |
| human-voice-gate | PASS | warnings: fact-check template; 4× exactly-5 lists |
| fact-check | PASS | 2 stats; unverified: «37 дней» (есть в research-notes) |
| link-verify | PASS | 3/3 OK (catalog, telegram, 2gis) |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 cliches; 6 over-long (таблица/списки); Flesch RU 56.0 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; H2 actionable; нет 2–3 blog internal |
| GEO / citability | 22/25 | insight, таблица, чек-лист 12, FAQ×7; ярлык «TL;DR / Быстрый инсайт» — шаблон |
| CORE-EEAT lite | 17/20 | ≥16 ✓ (см. ниже) |
| Human voice | 12/15 | gate PASS; шаблон Fact Check + одинаковые 5-step списки |
| Fact safety | 12/15 | «37 дней» не в fact-bank |
| Contract HTML | 10/10 | whitelist PASS, FAQ, CTA, без форм |
| Utility gate | **0/0 veto** | BLOCK → итог FAIL |
| **Итого** | **74/100** | veto utility |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как заказать авто из китая» в title/H1 |
| C02 | ✓ | Lead: депозит без договора → стоп + чек-лист |
| C03 | ✓ | Новичок, Telegram-скрин, страх депозита |
| C04 | ✓ | ИНН/ОГРН, инвойс, VIN, расчётный счёт объяснены |
| O01 | ✓ | H2 = рамка → канал → смета → договор → инвойс → флаги → 12 пунктов |
| O02 | ✓ | Логичный outline до депозита only |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | insight + критерий «готово» + FAQ |
| R02 | ✓ | ~37 дней + EV export 01.01.2026 в research-notes |
| R03 | ✓ | Нет самодельных пошлин/% |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» |
| E02 | ✓ | «Делать / Не делать» в секциях (но маркеры CLI другие) |
| E03 | ✓ | CTA: catalog×2 + Telegram×2 + 2GIS |
| Exp01 | ✓ | Mode B, без fake «я лично» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: не калькулятор пошлин; возврат смотреть в договоре |
| Ept02 | ✗ | Нет internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto utility BLOCK

## Pain / solution / beginner-fit

| Критерий | Статус | Деталь |
|----------|--------|--------|
| Боль новичка | ✓ (контент) | Lead: скрин + «депозит сегодня» без договора |
| Решение в H2 | ✓ | Канал/договор/смета/инвойс/флаги/12 пунктов |
| Первый результат до FAQ | ✓ | «Критерий готово» + решение ставлю/жду/отказ |
| Термины «на пальцах» | ✓ | Инвойс, расчётный счёт, ИНН/ОГРН, VIN |
| Beginner-fit | ✓ | Без тона «для профи»; первый шаг = рамка и сверка |

Utility CLI не считает «Делать/Не делать» и «чек-лист» — см. FIX.

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/списков)
- Flesch RU: 56.0

## Schema ready

BlogPosting: pending (FAIL) | FAQPage: yes (7) | HowTo: yes | Review: no

## Blockers

1. **utility gate BLOCK:** `action_markers=5 < 8`  
   Сейчас в тексте: `проверьте`×3 + `ориентир`×2.  
   Нет: `сделайте` / `не делайте` / `чеклист` (без дефиса) / `избегайте` / `используйте` / `шаг `.  
   Формулировки «Делать:» / «Не делать:» и «чек-лист» **не** входят в `recommendation_markers_ru`.

## FIX cycle (QA) — вернуть writer (цикл 1)

1. **Обязательно (utility):** довести action-маркеры до ≥8. Варианты без ломки смысла:
   - заменить «Делать:» → «Сделайте:», «Не делать:» → «Не делайте:» (минимум в 3–4 секциях);
   - 1–2 раза написать «чеклист» (без дефиса) рядом с «чек-лист»;
   - добавить «избегайте» / «используйте» / «проверьте» в финальный ol («Что сделать сегодня»).
2. **Желательно (human-voice WARN):** убрать ярлык `TL;DR / Быстрый инсайт` из первого blockquote — оставить суть инсайта; варьировать Fact Check wording; один из списков сделать не ровно 5 пунктов.
3. **Не трогать:** whitelist HTML, CTA domains, angle «до депозита», FAQ×7.

После правки: повтор `utility_gate` + `human_voice_gate` → затем GEO QA re-score.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- utility gate PASS ✗  

**Итог:** FAIL — cover \|\| schema **не** запускать; вернуть `excalibur-blog-writer` с FIX выше.
