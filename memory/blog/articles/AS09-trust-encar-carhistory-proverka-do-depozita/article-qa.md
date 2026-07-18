# Article QA — AS09

**topic_id:** AS09  
**slug:** trust-encar-carhistory-proverka-do-depozita  
**article_dir:** memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita  
**date:** 2026-07-17  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| fact-check | PASS | 2 stats; unverified vs fact-bank (1996, KRW 2,200) — есть в research-notes (Carhistory official) |
| link-verify | PASS | 2/2 OK (`avto-sales125.ru`, `t.me/avtosales125`); `--site-base https://avtosales125.ru` |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 4 over-long (склейка таблицы/схем парсером); Flesch RU 73.2 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action_markers 13 (≥8); numbered lists, FAQ×7, table×1 OK |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «trust encar» в title/H1; H2/H3; CTA-ссылки; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, схема, таблица источников, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop hits |
| Fact safety | 13/15 | Факты в research-notes; не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, объём ~8829, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «trust encar» в meta title / H1 |
| C02 | ✓ | Первый абзац — прямой ответ про депозит до проверки |
| C03 | ✓ | Читатель: заказ корейского авто, риск депозита |
| C04 | ✓ | Trust Encar / Performance Check / Carhistory объяснены |
| O01 | ✓ | H2 = how-to outline research (до депозита → Encar → Carhistory → осмотр → флаги → чеклист → FAQ) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | TL;DR, схема до депозита, FAQ-блоки |
| R02 | ✓ | KRW 2,200 + данные с 1996 + flood free в research-notes |
| R03 | ✓ | Нет цен лотов/%; пороги вон — эвристика с пометкой |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + разведение Trust Encar vs инструменты |
| E02 | ✓ | «Делать / Не делать» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты страховой базы, X/W, flood, осмотр |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/схемы)
- Flesch RU: 73.2

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Utility gate BLOCK → добавлены action-маркеры: «избегайте», «проверьте/используйте», «Шаг N» в финальном ol. Повтор: PASS (13 markers).

## FIX (non-blocking / optional)

1. **Ept02:** после URL AS01–AS08 на `avtosales125.ru` — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** KRW 2,200 / 1996 — дописать в fact-bank для verified.
3. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- utility gate PASS ✓  

**Итог:** PASS — можно cover || schema.
