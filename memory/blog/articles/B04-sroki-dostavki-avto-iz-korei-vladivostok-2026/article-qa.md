# Article QA — B04

**topic_id:** B04  
**slug:** sroki-dostavki-avto-iz-korei-vladivostok-2026  
**article_dir:** memory/blog/articles/B04-sroki-dostavki-avto-iz-korei-vladivostok-2026  
**date:** 2026-10-18  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-18; technical_topic=false; pain/outcome/map OK |
| utility gate | PASS | action_markers 9; pain 4; outcome 5; FAQ×7; table×1; ol items 18 |
| human-voice | PASS | warning: 3× exactly-5-step lists; fact-check template OK; story/pain overlap OK |
| fact-check | PASS | 8 stats; verified 3 / unverified 5 (диапазоны этапов — в research-notes, не в fact-bank) |
| link-verify | PASS | 2/2 OK (catalog + Telegram); `--site-base` from PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (склейка table/blockquote парсером); Flesch RU 58.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Путает море ~2 суток с полным циклом до выдачи; платит депозит под «ровно N дней» (lead + история Сергея) |
| Где решение | H2: этапы → ориентиры 2026 → пакет до СВХ → Влад. vs дальше по РФ → красные флаги → чек-лист до депозита |
| Первый результат | Заполненный чек-лист до депозита; письменные диапазоны по этапам; ясное «Владивосток ≠ Москва» (секция до FAQ) |
| Термины «на пальцах» | СВХ, СБКТС, ЭПТС, фрахт объяснены в теле; нет API/RAG/проф-жаргона |

**Beginner-fit:** PASS

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2/FAQ; CTA catalog×3+TG; нет 2–3 blog internal |
| GEO / citability | 24/25 | «Коротко», таблица этапов, FAQ×7, чек-листы, цитируемые диапазоны |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | PASS; soft: 3 списка ровно по 5 шагов |
| Fact safety | 12/15 | Ориентиры с оговорками; 5 unverified vs fact-bank (есть в research-notes) |
| Contract HTML | 10/10 | Whitelist PASS, ~9.5k chars, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «доставка авто из кореи» в meta title / H1 |
| C02 | ✓ | Lead: море ≠ полный цикл + депозит под «ровно N дней» |
| C03 | ✓ | Читатель: новичок под заказ из Кореи до Владивостока |
| C04 | ✓ | СВХ / СБКТС / ЭПТС / фрахт объяснены |
| O01 | ✓ | H2 = research outline (этапы → 2026 → пакет → Влад. vs РФ → флаги → чек-лист → FAQ) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица, mode B |
| R01 | ✓ | Insight, таймлайн-таблица, чек-лист, FAQ |
| R02 | ✓ | SASCO ~2 суток; апрель 2026 посты ~10 дней vs 3–5 |
| R03 | ✓ | Диапазоны + «не гарантия»; без фикс-цен пошлин |
| R04 | ✓ | FAQ-ответ в 1-м предложении |
| E01 | ✓ | «Море короткое, нервы длинные» + Авто-Сейлс Влад. |
| E02 | ✓ | «Делать / Не делать» в H2-секциях |
| E03 | ✓ | CTA: каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake «я лично» |
| Exp02 | ✓ | Тон research / редакция Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: ориентиры рынка, Влад. ≠ Москва, рейс/лаборатория |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт table/blockquote)
- Flesch RU: 58.9

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чек-листы) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все gates PASS с первого прогона GEO QA)

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних B0x — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** диапазоны 20–45 / море 1–3 / этапы — дописать в fact-bank для verified.
3. **human-voice soft:** разнести размеры списков (сейчас 3× ровно 5 шагов).
4. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
