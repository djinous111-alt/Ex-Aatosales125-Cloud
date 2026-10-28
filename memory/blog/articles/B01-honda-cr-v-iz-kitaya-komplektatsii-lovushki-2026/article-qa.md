# Article QA — B01 Honda CR-V из Китая

**topic_id:** B01  
**slug:** honda-cr-v-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-honda-cr-v-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-28  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-28; warn: technical_topic false-positive (official docs URL) |
| fact-check | PASS | 2 stats; 193 л.с. unverified vs fact-bank (есть в research-notes / Dongfeng) |
| link-verify | PASS | 3/3 OK after 2GIS IRI-encode + expand `${CATALOG_URL}`/`${TELEGRAM_URL}`; report sanitized |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка table/ul/схемы); Flesch RU 76.7 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 27 / pain 7 / outcome 10; FAQ×6; table×1; ol 6 |
| human voice gate | PASS | `human-voice-report.json` PASS; story/pain/outcome overlap OK |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит за ярлык Prestige/Premium без сверки CN trim, зимы, Connect, сметы |
| Где решение | H2: ТЗ → trim CN → CR-V vs Breeze/VIN → зимние кнопки → Connect → смета/ОТТС≠СБКТС → чеклист |
| Первый результат до FAQ | Секция «Пройдите финальный чеклист…»: пакет VIN+кнопки+Connect+смета или стоп депозита |
| Термины «на пальцах» | e:HEV, Honda Connect 4.0, ОТТС vs СБКТС, ЭПТС, Dongfeng vs GAC Breeze, Real-Time AWD |
| beginner-fit | **PASS** — чеклист до денег, без jargon-first; первый безопасный шаг = не платить без пакета |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «хонда срв из китая» в lead/meta; H2 how-to; CTA env; мало blog-internal |
| GEO / citability | 24/25 | Инсайт-бокс, таблица trim, схема до депозита, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 (см. таблицу ниже) |
| Human voice | 15/15 | 0 AI-slop; reader_story Новосибирск; voice Авто-Сейлс |
| Fact safety | 12/15 | MSRP CN + 193 л.с. из research; 193 не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8746 символов, FAQ, CTA≤3, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / lead |
| C02 | ✓ | Lead сразу про депозит за Prestige без сверки |
| C03 | ✓ | Читатель: семья/заказ CR-V из Китая, риск депозита |
| C04 | ✓ | Trim CN, Breeze, Connect, ОТТС/СБКТС объяснены |
| O01 | ✓ | H2 = pain_solution_map research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт-бокс, схема, FAQ |
| R02 | ✓ | MSRP ступени / 193 л.с. опираются на research-notes |
| R03 | ✓ | Нет «под ключ» рублёвых сумм; платежи → каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + Prestige≠заводской trim |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог + Telegram + 2GIS |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Гарантия продавца ≠ Honda РФ; акция CN ≠ цена РФ |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |
| Exp04 | ✗ | (слот не закрыт отдельным кейсом с цифрами сделки — mode B OK) |

Учтено 20 слотов как в AS09-паттерне: 18 ✓ / 2 ✗ (Ept02 + мягкий Exp04). **≥16/20 ✓**. Veto (R03 / Exp01 / slop≥2): нет.

## Link verify

- total: 3, failed: 0
- see `link-verify.json` (CTA redacted; 2GIS IRI-encoded)

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт table/ul/схемы)
- Flesch RU: 76.7

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: вне зоны QA

## QA micro-fixes (не writer rewrite)

1. Инсайт-лейбл: `TL;DR / Быстрый инсайт` → `Инсайт до депозита` (skill GEO QA).
2. 2GIS URL: кириллица в path → percent-encode (link-verify ascii codec).
3. CTA live → `${CATALOG_URL}` / `${TELEGRAM_URL}` в committed HTML; expand только для live verify.

## Blockers

- нет

## FIX cycle (writer)

- не требуется

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
