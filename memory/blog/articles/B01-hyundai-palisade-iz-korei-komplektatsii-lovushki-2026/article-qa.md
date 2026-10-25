# Article QA — B01

**topic_id:** B01  
**slug:** hyundai-palisade-iz-korei-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-hyundai-palisade-iz-korei-komplektatsii-lovushki-2026  
**date:** 2026-10-25  
**verdict:** PASS  
**score:** 88

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Хочет Palisade Calligraphy «из Кореи», не знает про лимит вывоза >2 000 см³; рискует депозитом на серую схему через KZ/KG |
| Где решение | H2: лимит моторов → комплектации без «блеска» → Encar/Carhistory → серые стоп-сигналы → легальный план Б → чеклист 10 пунктов |
| Первый результат | До депозита: см³ записан, серая схема отсеяна, есть план Б (Carnival/Santa Fe Hybrid / Япония / вторичка РФ) |
| Термины «на пальцах» | см³ vs «2.5»; Encar; Carhistory; Encar진단; лимит 2 000; льготный утиль vs вывоз |
| Beginner-fit | PASS — тон для семьи/заказчика авто, не для разработчиков; есть безопасный первый шаг без «команды» |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=today; sources/pain_map OK |
| utility gate | PASS | action 35 / pain 10 / outcome 13; FAQ×7; tables×2 |
| human-voice-gate | PASS | human-voice-report.json status PASS; concrete + story overlap |
| fact-check | PASS | 14 extracted; 2 verified / 12 unverified vs fact-bank (в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); failed_count=0 |
| html-linter | PASS | 0 errors; whitelist; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 7 over-long; Flesch RU 72.1 Easy — не blocker |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «хендай палисад из кореи» в title/H1; H2/FAQ; CTA каталог+TG; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, схема, 2 таблицы, FAQ×7, чеклист 10 |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | gate PASS; story/pain/outcome overlap |
| Fact safety | 12/15 | Ключевые цифры в research-notes; мало в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9359 зн., FAQ, CTA, без форм/`pre`/`code` |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead сразу называет боль депозита + лимит >2,0 л |
| C03 | ✓ | Читатель: семья / заказ Palisade из Кореи |
| C04 | ✓ | см³, Encar, Carhistory, серые схемы объяснены |
| O01 | ✓ | H2 = pain→solution outline research |
| O02 | ✓ | Логичный маршрут до депозита |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + 2 таблицы + чеклист; mode B |
| R01 | ✓ | TL;DR, схема, вердикт, FAQ |
| R02 | ✓ | 24.02.2024, 2497 см³, 179,6 млрд вон — в research-notes |
| R03 | ✓ | Нет статичного калькулятора пошлин; суммы «персонально в каталоге» |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «разговор до перевода денег» |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person hero |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты вывоза, лаг диагностики, серые риски |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 → **18/20** ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 7 (мягкий WARNING; читаемость Easy)
- Flesch RU: 72.1

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты/шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все обязательные gates PASS с первой проверки)

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** ключевые цифры (2497 / 2000 / 24.02.2024 / 179,6 млрд) — в fact-bank для verified↑.
3. **slop over-long:** 7 длинных предложений — по желанию укоротить в следующем рерайте.
4. **docs drift (наблюдение):** writing-contract требует ярлык `TL;DR / Быстрый инсайт`, skill geo-qa формулирует запрет того же ярлыка; gates/contract побеждают — skill стоит выровнять fixer’ом.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
