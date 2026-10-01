# Article QA — B06

**topic_id:** B06  
**slug:** avto-iz-kitaya-s-probegom-proverka-do-oplaty-2026  
**article_dir:** memory/blog/articles/B06-avto-iz-kitaya-s-probegom-proverka-do-oplaty-2026  
**date:** 2026-10-01  
**verdict:** FAIL  
**score:** 72  
**human_voice:** BLOCK  
**utility:** BLOCK (real: action_markers 3&lt;8; default-policy also false-fails pain/outcome — see incident)

## Pain / solution / beginner-fit (ручная проверка)

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Боюсь перевести депозит за «почти новую», а лот ≤180 дней застрянет без экспортной лицензии |
| Где в lead | История Ивана + «депозит в работе» / лот у границы |
| Где решение (H2) | 180 дней по 行驶证 → пакет сканов → письмо завода → красные флаги → чек-лист до перевода |
| Первый результат до FAQ | H2 «Что сделать сегодня»: дата регистрации, нужен ли letter, депозит не уходит при неполном пакете |
| Термины «на пальцах» | 行驶证 (права+учёт), 交强险 (базовая страховка), After-Sales Service Confirmation Letter / 售后维修服务确认书 |
| Beginner-fit | PASS (не для профи-разработчиков; есть первый безопасный шаг без команды) |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | status PASS; research_date 2026-10-01 |
| fact-check | PASS | 6 extracted / 1 verified in fact-bank; soft unverified (180 дней, Shangmao Han 648) — есть в research-notes |
| link-verify | PASS | 2/2 OK (Telegram + каталог); failed_count=0 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 67.7 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | BLOCK | **канонический re-run с marker lists:** action_markers **3 &lt; 8**; pain=8, outcome=3. Default `editorial-policy.json` без `pain_markers_ru`/`outcome_markers_ru` → ложный 0&lt;2/0&lt;3 (см. incident) |
| human-voice gate | BLOCK | `outcome_markers` unique **2 &lt; 3** (`результат`, `соберите`); pain OK; concrete OK; reader_* overlap OK. WARN: 4× exactly-5-step lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/meta; H2 how-to; CTA; мало blog internal |
| GEO / citability | 20/25 | Insight, схема, таблица, FAQ×6, чеклисты |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 8/15 | BLOCK: outcome unique &lt;3; иначе голос живой |
| Fact safety | 12/15 | Норма 180 дней + источники; не всё в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, FAQ, CTA, без форм |
| Utility action | 0/10 | action_markers 3&lt;8 — gate BLOCK |
| **Итого** | **72/100** | &lt;80 → FAIL |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из Китая с пробегом» в H1 / title_seo |
| C02 | ✓ | Lead сразу про проверку до оплаты |
| C03 | ✓ | Читатель: новичок с депозитом за б/у из Китая |
| C04 | ✓ | 行驶证 / 交强险 / letter объяснены |
| O01 | ✓ | H2 = research outline (до депозита → 180 → сканы → letter → флаги → чеклист → результат → FAQ) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote workflow, mode B |
| R01 | ✓ | «Коротко по делу», схема, FAQ |
| R02 | ✓ | Shangmao Han [2025] No. 648, Автостат, VL.ru |
| R03 | ✓ | Нет фейковых точных пошлин; «цифры плывут» |
| R04 | ✓ | FAQ отвечает с 1-го предложения |
| E01 | ✓ | Угол «до депозита», не калькулятор пошлин |
| E02 | ✓ | «Делать / Не делать» |
| E03 | ✓ | CTA каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person hero |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Письмо не от дилера; ≤180 без letter = стоп |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Но:** utility + human-voice gates BLOCK → итоговый PASS запрещён.

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 67.7

## Schema ready (после PASS)

BlogPosting: pending | FAQPage: pending (6) | HowTo: pending | — cover/schema **не** запускать до PASS

## Blockers

1. **human-voice-report.json BLOCK** — unique outcome markers 2 &lt; 3.
2. **utility-gate-report.json BLOCK** — recommendation/action markers 3 &lt; 8.
3. Score 72 &lt; 80.

## FIX → вернуть Writer (не править GEO QA)

Цикл 1/2. Переписать/дополнить `article.html` **без** смены угла темы. Не трогать research-notes.

### A. Utility action-маркеры (≥8 вхождений из списка policy)

В тексте сейчас матчятся только: `не делайте`×1, `шаг `×1, `добавьте`×1 (=3).

Добавить естественные императивы из `recommendation_markers_ru`:

- `сделайте`, `проверьте`, `используйте`, `избегайте`, `уберите`
- `ориентир`, `чеклист` (**без дефиса** — `чек-лист` **не** считается)
- ещё `шаг ` в финальном ol (`Шаг 1.`, `Шаг 2.` …)

Цель: `action_markers ≥ 8` в `utility-gate-report.json`.

### B. Human voice outcome (≥3 **уникальных** маркера)

Сейчас: `результат`, `соберите`. Нужен ещё ≥1 из:

`получите` | `сможете` | `проверьте` | `выберите` | `запустите` | `сэконом` | `настройте` | `исправьте`

Пример в H2 «Что сделать сегодня»: «Проверьте дату регистрации — получите ясный вердикт платить/не платить».

### C. WARN (желательно)

Разнести длины `<ol>`: сейчас 4 списка ровно по 5 пунктов → human-voice warning `exactly_five_lists`. Сделать 4/6/7/9 и т.п.

### D. Не менять

- Угол «до депозита / 180 дней / сканы / letter»
- Fact Check Box с «Редакция Авто-Сейлс»
- Whitelist HTML (без TOC/`pre`/`code`)

После правок Writer: снова `Task(excalibur-blog-geo-qa)` / generalPurpose GEO QA.

## Gate

- score ≥ 80 → **72** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✗  
- human voice gate PASS ✗  
- beginner-fit PASS ✓  

**Итог:** FAIL — cover || schema **не** запускать. Вернуть Writer по FIX A–C.

## Incident

- `memory/pipeline-fix-queue.md#INC-20261001-0935-geo-qa-utility-pain-outcome-empty-policy`
