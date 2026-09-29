# Article QA — B02 (rerun)

**topic_id:** B02  
**slug:** prohodnye-avto-iz-yaponii-2026  
**article_dir:** memory/blog/articles/B02-prohodnye-avto-iz-yaponii-2026  
**date:** 2026-09-29  
**qa_run:** rerun after editorial-policy pain/outcome markers restore (INC-20260929-1720)  
**verdict:** PASS  
**score:** 86

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical topic without official docs URL |
| utility gate | **PASS** | pain_markers=4 (≥2), outcome_markers=8 (≥3); action_markers=10 |
| human-voice | PASS | warning: multiple exactly-5-step lists |
| html-linter | PASS | 0 errors; TOC нет |
| slop-detector | PASS | 0 клише; 2 over-long; Flesch RU 64.5 |
| fact-check | PASS | 11 stats; verified 1; unverified 10 (годы/сроки — в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram) |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/meta; H2 actionable; CTA live; мало internal blog links |
| GEO / citability | 23/25 | инсайт, схема, таблица, FAQ×7, чек-лист 11 |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | HV PASS; 0 AI-slop |
| Fact safety | 12/15 | цифры в research-notes; мало в fact-bank |
| Contract HTML | 10/10 | whitelist PASS, FAQ, CTA |
| Utility gate | 6/10 | PASS (pain 4 / outcome 8); soft: нет internal blog links |
| **Итого** | **86/100** | ≥80 ✓ · no veto |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «проходные авто из Японии» в H1/meta |
| C02 | ✓ | Lead: депозит до проверки месяца выпуска |
| C03 | ✓ | Новичок + аукцион Япония / Владивосток |
| C04 | ✓ | ЕЭК №74, СВХ, утильсбор, кВт, e-Power объяснены |
| O01 | ✓ | H2 = окно → лист → мощность → санкции → чек-лист → результат |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol чек-лист + таблица + схемы, mode B |
| R01 | ✓ | инсайт + схема возраста + FAQ |
| R02 | ✓ | 117,68 кВт; санкции с 08.2023; окно 3–5 |
| R03 | ✓ | нет готовых сумм пошлин; расчёт только по лоту |
| R04 | ✓ | FAQ отвечает действием в 1–2 предложениях |
| E01 | ✓ | год в заголовке ≠ возраст таможни |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | тон Авто-Сейлс Владивосток |
| Exp03 | ✓ | slop hits = 0 |
| Ept01 | ✓ | край пятилетки, регистрация≠выпуск, гибрид порог |
| Ept02 | ✗ | нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · **veto utility gate: нет**

## Beginner-fit

- **Боль новичка:** верит году/"проходному" ярлыку, кидает депозит, потом ломается окно 3–5 лет / мощность / санкции.
- **Где решение:** H2 про окно по месяцу, аукционный лист vs выпуск, мощность/мотор, санкции, чек-лист до ставки.
- **Первый результат до FAQ:** мини-чек лота → зелёный/красный → расчёт в каталоге (H2 «Что изменится после проверки»).
- **Термины «на пальцах»:** СВХ, утильсбор, ЕЭК (1 июля/15-е), кВт vs л.с., e-Power, санкционный контур.
- **Verdict beginner-fit:** PASS

## Pain / solution (editorial)

- Lead называет боль (депозит до месяца выпуска) ✓  
- H2 закрывают pain_solution_map ✓  
- success_criteria до FAQ ✓  
- Машинный utility pain/outcome: **PASS** (pain=4, outcome=8)

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 2
- Flesch RU: 64.5

## Schema ready

BlogPosting: pending (вне зоны QA) | FAQPage: yes (7) | HowTo: yes (чек-лист) | cover/schema: **можно стартовать** после handoff PASS

## Soft notes (non-blocking)

1. Human-voice: варьировать длину одного из ol (два списка ровно по 5 пунктов).
2. Ept02: 2–3 internal links на соседние посты блога с `anchor_variants`, когда URL готовы (Indexer).
3. Fact soft: ключевые цифры (117,68 кВт; 09.08.2023; ЕЭК №74) — в `fact-bank.md` для verified.

## Blockers

_none_

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- link-verify pass ✓  
- utility gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — cover || schema можно запускать параллельно. Текст статьи в этом rerun не менялся; снят только policy-veto после restore маркеров.
