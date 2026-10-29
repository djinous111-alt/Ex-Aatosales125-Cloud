# Article QA — B01 Toyota RAV4 из Японии

**topic_id:** B01  
**slug:** toyota-rav4-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-rav4-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-29  
**verdict:** PASS  
**score:** 87

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Путает Комфорт/Престиж РФ с JP-грейдами X/G/Adventure; рискует депозитом на Hybrid / >1900 см³ / XA60 HEV |
| Где решение | H2: сверка до ставки → кузова XA50/XA60 → грейды → бензин/гибрид → ловушки листа → чек-лист 12 пунктов |
| Первый результат | Вердикт «проходной / непроходной / нужна сверка» по лоту без депозита вслепую |
| Термины «на пальцах» | Аукционный лист, грейд, карта A/U/B/W/XX, порог 1900 см³ / METI с 09.08.2023 |
| Beginner-fit | PASS — первый безопасный шаг без команды разработчиков; нет API/RAG-жаргона |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: technical_topic false-positive / no /docs URL |
| utility gate | PASS | action 22 / pain 21 / outcome 19 |
| human-voice gate | PASS | warn: exactly-5 lists (false-positive vs ol×6) |
| html-linter | PASS | whitelist OK; TOC нет; `<pre>`/`<code>` нет |
| fact-check | PASS | 7 stats extracted; soft unverified vs fact-bank |
| link-verify | PASS | 3/3 live after `${CATALOG_URL}`/`${TELEGRAM_URL}` expand; 2GIS percent-encoded |
| slop-detector | PASS | 0 cliches; 3 over-long; Flesch RU 78.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «тойота рав 4 комплектации» в title/H1/meta; H2 how-to; CTA×3 |
| GEO / citability | 23/25 | Инсайт, схема, таблица кузовов, FAQ×6, чек-лист 12 |
| CORE-EEAT lite | 18/20 | см. таблицу ниже |
| Human voice | 14/15 | reader_story/pain/outcome overlap OK; warn lists |
| Fact safety | 13/15 | METI 09.08.2023 + 1900 + Toyota releases; soft fact-check |
| Contract HTML | 10/10 | whitelist, ~8624 символов текста, FAQ, CTA placeholders, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary query в title / H1 / description |
| C02 | ✓ | Lead сразу называет боль и обещает чек-лист до ставки |
| C03 | ✓ | Читатель: семья / заказ JP RAV4, риск непроходного лота |
| C04 | ✓ | Грейд / лист / XA50·XA60 объяснены простым языком |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный путь: сверка → кузов → грейд → мотор → лист → чек-лист → результат |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote-схема, mode B |
| R01 | ✓ | Инсайт до ставки + схема + FAQ |
| R02 | ✓ | 1986 см³, 1900 порог, 09.08.2023, XA60 HEV-only |
| R03 | ✓ | Нет цен лотов / пошлин в статье |
| R04 | ✓ | FAQ отвечает в первом предложении |
| E01 | ✓ | Угол «стоп руки над ставкой» + surprising_fact |
| E02 | ✓ | «Делайте / Не делайте» в секциях |
| E03 | ✓ | CTA: Telegram + каталог + 2GIS |
| Exp01 | ✓ | Mode B, без fake first-person «я купил» |
| Exp02 | ✓ | Тон эксперта Владивостока |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: Hybrid/PHEV стоп, оценка ≠ гарантия |
| Ept02 | ✗ | Нет 2–3 internal blog links (ожидаемо до Indexer) |
| Ept02b | ✗ | (слот не отдельный; −2 к CORE за отсутствие interlink до Indexer) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- committed HTML: `${CATALOG_URL}`, `${TELEGRAM_URL}`, 2GIS IRI-encoded
- see `link-verify.json` (URLs scrubbed)

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 78.5

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чек-листы) | Review: no | cover/schema: вне зоны GEO QA

## Blockers

- нет

## FIX cycle (QA)

1. Insight label `TL;DR / Быстрый инсайт` → `Инсайт до ставки` (skill forbid).
2. Raw CTA URLs → `${CATALOG_URL}` / `${TELEGRAM_URL}` для commit/secret-scan; live expand только для link-verify.
3. Re-run all gates → PASS.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- link-verify pass ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
