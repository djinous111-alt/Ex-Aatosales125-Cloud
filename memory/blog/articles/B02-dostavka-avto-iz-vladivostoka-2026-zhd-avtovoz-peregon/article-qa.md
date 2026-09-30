# Article QA — B02

**topic_id:** B02  
**slug:** dostavka-avto-iz-vladivostoka-2026-zhd-avtovoz-peregon  
**article_dir:** memory/blog/articles/B02-dostavka-avto-iz-vladivostoka-2026-zhd-avtovoz-peregon  
**date:** 2026-10-01  
**verdict:** FAIL  
**score:** 74  
**fix_cycle:** 1 (return to writer)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic without official docs URL |
| utility gate (topic B02) | PASS | comparison / mode B |
| utility gate (article) | **BLOCK** | action_markers 7&lt;8; pain_markers 0&lt;2; outcome_markers 0&lt;3 |
| fact-check | PASS | 8 stats; 3 verified / 5 unverified vs fact-bank |
| link-verify | **fail** | 1 unique href = literal `[REDACTED]` → 404; Telegram/catalog URL отсутствуют |
| html-linter | PASS | 0 errors; TOC нет |
| slop-detector | WARNING | 0 клише; 7 over-long (склейка таблицы/схем); Flesch RU 59.7 |
| cannibalization | PASS | 0 issues |
| human-voice | PASS | warnings: 2× exactly-5-step lists |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Машина с ЭПТС во Владивостоке; три цены/срока; страх переплаты / очереди / царапин без доказательств |
| Где решение | H2: сравнение трёх способов → автовоз → ж/д сетка/контейнер → перегон → чек-лист сдачи → маршрут → критерий готового выбора |
| Первый результат | Выбран один способ + заполненный чек-лист (договор, 2–3 КП, фото, акт, страховка) до FAQ |
| Термины «на пальцах» | ЭПТС, сетка vs контейнер, срок «от сдачи», акт приёма-передачи, ЛКП |
| Beginner-fit | PASS (не dev-тон; есть безопасный первый шаг без команды профи) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 14/20 | Primary в H1/title; H2 actionable; CTA битые (`[REDACTED]`); нет blog internal |
| GEO / citability | 22/25 | Insight, таблица, схемы →, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 17/20 |
| Human voice | 14/15 | gate PASS; insight стартует с ярлыка `TL;DR / Быстрый инсайт` |
| Fact safety | 11/15 | 5 unverified чисел (18/7/60 дней, 245/130 тыс.) — есть в research-notes, нет в fact-bank |
| Contract HTML | 6/10 | Whitelist PASS, объём 9499, FAQ×6; **все 3 href = `[REDACTED]`** |
| **Итого** | **74/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «доставка авто из владивостока» в H1 / meta |
| C02 | ✓ | Lead — боль новичка + три цены/срока |
| C03 | ✓ | Читатель после растаможки во Владивостоке |
| C04 | ✓ | Автовоз / ж/д сетка·контейнер / перегон объяснены |
| O01 | ✓ | H2 закрывают pain_solution_map |
| O02 | ✓ | Логичный comparison → выбор → чек-лист → результат |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + table + blockquote workflows, mode B |
| R01 | ✓ | Insight + схемы + FAQ |
| R02 | ✓ | Сроки/вилки с пометкой «ориентир / не гарантия» |
| R03 | ✓ | Нет выдуманных % лотов; вилки как рыночные ориентиры |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «после таможни», три рабочих пути |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✗ | CTA hrefs = `[REDACTED]` (не рабочие ссылки) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Ограничения сроков, сезон перегона, акт/фото |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate score ≥80:** ✗ (74)

## Blockers (must FIX before cover||schema)

1. **UTILITY ARTICLE BLOCKER** — `utility-gate-report.json` BLOCK:
   - `action_markers=7 < 8`: в тексте «Делать/Не делать», а policy считает `сделайте` / `не делайте` / `избегайте` / `чеклист` (без дефиса) / `шаг ` и т.д. Добавить ≥1 точный маркер (например «избегайте» или «не делайте» / «чеклист»).
   - `pain_markers=0 < 2` и `outcome_markers=0 < 3`: в `memory/brief/editorial-policy.json` **нет** списков `pain_markers_ru` / `outcome_markers_ru`, при этом скрипт всё равно требует min 2/3 → systematic BLOCK (см. incident). Writer не сможет набрать маркеры по пустому списку; нужен Fixer **или** временный workaround после появления списков в policy.
2. **LINK VERIFY FAIL** — все три `<a href="[REDACTED]">` литералы-заглушки. Вернуть CTA из env `$CATALOG_URL` (×2) + `$TELEGRAM_URL` (×1), как в AS09. Перезапустить `excalibur_blog_link_verify.py --site-base $PUBLIC_SITE_URL`.

## FIX list для Writer (цикл 1)

1. Заменить все `href="[REDACTED]"` на `$CATALOG_URL` (×2) + `$TELEGRAM_URL` (×1), без плейсхолдеров.
2. Поднять `action_markers` до ≥8 точными фразами из `recommendation_markers_ru` (минимум +1: `избегайте` / `не делайте` / `чеклист` / `шаг N`).
3. Убрать ярлык `TL;DR / Быстрый инсайт:` из начала insight-blockquote (skill: не начинать с этих шаблонов); оставить суть.
4. После Fixer починит policy markers — перегнать utility gate; при появлении списков вписать 2+ pain и 3+ outcome маркера естественно в lead/H2/результат.
5. (Optional) Разный размер списков (сейчас 2× ровно 5 шагов — human-voice warning).
6. (Optional) Ept02: 2–3 internal blog links с `anchor_variants` после публикации соседних URL.

## Soft / non-blocking

- fact-check: дописать в fact-bank ориентиры 18–22 / 3–7 / 30–60 дней, 165–245 тыс., ~130 тыс. перегон (из research-notes).
- slop over-long: артефакт таблицы; не критично.
- char_count 9499 — у верхней границы; при правках не раздувать.

## Gate checklist

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS → ✓  
- utility gate article PASS → ✗  
- human-voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FAIL — вернуть Writer (FIX list выше). Cover||schema **не** запускать.
