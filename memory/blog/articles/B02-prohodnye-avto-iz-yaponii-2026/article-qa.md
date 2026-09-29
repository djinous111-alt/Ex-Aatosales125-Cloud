# Article QA — B02

**topic_id:** B02  
**slug:** prohodnye-avto-iz-yaponii-2026  
**article_dir:** memory/blog/articles/B02-prohodnye-avto-iz-yaponii-2026  
**date:** 2026-09-29  
**verdict:** FAIL  
**score:** 84

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic without official docs URL |
| utility gate | **BLOCK** | pain_markers=0&lt;2, outcome_markers=0&lt;3 — см. blocker ниже |
| human-voice | PASS | warnings: multiple exactly-5-step lists |
| html-linter | PASS | 0 errors; TOC нет |
| slop-detector | PASS | 0 клише; 2 over-long (таблица + success H2); Flesch RU 64.5 |
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
| Contract HTML | 10/10 | whitelist PASS, ~9172–9411 chars, FAQ, CTA |
| Utility gate | **0 (veto)** | BLOCK — policy markers empty |
| **Итого (content)** | **84/100** | veto utility → verdict FAIL |

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

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · **veto utility gate: да**

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
- Машинный utility pain/outcome: **FAIL** (см. blocker)

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 2
- Flesch RU: 64.5

## Schema ready

BlogPosting: pending (вне зоны QA) | FAQPage: yes (7) | HowTo: yes (чек-лист) | cover/schema: **не стартовать** без QA PASS

## Blockers

1. **`UTILITY ARTICLE BLOCKER`** — `utility-gate-report.json` status BLOCK:
   - `pain_markers=0 < 2`
   - `outcome_markers=0 < 3`
   - **Корневая причина не в тексте статьи:** в `memory/brief/editorial-policy.json` нет `pain_markers_ru` / `outcome_markers_ru`, скрипт берёт `[]`, счётчик всегда 0, пороги по умолчанию 2/3 → **любая** статья BLOCK (проверено на AS09: исторический PASS-отчёт, повторный прогон сейчас тоже BLOCK).
   - Human-voice gate по своим hardcoded маркерам: **PASS** (pain: боль/ошиб; outcome: результат/проверьте/соберите/выберите).

## FIX для Writer (цикл 1) — текст

> Writer **не** сможет снять utility BLOCK правками `article.html`, пока Fixer не добавит маркеры в policy. Ниже — лексический полир после policy-fix (или параллельно), без полного рерайта.

1. **После появления `pain_markers_ru` в policy** — в lead/ближайший `<p>` явно вставить ≥2 подстроки из списка policy (ориентир HV: `боль`/`проблем`/`ошиб`/`дорого`/`сложно`/`застр`). Сейчас в тексте уже есть «ошибка», «ловушка», «риск»; усилить формулировку боли одной фразой («главная боль новичка…»).
2. **После появления `outcome_markers_ru`** — в H2 результата и перед FAQ ≥3 маркера (ориентир HV: `результат`, `проверьте`, `соберите`, `выберите`, `получите`, `сможете`). Сейчас «результат»/«проверьте»/«выберите»/«соберите» уже есть — сверить с финальным списком policy 1:1.
3. **Non-blocking:** варьировать длину одного из ol (human-voice warning: два списка ровно по 5 пунктов).
4. **Non-blocking (Ept02):** 2–3 internal links на соседние посты блога с `anchor_variants`, когда URL готовы.
5. **Non-blocking fact soft:** ключевые цифры (117,68 кВт; 09.08.2023; ЕЭК №74) — в `fact-bank.md` для verified.

## FIX для Fixer (обязательно до re-QA)

См. `memory/pipeline-fix-queue.md#INC-20260929-1720-geo-qa-utility-pain-outcome-markers-missing`

- Добавить в `editorial-policy.json` списки `pain_markers_ru` / `outcome_markers_ru` (согласовать с `excalibur_blog_human_voice_gate.py`) и явные `min_pain_markers` / `min_outcome_markers` в `article_required_signals`.
- Либо: если списки пусты — **не** применять пороги (skip), чтобы не блокировать все статьи.

## Gate

- score ≥ 80 → **84** ✓ (content)  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- link-verify pass ✓  
- utility gate PASS ✗ **BLOCK**  
- beginner-fit PASS ✓  

**Итог:** FAIL — cover || schema **не** запускать. Вернуть writer после Fixer policy-fix + re-run utility; либо только Fixer, затем re-QA без правок текста если маркеры уже матчятся.
