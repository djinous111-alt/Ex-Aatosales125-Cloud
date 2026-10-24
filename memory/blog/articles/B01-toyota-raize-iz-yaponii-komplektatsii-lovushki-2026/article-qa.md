# Article QA — B01 (RETRY after Writer FIX + Fixer markers)

**topic_id:** B01  
**slug:** toyota-raize-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-raize-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-24  
**retry:** 1 (после Writer FIX CTA/insight + Fixer pain/outcome markers)  
**verdict:** PASS  
**score:** 92

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: technical false-positive «raize» / нет official docs URL |
| fact-check | PASS | 17 stats; 1 verified in fact-bank (2026); остальные в research-notes |
| link-verify | PASS | 2 unique external (каталог + Telegram), failed=0, HTTP 200; литерал `[REDACTED]` в href отсутствует |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 66.0 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | pain_markers=9, outcome_markers=5, action_markers=9; policy markers restored |
| human-voice gate | PASS | story/pain/outcome/success overlap OK; warn: 3× списки ровно из 5 пунктов |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Ставка «по фото/букве Z» → гибрид A202A, непроходной месяц, голая X, 2WD вместо 4WD |
| Где решение | H2: сценарий → код кузова/мотор/привод → X/G/Z → месяц+лист → чек-лист 10 → критерий готового выбора |
| Первый результат | Мини-бриф лота + список «не ставлю, если…» до FAQ |
| Термины «на пальцах» | Код кузова A201A/A210A/A202A, проходной месяц, remarks, оценка 4+, D-CVT — без тона «для профи» |
| Beginner-fit | **PASS** |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в H1/meta; CTA каталог×2 + Telegram×1 рабочие |
| GEO / citability | 23/25 | Инсайт «Коротко до ставки» + схема + таблица + FAQ×7 + чеклист |
| CORE-EEAT lite | 19/20 | см. таблицу ниже |
| Human voice | 14/15 | human-voice PASS; warn про одинаковые ol×5 |
| Fact safety | 12/15 | fact-check PASS; много дат вне fact-bank (есть в research) |
| Contract HTML | 10/10 | whitelist OK; объём ~9341; href из CATALOG_URL/TELEGRAM_URL |
| **Итого** | **92/100** | hard gates все PASS |

## CORE-EEAT lite: 19/20

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
| E03 | ✓ | CTA href = рабочие URL каталога и Telegram (200) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Гибрид, возраст, remarks, логистика |
| Ept02 | ✗ | Нет internal blog links на другие посты (только каталог+TG) — non-blocking |

**Target:** ≥16/20 ✓

## Link verify

- total unique: 2 external, failed: 0, verdict: **pass**
- CTA: catalog host `avto-sales125.ru` ×2 + Telegram `t.me` ×1; литерал `href="[REDACTED]"` count=0
- see `link-verify.json`

## AI-slop scan

- cliches: 0  
- over-long: 5  
- Flesch RU: 66.0  

## Schema ready

BlogPosting: pending | FAQPage: yes (7) | HowTo: yes (чеклисты) — **READY FOR COVER\|\|SCHEMA**

## Previous blockers (resolved)

1. ~~LINK VERIFY FAIL~~ → CTA из CATALOG_URL / TELEGRAM_URL, HTTP 200  
2. ~~UTILITY ARTICLE BLOCKER~~ → `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json`; utility PASS  
3. ~~Insight label TL;DR~~ → «Коротко до ставки»

## Non-blocking notes

- human-voice warn: варьировать длину ol (не три списка ровно по 5) — можно в следующем polish  
- 1–2 internal blog links когда соседние slug LIVE  
- research-notes-gate warn: technical false-positive на «raize»

## Gate

- score ≥ 80 → **92** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✓  
- research notes gate PASS → ✓  
- utility gate PASS → ✓  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — **READY FOR COVER\|\|SCHEMA**
