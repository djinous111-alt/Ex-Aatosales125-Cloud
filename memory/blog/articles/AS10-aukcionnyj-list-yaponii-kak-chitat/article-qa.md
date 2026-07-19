# Article QA — AS10

**topic_id:** AS10  
**slug:** aukcionnyj-list-yaponii-kak-chitat  
**article_dir:** memory/blog/articles/AS10-aukcionnyj-list-yaponii-kak-chitat  
**date:** 2026-07-20  
**verdict:** FAIL  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: false `technical_topic` (см. INC-0010) |
| fact-check | PASS | 2/2 verified (2026; 20 минут) |
| link-verify | FAIL | 1/1 failed: literal `href="[REDACTED]"` → 404 as internal_relative |
| html-linter | PASS | whitelist OK; TOC нет |
| slop-detector | PASS | 0 клише; 3 over-long (таблица/схема); Flesch RU 64.1 |
| cannibalization | PASS | 0 issues (3 metas loaded) |
| utility gate | BLOCK | action_markers 1<8; pain/outcome 0 — см. blockers |
| human-voice gate | BLOCK | outcome_markers 2<3 (`результат`, `проверьте`) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Шифр листа (4/4.5/R/A1/W…) → страх депозита «на красивую оценку» и скрытый ремонт |
| Где решение | H2: правило до депозита → шапка → оценки/салон → схема/примечания → фото → чек-лист → первый результат |
| Первый результат | За 15–20 мин закрыть чек-лист и сказать «беру / не беру / уточнение» с причиной |
| Термины «на пальцах» | 4/4.5/5, R/RA, салон A–E, A/U/W/X/XX/S/C — таблица + ul-легенда |
| beginner-fit | PASS (не профи-тон; есть безопасный первый шаг без команды) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 15/20 | Primary в title/H1; H2 action; CTA-ссылки битые |
| GEO / citability | 22/25 | Инсайт, схема, таблица, FAQ×7, чеклист 12 |
| CORE-EEAT lite | 17/20 | см. таблицу ниже |
| Human voice | 10/15 | concrete/pain OK; outcome <3 маркеров |
| Fact safety | 13/15 | fact-check PASS; источники в Fact Box |
| Contract HTML | 7/10 | linter PASS; literal `[REDACTED]` href; ярлык TL;DR |
| **Итого** | **74/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в meta/H1 |
| C02 | ✓ | Lead = боль + порядок чтения до депозита |
| C03 | ✓ | Новичок / заказ из Японии / депозит |
| C04 | ✓ | Оценки, салон, коды схемы объяснены |
| O01 | ✓ | H2 = pain_solution_map / checklist |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol 5 + ul чеклист + table; mode B |
| R01 | ✓ | Инсайт + порядок + FAQ |
| R02 | ✓ | Нюанс TAA vs USS 2026; источники в Fact Box |
| R03 | ✓ | Нет выдуманных цен лотов |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» |
| E02 | ✓ | «Делать / Не делать» (но utility считает только «сделайте/не делайте») |
| E03 | ✗ | CTA href = literal `[REDACTED]` (не живые URL) |
| Exp01 | ✓ | Mode B, reader_story Андрей |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты R/RA, XX≠рама, расхождение шкал |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог+TG, и те битые) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** score≥80 ✗ · link-verify ✗ · utility ✗ · human-voice ✗

## Link verify

- total: 1 unique broken pattern (оба CTA = literal `[REDACTED]`)
- failed: 1 (HTTP 404, kind=internal_relative)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 64.1

## Schema ready

BlogPosting: pending (после PASS) | FAQPage: yes (7) | HowTo: yes | cover/schema: **не запускать** до PASS

## Blockers

1. **link-verify FAIL** — в `article.html` стоят буквальные `href="[REDACTED]"` (не URL сайта/Telegram).
2. **utility gate BLOCK** — `action_markers=1` (нужно ≥8 из `recommendation_markers_ru`).
3. **utility gate BLOCK** — `pain_markers_ru` / `outcome_markers_ru` **отсутствуют** в `memory/brief/editorial-policy.json`, при этом скрипт требует min 2/3 → **любая** статья получает 0 (регрессия; см. incident).
4. **human-voice BLOCK** — outcome_markers только 2 из ≥3.

## FIX → Writer (цикл 1) — не longread с нуля

1. **CTA URLs:** заменить оба literal `href="[REDACTED]"` на абсолютные https-ссылки каталога и Telegram (как в PASSнувшем AS09 article.html). Не копировать плейсхолдер `[REDACTED]` из redacted examples.
2. **Utility action-маркеры ≥8:** вплести слова из policy: `сделайте`, `не делайте`, `проверьте`, `используйте`, `избегайте`, `чеклист` (без дефиса), `шаг `, `добавьте` / `уберите`. Сейчас «Делать:/Не делать:» **не** считаются; в тексте только 1×«проверьте».
3. **Human-voice outcome ≥3 разных маркера:** добавить ещё ≥1 из: `получите`, `сможете`, `выберите`, `сэконом…`, `соберите`, `настройте`, `исправьте` (уже есть `результат` + `проверьте`).
4. **Опционально (skill soft):** ярлык инсайта без шаблона `TL;DR` / `Быстрый инсайт` — переименовать в нейтральное («Коротко:» / «Суть:»), смысл блока сохранить.

## FIX → Fixer / Director (до повторного PASS utility)

5. **Policy/script:** добавить `pain_markers_ru` + `outcome_markers_ru` в `memory/brief/editorial-policy.json` **или** в `excalibur_blog_utility_gate.py` не применять min_pain/min_outcome, если списки маркеров пусты. Иначе utility article PASS недостижим текстом writer.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify → FAIL ✗  
- research-notes-gate → PASS ✓  
- utility gate → BLOCK ✗  
- human-voice → BLOCK ✗  

**Итог:** FAIL — cover \|\| schema **не** запускать. Вернуть Writer по FIX 1–4; параллельно Fixer по FIX 5 / incident.
