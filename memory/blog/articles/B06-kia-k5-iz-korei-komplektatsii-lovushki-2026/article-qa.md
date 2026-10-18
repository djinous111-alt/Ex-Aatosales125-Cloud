# Article QA — B06

**topic_id:** B06  
**slug:** kia-k5-iz-korei-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B06-kia-k5-iz-korei-komplektatsii-lovushki-2026  
**date:** 2026-10-18  
**verdict:** PASS  
**score:** 87

## Beginner / pain–solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Красивый лот Encar «без ДТП» + низкий пробег → риск депозита за скрытый ремонт / LPI / коммерцию |
| Где решение | H2: сценарий топлива → тримы (таблица) → мусаго → пробег/LPI → пакет до депозита → чек-лист 10 пунктов |
| Первый результат | До FAQ: VIN + Carhistory + лист Encar + трим + бензин/LPI + стоп-флаги; без пакета депозит не шлёт |
| Термины «на пальцах» | Encar, Carhistory, LPI, мусаго, ЭБУ — объяснены в lead / теле |

**beginner-fit:** PASS (не проф-жаргон, первый безопасный шаг — чеклист до денег)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=today; errors=[] |
| fact-check | PASS | 5 stats; verified 1 (2026); unverified 4 (2021 story, 1996, 2200 вон) — в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` from PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/схемы); Flesch RU 73.3 |
| cannibalization | PASS | 0 issues (3 meta loaded) |
| utility gate | PASS | action 22; pain 10; outcome 12; FAQ×6; table×1 |
| human-voice gate | PASS | warn: multiple exactly-5-step lists (non-blocking) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «киа к5 из кореи» в title/H1/meta; H2 how-to; CTA×3; нет blog internals |
| GEO / citability | 23/25 | Инсайт-блок, схема лота, таблица тримов, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 (Ept02 ✗) |
| Human voice | 14/15 | 0 AI-slop; story Андрей; warn exactly-5 lists |
| Fact safety | 13/15 | Факты в research-notes; 1996/2200 не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9327 зн., FAQ 6, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «киа к5 из кореи» в meta title / H1 |
| C02 | ✓ | Lead: Андрей + боль депозита + что ниже — без «в этой статье» |
| C03 | ✓ | Новичок, заказ K5 из Кореи через Владивосток |
| C04 | ✓ | Encar / Carhistory / LPI / мусаго / ЭБУ объяснены |
| O01 | ✓ | H2 = research outline (топливо → тримы → мусаго → пробег → пакет → чеклист → дальше) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + таблица + схемы, mode B |
| R01 | ✓ | Инсайт, вердикт трима, схема лота, итог-блок |
| R02 | ✓ | Мусаго ≠ покраска; Carhistory с 1996 / ~2200 вон — в research-notes |
| R03 | ✓ | Нет цен лотов/%; пошлины отложены в каталог |
| R04 | ✓ | FAQ: ответ в 1-м предложении |
| E01 | ✓ | Угол K5 тримы + ловушки; вне denylist логистики / AS09 |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B; reader_story без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты мусаго, flood, LPI/аренда, скрутка |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- verdict: pass
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/схем)
- Flesch RU: 73.3

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все gates PASS с первого прогона)

## FIX (non-blocking / optional)

1. **Ept02:** после публикаций B/AS — 2–3 internal links (Indexer / interlink).
2. **fact-check soft:** 1996 / KRW ~2200 → fact-bank для verified.
3. **human-voice warn:** варьировать длину списков (exactly-5); не блокер.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
