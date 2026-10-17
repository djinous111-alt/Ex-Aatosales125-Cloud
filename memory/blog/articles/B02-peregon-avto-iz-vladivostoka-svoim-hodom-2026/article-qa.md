# Article QA — B02

**topic_id:** B02  
**slug:** peregon-avto-iz-vladivostoka-svoim-hodom-2026  
**article_dir:** memory/blog/articles/B02-peregon-avto-iz-vladivostoka-svoim-hodom-2026  
**date:** 2026-10-17  
**verdict:** FIX  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | reconfirm 2026-10-17; source_table 21; pain_solution 7 |
| fact-check | PASS | 12 stats; verified 4 / unverified 8 (кейсы ₽, 01.03.2025, 20–30 дней — в research-notes, не в fact-bank) |
| link-verify | FAIL | 1/4 OK (`elpts.ru`); 3 fail: `$CATALOG_URL`, `$TELEGRAM_URL`, `$MAX_URL` → 404 как internal_relative |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/списки); Flesch RU 65.2 |
| cannibalization | PASS | 0 issues (3 articles loaded) |
| utility gate | BLOCK | pain_markers=0 < 2, outcome_markers=0 < 3 — **false BLOCK**: в `memory/brief/editorial-policy.json` нет `pain_markers_ru`/`outcome_markers_ru`, а скрипт всё равно требует min 2/3 |
| human-voice-gate | PASS | warnings: 4× exactly-5-step lists; reader_story/pain/outcome overlap OK |

## Beginner-fit / pain → solution → result

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Выдали авто во Владивостоке → едут без ОСАГО/пакета; ловушка «номера и страховку потом» (lead + история Игоря) |
| Где решение | H2: go/no-go таблица → осмотр на стоянке → ЭПТС/ОСАГО/10 суток → первый день → чек-лист 12 пунктов |
| Первый результат | До FAQ: «Что сделать сегодня» (5 шагов) + критерий результата в H2 чек-листа (пакет в бардачке / go или автовоз) |
| Термины «на пальцах» | ЭПТС, ТПО, СВХ, 10 суток, ОСАГО на VIN, транзиты vs учёт — объяснены при первом появлении |
| beginner-fit | PASS (не профиль для разработчиков; есть безопасный первый шаг) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; H2 actionable; CTA есть, но href-плейсхолдеры ломают link-verify (−4) |
| GEO / citability | 22/25 | TL;DR, таблица, схема первого дня, FAQ×7, чеклисты; ярлык «TL;DR / Быстрый инсайт» — soft |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | human-voice PASS; 4 одинаковых 5-step списка |
| Fact safety | 12/15 | Ориентиры ₽ помечены как кейсы; 8 unverified vs fact-bank |
| Contract HTML | 8/10 | Whitelist PASS; FAQ «Сколько roughly…» — англ. в H3; CTA `$…_URL` не publish-ready |
| Utility / gates | 0/10 | utility BLOCK + link-verify FAIL → hard blockers |
| **Итого** | **74/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «перегон … своим ходом» в H1 / meta |
| C02 | ✓ | Lead — сценарий Игоря + ловушка, без «в этой статье» |
| C03 | ✓ | Покупатель после выдачи во Владивостоке |
| C04 | ✓ | ЭПТС / ТПО / СВХ / 10 суток объяснены |
| O01 | ✓ | H2 = чек-лист до выезда (research outline) |
| O02 | ✓ | Логичный outline go/no-go → осмотр → документы → день 1 → 12 пунктов → сегодня |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + blockquote-схемы, mode B |
| R01 | ✓ | TL;DR, go/no-go, схема первого дня, критерий результата |
| R02 | ✓ | 10 суток / ОСАГО с 01.03.2025 / ориентиры ₽ — в research-notes |
| R03 | ✓ | Цены как вилки кейсов, не прайс компании |
| R04 | ✓ | FAQ: ответ в 1-м предложении |
| E01 | ✓ | Угол «до выезда своим ходом», не клон ж/д+автовоз |
| E02 | ✓ | «Делать / Не делать» в каждой H2 |
| E03 | ✓ | CTA каталог/Telegram/MAX уместны по смыслу |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Зима / дальняк / нет напарника → лучше доставка |
| Ept02 | ✗ | Нет 2–3 внутренних blog-ссылок; CTA — `$CATALOG_URL` / `$TELEGRAM_URL` / `$MAX_URL` |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 4, failed: 3
- OK: `https://elpts.ru/`
- FAIL: `$CATALOG_URL`, `$TELEGRAM_URL`, `$MAX_URL` (literal placeholders)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (таблица + списки)
- Flesch RU: 65.2

## Schema ready

BlogPosting: pending (после PASS) | FAQPage: yes (7) | HowTo: yes (чеклисты) | cover/schema: **не запускать** до QA PASS

## Blockers (FAIL list)

1. **link-verify FAIL** — заменить `$CATALOG_URL` / `$TELEGRAM_URL` / `$MAX_URL` на реальные публичные URL каталога / Telegram / MAX (как в AS09), без секретов в HTML.
2. **utility gate BLOCK** — false positive: пустые `pain_markers_ru`/`outcome_markers_ru` в policy + default min 2/3 в `excalibur_blog_utility_gate.py`. Нужен Fixer (скрипт/policy), не рерайт «для галочки». После фикса — перегон utility gate.

## Soft FIX (writer, non-blocking after hard FIX)

1. Убрать ярлык `TL;DR / Быстрый инсайт:` из открытия insight-blockquote (оставить суть).
2. H3 FAQ: «Сколько roughly…» → русский «примерно» / «ориентировочно».
3. Разнообразить длину списков (human-voice: 4× ровно 5 шагов).
4. После публикации соседних постов — 2–3 internal blog links (Ept02).

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✗ (script/policy false BLOCK)  
- human voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FIX — cover \|\| schema **не** запускать. Директор → Writer (CTA URLs + soft) и Fixer (utility gate policy/script).
