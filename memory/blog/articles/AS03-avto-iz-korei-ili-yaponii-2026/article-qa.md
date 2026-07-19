# Article QA — AS03

**topic_id:** AS03  
**slug:** avto-iz-korei-ili-yaponii-2026  
**article_dir:** memory/blog/articles/AS03-avto-iz-korei-ili-yaponii-2026  
**date:** 2026-07-19  
**verdict:** FAIL  
**score:** 84

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-07-19 |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified 2025 / 160 / 150 — в research-notes |
| link-verify | PASS | 2/2 OK (catalog + Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long (склейка таблицы); Flesch RU 61.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | **BLOCK** | action_markers 6&lt;8; pain/outcome 0 (см. script incident) |
| human-voice-gate | **PASS** | `human-voice-report.json` status PASS |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 действие; CTA OK; нет 2–3 blog internal |
| GEO / citability | 23/25 | TL;DR, схема →, таблица KR vs JP, FAQ×6, чеклист 9 |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice PASS; slop 0 |
| Fact safety | 12/15 | 160/150/2025 не в fact-bank (есть в research) |
| Contract HTML | 10/10 | Whitelist PASS, ~8692, FAQ, CTA≤3, без форм |
| Utility gate | 0/− | **BLOCK** — итог FAIL |
| **Итого** | **84/100** | score≥80, но utility BLOCK → FAIL |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать авто из кореи или японии» в meta/H1 |
| C02 | ✓ | Lead: боль депозита + ответ (фильтры → две сметы) |
| C03 | ✓ | Новичок: Алексей / Sportage / депозит до проверки |
| C04 | ✓ | LHD/RHD, «под ключ», утиль/мощность ~160 объяснены |
| O01 | ✓ | H2 = профиль → мощность → сравнение → сметы → проверка → чеклист |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol×2 + table + mode B |
| R01 | ✓ | TL;DR, схема до депозита, FAQ |
| R02 | ✓ | Факты из research-notes; порог ~160 с пометкой ориентира |
| R03 | ✓ | Нет готовых сумм пошлин/калькулятора |
| R04 | ✓ | FAQ — ответ-действие в 1-м предложении |
| E01 | ✓ | Угол только KR vs JP + до депозита через Владивосток |
| E02 | ✓ | «Делать / Не делать» в H2 (но маркеры utility ждут «сделайте/не делайте») |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: цифры плавают, правый руль/перепродажа, порог льготы |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Путает цену лота с «под ключ», выбирает страну наугад, риск депозита до сметы |
| Где решение | H2: мини-профиль → мощность → таблица KR/JP → две сметы → проверка → чеклист |
| Первый результат | Заполненный чек-лист + запрос двух сопоставимых расчётов до депозита |
| Термины «на пальцах» | LHD/RHD, «под ключ», аукционный лист, льготный порог ~160 л.с. |
| Beginner-fit | PASS (нет тона «для профи»; первый шаг без «команды разработчиков») |

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблицы + длинные фразы)
- Flesch RU: 61.6

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклист) | Review: no | cover/schema: **не стартовать** до utility PASS

## Blockers

1. **UTILITY ARTICLE BLOCKER** — `action_markers=6 < 8` (реальный контент-FIX → writer).
2. **UTILITY pain/outcome 0** — в `editorial-policy.json` нет `pain_markers_ru` / `outcome_markers_ru`; на этой ветке `excalibur_blog_utility_gate.py` без `DEFAULT_*` / `resolve_marker_lists` (есть в `0ebb811` на другой ветке). При defaults статья даёт pain≈5, outcome≈8 (как human-voice PASS). → Fixer, не writer.

## FIX cycle (QA) → Writer (обязательно)

1. Довести **recommendation/action markers ≥ 8** по списку `recommendation_markers_ru` в `memory/brief/editorial-policy.json`:
   - заменить «Делать:» / «Не делать:» на **«Сделайте:»** / **«Не делайте:»** (или добавить эти формы рядом);
   - либо добавить «избегайте», «Шаг N», «чеклист» (без дефиса), «используйте» — минимум +2 вхождения.
2. После правки: `python3 scripts/excalibur_blog_utility_gate.py --article-dir memory/blog/articles/AS03-avto-iz-korei-ili-yaponii-2026 --output utility-gate-report.json` → ожидается PASS **после** фикса script/policy (см. incident).
3. Не менять факты/цифры пошлин; CTA href без литерала `[REDACTED]`.

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links на AS01/AS08/AS09 с `anchor_variants` (после Indexer или writer).
2. **fact-check soft:** 160 л.с. / декабрь 2025 → fact-bank.
3. **slop over-long:** артефакт таблицы; не критично.

## Gate

- score ≥ 80 → **84** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- utility gate PASS ✗ → **FAIL**  

**Итог:** FAIL — вернуть writer (FIX action markers). Cover \|\| schema **не** запускать. Fixer: restore utility defaults + policy markers.
