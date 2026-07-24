# Article QA — B02

**topic_id:** B02  
**slug:** dostavka-avto-iz-vladivostoka-2026  
**article_dir:** memory/blog/articles/B02-dostavka-avto-iz-vladivostoka-2026  
**date:** 2026-07-24  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic false-positive via `ai`⊂`pain`; github_urls=3 |
| fact-check | PASS | 12 stats; 4 verified / 8 unverified vs fact-bank (сроки/тарифы есть в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 10 over-long (таблица/схемы + lead); Flesch RU 59.3 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 16; pain 23; outcome 8; ol=10; H2=8; FAQ×7; table×1 |
| human-voice | PASS | warnings: 2× exactly-5-step lists |

## Beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Машина на СВХ / после таможни — неясно автовоз vs ж/д vs перегон; страх простоя и царапин без акта |
| Где решение | H2: закрыть СВХ → таблица сравнения → автовоз / ж/д / отсев перегона → документы/стоп-правила → скрытые доплаты |
| Первый результат | До FAQ: выбран один способ, ориентир срока, стоп-правила (акт/страховка/трекинг); 5 шагов «на сегодня» |
| Термины «на пальцах» | СВХ, ЭПТС, автовоз, последняя миля, вагон-сетка — объяснены в тексте |

**Beginner-fit:** PASS (не тон «для профи», есть первый безопасный шаг без команды разработчиков)

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 actionable; CTA×3; нет 2–3 internal blog links |
| GEO / citability | 23/25 | Инсайт-блок, таблица, схема →, FAQ×7, чеклисты; ярлык «TL;DR / Быстрый инсайт» шаблонный |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop клише |
| Fact safety | 12/15 | Ориентиры с пометкой «не гарантия»; часть цифр не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9016–9301, FAQ, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «доставка авто из владивостока» в meta/H1 |
| C02 | ✓ | Lead: боль СВХ + три способа + результат сегодня |
| C03 | ✓ | Читатель после растаможки / на СВХ |
| C04 | ✓ | СВХ, ЭПТС, автовоз, последняя миля объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный comparison → выбор → стоп-правила → результат |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + workflow →, mode B |
| R01 | ✓ | Инсайт-блок, схема, FAQ |
| R02 | ✓ | Ориентиры 2026 + кейс Drive2 в research |
| R03 | ✓ | Цены как ориентиры; пошлины не выдуманы |
| R04 | ✓ | FAQ отвечает действием в 1-м предложении |
| E01 | ✓ | Угол «СВХ→город», перегон как ловушка |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я проехал 9000» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Стоп-правила акта/страховки/зимы |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |
| Exp? | — | — |

Доп. soft: инсайт начинается с «TL;DR / Быстрый инсайт» — skill просит без этого ярлыка (не блокирует скрипты).

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 10 (таблица + lead; не blocker)
- Flesch RU: 59.3

## Pain / solution map check

- Lead называет боль (СВХ + выбор способа + простой/царапины) ✓
- H2 закрывают pain_solution_map (СВХ, сравнение, автовоз, ж/д, перегон, документы, доплаты) ✓
- До FAQ — критерий успеха + 5 шагов ✓

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты/шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (utility gate сначала BLOCK из-за пустых `pain_markers_ru`/`outcome_markers_ru` в policy — восстановлено в `memory/brief/editorial-policy.json`, см. incident)

## FIX cycle (QA)

1. Utility BLOCK (pain=0/outcome=0 при пустых списках маркеров в policy) → добавлены `pain_markers_ru` / `outcome_markers_ru` + min в editorial-policy; повтор utility PASS. `article.html` не правился.

## FIX (non-blocking / optional)

1. **Ept02:** после live URL соседних постов — 2–3 internal blog links с `anchor_variants`.
2. **Инсайт-ярлык:** заменить «TL;DR / Быстрый инсайт» на нейтральный («Коротко:» / без ярлыка).
3. **fact-check soft:** дописать в fact-bank ориентиры сроков/тарифов 2026 и кейс Drive2.
4. **human-voice warn:** развести размеры двух ol по 5 пунктов (4 и 6 и т.п.).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
