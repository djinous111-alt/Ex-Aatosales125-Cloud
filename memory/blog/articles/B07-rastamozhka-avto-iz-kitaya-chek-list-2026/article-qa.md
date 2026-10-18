# Article QA — B07

**topic_id:** B07  
**slug:** rastamozhka-avto-iz-kitaya-chek-list-2026  
**article_dir:** memory/blog/articles/B07-rastamozhka-avto-iz-kitaya-chek-list-2026  
**date:** 2026-10-18  
**verdict:** PASS  
**score:** 87

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Путает СВХ/ПТД/ЕЛС/СБКТС/ЭПТС, думает «порт = почти дома», боится ДФО и платного простоя |
| Где боль в lead | Абзац про Игоря: депозит, трекер «порт», пустой ЕЛС, «страх сломать процесс» |
| Где решения (H2) | Папка+ЕЛС до порта → станции Владивостока → расчёт без готовых сумм → типичные задержки → критерий готовности → «сегодня без юристов» |
| Первый результат до FAQ | Личный чек-лист на одну страницу + критерий: выпуск + СБКТС + ЭПТС «действующий» |
| Термины «на пальцах» | СВХ, ПТД, ЕЛС, СБКТС, ЭПТС объяснены в 3-м абзаце |

**beginner-fit:** PASS (не проф/юрист-тон; есть первый безопасный шаг без «команды разработчиков»)

## Scripts

| Script | Verdict | Path / notes |
|--------|---------|--------------|
| research-notes gate | PASS | `research-notes-gate.json` (re-check; warn: technical_topic FP) |
| fact-check | PASS | `fact-check-report.json` — 4 stats; verified 2; unverified: «5 минут» (rhetoric SERP), «15 дней» (ориентир) |
| link-verify | PASS | `link-verify.json` — 2/2 OK (каталог + Telegram) |
| html-linter | PASS | `html-linter-report.json` — 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | `slop-detector-report.json` — 0 клише; 7 over-long (таблица/схемы); Flesch RU 55.2 |
| cannibalization | PASS | `cannibalization-report.json` — 0 issues (`--blog-dir`) |
| utility gate | PASS | `utility-gate-report.json` — action 16 / pain 9 / outcome 12; FAQ×6; table×1 |
| human voice | PASS | `human-voice-report.json` — warn: 2× exactly-5-step lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2/H3; CTA×3; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт-блок, схема, таблица станций, FAQ×6, чек-листы |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | PASS; warn про два списка ровно из 5 пунктов |
| Fact safety | 13/15 | 2 unverified vs fact-bank (риторика/ориентир, не цены) |
| Contract HTML | 10/10 | Whitelist PASS, ~9223 знаков, FAQ, CTA, Fact Check Box = registry |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как растаможить авто из китая» в title / H1 |
| C02 | ✓ | Lead + «Коротко по делу» — прямой ответ: порт ≠ финиш |
| C03 | ✓ | Читатель: новичок с авто из Китая через Владивосток |
| C04 | ✓ | СВХ/ПТД/ЕЛС/СБКТС/ЭПТС на пальцах |
| O01 | ✓ | H2 = этапы research outline |
| O02 | ✓ | Логичный порядок до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица, mode B |
| R01 | ✓ | Инсайт, схема станций, FAQ |
| R02 | ✓ | 01.04.2026 ЕЛС, ориентиры сроков из research |
| R03 | ✓ | Нет готовых сумм пошлин/утиля |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «чек-лист / рюкзак перед походом» |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person solo |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: ориентиры сроков, развилка ДФО, без гарантии «под ключ» |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 7 (часть — склейка таблицы/схемы парсером)
- Flesch RU: 55.2 (Standard)

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чек-листы) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не потребовался (все blocking gates PASS с первого прогона)

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal links с `anchor_variants`.
2. **human-voice warn:** разнести размеры списков (два ol ровно по 5 пунктов; в тексте уже есть ol×6 — ок, но warn остаётся).
3. **fact-check soft:** «15 дней» / риторика «5 минут» — при желании в fact-bank; не блокер.
4. **slop over-long:** таблица/схема; правки не критичны.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  
- cannibalization PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
