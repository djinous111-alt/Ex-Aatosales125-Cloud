# Article QA — B01 (re-run after Writer FIX + Fixer)

**topic_id:** B01  
**slug:** kak-rasschitat-utilsbor-pri-vvoze-avto-2026  
**article_dir:** memory/blog/articles/B01-kak-rasschitat-utilsbor-pri-vvoze-avto-2026  
**date:** 2026-10-06  
**verdict:** PASS  
**score:** 87

## Scripts (re-run)

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-06; technical_topic=false; sources/outline OK |
| fact-check | PASS | 17 stats; 3 verified vs fact-bank; 14 unverified (в research-notes / отраслевые ориентиры) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из PUBLIC_SITE_URL |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/схемы); Flesch RU 67.1 |
| cannibalization | PASS | 0 issues (3 meta loaded) |
| utility gate | PASS | pain_markers=10 (≥2); outcome_markers=10 (≥3); Fixer policy markers OK |
| human-voice gate | PASS | outcome_markers≥6; soft warn: exactly_five_lists=2 |

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
| CORE-EEAT lite | 15/15 | 19/20 (см. ниже; минус только internal links) |
| Human voice | 13/15 | Gate PASS; soft warn exactly_five_lists=2 |
| Fact safety | 11/15 | Ориентиры с пометкой; точная сумма → каталог; fact-bank неполный (14 unverified) |
| Contract HTML | 10/10 | Whitelist PASS, ~9440 знаков, FAQ, CTA, без форм |
| **Итого** | **87/100** | ≥80; все gates PASS |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как рассчитать утильсбор на авто 2026» в meta/H1 |
| C02 | ✓ | Lead — боль про льготу/1 л.с. + outcome markers |
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

**Target:** ≥16/20 ✓ · veto human-voice/utility: **нет**

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 67.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | cover/schema: **разрешены** после этого PASS

## Blockers

none

## Soft notes (не блокируют)

1. `exactly_five_lists=2` — желательно варьировать длины списков в следующих статьях.
2. Ept02: после Indexer появятся interlinks; для текущего PASS не veto.
3. fact-bank неполный относительно цифр статьи — опираемся на research-notes + пометки ориентиров.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — cover || schema **разрешены**.
