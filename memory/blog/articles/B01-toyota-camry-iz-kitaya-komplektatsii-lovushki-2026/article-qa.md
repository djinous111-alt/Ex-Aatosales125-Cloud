# Article QA — B01 Toyota Camry из Китая

**topic_id:** B01  
**slug:** toyota-camry-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-camry-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-28  
**verdict:** PASS  
**score:** 87

## Beginner / pain–solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит за «красивую Камри» из чата без сверки Elite/Sport/Premium, мотора 2.0 vs HEV 2.0/2.5 и путаницы 180 дней КНР с льготой утильсбора |
| Где решение | H2: рынок China Market vs Япония/Корея → таблица моторов XV80 → ловушка утильсбора → 180 дней vs 12 месяцев → стоп-пакет VIN → чек-лист Владивосток |
| Первый результат | Заполненный чек-лист до депозита на один VIN: две комплектации, мотор/поколение, 180 дней vs льгота, решение плачу/жду/отказываюсь |
| Термины «на пальцах» | XV80 = поколение кузова; параллельный гибрид; 30-минутная мощность электромотора из бумаг; China Market / GAC Toyota; полоса объёма ~1987 vs ~2487 см³ |

**beginner-fit:** PASS (нет API/RAG/MCP-жаргона; `Workflow` заменён на «Схема до денег»; безопасный первый шаг — сверка до депозита)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=today; warn: no official docs URL (автотема) |
| fact-check | PASS | 11 stats; 2 verified / 9 unverified vs fact-bank (ориентиры кВт/см³ + даты норм — в research-notes) |
| link-verify | PASS | 3/3 live (каталог + Telegram + 2GIS); в git — `${CATALOG_URL}` / `${TELEGRAM_URL}` |
| html-linter | PASS | whitelist OK; TOC нет; инсайт без TL;DR |
| slop-detector | WARNING→ok | 0 клише; 7 over-long; Flesch RU 68.4 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |
| utility gate | PASS | action 16 / pain 26 / outcome 14 |
| human voice gate | PASS | human-voice-report.json; overlap story/pain/outcome/success/voice |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «тойота камри из китая» в title/H1/lead; H2 how-to; CTA×3; мало internal blog links |
| GEO / citability | 23/25 | Инсайт, таблицы моторов/норм, FAQ×6, чеклисты, без статичных сумм утильсбора |
| CORE-EEAT lite | 18/20 | см. ниже |
| Human voice | 14/15 | PASS gate; конкретные маркеры + история Антона |
| Fact safety | 13/15 | Логика ПП 1713 / 180 дней; цифры как ориентир; расчёт только по VIN |
| Contract HTML | 10/10 | Whitelist PASS; ~9.8k; FAQ; CTA placeholders; Fact box = Редакция Авто-Сейлс |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: стоп до сверки двух комплектаций + VIN |
| C03 | ✓ | Читатель — заказ Camry China до депозита |
| C04 | ✓ | XV80, HEV, 30-мин мощность, 180 дней объяснены |
| O01 | ✓ | H2 = research outline |
| O02 | ✓ | Логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы + blockquotes, mode B |
| R01 | ✓ | Инсайт + схема до денег + FAQ |
| R02 | ✓ | Ориентиры 公告 / рестайл 2026 / нормы в research |
| R03 | ✓ | Нет статичных рублей утильсбора |
| R04 | ✓ | FAQ отвечает с первого предложения |
| E01 | ✓ | Угол «до депозита» + ловушки соседних trim |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×1 + Telegram×1 + 2GIS×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: ориентир ≠ VIN; 180 ≠ льгота РФ |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- see `link-verify.json` (placeholders sanitized)

## AI-slop scan

- cliches: 0
- over-long: 7
- Flesch RU: 68.4

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T Author: pending (schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Инсайт: `TL;DR / Быстрый инсайт` → `Инсайт до депозита` (GEO QA skill forbid).
2. Beginner-fit: `Workflow до денег` → `Схема до денег`.
3. CTA: live URL → `${CATALOG_URL}` / `${TELEGRAM_URL}` в committed HTML; expand только для link-verify; sanitize report.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
