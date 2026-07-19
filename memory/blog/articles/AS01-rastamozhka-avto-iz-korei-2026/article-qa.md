# Article QA — AS01

**topic_id:** AS01  
**slug:** rastamozhka-avto-iz-korei-2026  
**article_dir:** memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026  
**date:** 2026-07-19  
**verdict:** PASS  
**score:** 89  
**qa_cycle:** re-run after FIX (CTA hrefs + utility markers/policy)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN technical_topic false-positive (api/github) |
| utility gate (topic) | PASS | AS01 how_to / mode B |
| utility gate (article) | PASS | pain_markers=3, outcome_markers=5, action_markers=8 |
| human-voice-gate | PASS | WARN: 2× exactly-5-step lists; pain/outcome/story overlap OK |
| fact-check | PASS | 6 stats; 2 verified / 4 unverified (сроки в research-notes, не в fact-bank) |
| link-verify | PASS | 3 unique href; 0 failed — Trust Encar relative 200; catalog `[REDACTED]` 200; Telegram `t.me/avtosales125` 200 |
| html-linter | PASS | whitelist OK; TOC нет |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/схема); Flesch RU 61.0 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1; H2 action; CTA catalog+Telegram рабочие |
| GEO / citability | 22/25 | TL;DR, схема, таблица сроков, FAQ×6, чеклисты |
| CORE-EEAT lite | 18/20 | см. ниже; E03 ✓ после FIX CTA |
| Human voice | 14/15 | gate PASS; живой кейс Антона |
| Fact safety | 12/15 | сроки ориентиры; без статичных пошлин ✓; 4 unverified vs fact-bank |
| Contract HTML | 10/10 | whitelist PASS; CTA без literal `[REDACTED]` |
| Utility gates | 10/10 | article + topic PASS; human-voice PASS |
| **Итого** | **89/100** | ≥80 → PASS |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка авто из кореи» в meta/H1 |
| C02 | ✓ | Lead: депозит без понимания цепочки → простой СВХ |
| C03 | ✓ | Новичок, заказ из Кореи через Владивосток |
| C04 | ✓ | СВХ / СБКТС / ЭПТС / ТПО / BL объяснены |
| O01 | ✓ | H2 = путь → сроки → документы → расчёт → чеклист → дальше |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote-схема, mode B |
| R01 | ✓ | TL;DR + схема + FAQ |
| R02 | ✓ | Сроки с вилками; источники в research-notes |
| R03 | ✓ | Нет статичных сумм пошлин/утильсбора |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «растаможка ≠ одна пошлина» |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA catalog×2 + Telegram×1, рабочие URL |
| Exp01 | ✓ | Mode B, без fake first-person hero |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: ориентиры сроков, не гарантия; расчёт только у менеджера |
| Ept02 | ✗ | 1 internal blog link (Trust Encar); нет 2–3 стабильных internal |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

| Check | Result |
|-------|--------|
| Боль новичка решена | ✓ Lead: депозит «пока не увели» + непонимание СВХ/СБКТС → простой |
| Где показано решение | ✓ H2 путь/сроки/документы/чеклист до депозита |
| Первый результат до FAQ | ✓ Критерий: объяснить 7–8 этапов и когда машина «на учёте» |
| Термины на пальцах | ✓ СВХ, СБКТС, ЭПТС, BL, ТПО, ПТД |
| Первый безопасный шаг | ✓ Чеклист до депозита; стоп при «просто перевод продавцу» |
| Beginner-fit | **PASS** |

## Pain / solution map (editorial)

- **Боль:** растаможка как чёрный ящик; страх зависания на СВХ Владивостока.
- **Решение:** таймлайн Encar → … → ГИБДД + документы до судна + чеклист до депозита.
- **Результат:** читатель знает этапы/сроки-ориентиры и куда идти за расчётом (каталог/менеджер), без ложного калькулятора.

## Link verify

- total unique: 3, failed: 0
- Trust Encar relative: OK (200)
- catalog `[REDACTED]`: OK (200)
- Telegram `t.me/avtosales125`: OK (200)
- literal `href="[REDACTED]"`: нет
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/схемы)
- Flesch RU: 61.0

## Schema ready

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes | Review: no  
Cover/schema: **разрешены** директору (GEO QA PASS).

## Blockers

- нет

## FIX cycle (закрыт)

1. Writer: CTA hrefs → `[REDACTED]` + `[REDACTED]` (нет literal `[REDACTED]`).
2. Fixer: `editorial-policy.json` pain/outcome markers + utility script skip empty mins.

## Gate

- score ≥ 80 → **89** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✓  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✓  
- human-voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — cover \|\| schema можно запускать.
