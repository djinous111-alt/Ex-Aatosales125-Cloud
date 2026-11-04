# Article QA — AS21 (GEO QA re-run after Writer FIX cycle 1)

**topic_id:** AS21  
**slug:** hongqi-hs5-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS21-hongqi-hs5-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-04  
**verdict:** PASS  
**score:** 85  
**beginner_fit:** PASS  
**fix_cycle:** 1 (Writer) → GEO QA re-run  

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=today; pain/outcome/story present |
| fact-check | PASS | 17 stats; 1 verified / 16 unverified soft (в research-notes: MY2026 MSRP, 252 vs 245, WLTC) |
| link-verify | PASS | Telegram 200; catalog `catalog_ssl` soft-pass (Cloud egress handshake timeout) |
| html-linter | PASS | whitelist OK; TOC нет; без `<pre>`/`<code>` |
| slop-detector | PASS | 0 клише; over-long 4; Flesch RU 74.2 |
| cannibalization | PASS | 0 issues (`--blog-dir`) |
| utility gate | PASS | action 10 / pain 5 / outcome 8 |
| human-voice | PASS | insight `Инсайт до депозита:`; outcome_markers: результат, проверьте, выберите |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; H2 action; CTA×2; нет 2–3 blog internal |
| GEO / citability | 24/25 | инсайт+таблицы+FAQ×6+чеклист; ярлык без TL;DR |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 14/15 | PASS: topical insight + ≥3 outcome markers |
| Fact safety | 12/15 | цифры в research-notes; fact-bank почти пуст по теме |
| Contract HTML | 10/10 | whitelist PASS, FAQ, CTA, Fact Check author OK |
| **Итого** | **85/100** | ≥80 → PASS |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «hongqi hs5 комплектации» в title/H1 |
| C02 | ✓ | Lead — боль депозита / Comfort vs QiXiang |
| C03 | ✓ | Новичок под заказ из Китая до депозита |
| C04 | ✓ | QiYun/QiXiang/Shadow, 2WD/4WD, MY2026 объяснены |
| O01 | ✓ | H2 = сверить → trim → привод → лот → ловушки → чеклист → расчёт |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы + схемы, mode B |
| R01 | ✓ | Инсайт, схема до оплаты, вердикт, FAQ |
| R02 | ✓ | 252/245 л.с., MSRP CN, WLTC 7.34/7.92 в research-notes |
| R03 | ✓ | Без готовых сумм утиля/пошлин; цены РФ как ориентир с сайта |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + словарь CN vs Comfort/Deluxe |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог + Telegram ≤3 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Factory-order VIN, разные каналы мощности, стоп оплаты физлицу |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate veto:** нет (human-voice PASS)

## Beginner-fit

- **Боль новичка:** депозит уходит до сверки китайского имени trim / привода / мотора (Comfort≈Deluxe ловушка).
- **Где решение:** H2 словарь QiYun/QiXiang/Shadow, 2WD vs 4WD, ловушки официал vs CN, чеклист 10 пунктов.
- **Первый результат до FAQ:** заполненный чеклист + строка MY2026 + trim + 2WD/4WD + VIN-milestone в договоре → депозит / пауза / отказ (`Результат:` перед FAQ).
- **Термины «на пальцах»:** Shadow = чёрный пакет не другой мотор; 2WD/4WD по массе/WLTC; 252 vs 245 = разные каналы.

## Link verify

- total: 2, failed: 0
- soft_pass: `catalog_ssl`
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 74.2

## Writer FIX verification (cycle 1)

1. Insight label: `Инсайт до депозита:` (нет `TL;DR` / `Быстрый инсайт`) ✓  
2. OUTCOME_MARKER human: `результат` (+ `проверьте`, `выберите`) ≥3 ✓  
3. human-voice-report.json → PASS ✓  

## Next

cover || schema (parallel) — GEO QA PASS unlocked.
