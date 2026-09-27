# Article QA — AS10

**topic_id:** AS10  
**slug:** tank-300-iz-kitaya-ramnik-ili-krossover-2026  
**article_dir:** memory/blog/articles/AS10-tank-300-iz-kitaya-ramnik-ili-krossover-2026  
**date:** 2026-09-27  
**verdict:** FAIL  
**score:** 72

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic false-positive (см. INC-20260927-1715) |
| fact-check | PASS | 11 stats; verified 1 (2026); 10 unverified vs fact-bank (ТТХ/пороги есть в research-notes) |
| link-verify | FAIL | 1/1 failed: literal `href="[REDACTED]"` → treated as internal_relative → HTTP 404 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/чеклист); Flesch RU 74.6 |
| cannibalization | PASS | 0 issues (3 article metas) |
| utility gate | BLOCK | pain_markers=0, outcome_markers=0 — **пустые списки в editorial-policy.json** (не текст статьи) |
| human-voice | PASS | WARN: multiple exactly-5-step lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; H2 action; CTA битые |
| GEO / citability | 22/25 | Insight, таблица, схема →, FAQ×7, чеклист |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | Gate PASS; TL;DR-ярлык в insight |
| Fact safety | 11/15 | Цифры в research-notes; мало в fact-bank; CTA URL битые |
| Contract HTML | 5/10 | Whitelist PASS, объём 9477; **utility BLOCK** + **link-verify FAIL** |
| **Итого** | **72/100** | blockers → FAIL |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «tank 300 из китая» в H1 / meta |
| C02 | ✓ | Lead: боль депозита + рамник vs кроссовер + чеклист |
| C03 | ✓ | Читатель: заказ из Китая, риск депозита |
| C04 | ✓ | Рамник / Part-Time / Сити / утильсбор / VIN / инвойс объяснены |
| O01 | ✓ | H2 = задача → сравнение → привод → мощность → VIN → чеклист |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + workflow →, mode B |
| R01 | ✓ | Insight + схема канала + FAQ |
| R02 | ✓ | ТТХ tank.ru / пороги 160 л.с. в research-notes |
| R03 | ✓ | Нет самодельного калькулятора пошлин |
| R04 | ✓ | FAQ отвечает действием в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + рамник vs кроссовер |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✗ | CTA href = literal `[REDACTED]` (не кликабельны) |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Льгота, VIN, антикор, давление «только сегодня» |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** utility BLOCK, link-verify FAIL → overall FAIL

## Beginner-fit / pain-solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит «по красивому скрину» без понимания: рамник vs кроссовер, льгота утильсбора, VIN/комплектация |
| Где решение | H2: задача → таблица сравнения → Part-Time/Сити → мощность ≤160 → VIN+инвойс → чеклист |
| Первый результат | Заполненный чеклист; выбор «Tank 300 / кроссовер»; депозит не отправлен без VIN |
| Термины «на пальцах» | Рамник, Part-Time, Torque-on-Demand/Сити, утильсбор, VIN, инвойс |

## Link verify

- total unique: 1 (`[REDACTED]`), failed: 1 (404 internal_relative)
- anchor text mentions avto-sales125.ru / @avtosales125, но href невалиден
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/списков)
- Flesch RU: 74.6

## Schema ready

BlogPosting: pending (после PASS) | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no

## Blockers

1. **UTILITY ARTICLE BLOCKER** — `pain_markers_ru` / `outcome_markers_ru` отсутствуют в `memory/brief/editorial-policy.json` → count всегда 0. В тексте уже есть: боль/ошиб/не работает (pain≥2) и результат/проверьте/соберите/выберите (outcome≥3). Нужен Fixer, не рерайт статьи.
2. **link-verify FAIL** — три `<a href="[REDACTED]">`; Writer должен подставить реальные URL из env.

## FIX для Writer (цикл 1)

1. **BLOCKER / links:** заменить все `href="[REDACTED]"` на реальные CTA из env: `PUBLIC_SITE_URL` (каталог, 2 ссылки) и `TELEGRAM_URL` (`@avtosales125`, 1 ссылка). Не оставлять литерал `[REDACTED]` в HTML.
2. **Soft / insight:** убрать шаблонный ярлык `TL;DR / Быстрый инсайт:` в первом `<blockquote>` — заменить на нейтральный заголовок (например «Коротко:» / «Суть:»), без слов TL;DR и «Быстрый инсайт».
3. **Soft / human-voice WARN:** разнести размеры списков (сейчас несколько ровно по 5 пунктов) — один ol/ul сделать 4 или 6 пунктов без потери смысла.
4. **Не нужно** ради utility_gate дописывать «боль/результат» в текст: маркеры уже есть; после Fixer-восстановления policy gate должен пройти без рерайта.

## Gate

- score ≥ 80 → **72** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✗  
- human voice PASS → ✓  
- beginner-fit PASS → ✓ (контент)

**Итог:** FAIL — вернуть Writer (FIX links + soft); параллельно Director → Fixer по INC utility markers. Cover/schema **не** стартовать.
