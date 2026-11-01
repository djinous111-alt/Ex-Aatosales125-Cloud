# Article QA — AS04

**topic_id:** AS04  
**slug:** utilsbor-na-avto-2026  
**article_dir:** memory/blog/articles/AS04-utilsbor-na-avto-2026  
**date:** 2026-11-01  
**verdict:** FAIL  
**score:** 76

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic false-positive (official docs) |
| fact-check | WARNING | 15 stats; verified 2 / unverified 13 vs fact-bank (льгота 3400/5200, 160 л.с., ПП даты — в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long; Flesch RU 68.0 |
| cannibalization | PASS | 0 issues (3 article metas loaded) |
| utility gate | **BLOCK** | action_markers 5&lt;8; pain_markers 0&lt;2; outcome_markers 0&lt;3 |
| human voice gate | **BLOCK** | outcome_markers в тексте только 2 (`получите`, `соберите`) &lt; 3; warn: 3× ровно-5 списков |

## Beginner-fit

- **PASS (контент):** утильсбор / кВт / 30-минутная мощность / ТПО / льгота объяснены «на пальцах»; первый шаг — 5 полей до депозита без «команды юристов».
- Боль новичка: посчитать утильсбор «на глаз» / по чужому скрину и переплатить из‑за порога 160 л.с.
- Решение: H2 чек-лист льготы + поля + каталог; результат до FAQ — «льгота/не льгота + свежая цифра по лоту».

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 actionable; CTA каталог×2+TG; мало blog internal |
| GEO / citability | 22/25 | Insight, схема, таблица KR/CN/JP, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 10/15 | Живой lead/story OK; **gate BLOCK** по outcome-маркерам |
| Fact safety | 12/15 | Цифры в research-notes; fact-bank почти пуст по теме |
| Contract HTML | 10/10 | Whitelist PASS, ~8939, FAQ, CTA, без форм |
| Utility / gates | 0/10 | utility BLOCK + human-voice BLOCK → veto |
| **Итого** | **76/100** | score&lt;80 + gate veto → FAIL |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «утильсбор на авто 2026» в title/H1 |
| C02 | ✓ | Lead: боль «на глаз» + чек-лист до депозита |
| C03 | ✓ | Читатель: физлицо, ввоз KR/CN/JP через Владивосток |
| C04 | ✓ | кВт, льгота, коммерция, 30-мин мощность объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логика: логика → страны → льгота → ошибки → миф → 5 полей |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + blockquote schema; mode B |
| R01 | ✓ | Insight + схема до депозита + FAQ |
| R02 | ✓ | 3400/5200, 117,68 кВт, ПП 1291/1713, Интерфакс 31.03.2026 — в notes |
| R03 | ✓ | Нет статичной таблицы коммерческих миллионов; CTA в каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «страна ≠ ставка» + порог 160 л.с. |
| E02 | ✓ | «Делать / Не делать» в секциях (но маркеры policy — другие формы) |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Миф 01.04.2026, лимиты льготы, гибриды |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |
| Ept02b | ✗ | (учтено в Ept02) — только каталог + TG |

**Target:** ≥16/20 ✓ · veto gates: utility + human-voice · veto R03/Exp01/slop≥2: нет

## Pain / solution map (контент)

| Боль | Где решение | Результат читателя |
|------|-------------|--------------------|
| Скрин «3–5 тыс» без своих кВт | Lead + H2 пять полей | Пакет полей до депозита |
| Миф «из Кореи утиль дешевле» | H2 сравнение KR/CN/JP | Страна не меняет формулу |
| Льгота vs коммерция | H2 чек-лист 3400/5200 | Ясно «льгота / не льгота» |
| Гибрид/EV мощность | H2 ошибки мощности | Спросить 30-мин кВт из документов |
| Миф 1 апреля 2026 | H2 ЕАЭС | Не путать с прямым ввозом |

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 68.0

## Schema ready

BlogPosting: yes (после FIX) | FAQPage: yes (6) | HowTo: yes | Review: no | cover/schema: **не стартовать** до PASS

## Blockers

1. **utility-gate BLOCK** — `action_markers=5 < 8` (форма «Делать/Не делать» ≠ policy `сделайте/не делайте`; `чек-лист` ≠ `чеклист`).
2. **utility-gate BLOCK** — `pain_markers_ru` / `outcome_markers_ru` **отсутствуют в** `memory/brief/editorial-policy.json`, при этом скрипт требует min 2/3 → **вечный BLOCK** даже после правок writer (durable bug → fixer).
3. **human-voice BLOCK** — outcome lexicon hits = 2 (`получите`, `соберите`) &lt; 3; нужно ≥1 доп. маркер (`результат` / `проверьте` / `выберите` / `сможете` …).

## FIX (writer) — цикл 1

1. **Action markers ≥8:** в 3+ местах явно вставить токены из policy, напр. «Проверьте …», «Сделайте …», «Не делайте …», «чеклист» (без дефиса) или «Шаг N:» — сейчас только `избегайте`×1 + `ориентир`×4.
2. **Human-voice outcome ≥3:** добавить в lead/итог/«Что дальше» явную пользу: «результат», «проверьте», «выберите» или «сможете» (достаточно одного нового корня).
3. **Списки:** сейчас 3 списка ровно по 5 пунктов — развести размеры (4/5/6+), чтобы снять warning.
4. **Insight (желательно):** заменить ярлык `TL;DR / Быстрый инсайт` на нейтральный (`Коротко:` / `Сразу к делу:`) — skill запрещает шаблонный ярлык (linter сейчас PASS, но контракт writing).
5. **Не трогать** формулу/цифры льготы без сверки research-notes; fact-bank soft — опционально.

## FIX (fixer / director) — до бессмысленного writer-retry по utility

1. Добавить в `memory/brief/editorial-policy.json` `pain_markers_ru` / `outcome_markers_ru` (или не считать min, если списков нет; убрать `or 2`/`or 3` в пользу явного default).
2. См. incident `INC-20261101-0919-geo-qa-utility-pain-outcome-policy-gap`.

## Gate

- score ≥ 80 → **76** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✗  
- human voice gate PASS ✗  
- beginner-fit PASS ✓ (контент)

**Итог:** FAIL — cover \|\| schema **не** запускать. Вернуть writer по FIX 1–4; параллельно fixer по policy/script gap.
