# Article QA — B06

**topic_id:** B06  
**slug:** lgotnyy-utilsbor-fizlico-2026-kak-proverit  
**article_dir:** memory/blog/articles/B06-lgotnyy-utilsbor-fizlico-2026-kak-proverit  
**date:** 2026-07-25  
**verdict:** FAIL  
**score:** 72

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: false-positive technical (нет official docs URL) |
| fact-check | PASS | 10 stats; 3 verified / 7 unverified (пороги 160/117,68 и даты в research-notes, не в fact-bank) |
| link-verify | **FAIL** | 1 checked link → 404; все 3 CTA `href` в HTML = литерал `[REDACTED]` (не URL) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/схема + длинный insight); Flesch RU 71.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 38 / pain 10 / outcome 21; lists+FAQ×7+tables×2 |
| human-voice-gate | PASS | `human-voice-report.json` status PASS; story/pain/outcome overlap OK |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 по чеклисту; CTA сломаны литералом `[REDACTED]` |
| GEO / citability | 20/25 | Insight, схема, таблицы, FAQ×7, чеклист 10; ярлык `TL;DR / Быстрый инсайт` нарушает контракт insight |
| CORE-EEAT lite | 17/20 | 17/20 (см. таблицу); нет internal blog links |
| Human voice | 14/15 | Gate PASS; лёгкий штраф за шаблонный ярлык insight |
| Fact safety | 12/15 | Пороги/даты согласованы с research-notes; 7 unverified vs fact-bank |
| Contract HTML | 3/10 | Whitelist OK, но CTA href = `[REDACTED]` → link-verify fail (блокер) |
| **Итого** | **72/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «льготный утильсбор» в meta title / H1 |
| C02 | ✓ | Lead: депозит + ложная ставка «я физлицо» → чеклист до оплаты |
| C03 | ✓ | Читатель-новичок, ввоз через Владивосток / Азия |
| C04 | ✓ | кВт, 30-мин. мощность, параллельный/последовательный гибрид «на пальцах» |
| O01 | ✓ | H2 = боль → мощность → гибрид → 1 авто/год → ЕАЭС → чеклист → расчёт → дальше |
| O02 | ✓ | Логичный outline checklist mode B |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol + таблицы + blockquote-схема |
| R01 | ✓ | Insight + схема до депозита + FAQ |
| R02 | ✓ | ПП 1713 / 01.12.2025 / порог 117,68 кВт в Fact Check Box + research |
| R03 | ✓ | Нет коммерческих сумм утиля; CTA в каталог на расчёт по VIN |
| R04 | ✓ | Ответ FAQ с первого предложения |
| E01 | ✓ | Угол «льгота ≠ статус физлица» + чеклист до депозита |
| E02 | ✓ | «Делать / Не делайте» в секциях |
| E03 | ✗ | CTA-ссылки битые (`href="[REDACTED]"`) — не рабочие каталог/Telegram |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Граница 117,68 vs 117,69; EV 80 л.с.; СВО/многодетные ≠ закон |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate fail:** link-verify FAIL (обязательный Pass-критерий skill)

## Beginner-fit / utility story

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Думает, что «льготный утильсбор» положен любому физлицу → риск коммерческого тарифа из‑за 161 л.с. / гибрида / ранней продажи |
| Где решение | H2 про статус, кВт, гибрид/EV, лимит 1 авто/год, чеклист 10 пунктов |
| Первый результат | Заполненный чеклист «да/нет» до депозита; при «нет» — расчёт в каталоге, не оплата |
| Термины «на пальцах» | кВт vs л.с.; 30-минутная мощность; последовательный vs параллельный гибрид |

## Link verify

- total checked: 1, failed: 1 (verdict **fail**)
- root cause: в `article.html` все 3 `href` = литерал `[REDACTED]` (не URL из conversion-map)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблиц + длинный insight)
- Flesch RU: 71.1

## Schema ready

BlogPosting: yes (после FIX ссылок) | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

1. **link-verify FAIL:** заменить все `href="[REDACTED]"` на рабочие CTA из `memory/brief/conversion-map.md` (строки «Каталог авто» и «Telegram Авто-Сейлс»), как в AS08/AS09. Три вхождения в блоках расчёта / «Что дальше».
2. **Insight label (контракт):** убрать шаблонный ярлык `TL;DR / Быстрый инсайт` из первого blockquote; оставить смысл инсайта без этих слов (skill HTML/writer).

## FIX cycle (QA → writer) — cycle 1

1. **CRITICAL:** восстановить валидные абсолютные CTA URL (каталог ≤3, Telegram ≤2) из conversion-map / эталон AS08–AS09; не писать литерал `[REDACTED]` в HTML.
2. **REQUIRED:** переименовать insight-блок без `TL;DR` и без фразы `Быстрый инсайт`.
3. **OPTIONAL:** 2–3 internal blog links с `anchor_variants` после появления URL соседних постов; дописать пороги 160 л.с. / 117,68 кВт в fact-bank.

После FIX — повтор GEO QA (link-verify + human-voice + article-qa). **Не** стартовать cover||schema.

## Gate

- score ≥ 80 → **72** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → **FAIL** ✗  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓ (смысл OK; CTA сломаны отдельно)

**Итог:** FAIL — вернуть writer (FIX cycle 1). Cover/schema запрещены.
