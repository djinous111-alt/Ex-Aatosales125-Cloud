# Article QA — B01

**topic_id:** B01  
**slug:** mozhno-li-privezti-gibrid-iz-yaponii-2026  
**article_dir:** memory/blog/articles/B01-mozhno-li-privezti-gibrid-iz-yaponii-2026  
**date:** 2026-10-14  
**verdict:** PASS  
**score:** 88  
**human_voice:** PASS  
**utility_gate:** PASS  
**beginner_fit:** PASS  
**cycle:** re-run after Writer FIX + editorial-policy pain/outcome restore

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN: technical_topic false-positive (known INC) |
| fact-check | PASS | 3 facts; 2023/2024 unverified vs fact-bank (есть в research-notes) |
| link-verify | PASS | Telegram 200; catalog 503 → **soft-pass** (`catalog_5xx`) |
| html-linter | PASS | whitelist OK, TOC нет, pre/code нет |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 71.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 21 (≥8); pain 10 (≥2); outcome 9 (≥3) |
| human voice gate | PASS | outcome: результат/получите/сможете/проверьте/выберите; warnings=[] |

## Pain / solution / beginner (обязательная фиксация)

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Путает любой Hybrid с разрешённым вывозом; риск депозита за полный/PHEV/EV/e-POWER (lead: Freed GB7 vs GP3) |
| Где решение | H2: мягкий vs полный → чтение листа/кузова → красные флаги → чеклист 10 → «что сделать сегодня» |
| Первый результат | Код кузова + вердикт мягкий/стоп + ДВС ≤1,9 л **до** депозита |
| Термины «на пальцах» | mild / полный / PHEV / e-POWER / аукционный лист / код кузова |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Title/H1/primary ок; live CTA (catalog+Telegram); нет 2–3 blog internal |
| GEO / citability | 22/25 | TL;DR, таблица, FAQ×6, чеклисты; outcome/pain маркеры сильные |
| CORE-EEAT lite | 18/20 | см. ниже |
| Human voice | 14/15 | gate PASS; exactly_five_lists=1 (не BLOCK) |
| Fact safety | 12/15 | даты 2023/2024 не в fact-bank; тон осторожный |
| Contract HTML | 10/10 | whitelist PASS; char_count 8886; FAQ; CTA |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в title/H1 |
| C02 | ✓ | Lead: можно, но не любой Hybrid |
| C03 | ✓ | Новичок до депозита |
| C04 | ✓ | Термины объяснены |
| O01 | ✓ | H2 = pain→solution map |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + mode B |
| R01 | ✓ | TL;DR + схема + FAQ |
| R02 | ✓ | Ноябрь 2024 / август 2023 + кузова в тексте |
| R03 | ✓ | Нет копирования пошлин; «расчёт под лот» |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки / шильдик ≠ разрешение» |
| E02 | ✓ | «сделайте / не делайте» + action markers |
| E03 | ✓ | CTA: каталог + Telegram (live href в working tree) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop 0 |
| Ept01 | ✓ | Сверка кузова «на сегодня» |
| Ept02 | ✗ | Нет внутренних blog-links на другие посты |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate score ≥80:** ✓ (88)

## Link verify

- total: 2; hard-fail raw: catalog 503; after soft-pass: failed_count=0
- Telegram: 200 OK
- Catalog: 503 HEAD+GET → soft-pass `catalog_5xx` (pipeline memory / pitfalls)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (таблица/схема парсером)
- Flesch RU: 71.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после URL соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 2023/2024 — дописать в fact-bank для verified.
3. **link-verify durable:** `excalibur_blog_link_verify.py` всё ещё hard-fail на catalog 5xx; soft-pass пока ручной (QA).

## Gate checklist

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✓ (catalog 503 soft-pass)  
- research notes gate PASS → ✓  
- utility gate PASS → ✓  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — можно cover || schema.
