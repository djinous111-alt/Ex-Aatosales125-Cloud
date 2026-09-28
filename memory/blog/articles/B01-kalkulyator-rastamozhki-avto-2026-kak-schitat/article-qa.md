# Article QA — B01

**topic_id:** B01  
**slug:** kalkulyator-rastamozhki-avto-2026-kak-schitat  
**article_dir:** memory/blog/articles/B01-kalkulyator-rastamozhki-avto-2026-kak-schitat  
**date:** 2026-09-28  
**verdict:** FAIL  
**score:** 74  
**FIX cycle:** 1 (return → writer)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-09-28; source_table/pain_map OK |
| utility gate (article) | **BLOCK** | action_markers 7<8; pain_markers 0<2; outcome_markers 0<3 |
| human-voice-gate | **BLOCK** | outcome_markers unique 2<3 (`проверьте`, `соберите`); WARN: exactly-5 lists×2 |
| fact-check | PASS | 15 stats; verified 2 / unverified 13 (пороги в research-notes, не все в fact-bank) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` = PUBLIC_SITE_URL |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; over-long 2; Flesch RU 65.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит «наугад» + каша пошлина/утиль/льгота 160 л.с. (lead + Алексей 165 л.с.) |
| Где решение | H2: 3 строки сметы → поля калькулятора → льгота → миф о стране → расхождение калькуляторов → чек-лист до депозита |
| Первый результат | Закрытый чек-лист + вилка «под ключ» до депозита (до FAQ) |
| Термины «на пальцах» | ЕТС, СБКТС, ЭПТС, утильсбор, корзины возраста — объяснены |
| Beginner-fit | PASS (не developer-tone; есть безопасный первый шаг) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 how-to; CTA×3; мало blog-internal |
| GEO / citability | 20/25 | TL;DR-инсайт, таблицы×2, FAQ×6, чек-лист; outcome-маркеры слабые для gate |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 10/15 | story/pain OK; **human-voice BLOCK** по outcome |
| Fact safety | 12/15 | Факты в research-notes; много unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; объём ~8980–9157; FAQ; без форм/`pre` |
| **Итого** | **74/100** | ← ниже порога 80 |

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
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Калькулятор ≠ касса; курс/корректировка стоимости |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Score gate:** 74 < 80 → FAIL

## Blockers (вернуть writer)

1. **HUMAN VOICE BLOCKER** — в тексте только 2 из списка `OUTCOME_MARKERS` (`проверьте`, `соберите`). Нужно ≥3: добавить явно одно из `результат` / `получите` / `сможете` / `выберите` / `сэконом` (без ломки смысла; напр. в чек-листе или lead: «результат — закрытый чек-лист до депозита»).
2. **UTILITY action_markers 7<8** — сейчас засчитываются вхождения `ориентир`(×5) + `проверьте` + `добавьте`. Не хватает ≥1. Варианты: заменить «Делать/Не делать» на **«Сделайте/Не делайте»** (≥1–2 вхождения), добавить `избегайте` / `используйте` / `чеклист` (без дефиса; сейчас только «чек-лист»).
3. **UTILITY pain/outcome 0** — см. incident policy: в `memory/brief/editorial-policy.json` **нет** `pain_markers_ru` / `outcome_markers_ru`, а скрипт требует min 2/3 → gate всегда BLOCK даже на ранее PASS AS08/AS09. Writer не может закрыть это только текстом; нужен Fixer/policy. Параллельно human-voice уже требует явные outcome-слова (п.1).

## FIX (writer) — конкретные правки

1. Lead или блок перед FAQ: одна фраза с маркером **`результат`** или **`сможете`** (human-voice).
2. ≥1 action-маркер из policy: **`сделайте`/`не делайте`** или **`избегайте`/`используйте`/`чеклист`**.
3. Опционально: развести длины списков (WARN exactly-5×2) — не блокер.
4. Не добавлять готовые суммы «итого растаможки» — constraint research.

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links на AS08/AS09 после publish URL.
2. **fact-check soft:** дописать в fact-bank пороги 160 л.с., 3000 см³, шкалу сбора 1231–73860, базу утиля 20000.
3. Meta `char_count` 9157 vs plain ~8980 — пересчитать после FIX.

## Gate checklist

- score ≥ 80 → **74** FAIL  

- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✗  
- human-voice PASS ✗  
- beginner-fit PASS ✓  

**Итог:** FAIL — cover\|\|schema **не** запускать. Следующий шаг: `Task(excalibur-blog-writer)` FIX cycle 1 + Fixer по INC utility-policy.
