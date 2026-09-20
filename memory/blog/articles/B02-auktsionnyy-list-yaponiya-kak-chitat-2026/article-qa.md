# Article QA — B02 (RE-RUN #2 after Writer FIX2)

**topic_id:** B02  
**slug:** auktsionnyy-list-yaponiya-kak-chitat-2026  
**article_dir:** memory/blog/articles/B02-auktsionnyy-list-yaponiya-kak-chitat-2026  
**date:** 2026-07-23  
**verdict:** PASS  
**score:** 91  
**cover_schema:** allowed

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | technical_topic=false; warnings=[] |
| fact-check | PASS | 1/1 verified (2026) |
| link-verify | PASS | 2/2 OK; Telegram CTA `https`+`t.me` restored (FIX2); catalog 200 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 71.5 |
| cannibalization | PASS | 0 issues (3 meta loaded) |
| utility gate | PASS | action=37; pain=6; outcome=9 |
| human-voice-gate | PASS | warning: два списка ровно по 5 шагов |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA каталог+TG; нет 2–3 blog internal |
| GEO / citability | 22/25 | Insight «Коротко до ставки», схема →, таблицы×2, FAQ×7, чек-лист |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | Gate PASS; ярлык TL;DR убран |
| Fact safety | 15/15 | Fact-check PASS; link-verify PASS (FIX2) |
| Contract HTML | 10/10 | Whitelist PASS, ~9205, FAQ, CTA, без форм/pre/code |
| Utility / action | 10/10 | PASS после FIX1 + policy markers |
| **Итого** | **91/100** | ≥80; все hard gates PASS |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в meta/H1 |
| C02 | ✓ | Lead: боль ставки вслепую + ответ |
| C03 | ✓ | Новичок у японского листа до ставки |
| C04 | ✓ | Grade, A/U/W/X/XX, R/RA «на пальцах» |
| O01 | ✓ | H2 = action outline |
| O02 | ✓ | Оригинал → зоны → схема → R/RA → ориентир → чек-лист |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul/tables/blockquotes, mode B |
| R01 | ✓ | Insight, схема →, таблицы, FAQ |
| R02 | ✓ | «больше 90% на японском»; R vs RA |
| R03 | ✓ | Нет выдуманных цен/VIN/лотов |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки, не после выкупа» |
| E02 | ✓ | «Сделайте / Не делайте» + Шаг N / Избегайте |
| E03 | ✓ | CTA: каталог×2 + Telegram (t.me, FIX2) |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | R/RA не приговор; XX ≠ авто-авария |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

**PASS.** Боль новичка в lead; термины объяснены; первый шаг — оригинал + 5 зон до ставки; без тона «для профи».

| Вопрос | Ответ |
|--------|-------|
| Какая боль новичка решена? | Не понимает 4.5 / R/RA / A2 / W2 и боится согласиться на ставку вслепую |
| Где показано решение? | H2: оригинал → 5 зон → схема → R/RA → ориентир 4–4.5 → чек-лист |
| Какой первый результат? | Пройти один лист и сказать менеджеру «ок» или «стоп» до ставки |
| Термины «на пальцах»? | Grade, салон A–E, A/U/W/X/XX, R/RA, структурный vs съёмная панель |

## Pain / solution check

- **Lead:** называет боль — ставка вслепую / бланк как шифр.
- **H2:** решения по `pain_solution_map` (оригинал → зоны → схема → R/RA → ориентир → чек-лист).
- **До FAQ:** success_criteria — чек-лист «ок/стоп» до ставки.
- Utility lexical: PASS.

## Link verify

- total: 2 unique (3 href occurrences), failed: 0
- `https://avto-sales125.ru` → 200 OK
- Telegram CTA → `https` scheme, `t.me` present, len=25, literal `[REDACTED]` absent → 200 OK
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 71.5

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes | Review: no | **cover_schema: allowed**

## Blockers

none

## Optional (non-blocking)

- Ept02: 2–3 internal blog links после появления URL других постов.
- Human-voice warning: варьировать длину списков (не два×ровно 5).

## Gate

- score ≥ 80 → **91** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → **PASS** ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- utility gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — `cover_schema: allowed`. Директор → cover || schema.
