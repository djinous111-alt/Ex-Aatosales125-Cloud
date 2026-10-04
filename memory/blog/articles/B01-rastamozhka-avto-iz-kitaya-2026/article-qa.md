# Article QA — B01

**topic_id:** B01  
**slug:** rastamozhka-avto-iz-kitaya-2026  
**article_dir:** memory/blog/articles/B01-rastamozhka-avto-iz-kitaya-2026  
**date:** 2026-10-05  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | `research_date` = today; pain/outcome/voice fields OK; WARN technical false-positive `/docs` |
| fact-check | PASS | 9 stats; 2 verified vs fact-bank; 7 unverified (160 л.с., 3 400/5 200 ₽, ПП 1291, 1498, 186) — есть в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram); после подстановки `CATALOG_URL`/`TELEGRAM_URL` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long; Flesch RU 61.7 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | numbered 11, FAQ×6, table×1, action 10 / pain 9 / outcome 13 |
| human voice gate | PASS | pain/story/outcome overlap OK; WARN: 2 списка ровно по 5 пунктов |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «как растаможить авто из китая» в title/H1; H2 actionable; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт-блок, таблица платежей, карта этапов, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop hits |
| Fact safety | 13/15 | Ориентиры утильсбора/ПП 1291 в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8631 символов, FAQ×6, CTA≤3, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 / lead |
| C02 | ✓ | Lead — боль депозита + прямой ответ (чек-лист до оплаты) |
| C03 | ✓ | Читатель: новичок с авто из Китая через Владивосток |
| C04 | ✓ | СВХ / СБКТС / ЭПТС / единая ставка объяснены «на пальцах» |
| O01 | ✓ | H2 = action_outline research (параметры → платежи → этапы → ошибки → чеклист → результат → FAQ) |
| O02 | ✓ | Логичный outline до оплаты → ГИБДД |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт-блок, карта этапов, FAQ |
| R02 | ✓ | ПП 1291, utilsbor-calc, elpts — в research-notes с accessed_at |
| R03 | ✓ | Нет «магической» цены под ключ; ориентиры с оговоркой сверки на дату |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до депозита / Владивосток», не абстрактный калькулятор |
| E02 | ✓ | «Делать / Не делать» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Пороги утиля, инвойс, регион/ДФО, путаница выпуск≠ЭПТС |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Проверка | Результат |
|----------|-----------|
| Боль новичка | Депозит по «красивой» цене без понимания таможни/СВХ/утильсбора/ЭПТС во Владивостоке |
| Где решение | H2: 5 параметров → три платежа → этапы порта→ЭПТС → ошибки → чек-лист до оплаты |
| Первый результат | Заполненный чек-лист 5 параметров + стоп-факторы до перевода денег; критерий в H2 до FAQ |
| Термины «на пальцах» | СВХ = камера хранения в порту; СБКТС = подтверждение конструкции; ЭПТС «действующий» ≠ выпуск таможни |
| Beginner-fit | PASS — тон не для брокеров; первый безопасный шаг без команды «профи» |

## Link verify

- total: 2, failed: 0
- see `link-verify.json`
- QA FIX: writer оставил литералы `[CATALOG_URL]` / `[TELEGRAM_URL]` → подставлены абсолютные URL из env; иначе link-verify fail (404 на site-base)

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 61.7

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/этапы) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (после CTA URL FIX)

## FIX cycle (QA)

1. **link-verify FAIL** на литералах `[CATALOG_URL]` / `[TELEGRAM_URL]` (relative → 404). Подставлены `CATALOG_URL` и `TELEGRAM_URL` из env; pragma-комментарии сняты. Повтор: link-verify PASS, html/slop/human-voice/utility/fact-check PASS.

## FIX (non-blocking / optional)

1. **Ept02:** после известных URL AS/B-постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** пороги 160 л.с. / 3 400–5 200 ₽ / ПП 1291 — дописать в fact-bank для verified.
3. **human-voice WARN:** два списка ровно по 5 пунктов — варьировать длину при следующем edit.
4. **Writer contract:** в `article.html` сразу абсолютные CTA URL, не плейсхолдеры env-имён.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
