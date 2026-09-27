# Article QA — AS10 (re-run after FIX)

**topic_id:** AS10  
**slug:** tank-300-iz-kitaya-ramnik-ili-krossover-2026  
**article_dir:** memory/blog/articles/AS10-tank-300-iz-kitaya-ramnik-ili-krossover-2026  
**date:** 2026-09-27  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic false-positive (INC-20260927-1715) |
| fact-check | PASS | 11 stats; verified 1 (2026); 10 unverified vs fact-bank (цифры в research-notes) |
| link-verify | PASS | 2 unique CTA; failed=0; HEAD 200 (catalog + telegram); href startswith http, len=25, не литерал `[REDACTED]` |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/списки); Flesch RU 74.3 |
| cannibalization | PASS | 0 issues (3 article metas) |
| utility gate | PASS | pain_markers=4, outcome_markers=4; policy markers restored + empty-list defense |
| human-voice | PASS | WARN: multiple exactly-5-step lists (soft) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в H1/title; H2 action; CTA живые |
| GEO / citability | 22/25 | Insight, таблица, схема →, FAQ×7, чеклист |
| CORE-EEAT lite | 15/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | Gate PASS; soft WARN по размерам списков |
| Fact safety | 13/15 | Цифры в research-notes; CTA OK; часть stats вне fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; utility PASS; link-verify PASS |
| **Итого** | **88/100** | ≥80 → PASS |

## CORE-EEAT lite: 19/20

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
| E03 | ✓ | CTA href = реальные http URL (catalog×2 + telegram×1), link-verify 200 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Льгота, VIN, антикор, давление «только сегодня» |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** нет

## Beginner-fit / pain-solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит «по красивому скрину» без понимания: рамник vs кроссовер, льгота утильсбора, VIN/комплектация |
| Где решение | H2: задача → таблица сравнения → Part-Time/Сити → мощность ≤160 → VIN+инвойс → чеклист |
| Первый результат | Заполненный чеклист; выбор «Tank 300 / кроссовер»; депозит не отправлен без VIN |
| Термины «на пальцах» | Рамник, Part-Time, Torque-on-Demand/Сити, утильсбор, VIN, инвойс |

## Link verify

- total unique: 2 (catalog + telegram), failed: 0, verdict pass
- python check: 3 href, all startswith http, lens=[25,25,25], kinds catalog/telegram/catalog
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/списков)
- Flesch RU: 74.3

## Schema ready

BlogPosting: ready for schema agent | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no

## Soft notes (не blockers)

1. human-voice WARN: vary exactly-5-step lists when editorially possible.
2. Ept02: после появления соседних AS-статей можно добавить 2–3 internal blog links (не блокер mode B).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✓  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✓  
- human voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — cover\|\|schema можно стартовать.
