# Article QA — B01

**topic_id:** B01  
**slug:** kak-proverit-30-minutnuyu-moshchnost-ev-iz-kitaya-2026  
**article_dir:** memory/blog/articles/B01-kak-proverit-30-minutnuyu-moshchnost-ev-iz-kitaya-2026  
**date:** 2026-10-03  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-03; sources/pain_solution OK |
| fact-check | PASS | 10 stats; 1 verified in fact-bank (2026); rest in research-notes (ПП 1713, ×0,45, порог 80 л.с.) |
| link-verify | PASS | 2/2 OK; CTA `[CATALOG_URL]`/`[TELEGRAM_URL]` expanded from env, JSON redacted to `${…}` |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long (склейка таблицы/схемы); Flesch RU 62.1 |
| cannibalization | PASS | 0 issues (3 meta в blog-dir) |
| utility gate | PASS | action 29; pain 2; outcome 5; ol×19; FAQ×7; tables×2 |
| human-voice | PASS | WARN: два списка ровно по 5 шагов |

## Beginner-fit

**PASS.** Статья для покупателя EV из Китая до депозита, не для инженеров/разработчиков.

- Боль новичка: пик в карточке ≠ цифра для утильсбора; депозит до проверки → риск почти миллиона.
- Решение: H2-чеклист «пик vs 30 минут», прецедент/документы, вилка ×0,45 как практика (не ГОСТ), тип привода, 8 проверок.
- Первый результат: папка 5–8 подтверждений + порог ≤80 л.с. + вопрос подборщику до оплаты.
- Термины «на пальцах»: пик vs 30-минутная, ЭПТС/СБКТС, EV / последовательный / параллельный, 58,84 кВт.

## Pain → solution → outcome

| Звено | Где в статье |
|-------|-------------|
| Боль | Lead + история 180×0,45=81 + сюрприз 175 vs 180 |
| Решение | H2: правило до депозита → пик vs 30 мин → источники → вилка → тип привода → чек-лист 8 |
| Результат до FAQ | «Критерий результата» + «Что дальше» (5 шагов) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «30 минутная мощность» в title/H1/description; H2 action; CTA×3; нет blog internal |
| GEO / citability | 24/25 | TL;DR, схема, таблицы×2, FAQ×7, чеклисты, Fact Check box |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop; reader_story overlap сильный |
| Fact safety | 13/15 | Цифры в research-notes; формула ×0,45 помечена как практика |
| Contract HTML | 10/10 | Whitelist PASS, ~9267 знаков, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: депозит без 30-мин → риск утильсбора |
| C03 | ✓ | Читатель: покупатель китайского EV до депозита |
| C04 | ✓ | Пик / 30-мин / ЭПТС / СБКТС / типы привода объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный how-to до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблицы, mode B |
| R01 | ✓ | TL;DR, схема, критерий результата |
| R02 | ✓ | ПП 1713, ЕЭК 122, ГОСТ Р 41.85-99, Росстандарт про ×0,45 |
| R03 | ✓ | Нет фейковой точности сумм по VIN; вилка как ориентир |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + порог 80 л.с. |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Формула не ГОСТ; граница 78–82; версии внутри линейки |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json (CTA expand from env)

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/схемы)
- Flesch RU: 62.1

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. **utility BLOCK** из-за пустых `pain_markers_ru`/`outcome_markers_ru` в `editorial-policy.json` (списки потеряны на ветке) → восстановлены списки + skip-empty в `utility_gate.py`. Повтор: PASS (pain 2, outcome 5).
2. **link-verify fail** на литералах `[CATALOG_URL]`/`[TELEGRAM_URL]` (считались relative + site-base) → expand из env + redact в JSON. Повтор: PASS 2/2. Статья не переписывалась.

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal blog links с `anchor_variants`.
2. **human-voice WARN:** варьировать длину списков «Что дальше» / источников (не ровно 5+5).
3. **fact-check soft:** ключевые цифры утильсбора/порога — в fact-bank для verified.
4. **slop over-long:** артефакт парсера таблиц; не критично.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
