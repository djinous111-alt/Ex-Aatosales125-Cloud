# Article QA — B05

**topic_id:** B05  
**slug:** kak-popolnit-els-fts-pered-rastamozhkoy-avto-2026  
**article_dir:** memory/blog/articles/B05-kak-popolnit-els-fts-pered-rastamozhkoy-avto-2026  
**date:** 2026-10-18  
**cycle:** RETRY after FIX (writer CTA + fixer policy/link-verify)  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | `research-notes-gate.json`; errors=[]; warnings=[] |
| utility gate | PASS | pain_markers=7, outcome_markers=8; `utility-gate-report.json` overall PASS |
| human-voice-gate | PASS | `human-voice-report.json`; warn: 4× exactly-5-step lists |
| fact-check | PASS | 8 stats; 1 verified (2026); 7 unverified vs fact-bank (КБК/коды/15 мин/1e6 — в research-notes) |
| link-verify | PASS | failed_count=0; edata SSL timeout → soft warning OK; CTA catalog+Telegram HTTP 200 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; over-long 4; Flesch RU 65.9 |
| cannibalization | PASS | 0 issues (`cannibalization-report.json`) |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка решена? | Машина на пути/СВХ, непонятный ЕЛС, миф «жена/брокер заплатит» — с 01.04.2026 чужой платёж не зачисляют |
| Где показано решение? | H2: кошелёк ЕЛС → ЛК через Госуслуги → СБП своей картой → реквизиты/КБК → остаток+скрин → troubleshooting → чек-лист |
| Первый результат до FAQ? | «Открытый ЛК, достаточный остаток на своём ЕЛС и скрин у менеджера» + критерии «готово» |
| Термины «на пальцах»? | ЕЛС, СВХ, СБП, КБК, код органа 10000010 vs 10702000 — объяснены |
| Beginner-fit | PASS (первый шаг без ЭЦП/разработчиков; без тона «для профи») |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1; H2 actionable; CTA живые HTTPS |
| GEO / citability | 22/25 | Инсайт, схема, таблица, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS, slop 0 |
| Fact safety | 12/15 | Факты в research; не все в fact-bank; edata soft-fail warning |
| Contract HTML | 10/10 | Whitelist PASS; utility PASS; link-verify PASS |
| **Итого** | **88/100** | порог ≥80 ✓ |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как пополнить елс фтс» в title/H1 |
| C02 | ✓ | Lead: боль СВХ + запрет чужого платежа + чек-лист |
| C03 | ✓ | Читатель: физлицо, авто под заказ Владивосток |
| C04 | ✓ | ЕЛС/СБП/КБК объяснены |
| O01 | ✓ | H2 ≈ action_outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | Инсайт + схема + FAQ |
| R02 | ✓ | 58н / КБК / лимит СБП / ~15 мин — в research |
| R03 | ✓ | Нет сумм пошлин; запас 20–30 тыс. с оговоркой |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «только свой ИНН» + конфликт кодов органа |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA catalog + Telegram — живые URL, link-verify 200 |
| Exp01 | ✓ | Mode B, история Игоря без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Выходные/чужая карта/конфликт кодов |
| Ept02 | ✗ | Нет internal blog links (ожидаемо до Indexer) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** нет

## Link verify

- total_links: 3
- failed_count: 0
- verdict: pass
- edata.customs.ru: SSL handshake timeout → soft external warning (ok=true)
- catalog + Telegram CTA: HTTP 200

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 65.9

## Soft notes (не blockers)

1. Инсайт-блок начинается с ярлыка `TL;DR / Быстрый инсайт` — skill preference; html-linter/HV PASS; не требуем writer rewrite на этом цикле.
2. 4× списки ровно по 5 шагов — HV warning only.
3. Internal interlinks — зона Indexer после cover||schema.

## Schema ready

BlogPosting: ready for schema Task | FAQPage: yes (6) | HowTo: yes | cover/schema: **можно** запускать параллельно

## Blockers

(none)

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-gate PASS ✓  
- link-verify pass ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — cover || schema разрешены.
