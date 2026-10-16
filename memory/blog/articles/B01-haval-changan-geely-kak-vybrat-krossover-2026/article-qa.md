# Article QA — B01

**topic_id:** B01  
**slug:** haval-changan-geely-kak-vybrat-krossover-2026  
**article_dir:** memory/blog/articles/B01-haval-changan-geely-kak-vybrat-krossover-2026  
**date:** 2026-10-16  
**verdict:** PASS  
**score:** 86

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-16; source_table_rows=26 |
| utility gate | PASS | pain=4 (≥2), outcome=9 (≥3), action_markers=35; ol=10, H2=6, FAQ h3=6, table×1 |
| human-voice gate | PASS | pain/outcome hits OK; reader_story/pain/outcome overlap; Fact Check author OK |
| html-linter | PASS | 0 errors; whitelist OK; TOC в теле нет |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из `PUBLIC_SITE_URL` |
| fact-check | PASS | 3 stats; verified 1 (2026); unverified 2 (181 л.с., «от 2 379 900 ₽») — ориентиры из research/офиц. сайтов |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/workflow/Fact Check); Flesch RU 73.5 |
| cannibalization | PASS | 0 issues (3 article metas) |

## Beginner-fit

**PASS.** Статья для новичка-покупателя: DCT/4WD/UNI-S объяснены на пальцах; первый шаг — сценарий недели на бумаге до депозита; нет жаргона API/RAG/MCP.

## Pain / solution / result

| Критерий | Где в статье |
|----------|----------------|
| Боль новичка | Lead: Аня почти внесла депозит «по ролику»; сервис/4WD/робот не совпали |
| Решение в H2 | Сценарий недели → сравнение брендов → модели-якоря → 7 пунктов до депозита → чеклист |
| Первый результат до FAQ | 1–2 кандидата на бумаге, депозит не внесён; workflow blockquote + ol×10 |
| Термины «на пальцах» | DCT = робот в пробке; CS55 Plus = UNI-S (переименование); 4WD письменно |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary «хавал джили» в meta_ab; actionable H2; CTA×3; нет 2–3 internal blog links |
| GEO / citability | 23/25 | Инсайт-блок, таблица сценариев, FAQ×6, чеклисты, workflow |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; slop=0 |
| Fact safety | 12/15 | АВТОСТАТ/Newsinfo + офиц. сайты в Fact Check; 2 числа вне fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; ~9076 знаков; FAQ; CTA; без форм/`<pre>` |
| **Итого** | **86/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в title_seo / lead |
| C02 | ✓ | Lead отвечает: сценарий → бренд → чеклист до депозита |
| C03 | ✓ | Читатель: новичок, выбор кроссовера из Китая |
| C04 | ✓ | Jolion / Coolray / UNI-S, DCT, 4WD объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный порядок до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + blockquotes, mode B |
| R01 | ✓ | Коротко-блок + workflow + FAQ |
| R02 | ✓ | АВТОСТАТ сервис 83,9/78,8/77,3; цены как ориентир |
| R03 | ✓ | Нет калькулятора пошлин; цены — ориентир, не прайс статьи |
| R04 | ✓ | FAQ ответ с первого предложения |
| E01 | ✓ | Угол «не по ролику / до депозита» |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: сервис, 4WD в оффере, DCT в пробке |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/workflow)
- Flesch RU: 73.5

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (после restore `pain_markers_ru` / `outcome_markers_ru` в editorial-policy)

## FIX cycle (QA)

1. Utility gate сначала BLOCK: `pain_markers=0`, `outcome_markers=0` при **пустых списках** в `memory/brief/editorial-policy.json` (регрессия rebrand; та же ошибка валила и AS09). Не text-FAIL writer.
2. GEO QA восстановил списки + `min_pain_markers`/`min_outcome_markers` и fail-fast в `excalibur_blog_utility_gate.py` (как в fix-коммите на соседней ветке). Повтор utility: **PASS** (pain=4, outcome=9).
3. Incident: `memory/pipeline-fix-queue.md#INC-20261016-1332-geo-qa-utility-pain-outcome-markers-wiped`

## FIX (non-blocking / optional)

1. **Ept02:** после Indexer — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 181 л.с. / «от 2 379 900 ₽» — дописать в fact-bank при желании.
3. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
