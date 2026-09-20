# Article QA — AS10

**topic_id:** AS10  
**slug:** hyundai-avante-iz-korei-kak-vybrat-2026  
**article_dir:** memory/blog/articles/AS10-hyundai-avante-iz-korei-kak-vybrat-2026  
**date:** 2026-07-22  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes gate | PASS | research_date=2026-07-22; technical_topic=false |
| fact-check | PASS | 7 stats; 1 verified (2026); 6 unverified (л.с./сроки) — в research-notes |
| link-verify | PASS | 3/3 OK (internal Trust Encar + catalog + Telegram) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/чеклист/достоверность); Flesch RU 79.7 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 22; pain 3; outcome 5; ol 14; FAQ×6; table×1 |
| human voice gate | PASS | pain/outcome/concrete OK; warn: 2× exactly-5-step lists |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит за N-Line/турбо без понимания л.с., Smart/Modern/Inspiration и кодов X/W → риск утильсбора |
| Где решение | H2: мощность ≤160 → тримы → Avante≠реклама CN8 → Performance Check → путь Владивосток → чеклист |
| Первый результат | Shortlist 2–3 лота в льготной зоне + пакет проверок до депозита; смета в каталоге |
| Термины «на пальцах» | Утиль/л.с., N Line vs N, Avante=Elantra, Performance Check X/W, ЭПТС/СБКТС |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «хендай аванте из кореи» в title/H1/lead; H2 actionable; 1 blog internal + CTA |
| GEO / citability | 23/25 | Insight-блок, таблица моторов, схема →, FAQ×6, чеклист 12 |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop |
| Fact safety | 12/15 | Мощности/даты в research; soft unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8667 зн., FAQ, CTA без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 / lead |
| C02 | ✓ | Lead: ошибка депозита за «спорт» без л.с. |
| C03 | ✓ | Читатель: новичок после Соляриса, заказ из Кореи |
| C04 | ✓ | л.с., тримы, X/W, Avante/Elantra объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный how-to до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + ul чеклист + table + workflow → |
| R01 | ✓ | Insight + схема до депозита + FAQ |
| R02 | ✓ | Busan 26.06.2026, ориентиры л.с., сроки с оговоркой |
| R03 | ✓ | Нет самодельных сумм утиля/%; смета только в каталоге |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + отсев турбо/N |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person кейса |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: сроки плавают, X=стоп, утиль только в каталоге |
| Ept02 | ✗ | Только 1 internal blog link (Trust Encar); желательно 2–3 |
| Exp04 soft | ✗ | Insight начинается с ярлыка `TL;DR / Быстрый инсайт` (skill: избегать) — не blocker скриптов |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/чеклиста)
- Flesch RU: 79.7

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (ol + чеклист) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (utility gate false-BLOCK из пустых `pain_markers_ru`/`outcome_markers_ru` в policy снят в этом run — см. incident)

## FIX cycle (QA)

1. Utility gate BLOCK (pain=0/outcome=0 при пустых списках в policy) → дописаны маркеры в `editorial-policy.json` + harden script; повтор: PASS. Longread writer не переписывался.

## FIX (non-blocking / optional)

1. **Ept02:** ещё 1–2 internal links на смежные AS-посты с `anchor_variants`.
2. **Insight label:** убрать шаблонный префикс `TL;DR / Быстрый инсайт:` (оставить смысл блока).
3. **human-voice warn:** разная длина списков (не два раза ровно 5 пунктов).
4. **fact-check soft:** мощности 123/160/204/280 и 20–45 дней — в fact-bank при желании verified.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
