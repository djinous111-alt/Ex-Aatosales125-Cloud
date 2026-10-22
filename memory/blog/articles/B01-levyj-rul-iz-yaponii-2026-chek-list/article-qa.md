# Article QA — B01

**topic_id:** B01  
**slug:** levyj-rul-iz-yaponii-2026-chek-list  
**article_dir:** memory/blog/articles/B01-levyj-rul-iz-yaponii-2026-chek-list  
**date:** 2026-10-22  
**recheck:** after writer FIX (char_count 9487)  
**verdict:** PASS  
**score:** 86

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic official docs URL |
| fact-check | PASS | 5 extracted; verified 1 (2026); unverified: 2025, 2023, 30 минут, 243 129 (research / JAIA) |
| link-verify | PASS | 3/3 OK; 2GIS percent-encoded path |
| html-linter | PASS | 0 errors; TOC нет |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 62.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 11; pain 3; outcome 8 |
| human-voice | PASS | warning: 3× lists ровно по 5 шагов |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Страх депозита за правый руль / переделку / чужой рынок под ярлыком «левый руль из Японии» |
| Где решение | H2: задача по рулю → рынки → пакет до денег → Корея/Китай → чеклист 10 → что дальше |
| Первый результат | Заполненный чек + решение ставлю / меняю рынок / отказ до перевода |
| Термины «на пальцах» | LHD/RHD, аукцион vs шильдик, VIN/кузов, Encar, «под ключ» |
| Beginner-fit | PASS |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 actionable; CTA; нет 2–3 blog internal |
| GEO / citability | 22/25 | TL;DR, схема, таблица, FAQ×7, чеклист, явный pain/outcome |
| CORE-EEAT lite | 17/20 | 17/20 (Ept02 internal blog links) |
| Human voice | 14/15 | Script PASS; soft warning про 5-step lists |
| Fact safety | 13/15 | JAIA/export в research; soft fact-bank gap |
| Contract HTML | 10/10 | Whitelist + utility + link-verify + human-voice PASS |
| **Итого** | **86/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta/H1 |
| C02 | ✓ | Lead: боль депозита + чеклист |
| C03 | ✓ | Новичок, риск ложного LHD |
| C04 | ✓ | LHD/RHD, аукцион, VIN, Encar |
| O01 | ✓ | H2 = action outline |
| O02 | ✓ | Outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | TL;DR + критерий «готово» |
| R02 | ✓ | JAIA 243 129, август 2023, сроки-ориентир |
| R03 | ✓ | Нет цен лотов/% |
| R04 | ✓ | FAQ с прямого ответа |
| E01 | ✓ | Брокер Владивосток / марка vs аукцион |
| E02 | ✓ | Делать/Не делать + recommendation markers |
| E03 | ✓ | Каталог×2 + Telegram + 2GIS |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Красный флаг переделки руля |
| Ept02 | ✗ | Нет 2–3 internal blog links (Indexer) |

**Target:** ≥16/20 ✓ · veto: нет

## Link verify

- total: 3, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 62.9

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes | Review: no | E-E-A-T SameAs Author: pending (cover/schema)

## Blockers

- нет

## FIX cycle (QA)

1. FAIL#1 → writer: action markers 7→11; pain/outcome лексика; 2GIS encode; policy `pain_markers_ru`/`outcome_markers_ru` synced.  
2. Recheck: all required gates PASS → verdict PASS.

## FIX (non-blocking)

1. **Ept02:** 2–3 internal blog links после Indexer.  
2. **fact-bank soft:** JAIA 243 129 (2025), export limits 09.08.2023.  
3. **INC-0921:** `link_verify` должен IRI-quote сам (writer workaround уже в статье).  
4. **human-voice soft:** развести размер ol-списков.

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
