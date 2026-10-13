# Article QA — B01

**topic_id:** B01  
**slug:** kak-privezti-elektromobil-iz-kitaya-2026  
**article_dir:** memory/blog/articles/B01-kak-privezti-elektromobil-iz-kitaya-2026  
**date:** 2026-10-14  
**verdict:** PASS  
**score:** 88  
**COVER_SCHEMA_ALLOWED:** yes

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит по рекламным пиковым л.с. → сюрприз с 30-минутной мощностью и льготным утилем во Владивостоке |
| Где решение | H2: задача → 30-мин мощность → льготный утиль (таблица) → пакет до депозита → смета по строкам → красные флаги → чеклист stop/go |
| Первый результат | Папка «до депозита» + решение ставлю / не ставлю / спрашиваю |
| Термины «на пальцах» | 30-минутная vs пик; совокупный платёж vs «единая ставка»; «проходные»; СБКТС→ЭПТС; GB/T / адаптер |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | reconfirm; warning: no obvious official docs URL |
| utility gate | PASS | pain=7, outcome=7, action=39; after restore `pain_markers_ru`/`outcome_markers_ru` in editorial-policy (empty lists → false BLOCK) |
| human-voice | PASS | WARN: 2× exactly-5-step lists |
| fact-check | PASS | 12 extracted / 1 verified in fact-bank; rest in research-notes |
| link-verify | PASS (soft) | catalog host HTTP 503 soft-pass (href≈CATALOG_URL); telegram 200; 2 internal blog 200 |
| html-linter | PASS | 0 errors; whitelist OK; no TOC |
| slop-detector | WARNING | 0 cliches; 9 over-long (table/ul/blockquote glue); Flesch RU 65.4 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в meta/H1; 7 actionable H2; 2 deep-link blog + catalog + Telegram |
| GEO / citability | 23/25 | Insight-блок, таблица, workflow→, FAQ×7, чеклисты; ярлык `TL;DR / Быстрый инсайт` — optional soft FIX |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | gate PASS; concrete markers + reader_story overlap |
| Fact safety | 13/15 | Минфин/ЕЭК/порог 80 л.с. в research; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9450 chars, mode B, FAQ, CTA |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «электромобиль из китая» в title/meta |
| C02 | ✓ | Lead: боль депозита + чек-лист до оплаты |
| C03 | ✓ | Читатель: физлицо, заказ EV из КНР |
| C04 | ✓ | 30-мин мощность, утиль, СБКТС/ЭПТС, GB/T объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный stop/go до депозита |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + table + workflow, mode B |
| R01 | ✓ | Insight + чеклист результата |
| R02 | ✓ | Письмо Минфина, ЕЭК №107, порог 58,84 кВт |
| R03 | ✓ | Нет статичных сумм пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «сначала цифра для документов» |
| E02 | ✓ | Сделайте / Не делайте в секциях |
| E03 | ✓ | CTA catalog×1 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Вилка 0,45 как практика не ГОСТ; граница 78–82 |
| Ept02 | ✗ | Insight-метка `TL;DR / Быстрый инсайт` (контракт предпочитает без ярлыка) |
| Ept03 | ✗ | (слот) catalog CTA 503 на момент проверки — soft-pass |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 4, failed hard: 0
- catalog `avto-sales125.ru` → 503 soft-pass (href matches CATALOG_URL rstrip)
- telegram OK; 2 internal posts OK
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 9 (артефакт списков/таблицы)
- Flesch RU: 65.4

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (utility false-BLOCK снят восстановлением marker lists в policy)

## FIX cycle (QA)

1. Utility BLOCK pain=0/outcome=0 при пустых `pain_markers_ru`/`outcome_markers_ru` в `memory/brief/editorial-policy.json` — **не** правка текста статьи; восстановлены известные списки маркеров (регрессия после rebrand). Повтор utility: PASS.
2. link-verify fail catalog 503 → soft-pass по правилу href≈CATALOG_URL; durable soft-pass в `link_verify.py` ещё нужен (incident).

## FIX (non-blocking / optional writer)

1. Убрать ярлык `TL;DR / Быстрый инсайт:` из первого blockquote (оставить смысл инсайта).
2. Разнообразить размер ol (сейчас 2× ровно 5 шагов) — WARN human-voice.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass (soft catalog 5xx) ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
