# Article QA — B03

**topic_id:** B03  
**slug:** avto-iz-korei-ili-kitaya-2026  
**article_dir:** memory/blog/articles/B03-avto-iz-korei-ili-kitaya-2026  
**date:** 2026-07-24  
**verdict:** PASS  
**score:** 87  
**author_id:** avtosales-editorial  
**article_mode:** B  
**char_count:** ~9225

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Застрял между Кореей и Китаем под один бюджет; боится депозита без проверок и правила ~180 дней (lead: Антон / 2,8 млн / «внесите депозит сегодня») |
| Где решение | H2: бюджет «под ключ» → Корея/Encar → Китай/регистрация → таблица сравнения → сценарии → чек-лист 10 → план на сегодня |
| Первый результат до FAQ | Потолок бюджета + страна с фразой «почему» + чек-лист 10 пунктов + путь в каталог за расчётом |
| Термины «на пальцах» | Encar, VIN, Performance Check, правило ~180 дней (дата регистрации ≠ завод), СБКТС/ЭПТС, СВХ |
| Beginner-fit | **PASS** — не для профи/разработчиков; первый безопасный шаг до депозита; без требования «команды аукционов» |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: false technical_topic (github/mcp markers) |
| utility gate | PASS | action 19; pain 4; outcome 12; FAQ×7; tables×2; ol×10 |
| human-voice-gate | PASS | `human-voice-report.json`; story/pain/outcome overlap OK |
| fact-check | PASS | 6 stats; verified 2 (2026); unverified: 180 дней / 5 лет / 160 л.с. — есть в research-notes |
| link-verify | PASS | 4/4 OK после GET-fallback на HEAD 502 (kolesa.kz) |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (склейка таблиц/схем); Flesch RU 59.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «авто из кореи или китая» в H1/meta; H2 how-to; 1 internal blog + каталог×2 + Telegram |
| GEO / citability | 23/25 | Инсайт-блок, 2 таблицы, FAQ×7, чек-лист 10, схема шагов |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; slop 0 |
| Fact safety | 12/15 | 180/160 не в fact-bank, но backed research + внешняя ссылка |
| Contract HTML | 10/10 | Whitelist PASS; CTA pragma; без форм/цен лотов/pre/code |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в H1 / title_seo |
| C02 | ✓ | Lead: боль + прямой framing сравнения до депозита |
| C03 | ✓ | Новичок / один бюджет / до депозита |
| C04 | ✓ | Encar, VIN, 180 дней, СБКТС/ЭПТС объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный порядок до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol + 2 таблицы, mode B |
| R01 | ✓ | Инсайт, схема, таблицы, FAQ |
| R02 | ✓ | Kolesa.kz + research evidence на 180 дней |
| R03 | ✓ | Нет цен лотов / статичного калькулятора |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол KR vs CN comparison only |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | Каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон редакции Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски: депозит без пакета, путаница даты регистрации, утильсбор/л.с. |
| Ept02 | ✗ | Только 1 internal blog link (Trust Encar); желательно 2–3 |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 4, failed: 0
- internal blog AS09 Trust Encar: 200 HEAD
- kolesa.kz: 200 GET (HEAD 502 → fallback)
- catalog + Telegram: 200 HEAD
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблиц/схем)
- Flesch RU: 59.1

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклист/план) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. link-verify FAIL на kolesa.kz HEAD 502 при живом GET → патч `scripts/excalibur_blog_link_verify.py` (GET-fallback на 502/503/504). Повтор: PASS.

## FIX (non-blocking / optional)

1. **Ept02:** добавить 2-й internal blog link (напр. доставка Владивосток / Япония as contrast) с `anchor_variants`.
2. **fact-bank soft:** дописать «~180 дней регистрации КНР с 01.01.2026» и эвристику ~160 л.с. утильсбора.
3. **slop over-long:** артефакт парсера таблиц; правки не критичны.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-gate PASS ✓  
- beginner-fit PASS ✓  
- link-verify pass ✓  

**Итог:** PASS — можно cover || schema.
