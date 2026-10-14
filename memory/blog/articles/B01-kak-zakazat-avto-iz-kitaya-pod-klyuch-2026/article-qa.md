# Article QA — B01

**topic_id:** B01  
**slug:** kak-zakazat-avto-iz-kitaya-pod-klyuch-2026  
**article_dir:** memory/blog/articles/B01-kak-zakazat-avto-iz-kitaya-pod-klyuch-2026  
**date:** 2026-10-14  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL |
| fact-check | PASS | 10 stats; verified 2; unverified 8 (180 дней / сроки / ПП №506 — в research-notes) |
| link-verify | PASS (soft) | catalog `avto-sales125.ru` → 503 soft-pass (`href==CATALOG_URL`); 2GIS Unicode path → recheck percent-encoded 200; Telegram 200 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы); Flesch RU 61.3 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 27; pain 5; outcome 6; FAQ×6; table×1 |
| human-voice | PASS | warning: multiple exactly-5-step lists |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Страх депозита «на карту менеджера» без договора/сметы/VIN — остаться без машины и денег |
| Где решение | H2: смета под ключ → модель → контрагент/VIN/180 дней → договор → маршрут → чек-лист 12 пунктов |
| Первый результат | До FAQ: критерий успеха — договор/образец, смета в рублях, VIN/критерии, ответ при срыве; затем «Что дальше» шаг 1–6 |
| Термины «на пальцах» | «под ключ», смета vs цена в юанях, р/с vs карта, VIN, СВХ, правило 180 дней / справка завода, ПП №506 |

**Beginner-fit:** PASS — не профи-жаргон без объяснений; первый безопасный шаг до депозита ясен.

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; CTA каталог×2 + Telegram; мало internal blog links |
| GEO / citability | 24/25 | TL;DR, таблицы, схемы, FAQ×6, чек-лист 12 |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | Gate PASS; warning про 5-step lists |
| Fact safety | 13/15 | Ключевые цифры в research-notes; часть не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9444 символов, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как заказать авто из китая» в meta/H1 |
| C02 | ✓ | Lead: боль депозита → обещание чек-листа до перевода |
| C03 | ✓ | Новичок первого заказа под ключ |
| C04 | ✓ | VIN, СВХ, под ключ, 180 дней объяснены |
| O01 | ✓ | H2 = pain→solution outline research |
| O02 | ✓ | Логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + схемы, mode B |
| R01 | ✓ | TL;DR, схема до депозита, FAQ |
| R02 | ✓ | 180 дней / gov.cn / ПП №506 с пометкой в Fact Check Box |
| R03 | ✓ | Нет фейковых точных цен лота; ориентиры сроков с оговорками |
| R04 | ✓ | Ответ FAQ с первого предложения |
| E01 | ✓ | Угол «до депозита», не EV/растаможка |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон редакции Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: EV отдельно, сроки ориентиры, договор ≠ закон |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог / Telegram / 2GIS) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed after soft-pass: 0
- soft-pass: CATALOG_URL 503; 2GIS Unicode path (encoded recheck 200)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схем)
- Flesch RU: 61.3

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чек-лист / шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требовался (gates PASS; link soft-pass задокументирован)

## FIX (non-blocking / optional)

1. **Ept02:** после публикации AS* URL — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** 180 дней / ПП №506 → fact-bank для verified.
3. **human-voice warning:** разнести размер списков (сейчас несколько ровно из 5 пунктов).
4. **2GIS href:** заранее percent-encode кириллицу в path (иначе CLI link-verify падает на ascii codec).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass (с soft-pass catalog/2GIS) ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
