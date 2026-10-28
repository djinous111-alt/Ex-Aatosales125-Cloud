# Article QA — B01

**topic_id:** B01  
**slug:** toyota-crown-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-crown-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-28  
**verdict:** PASS  
**score:** 88

## Pain / solution / beginner-fit

| Check | Result |
|-------|--------|
| Боль новичка в lead | ✓ Иван + депозит Sport RS / PHEV / W2; «путаете кузова и буквы G/Z/RS» |
| Решение в H2 | ✓ кузова → G/Z/RS → HEV/PHEV+маршрут → лист R/RA → чеклист 8 пунктов |
| Результат до FAQ | ✓ критерий успеха + чеклист заполнен; бриф без «гуру» |
| Термины «на пальцах» | ✓ HEV/PHEV, G/Z/RS, оценка R/RA vs код R на стекле, W2–W3 |
| Первый безопасный шаг | ✓ 8 пунктов + запрос маршрута до депозита |
| Beginner-fit | **PASS** (не профиль/разработчик; без требования команды «на местах») |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | status PASS; urls=29 domains=14 accessed_at=13; technical_topic=false |
| utility gate | PASS | action_markers 36; pain 4; outcome 13; FAQ×6; table×1 |
| human-voice gate | PASS | human-voice-report.json; concrete/pain/outcome markers OK |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified 2025/2023/1900 — есть в research-notes (Toyota/METI) |
| link-verify | PASS | 3/3 OK после percent-encode кириллицы в 2GIS URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (склейка table/схем); Flesch RU 84.4 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «тойота краун из японии» в title/H1; H2 how-to; CTA×3; нет 2–3 blog internal |
| GEO / citability | 24/25 | Инсайт-блок, схема до депозита, таблица кузовов, FAQ×6, чеклист×8 |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice PASS; slop hits = 0 |
| Fact safety | 13/15 | METI/Toyota/лист в notes; часть дат не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9.2k chars, FAQ, CTA≤3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: боль депозита + обещание чеклиста |
| C03 | ✓ | Новичок, импорт Crown из Японии |
| C04 | ✓ | Кузова / G Z RS / HEV PHEV / лист объяснены |
| O01 | ✓ | H2 = pain_solution_map research |
| O02 | ✓ | Логичный outline до ставки |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | Инсайт, схема, FAQ |
| R02 | ✓ | MSRP ¥ / METI 09.08.2023 / Estate 13.03.2025 в notes |
| R03 | ✓ | Нет «под ключ» цифр РФ; расчёт по лоту |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до ставки / до депозита» |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×1 + Telegram×1 + 2GIS×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | METI, R/RA, W2, гибрид-узлы |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- see link-verify.json
- FIX cycle: 2GIS URL с сырой кириллицей → ASCII percent-encode (urllib ascii codec)

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/схемы)
- Flesch RU: 84.4

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. link-verify FAIL на 2GIS (`ascii codec`) → percent-encode path в `article.html` → PASS 3/3.

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 13.03.2025 / 09.08.2023 / 1900 cc — дописать в fact-bank.
3. **link_verify durable:** IRI-encode non-ASCII URLs в `excalibur_blog_link_verify.py` (см. incident).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- link-verify pass ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
