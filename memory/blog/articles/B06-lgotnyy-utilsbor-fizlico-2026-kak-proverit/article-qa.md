# Article QA — B06 (attempt 2 / after Writer FIX cycle 1)

**topic_id:** B06  
**slug:** lgotnyy-utilsbor-fizlico-2026-kak-proverit  
**article_dir:** memory/blog/articles/B06-lgotnyy-utilsbor-fizlico-2026-kak-proverit  
**date:** 2026-07-25  
**attempt:** 2 (after FIX)  
**verdict:** PASS  
**score:** 90

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: false-positive technical (нет official docs URL) |
| fact-check | PASS | 10 stats; 3 verified / 7 unverified (пороги/даты в research-notes) |
| link-verify | **PASS** | 2 unique external links; failed_count=0; HTTP 200 (каталог + Telegram); литерал `[REDACTED]` в href = 0 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/схема + длинный insight); Flesch RU 70.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 38 / pain 10 / outcome 21; lists+FAQ×7+tables×2 |
| human-voice-gate | PASS | `human-voice-report.json` status PASS |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1; H2 по чеклисту; CTA рабочие |
| GEO / citability | 22/25 | Insight «Главное до депозита» (без TL;DR); схема; таблицы; FAQ×7; чеклист 10 |
| CORE-EEAT lite | 18/20 | 18/20; нет 2–3 internal blog links (мягкий минус) |
| Human voice | 15/15 | Gate PASS; story/pain/outcome OK |
| Fact safety | 12/15 | Пороги согласованы с research-notes; 7 unverified vs fact-bank |
| Contract HTML | 9/10 | Whitelist OK; CTA href валидные https |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «льготный утильсбор» в meta title / H1 |
| C02 | ✓ | Lead: депозит + ложная ставка «я физлицо» → чеклист до оплаты |
| C03 | ✓ | Читатель-новичок, ввоз через Владивосток / Азия |
| C04 | ✓ | кВт, 30-мин. мощность, параллельный/последовательный гибрид «на пальцах» |
| O01 | ✓ | H2 = боль → мощность → гибрид → 1 авто/год → ЕАЭС → чеклист → расчёт → дальше |
| O02 | ✓ | Логичный outline checklist mode B |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol + таблицы + blockquote-схема |
| R01 | ✓ | Insight + схема до депозита + FAQ |
| R02 | ✓ | ПП 1713 / 01.12.2025 / порог 117,68 кВт в Fact Check Box + research |
| R03 | ✓ | Нет коммерческих сумм утиля; CTA в каталог на расчёт |
| R04 | ✓ | Ответ FAQ с первого предложения |
| E01 | ✓ | Угол «льгота ≠ статус физлица» + чеклист до депозита |
| E02 | ✓ | «Делать / Не делайте» в секциях |
| E03 | ✓ | CTA каталог + Telegram рабочие (link-verify PASS) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Граница 117,68 vs 117,69; EV 80 л.с.; СВО/многодетные ≠ закон |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate:** link-verify PASS ✓ · human-voice PASS ✓

## Beginner-fit / utility story

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Думает, что «льготный утильсбор» положен любому физлицу → риск коммерческого тарифа из‑за 161 л.с. / гибрида / ранней продажи |
| Где решение | H2 про статус, кВт, гибрид/EV, лимит 1 авто/год, чеклист 10 пунктов |
| Первый результат | Заполненный чеклист «да/нет» до депозита; при «нет» — расчёт в каталоге, не оплата |
| Термины «на пальцах» | кВт vs л.с.; 30-минутная мощность; последовательный vs параллельный гибрид |

## Link verify

- total unique checked: 2, failed: 0 (verdict **pass**)
- CTA: 3 href в HTML (каталог×2 + Telegram×1); литерал `[REDACTED]` отсутствует
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблиц + длинный insight)
- Flesch RU: 70.9

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

none

## Soft notes (не блокер)

1. OPTIONAL: 2–3 internal blog links с `anchor_variants` на соседние посты (AS08/AS09/B05).
2. OPTIONAL: дописать пороги 160 л.с. / 117,68 кВт в fact-bank (снизит unverified).

## FIX history

- **attempt 1:** FAIL score 72 — CTA `href="[REDACTED]"` + ярлык `TL;DR / Быстрый инсайт`
- **Writer FIX cycle 1:** CTA восстановлены; insight → «Главное до депозита»
- **attempt 2:** PASS score 90

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → **PASS** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — директор может запускать cover \|\| schema.
