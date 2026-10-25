# Article QA — B01

**topic_id:** B01  
**slug:** toyota-noah-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-noah-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-26  
**verdict:** PASS  
**score:** 89

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | confirm; warning: technical_topic false-positive (нет official docs URL) |
| fact-check | PASS | 4 stats; 1 verified (2026); 2014/2021/2022 unverified vs fact-bank — есть в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram); failed=0 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (lead + склейка таблиц парсером); Flesch RU 72.8 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 28; FAQ×6; tables×2; pain/outcome OK |
| human voice gate | PASS | human-voice-report.json; overlap pain/outcome/voice/surprising OK |

## Beginner-fit

**PASS.** Статья для семьи/первого импорта, не для профи-разработчиков. Термины R80/R90, ZWR/MZRA, Si vs S-Z, A/U/W/X/XX, E-Four, оценка R/RA объяснены «на пальцах». Первый безопасный шаг: сценарий семьи на бумаге → сверка кода → лист до ставки.

## Pain → solution → result

| Элемент | Где |
|---------|-----|
| Боль новичка | Lead: путаница R80/R90 и Si/S-Z + страх ставки при XX/R в листе |
| Решение | H2: сценарий → код кузова → комплектации → Noah vs Voxy → чтение листа → путь Япония→Влад |
| Первый результат | H2 «чеклист из 10 пунктов» + формулировка запроса менеджеру до FAQ |
| Успех | Заполненный чеклист; без готовых сумм пошлин |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «тойота ноах из японии» в title/H1; H2/H3; CTA; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, таблицы×2, FAQ×6, чеклисты, схема чтения листа |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | 0 AI-slop hits; HV gate PASS |
| Fact safety | 13/15 | Годы кузова в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9487 знаков, FAQ, CTA, без форм |
| **Итого** | **89/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead → чеклист до ставки |
| C03 | ✓ | Читатель: семья, импорт Noah |
| C04 | ✓ | R80/R90, грейды, лист объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблицы, mode B |
| R01 | ✓ | TL;DR, схема листа, FAQ |
| R02 | ✓ | Годы/коды из research-notes |
| R03 | ✓ | Нет цен лотов/%; пошлины → импортёр |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «до ставки» + Владивосток |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×3 + Telegram |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: XX≠R; пошлины не в статье |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблиц/списков + lead)
- Flesch RU: 72.8

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требовался (все обязательные gates PASS с первого прогона)

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** годы R80/R90 (2014–2021, 2022) — дописать в fact-bank.
3. **slop over-long:** артефакт парсера таблиц; правки не критичны.

## Gate

- score ≥ 80 → **89** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
