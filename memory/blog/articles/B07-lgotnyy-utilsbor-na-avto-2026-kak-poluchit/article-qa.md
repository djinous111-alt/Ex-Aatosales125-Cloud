# Article QA — B07

**topic_id:** B07  
**slug:** lgotnyy-utilsbor-na-avto-2026-kak-poluchit  
**article_dir:** memory/blog/articles/B07-lgotnyy-utilsbor-na-avto-2026-kak-poluchit  
**date:** 2026-10-01  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date == today; warning: tech topic false-positive (already INC-1330) |
| fact-check | PASS | 14 stats; 3 verified / 11 unverified vs fact-bank (пороги кВт, 3400/5200, ПП 1713 — в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из `PUBLIC_SITE_URL` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/инсайт/Fact Check); Flesch RU 67.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 8; pain 4; outcome 6; ol=24; FAQ×6; table×1 |
| human-voice | PASS | pain/outcome/concrete OK; warn: Fact Check template + 4× exactly-5 lists |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Узнать на таможне, что льготы нет / доплата после ранней продажи (lead) |
| Где решение | H2: проверка до ставки → условия → кВт → гибрид/электро → ТПО → чек-лист → коммерческая ставка |
| Первый результат | Статус «льгота да / нет / риск» + заполненный чек-лист до депозита (критерий результата до FAQ) |
| Термины «на пальцах» | кВт vs л.с.; ТПО; СБКТС/ЭПТС; параллельный vs последовательный гибрид; 30-минутная мощность |
| Beginner-fit | PASS — физлицо, без «команды разработчиков», первый безопасный шаг до ставки |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «льготный утильсбор» в title/H1; actionable H2; CTA; мало blog-internal |
| GEO / citability | 23/25 | Инсайт, схема →, таблица условий, FAQ×6, чеклисты, критерий результата |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop cliches |
| Fact safety | 12/15 | Ориентиры с оговоркой; цифры в research; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9492 chars, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead — страх таможни + чек-лист до депозита |
| C03 | ✓ | Читатель: физлицо, авто из Азии «для себя» |
| C04 | ✓ | кВт, ТПО, СБКТС, ЭПТС, типы гибрида объяснены |
| O01 | ✓ | H2 = pain_solution_map research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + схемы, mode B |
| R01 | ✓ | Инсайт, схема до депозита, критерий результата |
| R02 | ✓ | Пороги 117,68/58,84 кВт; 3400/5200; ПП 1713 в research |
| R03 | ✓ | Нет фейкового прайса; «не прайс», расчёт в каталоге |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки/депозита» |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Риски продажи, второй ввоз, коммерческая шкала |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (таблица/инсайт — soft)
- Flesch RU: 67.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (после restore `pain_markers_ru` / `outcome_markers_ru` в editorial-policy)

## FIX cycle (QA)

1. Utility gate false BLOCK (`pain_markers=0`, `outcome_markers=0`) из-за пустых списков в `memory/brief/editorial-policy.json` + отсутствие skip-when-empty в скрипте после rebrand.  
   **Восстановлены** маркеры (sync с human-voice) и skip-логика в `excalibur_blog_utility_gate.py`. Повтор: **PASS** (pain 4, outcome 6).  
   Статья Writer **не** правилась.

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links на live-посты (растаможка / СБКТС-ЭПТС / под ключ) с `anchor_variants`.
2. **fact-bank:** дописать 117,68 кВт / 58,84 кВт / 3400 / 5200 / ПП 1713.
3. **slop over-long / HV warn:** укоротить инсайт; варьировать длину ol (сейчас 4× ровно 5).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema. Writer FIX **не** нужен.
