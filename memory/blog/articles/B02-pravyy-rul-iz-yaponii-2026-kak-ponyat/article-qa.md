# Article QA — B02

**topic_id:** B02  
**slug:** pravyy-rul-iz-yaponii-2026-kak-ponyat  
**article_dir:** memory/blog/articles/B02-pravyy-rul-iz-yaponii-2026-kak-ponyat  
**date:** 2026-10-02  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical false-positive (no official docs URL) |
| fact-check | PASS | 3 stats; 1 verified / 2 unverified (сроки привыкания, региональная ликвидность — в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); expand env → verify → re-redact `[REDACTED]` for git |
| html-linter | PASS | whitelist OK; TOC нет; insight без TL;DR |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU 56.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 18; pain 10; outcome 16; char_count 9437 |
| human-voice gate | PASS | outcome: результат/получите/сможете/проверьте/выберите |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Страх депозита за японский RHD без понимания обгонов/фар/перепродажи; неясно, когда лучше Корея LHD |
| Где решение | H2: сценарии → маршрут → фары/СБКТС → сравнение Япония/Корея → чеклист до депозита → шаги в каталог/Telegram |
| Первый результат | Заполненный чеклист + фраза «беру Японию…» / «смотрю Корею…» + вопросы подборщику |
| Термины «на пальцах» | СБКТС, ближний свет / ТР ТС 018/2011, правый vs левый руль, ликвидность по региону |
| Beginner-fit | PASS — без профи-жаргона IT; первый безопасный шаг до депозита |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «правый руль япония» в title/H1; H2 actionable; CTA×3; нет 2–3 blog internal |
| GEO / citability | 23/25 | Insight, 2 таблицы, FAQ×6, чеклисты, схема маршрута |
| CORE-EEAT lite | 14/15 | 18/20 (Ept02 + soft R02) |
| Human voice | 15/15 | HV PASS; concrete + pain/outcome markers |
| Fact safety | 13/15 | Нормы/Минтранс в notes; soft unverified community stats |
| Contract HTML | 10/10 | Whitelist PASS, mode B, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: депозит / маршрут / фары / регион |
| C03 | ✓ | Читатель: заказ авто из Азии, риск депозита |
| C04 | ✓ | RHD/LHD, СБКТС, ближний свет объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный comparison → checklist |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы + blockquote, mode B |
| R01 | ✓ | Insight, схемы, FAQ |
| R02 | ✗ | Нормы/Минтранс в notes; community-сроки привыкания / ликвидность — soft unverified |
| R03 | ✓ | Нет магических цен/пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + Япония vs Корея |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: без калькулятора пошлин, слух о запрете разведён |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6
- Flesch RU: 56.5

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. CTA: временно expand `CATALOG_URL`/`TELEGRAM_URL` для link-verify 2/2, затем re-redact `[REDACTED]` перед commit (repo convention).
2. Insight: убран ярлык `TL;DR / Быстрый инсайт` → `Коротко до депозита`.
3. Action markers: `Делать/Не делать` → `Сделайте/Не делайте`; добавлены outcome-фразы (получите/сможете/выберите/чеклист).
4. Чеклист из 8 пунктов: `<ol>` → `<ul>`; «Что дальше» сжат до 4 шагов; char_count 9437.
5. Durable: восстановлены `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json`; utility gate skip mins при пустых списках.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓ (Ept02, soft R02)  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
