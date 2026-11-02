# Article QA — AS02

**topic_id:** AS02  
**slug:** encar-na-russkom-kak-chitat  
**article_dir:** memory/blog/articles/AS02-encar-na-russkom-kak-chitat  
**date:** 2026-11-02  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: нет official docs URL (technical topic) |
| fact-check | PASS | 3 stats; unverified: манвон 10 000 / Carhistory ~2 200 — есть в research-notes |
| link-verify | PASS | 5 links; 1× soft_pass=`catalog_dns` (catalog TLS timeout из Cloud); Telegram 200; encar/carhistory 200 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU 71.7 |
| cannibalization | PASS | secondary «что такое trust encar» (после QA FIX); 0 issues |
| utility gate | PASS | action 33 / pain 13 / outcome 13 |
| human-voice | PASS | `human-voice-report.json` |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Корейский интерфейс, ложная «без ДТП», риск битого/утопленного, путаница с RU-зеркалами |
| Где решение | H2: официальный Encar → 5 полей → X/W → пробег/Carhistory → Trust vs сервис → красные флаги → критерий успеха |
| Первый результат | Мини-чеклист по одной карточке + понимание X/W + стоп до депозита |
| Термины «на пальцах» | манвон, Performance Check, X/W, flood/fire, Trust Encar vs Carhistory, General vs Lease/Rental |

**beginner_fit:** PASS (how-to для новичка, без профи-жаргона без расшифровки)

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «encar на русском» в title/H1; H2 how-to; CTA каталог+Telegram; мало blog internal |
| GEO / citability | 24/25 | Короткий разбор, таблица X/W, FAQ×6, чеклисты, схема-ритуал |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; 0 AI-opening hits |
| Fact safety | 13/15 | Факты в research-notes; 2 200 / 10 000 не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, FAQ, CTA×2, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: боль Антона + прямой обещаемый результат |
| C03 | ✓ | Читатель: новичок, перевод Encar, риск депозита |
| C04 | ✓ | Performance Check / X/W / Carhistory / Trust объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Короткий разбор + ритуал + FAQ |
| R02 | ✓ | ~2 200 вон, AuctionsAPI 2026-10-01, flood-check |
| R03 | ✓ | Нет выдуманных цен лотов/% |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «чтение карточки», не полный buy-cycle |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×1 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты страховки, X/W, flood, осмотр |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## FIX cycle (QA)

1. Insight `TL;DR / Быстрый инсайт` → `Короткий разбор` (контракт GEO QA skill).
2. Secondary query `trust encar` → `что такое trust encar` (cannibalization vs AS09 primary).
3. `link_verify`: восстановлен soft_pass catalog/site hosts из env (`catalog_dns`) + redact secret URLs в отчёте.

## Blockers

- нет

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓ (soft catalog_dns)  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema. GEO QA не запускает cover/schema/publish.
