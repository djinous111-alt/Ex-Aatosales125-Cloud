# Article QA — AS02 (recheck after FIX cycle 1)

**topic_id:** AS02  
**slug:** encar-na-russkom-kak-chitat  
**article_dir:** memory/blog/articles/AS02-encar-na-russkom-kak-chitat  
**date:** 2026-11-03  
**verdict:** PASS  
**score:** 91  
**author_id:** avtosales-editorial  
**recheck:** after Writer FIX cycle 1 (insight label → «Короткий разбор»)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date/today OK; source table + pain/outcome map |
| fact-check | PASS | 6 stats; 1 verified (2026); 5 unverified (манвон×10000, 30 дней/2000 км, примеры 1890/2450) — есть в research-notes |
| link-verify | PASS (soft) | encar.com HEAD 200; Telegram HEAD 200; brand-twin catalog → `catalog_ssl` soft-pass после retry 15/30/45s (Cloud egress SSL handshake timeout) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка таблиц/схем парсером); Flesch RU 69.5 |
| cannibalization | PASS | 0 issues (AS09 = Carhistory/депозит; AS02 = чтение карточки) |
| utility gate | PASS | action 24 / pain 5 / outcome 13; FAQ×6; tables×2 |
| human-voice gate (CLI) | PASS | concrete/pain/outcome markers OK; reader_story overlap OK |
| **insight label (skill manual)** | **PASS** | blockquote: `Короткий разбор` — без `TL;DR` / `Быстрый инсайт` |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «encar на русском» в title/H1; H2 how-to; CTA catalog×2 + Telegram×1; мало blog-internal |
| GEO / citability | 24/25 | Инсайт+таблицы+FAQ×6+чеклист; ярлык инсайта OK |
| CORE-EEAT lite | 18/20 | 18/20 (см. таблицу) |
| Human voice | 14/15 | CLI PASS + нейтральный ярлык инсайта |
| Fact safety | 13/15 | Цифры в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; insight label соответствует skill |
| **Итого** | **91/100** | score ≥80 ✓ · все hard gates PASS |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «encar на русском» в meta / H1 |
| C02 | ✓ | Lead: боль депозита + прямой ответ «перевод + 5 полей + X/W» |
| C03 | ✓ | Читатель: новичок корейского лота |
| C04 | ✓ | Манвон, 무사고, X/W, Performance Check, Trust Encar объяснены |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы + чеклист, mode B |
| R01 | ✓ | Инсайт-блок + мини-схема + FAQ |
| R02 | ✓ | Vinlid ~1,55 млн / 14,4% / ~40% + манвон×10 000 |
| R03 | ✓ | Нет выдуманных «под ключ» цен; ориентиры с пометкой |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «чтение карточки до депозита», мост AS09 |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты страховки, навесные vs силовые, перевод |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · insight-label veto: **нет** → overall PASS

## Beginner-fit: PASS

- Боль новичка: корейский интерфейс + ложное «без ДТП» → депозит вслепую.
- Решение: перевод браузера → 5 полей → схема X/W → стоп до депозита.
- Первый результат: чеклист из 5 полей + правило по силовым за один вечер.
- Термины на пальцах: 만원/манвон, 무사고, X/W, Performance Check, Trust Encar vs лист осмотра.

## Pain / solution map

| Боль | Где решена |
|------|------------|
| Сайт на корейском / кривой перевод | H2 «Откройте официальный Encar…» |
| Путаница манвон vs «под ключ» | H2 «Выпишите пять полей…» |
| «Без ДТП» ≠ чистый кузов | H2 схема X/W + FAQ |
| Депозит до отчёта | H2 чеклист стоп + красные флаги |

## Link verify

- total unique: 3; failed hard: 0 after soft-pass
- soft_pass: `catalog_ssl` ×1 unique brand-twin catalog URL (2 CTA в тексте)
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблиц/схем)
- Flesch RU: 69.5

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: **можно** после Director handoff

## Optional (non-blocking)

1. **Ept02:** после publish соседних AS* — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** манвон×10 000, 30 дней/2000 км — дописать в fact-bank.
3. **slop over-long:** артефакт таблиц; не критично.

## Gate checklist

- score ≥ 80 → **91** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass (incl. soft) ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice CLI PASS ✓  
- beginner-fit PASS ✓  
- insight label skill → **PASS** ✓  

**Итог:** PASS — Director может запускать cover \|\| schema.
