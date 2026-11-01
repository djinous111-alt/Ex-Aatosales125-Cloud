# Article QA — AS12

**topic_id:** AS12  
**slug:** jetour-t2-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS12-jetour-t2-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-01  
**verdict:** PASS  
**score:** 88  
**beginner_fit:** PASS

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-11-01; sources/pain_map OK |
| fact-check | PASS | 6 stats; verified 2 (2026); unverified 245/220/700/160 — в research-notes (JETOUR RU pricelist / VC.ru) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из `PUBLIC_SITE_URL` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (склейка table/blockquote парсером); Flesch RU 74.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 17 / pain 5 / outcome 11; FAQ×6; table×1; ol 8 items |
| human-voice | PASS | errors=[]; warnings=[]; `-o human-voice-report.json` (filename-only) |

## Pain → solution → result

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит по витринному имени (Discovery / «как у дилера»), а железо другое (1.5T FWD Exploration) |
| Где решение | H2: сверка РФ Люкс/Престиж/Премиум vs китайские пакеты; договор мотор/КПП/привод; чек-лист фото/доков |
| Первый результат | Одностраничный бриф в чате до перевода денег (критерий успеха перед FAQ) |
| Термины «на пальцах» | 7DCT (робот), 8AT (гидроавтомат), XWD/AWD, C-DM, СБКТС, ЭПТС |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «джетур т2 комплектации» в meta; H1/H2; CTA каталог×2 + Telegram×1; нет 2–3 blog internals |
| GEO / citability | 24/25 | Insight-блок, таблица соответствий, FAQ×6, чеклист ol, Fact Check Box |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | Gate PASS; 0 AI-slop hits |
| Fact safety | 13/15 | Числа в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8954 chars, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary query в title_seo / H1 про комплектации T2 |
| C02 | ✓ | Lead: боль депозита + прямой ответ «имя ≠ железо» |
| C03 | ✓ | Читатель: заказ T2 из Китая до депозита |
| C04 | ✓ | Люкс/Престиж/Премиум, Traveller, 7DCT/8AT объяснены |
| O01 | ✓ | H2 = how-to: стоп депозит → матрица → договор → Китай vs дилер → чеклист → расчёт |
| O02 | ✓ | Логичный outline без TOC-списка в теле |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote workflow, mode B |
| R01 | ✓ | «Коротко по делу», таблица, FAQ |
| R02 | ✓ | 245 л.с., клиренс 208–220, брод 700, порог 160 л.с. — в research-notes |
| R03 | ✓ | Нет розничных цен / готового утиля в теле |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + РФ vs Китай имена |
| E02 | ✓ | «Делать / Не делайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Автор Редакция Авто-Сейлс = registry `avtosales-editorial` |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: гарантия РФ, меню, смета, >160 л.с. |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт table/blockquote)
- Flesch RU: 74.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (текст статьи не правил; CLI артефакты перезаписаны корректно)

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних AS — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 245 / 220 / 700 / 160 — дописать в fact-bank для verified.
3. **slop over-long:** артефакт парсера таблицы; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research notes gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
