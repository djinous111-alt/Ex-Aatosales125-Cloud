# Article QA — B01

**topic_id:** B01  
**slug:** kak-zakazat-avto-iz-korei-pod-klyuch-2026  
**article_dir:** memory/blog/articles/B01-kak-zakazat-avto-iz-korei-pod-klyuch-2026  
**date:** 2026-10-03  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-03; warn: no official docs URL |
| fact-check | PASS | 13 stats; 2 verified; 11 unverified vs fact-bank — есть в research-notes (2.0 л / 160 л.с. / 30–55 дней / Carhistory 1996) |
| link-verify | PASS | 3/3 OK (каталог, Carhistory, Telegram); `--site-base` = PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (склейка таблицы/схемы парсером); Flesch RU 70.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 10; FAQ×6; table×1; pain/outcome markers OK |
| human-voice gate | PASS | human-voice-report.json status PASS |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «авто из кореи под ключ» в title/H1; H2 how-to; CTA×3; нет blog internal |
| GEO / citability | 23/25 | Инсайт-блок, таблица сметы, схема до платежа, FAQ×6, чеклист 12 |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop; reader_story Игорь/Tucson; concrete markers OK |
| Fact safety | 12/15 | Даты/сроки в research; не все в fact-bank; нет цен лотов/% |
| Contract HTML | 10/10 | Whitelist PASS, ~9456 симв., FAQ, CTA≤3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из кореи под ключ» в meta title / H1 |
| C02 | ✓ | Lead — боль + ответ без «в этой статье» |
| C03 | ✓ | Читатель: новичок, заказ Корея под ключ |
| C04 | ✓ | Encar / Carhistory / СБКТС / ЭПТС / «под ключ» объяснены |
| O01 | ✓ | H2 = action_outline research (смета → фильтры → проверка → договор → путь → чеклист) |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + схема, mode B |
| R01 | ✓ | Инсайт-блок, схема до платежа, FAQ-блоки |
| R02 | ✓ | 2.0 л экспорт / 160 л.с. / 30–55 дней / Carhistory с 1996 — в research-notes |
| R03 | ✓ | Нет цен лотов и неподтверждённых % |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Полный заказ Корея Encar→ЭПТС; не клон AS01 / Japan-China turnkey |
| E02 | ✓ | «Делать / Не делать» в каждой H2-секции |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я лично пригнал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс + история Игоря |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски депозита, мощность/утиль, flood, сроки 30–55 |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (карточка `internal_links: /`; только каталог + Telegram + Carhistory) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Принять цену Encar за итог «под ключ»; депозит «в никуда»; непонятный финиш ЭПТС |
| Где решение | H2 смета/фильтры/проверка/договор/Пусан→Вл→ЭПТС + чеклист 12 пунктов |
| Первый результат | Заполненный чек-лист до первого платежа; критерий — «да» по пунктам + понимание финиша (ЭПТС на своё имя) |
| Термины «на пальцах» | Encar = витрина не аукцион; Carhistory = страховая картотека; СБКТС/ЭПТС простыми словами |
| Beginner-fit | PASS — первый безопасный шаг без «команды разработчиков»; тон для новичка |

## Link verify

- total: 3, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/схемы + 1–2 длинных абзаца)
- Flesch RU: 70.6

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (writer)

- нет (текстовый FAIL отсутствует)

## FIX (non-blocking / optional)

1. **Ept02:** после появления URL AS01/AS09 на live — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** даты 01.12.2025 / февраль 2024 / Carhistory 1996 / рамки 30–55 дней — дописать в fact-bank.
3. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-report.json PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
