# Article QA — B01

**topic_id:** B01  
**slug:** ustanovka-era-glonass-na-vvezennyy-avto-2026  
**article_dir:** memory/blog/articles/B01-ustanovka-era-glonass-na-vvezennyy-avto-2026  
**date:** 2026-09-29  
**verdict:** PASS  
**score:** 86

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | status PASS; research_date=2026-09-29 |
| utility gate | PASS | action_markers 10; pain 10; outcome 13; ol 16; FAQ×6; table×1 |
| human-voice | PASS | WARN: 3× exactly-5-step lists; concrete + story overlap OK |
| fact-check | PASS | 5 stats; 1 verified (2026); 4 unverified vs fact-bank (01.10.2022, 2027, 855, 35 000) — в research-notes |
| link-verify | PASS | 3/3 OK (855.aoglonass.ru + каталог + Telegram); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 55.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Путаница «с 01.04.2026 всем обязательно» vs мораторий для физлиц; страх гаражной кнопки и отказа без ЭПТС |
| Где решение | H2: развилка статуса → устаревшие SEO → карта 855 → чек-лист документов → полный комплект → тест-вызов → СБКТС/ЭПТС → план на сегодня |
| Первый результат | За 20–30 мин: статус физлицо/ИП, центр с карты, папка документов, критерий «акт + паспорт УВЭОС + тест-вызов» |
| Термины «на пальцах» | УВЭОС = кнопка SOS; СБКТС; ЭПТС — объяснены в lead после инсайт-блока |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «установка эра глонасс» в H1/H2; FAQ×6; CTA каталог+Telegram; мало внутренних blog-links |
| GEO / citability | 23/25 | Инсайт, таблица статуса, схема → ЭПТС, чек-лист 11, FAQ |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 14/15 | PASS; WARN одинаковые 5-шаговые ol |
| Fact safety | 12/15 | Даты/цены в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9216 знаков, FAQ, CTA≤3, без форм |
| **Итого** | **86/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в title/H1 |
| C02 | ✓ | Lead: история Сергея + прямой ответ (мораторий / чек-лист) |
| C03 | ✓ | Читатель: ввоз через Владивосток, физлицо vs ИП |
| C04 | ✓ | УВЭОС / СБКТС / ЭПТС / карта 855 объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичная цепочка до ЭПТС |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | Инсайт-блок + схема + FAQ |
| R02 | ✓ | 01.10.2022, мораторий, ориентиры цен — в research-notes |
| R03 | ✓ | Цены как ориентиры, не прайс Авто-Сейлс |
| R04 | ✓ | FAQ отвечает действием в 1-м предложении |
| E01 | ✓ | Угол «чек-лист до ЭПТС» + SEO vs Минпромторг |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Мораторий ещё действует; гараж vs карта 855 |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Soft WARN:** три `<ol>` ровно по 5 пунктов (human-voice)

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 55.6

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/ol) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (после QA-фиксов: CTA href + policy pain/outcome markers)

## FIX cycle (QA)

1. Utility gate BLOCK → в `editorial-policy.json` не было `pain_markers_ru` / `outcome_markers_ru`, при этом скрипт требовал min 2/3 → gate всегда BLOCK. Добавлены маркеры + guard в `excalibur_blog_utility_gate.py`. Повтор: PASS.
2. link-verify FAIL → в `article.html` литералы `href="[REDACTED]"` вместо CTA. Восстановлены URL каталога и Telegram по образцу AS09 / conversion-map. Повтор: PASS 3/3.

## FIX (non-blocking / optional for writer)

1. **Ept02:** 2–3 internal blog links на соседние гайды (СБКТС/ЭПТС и т.п.) с `anchor_variants`.
2. **human-voice WARN:** разнести длины ol (не три списка ровно по 5).
3. **fact-bank soft:** дописать 01.10.2022, ПП 855, ориентир 35 000 ₽.
4. **Инсайт-лейбл:** skill рекомендует не начинать инсайт с `TL;DR` / `Быстрый инсайт` (как у AS09 — soft).

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
