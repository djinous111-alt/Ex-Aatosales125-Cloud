# Article QA — B02

**topic_id:** B02  
**slug:** kak-podobrat-zapchasti-na-kitajskoe-avto-po-vin-2026  
**article_dir:** memory/blog/articles/B02-kak-podobrat-zapchasti-na-kitajskoe-avto-po-vin-2026  
**date:** 2026-10-13  
**verdict:** PASS  
**score:** 87

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Заказал «колодки как у Jolion» по модели/году → приехали не те; машина стоит, деньги на возврате |
| Где решение | H2: когда нужен полный VIN; сверка VIN→OEM; оригинал/аналог/разбор; каналы РФ; чек-лист 10 пунктов до оплаты |
| Первый результат | Сегодня: фото VIN + сверка с ПТС + запрос OEM + фото детали; пакет до оплаты без сервиса |
| Термины «на пальцах» | VIN (17 знаков, табличка/ПТС), OEM («паспортный номер» запчасти), оригинал / аналог / разбор, EPC |

**Beginner-fit:** PASS — пошаговые ol, таблицы, «Делать / Не делайте», без профиля механика/разработчика.

**Angle vs WP 3296:** aftermarket заказ детали на уже своё авто; явно отстроено от «проверки машины до покупки кузова». Нет ОТТС/ЭПТС/сертификатов до покупки.

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date 2026-10-13; pain/outcome/voice OK |
| utility gate | PASS | action 35, pain 13, outcome 12; FAQ×6, tables×2 |
| human-voice gate | PASS | `human-voice-report.json`; story/pain/outcome overlap OK |
| fact-check | PASS | 7 extracted; 1 verified (2026); years/ISO/1688 — soft unverified |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из env |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 7 over-long (склейка таблиц/списков); Flesch RU 67.4 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues; live WP 3296 — ручной angle check OK |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1/description; H2/FAQ; нет 2–3 blog internal |
| GEO / citability | 23/25 | TL;DR, workflow, таблицы, FAQ×6, чек-лист 10 |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop hits |
| Fact safety | 12/15 | Нет цен/%; soft unverified years/ISO vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9530 символов, CTA без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «запчасти на китайские автомобили» в title / H1 / meta |
| C02 | ✓ | Lead: боль Jolion + чек-лист VIN→OEM→канал→10 пунктов |
| C03 | ✓ | Владелец Haval/Geely/Changan, деталь уже нужна |
| C04 | ✓ | VIN, OEM, оригинал/аналог/разбор объяснены |
| O01 | ✓ | H2 = research outline (VIN scope → сверка → тип детали → каналы → чек-лист → аптечка → сегодня) |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы + workflow blockquote, mode B |
| R01 | ✓ | TL;DR, workflow, «Коротко», success после чек-листа |
| R02 | ✓ | GOODVIN/EPC, бедность каталогов, ISO 3779 / GB 16735 в research-notes |
| R03 | ✓ | Нет фиксированных цен/% лотов |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Aftermarket VIN-чек-лист; отстройка от WP 3296 |
| E02 | ✓ | «Делать / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс; human-voice PASS |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Каталог может врать; подделки; возврат из Китая почти невозможен |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 7 (артефакт таблиц/списков парсером)
- Flesch RU: 67.4

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требовался: все обязательные gates PASS с первого прогона

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних B-статей — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** ISO 3779 / GB 16735 / «5 минут» — при желании дописать в fact-bank.
3. **slop over-long:** артефакт таблиц; правки не критичны.
4. **Ярлык TL;DR:** skill GEO упоминает запрет шаблонного «TL;DR / Быстрый инсайт», writer-контракт и PASS-статьи (AS09) используют его; human-voice PASS — не блокер.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
