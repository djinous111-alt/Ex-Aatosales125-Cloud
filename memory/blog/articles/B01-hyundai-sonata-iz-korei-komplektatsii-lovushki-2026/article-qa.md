# Article QA — B01

**topic_id:** B01  
**slug:** hyundai-sonata-iz-korei-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-hyundai-sonata-iz-korei-komplektatsii-lovushki-2026  
**date:** 2026-10-23  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-23; source_table 27; pain/outcome/voice OK |
| fact-check | PASS | 10 stats; 1 verified (2026); 9 unverified vs fact-bank — есть в research-notes (ФНС 160 л.с., DN8/The Edge, LPG rental) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 0 over-long; Flesch RU 73.3 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 18; pain 11; outcome 12; FAQ×6; table×1; ol/ul OK |
| human-voice | PASS | human-voice-report.json PASS; warn: 2× exactly-5-step lists |

## Beginner-fit / pain → solution → result

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит «по красивому Premium/Inspiration», пока в карточке мелко 1.6T 180 л.с. или LPG rental |
| Где решение | H2: задача → мотор/160 л.с. → бензин vs LPi → trim по фото → история → чек-лист 10 пунктов |
| Первый результат | Заполненный чеклист с вердиктом «можно платить / стоп» до перевода |
| Термины «на пальцах» | Encar, Trust Encar/Carhistory, LPi vs rental, порог 160 л.с., trim The Edge |

**beginner-fit:** PASS (how-to до депозита, без профи-жаргона без пояснений)

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «соната из кореи» в title/H1/meta; H2 how-to; CTA каталог×2 + Telegram; мало internal blog links |
| GEO / citability | 23/25 | Insight-box, таблица моторов, FAQ×6, чеклист×10, стоп-правила |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | 0 AI-slop; warn про два списка ровно из 5 шагов |
| Fact safety | 12/15 | Цифры утиля/мощности в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8556 символов, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «соната из кореи» в meta title / H1 |
| C02 | ✓ | Lead — прямой ответ: стоп до депозита, фильтр по мощности/газу/trim |
| C03 | ✓ | Читатель: первая Sonata из Кореи, риск депозита |
| C04 | ✓ | Encar / Trust / Carhistory / LPi / rental объяснены |
| O01 | ✓ | H2 = outline research (задача → мотор → газ → trim → история → чеклист → next → FAQ) |
| O02 | ✓ | Логичный how-to |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote, mode B |
| R01 | ✓ | Insight-box, стоп-правила, критерий успеха, FAQ |
| R02 | ✓ | 01.12.2025 / 160 л.с. / 3400–5200 ₽ / ~146–180–290 л.с. в research-notes |
| R03 | ✓ | Нет самодельного калькулятора пошлин; коммерческий тариф без ложных точных сумм «в уме» |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + ловушка турбо/объём |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Vladivostok hub |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: rental LPG, hybrid суммарная мощность, осмотр до оплаты |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 0
- Flesch RU: 73.3

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все gates PASS с первого прогона)

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 01.12.2025 / 3400–5200 ₽ / мощности Sonata — дописать в fact-bank.
3. **human-voice warn:** варьировать длину списков (сейчас 2× ровно 5 шагов).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
