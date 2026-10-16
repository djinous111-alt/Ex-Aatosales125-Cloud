# Article QA — B01

**topic_id:** B01  
**slug:** nuzhna-li-era-glonass-pri-vvoze-avto-2026  
**article_dir:** memory/blog/articles/B01-nuzhna-li-era-glonass-pri-vvoze-avto-2026  
**date:** 2026-10-17  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: technical_topic без official docs URL (ложный tech-маркер — см. INC research) |
| utility gate | PASS | action_markers 34; pain 3; outcome 9; FAQ×7; table×1; ol 8 |
| human-voice-gate | PASS | human-voice-report.json; warn rhythm variance/avg=0.34 |
| fact-check | PASS | 5 stats; verified 1 (2026); unverified 4 (2027/2022/45 000/855) — в research-notes |
| link-verify | PASS | 3/3 OK (855.aoglonass.ru + каталог + Telegram) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (склейка таблицы/схем); Flesch RU 63.0 |
| cannibalization | PASS | 0 issues (3 meta в blog-dir) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Страх «сломать» растаможку из‑за заголовков про 1 апреля 2026 и лишней строки ЭРА в смете до депозита |
| Где решение | H2: правило до депозита → физ vs ИП/юр → страна не меняет правило → разбор сметы → чеклист 8 пунктов |
| Первый результат | Вслух: (1) физлицо для себя — кнопку не ставлю / (2) ИП/юр — ставлю через партнёра АО ГЛОНАСС; строка сметы вычеркнута или подтверждена |
| Термины «на пальцах» | УВЭОС / кнопка SOS / ЭРА-ГЛОНАСС; СБКТС ≠ кнопка; eCall и китайский SOS ≠ ГАИС ЭРА-ГЛОНАСС; ЭПТС; заявитель на таможне |

**beginner-fit:** PASS — без жаргона профи; первый безопасный шаг до депозита; альтернатива «через фирму» разобрана.

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «нужна ли эра глонасс» в title/H1; H2/H3; CTA; мало внутренних blog-links |
| GEO / citability | 24/25 | Коротко-блок, схема, таблица, FAQ×7, чеклист×8 |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice PASS; slop 0 |
| Fact safety | 12/15 | Даты/ПП в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9336 символов, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead + «Коротко» — прямой ответ физ/ИП на 2026-10-17 |
| C03 | ✓ | Читатель: ввоз из Азии, страх сметы/СВХ |
| C04 | ✓ | УВЭОС, СБКТС, ЭПТС, eCall объяснены |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица, mode B |
| R01 | ✓ | Коротко, схема, FAQ |
| R02 | ✓ | Минпромторг 27.03.2026, ПП №855, 01.10.2022 — в research-notes |
| R03 | ✓ | Нет калькулятора пошлин; 17–50 тыс. как ориентир рынка |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол checklist + миф 01.04.2026 |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог + Telegram + карта партнёров |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Мораторий может сдвинуться подписанным актом; перепроверка |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/схемы)
- Flesch RU: 63.0

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все gates PASS с первого прогона GEO QA)

## FIX (non-blocking / optional)

1. **Ept02:** после publish — 2–3 internal links на AS08/AS09 или era-glonass соседний пост с `anchor_variants`.
2. **fact-check soft:** 31.12.2027 / 01.10.2022 / ПП №855 / ориентир 17–50 тыс. — дописать в fact-bank.
3. **slop over-long:** артефакт таблицы; правки не критичны.
4. **human-voice warn:** paragraph rhythm variance 0.34 — косметика.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
