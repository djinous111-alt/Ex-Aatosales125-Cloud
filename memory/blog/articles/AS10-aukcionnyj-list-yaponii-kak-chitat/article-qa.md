# Article QA — AS10

**topic_id:** AS10  
**slug:** aukcionnyj-list-yaponii-kak-chitat  
**article_dir:** memory/blog/articles/AS10-aukcionnyj-list-yaponii-kak-chitat  
**date:** 2026-07-20  
**verdict:** PASS  
**score:** 88  
**cycle:** re-QA after Writer FIX

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: false `technical_topic` (INC-0010) |
| fact-check | PASS | 2/2 verified (2026; 20 минут) |
| link-verify | PASS | 2/2 OK (catalog + Telegram, HTTP 200) |
| html-linter | PASS | whitelist OK; TOC нет; инсайт «Коротко:» |
| slop-detector | PASS | 0 клише; 3 over-long (таблица/схема); Flesch RU 63.1 |
| cannibalization | PASS | 0 issues (3 metas loaded) |
| utility gate | PASS | action_markers 27 (≥8); pain 3; outcome 7 |
| human-voice gate | PASS | outcome: результат, получите, сможете, проверьте, выберите |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Шифр листа (4/4.5/R/A1/W…) → страх депозита «на красивую оценку» и скрытый ремонт |
| Где решение | H2: правило до депозита → шапка → оценки/салон → схема/примечания → фото → чеклист → первый результат |
| Первый результат | За 15–20 мин закрыть чеклист и сказать «беру / не беру / уточнение» с причиной |
| Термины «на пальцах» | 4/4.5/5, R/RA, салон A–E, A/U/W/X/XX/S/C — таблица + ul-легенда |
| beginner-fit | PASS (не профи-тон; безопасный первый шаг без команды) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 action; CTA живые; нет 2–3 blog internal |
| GEO / citability | 22/25 | Коротко-инсайт, схема, таблица, FAQ×7, чеклист 12 |
| CORE-EEAT lite | 14/15 | 19/20 — см. таблицу ниже |
| Human voice | 15/15 | human-voice PASS; concrete/pain/outcome OK |
| Fact safety | 13/15 | fact-check PASS; источники в Fact Box |
| Contract HTML | 10/10 | linter PASS; живые CTA; ярлык без TL;DR |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в meta/H1 |
| C02 | ✓ | Lead = боль + порядок чтения до депозита |
| C03 | ✓ | Новичок / заказ из Японии / депозит |
| C04 | ✓ | Оценки, салон, коды схемы объяснены |
| O01 | ✓ | H2 = pain_solution_map / checklist |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol 5 + ul чеклист + table; mode B |
| R01 | ✓ | Инсайт «Коротко» + порядок + FAQ |
| R02 | ✓ | Нюанс TAA vs USS 2026; источники в Fact Box |
| R03 | ✓ | Нет выдуманных цен лотов |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» |
| E02 | ✓ | «Сделайте / Не делайте» (≥8 utility markers) |
| E03 | ✓ | CTA: каталог + Telegram (живые https, link-verify PASS) |
| Exp01 | ✓ | Mode B, reader_story Андрей |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты R/RA, XX≠рама, расхождение шкал |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблицы/схемы)
- Flesch RU: 63.1

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | cover/schema: можно запускать

## Blockers

- нет

## FIX cycle closed (Writer → re-QA)

1. CTA literal `[REDACTED]` → живые CATALOG_URL / TELEGRAM_URL → link-verify PASS  
2. Utility action-маркеры ≥8 → 27 → PASS  
3. Human-voice outcome ≥3 → 5 маркеров → PASS  
4. Инсайт-ярлык → «Коротко:» (без TL;DR)

## FIX (non-blocking / optional)

1. **Ept02:** после URL других постов AS* на сайте — 2–3 internal links с `anchor_variants`.  
2. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify → PASS ✓  
- research-notes-gate → PASS ✓  
- utility gate → PASS ✓  
- human-voice → PASS ✓  
- beginner-fit → PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
