# Article QA — AS01

**topic_id:** AS01  
**slug:** rastamozhka-avto-iz-korei-2026  
**article_dir:** memory/blog/articles/AS01-rastamozhka-avto-iz-korei-2026  
**date:** 2026-07-19  
**verdict:** FAIL  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN technical_topic false-positive (api/github) |
| utility gate (topic) | PASS | AS01 how_to / mode B |
| utility gate (article) | BLOCK | pain_markers=0&lt;2, outcome_markers=0&lt;3 — **script/policy bug**: `editorial-policy.json` не содержит `pain_markers_ru`/`outcome_markers_ru`, а CLI default min=2/3 → всегда BLOCK (AS09 тоже) |
| human-voice-gate | PASS | WARN: 2× exactly-5-step lists; pain/outcome/story overlap OK |
| fact-check | PASS | 6 stats; 2 verified / 4 unverified (сроки в research-notes, не в fact-bank) |
| link-verify | FAIL | 2 unique href; 1 OK (Trust Encar relative); 1 FAIL — literal `href="[REDACTED]"` (×3 CTA) → 404 |
| html-linter | PASS | whitelist OK; TOC нет |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/схема); Flesch RU 61.0 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA сломаны `[REDACTED]` |
| GEO / citability | 22/25 | TL;DR, схема, таблица сроков, FAQ×6, чеклисты |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 14/15 | gate PASS; живой кейс Антона |
| Fact safety | 12/15 | сроки ориентиры; без статичных пошлин ✓; 4 unverified vs fact-bank |
| Contract HTML | 6/10 | whitelist PASS; CTA href = literal `[REDACTED]` (blocker) |
| Utility gates | 0/10 | article utility BLOCK (policy/script); human-voice PASS |
| **Итого** | **74/100** | &lt;80 → FAIL |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка авто из кореи» в meta/H1 |
| C02 | ✓ | Lead: депозит без понимания цепочки → простой СВХ |
| C03 | ✓ | Новичок, заказ из Кореи через Владивосток |
| C04 | ✓ | СВХ / СБКТС / ЭПТС / ТПО / BL объяснены |
| O01 | ✓ | H2 = путь → сроки → документы → расчёт → чеклист → дальше |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote-схема, mode B |
| R01 | ✓ | TL;DR + схема + FAQ |
| R02 | ✓ | Сроки с вилками; источники в research-notes |
| R03 | ✓ | Нет статичных сумм пошлин/утильсбора |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «растаможка ≠ одна пошлина» |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✗ | CTA catalog×2 + Telegram×1, но href=`[REDACTED]` |
| Exp01 | ✓ | Mode B, без fake first-person hero |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: ориентиры сроков, не гарантия; расчёт только у менеджера |
| Ept02 | ✗ | 1 internal blog link (Trust Encar); нет 2–3 стабильных internal |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

| Check | Result |
|-------|--------|
| Боль новичка решена | ✓ Lead: депозит «пока не увели» + непонимание СВХ/СБКТС → простой |
| Где показано решение | ✓ H2 путь/сроки/документы/чеклист до депозита |
| Первый результат до FAQ | ✓ Критерий: объяснить 7–8 этапов и когда машина «на учёте» |
| Термины на пальцах | ✓ СВХ, СБКТС, ЭПТС, BL, ТПО, ПТД |
| Первый безопасный шаг | ✓ Чеклист до депозита; стоп при «просто перевод продавцу» |
| Beginner-fit | **PASS** |

## Pain / solution map (editorial)

- **Боль:** растаможка как чёрный ящик; страх зависания на СВХ Владивостока.
- **Решение:** таймлайн Encar → … → ГИБДД + документы до судна + чеклист до депозита.
- **Результат:** читатель знает этапы/сроки-ориентиры и куда идти за расчётом (каталог/менеджер), без ложного калькулятора.

## Link verify

- total unique: 2, failed: 1
- Trust Encar relative: OK (200)
- CTA `href="[REDACTED]"` (catalog×2 + Telegram×1, unique string): FAIL 404
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/схемы)
- Flesch RU: 61.0

## Schema ready

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes | Review: no  
Cover/schema: **не запускать** до QA PASS.

## Blockers

1. **link-verify FAIL** — в `article.html` три CTA с буквальным `href="[REDACTED]"` (не URL). Writer обязан восстановить реальные URL каталога и Telegram из fact-bank / site brief.
2. **utility gate (article) BLOCK** — `pain_markers=0`, `outcome_markers=0` из‑за отсутствия списков маркеров в `memory/brief/editorial-policy.json` при default min 2/3 в `excalibur_blog_utility_gate.py`. Контент уже проходит human-voice pain/outcome; чинить policy/script (Fixer), не «набивать» статью вслепую.

## FIX list → Writer (цикл 1)

1. Заменить все literal `href="[REDACTED]"` на рабочие CTA: каталог сайта + Telegram `@avtosales125` (URL из fact-bank / env `TELEGRAM_URL`). Не оставлять плейсхолдер `[REDACTED]` в HTML.
2. После правки CTA — перезапуск GEO QA (link-verify + utility после фикса policy, если Fixer успеет).

## FIX → Fixer / Director (не Writer)

1. `excalibur_blog_utility_gate.py`: не применять `min_pain_markers`/`min_outcome_markers`, если `pain_markers_ru`/`outcome_markers_ru` пусты; **или** добавить списки в `memory/brief/editorial-policy.json` (можно выровнять с human-voice PAIN/OUTCOME_MARKERS).
2. Pitfall: Writer/commit не должен подставлять literal `[REDACTED]` в `article.html` CTA.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✗ (article BLOCK)  
- human-voice PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FAIL — cover \|\| schema **запрещены**. Вернуть Writer (CTA) + Fixer (utility policy/script).
