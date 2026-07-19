# Article QA — AS07

**topic_id:** AS07  
**slug:** dokumenty-na-avto-iz-kitaya  
**article_dir:** memory/blog/articles/AS07-dokumenty-na-avto-iz-kitaya  
**date:** 2026-07-19  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-07-19; warn: technical topic без official docs URL |
| utility gate | PASS | action_markers 38; pain 10; outcome 13; FAQ×6; table×1 |
| human-voice-gate | PASS | WARN: 4 списка ровно по 5 шагов |
| fact-check | PASS | 4 stats; unverified: «180 дней» (есть в research-notes) |
| link-verify | PASS | 3/3 OK (`elpts.ru`, каталог, Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка таблицы/схем); Flesch RU 62.9 |
| cannibalization | PASS | 0 issues |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Страх перевести деньги за авто из Китая и получить поддельные документы / «левый» VIN → отказ ГАИ |
| Где решение | H2: пакет до оплаты, сверка VIN, инвойс, СБКТС/ЭПТС, красные флаги, правило 180 дней, чеклист |
| Первый результат | Чеклист до оплаты заполнен; VIN совпал в 3+ местах; сделка стоп или безопасные этапы оплаты |
| Термины «на пальцах» | VIN, инвойс, ЭПТС, СБКТС, СВХ объяснены в lead/первых H2 |

**Beginner-fit:** PASS — не профиль для юристов/декларантов; безопасный первый шаг до депозита ясен.

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2/H3; CTA; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт, схема, таблица, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop hits; human-voice PASS |
| Fact safety | 13/15 | 180 дней не в fact-bank; кейс VIN 2026 в research |
| Contract HTML | 10/10 | Whitelist PASS, объём ~9078, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «документы на авто из китая» в meta title / H1 |
| C02 | ✓ | Lead: стоп до депозита + сверка VIN/реестров |
| C03 | ✓ | Читатель: заказ/покупка авто из Китая, риск предоплаты |
| C04 | ✓ | VIN / инвойс / ЭПТС / СБКТС объяснены |
| O01 | ✓ | H2 = outline research (пакет → VIN → инвойс → реестры → флаги → 180 → чеклист → FAQ) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт, схема сделки, FAQ |
| R02 | ✓ | Март 2026 VIN-шильдики + правило ~180 дней в research-notes |
| R03 | ✓ | Нет выдуманных пошлин/%; цены лотов не фиксируются |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «сначала бумага и шильдик, потом деньги» |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: Госуслуги не отдают ЭПТС; PDF ≠ запись в реестре |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- FIX this run: `portal.elpts.ru` (DNS NXDOMAIN) → `https://elpts.ru`; deep-link `rst.gov.ru` снят с `<a href>` (Cloud TLS reset) → текстовая инструкция rst.gov.ru
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схемы)
- Flesch RU: 62.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. link-verify FAIL → `portal.elpts.ru` NXDOMAIN; `www.rst.gov.ru` Connection reset из Cloud.
2. GEO QA: заменён ЭПТС-URL на `https://elpts.ru`; Росстандарт оставлен текстом (rst.gov.ru); ярлык инсайта `TL;DR / Быстрый инсайт` → `Коротко`.
3. Повтор всех gates: PASS (slop WARNING non-blocking).

## FIX (non-blocking / optional)

1. **Ept02:** после URL соседних статей — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** «180 дней» — дописать в fact-bank.
3. **slop over-long:** артефакт таблицы; правки не критичны.
4. **human-voice WARN:** варьировать длину списков (не все по 5 шагов).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-report PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
