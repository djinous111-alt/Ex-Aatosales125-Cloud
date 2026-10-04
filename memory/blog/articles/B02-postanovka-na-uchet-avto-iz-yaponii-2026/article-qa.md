# Article QA — B02

**topic_id:** B02  
**slug:** postanovka-na-uchet-avto-iz-yaponii-2026  
**article_dir:** memory/blog/articles/B02-postanovka-na-uchet-avto-iz-yaponii-2026  
**date:** 2026-10-04  
**verdict:** PASS  
**score:** 87  
**human_voice:** PASS

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Lead: выписка ЭПТС есть, а в ГИБДД отказ из‑за «незавершённого» паспорта / утильсбора — день и запись сгорели |
| Где решение | H2: когда ехать → проверка ЭПТС «действующий» → пакет документов → ОСАГО+маркировки → Госуслуги → отказы → чек-лист |
| Первый результат до FAQ | Чек-лист «готов к номерам» + блок «Что изменится после чек-листа»: один визит до СТС/номеров |
| Термины «на пальцах» | СБКТС, ЭПТС, ПТД/ТПО, FRAME/VIN, МРЭО, госпошлина СТС/номера объяснены без жаргона профи |

**beginner-fit:** PASS

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-04; sources/pain_solution OK |
| utility gate | PASS | action 21; pain 5; outcome 5; faq×6; table×1 |
| human-voice gate | PASS | pain: боль/ошиб; outcome: проверьте/соберите/исправьте/выберите; warn: 4× exactly-5-step lists |
| fact-check | PASS | 10 extracted; 2 verified in fact-bank; 8 soft unverified (ставки/даты в research-notes) |
| link-verify | PASS | 2/2 OK после expand CATALOG_URL/TELEGRAM_URL → verify → re-redact |
| html-linter | PASS | 0 errors; whitelist; TOC нет |
| slop-detector | PASS | 0 клише; 4 over-long (TL;DR/таблица/достоверность — парсер); Flesch RU 62.3 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1/lead; H2 actionable; CTA×2; нет 2–3 internal blog links |
| GEO / citability | 23/25 | TL;DR, workflow, таблица документов, FAQ×6, чек-лист успеха |
| CORE-EEAT lite | 18/20 | см. ниже |
| Human voice | 14/15 | PASS gate; warn на одинаковые 5-step списки |
| Fact safety | 12/15 | ФЗ-283/пошлины/ОСАГО-ловушка в research; не всё в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9138 символов, mode B, FAQ, CTA без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «постановка на учет авто из японии» в title/H1/description |
| C02 | ✓ | Lead = прямой ответ: пакет + статус «действующий» до одного визита |
| C03 | ✓ | Читатель после СВХ/растаможки во Владивостоке |
| C04 | ✓ | ЭПТС/СБКТС/ПТД/ТПО объяснены |
| O01 | ✓ | H2 = research action outline |
| O02 | ✓ | Логичный порядок до окошка |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + workflow blockquote, mode B |
| R01 | ✓ | TL;DR + чек-лист + FAQ |
| R02 | ✓ | 10 дней ФЗ-283, пошлины с 01.09.2025, ОСАГО 1–3 дня активации |
| R03 | ✓ | Нет сумм утильсбора/пошлин ввоза; отсылка в каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «после таможни, до окошка» + ловушка ОСАГО |
| E02 | ✓ | «Делайте / Не делайте» + рекомендации |
| E03 | ✓ | CTA: Telegram + каталог (мягко) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон редакции Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Расхождение СМИ vs практика МРЭО по ОСАГО; срок синхронизации ЭПТС |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |
| Exp soft | ✗ | Human-voice warn: 4 списка ровно по 5 шагов |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0, verdict: pass
- see `link-verify.json` (CTA expand → verify → re-redact)

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт TL;DR/таблицы)
- Flesch RU: 62.3

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: вне зоны QA

## Blockers

- нет

## FIX cycle (QA / durable, не текст статьи)

1. `editorial-policy.json` снова без `pain_markers_ru` / `outcome_markers_ru` → false utility BLOCK → списки восстановлены.
2. `utility_gate.py`: снова skip-empty при пустых списках (защита от регресса).
3. CTA в HTML как `[REDACTED]` → link-verify expand из `CATALOG_URL`/`TELEGRAM_URL` → 2/2 PASS → re-redact.

## FIX (non-blocking / optional для writer)

1. **Ept02:** после публикации соседних URL — 2–3 internal blog links с `anchor_variants`.
2. **human-voice warn:** разнести длину списков (не все ровно по 5 пунктов), если будет рерайт.
3. **fact-bank soft:** дописать ставки госпошлин / дату ОСАГО-изменения для verified.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- link-verify PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
