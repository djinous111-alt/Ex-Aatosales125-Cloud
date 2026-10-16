# Article QA — B01

**topic_id:** B01  
**slug:** kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026  
**article_dir:** memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026  
**date:** 2026-10-16  
**verdict:** PASS  
**score:** 91  
**fix_cycle:** 1 (повтор после Fixer + Writer FIX)  
**cover_schema:** разрешено (директор: cover || schema)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | recheck; warn: no official docs URL |
| fact-check | PASS | 3/3 verified |
| link-verify | pass | 2 unique URLs, failed_count=0, HTTP 200 |
| html-linter | PASS | 0 errors; TOC/`pre`/`code` нет |
| slop-detector | PASS | 0 клише; 4 over-long (склейка table/схемы); Flesch RU 70.0 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action 37; pain 2; outcome 11 |
| human voice gate | PASS | outcome 6 маркеров; warnings 0; exactly_five_lists=1 (не блокер) |

## Pain / solution / beginner-fit

| Вопрос | Статус | Где |
|--------|--------|-----|
| Боль новичка в lead | PASS | предоплата за «чистую» машину без понимания баз до ввоза |
| Решение в H2 | PASS | VIN → отчёт КНР → ГИБДД/ФНП → флаги → чеклист 10 → «Что дальше» |
| Первый результат до FAQ | PASS | пакет: VIN + отчёт + скрины + стоп-список; «плачу / не плачу» за 20–40 мин |
| Термины «на пальцах» | PASS | VIN/WMI, I/O/Q, пустой ГИБДД = норма, два слоя Китай+РФ |
| Beginner-fit blocker | нет | тон для покупателя под заказ, не для профи/разработчиков |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в H1/meta; CTA валидны; нет 2–3 blog internal |
| GEO / citability | 23/25 | insight без TL;DR, схема, таблица, FAQ×6, чеклист 10 |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | human-voice PASS; 0 AI-openings |
| Fact safety | 15/15 | fact-check 3/3 |
| Contract HTML | 10/10 | whitelist PASS; CTA OK; mode B |
| **Итого** | **91/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | primary в H1/meta |
| C02 | ✓ | lead = боль + ответ |
| C03 | ✓ | читатель: заказ авто из КНР, риск депозита |
| C04 | ✓ | VIN/отчёт/ГИБДД/ФНП объяснены |
| O01 | ✓ | H2 = action outline |
| O02 | ✓ | логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + ul + table + checklist, mode B |
| R01 | ✓ | insight + схема + FAQ |
| R02 | ✓ | 73 тыс / окт 2026 / Автотека World — в research |
| R03 | ✓ | нет ложных цен лотов |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «сначала VIN и отчёт» |
| E02 | ✓ | сделайте / не делайте в теле |
| E03 | ✓ | CTA: каталог×2 + Telegram×1, link-verify pass |
| Exp01 | ✓ | mode B |
| Exp02 | ✓ | тон Авто-Сейлс |
| Exp03 | ✓ | slop 0 |
| Ept01 | ✓ | лимиты баз / пустой ГИБДД |
| Ept02 | ✗ | нет internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit / utility narrative

- **Боль:** депозит за «чистую» машину из Китая без понимания, какие базы видят историю до ввоза.
- **Решение:** VIN с фото → китайский/зарубежный отчёт → ГИБДД+ФНП → красные флаги → чеклист 10 → решение плачу/не плачу.
- **Первый результат:** пакет доказательств до перевода денег (20–40 минут).
- **Сложные термины:** VIN/WMI, пустой ГИБДД до учёта в РФ, два слоя отчётов.

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal blog links с `anchor_variants`.
2. **slop over-long:** артефакт парсера на table/схеме; правки не критичны.
3. **research-notes warn:** нет official docs URL — ожидаемо для niche VIN/авто, не блокер статьи.

## Reports (paths)

- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/research-notes-gate.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/fact-check-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/link-verify.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/html-linter-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/slop-detector-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/cannibalization-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/utility-gate-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/human-voice-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/article-qa.md`

## Gate

- score ≥ 80 → **91** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✓  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✓  
- human voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — можно cover || schema.
