# Article QA — B09

**topic_id:** B09  
**slug:** kia-seltos-iz-korei-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B09-kia-seltos-iz-korei-komplektatsii-lovushki-2026  
**date:** 2026-10-19  
**verdict:** FAIL  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date 2026-10-19; source table OK |
| fact-check | PASS | 5 stats; 1 verified / 4 soft-unverified vs fact-bank |
| link-verify | PASS | 3/3 OK (catalog, Telegram, 2GIS); IRI encode for Cyrillic 2GIS |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU 75.6 |
| cannibalization | PASS | 0 issues (3 meta loaded) |
| utility gate | BLOCK | action_markers **2 < 8**; pain=5 outcome=5 после restore policy |
| human-voice | PASS | warnings: Fact Check template + два ol по 5–7 пунктов |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1/meta; H2 how-to; CTA×3; мало blog internal |
| GEO / citability | 20/25 | Таблицы, чек-листы, FAQ×6; insight с запрещённым ярлыком TL;DR |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 12/15 | HV PASS, но TL;DR + шаблон Fact Check |
| Fact safety | 12/15 | Soft unverified counts; факты в research-notes |
| Contract HTML | 7/10 | Linter PASS; utility action-маркеры FAIL |
| **Итого** | **74/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «киа селтос из кореи» в meta/H1 |
| C02 | ✓ | Lead: депозит за имя trim, не за кнопки |
| C03 | ✓ | Читатель: заказ Seltos из Кореи до депозита |
| C04 | ✓ | Encar / trim / X·W / SP2 vs 2026 объяснены |
| O01 | ✓ | H2 = бриф → trim → ловушки → мотор → чек-лист → подбор |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + таблицы + mode B |
| R01 | ✓ | Схема первого дня + депозит OK/стоп |
| R02 | ✓ | 25,5% / 19% / 0,4% + размеры 2026 в тексте |
| R03 | ✓ | Нет цен лотов/% пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол trim≠опции + ловушки Encar (не Sportage/K5) |
| E02 | ✓ | «Делать / Не делать» в H2 (но не policy-маркеры) |
| E03 | ✓ | CTA: каталог + Telegram + 2GIS |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты X/W, коммерция, модельный год ≠ выпуск |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит за «красивое» имя Signature/Trendy без сверки опций, такси/лизинга и кузова; путаница SP2 vs 2026 |
| Где решение | H2 trim≠опции; H2 ловушки Encar (VIN/X·W/такси); H2 мотор/привод; H2 чек-лист «депозит OK / стоп» |
| Первый результат | Заполненный лист «депозит OK / стоп» до перевода денег |
| Термины «на пальцах» | Encar, trim, Performance Check, X/W, SP2, 2WD/4WD, модельный год vs дата выпуска |
| Beginner-fit | PASS — не для профи-разработчиков; есть безопасный первый шаг (бриф → must-have → лот) |

## Link verify

- total: 3, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6
- Flesch RU: 75.6
- verdict: warning (non-blocking)

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: **blocked until QA PASS**

## Blockers (обязательные gates)

1. **utility gate BLOCK** — `action_markers=2 < 8` (policy `recommendation_markers_ru`)
2. **score 74 < 80**

## FIX list → writer (не править longread в GEO QA)

1. **Action-маркеры (≥8):** сейчас в тексте в основном «Делать / Не делать», а utility считает `сделайте`, `не делайте`, `проверьте`, `используйте`, `избегайте`, `шаг `, `чеклист`, `ориентир`, `workflow` и т.п. Добавить/заменить формулировки так, чтобы `action_markers ≥ 8` (как в AS09: «избегайте», «проверьте», «Шаг N», «чеклист»).
2. **Insight-ярлык:** заменить `TL;DR / Быстрый инсайт` на человеческий ярлык без этих шаблонов (например «До депозита» / «Коротко»).
3. **(soft)** Разнообразить Fact Check wording (human-voice warning про repeated template).
4. **(soft)** Развести длины нумерованных списков (не два ol ровно ~5–7 пунктов одинаковым шаблоном).
5. **(optional Ept02)** После publish соседних постов — 1–2 internal blog links с `anchor_variants`.

После FIX writer → повтор GEO QA (cycle 1/2).

## Gate checklist

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✗  
- human-voice PASS ✓  
- link-verify PASS ✓  
- beginner-fit PASS ✓  

**Итог:** FAIL — вернуть writer по FIX-листу; cover\|\|schema не запускать.
