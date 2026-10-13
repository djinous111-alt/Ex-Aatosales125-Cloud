# Article QA — B01

**topic_id:** B01  
**slug:** avto-iz-korei-ili-kitaya-2026  
**article_dir:** memory/blog/articles/B01-avto-iz-korei-ili-kitaya-2026  
**date:** 2026-10-13  
**verdict:** FAIL  
**score:** 78  
**COVER_SCHEMA_ALLOWED:** no

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes gate | PASS | `research-notes-gate.json`; warn: нет official docs URL (не блокер для non-dev темы) |
| fact-check | PASS | 10 stats; 1 verified / 9 unverified vs fact-bank (цифры есть в research-notes: 160 л.с., 3400/5200, ПП 1713, сроки) |
| link-verify | FAIL | 1/2 fail: host каталога (`CATALOG_URL`) → HTTP 503 HEAD/GET; Telegram OK; `PUBLIC_SITE_URL` host отвечает 200 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 8 over-long (склейка таблиц/схем парсером); Flesch RU 67.8 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | BLOCK | `pain_markers=0 < 2`, `outcome_markers=0 < 3` — **ложный блокер**: в `editorial-policy.json` нет `pain_markers_ru` / `outcome_markers_ru`, а скрипт жёстко требует min 2/3. AS09 на той же policy тоже BLOCK |
| human voice gate | PASS | `human-voice-report.json`; warn: Fact Check template + два списка ровно по 5 пунктов |

## Beginner-fit

**PASS.** Статья для новичка первого заказа: боль в lead, порог 160 л.с. и смета «под ключ» без калькулятора; термины СВХ / СБКТС / ЭПТС / EREV / BEV объяснены; есть 10 пунктов до депозита и 5 шагов «что дальше»; тон не «для брокера/разработчика».

## Pain / solution / result

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка решена? | Страх выбрать «не ту» страну и потерять деньги, путая цену лота с итогом под ключ |
| Где показано решение? | H2: задача → парк → 160 л.с. → сроки/Владивосток → смета по статьям → чек-лист до депозита |
| Какой первый результат? | Формула «моя задача → Корея / Китай / посчитать оба» + галочка 160 л.с. + запрос двух смет без депозита вслепую |
| Термины «на пальцах» | СВХ, СБКТС, ЭПТС, кВт→л.с., BEV/EREV |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; actionable H2; CTA×3; мало blog-internal |
| GEO / citability | 22/25 | Инсайт-блок, таблицы, схемы →, FAQ×6, чеклист; ярлык «TL;DR / Быстрый инсайт» — soft FIX |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | gate PASS, 0 AI-openers |
| Fact safety | 11/15 | fact-check PASS, но много unverified vs fact-bank; link-verify FAIL (503 каталог) |
| Contract HTML | 10/10 | whitelist PASS, ~9479 символов, FAQ, CTA, без форм |
| Utility / gates | 0/10 | utility BLOCK + link-verify FAIL → вето на PASS |
| **Итого** | **78/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из кореи и китая» в title/H1 |
| C02 | ✓ | Lead: страх страны + путь до оплаты |
| C03 | ✓ | Читатель: первый заказ Корея vs Китай |
| C04 | ✓ | Encar/Che168, утиль, СВХ объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ×6 |
| O04 | ✓ | ol + таблицы + чеклист, mode B |
| R01 | ✓ | Инсайт, схемы, FAQ |
| R02 | ✓ | Цифры с оговоркой «ориентир / в каталоге» |
| R03 | ✓ | Нет готового калькулятора пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «задача и 160 раньше страны» |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Владивосток / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты сроков, расхождение гайдов |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 1  
- fail: catalog host из `CATALOG_URL` → 503 (HEAD и GET)  
- ok: Telegram  
- note: `PUBLIC_SITE_URL` host отвечает 200; CTA в статье совпадает с `CATALOG_URL` (не опечатка Writer)

## AI-slop scan

- cliches: 0  
- over-long: 8 (артефакт таблиц/схем)  
- Flesch RU: 67.8  

## Schema ready

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (чеклисты) | cover/schema: **не запускать** до PASS

## Blockers (почему FAIL)

1. **utility gate BLOCK** — ложный: пустые списки маркеров в policy + hardcoded `min_pain_markers=2` / `min_outcome_markers=3` в `excalibur_blog_utility_gate.py`. Human-voice при этом PASS (pain/outcome маркеры в тексте есть). Writer не может «дописать маркеры», пока списки в policy пустые. → Fixer / INC ниже.
2. **link-verify FAIL** — каталог `avto-sales125.ru` отдаёт 503. → infra / retry; не править longread вслепую на другой host без решения по `CATALOG_URL`.

## FIX cycle (Writer) — только если после Fixer utility снова BLOCK по тексту

Сейчас **не слать Writer** только ради utility pain/outcome: gate сломан для всех статей.

Soft FIX (после разблокировки gate, по желанию):

1. Убрать шаблонный ярлык `TL;DR / Быстрый инсайт:` из первого `<blockquote>` (оставить смысл инсайта).
2. По возможности разнообразить длину списков (сейчас два ol ровно по 5).
3. После появления URL соседних постов — 2–3 internal links с `anchor_variants`.

## Gate checklist

- score ≥ 80 → **78** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✗  
- research-notes gate PASS → ✓  
- utility gate PASS → ✗  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FAIL — cover \|\| schema **запрещены** (`COVER_SCHEMA_ALLOWED=no`). Сначала Fixer (utility policy/script) + повтор link-verify / GEO QA.
