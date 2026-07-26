# Article QA — AS10

**topic_id:** AS10  
**slug:** peregon-avto-iz-vladivostoka-2026  
**article_dir:** memory/blog/articles/AS10-peregon-avto-iz-vladivostoka-2026  
**date:** 2026-07-26  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=today; source_table OK |
| fact-check | PASS | 9 stats; 3 verified / 6 unverified vs fact-bank (есть в research-notes: 9128 км, ОСАГО 5–20, ~1450 км Ерофей→Улан-Удэ) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 7 over-long (склейка таблицы/схем парсером); Flesch RU 56.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 13; pain 3; outcome 13; ol×24 items; FAQ×7; table×1 |
| human-voice gate | PASS | pain/outcome OK; soft warn: regex «exactly-5» ловит и 6-item ol |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Путает перегон и автовоз; риск предоплаты водителю из чата без акта/фото |
| Где решение | H2: форматы → пригодность авто → документы/ОСАГО → договор+акт+фото → маршрут/топливо → приёмка |
| Первый результат | До FAQ: выбран формат + чек-лист «до старта» + пакет до ключей |
| Термины «на пальцах» | свой ход / перегонщик / автовоз; ЭПТС; ТПО/ПТД; ДКП; транзит ОСАГО 5–20 дней |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; CTA×3; нет 2–3 blog internal |
| GEO / citability | 24/25 | Инсайт, таблица сравнения, схема передачи, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop hits; PASS gate |
| Fact safety | 13/15 | Факты в research-notes; часть не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9231 символов, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «перегон авто из владивостока» в title / H1 |
| C02 | ✓ | Lead — прямая развилка форматов + типичная ошибка предоплаты |
| C03 | ✓ | Читатель после выдачи с СВХ во Владивостоке |
| C04 | ✓ | ЭПТС / ТПО / ПТД / ДКП / транзит ОСАГО объяснены |
| O01 | ✓ | H2 = writer outline (форматы → авто → документы → договор → маршрут → приёмка → результат) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + схемы, mode B |
| R01 | ✓ | Инсайт, вердикт, схема передачи, FAQ |
| R02 | ✓ | ~1450 км Ерофей→Улан-Удэ + ОСАГО 5–20 в research-notes |
| R03 | ✓ | Бюджеты как ориентиры, не оферта |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол свой ход / перегонщик (не дубль автовоза) |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Зима/кейс-кар/топливный разрыв/риск без акта |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 7 (артефакт таблицы/схемы)
- Flesch RU: 56.5

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. **Utility BLOCK** — `pain_markers_ru` / `outcome_markers_ru` отсутствовали в `memory/brief/editorial-policy.json`, а скрипт дефолтил `min_pain=2` / `min_outcome=3` при пустых списках → любой article BLOCK.  
   Fix: маркеры + min_* в policy; utility_gate enforce только если списки не пусты.
2. **link-verify FAIL** — в `article.html` литералы `href="[REDACTED]"` (writer placeholder).  
   Fix: восстановлены CTA каталог + Telegram по conversion-map / AS09.
3. Инсайт-лейбл `TL;DR / Быстрый инсайт` → `Коротко по делу`; усилен блок результата до FAQ; списки ol разведены по длине.

## FIX (non-blocking / optional)

1. **Ept02:** после publish URL соседних AS — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** дописать ориентиры км/ОСАГО/топливный участок в fact-bank.
3. **slop over-long / human-voice warn:** артефакты парсера таблицы и regex «exactly-5» на ≥5 li.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
