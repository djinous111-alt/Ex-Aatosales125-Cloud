# Article QA — B01

**topic_id:** B01  
**slug:** dostavka-avto-iz-vladivostoka-zd-avtovoz-2026  
**article_dir:** memory/blog/articles/B01-dostavka-avto-iz-vladivostoka-zd-avtovoz-2026  
**date:** 2026-10-16  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-16; technical_topic=false; sources≥14 domains |
| fact-check | WARNING | 19 stats; verified 2; unverified в research-notes (Т–Ж, прайсы операторов) — не fact-bank |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы парсером); Flesch RU 60.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 13; pain 19; outcome 14; ol/FAQ/table OK (после restore pain/outcome lists) |
| human-voice | PASS | soft WARN: 2× exactly-5 lists; Fact Check «Материал проверен» + Редакция Авто-Сейлс |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 actionable; CTA×2; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, таблица сравнения, схема сдачи, FAQ×6, чек-лист |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop; reader_story Игорь; угол «сосед из порта» |
| Fact safety | 13/15 | Ориентиры с пометкой «не оферта»; цифры в research-notes |
| Contract HTML | 10/10 | Whitelist PASS, ~9446, FAQ×6, CTA≤3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «доставка авто из владивостока» в title / H1 |
| C02 | ✓ | Lead: тупик ж/д vs автовоз vs перегон + обещание выбора |
| C03 | ✓ | Читатель после растаможки во Владивостоке |
| C04 | ✓ | Автовоз / сетка / контейнер / перегон объяснены «на пальцах» |
| O01 | ✓ | H2 = этапы → таблица → автовоз → ж/д → перегон → чек-лист → критерий → FAQ |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol чек-лист + таблица + схема →, mode B |
| R01 | ✓ | TL;DR, итоговый вердикт, схема сдачи |
| R02 | ✓ | Сроки/цены операторов + кейс Т–Ж в research-notes |
| R03 | ✓ | Цены как ориентир рынка, не оферта |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Два этапа + «контейнер нередко быстрее автовоза» |
| E02 | ✓ | «Делать / Не делать» в H2-секциях |
| E03 | ✓ | CTA: каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Голос «сосед из порта» / Игорь из Казани |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Сколы, попутное место, бензин, габарит 1,87 м |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

**PASS.** Боль новичка: машина во Владивостоке, непонятно что выбрать, страх сколов и мошенника. Решение в H2-таблице + чек-лист сдачи. Первый результат до FAQ: один способ с «почему» + папка фото/документов + реалистичный общий срок. Термины (сетка, контейнер, автовоз, пломба) объяснены без жаргона логиста.

## Pain / solution map

| Боль | Где решение | Результат читателя |
|------|-------------|-------------------|
| Тупик ж/д / автовоз / перегон | H2 таблица + вердикт | Один выбранный способ |
| Страх сколов / «последнее место» | Автовоз / ж/д секции + стоп-правила | Договор, страховка, не карта физлица |
| Срок «18 дней» → 40 | Lead + FAQ + критерий успеха | Общий календарь погрузка+путь+выдача |

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схемы)
- Flesch RU: 60.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чек-лист) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (utility false-BLOCK снят restore `pain_markers_ru` / `outcome_markers_ru` в editorial-policy)

## FIX cycle (QA)

1. Utility gate BLOCK → `pain_markers=0` / `outcome_markers=0` из-за пустых списков в `memory/brief/editorial-policy.json` (не из-за статьи). Списки восстановлены + fail-fast в `excalibur_blog_utility_gate.py`. Повтор: PASS.

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних постов — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** ключевые ориентиры Т–Ж / операторов — в fact-bank.
3. **slop over-long:** артефакт таблицы; правки не критичны.
4. **human-voice WARN:** варьировать длину ol (сейчас 2× ровно по 5 в «Что дальше» и др.).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
