# Article QA — AS15

**topic_id:** AS15  
**slug:** dostavka-avto-iz-vladivostoka-2026  
**article_dir:** memory/blog/articles/AS15-dostavka-avto-iz-vladivostoka-2026  
**date:** 2026-07-21  
**verdict:** PASS  
**score:** 90

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical false-positive (INC-20260721-2109) |
| fact-check | PASS | 11 stats; 4 verified / 7 unverified vs fact-bank (сроки/тарифы 2026 в research-notes) |
| link-verify | PASS | 4/4 OK: internal СВХ+СБКТС, каталог `avto-sales125.ru` ×2, Telegram CTA ×1 |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 4 over-long (склейка таблицы/схем); Flesch RU 66.4 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 21; pain 19; outcome 9; FAQ×6; table×1 |
| human-voice gate | PASS | warning: 2× exactly-5-step lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1; H2 actionable; CTA каталог+Telegram рабочие |
| GEO / citability | 22/25 | «Коротко:», таблица, FAQ×6, чек-лист, success-критерий |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 14/15 | gate PASS; soft warning про 5-step lists |
| Fact safety | 12/15 | Ориентиры рынка с оговоркой; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; CTA из env; utility PASS |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «доставка авто из владивостока» в title/H1 |
| C02 | ✓ | Lead — боль после СВХ + сравнение способов |
| C03 | ✓ | Новичок после растаможки во Владивостоке |
| C04 | ✓ | Автовоз / жд / перегон / общий срок объяснены |
| O01 | ✓ | H2 = город+дедлайн → сравнение → срок → перегон → чек-лист → результат → FAQ |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чек-лист, mode B |
| R01 | ✓ | Инсайт «Коротко:», схема, вердикт, success-критерий |
| R02 | ✓ | Сроки/тарифы с источниками в research-notes |
| R03 | ✓ | Цены как ориентиры рынка, не оферта |
| R04 | ✓ | FAQ ответ в 1-м предложении |
| E01 | ✓ | Угол «общий срок vs дни в пути» + чек-лист до оплаты |
| E02 | ✓ | «Делать / Не делайте» в H2 |
| E03 | ✓ | CTA каталог×2 + Telegram×1 (env URLs, link-verify 200) |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | История Игоря / тон Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски кузова, зима, EV, серая ТК |
| Ept02 | ✓ | Internal: СВХ + СБКТС/ЭПТС |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Overall PASS:** все обязательные гейты PASS, score ≥80

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | После СВХ неясно: автовоз / жд / перегон; страх переплатить, ждать, словить сколы |
| Где решение | H2 сравнение + общий срок + чек-лист логисту + критерий «одна фраза выбора» |
| Первый результат | Заполненная таблица сравнения + 7–10 ответов перевозчика до оплаты |
| Термины «на пальцах» | Автовоз / жд / перегон / общий срок vs транзит / неход |

## Link verify

- total unique: 4, failed: 0
- OK: `/2026/07/19/svh-vladivostok-2026/`, `/2026/07/20/sbkts-i-epts-vladivostok-2026/`, catalog CTA, Telegram CTA
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 66.4

## Schema ready

BlogPosting: pending (после PASS → cover\|\|schema) | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no

## Blockers

- нет

## FIX cycle (закрыт Writer FIX)

1. CTA: `href` из env `CATALOG_URL` / `TELEGRAM_URL` — link-verify PASS.
2. Action markers ≥8 — utility gate PASS (21).
3. Инсайт: «Коротко:» вместо TL;DR — ок.
4. Policy/utility pain-outcome — PASS (pain 19 / outcome 9).

## Soft (non-blocking)

1. human-voice: варьировать длину `<ol>` (сейчас 2 списка по 5 шагов).
2. fact-check soft: дописать ориентиры сроков/тарифов 2026 в fact-bank.
3. Fixer: закрыть open INC-0023/0024/0025 (durable docs/tooling; content уже PASS).

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify → ✓  
- research-notes-gate → ✓  
- utility gate → ✓  
- human-voice gate → ✓  
- beginner-fit → ✓  

**Итог:** PASS — можно cover \|\| schema.
