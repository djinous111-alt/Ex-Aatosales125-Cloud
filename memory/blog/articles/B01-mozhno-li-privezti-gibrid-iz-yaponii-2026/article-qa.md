# Article QA — B01

**topic_id:** B01  
**slug:** mozhno-li-privezti-gibrid-iz-yaponii-2026  
**article_dir:** memory/blog/articles/B01-mozhno-li-privezti-gibrid-iz-yaponii-2026  
**date:** 2026-10-14  
**verdict:** FAIL  
**score:** 68  
**human_voice:** BLOCK  
**utility_gate:** BLOCK  
**beginner_fit:** PASS (контент для новичка ок; маркеры голоса/utility — нет)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic false-positive (known INC) |
| fact-check | PASS | 3 facts; 2023/2024 unverified vs fact-bank (есть в research-notes) |
| link-verify | FAIL | 1 checked link → 404; оба `href` в HTML = литерал `[REDACTED]` |
| html-linter | PASS | whitelist OK, TOC нет, pre/code нет |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 72.1 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | BLOCK | action_markers 4&lt;8; pain_markers 0&lt;2; outcome_markers 0&lt;3 |
| human voice gate | BLOCK | outcome_hits 2&lt;3 (`результат`, `проверьте`); WARN: 2× списка ровно из 5 пунктов |

## Pain / solution / beginner (обязательная фиксация)

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Путает любой Hybrid с разрешённым вывозом; риск депозита за полный/PHEV/EV/e-POWER (lead: Freed GB7 vs GP3) |
| Где решение | H2: мягкий vs полный → чтение листа/кузова → красные флаги → чек-лист 10 → «что сделать сегодня» |
| Первый результат | Код кузова + вердикт мягкий/стоп + ДВС ≤1,9 л **до** депозита |
| Термины «на пальцах» | mild / полный / PHEV / e-POWER / аукционный лист / код кузова |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 14/20 | Title/H1/primary ок; CTA-ссылки сломаны (`[REDACTED]`) |
| GEO / citability | 18/25 | TL;DR, таблица, FAQ×6, чеклисты; outcome-маркеры для gate слабые |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 6/15 | gate BLOCK (outcome markers) |
| Fact safety | 12/15 | даты 2023/2024 не в fact-bank; тон осторожный |
| Contract HTML | 7/10 | whitelist PASS; href placeholders; char_count 8607 |
| **Итого** | **68/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в title/H1 |
| C02 | ✓ | Lead: можно, но не любой Hybrid |
| C03 | ✓ | Новичок до депозита |
| C04 | ✓ | Термины объяснены |
| O01 | ✓ | H2 = pain→solution map |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + mode B |
| R01 | ✓ | TL;DR + схема + FAQ |
| R02 | ✓ | Ноябрь 2024 / август 2023 + кузова в тексте |
| R03 | ✓ | Нет копирования пошлин; «расчёт под лот» |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки / шильдик ≠ разрешение» |
| E02 | ~ | Есть «Делать/Не делать», но utility ждёт «сделайте/не делайте» |
| E03 | ✗ | CTA href = `[REDACTED]` (не рабочие ссылки) |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop 0 |
| Ept01 | ✓ | Сверка кузова «на сегодня» |
| Ept02 | ✗ | Нет внутренних blog-links на другие посты |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate score ≥80:** ✗ (68)

## FIX для Writer (обязательно; article.html GEO QA не правил)

1. **Ссылки (blocker link-verify):** заменить оба `href="[REDACTED]"` на реальные URL каталога и Telegram из `shared/authors-registry.json` / site-brief (как в AS09: каталог + `t.me/avtosales125`). Не оставлять placeholder.
2. **Utility action-маркеры (≥8):** сейчас 4 (`проверьте`×2, `ориентир`×2). Заменить/добавить формы из policy: `сделайте`, `не делайте` (вместо «Делать/Не делать»), `проверьте`, `избегайте`, `используйте`, `шаг ` (с пробелом), при необходимости `чеклист` без дефиса. Цель: ≥8 hits.
3. **Human voice outcome (≥3 маркера из списка gate):** добавить в lead/H2 «сегодня»/итог явные слова: `получите`, `сможете`, `выберите` (уже есть `результат`, `проверьте` — нужно ≥3 уникальных маркера из OUTCOME_MARKERS).
4. **Списки по 5 пунктов:** сейчас 2× ровно 5 `<li>` (WARN). Укоротить/удлинить один список (4 или 6), чтобы не было двух identical-size пятёрок.
5. **(опционально soft)** дописать 2023/2024 в fact-bank или оставить как soft; 2–3 internal blog links с `anchor_variants` после появления URL других постов.

## Blockers (не writer-only)

- **Utility pain/outcome policy gap:** в `memory/brief/editorial-policy.json` отсутствуют `pain_markers_ru` и `outcome_markers_ru`, при этом `excalibur_blog_utility_gate.py` требует min 2/3. При пустых списках счётчики всегда 0 → utility **непроходим** правками текста. Нужен Fixer: добавить списки маркеров (+ min_* в `article_required_signals` при необходимости). См. incident ниже.

## Gate checklist

- score ≥ 80 → **68** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- research notes gate PASS → ✓  
- utility gate PASS → ✗  
- human voice gate PASS → ✗  
- beginner-fit PASS → ✓ (смысл); маркеры — через FIX writer  

**Итог:** FAIL — вернуть Writer (FIX 1–4). Параллельно Fixer: policy pain/outcome markers. Cover/schema **не** запускать.
