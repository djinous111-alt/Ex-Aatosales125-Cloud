# Article QA — B01

**topic_id:** B01  
**slug:** rastamozhka-avto-iz-kitaya-2026  
**article_dir:** memory/blog/articles/B01-rastamozhka-avto-iz-kitaya-2026  
**date:** 2026-10-04  
**verdict:** FAIL  
**score:** 76

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic github false-positive |
| fact-check | PASS | 6 stats; verified 3; unverified: 2025, 160, 1713 (есть в research-notes) |
| link-verify | **FAIL** | 1 unique href = literal `[REDACTED]` ×3 в HTML → internal_relative + site-base → HTTP 404 |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 3 over-long (склейка table/workflow парсером); Flesch RU 66.8 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action_markers 15; pain 4; outcome 9; FAQ×7; tables×2 |
| human-voice gate | PASS | human-voice-report.json status PASS |

## Pain / solution / beginner-fit

| Check | Result | Evidence |
|-------|--------|----------|
| Боль новичка в lead | PASS | «Машина уже едет… боюсь сюрприза»; история Игоря + СВХ/инвойс/160 л.с. |
| H2 = решения | PASS | карта этапов; документы до оплаты; платежи/160; явка; СБКТС/ЭПТС; сам vs ключ; чек-лист; что дальше |
| Результат до FAQ | PASS | «заполненный чек-лист + карта этапов… сможете запросить платежи по своим цифрам» |
| Термины «на пальцах» | PASS | СВХ, ПТД/декларация, выпуск, СБКТС, ЭПТС, ТПО |
| Beginner-fit | PASS | не tech/RAG/API; первый безопасный шаг = пакет до оплаты + живой расчёт |
| CTA links usable | **FAIL** | все 3 `href` = строка `[REDACTED]`, не URL из conversion-map |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 14/20 | Primary в title/H1; H2/FAQ OK; CTA-ссылки мёртвые |
| GEO / citability | 22/25 | Инсайт, workflow, таблицы, FAQ×7; opener с ярлыком `TL;DR / Быстрый инсайт` |
| CORE-EEAT lite | 13/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS, slop 0 |
| Fact safety | 12/15 | soft unverified vs fact-bank; цифры в research-notes |
| Contract HTML | 0/10 | link-verify FAIL; literal `[REDACTED]` href блокирует publish |
| **Итого** | **76/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка авто из китая» в title / H1 |
| C02 | ✓ | Lead отвечает: этапы + чек-лист до оплаты |
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
| E03 | ✗ | CTA-тексты есть, но `href="[REDACTED]"` не кликабельны |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты сроков, порог л.с., корректировка цены |
| Ept02 | ✗ | Нет 2–3 internal blog links (только CTA; и те сломаны) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate:** link-verify pass — **нет** → overall FAIL

## Link verify

- total unique: 1 (`[REDACTED]`), failed: 1 (404 as site-base + `/[REDACTED]`)
- В HTML 3 якоря с одним и тем же placeholder
- Контроль вне статьи: `CATALOG_URL` + `TELEGRAM_URL` из env дают link-verify PASS (2/2 OK)

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт table/workflow)
- Flesch RU: 66.8

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | Author registry: pending schema agent  
**Не запускать cover/schema** до FIX writer + повторного GEO QA PASS.

## Blockers

1. **link-verify FAIL** — все CTA `href` заменены на literal `[REDACTED]` вместо URL из `memory/brief/conversion-map.md` / `CATALOG_URL` / `TELEGRAM_URL`.

## FIX cycle (QA → Writer) — обязательно

1. **CRITICAL CTA:** в `article.html` заменить 3 вхождения `href="[REDACTED]"`:
   - 2× каталог (`каталоге avto-sales125.ru`, `каталоге Авто-Сейлс`) → URL «Каталог авто» из conversion-map / `CATALOG_URL`;
   - 1× Telegram `@avtosales125` → URL «Telegram Авто-Сейлс» / `TELEGRAM_URL`.
2. Не использовать строку `[REDACTED]` как href (это secret-scan placeholder, не CTA).
3. После правки: `python3 scripts/excalibur_blog_link_verify.py … --site-base "$PUBLIC_SITE_URL"` → PASS, затем повтор GEO QA.

## FIX (non-blocking / optional)

1. **Insight opener:** убрать точный ярлык `TL;DR / Быстрый инсайт:` в начале blockquote (GEO skill); оставить смысл выжимки. Writing-contract example пока конфликтует — durable align через fixer.
2. **Ept02:** 2–3 internal links на AS08/AS09 с `anchor_variants` после появления public permalinks.
3. **fact-bank soft:** дописать 160 л.с. / ПП 1713 / 01.12.2025.

## Gate

- score ≥ 80 → **76** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** FAIL — вернуть Writer (FIX CTA href). Cover || schema **не** стартовать.
