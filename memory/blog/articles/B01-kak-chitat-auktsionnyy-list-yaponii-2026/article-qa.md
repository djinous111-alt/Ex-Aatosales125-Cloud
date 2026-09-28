# Article QA — B01

**topic_id:** B01  
**slug:** kak-chitat-auktsionnyy-list-yaponii-2026  
**article_dir:** memory/blog/articles/B01-kak-chitat-auktsionnyy-list-yaponii-2026  
**date:** 2026-09-29  
**verdict:** PASS  
**score:** 89

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic false-positive (ai in `reader_pain`) |
| fact-check | PASS | 2 stats; verified 2026; unverified Reiwa 2019 (research-notes / common knowledge) |
| link-verify | PASS | 2/2 OK (каталог + Telegram) |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long; Flesch RU 67.0 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action_markers ≥8; pain/outcome markers OK; char_count 9477 |
| human-voice gate | PASS | pain/outcome/concrete OK; warn: exactly-5-step lists heuristic |

## Pain / solution / result (beginner-fit)

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка решена? | Смотрит только балл/цену в йенах, боится R, пропускает схему и примечания до депозита |
| Где показано решение? | H2: порядок чтения → R/RA → коды схемы → перевод примечаний → пробег/кузов/салон → фото + решение → чеклист 10 |
| Первый результат читателя | Решение «ставлю / уточняю / пропускаю» до депозита; критерий «вслух» до FAQ |
| Термины «на пальцах» | R/RA = история каркаса; XX/W = панели; 特記事項 = рукописные примечания; балл = фильтр |

**Beginner-fit:** PASS — тон для новичка, первый безопасный шаг без «команды профи».

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; CTA; мало internal blog links |
| GEO / citability | 23/25 | инсайт-блок, workflow →, таблица кодов, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice PASS; concrete markers OK |
| Fact safety | 13/15 | JAAI / R vs RA / коды в Fact Check; 2019 soft unverified |
| Contract HTML | 10/10 | whitelist, FAQ, CTA≤3, без форм, ~9477 |
| **Итого** | **89/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в title / H1 |
| C02 | ✓ | Lead: ошибка Игоря + ответ «порядок до депозита» |
| C03 | ✓ | Читатель: новичок, ставка по листу из Японии |
| C04 | ✓ | R/RA, XX/W, примечания объяснены |
| O01 | ✓ | H2 = pain_solution_map / action outline |
| O02 | ✓ | Логичный outline до чеклиста |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol×2 + таблица + workflow →, mode B |
| R01 | ✓ | Инсайт-блок, схема до депозита, FAQ |
| R02 | ✓ | JAAI / R vs RA / Provide Cars в Fact Check |
| R03 | ✓ | Нет выдуманных цен лотов/% |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита / до ставки» |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person expertise |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: нет R ≠ не битая; автоперевод врёт |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 67.0

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Utility + human-voice BLOCK → маркеры боли/результата/действия слабые; в `editorial-policy.json` не было `pain_markers_ru` / `outcome_markers_ru` (пустой список → вечный BLOCK).
2. FIX: добавлены маркеры в policy; точечные правки `article.html` (Сделайте/Не делайте, чеклист, результат/проблема); убран ярлык `TL;DR / Быстрый инсайт`.
3. Повтор gates → все PASS; char_count 9477.

## FIX (non-blocking / optional)

1. **Ept02:** после publish URL — 2–3 internal links на смежные посты.
2. **fact-check soft:** Reiwa с 2019 — можно в fact-bank.
3. **human-voice warn:** heuristic «exactly-5-step lists» на ol 8+10 — шум.

## Gate

- score ≥ 80 → **89** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
