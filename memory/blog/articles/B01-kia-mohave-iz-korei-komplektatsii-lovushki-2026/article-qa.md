# Article QA — B01

**topic_id:** B01  
**slug:** kia-mohave-iz-korei-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-kia-mohave-iz-korei-komplektatsii-lovushki-2026  
**date:** 2026-10-21  
**verdict:** PASS  
**score:** 89  
**qa_cycle:** 2 (re-run after Writer FIX)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date OK; WARN: no obvious official docs URL (не блокер AVTO) |
| fact-check | PASS | 6 stats; 1 verified (2026); 5 unverified (2022, 3 лет, 257/260/160) — в research-notes |
| link-verify | PASS | 4/4 OK: AS08 + AS09 internal_absolute; catalog + Telegram external (HTTP 200) |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 4 over-long (склейка таблиц/схем); Flesch RU 78.9 |
| cannibalization | PASS | 0 issues (3 meta в blog-dir) |
| utility gate | PASS | action 34; pain 15; outcome 18; FAQ×6; tables×2 |
| human-voice gate | PASS | WARN: multiple exactly-5-step lists (regex ≥5) |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Encar-цена + слово Gravity + надежда на льготный утильсбор → депозит вслепую |
| Где решение | H2: места → Platinum/Masters/Gravity → стоп 160 л.с. → VIN/Carhistory → смета → чеклист 12 → shortlist |
| Первый результат | Лист выбора + чеклист без красных дыр + запрос живого расчёта до депозита |
| Термины «на пальцах» | Encar, VIN, Carhistory, утильсбор, СВХ, СБКТС, ЭПТС |

**beginner-fit:** PASS

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1/lead; H2 how-to; CTA живые; internal AS08/AS09 |
| GEO / citability | 23/25 | Инсайт «Коротко по делу», таблицы, FAQ×6, чеклист 12, схема денег |
| CORE-EEAT lite | 15/15 | 20/20 |
| Human voice | 14/15 | 0 slop; WARN 5-step lists |
| Fact safety | 12/15 | Пороги в notes; не все в fact-bank; без статичных сумм утильсбора |
| Contract HTML | 10/10 | Whitelist PASS, FAQ, CTA×3 env, internal×2, ~9481 chars, без форм |
| **Итого** | **89/100** | |

## CORE-EEAT lite: 20/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать киа мохаве из кореи» в meta/H1/lead |
| C02 | ✓ | Lead — боль + прямой ответ до депозита |
| C03 | ✓ | Читатель: заказ Mohave из Кореи |
| C04 | ✓ | Encar / Gravity / утильсбор / Carhistory объяснены |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный outline → FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + таблицы, mode B |
| R01 | ✓ | Инсайт, вердикт trim, стоп-правило, FAQ |
| R02 | ✓ | 257–260 / 160 / места 5–7 в research-notes |
| R03 | ✓ | Нет статичных сумм утильсбора / цен лотов |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Gravity≠максимум + чеклист до депозита |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 (живые URL) |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты Carhistory, СВХ, льготы |
| Ept02 | ✓ | Internal: AS09 Trust Encar + AS08 мягкая подвеска |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 4, failed: 0, verdict: pass
- kinds: internal_absolute×2 (AS08, AS09), external×2 (catalog, Telegram)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблиц/схем)
- Flesch RU: 78.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle history

1. Cycle 1 FIX: `href="[REDACTED]"` ×3 → Writer hydrated CATALOG_URL/TELEGRAM_URL; insight → «Коротко по делу»; + AS08/AS09 internals.
2. Cycle 2 re-run: all gates PASS.

## FIX (non-blocking / optional)

1. fact-bank: дописать 160 л.с. / ~257–260 л.с. Mohave.
2. human-voice WARN: варьировать размер списков.
3. Durable (fixer): запрет литерала `[REDACTED]` в article.html до GEO QA — см. INC-20261021-2135.

## Gate

- score ≥ 80 → **89** ✓  
- CORE-EEAT ≥ 16/20 → **20/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
