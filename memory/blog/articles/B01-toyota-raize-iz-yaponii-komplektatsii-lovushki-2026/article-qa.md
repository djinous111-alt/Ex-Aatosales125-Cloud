# Article QA — B01

**topic_id:** B01  
**slug:** toyota-raize-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-raize-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-24  
**verdict:** FAIL  
**score:** 72 (veto: hard blockers)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical false-positive on «raize» (см. INC research) |
| fact-check | PASS | 17 stats; 1 verified in fact-bank (2026); остальные в research-notes |
| link-verify | **FAIL** | 3/3 CTA `href` = литерал `[REDACTED]` → HTTP 404; не реальные URL каталога/Telegram |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 66.2 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | **BLOCK** | `pain_markers=0`, `outcome_markers=0` — в `editorial-policy.json` нет `pain_markers_ru` / `outcome_markers_ru` (пустые списки → вечный BLOCK). Контент статьи при маркерах human-voice проходит |
| human-voice gate | PASS | concrete/pain/outcome/story overlap OK; warn: 3× списки ровно из 5 пунктов |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Ставка «по фото/букве Z» → гибрид A202A, непроходной месяц, голая X, 2WD вместо 4WD |
| Где решение | H2: сценарий → код кузова/мотор/привод → X/G/Z → месяц+лист → чек-лист 10 → критерий готового выбора |
| Первый результат | Мини-бриф лота + список «не ставлю, если…» до FAQ |
| Термины «на пальцах» | Код кузова A201A/A210A/A202A, проходной месяц, remarks, оценка 4+, D-CVT — без тона «для профи» |
| Beginner-fit | **PASS** |

## Scores (до veto)

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/meta; CTA сломаны литералом REDACTED |
| GEO / citability | 22/25 | TL;DR+схема+таблица+FAQ×7+чеклист; ярлык «TL;DR / Быстрый инсайт» запрещён skill |
| CORE-EEAT lite | 18/20 | см. таблицу ниже |
| Human voice | 14/15 | human-voice PASS; предупреждение про одинаковые ol×5 |
| Fact safety | 12/15 | fact-check PASS; много дат вне fact-bank (есть в research) |
| Contract HTML | 8/10 | whitelist OK; объём 9346; **битые href** |
| **Итого** | **72/100** | veto link-verify + utility BLOCK |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary how-to в H1/title |
| C02 | ✓ | Lead: боль ставки + чек-лист до торгов |
| C03 | ✓ | Новичок, Дром/аукцион, риск СВХ |
| C04 | ✓ | Коды кузова / комплектации объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный путь до ставки |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + workflow, mode B |
| R01 | ✓ | Инсайт, схема, чеклист, FAQ |
| R02 | ✓ | Габариты/коды/возраст — research |
| R03 | ✓ | Нет готовых сумм пошлин; расчёт → каталог |
| R04 | ✓ | FAQ отвечает действием в 1-м предложении |
| E01 | ✓ | Угол «до ставки / лист важнее фото» |
| E02 | ✓ | Делайте / Не делайте |
| E03 | ✗ | CTA href = `[REDACTED]` (некликабельно / 404) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Гибрид, возраст, remarks, логистика |
| Ept02 | ✗ | Нет internal blog links на другие посты (только каталог+TG — и те битые) |

**Target:** ≥16/20 ✓ · hard veto: link-verify FAIL, utility BLOCK

## Link verify

- total: 3 (internal_relative после `--site-base`), failed: 3  
- причина: в `article.html` записано буквально `href="[REDACTED]"` (hex `5b52454441435445445d`), не URL из conversion-map/fact-bank  
- see `link-verify.json`

## AI-slop scan

- cliches: 0  
- over-long: 5  
- Flesch RU: 66.2  

## Schema ready

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (чеклисты) — **cover/schema не стартовать** до PASS

## Blockers

1. **LINK VERIFY FAIL** — восстановить реальные CTA: каталог сайта + Telegram avtosales125 из `memory/brief/conversion-map.md` / fact-bank (не строка `[REDACTED]`).
2. **UTILITY ARTICLE BLOCKER** — machine gate: `pain_markers_ru` / `outcome_markers_ru` отсутствуют в `memory/brief/editorial-policy.json` → счётчики всегда 0. Нужен durable fix (fixer): добавить маркеры (как в `excalibur_blog_human_voice_gate.py`) или не требовать min при пустом списке. Контент статьи по human-voice уже содержит боль/результат.
3. **Insight label** — блок начинается с `TL;DR / Быстрый инсайт` (запрет skill/linter guidance) → переименовать (напр. «Коротко до ставки:»).

## FIX cycle (QA → Writer) — цикл 1

Writer **должен** (без правок от GEO QA):

1. Заменить все `href="[REDACTED]"` на рабочие URL каталога и Telegram из brief (≤3 CTA).
2. Убрать ярлык `TL;DR` / `Быстрый инсайт` из первого blockquote.
3. (Опционально non-blocking) варьировать длину ol (не три списка ровно по 5); 1–2 internal blog links когда slug LIVE.

**Параллельно Director/Fixer:** починить `editorial-policy.json` (+ pitfalls), иначе utility gate останется BLOCK даже после контент-FIX.

## Gate

- score ≥ 80 → **72** ✗ (veto)  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✗  
- research notes gate PASS → ✓  
- utility gate PASS → ✗  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FAIL — **не** READY FOR COVER\|\|SCHEMA. Вернуть **Writer FIX** (+ Fixer на policy markers).
