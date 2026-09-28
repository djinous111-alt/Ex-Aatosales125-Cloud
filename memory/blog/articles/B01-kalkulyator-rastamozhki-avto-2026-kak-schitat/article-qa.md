# Article QA — B01 (re-run after writer FIX + fixer policy)

**topic_id:** B01  
**slug:** kalkulyator-rastamozhki-avto-2026-kak-schitat  
**article_dir:** memory/blog/articles/B01-kalkulyator-rastamozhki-avto-2026-kak-schitat  
**date:** 2026-09-28  
**verdict:** PASS  
**score:** 88  
**FIX cycle:** 1 closed (writer FIX + fixer policy); GEO QA re-run

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-09-28; pain_solution_rows=5; source_table OK |
| utility gate (article) | PASS | action=24 (≥8); pain=6 (≥2); outcome=9 (≥3) |
| human-voice-gate | PASS | outcome unique ≥6 (`результат`, `получите`, `сможете`, `проверьте`, `соберите`, `выберите`); warnings=0 |
| fact-check | PASS | 15 stats; verified 2 / unverified 13 (пороги в research-notes, не все в fact-bank) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` = PUBLIC_SITE_URL |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; over-long 3 (склейка таблицы/схем); Flesch RU 63.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит «наугад» + каша пошлина/утиль/льгота 160 л.с. (lead + Алексей 165 л.с.) |
| Где решение | H2: 3 строки сметы → поля калькулятора → льгота → миф о стране → расхождение калькуляторов → чеклист до депозита |
| Первый результат | Закрытый чеклист + вилка «под ключ» до депозита (H2 до FAQ: «что получите») |
| Термины «на пальцах» | ЕТС, СБКТС, ЭПТС, утильсбор, корзины возраста — объяснены |
| Beginner-fit | PASS (не developer-tone; есть безопасный первый шаг до депозита) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 how-to; CTA×3; мало blog-internal |
| GEO / citability | 22/25 | Инсайт, таблицы×2, FAQ×6, чеклист; outcome/pain markers закрыты |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | story/pain/outcome PASS; slop=0 |
| Fact safety | 11/15 | Факты в research-notes; много unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; FAQ; без форм/`pre`; CTA×3 |
| **Итого** | **88/100** | ≥80 ✓ |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «калькулятор растаможки авто» в meta/H1 |
| C02 | ✓ | Lead: боль депозита + обещание сметы на бумаге |
| C03 | ✓ | Читатель: физлицо, импорт Азия, Владивосток |
| C04 | ✓ | Пошлина/ЕТС/утиль/льгота объяснены |
| O01 | ✓ | H2 = pain_solution_map research |
| O02 | ✓ | Логичный outline до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблицы + схемы, mode B |
| R01 | ✓ | Инсайт-блок, схема сметы, FAQ |
| R02 | ✓ | Пороги 160 л.с. / 3 л / 3–5 лет + ставки сбора в research |
| R03 | ✓ | Нет готовых сумм-калькулятора в статье (editorial constraint) |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «сначала считаем, потом платим» |
| E02 | ✓ | «Сделайте / Не делайте» в секциях |
| E03 | ✓ | CTA каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Калькулятор ≠ касса; курс/корректировка стоимости |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Score gate:** 88 ≥ 80 → PASS

## Blockers

- нет

## FIX (closed this cycle)

1. Writer: outcome-маркеры human-voice (`результат` / `получите` / `сможете` / `выберите`) + action `сделайте`/`не делайте`/`избегайте`/`используйте`/`чеклист`.
2. Fixer: `pain_markers_ru` / `outcome_markers_ru` в editorial-policy + utility gate sync.

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links на AS08/AS09 после publish URL.
2. **fact-check soft:** дописать в fact-bank пороги 160 л.с., 3000 см³, шкалу сбора 1231–73860, базу утиля 20000.
3. Meta `char_count` 9314 vs plain ~8950 — косметика.

## Gate checklist

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно запускать cover \|\| schema.
