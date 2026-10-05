# Article QA — B01

**topic_id:** B01  
**slug:** kak-sdelat-pervuyu-stavku-na-yaponskom-aukcione-2026  
**article_dir:** memory/blog/articles/B01-kak-sdelat-pervuyu-stavku-na-yaponskom-aukcione-2026  
**date:** 2026-10-05  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic false-positive (офиц. docs URL); уже в incident Research |
| utility gate | PASS | action_markers 25 (≥8); pain 6; outcome 7; ol×6, FAQ×7, table×1 |
| human-voice | PASS | H2≠шаблон; reader_story/pain/outcome overlap OK; fact-check template 0 |
| fact-check | PASS | 1 stat (`50–100` тыс.); unverified vs fact-bank — есть в research-notes (АМ ГАММА) |
| link-verify | PASS | 2/2 OK (каталог + Telegram; дубль каталога дедуп); `--site-base` PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (склейка ul/table/blockquote парсером); Flesch RU 58.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Страх первой ставки/депозита без понимания листа, лимита бида и возврата залога (lead + reader_story) |
| Где решение | H2: бюджет → устройство аукциона → чек-лист листа → max bid → красные флаги → после выигрыша → итог до депозита |
| Первый результат | До депозита: договор с возвратом + лот с листом без красных флагов + потолок в иенах + смета «под ключ» (H2 «Соберите итог») |
| Термины «на пальцах» | USS/посредник, оценка 4, R/RA (≠ airbag), депозит как залог, «под ключ» vs ставка |
| Beginner-fit | PASS: тон для новичка, первый безопасный шаг до денег, без «команды разработчиков» |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2/H3; CTA; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, схема, таблица мифов, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop; human-voice PASS |
| Fact safety | 13/15 | 50–100 тыс. в research-notes; не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, объём 9155, FAQ, CTA≤3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как купить авто на японском аукционе» в title / H1 |
| C02 | ✓ | Lead — боль + чек-лист до депозита, без «в этой статье» |
| C03 | ✓ | Новичок РФ, первая ставка через посредника |
| C04 | ✓ | USS, оценка 4, RA, депозит, лист объяснены |
| O01 | ✓ | H2 = action_outline research (до депозита) |
| O02 | ✓ | Логичный outline: бумага → торги → после |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + схема →, mode B |
| R01 | ✓ | TL;DR, таблица мифов, критерий результата, схема |
| R02 | ✓ | Депозит 50–100 / RA / USS — в research-notes |
| R03 | ✓ | Нет выдуманных пошлин; ориентир депозита с оговоркой |
| R04 | ✓ | FAQ ответ в 1-м предложении |
| E01 | ✓ | Угол «строго до депозита» + RA≠airbag |
| E02 | ✓ | «Сделайте / Не делайте» в каждой H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски: отказ после выигрыша, R/RA, давление на депозит |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2 unique, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт ul/table/blockquote)
- Flesch RU: 58.6

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после появления URL соседних постов на сайте — 2–3 internal links с `anchor_variants` (Indexer может закрыть).
2. **fact-check soft:** ориентир депозита 50–100 тыс. — дописать в fact-bank для verified.
3. **insight label:** ярлык `TL;DR / Быстрый инсайт` в blockquote — по skill лучше без шаблонного старта; human-voice/linter PASS, не блокер.
4. **slop over-long:** артефакт списков; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
