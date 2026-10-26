# Article QA — B01

**topic_id:** B01  
**slug:** haval-jolion-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-haval-jolion-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-27  
**verdict:** FAIL  
**score:** 74  
**author_id:** avtosales-editorial (registry OK)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN: technical_topic false-positive (see INC-20261027-0020) |
| utility gate (stock policy) | BLOCK | `pain_markers=0` / `outcome_markers=0` — пустые списки в `editorial-policy.json` |
| utility gate (FALLBACK markers) | PASS | overlay `utility-gate-policy-fallback.json` = human-voice PAIN/OUTCOME; metrics pain=4 outcome=6 action=13 |
| human-voice-gate | PASS | WARN: multiple exactly-5-step lists; pain/outcome/story overlap OK |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| fact-check | PASS | 4 stats; verified 1 (`2026`); unverified: 2023 / 143 / 270 (есть в research-notes) |
| link-verify | FAIL | 1 unique href = литерал `[REDACTED]` → internal_relative + site-base → HTTP 404 |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы); Flesch RU 65.8 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Beginner-fit / pain→outcome

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит на «красивый Премиум из Китая» без сверки привода/КПП/VIN → без гарантии/запчастей |
| Где решение | H2: сверка с РФ-матрицей; сравнение Comfort/Оптимум/Premium/Techno+; ловушки ввоза; VIN до перевода; чек-лист 10 пунктов |
| Первый результат | Заполненный 10-пунктный лист до депозита + стоп без VIN |
| Термины «на пальцах» | 2WD/4WD, MT/7DCT, СВХ, СБКТС, ЭПТС объяснены в lead-секции |

**beginner-fit:** PASS (не tech-pro tone; есть безопасный первый шаг до денег).

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; H2 action; CTA-текст есть, но href сломан (−4) |
| GEO / citability | 22/25 | Insight, таблица, FAQ×7, чеклисты; ярлык `TL;DR / Быстрый инсайт` шаблонный (−1) |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 14/15 | 0 AI-slop; warn по 5-step lists |
| Fact safety | 12/15 | Цифры в research; не все в fact-bank |
| Contract HTML | 8/10 | Whitelist PASS; CTA href=`[REDACTED]` ломает publish-ready (−2) |
| **Итого** | **74/100** | ниже порога 80 из-за link-verify + CTA |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «хавал джолион из китая» в H1/title |
| C02 | ✓ | Lead: боль депозита → чек-лист до оплаты |
| C03 | ✓ | Читатель: новичок параллельного ввоза Jolion |
| C04 | ✓ | 2WD/4WD, DCT, СВХ, СБКТС, ЭПТС |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol + table + mode B |
| R01 | ✓ | Insight + таблица + FAQ |
| R02 | ✓ | Ориентиры МЦП / 270 Нм / 2023 в research |
| R03 | ✓ | Нет «цены под ключ»; якоря с оговоркой |
| R04 | ✓ | FAQ ответ с 1-го предложения |
| E01 | ✓ | Угол «до депозита» + Chitu/Jolion Pro |
| E02 | ✓ | Делать / Не делать |
| E03 | ✗ | CTA текстами есть, но 3× `href="[REDACTED]"` не кликабельны |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты гарантии серого ввоза |
| Ept02 | ✗ | Нет internal blog links на AS08/AS09 |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate link-verify:** FAIL → overall FAIL

## Link verify

- total unique: 1 (literal placeholder `[REDACTED]`), failed: 1 (404 via site-base)
- Ожидаемый паттерн: те же абсолютные CTA, что в AS09 (`$CATALOG_URL` + `$TELEGRAM_URL`), ≤3 ссылки, без форм
- При commit: строки с CTA помечать `pragma: allowlist secret` — `CATALOG_URL`/`TELEGRAM_URL` в Cloud secrets scanner

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт table/schema)
- Flesch RU: 65.8

## Schema ready

BlogPosting: pending (после FIX) | FAQPage: yes (7) | HowTo: yes | cover/schema: **не стартовать** до QA PASS

## Blockers

1. **link-verify FAIL:** все CTA `href` = литерал `[REDACTED]` — восстановить абсолютные URL из `$CATALOG_URL` / `$TELEGRAM_URL` (как AS09). Placeholder ломает клики и verify.
2. **utility gate stock BLOCK:** durable policy gap — см. INC-20261027-0035; для этой статьи контент закрывает pain→outcome (FALLBACK PASS). Не требует rewrite текста ради маркеров.

## FIX → writer (обязательно)

1. Заменить три `href="[REDACTED]"` на значения env `$TELEGRAM_URL` (якорь Telegram) и `$CATALOG_URL` (якоря каталога; можно 2× как AS09).
2. Не оставлять placeholder `[REDACTED]` в HTML.
3. Commit: на строках с CTA добавить `<!-- pragma: allowlist secret -->` (Cloud pre-commit блокирует совпадение с secret values `CATALOG_URL`/`TELEGRAM_URL`).
4. Опционально soft: убрать ярлык `TL;DR / Быстрый инсайт` из первого blockquote (оставить смысл инсайта).
5. Опционально soft: варьировать длину одного из ol≠5 (human-voice warn).

После FIX — повтор GEO QA (link-verify + utility FALLBACK/stock).

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- research notes gate PASS ✓  
- utility gate PASS (FALLBACK) ✓ / stock BLOCK (policy)  
- human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** FAIL — вернуть writer; cover \|\| schema **не** запускать.
