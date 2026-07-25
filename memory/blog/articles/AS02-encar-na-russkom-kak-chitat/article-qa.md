# Article QA — AS02

**topic_id:** AS02  
**slug:** encar-na-russkom-kak-chitat  
**article_dir:** memory/blog/articles/AS02-encar-na-russkom-kak-chitat  
**date:** 2026-07-26  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-07-26; sources/pain/outcome OK |
| fact-check | PASS | 6 stats; 2 verified (2026, 90 дней); 4 soft-unverified (15 мин, 5 лет, 3000, 5000) — есть в research-notes / эвристики |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка table/list парсером); Flesch RU 68.3 Easy |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 24 / pain 8 / outcome 11; FAQ×6; table×1; lists OK |
| human voice gate | PASS | errors=[]; warnings: rhythm variance/avg=0.27; 3× exactly-5-step lists |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Скрин Encar на корейском / «без ДТП» → страх купить «кота в мешке», не знает, что смотреть |
| Где решение | H2: открыть карточку → схема X/W → пробег/фото → Diagnosis vs Carhistory vs Trust Encar → фильтр vs подборщик → пакет к заказу |
| Первый результат | За 10–15 мин вердикт «лот ок / пропускаем» до депозита; назвать пробег, владельцев, X/W на силовых, крупные выплаты |
| Термины «на пальцах» | Performance Check, X/W, Encar Diagnosis, Carhistory, Trust Encar, Insurance History |
| Beginner-fit | PASS — first safe step без корейского; без «только для профи» |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «encar на русском» в title/H1; H2 how-to; CTA; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, таблица отчётов, FAQ×6, чеклисты, standalone blocks |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | PASS; soft WARN rhythm + 5-step lists |
| Fact safety | 13/15 | Ключевые факты в research-notes; часть чисел не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8863 chars, FAQ, CTA≤3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «encar на русском» в meta title / H1 |
| C02 | ✓ | Lead — боль + прямой ответ (порядок чтения), без «в этой статье» |
| C03 | ✓ | Новичок без корейского, заказ/скрин от перекупа |
| C04 | ✓ | X/W, Performance Check, Carhistory, Trust Encar объяснены |
| O01 | ✓ | H2 = action_outline research |
| O02 | ✓ | Логичный outline шапка → кузов → пробег → отчёты → решение → пакет → FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | TL;DR, вердикт лист/история, FAQ-блоки |
| R02 | ✓ | KRW 2,200 + 90 дней/5000 км + flood-check в research-notes |
| R03 | ✓ | Нет цен лотов/%; пороги вон — эвристика с пометкой |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «переводчик не спасает от битого кузова» + Игорь/Tucson |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты листа vs страховки, LPG/коммерция, «Trust Encar» путаница |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/списков)
- Flesch RU: 68.3 Easy

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после известных URL соседних AS* — 2–3 internal links с `anchor_variants` (напр. AS09 Trust Encar / Carhistory).
2. **fact-check soft:** 5000 км / порог 3000 км / «15 минут» — дописать в fact-bank при желании полного verified.
3. **human voice WARN:** чуть разнообразить длину абзацев и размер списков (не блокирует PASS).
4. **slop WARNING:** over-long в основном артефакт table/list; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
