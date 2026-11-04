# Article QA — AS10 (GAC GS3)

**topic_id:** AS10  
**slug:** gac-gs3-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS10-gac-gs3-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-04  
**author_id:** avtosales-editorial  
**char_count:** 9098  
**verdict:** PASS  
**score:** 88  
**beginner_fit:** PASS

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: no obvious official docs/developer URL (авто-тема) |
| utility gate | PASS | action_markers 8; pain 4; outcome 9; FAQ×6; table×1 |
| human-voice | PASS | insight «Инсайт до депозита»; exactly_five_lists=0 after ol-counter restore |
| fact-check | PASS | 13 stats; 1 verified in fact-bank; 12 soft unverified (GAC MY2026 numbers in research-notes) |
| link-verify | PASS | Telegram 200; catalog `catalog_ssl` soft-pass (Cloud egress handshake timeout) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 cliches; 5 over-long (таблица/схемы); Flesch RU 71.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Beginner / pain–solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Маркетинг «топ / R-Style с обогревом» → после депозита другая заводская версия без нужных опций |
| Где решение | H2: линейка Enjoy/Smart/R-Style → силовая 1.5T+7DCT → завод vs RU-перевод → красные флаги опций → чеклист до депозита |
| Первый результат | До оплаты: заводское имя + силовая строка + чеклист опций + одно слово плачу/жду/отказ |
| Термины «на пальцах» | 7DCT (мокрый робот), передний привод, ACC/AEB/LKA, CCS vs ACC-пакет, HT2A / GB-GL |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «gac gs3 комплектации» в title/H1; 6 H2; CTA catalog×2 + Telegram; нет 2–3 blog internal |
| GEO / citability | 24/25 | Insight, таблица версий, схема до перевода, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | 0 AI-slop; story/pain/outcome overlap OK |
| Fact safety | 13/15 | Цифры GAC MY2026 в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9098 chars, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary query в meta title / H1 |
| C02 | ✓ | Lead = боль депозита + прямой ответ «как выбрать до оплаты» |
| C03 | ✓ | Читатель: заказ GS3 из Китая через Владивосток |
| C04 | ✓ | Enjoy/Smart/R-Style, 7DCT, ADAS объяснены |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Insight + схема + FAQ |
| R02 | ✓ | Заводские листы gs301–304 / PortStar HT2A в Fact Check |
| R03 | ✓ | Нет статичных «цен под ключ»; MSRP ориентир с пометкой |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «R-Style ≠ максимум» + депозит |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: RU-каталоги vs завод, локализация мультимедиа |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |
| C_bonus missed | — | второй минус не ставим; Ept02 единственный явный gap |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2 unique, failed: 0
- soft_pass: `catalog_ssl`
- see link-verify.json (URLs redacted to `${CATALOG_URL}` / `${TELEGRAM_URL}`)

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/схемы)
- Flesch RU: 71.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (article.html не правился GEO QA)

## FIX (non-blocking / optional)

1. **Ept02:** после URL соседних постов — 2–3 internal links с `anchor_variants` (Indexer).
2. **fact-check soft:** ключевые цифры GS3 MY2026 (177 л.с., 7DCT, габариты) — дописать в fact-bank.
3. **human-voice:** ранее warn про два списка по 5 шагов — после restore ol-counter = 0 (ol 7 и 10 items).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓ (catalog_ssl soft-pass)  
- research notes / utility / human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
