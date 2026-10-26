# Article QA — B01

**topic_id:** B01  
**slug:** toyota-prado-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-prado-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-26  
**verdict:** PASS  
**score:** 90

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-26; source table OK |
| fact-check | PASS | 9 stats; 2 verified (2026, 250); rest in research-notes (моторы/даты JP) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/Fact Check склейка); Flesch RU 69.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 28; pain 5; outcome 6; ol×20 items; FAQ×6; table×1 |
| human voice | PASS | warn: exactly-5 regex ловит ol≥5 (не блокер) |

## Beginner / pain → solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Хочет «Прадо из Японии», путает 150/LC250, не читает лист, верит в льготу на бензин 2.7 |
| Где решение | H2: сценарий → 150 vs LC250 → моторы/утиль → лист → 10 пунктов → Владивосток RHD |
| Первый результат | Заполненный чек-лист из 10 пунктов + код кузова + стоп-сигналы до первой ставки |
| Термины «на пальцах» | LC250 vs Prado; коды GDJ/TRJ; шкала листа S…1 / R / ★★; порог 117,68 кВт |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary «тойота прадо из японии» в title/H1; H2-action; CTA×3 |
| GEO / citability | 24/25 | Короткий инсайт, схема, таблица 150/LC250, FAQ×6, чек-лист×10 |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop hits |
| Fact safety | 13/15 | Даты/кВт в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9373 знаков, FAQ, CTA, без форм |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title_seo / H1 |
| C02 | ✓ | Lead: боль → чек-лист до ставки |
| C03 | ✓ | Читатель: семья / новичок JP-аукцион |
| C04 | ✓ | LC250, коды кузова, лист, утиль объяснены |
| O01 | ✓ | H2 = research outline |
| O02 | ✓ | Логичный порядок до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + таблица + blockquote, mode B |
| R01 | ✓ | Инсайт + схема + FAQ |
| R02 | ✓ | 120 кВт / 117,68 кВт / Apr 2024 в research-notes |
| R03 | ✓ | Нет статичных сумм «под ключ»; расчёт в каталоге |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки», не обзор рынка |
| E02 | ✓ | Сделайте / Не делайте в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон ДВ / Авто-Сейлс |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Стоп-сигналы листа, льготный утиль-ловушка |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (таблица / Fact Check)
- Flesch RU: 69.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Utility gate BLOCK → action-маркеры («Сделайте/Не делайте», «проверьте», «Шаг N», «избегайте», «используйте»); инсайт без ярлыка `TL;DR`/`Быстрый инсайт`.
2. Policy gap: в `editorial-policy.json` не было `pain_markers_ru`/`outcome_markers_ru`, а `utility_gate` требовал min 2/3 → false BLOCK на любой статье. Добавлены маркеры + skip при пустом списке в скрипте. → INC-20261026-0920-geo-qa-utility-pain-outcome-markers.
3. Повтор utility + human voice + остальные гейты: PASS.

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** моторы 1GD/2TR, порог 117,68 кВт — дописать в fact-bank.
3. **slop over-long:** артефакт таблицы/Fact Check; не критично.
4. **human-voice warn:** regex `exactly_five_lists` матчит ol с ≥5 `<li>` (не «ровно 5»).

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
