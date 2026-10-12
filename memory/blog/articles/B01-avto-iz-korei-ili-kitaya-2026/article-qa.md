# Article QA — B01

**topic_id:** B01  
**slug:** avto-iz-korei-ili-kitaya-2026  
**article_dir:** memory/blog/articles/B01-avto-iz-korei-ili-kitaya-2026  
**date:** 2026-10-12  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | `research_date` 2026-10-12; technical_topic=false; accessed_at=19; pain_solution_rows=4 |
| utility gate | PASS | action_markers 27; pain 6; outcome 8; FAQ×6; table×1; numbered 21 |
| human-voice gate | PASS | WARN: 3 списка ровно по 5 шагов; concrete/pain/outcome markers OK; reader_story overlap OK |
| fact-check | PASS | 11 stats; 1 verified (2026); 10 unverified (160/170/155 л.с., 2200 вон, 1996, 180 дней, 83 дней, №1713) — в research-notes |
| link-verify | PASS | 3/3 OK (internal rastamozhka + catalog + Telegram) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long (склейка таблицы/схемы); Flesch RU 65.9 |
| cannibalization | PASS | 0 issues (3 article meta в blog-dir) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «авто из кореи или китая» в title/H1; H2 action; CTA; 1 blog internal (не 2–3) |
| GEO / citability | 24/25 | TL;DR, таблица KR/CN, схема до депозита, FAQ×6, чеклист |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop hits |
| Fact safety | 13/15 | Цифры в research-notes; мало в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9.5k chars, FAQ, CTA≤3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из кореи или китая» в meta title / H1 |
| C02 | ✓ | Lead: боль новичка + страна как маршрут риска |
| C03 | ✓ | Читатель: заказ из Азии, выбор Корея vs Китай |
| C04 | ✓ | Encar, Carhistory, СБКТС, ЭПТС объяснены «на пальцах» |
| O01 | ✓ | H2 = action_outline / pain_solution_map research |
| O02 | ✓ | Фильтр → сервис → проверки → логистика → сметы → чеклист → дальше → FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + таблица + схемы, mode B comparison |
| R01 | ✓ | TL;DR, вердикт по задаче, схема до депозита |
| R02 | ✓ | 160 л.с., Carhistory 2200 вон, 180 дней, 83 дня — в research-notes |
| R03 | ✓ | Нет цен лотов/%; расчёт — в каталоге |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «страна = маршрут риска», не спор брендов |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты Carhistory, сроки Китая, порог 160 л.с. |
| Ept02 | ✗ | Только 1 blog internal (растаможка); нет 2–3 соседних постов |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Не понять, с какой страны начать; страх утильсбора, битой машины, срыва сроков |
| Где решение | H2 фильтр задачи + таблица KR/CN; проверки до депозита; две сметы; чек-лист |
| Первый результат | За вечер: один маршрут с 3 причинами + готовность запросить 2 сметы под ключ |
| Критерий успеха до FAQ | «Вслух называете страну и три причины… пустой пункт = депозит рано» |
| Термины «на пальцах» | Carhistory, СБКТС, ЭПТС, правило 180 дней, порог 160 л.с. |
| Beginner-fit | PASS — без тона «для профи»; стоп-правило до депозита; без «своих связей» |

## Link verify

- total: 3, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблицы/схемы)
- Flesch RU: 65.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FAIL list

- нет

## FIX cycle (QA)

- не требуется (все gates PASS с первого прогона)

## FIX (non-blocking / optional)

1. **Ept02:** добавить ещё 1–2 internal links на соседние посты блога с `anchor_variants` (сейчас только растаможка CN).
2. **fact-check soft:** 160 л.с. / 2200 вон / 1996 / 180 дней / 83 дня — дописать в fact-bank для verified.
3. **human-voice WARN:** варьировать длину нумерованных списков (сейчас 3× ровно 5 шагов).
4. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
