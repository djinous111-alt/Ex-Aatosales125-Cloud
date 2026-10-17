# Article QA — B03 (re-run after Writer FIX2)

**topic_id:** B03  
**slug:** kak-zakazat-avto-iz-kitaya-chek-list-do-depozita-2026  
**article_dir:** memory/blog/articles/B03-kak-zakazat-avto-iz-kitaya-chek-list-do-depozita-2026  
**date:** 2026-10-17  
**verdict:** PASS  
**score:** 88  
**qa_cycle:** 3 (after FIX2)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-17 |
| utility gate | PASS | action_markers **33** ≥ 8 |
| human-voice-gate | PASS | `-o human-voice-report.json`; WARN: Fact Check template + exactly-5 lists |
| fact-check | PASS | 2 stats; unverified «37 дней» (в research-notes) |
| link-verify | PASS | 3/3 OK (catalog, telegram, 2gis) |
| html-linter | PASS | whitelist OK; TOC нет |
| slop-detector | WARNING | 0 cliches; 6 over-long; Flesch RU 54.8 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; нет 2–3 blog internal |
| GEO / citability | 23/25 | «Коротко», таблица, чеклист 12, FAQ×7 |
| CORE-EEAT lite | 14/15 | checklist 17/20 |
| Human voice | 13/15 | PASS; WARN template + 5-step lists |
| Fact safety | 12/15 | «37 дней» не в fact-bank |
| Contract HTML | 10/10 | whitelist, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как заказать авто из китая» в title/H1 |
| C02 | ✓ | Lead: депозит без договора → стоп + чеклист |
| C03 | ✓ | Новичок, Telegram-скрин, страх депозита |
| C04 | ✓ | ИНН/ОГРН, инвойс, VIN, расчётный счёт |
| O01 | ✓ | H2 = рамка → канал → смета → договор → инвойс → флаги → 12 пунктов |
| O02 | ✓ | Outline до депозита only |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | insight + критерий «готово» + FAQ |
| R02 | ✓ | ~37 дней + EV export 01.01.2026 в research-notes |
| R03 | ✓ | Нет самодельных пошлин/% |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» |
| E02 | ✓ | Сделайте / Не делайте |
| E03 | ✓ | CTA catalog + Telegram + 2GIS |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: не калькулятор пошлин |
| Ept02 | ✗ | Нет internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Критерий | Статус | Деталь |
|----------|--------|--------|
| Боль новичка | ✓ | Lead: скрин + «депозит сегодня» без договора |
| Решение в H2 | ✓ | Канал / договор / смета / инвойс / флаги / 12 пунктов |
| Первый результат до FAQ | ✓ | Критерий «готово» + ставлю/жду/отказ |
| Термины «на пальцах» | ✓ | Инвойс, расчётный счёт, ИНН/ОГРН, VIN |
| Beginner-fit | ✓ | Без тона «для профи» |
| Utility markers | ✓ | 33 |

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/списков)
- Flesch RU: 54.8

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes | Review: no | E-E-A-T SameAs Author: pending (cover/schema)

## Blockers

- нет

## FIX history

1. FIX1: action_markers / чеклист / императивы → utility PASS  
2. FIX2: восстановлен якорь «Материал проверен» + «Редакция Авто-Сейлс» → human-voice PASS  

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal links.  
2. **fact-check soft:** «37 дней» → fact-bank.  
3. **human-voice WARN:** варьировать вторую строку Fact Check / один список ≠5 (не ломая якорь «Материал проверен»).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- research-notes PASS ✓  
- utility PASS ✓  
- human-voice PASS ✓ (`human-voice-report.json`)  
- link-verify PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
