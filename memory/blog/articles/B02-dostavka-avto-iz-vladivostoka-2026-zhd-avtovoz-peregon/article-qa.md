# Article QA — B02 (FIX cycle 1 rerun)

**topic_id:** B02  
**slug:** dostavka-avto-iz-vladivostoka-2026-zhd-avtovoz-peregon  
**article_dir:** memory/blog/articles/B02-dostavka-avto-iz-vladivostoka-2026-zhd-avtovoz-peregon  
**date:** 2026-10-01  
**verdict:** PASS  
**score:** 88  
**fix_cycle:** 1 rerun (after writer FIX)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical topic without official docs URL |
| utility gate (topic B02) | PASS | comparison / mode B |
| utility gate (article) | PASS | action_markers 10; pain_markers 8; outcome_markers 6 |
| fact-check | PASS | 8 stats; 3 verified / 5 unverified vs fact-bank |
| link-verify | PASS | 2 unique external hrefs OK (catalog + Telegram); failed_count 0; `--site-base $PUBLIC_SITE_URL` |
| html-linter | PASS | 0 errors; TOC нет |
| slop-detector | WARNING | 0 клише; 7 over-long (склейка таблицы/схем); Flesch RU 59.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| human-voice | PASS | warnings: paragraph rhythm variance/avg=0.34; 2× exactly-5-step lists |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Машина с ЭПТС во Владивостоке; три цены/срока; страх переплаты / очереди / царапин без доказательств |
| Где решение | H2: сравнение трёх способов → автовоз → ж/д сетка/контейнер → перегон → чек-лист сдачи → маршрут → критерий готового выбора |
| Первый результат | Выбран один способ + заполненный чек-лист (договор, 2–3 КП, фото, акт, страховка) до FAQ |
| Термины «на пальцах» | ЭПТС, сетка vs контейнер, срок «от сдачи», акт приёма-передачи, ЛКП |
| Beginner-fit | PASS (не dev-тон; есть безопасный первый шаг без команды профи) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в H1/title; H2 actionable; CTA catalog×2 + Telegram×1 OK; нет blog internal |
| GEO / citability | 22/25 | Insight (без ярлыка TL;DR), таблица, схемы →, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | gate PASS; ярлык TL;DR убран |
| Fact safety | 12/15 | 5 unverified чисел — есть в research-notes, нет в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, объём 9481, FAQ×6, живые CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «доставка авто из владивостока» в H1 / meta |
| C02 | ✓ | Lead — боль новичка + три цены/срока |
| C03 | ✓ | Читатель после растаможки во Владивостоке |
| C04 | ✓ | Автовоз / ж/д сетка·контейнер / перегон объяснены |
| O01 | ✓ | H2 закрывают pain_solution_map |
| O02 | ✓ | Логичный comparison → выбор → чек-лист → результат |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + table + blockquote workflows, mode B |
| R01 | ✓ | Insight + схемы + FAQ |
| R02 | ✓ | Сроки/вилки с пометкой «ориентир / не гарантия» |
| R03 | ✓ | Нет выдуманных % лотов; вилки как рыночные ориентиры |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «после таможни», три рабочих пути |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: catalog×2 + Telegram×1 (HTTP 200) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Ограничения сроков, сезон перегона, акт/фото |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate score ≥80:** ✓ (88)

## FIX cycle 1 — verified on rerun

1. CTA href из env CATALOG_URL×2 + TELEGRAM_URL×1 — literal `[REDACTED]` в HTML отсутствует; link-verify PASS.
2. utility article PASS — action_markers 10 (≥8); pain 8; outcome 6 (policy lists restored).
3. Ярлык `TL;DR / Быстрый инсайт` убран из insight.
4. char_count 9481 (в коридоре 8500–9500).

## Soft / non-blocking (optional)

- Ept02: 2–3 internal blog links с `anchor_variants` после публикации соседних URL.
- fact-check: дописать в fact-bank ориентиры 18–22 / 3–7 / 30–60 дней, 165–245 тыс., ~130 тыс. перегон.
- slop over-long / human-voice list-size warnings — не блокеры.
- Vary size of two 5-item lists when editorially possible.

## Gate checklist

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✓  
- research-notes-gate PASS → ✓  
- utility gate article PASS → ✓  
- human-voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — cover\|\|schema можно стартовать.
