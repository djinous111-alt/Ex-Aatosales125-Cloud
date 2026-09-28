# Article QA — AS02

**topic_id:** AS02  
**slug:** encar-na-russkom-kak-chitat  
**article_dir:** memory/blog/articles/AS02-encar-na-russkom-kak-chitat  
**date:** 2026-09-28  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: нет official docs URL (не блокер; тема marketplace how-to) |
| fact-check | PASS | 8 stats; 1 verified (2026); 7 unverified — в research-notes (120 дней, X/W, 1890→18.9M, 2000 км) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (склейка table/checklist парсером); Flesch RU 74.8 |
| cannibalization | WARNING | secondary AS02 `trust encar` = primary AS09 (100%); см. FIX optional |
| utility gate | PASS | action_markers 22; pain 24; outcome 11; FAQ×6; table×1; numbered 11 |
| human-voice gate | PASS | h2=8 actionable; concrete/pain/outcome markers; overlap research story/pain/outcome |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary «encar на русском» в title/H1; H2 how-to; CTA каталог×2+TG×1; нет 2–3 blog internal |
| GEO / citability | 24/25 | Insight-блок, схема→, таблица слоёв, FAQ×6, чеклист 7 |
| CORE-EEAT lite | 14/15 | 19/20 (см. таблицу) |
| Human voice | 15/15 | 0 AI-slop; живой Tucson/W на лонжероне; ритм OK |
| Fact safety | 13/15 | Цифры из research; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8687 chars meta / ~10k HTML, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «encar на русском» в meta title / H1 |
| C02 | ✓ | Lead: боль + ритуал «на осмотр / мимо» до депозита |
| C03 | ✓ | Читатель: новичок, корейское авто, страх битой/скрутки |
| C04 | ✓ | Performance Check / X/W/C / Carhistory / VIN объяснены |
| O01 | ✓ | H2 = action_outline research (клон→5 полей→лист→пробег→Carhistory→чеклист→CTA) |
| O02 | ✓ | Логичный outline mode B |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + table + workflow → + чеклист |
| R01 | ✓ | Insight «Коротко по делу», схема кузова, таблица слоёв |
| R02 | ✓ | 120 дней, X/W из Encar Media, манвон-пример — в research-notes |
| R03 | ✓ | Нет сумм пошлин/утиля; цены лотов не выдаются за «под ключ» |
| R04 | ✓ | FAQ-ответы с первого предложения |
| E01 | ✓ | Угол «ритуал одной карточки» vs клоны «на русском» |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты листа 120 дней, Carhistory vs наличные, клоны |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

| Crit | Status | Evidence |
|------|--------|----------|
| Боль новичка | PASS | Lead: Encar на корейском → страх битой/скрутки; W на лонжероне + просроченный лист |
| Решение в H2 | PASS | encar.com не клон → 5 полей → X/W/120 → пробег → Carhistory → чеклист 7 |
| Первый результат до FAQ | PASS | Вердикт «на осмотр / мимо» + workflow encar.com→…→чеклист |
| Термины «на пальцах» | PASS | Performance Check, X/W/C, лонжерон, манвон, Carhistory=страховые кейсы |
| Первый безопасный шаг | PASS | Один лот, ссылка с encar.com, без депозита по скрину клона |
| Тон не «для профи» | PASS | «как инструкция к стиральной машине»; human-voice PASS |

## Pain → solution map (QA)

- **Боль:** не понять корейский отчёт / купить битое → **Lead + H2 Performance Check**
- **Боль:** клон «Encar на русском» → **H2 официальный encar.com**
- **Боль:** скрутка пробега → **H2 сверка шапка vs лист**
- **Боль:** ложный «зелёный» Carhistory → **H2 + таблица слоёв**
- **Результат:** чеклист 7 пунктов → осмотр или мимо до депозита

## Link verify

- total: 2 unique OK (каталог + Telegram; в HTML каталог×2)
- failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт table/checklist/workflow)
- Flesch RU: 74.8

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/ol) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Cannibalization WARN:** убрать secondary `trust encar` из `article.meta.json` AS02 (primary принадлежит AS09) — или переименовать в long-tail вроде «trust encar vs performance check».
2. **Ept02:** после publish AS02 — 2–3 internal links на AS08/AS09 с `anchor_variants`.
3. **fact-check soft:** дописать в fact-bank: срок листа 120 дней, X=обмен / W=сварка (Encar Media), ориентир гарантии 1 мес / 2000 км.
4. **slop over-long:** артефакт парсера table/checklist; правки не критичны.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
