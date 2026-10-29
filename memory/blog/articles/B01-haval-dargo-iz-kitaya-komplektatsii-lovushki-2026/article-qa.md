# Article QA — B01 Haval Dargo из Китая (re-run after FIX cycle 1)

**topic_id:** B01  
**slug:** haval-dargo-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-haval-dargo-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-29  
**verdict:** PASS  
**score:** 87  
**EXCALIBUR_RUN_DATE:** 2026-10-29  
**fix_cycle_applied:** writer 1/2 (insight / CTA / pain markers)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: technical_topic/docs URL |
| utility gate | PASS | action 25 / pain 3 / outcome 6 |
| human-voice | **PASS** | pain: `проблем` + `ошиб`; warn: exactly-5 lists×2 |
| html-linter | PASS | 0 errors; TOC нет |
| link-verify | **pass** | 2/2 OK (HEAD 200); CTA `${CATALOG_URL}` / `${TELEGRAM_URL}` after env expand |
| fact-check | PASS | 6 stats; 1 verified / 5 unverified vs fact-bank |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 67.7 |
| cannibalization | PASS | 0 issues |

## Writer FIX 1 — verified

| Expectation | Result |
|-------------|--------|
| Insight label `Инсайт до депозита` (не TL;DR) | OK |
| CTA `${CATALOG_URL}` / `${TELEGRAM_URL}` + pragma | OK |
| pain markers `проблем` + `ошиб` | OK (human-voice) |
| char_count ~9182 | OK (meta 9182; collapse-ws ≈9181) |

## Beginner-fit

**PASS.** Статья для новичка-покупателя: Big Dog / Оптимум / Техно+ / VIN / утиль / СБКТС через таблицы и чек-лист; первый безопасный шаг — сверка до депозита без поездки в Китай.

## Pain / solution map

| Вопрос | Ответ в статье |
|--------|----------------|
| Боль новичка | Путает Big Dog и РФ Dargo → депозит за «не ту» комплектацию / без зимы (lead Антон + «проблема новичка») |
| Где решение | H2: 3 типа машин → CN vs РФ → зимний пакет на видео → документы/Владивосток → шаги + красные флаги |
| Первый результат | Чек-лист до депозита + H2 «Как понять, что вы готовы…» до FAQ |
| Термины «на пальцах» | 1.5/2.0, 2WD/4WD, 7DCT/9DCT, Labrador vs Оптимум/Премиум/Техно+, утиль 160 л.с. |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1; H2 action; CTA placeholders OK |
| GEO / citability | 21/25 | Таблицы×2, FAQ, чек-лист, insight; − за over-long / unverified nums |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 13/15 | gate PASS; warn exactly-5 lists |
| Fact safety | 12/15 | без сумм растаможки; 5 unverified vs fact-bank |
| Contract HTML | 9/10 | whitelist + insight + CTA pragma |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | primary «хавал дарго комплектации» в meta/H1 |
| C02 | ✓ | lead = история депозита + что сделать до оплаты |
| C03 | ✓ | читатель: заказ CN-кроссовера, риск депозита |
| C04 | ✓ | Big Dog / РФ-пакеты / зимний пакет объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | логичный порядок до депозита |
| O03 | ✓ | FAQ 6+ |
| O04 | ✓ | ol/ul + 2 таблицы, mode B |
| R01 | ✓ | insight «Инсайт до депозита» + схема + FAQ |
| R02 | ✓ | мощность/коробки/утиль порог в research |
| R03 | ✓ | нет готовых сумм растаможки |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «до депозита» + CN vs РФ |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA `${CATALOG_URL}` / `${TELEGRAM_URL}` кликабельны после expand |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | slop hits = 0 |
| Ept01 | ✓ | лимиты гарантии/утиля/языка меню |
| Ept02 | ✗ | нет 2–3 internal blog links (Indexer) |

**Target:** ≥16/20 ✓ · hard veto: none → overall PASS

## Schema ready

BlogPosting: yes | FAQPage: yes | HowTo: yes | cover/schema: **можно** после handoff PASS

## Soft notes (не blocker)

1. human-voice warn: 2× exactly-5 lists — по возможности варьировать (не FIX cycle).
2. slop: 4 over-long (в т.ч. табличные строки) — косметика.
3. Internal interlinks — зона Indexer.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✓  
- research notes gate PASS → ✓  
- utility gate PASS → ✓  
- **human voice gate PASS → ✓**  
- beginner-fit PASS → ✓  

**Итог:** PASS → директор запускает cover \|\| schema.
