# Article QA — AS13

**topic_id:** AS13  
**slug:** chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS13-chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-01  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | re-check; research_date=2026-11-01; sources/pain/outcome OK |
| utility gate | PASS | article gate; action 27 / pain 7 / outcome 9; FAQ×7; table×1 |
| human-voice gate | PASS | `human-voice-report.json`; warn: multiple exactly-5-step lists (non-blocking) |
| fact-check | PASS | 15 extracted; 2 verified in fact-bank; 13 soft unverified — numbers in research-notes (Chery CN 79900–91900 / 4530×1862×1695 / 2670; ZOL 156/115; Drom/МироМобиль 197; AutoProfi 180 дней; Kolesa 2720) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING→accept | 0 клише; 6 over-long (склейка table/blockquote парсером); Flesch RU 74.5 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary how-to в title/H1; H2 checklist; CTA каталог×3 + Telegram×1; нет 2–3 blog internal |
| GEO / citability | 24/25 | Инсайт-блок, схема до денег, таблица ярлыков, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; 0 AI-opening; pain/outcome markers OK |
| Fact safety | 13/15 | Цифры в research-notes; soft vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; char_count 9484 (8500–9500); FAQ; CTA; без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать тигго 7 про из китая» в meta/H1 |
| C02 | ✓ | Lead: боль депозита без VIN → чеклист + результат «заявлено vs факт» |
| C03 | ✓ | Читатель: новичок, заказ из Китая до депозита |
| C04 | ✓ | CVT, 7DCT, ADAS, VIN, 180 дней объяснены «на пальцах» |
| O01 | ✓ | H2 = задача → имена → VIN/мотор → опции → 180 дней → чеклист → дальше |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + blockquote; mode B |
| R01 | ✓ | Инсайт + схема + FAQ |
| R02 | ✓ | Chery CN / Дром / Колёса / AutoProfi в research-notes |
| R03 | ✓ | Нет ложных «цен под ключ»; смету после фактов |
| R04 | ✓ | FAQ отвечает с первого предложения |
| E01 | ✓ | Угол «до депозита» + отсев Jaecoo/High Energy/7L |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×3 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Стоп без VIN/пакета документов; отличие рынков CN/РФ |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit: PASS

- **Боль новичка:** депозит по объявлению «Tiggo 7 Pro Max полный фарш» без VIN → чужой мотор/опции или Jaecoo.
- **Где решение:** H2 про имена, VIN/мотор/коробку, опции на видео, пакет 180 дней, финальный чеклист до депозита.
- **Первый результат:** таблица «заявлено vs факт» + стоп перевода, пока пакет не собран.
- **Термины на пальцах:** VIN, CVT vs «автомат»/7DCT, ADAS, правило 180 дней, High Energy = Jaecoo J7.

## Pain / solution map

| Элемент | Статус |
|---------|--------|
| Lead называет боль | ✓ депозит без VIN / чужая табличка |
| H2 дают решения | ✓ имена → железо → опции → 180 дней → чеклист |
| Результат до FAQ | ✓ критерий успеха + чеклист + «Что дальше» |
| Не повтор Tiggo 8 Pro | ✓ FAQ + lead явно разводят |

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт table/blockquote)
- Flesch RU: 74.5

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Voice/skill: ярлык инсайта `TL;DR / Быстрый инсайт` → `Инсайт до депозита` (skill geo-qa запрещает шаблонный TL;DR; writing-contract example всё ещё показывает старый ярлык). Повтор human-voice / html-linter / utility: PASS. `char_count` meta → 9484.

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** дописать ключевые цифры (79900–91900 CNY, 156/115, 197, 2670/2720, 180 дней) в fact-bank.
3. **human-voice warn:** варьировать длину step-list (сейчас несколько ровно из 5 пунктов).
4. **slop over-long:** артефакт парсера таблиц; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
