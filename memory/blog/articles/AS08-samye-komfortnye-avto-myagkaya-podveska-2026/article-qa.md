# Article QA — AS08

**topic_id:** AS08  
**slug:** samye-komfortnye-avto-myagkaya-podveska-2026  
**article_dir:** memory/blog/articles/AS08-samye-komfortnye-avto-myagkaya-podveska-2026  
**date:** 2026-07-17  
**verdict:** PASS  
**score:** 86

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| fact-check | PASS | 3 stats; 1 verified (2026); 2 unverified (200 / 210 мм клиренс) — есть в research-notes (Favorit/Geely), не в fact-bank |
| link-verify | PASS | 2/2 OK (`avto-sales125.ru`, `t.me/avtosales125`); `--site-base ${PUBLIC_SITE_URL}` |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long (в основном склейка таблиц/схем парсером); Flesch RU 55.2 |
| cannibalization | PASS | 0 issues (1 article meta в blog-dir) |
| utility gate | PASS | numbered lists, FAQ×6, tables×2, action markers OK |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «самые комфортные автомобили» в meta title / research H1 |
| C02 | ✓ | Первый абзац — прямой ответ, без «в этой статье» |
| C03 | ✓ | Читатель: заказ из Азии, комфорт на РФ-дорогах |
| C04 | ✓ | Энергоёмкость объяснена при первом появлении |
| O01 | ✓ | H2 = how-to / action_outline research |
| O02 | ✓ | Логичный outline критерии → проверка → классы → рынки → ошибки → чеклист → FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + чеклисты, mode B |
| R01 | ✓ | TL;DR, вердикт JP/KR/CN, FAQ-блоки |
| R02 | ✓ | Monjaro 210 мм + Highlander/Drom + Wordstat в research-notes |
| R03 | ✓ | Нет %/цен лотов |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол JP/KR/CN + чеклист, не топ-10 премиум |
| E02 | ✓ | «Делать / Не делать» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски пневмо/спорт-пакета/низкого профиля |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Blockers

- нет

## FIX (non-blocking / optional for next cycle)

1. **Ept02:** после появления/известных URL AS01–AS07 на `avtosales125.ru` — добавить 2–3 internal links с `anchor_variants` (не блокирует PASS).
2. **fact-check soft:** клиренс 200/210 мм — уже в research-notes; при желании дописать в fact-bank для полного verified.
3. **slop WARNING:** over-long в основном артефакт таблиц; правки не критичны.

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- utility gate PASS ✓  

**Итог:** PASS — можно cover || schema.
