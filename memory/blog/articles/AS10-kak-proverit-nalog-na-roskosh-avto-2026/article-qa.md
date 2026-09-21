# Article QA — AS10

**topic_id:** AS10  
**slug:** kak-proverit-nalog-na-roskosh-avto-2026  
**article_dir:** memory/blog/articles/AS10-kak-proverit-nalog-na-roskosh-avto-2026  
**date:** 2026-07-26  
**verdict:** PASS  
**score:** 84

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=today; source_table/accessed_at OK; technical_topic=false |
| fact-check | PASS | 14 stats extracted; 4 verified / 10 unverified vs fact-bank |
| link-verify | PASS | 3/3 OK (catalog, telegram, nalog.gov.ru calc); `--site-base` from env |
| html-linter | PASS | whitelist OK; TOC в теле нет; без pre/code |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 63.8 |
| cannibalization | PASS | `--blog-dir memory/blog/articles` → `-o …/cannibalization-report.json`; 0 issues |
| utility gate | PASS | pain=3, outcome=8, action=12; после Fixer editorial-policy markers |
| human-voice-gate | PASS | warnings: Fact Check template + 2× exactly-5-step lists (soft) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; meta_ab OK; мало internal blog links |
| GEO / citability | 22/25 | схема, таблица порогов, FAQ×6, чеклисты; soft: ярлык TL;DR в инсайте |
| CORE-EEAT lite | 18/20 | 18/20 self-check |
| Human voice | 14/15 | gate PASS; soft template warnings |
| Fact safety | 12/15 | рамка НК/ФНС ок; часть цифр (573/581, пример 202050) unverified в fact-bank |
| Contract / utility | 10/10 | utility PASS (pain≥2, outcome≥3); whitelist PASS |
| **Итого** | **84/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «налог на роскошь автомобили 2026» в meta/H1 |
| C02 | ✓ | Lead: сюрприз ×3 после депозита → сверка до оплаты |
| C03 | ✓ | Читатель: заказ авто из Азии, риск коэффициента |
| C04 | ✓ | Перечень / коэффициент 3 / средняя стоимость объяснены |
| O01 | ✓ | H2 = pain_solution_map (до депозита → перечень → пороги → рынки → флаги → чеклист) |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + blockquotes, mode B |
| R01 | ✓ | инсайт-блок, схема, критерий результата, FAQ |
| R02 | ✓ | порог 10 млн, ×3, сроки уплаты, примеры моделей из research |
| R03 | ✓ | нет обещаний %/цен лотов; суммы пошлин отложены в каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «до депозита / до заказа из Азии» |
| E02 | ✓ | делать/не делать в H2 (избегайте эмоций, не верьте «дешевле 10 млн») |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | тон Авто-Сейлс / research |
| Exp03 | ✓ | slop cliches = 0 |
| Ept01 | ✓ | риски комплектации/года/мощности |
| Ept02 | ✗ | нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · **veto utility gate:** нет

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Сюрприз транспортного налога ×3 после депозита/растаможки; фраза посредника «дешевле 10 млн» не спасает |
| Где решение | H2: перечень Минпромторга → пороги/возраст → маршруты CN/KR/JP → красные флаги → чеклист до оплаты |
| Первый результат | Заметка/скрин «модель X, версия Y, год Z – в перечне 2026: да/нет» + порядок л.с.×ставка×3 |
| Термины «на пальцах» | «налог на роскошь» = коэффициент 3 к транспортному; перечень = файл Минпромторга; средняя стоимость ≠ цена в договоре |
| Beginner-fit | PASS — без dev-жаргона, есть безопасный шаг до депозита |

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 63.8

## Soft findings (не блокируют)

- Ярлык `TL;DR / Быстрый инсайт` в инсайт-блоке (skill discourages) — текст не переписывали: gates PASS, score≥80.
- human-voice WARN: Fact Check template + 2× exactly-5-step lists.

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: **ready after Director**

## Blockers

- нет

## FIX cycle (QA)

- не требуется (re-QA после Fixer INC-0918: editorial-policy markers → utility PASS)
- article.html без изменений

## Gate

- score ≥ 80 → **84** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- human-voice-gate PASS ✓  
- utility gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — cover||schema можно запускать.
