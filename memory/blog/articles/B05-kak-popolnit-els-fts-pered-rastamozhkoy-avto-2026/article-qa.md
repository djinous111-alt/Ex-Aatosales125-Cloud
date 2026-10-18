# Article QA — B05

**topic_id:** B05  
**slug:** kak-popolnit-els-fts-pered-rastamozhkoy-avto-2026  
**article_dir:** memory/blog/articles/B05-kak-popolnit-els-fts-pered-rastamozhkoy-avto-2026  
**date:** 2026-10-18  
**verdict:** FIX  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic false-positive (known INC) |
| utility gate | **BLOCK** | `pain_markers=0 < 2`, `outcome_markers=0 < 3` — в `editorial-policy.json` нет `pain_markers_ru` / `outcome_markers_ru`; AS09 тоже BLOCK на текущем скрипте |
| human-voice-gate | PASS | `human-voice-report.json`; warn: 4× exactly-5-step lists |
| fact-check | PASS | 8 stats; 1 verified (2026); 7 unverified vs fact-bank (КБК/коды/15 мин/1e6 — в research-notes) |
| link-verify | **FAIL** | edata.customs.ru SSL timeout; 3× CTA `href="[REDACTED]"` → internal_relative 404 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; over-long 4; Flesch RU 65.9 |
| cannibalization | PASS | 0 issues (`cannibalization-report.json`) |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка решена? | Машина на пути/СВХ, непонятный ЕЛС, миф «жена/брокер заплатит» — с 01.04.2026 чужой платёж не зачисляют |
| Где показано решение? | H2: кошелёк ЕЛС → ЛК через Госуслуги → СБП своей картой → реквизиты/КБК → остаток+скрин → troubleshooting → чек-лист 10 |
| Первый результат до FAQ? | «Открытый ЛК, достаточный остаток на своём ЕЛС и скрин у менеджера» + критерии «готово» |
| Термины «на пальцах»? | ЕЛС, СВХ, СБП, КБК, код органа 10000010 vs 10702000 — объяснены |
| Beginner-fit | PASS (первый шаг без ЭЦП/разработчиков; без тона «для профи») |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 actionable; CTA сломаны `[REDACTED]` |
| GEO / citability | 22/25 | Инсайт, схема, таблица, FAQ×6, чеклисты |
| CORE-EEAT lite | 13/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS, slop 0 |
| Fact safety | 12/15 | Факты в research; не в fact-bank; edata недоступен по SSL |
| Contract HTML | 6/10 | Whitelist PASS, FAQ OK; **utility BLOCK** + **link-verify FAIL** |
| **Итого** | **74/100** | ниже порога 80 из‑за gate blockers |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как пополнить елс фтс» в title/H1 |
| C02 | ✓ | Lead: боль СВХ + запрет чужого платежа + чек-лист |
| C03 | ✓ | Читатель: физлицо, авто под заказ Владивосток |
| C04 | ✓ | ЕЛС/СБП/КБК объяснены |
| O01 | ✓ | H2 ≈ action_outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | Инсайт + схема + FAQ |
| R02 | ✓ | 58н / КБК / лимит СБП / ~15 мин — в research |
| R03 | ✓ | Нет сумм пошлин; запас 20–30 тыс. с оговоркой |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «только свой ИНН» + конфликт кодов органа |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✗ | CTA href литералы `[REDACTED]` — не рабочие URL |
| Exp01 | ✓ | Mode B, история Игоря без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Выходные/чужая карта/конфликт кодов |
| Ept02 | ✗ | Нет internal blog links (ожидаемо до Indexer) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers вне EEAT:** utility BLOCK, link-verify FAIL → overall FIX

## Link verify

- total unique: 2 (edata + один `[REDACTED]` после dedupe)
- failed: 2
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 65.9

## Schema ready

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes | cover/schema: **не стартовать** до re-QA PASS

## Blockers

1. **utility gate BLOCK** — policy gap: нет `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json`, при этом скрипт требует min 2/3 по умолчанию. Текст статьи уже содержит маркеры human-voice (`боль`, `проблем`, `ошиб`, `результат`, `проверьте`, `выберите`). Durable fix → fixer (не writer rewrite).
2. **link-verify FAIL** — CTA: заменить литералы `href="[REDACTED]"` на реальные URL каталога и Telegram (как в AS09: `avto-sales125.ru` + `t.me/avtosales125`), брать из env/site-brief, не писать placeholder в HTML.
3. **link-verify FAIL** — `https://edata.customs.ru/FtsPersonalCabinetWeb/` SSL handshake timeout (повтор 45s тоже fail; родственно research WebFetch 504). Soft-fail host для customs/edata **или** оставить URL после ручной пометки; не считать единственным writer-FIX, если CTA починены.

## FIX cycle (QA) — для Writer (цикл 1)

1. **CTA href:** три ссылки каталог×2 + Telegram×1 — живые `https://…` URL, не строка `[REDACTED]`.
2. **Optional:** переименовать инсайт-блок — не начинать с ярлыка `TL;DR` / `Быстрый инсайт` (skill preference; html-linter/HV сейчас PASS).
3. **Не требуется** массовый рерайт под utility markers, пока fixer не синхронизирует policy со списками human-voice gate.

## FIX (Director / Fixer — до cover||schema)

1. Добавить в `memory/brief/editorial-policy.json` списки `pain_markers_ru` / `outcome_markers_ru` (+ `min_pain_markers` / `min_outcome_markers` в `article_required_signals`) в паритете с `excalibur_blog_human_voice_gate.py`.
2. Рассмотреть soft-fail / retry для `edata.customs.ru` / `customs.gov.ru` в `excalibur_blog_link_verify.py`.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✗  
- human-voice-gate PASS ✓  
- link-verify pass ✗  

**Итог:** FIX — cover || schema **не** запускать. Сначала fixer (utility policy) + writer FIX (CTA), затем повтор GEO QA.
