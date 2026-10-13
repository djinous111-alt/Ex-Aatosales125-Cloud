# Article QA — B01

**topic_id:** B01  
**slug:** avto-iz-korei-ili-kitaya-2026  
**article_dir:** memory/blog/articles/B01-avto-iz-korei-ili-kitaya-2026  
**date:** 2026-10-13  
**verdict:** PASS  
**score:** 90  
**COVER_SCHEMA_ALLOWED:** yes

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes gate | PASS | `research-notes-gate.json`; warn: нет official docs URL (не блокер для non-dev темы) |
| fact-check | PASS | 10 stats; 1 verified / 9 unverified vs fact-bank (цифры есть в research-notes: 160 л.с., 3400/5200, ПП 1713, сроки) |
| link-verify | PASS (soft) | catalog host 503 HEAD → soft-pass (`href` matches `CATALOG_URL`); Telegram 200; `failed_count=0` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 8 over-long (склейка таблиц/схем парсером); Flesch RU 67.8 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | `pain_markers=2`, `outcome_markers=3`, action=11; errors=[] |
| human voice gate | PASS | warn: Fact Check template + два списка ровно по 5 пунктов |

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
| GEO / citability | 22/25 | Инсайт-блок, таблицы, схемы →, FAQ×6, чеклист; ярлык «TL;DR / Быстрый инсайт» — soft note |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | gate PASS, 0 AI-openers |
| Fact safety | 13/15 | fact-check PASS; unverified vs fact-bank; catalog 503 soft-pass |
| Contract HTML | 10/10 | whitelist PASS, FAQ, CTA, без форм |
| Utility / gates | 10/10 | research + utility + human-voice PASS |
| **Итого** | **90/100** | |

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

- total: 2; failed_count: 0  
- catalog: HTTP 503 → soft-pass (href matches `CATALOG_URL`)  
- Telegram: 200  

## AI-slop scan

- cliches: 0  
- over-long: 8 (артефакт таблиц/схем)  
- Flesch RU: 67.8  

## Schema ready

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (чеклисты) | cover/schema: **разрешены** (`COVER_SCHEMA_ALLOWED=yes`)

## Soft notes (не блокер)

1. Инсайт-блок начинается с ярлыка `TL;DR / Быстрый инсайт:` — желательно убрать ярлык при следующем Writer-цикле (gates PASS, article.html не трогаем).
2. Два списка ровно по 5 пунктов + шаблон Fact Check — human-voice WARN.
3. После появления URL соседних постов — 2–3 internal links (`Ept02`).

## Gate checklist

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✓ (soft catalog 503)  
- research-notes gate PASS → ✓  
- utility gate PASS → ✓  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — cover \|\| schema **разрешены** (`COVER_SCHEMA_ALLOWED=yes`).
