# Article QA — B02 (re-run after Writer FIX1 + Fixer policy)

**topic_id:** B02  
**slug:** auktsionnyy-list-yaponiya-kak-chitat-2026  
**article_dir:** memory/blog/articles/B02-auktsionnyy-list-yaponiya-kak-chitat-2026  
**date:** 2026-07-23  
**verdict:** FAIL  
**score:** 86

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | technical_topic=false; warnings cleared |
| fact-check | PASS | 1/1 verified (2026) |
| link-verify | **FAIL** | 1/2 failed: Telegram CTA `href` is literal `[REDACTED]` (no scheme) → checked as internal vs site-base → HTTP 404 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long (таблицы/схемы); Flesch RU 71.5 |
| cannibalization | PASS | 0 issues (3 meta loaded) |
| utility gate | PASS | action=37; pain=6; outcome=9 |
| human-voice-gate | PASS | warning: два списка ровно по 5 шагов |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA каталог+TG; нет 2–3 blog internal |
| GEO / citability | 22/25 | Insight «Коротко до ставки», схема →, таблицы×2, FAQ×7, чек-лист |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | Gate PASS; ярлык TL;DR убран |
| Fact safety | 10/15 | Fact-check PASS; **битый Telegram href** |
| Contract HTML | 10/10 | Whitelist PASS, ~9205, FAQ, CTA, без форм/pre/code |
| Utility / action | 10/10 | PASS после FIX1 + policy markers |
| **Итого** | **86/100** | ≥80, но hard-gate link-verify ✗ |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в meta/H1 |
| C02 | ✓ | Lead: боль ставки вслепую + ответ |
| C03 | ✓ | Новичок у японского листа до ставки |
| C04 | ✓ | Grade, A/U/W/X/XX, R/RA «на пальцах» |
| O01 | ✓ | H2 = action outline |
| O02 | ✓ | Оригинал → зоны → схема → R/RA → ориентир → чек-лист |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul/tables/blockquotes, mode B |
| R01 | ✓ | Insight, схема →, таблицы, FAQ |
| R02 | ✓ | «больше 90% на японском»; R vs RA |
| R03 | ✓ | Нет выдуманных цен/VIN/лотов |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки, не после выкупа» |
| E02 | ✓ | «Сделайте / Не делайте» + Шаг N / Избегайте |
| E03 | ✓ | CTA: каталог×2 + Telegram (href сломан — см. FIX) |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | R/RA не приговор; XX ≠ авто-авария |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

**PASS.** Боль новичка в lead; термины объяснены; первый шаг — оригинал + 5 зон до ставки; без тона «для профи».

| Вопрос | Ответ |
|--------|-------|
| Какая боль новичка решена? | Не понимает 4.5 / R/RA / A2 / W2 и боится согласиться на ставку вслепую |
| Где показано решение? | H2: оригинал → 5 зон → схема → R/RA → ориентир 4–4.5 → чек-лист |
| Какой первый результат? | Пройти один лист и сказать менеджеру «ок» или «стоп» до ставки |
| Термины «на пальцах»? | Grade, салон A–E, A/U/W/X/XX, R/RA, структурный vs съёмная панель |

## Link verify

- total: 2 unique, failed: 1
- `https://avto-sales125.ru` → 200 OK
- Telegram CTA → literal `href="[REDACTED]"` on disk (len=10, no `t.me`) → FAIL
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 71.5

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes | Review: no | cover/schema: **blocked** (no QA PASS)

## Blockers

1. **LINK-VERIFY FAIL** — в `article.html` у CTA Telegram вместо URL лежит литерал `[REDACTED]` (артефакт secret-scan / копипаст из redacted view при FIX1). Каталог OK.

## FIX cycle (QA) — вернуть writer (узкий FIX2)

### FIX-2 (writer, 1 href) — восстановить Telegram CTA

В финальном `<li>` «Что дальше» заменить:

- `href="[REDACTED]"` → рабочий `https://t.me/<TELEGRAM_HANDLE>` (как в AS08/AS09; текст якоря `Telegram @avtosales125` уже верный).
- При коммите: не подставлять placeholder `[REDACTED]` в HTML; при необходимости `<!-- pragma: allowlist secret -->` рядом с CTA (см. automation memory / pitfalls).

Не трогать остальной текст: utility/human-voice/research уже PASS.

### Optional (non-blocking)

- Ept02: 2–3 internal blog links после появления URL других постов.
- Human-voice warning: варьировать длину списков (не два×ровно 5).

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → **FAIL** ✗  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- utility gate PASS ✓  

**Итог:** FAIL — cover||schema **не** запускать. Директор → writer FIX2 (только Telegram href) → GEO QA re-run.
