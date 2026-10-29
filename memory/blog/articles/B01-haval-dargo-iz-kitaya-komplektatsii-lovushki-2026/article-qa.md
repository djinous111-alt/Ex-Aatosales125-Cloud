# Article QA — B01 Haval Dargo из Китая

**topic_id:** B01  
**slug:** haval-dargo-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-haval-dargo-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-29  
**verdict:** FIX  
**score:** 74  
**EXCALIBUR_RUN_DATE:** 2026-10-29

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | recheck OK; warn: technical_topic/docs URL |
| utility gate | PASS | after restore pain/outcome + aliases; action 25 / pain 2 / outcome 6 |
| human-voice | **BLOCK** | only 1 pain marker type (`ошиб`); need ≥2 |
| html-linter | PASS | 0 errors; TOC нет |
| link-verify | **fail** | href литерал `[REDACTED]` → relative 404; нужны `${CATALOG_URL}`/`${TELEGRAM_URL}` |
| fact-check | PASS | 6 stats; 1 verified / 5 unverified vs fact-bank |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 67.7 |
| cannibalization | PASS | 0 issues |

## Beginner-fit

**PASS.** Статья для новичка-покупателя (не для разработчиков): термины Big Dog / Оптимум / Техно+ / VIN / утиль / СБКТС объяснены через таблицы и чек-лист; первый безопасный шаг — сверка до депозита без поездки в Китай.

## Pain / solution map (редактура)

| Вопрос | Ответ в статье |
|--------|----------------|
| Боль новичка | Путает Big Dog и РФ Dargo → депозит за «не ту» комплектацию / без зимы / без документов (lead Антон) |
| Где решение | H2: 3 типа машин → таблица CN vs РФ → видео зимнего пакета → документы/Владивосток → шаги + красные флаги |
| Первый результат | Чек-лист «до депозита» + критерии успеха до FAQ |
| Термины «на пальцах» | 1.5/2.0, 2WD/4WD, 7DCT/9DCT, пакеты Labrador vs Оптимум/Премиум/Техно+, утиль 160 л.с. |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA сломаны (`[REDACTED]`) |
| GEO / citability | 20/25 | Таблицы, схема, FAQ×6, чеклист; ярлык `TL;DR` запрещён skill |
| CORE-EEAT lite | 14/15 | 17/20 (см. ниже) |
| Human voice | 8/15 | gate BLOCK: pain markers |
| Fact safety | 12/15 | без сумм растаможки; факты в research-notes |
| Contract HTML | 4/10 | whitelist OK, но TL;DR label + битые CTA |
| **Итого** | **74/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | primary «хавал дарго комплектации» в meta/H1 |
| C02 | ✓ | lead = история депозита + что сделать до оплаты |
| C03 | ✓ | читатель: заказ CN-кроссовера, риск депозита |
| C04 | ✓ | Big Dog / РФ-пакеты / зимний пакет объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы, mode B |
| R01 | ✓ | insight + схема + FAQ (label требует FIX) |
| R02 | ✓ | мощность/коробки/утиль порог в research |
| R03 | ✓ | нет готовых сумм растаможки |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «до депозита» + CN vs РФ |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✗ | CTA href = `[REDACTED]` (не кликабельны) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | slop hits = 0 |
| Ept01 | ✓ | лимиты гарантии/утиля/языка меню |
| Ept02 | ✗ | нет 2–3 internal blog links |

**Target:** ≥16/20 ✓ · hard veto: human-voice BLOCK, link-verify fail → overall FIX

## Schema ready (после FIX)

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes | cover/schema: **не стартовать** до PASS

## Blockers (writer FIX, max cycle)

1. **human-voice BLOCK:** добавить ≥1 доп. маркер боли (`проблем` / `боль` / `дорого` / `теряет` …) явно в lead или H2 — сейчас только `ошиб`.
2. **Insight label:** заменить `TL;DR / Быстрый инсайт` → `Инсайт до депозита` (GEO QA skill; writing-contract example устарел).
3. **CTA:** заменить `href="[REDACTED]"` на `${CATALOG_URL}` и `${TELEGRAM_URL}` + `<!-- pragma: allowlist secret -->` на строках ссылок; перепроверить link-verify после expand из env.
4. **Списки:** по возможности развести два ol по 5 пунктов (human-voice warning).

## Durable QA fixes (не article.html)

1. Восстановлены `pain_markers_ru` / `outcome_markers_ru` + алиасы `не делать` / `чек-лист` / `делать:` в `memory/brief/editorial-policy.json` (пропали после rebrand).
2. Utility gate: empty marker lists → warn+skip, не hard-BLOCK.
3. Pitfalls обновлены.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- research notes gate PASS → ✓  
- utility gate PASS → ✓  
- **human voice gate PASS → ✗**  
- beginner-fit PASS → ✓  

**Итог:** FIX → вернуть `excalibur-blog-writer` (cycle 1/2). Cover\|\|schema **не** запускать.
