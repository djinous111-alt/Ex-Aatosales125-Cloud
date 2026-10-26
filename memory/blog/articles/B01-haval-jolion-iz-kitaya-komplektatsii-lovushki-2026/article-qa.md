# Article QA — B01

**topic_id:** B01  
**slug:** haval-jolion-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-haval-jolion-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-27  
**verdict:** PASS  
**score:** 86  
**author_id:** avtosales-editorial (registry OK)  
**cycle:** re-QA after writer FIX (CTA hrefs + TL;DR label)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN: technical_topic false-positive (INC-20261027-0020) |
| utility gate (stock policy) | BLOCK | empty `pain_markers_ru`/`outcome_markers_ru` — durable INC-0035 |
| utility gate (FALLBACK) | PASS | overlay human-voice markers; pain=4 outcome=6 action=12 |
| human-voice-gate | PASS | WARN: multiple exactly-5-step lists |
| html-linter | PASS | whitelist OK; TOC нет; TL;DR ярлык снят |
| fact-check | PASS | 4 stats; verified 1 (`2026`); unverified 2023/143/270 в research |
| link-verify | PASS | 2/2 OK (`$TELEGRAM_URL`, `$CATALOG_URL`); status 200 |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU 65.4 |
| cannibalization | PASS | 0 issues |

## Beginner-fit / pain→outcome

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит на «красивый Премиум из Китая» без сверки привода/КПП/VIN |
| Где решение | H2: РФ-матрица; Comfort/Оптимум/Premium/Techno+; ловушки; VIN; чек-лист 10 пунктов |
| Первый результат | Заполненный 10-пунктный лист + стоп без VIN до денег |
| Термины «на пальцах» | 2WD/4WD, MT/7DCT, СВХ, СБКТС, ЭПТС |

**beginner-fit:** PASS

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в H1/title; CTA живые; нет 2–3 internal blog (−2) |
| GEO / citability | 23/25 | Insight «Коротко», таблица, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | 0 AI-slop; warn по спискам×5 |
| Fact safety | 12/15 | Цифры в research; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; CTA×3 с pragma; объём ~9429 |
| **Итого** | **86/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: боль депозита → чек-лист |
| C03 | ✓ | Новичок параллельного ввоза Jolion |
| C04 | ✓ | 2WD/4WD, DCT, СВХ, СБКТС, ЭПТС |
| O01 | ✓ | H2 = action outline |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol + table + mode B |
| R01 | ✓ | Insight + таблица + FAQ |
| R02 | ✓ | Ориентиры МЦП / момент / 2023 в research |
| R03 | ✓ | Нет «цены под ключ» без оговорки |
| R04 | ✓ | FAQ с 1-го предложения |
| E01 | ✓ | Угол до депозита + Chitu |
| E02 | ✓ | Делать / Не делать |
| E03 | ✓ | CTA: `$CATALOG_URL`×2 + `$TELEGRAM_URL`×1 |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты гарантии серого ввоза |
| Ept02 | ✗ | Нет internal blog links на AS08/AS09 |

**Target:** ≥16/20 ✓ · veto: нет

## Link verify

- total: 2 unique, failed: 0
- `$TELEGRAM_URL` → 200; `$CATALOG_URL` → 200
- see link-verify.json (env placeholders in committed copy)

## AI-slop scan

- cliches: 0
- over-long: 6
- Flesch RU: 65.4

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes | cover/schema: **можно** после Director handoff

## Blockers

- нет

## FIX cycle (QA)

1. Cycle 1 FAIL: CTA `href="[REDACTED]"` → writer restored `$CATALOG_URL`/`$TELEGRAM_URL` + pragma; TL;DR label removed.
2. Cycle 2 re-QA: link-verify PASS; overall PASS 86.

## Soft / optional (non-blocking)

1. **Ept02:** после publish — 2–3 internal links на AS08/AS09.
2. **utility stock:** fixer — `pain_markers_ru`/`outcome_markers_ru` в editorial-policy (INC-0035).
3. **human-voice warn:** варьировать длину ol.
4. **fact-bank:** дописать 143 л.с. / 270 Нм / 2023 при желании.

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS (FALLBACK) ✓  
- human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
