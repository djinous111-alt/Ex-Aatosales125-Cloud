# Article QA — B01

**topic_id:** B01  
**slug:** levyj-rul-iz-yaponii-2026-chek-list  
**article_dir:** memory/blog/articles/B01-levyj-rul-iz-yaponii-2026-chek-list  
**date:** 2026-10-22  
**verdict:** FAIL  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic official docs URL |
| fact-check | PASS | 5 extracted; verified 1 (2026); unverified: 2025, 2023, 30 минут, 243 129 (есть в research-notes / JAIA) |
| link-verify | FAIL | 1/3 fail: 2GIS URL с кириллицей в path → `'ascii' codec can't encode` |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схема); Flesch RU 62.8 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | BLOCK | action_markers 7&lt;8; pain_markers 0&lt;2; outcome_markers 0&lt;3 |
| human-voice | PASS | warning: 3× lists ровно по 5 шагов |

## Pain / solution / beginner-fit (editorial)

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Верит в массовый «левый руль из Японии» с JP-аукциона и готов слать депозит без фото салона / страны вывоза / VIN |
| Где решение | H2: задача по рулю → рынки → пакет до денег → Корея/Китай → чек-лист 10 пунктов → что дальше |
| Первый результат | До депозита: галочки по 10 пунктам + 3 строки в договоре; решение ставлю / меняю рынок / отказ |
| Термины «на пальцах» | LHD/RHD, японский аукцион vs шильдик, VIN/кузов, Encar, «под ключ», экспорт &gt;1,9 л |
| Beginner-fit | PASS — тон для новичка, есть безопасный первый шаг без команды разработчиков |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 actionable; CTA есть; нет 2–3 internal blog links |
| GEO / citability | 20/25 | TL;DR, схема, таблица рынков, FAQ×7, чеклист; citability ок |
| CORE-EEAT lite | 17/20 | см. таблицу ниже |
| Human voice | 14/15 | Script PASS; warning про одинаковые 5-step lists |
| Fact safety | 12/15 | JAIA 243 129 / август 2023 не в fact-bank (есть в research) |
| Contract HTML | 7/10 | Whitelist PASS, объём ~9437; **link-verify FAIL**; utility BLOCK |
| **Итого** | **74/100** | ниже порога 80; blockers ниже |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «левый руль из японии» в meta/H1 |
| C02 | ✓ | Lead: боль депозита + чек-лист до перевода |
| C03 | ✓ | Читатель-новичок, риск ложного LHD |
| C04 | ✓ | LHD/RHD, аукцион, VIN, Encar объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | TL;DR + критерий «готово» |
| R02 | ✓ | JAIA 243 129, август 2023, сроки ~месяц/два с пометкой ориентира |
| R03 | ✓ | Нет цен лотов/%; суммы «в каталоге» |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол брокер Владивосток / марка vs аукцион |
| E02 | ✓ | «Делать / Не делать» в H2 (но utility считает другие маркеры) |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 + 2GIS×1 |
| Exp01 | ✓ | Mode B, без fake first-person hero |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Красный флаг переделки руля; лимиты VIN |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 1
- fail: 2GIS reviews URL — non-ASCII path segment; see `link-verify.json`
- catalog + telegram: OK (redacted in report)

## AI-slop scan

- cliches: 0
- over-long: 6 (в т.ч. склейка таблицы/схемы)
- Flesch RU: 62.8

## Schema ready

BlogPosting: pending PASS | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | cover/schema: **не стартовать** до QA PASS

## Blockers (критичные)

1. **utility gate BLOCK** — `action_markers=7 < 8`; плюс `pain_markers=0`, `outcome_markers=0` из-за пустых списков в policy (см. incident).
2. **link-verify FAIL** — URL 2GIS с кириллицей в path ломает urllib ascii encode.
3. **score 74 &lt; 80** — cover\|\|schema запрещены.

## FIX для writer (цикл 1) — не править GEO QA самому

1. **Action markers ≥8:** сейчас считаются вхождения из `recommendation_markers_ru`. Есть `шаг `×5 + `проверьте` + `ориентир` = 7. Формы «Делать / Не делать» **не** входят в список. Добавить ≥1 маркер дословно: `сделайте` / `не делайте` / `избегайте` / `используйте` / `чеклист` / `добавьте` (без ломки смысла).
2. **2GIS href:** полностью percent-encode кириллицу в path (пример сегмента search: `%D0%B0%D0%B2%D1%82%D0%BE%20%D1%81%D0%B5%D0%B9%D0%BB%D1%81%20%D0%B2%D0%BB%D0%B0%D0%B4%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%BA`), перезапустить link-verify.
3. **Pain/outcome для utility (после sync policy или сразу):** явно добавить слова из будущего/ожидаемого списка (как в human-voice): боль/проблема/ошибка + результат/получите/соберите — не полагаться на ложное «боль» внутри «больше».
4. **Human-voice soft:** развести размер списков (сейчас 3× ровно 5 пунктов) — не blocker.

## FIX (non-blocking / fixer)

1. **INC utility-policy:** `editorial-policy.json` не содержит `pain_markers_ru` / `outcome_markers_ru`, а `utility_gate` требует min 2/3 → любой article BLOCK.
2. **link_verify IRI:** скрипт должен quote non-ASCII перед request.
3. **fact-bank soft:** JAIA 243 129 (2025), экспортные ограничения с 09.08.2023.
4. **Ept02:** 2–3 internal blog links после Indexer / live URLs.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- research notes gate PASS → ✓  
- utility gate PASS → ✗  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FAIL — **не** READY FOR COVER\|\|SCHEMA. Вернуть writer на FIX; параллельно Fixer — policy markers + link_verify IRI.
