# Article QA — B01

**topic_id:** B01  
**slug:** kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026  
**article_dir:** memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026  
**date:** 2026-10-16  
**verdict:** FAIL  
**score:** 62  
**fix_cycle:** 1 (вернуть Writer; cover/schema не стартовать)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | recheck; warnings: no official docs URL |
| fact-check | PASS | 3/3 verified |
| link-verify | FAIL | 1/1 fail — CTA `href` = литерал `[REDACTED]` (не URL); 404 после join с site-base |
| html-linter | PASS | 0 errors; TOC/`pre`/`code` нет |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/схема); Flesch RU 67.1 |
| cannibalization | PASS | 0 issues |
| utility gate | BLOCK | action_markers 1&lt;8; pain_markers 0&lt;2; outcome_markers 0&lt;3 |
| human voice gate | BLOCK | outcome_markers 2&lt;3 (`проверьте`,`выберите`); warn: 4× ровно-5-шаговые ol |

## Pain / solution / beginner-fit (ручная проверка)

| Вопрос | Статус | Где |
|--------|--------|-----|
| Боль новичка в lead | OK по смыслу | предоплата за «чистую» машину без понимания баз |
| Решение в H2 | OK | VIN → отчёт КНР → ГИБДД/ФНП → флаги → чек-лист 10 |
| Первый результат до FAQ | OK по смыслу | пакет: VIN + отчёт + скрины + стоп-список |
| Термины «на пальцах» | OK | VIN/WMI, пустой ГИБДД = норма |
| Beginner-fit blocker | нет | тон не для профи/разработчиков |

Машинные gates (utility pain/outcome + human-voice outcome) всё равно BLOCK — см. FIX.

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 14/20 | H1/primary OK; CTA-ссылки битые |
| GEO / citability | 18/25 | схема, таблица, FAQ×6, чеклист; инсайт с ярлыком TL;DR |
| CORE-EEAT lite | 16/20 | см. ниже |
| Human voice | 6/15 | human-voice BLOCK |
| Fact safety | 13/15 | fact-check PASS |
| Contract HTML | 8/10 | whitelist PASS; CTA href invalid |
| **Итого** | **62/100** | |

## CORE-EEAT lite: 16/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | primary в H1/meta |
| C02 | ✓ | lead = боль + ответ |
| C03 | ✓ | читатель: заказ авто из КНР, риск депозита |
| C04 | ✓ | VIN/отчёт/ГИБДД/ФНП объяснены |
| O01 | ✓ | H2 = action outline |
| O02 | ✓ | логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + table + checklist, mode B |
| R01 | ✓ | insight + схема + FAQ |
| R02 | ✓ | 73 тыс / окт 2026 / Автотека World — в research |
| R03 | ✓ | нет ложных цен лотов |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «сначала VIN и отчёт» |
| E02 | ✓ | Делать/Не делать в H2 (но маркеры policy не совпали) |
| E03 | ✗ | CTA URL = `[REDACTED]` — невалидны |
| Exp01 | ✓ | mode B |
| Exp02 | ✓ | тон Авто-Сейлс |
| Exp03 | ✓ | slop 0 |
| Ept01 | ✓ | лимиты баз / пустой ГИБДД |
| Ept02 | ✗ | нет internal blog links |

**Target:** ≥16/20 ✓ на грани · veto (R03 / Exp01 / slop≥2): нет  
**Blockers gates:** score&lt;80, link-verify fail, utility BLOCK, human-voice BLOCK

## Beginner-fit / utility narrative

- **Боль:** депозит за «чистую» машину из Китая без понимания, какие базы видят историю до ввоза.
- **Решение:** связка VIN с фото → китайский/зарубежный отчёт → ГИБДД+ФНП → чек-лист 10 → решение плачу/не плачу.
- **Первый результат:** пакет доказательств до перевода денег (20–40 минут).
- **Сложные термины:** VIN/WMI, пустой ГИБДД до учёта в РФ.

## Blockers (машинные)

1. `human-voice-report.json` **BLOCK** — `outcome_markers` 2 &lt; 3  
2. `utility-gate-report.json` **BLOCK** — action 1&lt;8; pain 0&lt;2; outcome 0&lt;3  
3. `link-verify.json` **fail** — CTA href не URL  

## FIX для Writer (цикл 1) — не чинить в GEO QA

1. **CTA URLs (blocker):** во всех `<a href="...">` заменить литерал `[REDACTED]` на реальные URL из `memory/brief/conversion-map.md` (каталог ×2 + Telegram ×1). Перезапустить `excalibur_blog_link_verify.py` → verdict pass.
2. **Action/recommendation markers (utility, ≥8):** в теле использовать **точные** фразы из `editorial-policy.json` → `recommendation_markers_ru`:  
   `сделайте`, `не делайте` (не «Делать/Не делать»), `проверьте`, `избегайте`, `шаг ` (с пробелом, напр. «Шаг 1»), `чеклист` (без дефиса), `используйте`, `ориентир`. Цель: `action_markers ≥ 8`.
3. **Human voice outcome (≥3 разных маркера):** добавить в lead/H2/«Что дальше» минимум ещё один из: `результат`, `получите`, `сможете`, `соберите`, `запустите`, `исправьте` (сейчас есть только `проверьте` + `выберите`).
4. **Инсайт-блок:** убрать ярлык `TL;DR` / `Быстрый инсайт` (контракт skill); оставить суть в `<blockquote>` без шаблонного префикса.
5. **Списки:** сейчас 4× `ol` ровно по 5 пунктов — разнести длины (напр. 4/5/6/10), чтобы снять warn human-voice.
6. **Не трогать** смысловой каркас pain→solution; не раздувать char_count водой.

## Policy blocker (не Writer) — Fixer

`memory/brief/editorial-policy.json` **не содержит** `pain_markers_ru` / `outcome_markers_ru`, а `excalibur_blog_utility_gate.py` требует `min_pain_markers=2` и `min_outcome_markers=3` с дефолтами. На текущем policy **любая** статья (включая AS08/AS09) получает utility BLOCK по pain/outcome=0.  
Incident: `memory/pipeline-fix-queue.md#INC-20261016-0924-geo-qa-utility-policy-markers-missing`  
**До повторного GEO QA:** Fixer обязан дописать списки маркеров в policy (или ослабить min до 0, если маркеры только в human-voice). Иначе Writer не сможет получить utility PASS даже после FIX 1–5.

## Reports (paths)

- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/research-notes-gate.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/fact-check-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/link-verify.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/html-linter-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/slop-detector-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/cannibalization-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/utility-gate-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/human-voice-report.json`
- `memory/blog/articles/B01-kak-proverit-avto-iz-kitaya-po-vin-do-depozita-2026/article-qa.md`

## Gate

- score ≥ 80 → **62** ✗  
- CORE-EEAT ≥ 16/20 → **16/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✗  
- human voice PASS → ✗  

**Итог:** FAIL — вернуть Writer (FIX выше) + Fixer по policy markers. Cover/schema/publish **не** запускать.
