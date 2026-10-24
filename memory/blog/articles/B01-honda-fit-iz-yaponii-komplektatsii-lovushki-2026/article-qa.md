# Article QA — B01

**topic_id:** B01  
**slug:** honda-fit-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-honda-fit-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-25  
**verdict:** FAIL  
**score:** 84

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical_topic false-positive (см. INC-0018) |
| utility gate (article) | **BLOCK** | `pain_markers=0 < 2`, `outcome_markers=0 < 3` — маркеры в `editorial-policy.json` пустые (false fail) |
| human-voice-report | PASS | pain/outcome hits есть; warn: 2× exactly-5-step lists |
| fact-check | PASS | 6 stats; verified 1; unverified: 2022/2023/1900/2024/9 973 (в research-notes) |
| link-verify | PASS | 2/2 OK; `--site-base` из `PUBLIC_SITE_URL` |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 7 over-long (часть — склейка table/blockquote); Flesch RU 79.9 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Ставка на Fit/HYBRID по красоте и оценке 4.5 без кода кузова → риск непроходного полного гибрида/e:HEV и депозита вслепую |
| Где решение | H2: матрица кодов → бензин/мягкий/e:HEV → грейды после 10.07.2026 → флаги R/RA/CVT → чеклист 10 пунктов |
| Первый результат до FAQ | Shortlist «можно/нельзя» по кодам, понятные грейды, заполненный чеклист; HYBRID/e:HEV отсеяны до депозита |
| Термины «на пальцах» | Мягкий гибрид IMA vs полный i-DCD/e:HEV; грейд ≠ разрешение на вывоз; оценка ≠ индульгенция |
| Beginner-fit | PASS (не профи-тон; есть безопасный первый шаг без «команды разработчиков») |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в meta/H1; CTA каталог×2 + Telegram×1; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт, таблица кодов, схема →, FAQ×6, чеклист×10 |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | Gate PASS; ярлык «TL;DR / Быстрый инсайт» — skill-soft fail |
| Fact safety | 12/15 | METI/Honda/Autostat в Fact Check; часть цифр не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9358 chars, mode B, FAQ, без форм |
| **Итого** | **84/100** | score ≥80 ✓, но utility gate BLOCK → pipeline FAIL |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «хонда фит из японии» в title_seo / H1 |
| C02 | ✓ | Lead — боль ставки без кода кузова |
| C03 | ✓ | Читатель: новичок на аукционе Fit до депозита |
| C04 | ✓ | GP/GS/e:HEV, BASIC→X, R/RA, CVT объяснены |
| O01 | ✓ | H2 = research action outline |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 (≥5) |
| O04 | ✓ | ol + table + checklist, mode B |
| R01 | ✓ | Инсайт + схема + таблица + FAQ |
| R02 | ✓ | Autostat ~9973; METI с 09.08.2023; Honda minor 10.07.2026 |
| R03 | ✓ | Нет цен лотов / готовых пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «код до фото / до депозита» |
| E02 | ✓ | «Сделайте / Не делайте / Проверьте» |
| E03 | ✓ | CTA каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: e:HEV стоп, GP1/GP4 только со сверкой |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Gate checklist (обязательные для PASS)

| Gate | Required | Actual |
|------|----------|--------|
| research-notes-gate | PASS | PASS ✓ |
| utility gate статьи | PASS | **BLOCK** ✗ |
| human-voice-report | PASS | PASS ✓ |
| link-verify | pass | pass ✓ |
| score ≥ 80 | yes | 84 ✓ |
| CORE-EEAT ≥ 16/20 | yes | 18/20 ✓ |
| beginner-fit | PASS | PASS ✓ |

## Blockers

1. **Utility gate BLOCK (mandatory):** `pain_markers=0`, `outcome_markers=0` при пустых `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json`. Human-voice gate на тех же смыслах PASS (hits: боль/ошиб/долго + результат/получите/сможете/проверьте/выберите). Это false fail скрипта/policy — см. incident ниже. Cover||schema **не** стартовать.

## FIX для Writer (цикл 1)

### A. После Fixer поправит policy (предпочтительный путь)

Перезапустить только:

```bash
python3 scripts/excalibur_blog_utility_gate.py \
  --article-dir memory/blog/articles/B01-honda-fit-iz-yaponii-komplektatsii-lovushki-2026 \
  --output utility-gate-report.json
```

Текст B01 уже содержит маркеры human-voice (`боль`, `ошибк*`, `результат`, `получите`, `сможете`, `проверьте`, `выберите`) — **полный рерайт не нужен**, если Fixer выровняет списки маркеров.

### B. Обязательные правки article.html (whitelist-safe), даже если utility починится policy

1. **Инсайт-блок:** убрать ярлык `TL;DR / Быстрый инсайт:` — начать сразу с сути («Сначала код кузова, потом фото…»). Skill: инсайт не должен начинаться с этих шаблонов.
2. **Списки:** human-voice warn — два списка ровно по 5/6 шагов; при правке развести длины (например 4 и 7), не плодить ещё один ровно-5.

### C. Soft / non-blocking

1. Дописать в fact-bank: Autostat Fit ~9973 (янв–авг 2026), METI export limit 09.08.2023 / 1900 см³, Honda Fit minor 10.07.2026.
2. Укоротить 1–2 длинных предложения в lead/Fact Check (slop over-long=7, часть — артефакт таблицы).
3. После публикации AS/B-серии — 2–3 internal blog links (Ept02).

## Schema ready (после PASS)

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes | Review: no | cover/schema: **blocked until QA PASS**

## Incident

`incident_report: memory/pipeline-fix-queue.md#INC-20261025-2130-geo-qa-utility-pain-markers-empty`

## Gate

- score ≥ 80 → **84** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- utility gate PASS ✗ → **FAIL**

**Итог:** FAIL — вернуть Writer (FIX B) + Fixer (policy markers); cover||schema не запускать.
