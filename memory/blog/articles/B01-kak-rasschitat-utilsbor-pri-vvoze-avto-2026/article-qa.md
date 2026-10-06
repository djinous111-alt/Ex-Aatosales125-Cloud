# Article QA — B01

**topic_id:** B01  
**slug:** kak-rasschitat-utilsbor-pri-vvoze-avto-2026  
**article_dir:** memory/blog/articles/B01-kak-rasschitat-utilsbor-pri-vvoze-avto-2026  
**date:** 2026-10-06  
**verdict:** FIX  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-06; sources/outline OK |
| fact-check | PASS | 17 stats; 3 verified vs fact-bank; 14 unverified (в research-notes / отраслевые ориентиры) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из PUBLIC_SITE_URL |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/схемы); Flesch RU 66.9 |
| cannibalization | PASS | 0 issues (3 meta loaded) |
| utility gate | **BLOCK** | pain_markers=0&lt;2; outcome_markers=0&lt;3 — в `editorial-policy.json` нет `pain_markers_ru`/`outcome_markers_ru` (пустые списки → всегда 0) |
| human-voice gate | **BLOCK** | outcome markers: только «результат», «соберите» (нужно ≥3) |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Какая боль новичка решена? | Страх сорвать льготу на 1 л.с./гибриде и не знать, с каких цифр считать до депозита |
| Где показано решение? | H2: 5 вводных → чек-лист льготы → кВт → гибриды/EV → страна не меняет формулу → чек-лист до депозита |
| Первый результат до FAQ? | Мини-чек-лист + сценарий «льгота 3400/5200 или коммерция» + запрос в каталог (секция «Что дальше») |
| Термины «на пальцах»? | Утильсбор, ТПО, ЭПТС, параллельный/последовательный гибрид, 30-минутная мощность |
| Beginner-fit | **PASS** — не профи-жаргон; есть безопасный первый шаг до депозита |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1/meta; CTA есть; нет 2–3 internal blog links |
| GEO / citability | 22/25 | Инсайт, схема, таблица условий, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 8/15 | Скрипт BLOCK: мало outcome-маркеров; concrete/pain OK |
| Fact safety | 12/15 | Ориентиры с пометкой; точная сумма → каталог; fact-bank неполный |
| Contract HTML | 10/10 | Whitelist PASS, ~9466 знаков, FAQ, CTA, без форм |
| **Итого** | **74/100** | Ниже порога 80 из-за utility + human-voice BLOCK |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как рассчитать утильсбор на авто 2026» в meta/H1 |
| C02 | ✓ | Lead — боль про льготу/1 л.с. + обещание разбора до депозита |
| C03 | ✓ | Читатель: ввоз из Азии, физлицо, до депозита |
| C04 | ✓ | ТПО / ЭПТС / пороги кВт объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + схема, mode B |
| R01 | ✓ | Инсайт + схема + FAQ |
| R02 | ✓ | 3400/5200, 117,68 кВт, ПП 1291/1713 в research-notes |
| R03 | ✓ | Коммерческий ориентир ~900k помечен; точная сумма — в каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита», страна не меняет формулу |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты льготы, пороги без округления, EV 30-мин |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |
| Exp? | ✗ | Human-voice gate BLOCK (outcome) — veto на PASS пайплайна |

**Target:** ≥16/20 ✓ · veto human-voice/utility: **да** → overall FIX

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 66.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: **не стартовать** до PASS

## Blockers (вернуть Writer / Fixer)

### Writer FIX (обязательно)

1. **human-voice outcome ≥3:** сейчас только «результат» + «соберите». Добавить в тело ≥1–2 маркера из списка gate: `получите` / `сможете` / `проверьте` / `выберите` / `сэконом` (без шаблонной воды). Цель: `outcome_markers ≥ 3` в `human-voice-report.json`.
2. **(желательно)** убрать ярлык `TL;DR / Быстрый инсайт:` в первом blockquote — skill запрещает стартовый шаблон; оставить суть инсайта.
3. **(желательно)** разнести размеры списков: сейчас 4× ровно 5 пунктов (`exactly_five_lists`); варьировать 4/6/7 где уместно.
4. **(желательно)** слегка перефразировать Fact Check (`Материал проверен` + `Достоверность данных`) — warning про повторный шаблон.

### Fixer / policy BLOCKER (Writer не может закрыть текстом)

5. **utility gate всегда BLOCK:** в `memory/brief/editorial-policy.json` отсутствуют `pain_markers_ru` и `outcome_markers_ru`, при этом скрипт требует `min_pain_markers` (default 2) и `min_outcome_markers` (default 3). Пустые списки → счётчики всегда 0 → любая статья падает. Нужно: добавить маркеры в policy (согласовать с human-voice) **или** не применять min-пороги, если списки пусты. См. incident.

## FIX cycle (QA)

1. Utility BLOCK + Human Voice BLOCK → **не** cover/schema. Вернуть Writer на пункты 1–4; Fixer на пункт 5.
2. После правок Writer: повтор `human_voice_gate` + `utility_gate` (после policy fix) → цель PASS.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✗  
- human-voice PASS ✗  
- beginner-fit PASS ✓  

**Итог:** FIX — cover || schema **запрещены** до PASS.
