# Article QA — AS05

**topic_id:** AS05  
**slug:** svh-vladivostok-2026  
**article_dir:** memory/blog/articles/AS05-svh-vladivostok-2026  
**date:** 2026-07-19  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL |
| fact-check | PASS | 3 stats; verified 1 (2026); unverified 2 («4 месяцев», «101») — есть в research-notes / Fact Check Box |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из `PUBLIC_SITE_URL` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка таблицы/списков парсером); Flesch RU 58.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 25; pain 5; outcome 6; FAQ×6; table×1 |
| human-voice gate | PASS | warnings: multiple exactly-5-step lists; story/pain/outcome overlap OK |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит уже внесён / «на складе» = бесплатно; путает 4 месяца закона и льготу 5–10 суток; страх счёта за перестой |
| Где решение | H2: что такое СВХ → две шкалы → чеклист до депозита → ритм после выгрузки → ловушки → выдача/доставка → первый результат |
| Первый результат до FAQ | Секция «Что сделать сегодня»: объяснить СВХ своими словами + 5 вопросов посреднику до депозита |
| Термины «на пальцах» | СВХ, льгота vs закон, ПРР vs хранение, выгрузка = день 0, слот выдачи |

**beginner-fit:** PASS

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «свх владивосток» в title/H1; H2 how-to; CTA каталог×2 + Telegram; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт-блок, таблица сроков, FAQ×6, чеклисты; ярлык «TL;DR / Быстрый инсайт» — soft style |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | HV gate PASS; 0 AI-slop hits |
| Fact safety | 12/15 | ст. 101 / 4 мес не в fact-bank; сверка в Fact Check Box + research-notes |
| Contract HTML | 10/10 | Whitelist PASS, ~9278 знаков, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «свх владивосток» в meta title / H1 |
| C02 | ✓ | Lead: боль Антона + прямой ответ про СВХ/льготу |
| C03 | ✓ | Читатель: новичок с авто из JP/KR/CN через Владивосток |
| C04 | ✓ | СВХ / льгота / ПРР / перестой объяснены |
| O01 | ✓ | H2 = research outline (термин → шкалы → чеклист → ритм → ловушки → выдача → результат) |
| O02 | ✓ | Логичный outline без скачков |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт-блок, таблица, схема ритма, FAQ |
| R02 | ✓ | ст. 101 ТК ЕАЭС + ориентиры 5–10 / ПРР / ступени с пометкой «обзоры» |
| R03 | ✓ | Нет прайса Авто-Сейлс; пошлины → каталог |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + две шкалы сроков |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, история Антона без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: ориентиры ≠ прайс; кто платит — зафиксировать |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/списков)
- Flesch RU: 58.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (Writer) — blocking

- нет (overall PASS; cover\|\|schema разрешены)

## FIX (non-blocking / optional)

1. **Ept02:** после появления URL AS01–AS09 на сайте — 2–3 internal blog links с `anchor_variants`.
2. **Инсайт-блок:** убрать шаблонный ярлык `TL;DR / Быстрый инсайт` → нейтральный заголовок (skill style; gates уже PASS).
3. **fact-check soft:** «4 месяца» / ст. 101 ТК ЕАЭС — дописать в fact-bank.
4. **HV warning:** варьировать длину списков (сейчас несколько ровно по 5 пунктов).
5. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-report PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
