# Article QA — B01

**topic_id:** B01  
**slug:** rastamozhka-avto-iz-kitaya-2026  
**article_dir:** memory/blog/articles/B01-rastamozhka-avto-iz-kitaya-2026  
**date:** 2026-10-04  
**verdict:** PASS  
**score:** 90  
**qa_cycle:** 2 (re-QA after Writer FIX CTA)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic github false-positive |
| fact-check | PASS | 6 stats; verified 3; unverified: 2025, 160, 1713 (в research-notes) |
| link-verify | PASS | 2/2 OK (catalog + Telegram; unique hrefs) |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 3 over-long (склейка table/workflow); Flesch RU 66.6 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action_markers 15; pain 4; outcome 9; FAQ×7; tables×2 |
| human-voice gate | PASS | human-voice-report.json status PASS |

## Pain / solution / beginner-fit

| Check | Result | Evidence |
|-------|--------|----------|
| Боль новичка в lead | PASS | «Машина уже едет…»; страх сюрприза / СВХ; история Игоря |
| H2 = решения | PASS | карта этапов; документы до оплаты; платежи/160; явка; СБКТС/ЭПТС; сам vs ключ; чек-лист; что дальше |
| Результат до FAQ | PASS | заполненный чек-лист + карта этапов → «сможете запросить платежи по своим цифрам» |
| Термины «на пальцах» | PASS | СВХ, ПТД/декларация, выпуск, СБКТС, ЭПТС, ТПО |
| Beginner-fit | PASS | не tech/API; первый шаг = пакет до оплаты + живой расчёт |
| CTA links usable | PASS | `CATALOG_URL`×2 + `TELEGRAM_URL`×1; link-verify 200 |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2/FAQ; CTA OK; нет 2–3 blog internal |
| GEO / citability | 24/25 | «Коротко по делу», workflow, таблицы, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice PASS, slop 0 |
| Fact safety | 12/15 | soft unverified vs fact-bank; цифры в research-notes |
| Contract HTML | 10/10 | whitelist PASS; CTA live; объём ~9079; FAQ; без форм |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка авто из китая» в title / H1 |
| C02 | ✓ | Lead: этапы + чек-лист до оплаты |
| C03 | ✓ | Читатель: первый ввоз из Китая, страх СВХ/сюрприза |
| C04 | ✓ | СВХ / ПТД / СБКТС / ЭПТС / ТПО объяснены |
| O01 | ✓ | H2 = pain_solution_map research |
| O02 | ✓ | Логичный outline до ГИБДД |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + 2 таблицы + workflow, mode B |
| R01 | ✓ | Инсайт + workflow + FAQ |
| R02 | ✓ | 33,5 тыс. / 545 (~1,6%) Уссурийск |
| R03 | ✓ | Нет статичных сумм платежей |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол Владивосток / документы до оплаты |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 (живые URL) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты сроков, порог л.с., корректировка цены |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0
- catalog + Telegram → HTTP 200
- see link-verify.json (URLs redacted to placeholders in commit)

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт table/workflow)
- Flesch RU: 66.6

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | Author registry: pending schema agent

## Blockers

- нет

## FIX cycle history

1. **Cycle 1 FAIL:** literal `href="[REDACTED]"` ×3 → Writer заменил на `CATALOG_URL`/`TELEGRAM_URL`; инсайт → «Коротко по делу».
2. **Cycle 2:** re-QA — все hard gates PASS.

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal blog links (AS08/AS09) с `anchor_variants` — зона Indexer/после publish URL.
2. **fact-bank soft:** 160 л.с. / ПП 1713 / 01.12.2025.

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
