# Article QA — B01

**topic_id:** B01  
**slug:** mitsubishi-outlander-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-mitsubishi-outlander-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-26  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified 1900/2023/1998 — в research-notes (METI/Reuters/GF7W) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из `PUBLIC_SITE_URL` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 71.7 |
| cannibalization | PASS | 0 issues (3 article meta loaded) |
| utility gate | PASS | action_markers 31; pain 6; outcome 9; FAQ×7; table×1; ol×6 |
| human voice | PASS | после FIX ярлыка Fact Check — warnings [] |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Красивый лот Outlander без кода кузова и без ответа, можно ли вывезти из Японии в 2026; риск ставки «с глаз» и путаница грейда «P» с бензином |
| Где решение | H2: бюджет → код XL/GF/GG/GN → экспортный контроль → лист R/RA → чеклист 10 → шаги до лимита |
| Первый результат | До ставки заполнены 10 пунктов чеклиста; ясно «проходной / стоп / нужен расчёт»; утиль не из чужой таблицы |
| Термины «на пальцах» | Код кузова, экспортный контроль, аукционный лист, R/RA, CVT, PHEV, бюджет «до ключей» |
| Beginner-fit | PASS — без профи-жаргона без пояснений; безопасный первый шаг = нет пакета → нет ставки |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «аутлендер из японии» в title/H1/meta; H2/H3; CTA каталог×2 + Telegram; нет 2–3 blog internal |
| GEO / citability | 23/25 | TL;DR, схема до ставки, таблица кодов, FAQ×7, чеклист, success criteria до FAQ |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | 0 AI-slop; concrete/pain/outcome markers OK |
| Fact safety | 13/15 | Даты/объёмы в research-notes; soft unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8.9k символов текста, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «аутлендер из японии» в title / H1 / description |
| C02 | ✓ | Lead: боль лота без кода кузова + прямой результат до ставки |
| C03 | ✓ | Читатель: заказ Outlander из Японии через Владивосток |
| C04 | ✓ | Код кузова, экспортный контроль, лист, R/RA, CVT объяснены |
| O01 | ✓ | H2 = research outline до ставки |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol×6 + ul×10 + таблица; mode B |
| R01 | ✓ | TL;DR, схема, FAQ-блоки |
| R02 | ✓ | METI 09.08.2023 + порог 1900 cc + GF7W ~1998 в notes |
| R03 | ✓ | Нет цен лотов / статичных сумм утиля |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до ставки» + конфликт реклама vs экспортный контроль |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс + reader_story Иван |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Стоп PHEV/HV/>1900 cc, R/RA, CVT/батарея названы честно |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 71.7

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклист + шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Human voice WARN: Fact Check с ярлыком «Достоверность данных» (шаблонный матч gate). Заменено на контрактное «Достоверность:» с теми же источниками. Повтор: PASS, warnings [].

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 1900 / 09.08.2023 / 1998 cc — дописать в fact-bank для verified.
3. **slop over-long:** 4 предложения; правки не критичны.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
