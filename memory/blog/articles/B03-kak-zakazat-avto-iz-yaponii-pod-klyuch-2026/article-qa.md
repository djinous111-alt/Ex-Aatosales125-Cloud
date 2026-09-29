# Article QA — B03

**topic_id:** B03  
**slug:** kak-zakazat-avto-iz-yaponii-pod-klyuch-2026  
**article_dir:** memory/blog/articles/B03-kak-zakazat-avto-iz-yaponii-pod-klyuch-2026  
**date:** 2026-09-30  
**verdict:** PASS  
**score:** 90

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN: technical topic without official docs URL |
| utility gate | PASS | action 21; pain 4; outcome 6; FAQ×6; table×1 |
| human-voice-gate | PASS | WARN: multiple exactly-5-step lists |
| fact-check | PASS | 6 stats; verified 3; unverified 3 (5 лет, 160, 1713 — есть в research-notes) |
| link-verify | PASS | 5/5 OK (catalog, Telegram, 3 internal relative) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка table/blockquote парсером); Flesch RU 61.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Pain / solution / beginner-fit

| Критерий | Статус | Где в статье |
|----------|--------|--------------|
| Боль новичка в lead | PASS | Депозит без сметы/листа; «под ключ» = дырявая смета |
| Решение в H2 | PASS | Смета → бюджет → лист → договор/7 вопросов → Владивосток → приёмка → чек-лист |
| Понятный результат до FAQ | PASS | H2 чек-лист + blockquote «Что изменится после этих шагов» |
| Термины «на пальцах» | PASS | СВХ, СБКТС, ЭПТС, утильсбор, аукционный лист, «под ключ» |
| Первый безопасный шаг | PASS | Три цифры до ставки; нет сметы/перевода листа — нет депозита |
| Beginner-fit | PASS | Не для перекупов; без API/проф-жаргона без объяснения |

**Боль:** новичок боится дырявой сметы «под ключ» и потери депозита.  
**Решение:** таблица этапов + 7 вопросов до оплаты + правило по аукционному листу + маршрут Владивосток.  
**Первый результат:** чек-лист первого заказа и три цифры до ставки (возраст, объём/мощность, бюджет до города).

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary «заказ авто из японии» в title/H1; H2 how-to; CTA catalog×2 + Telegram×1; 3 internal |
| GEO / citability | 24/25 | Insight, схемы, таблица этапов, FAQ×6, чек-лист результата |
| CORE-EEAT lite | 15/15 | 20/20 |
| Human voice | 14/15 | PASS gate; WARN на 3 списка ровно по 5 пунктов |
| Fact safety | 13/15 | Факты в research-notes; 3 soft unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9468 символов, FAQ, CTA, без форм |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 20/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в title / H1 |
| C02 | ✓ | Lead — боль + прямой маршрут без «в этой статье» |
| C03 | ✓ | Новичок, первый заказ из Японии |
| C04 | ✓ | СВХ / СБКТС / ЭПТС / утильсбор / аукционный лист объяснены |
| O01 | ✓ | H2 = action_outline research |
| O02 | ✓ | Логичный путь от сметы до выдачи |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + схемы, mode B |
| R01 | ✓ | Insight, схемы, FAQ, блок результата |
| R02 | ✓ | 5–10 суток СВХ; 160 л.с./льгота; закрытость аукционов — в research-notes |
| R03 | ✓ | Нет готовых сумм пошлин; расчёт → каталог |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол Авто-Сейлс: за руку от сметы до выдачи |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Депозит, СВХ-простой, льготный утиль, подделка листа |
| Ept02 | ✓ | Internal: аукционный лист, проходные авто, СВХ Владивосток |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 5, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схем + lead/достоверность)
- Flesch RU: 61.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Editorial insight label:** blockquote начинается с `TL;DR / Быстрый инсайт` — skill предпочитает без шаблонного ярлыка; linter не блокирует. Writer в след. цикле может переименовать в нейтральный заголовок.
2. **human-voice WARN:** 3 списка ровно по 5 пунктов — варьировать длину списков.
3. **fact-check soft:** дописать в fact-bank «5 лет / проходность», «160 л.с.», «ПП №1713».
4. **slop over-long:** в основном склейка table/blockquote парсером; правки не критичны.
5. **Telegram href:** в HTML литерал `[REDACTED]` + pragma — для secret-scan; убедиться, что publish подставит реальный URL.

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **20/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
