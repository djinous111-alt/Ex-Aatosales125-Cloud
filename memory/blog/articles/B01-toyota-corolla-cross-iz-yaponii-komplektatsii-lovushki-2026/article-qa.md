# Article QA — B01 Toyota Corolla Cross из Японии

**topic_id:** B01  
**slug:** toyota-corolla-cross-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-corolla-cross-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-28  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-28; sources 29; pain_solution 7 |
| utility gate | PASS | action 23 / pain 2 / outcome 9; H2×7 FAQ×7 table×1 |
| human-voice | PASS | warn: exactly-5 lists (known false-positive on ≥5 ol); story/pain/outcome/success overlap OK |
| fact-check | PASS | 5 stats; verified 2; unverified 2025/2023/160 в research-notes |
| link-verify | PASS | 3/3 live OK после env CTA; в git снова `${CATALOG_URL}`/`${TELEGRAM_URL}`/`${MAX_URL}` (secret-scan) |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU 72.2 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Beginner-fit

**PASS.** Статья для первого заказа через Владивосток, не для профи-разработчиков: коды кузова, E-Four, оценка листа и экспорт гибрида объяснены «на пальцах»; первый безопасный шаг — бриф до ставки без депозита «на слово».

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Перепутать седан Corolla / JP Cross / CN LHD, букву Z с оценкой аукциона, поставить ставку на гибрид без экспорта |
| Где решение | H2: отсев кузовов → коды ZSG/ZVG/MXGH → комплектации → топливо/экспорт → лист → чек-лист Владивосток |
| Первый результат | Заполненный одностраничный бриф + умение отсечь лоты без кода/листа, с R/XX, гибриды без экспорта |
| Термины «на пальцах» | E-Four, ZSG10 vs ZVG*, комплектация Z ≠ оценка «4/Z», JP RHD vs CN LHD |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; CTA×3; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт, таблица кодов, схема, FAQ×7, чеклист |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | PASS; warn списков |
| Fact safety | 13/15 | Даты/клиренс не в fact-bank, есть в research-notes |
| Contract HTML | 10/10 | Whitelist PASS, ~9262 знаков, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «тойота королла кросс из японии» в meta/H1 |
| C02 | ✓ | Lead сразу называет боль и обещает коды/комплектации/ловушки |
| C03 | ✓ | Читатель: семья/первый заказ JP Cross до ставки |
| C04 | ✓ | ZSG/ZVG/MXGH, G/S/Z/GR, E-Four, лист объяснены |
| O01 | ✓ | H2 = outline research (кузова → коды → комплектации → экспорт → лист → чеклист) |
| O02 | ✓ | Логичный how-to до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + схема, mode B |
| R01 | ✓ | Инсайт, схема до ставки, FAQ |
| R02 | ✓ | Май 2025 / авг 2023 / коды из research |
| R03 | ✓ | Нет готовых «под ключ» сумм; расчёт в каталоге |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки» + JP vs CN + гибрид-ловушка |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог + Telegram + MAX |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Экспорт гибрида, R/XX, пробег*, путаница Z |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution map

- **Lead pain:** седан vs Cross, JP vs CN, Z vs оценка, ставка на невыездной гибрид  
- **H2 solutions:** фильтр кузовов; коды; комплектации; топливо/экспорт; лист; чек-лист  
- **Success before FAQ:** критерий успеха + бриф; CTA после чек-листа

## Link verify

- total: 3, failed: 0  
- see `link-verify.json`

## AI-slop scan

- cliches: 0  
- over-long: 6 (не блокер)  
- Flesch RU: 72.2

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T Author: pending (cover/schema вне зоны QA)

## FIX cycle (QA)

1. Insight label: `TL;DR / Быстрый инсайт` → `Инсайт до ставки` (контракт skill).  
2. CTA: live-expand env для link-verify PASS 3/3; перед commit вернуть `${…}` плейсхолдеры (CATALOG/TELEGRAM/MAX — Cloud Secrets, pre-commit блокирует значения).  
3. `link-verify.json` санитизирован (placeholder URLs + verdict pass).  
4. Re-run gates после insight FIX: PASS.

## Blockers

- нет

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
