# Article QA — B01

**topic_id:** B01  
**slug:** rastamozhka-avto-iz-korei-2026  
**article_dir:** memory/blog/articles/B01-rastamozhka-avto-iz-korei-2026  
**date:** 2026-10-13  
**verdict:** PASS  
**score:** 88  
**qa_cycle:** 2 / 2 (re-QA after writer FIX)

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Путаница ПТД/СВХ/коносамент; попытка «подать декларацию, пока судно в море»; риск платного простоя и чужих сумм пошлин |
| Где боль в lead | Абзац про Игоря + депозит до выгрузки; ПТД нельзя до СВХ |
| Где решение (H2) | Маршрут на пальцах → правило ПТД после СВХ → чек-лист документов → где считать платежи → анти-простой СВХ → чек-лист до депозита |
| Первый результат до FAQ | Критерий в H2 «Пройдите финальный чек-лист…»: объяснить маршрут, знать момент ПТД, пакет до ETA, горизонт 45–55 дней, персональный расчёт |
| Термины «на пальцах» | СВХ, коносамент, ПТД, СБКТС, ЭПТС, ТСЛП — объяснены в первых H2 |

**beginner-fit:** PASS (не enterprise/dev-тон; есть безопасный шаг до депозита)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: нет official docs URL (topic customs, ok) |
| fact-check | PASS | 9 stats; verified 2 / unverified 7 (есть в research-notes) |
| link-verify | PASS (soft) | 2 unique href: catalog HTTP 503 soft-pass brand 5xx (href = `CATALOG_URL`, absolute https); telegram HTTP 200. См. `link-verify.json` `soft_pass_applied` |
| html-linter | PASS | whitelist OK; TOC в теле нет; ярлык TL;DR / Быстрый инсайт отсутствует |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 66.3 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | `utility-gate-report.json` |
| human-voice gate | PASS | `human-voice-report.json`; WARN: multiple exactly-5-step lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1; H2=how-to; CTA catalog×2 + Telegram×1 с живыми href |
| GEO / citability | 22/25 | Инсайт без шаблонного ярлыка, схема, таблица сроков, FAQ×7, чеклисты |
| CORE-EEAT lite | 18/20 | см. таблицу ниже |
| Human voice | 14/15 | Gate PASS; WARN про списки по 5 пунктов |
| Fact safety | 12/15 | Цифры в research-notes; часть не в fact-bank |
| Contract HTML | 4/10 | base 10; −3 soft catalog 503 egress; −3 нет internal links (Ept02). Linter/CTA/FAQ зелёные |
| **Итого** | **88/100** | 18+22+18+14+12+4 |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка авто из Кореи» в title / H1 |
| C02 | ✓ | Lead сразу про ловушку ПТД до выгрузки |
| C03 | ✓ | Читатель: заказ из Кореи через Владивосток, новичок |
| C04 | ✓ | СВХ / коносамент / ПТД / СБКТС / ЭПТС объяснены |
| O01 | ✓ | H2 = этапы research outline |
| O02 | ✓ | Логичный how-to порядок |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица, mode B |
| R01 | ✓ | Инсайт + схема + FAQ |
| R02 | ✓ | 2,9 сут / 45–55 дн / ст. 119 в research-notes |
| R03 | ✓ | Нет готовых сумм пошлин; расчёт под VIN |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «не подавать ПТД раньше СВХ» |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA catalog×2 + Telegram×1 — живые absolute href из env (не литерал `[REDACTED]`) |
| Exp01 | ✓ | Mode B, без fake first-person hero |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: нет точной пошлины; льготные сутки зависят от склада |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога (Indexer может добавить) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate link-verify:** PASS (soft brand catalog 5xx)

## Link verify

- total unique: 2 (catalog + telegram)
- catalog: HTTP 503 from cloud egress → **soft-pass** (href absolute, equals `CATALOG_URL`; не placeholder)
- telegram: HTTP 200 OK
- failed_count after soft-pass: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 66.3

## Schema ready

BlogPosting: ready for schema Task | FAQPage: yes (7) | HowTo: yes | cover/schema: **можно** стартовать после этого PASS

## Blockers

нет

## FIX (writer) — закрыто в cycle 1

1. ~~CTA href `[REDACTED]`~~ → live `CATALOG_URL`×2 + `TELEGRAM_URL`×1  
2. ~~Ярлык TL;DR / Быстрый инсайт~~ → убран  
3. Soft-pass catalog 503 задокументирован (не writer defect)

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links (Indexer / post-publish).  
2. **human-voice WARN:** разная длина списков.  
3. **fact-bank soft:** дописать 2,9 сут / 45–55 дн / тарифы СВХ.  
4. **link-verify script:** durable soft-pass brand catalog 5xx в `excalibur_blog_link_verify.py` (см. INC catalog-503).

## Gate checklist

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✓ (soft brand 5xx)  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✓  
- human-voice-report.json PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — директор может запускать cover || schema.
