# Article QA — B01

**topic_id:** B01  
**slug:** geely-coolray-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-geely-coolray-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-23  
**verdict:** PASS  
**score:** 88  
**qa_cycle:** 2 (после writer FIX CTA)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic / no official docs URL |
| fact-check | PASS | 18 stats; 1 verified (2026); 17 unverified vs fact-bank (цифры в research-notes) |
| link-verify | **PASS** | 2 unique URL (каталог + Telegram), 3 anchors; failed 0; HEAD 200 |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 3 over-long; Flesch RU 84.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 21 / pain 10 / outcome 13; FAQ×6; table×1 |
| human-voice gate | PASS | warn: rhythm variance/avg=0.34; exactly-5-step lists×2 |

## Beginner-fit / pain→solution

| Check | Result |
|-------|--------|
| Боль новичка в lead | PASS — депозит «пока не ушло», путаница Super Max (атмо) vs турбо Binyue L |
| Решение в H2 | PASS — Monjaro vs Coolray → две линейки → мощность/льгота → VIN/ЭПТС → чеклист |
| Первый результат до FAQ | PASS — таблица «версия = мотор + коробка + салон» + «депозит можно / нельзя» |
| Термины «на пальцах» | PASS — Chaoneng/Binyue L, кВт→л.с., ЭРА-ГЛОНАСС → СБКТС/ЗоЕТС → ЭПТС |
| Beginner-fit | PASS |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2/FAQ; рабочие CTA; нет 2–3 blog internal |
| GEO / citability | 23/25 | insight, таблица линеек, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | gate PASS; мягкий warn ритм/ровные списки |
| Fact safety | 12/15 | цифры в research-notes; мало в fact-bank |
| Contract HTML | 10/10 | whitelist PASS; CTA absolute https×3; REDACTED=0 |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «geely coolray из китая» в title/H1 |
| C02 | ✓ | Lead — боль депозита и путаница моторов |
| C03 | ✓ | Новичок заказа Coolray из Китая |
| C04 | ✓ | Комплектации/льгота/VIN без «для профи» |
| O01 | ✓ | H2 = actionable outline |
| O02 | ✓ | Логика до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица, mode B |
| R01 | ✓ | insight + чеклист + FAQ |
| R02 | ✓ | кВт/л.с./юани в research-notes |
| R03 | ✓ | готовых сумм утильсбора нет |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + атмо vs турбо |
| E02 | ✓ | «Сделайте / Не делайте» |
| E03 | ✓ | CTA: каталог×2 + Telegram×1, absolute https |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Смета только в каталоге; «прошивка» = стоп |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2 / link-verify): нет

## Link verify

- total unique: 2, anchors: 3, failed: 0
- verdict: **pass**
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 84.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: **можно** после Director launch

## Blockers

- нет

## FIX cycle (QA)

1. Cycle 1 FAIL: `href="[REDACTED]"` ×3 → link-verify fail.  
2. Writer FIX: absolute CATALOG×2 + TELEGRAM×1; REDACTED=0.  
3. Cycle 2: all gates PASS, score 88.

## FIX (non-blocking / optional)

1. Инсайт-блок: убрать ярлык `TL;DR / Быстрый инсайт:` (мягко, skill geo-qa).  
2. Human-voice warns: разнести длину абзацев; не держать два списка ровно по 5.  
3. Ept02: 2–3 internal links после indexer.  
4. fact-bank: ключевые кВт/л.с. Coolray 2026.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
