# Article QA — AS14

**topic_id:** AS14  
**slug:** jaecoo-j7-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS14-jaecoo-j7-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-02  
**verdict:** PASS  
**score:** 88  
**beginner_fit:** PASS

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Перепутать Explore 06 / Jaecoo J7, привод 2WD/4WD или «Престиж по скрину» и отдать депозит за не ту машину |
| Где решение | H2: задача+привод → паспорт trim Актив/Комфорт/Престиж → красные флаги VIN/ПО → смета без магической цифры → чеклист документов |
| Первый результат до FAQ | В заметках: привод+мощность+уровень+must-have; договор/смета без одной цифры; решение ставлю/жду/отказ; депозит ещё не отправлен |
| Термины «на пальцах» | Explore 06 / Tansuo 06 = J7; 2WD 150 vs 4WD 186 и клиренс; CN-trim ≠ РФ-имя; VIN; SHS/PHEV только передний привод |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-11-02; sources/pain_solution/action_outline OK |
| fact-check | PASS | 6 stats; 1 verified (2026); 5 soft unverified (150/186/196/540/60 дней) — все в research-notes (JAECOO PDF / Avtogermes / Auto.ru / Drom / auto-geek) |
| link-verify | PASS | 3/3 OK (каталог, Telegram, internal China checklist); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK; insight «Коротко до депозита» (не TL;DR) |
| slop-detector | WARNING | 0 клише; 9 over-long (склейка таблиц/списков/схем парсером); Flesch RU 65.9 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |
| utility gate | PASS | ol×8, FAQ×6, table×1, action 13 / pain 6 / outcome 10 |
| human-voice-gate | PASS | reader_story/pain/outcome/success/voice/surprising overlap OK; 0 AI openings |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в H1/title; 1 blog internal + CTA catalog×2 / Telegram×1 |
| GEO / citability | 24/25 | Insight-блок, таблица 2WD/4WD, схемы, FAQ×6, чеклист |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice PASS; 0 slop hits |
| Fact safety | 12/15 | Soft unverified vs fact-bank; опора в research-notes + блок «Материал проверен» |
| Contract HTML | 10/10 | Whitelist PASS; char_count 9039; author `avtosales-editorial`; без форм/MCP URL |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать jaecoo j7 из китая» в H1 / meta title |
| C02 | ✓ | Lead: боль + «сначала чеклист, потом деньги» без «в этой статье» |
| C03 | ✓ | Новичок под заказ из Китая через Владивосток |
| C04 | ✓ | Explore 06 / Tansuo 06, 2WD/4WD, CN-trim, VIN, SHS/PHEV объяснены |
| O01 | ✓ | H2 = action_outline research |
| O02 | ✓ | Задача → trim → флаги → смета → документы → FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + схемы, mode B |
| R01 | ✓ | Insight, workflow, критерий результата, FAQ |
| R02 | ✓ | Клиренс 196/186 + линейка 150/186 в research-notes |
| R03 | ✓ | Нет цен лотов/%; сроки 30–60 как ориентир договора |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол до депозита + Explore 06=J7 + клиренс 4WD ниже |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B; опыт редакции, без fake «я купил» |
| Exp02 | ✓ | Тон research / Авто-Сейлс у роллкера |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Красные флаги: trim/скрин, карта физлица, VIN, гибрид |
| Ept02 | ✗ | 1 internal blog link (гайд депозита); мало 2–3 из карточки темы |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Author / contract

- `author_id`: avtosales-editorial → registry OK («Редакция Авто-Сейлс»)
- insight label: **Коротко до депозита** (не TL;DR / «Быстрый инсайт»)
- MCP URLs: нет

## Link verify

- total: 3, failed: 0  
- see `link-verify.json`

## AI-slop scan

- cliches: 0  
- over-long: 9 (артефакт таблицы/списков)  
- Flesch RU: 65.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклист ol) | Review: no | Author SameAs: pending schema agent

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все gate PASS с первого прогона; article.html не правился)

## FIX (non-blocking / optional)

1. **Ept02:** после известных URL соседних AS/B-постов — ещё 1–2 internal links с `anchor_variants`.
2. **fact-check soft:** 150/186 л.с., клиренс 196/186, камеры 540, 30–60 дней — дописать в fact-bank.
3. **slop WARNING:** over-long от склейки table/ul; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
