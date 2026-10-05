# Article QA — B01 (retry after Writer FIX cycle 1 + Fixer)

**topic_id:** B01  
**slug:** rastamozhka-avto-iz-kitaya-vladivostok-2026  
**article_dir:** memory/blog/articles/B01-rastamozhka-avto-iz-kitaya-vladivostok-2026  
**date:** 2026-10-05  
**retry:** after FIX cycle 1 (action_markers) + Fixer (pain/outcome policy + elpts soft 403)  
**verdict:** FAIL  
**score:** 79  
**human_voice:** PASS  
**beginner_fit:** PASS  

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | errors=[]; research_date=2026-10-05 |
| fact-check | PASS | 5 extracted; verified 1 (`2026`); soft: `180 дней`, `180`, `160`, `2025` not in fact-bank |
| link-verify | FAIL | elpts `dp.elpts.ru/portal` → soft-pass warning (403 bot-block, ok=true); **1 fail:** unique href=`[REDACTED]` (literal placeholder, 3× in HTML) → checked as `PUBLIC_SITE_URL/[REDACTED]` → HTTP 404 |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 cliches; 7 over-long; Flesch RU 58.4 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers=34; pain_markers=6; outcome_markers=13 |
| human voice gate | PASS | errors=[]; warnings=[]; exactly_five_lists=1 (ok) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит «вслепую», простой на СВХ, путаница ДФО/транзит и СБКТС/ЭПТС до выдачи |
| Где решена | Lead (Новосибирск) + H2 пакет до депозита / ветка ДФО / цепочка Владивосток / stop-флаги / СБКТС+ЭПТС |
| Первый результат | Чеклист документов + выбранная ветка + критерий «готова только после выпуска+СБКТС+ЭПТС» до FAQ |
| Термины «на пальцах» | СВХ, ПТД, выпуск, СБКТС, ЭПТС объяснены в цепочке |
| Beginner-fit | PASS — первый безопасный шаг до депозита |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 15/20 | Primary в title/H1; H2 actionable; CTA-якоря есть, но href=`[REDACTED]` (мёртвые); нет 2–3 internal blog links |
| GEO / citability | 22/25 | TL;DR, схемы, таблицы, FAQ×6, критерий успеха; 7 over-long |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice-report PASS |
| Fact safety | 8/15 | Нет статичных сумм; soft unverified 180/160; **link-verify FAIL на CTA placeholders** |
| Contract HTML | 5/10 | html-linter PASS + utility PASS; **link-verify FAIL** (3× `[REDACTED]` href) |
| **Итого** | **79/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка авто из китая» в title/H1 |
| C02 | ✓ | Lead — история депозита + прямой ответ про чеклист |
| C03 | ✓ | Новичок / заказ из Китая через Владивосток |
| C04 | ✓ | СВХ/ПТД/СБКТС/ЭПТС расшифрованы |
| O01 | ✓ | H2 = пакет → ветка → цепочка → платежи → stop → ЭПТС → дальше |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы + blockquote-схемы |
| R01 | ✓ | TL;DR, схема ветки, цепочка, критерий успеха |
| R02 | ✓ | 01.01.2026 / 180 дней / отложенный утиль — в research-notes |
| R03 | ✓ | Нет готовых сумм пошлин/утиля |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «пакет и ветка раньше денег», Владивосток |
| E02 | ✓ | «Сделайте / Не делайте» + action markers ≥8 |
| E03 | ✗ | CTA-текст есть, но href=`[REDACTED]` — ссылки нерабочие |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Риски СВХ, 180 дней, мощность, посредник |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate fail:** link-verify (не score alone)

## Link verify

- total unique: 2 (elpts + `[REDACTED]`); HTML occurrences of `[REDACTED]` href: 3
- elpts: soft-pass warning (403, ok=true) — Fixer soft-host работает
- failed: `href="[REDACTED]"` → 404 (не URL каталога/Telegram)
- v1 (commit e1f4605) имел рабочие CTA (`https://avto-sales125.ru/`, `https://t.me/avtosales125`); FIX cycle 1 заменил их на placeholder
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 7
- Flesch RU: 58.4

## Schema ready

BlogPosting: blocked | FAQPage: yes (6) | HowTo: yes | Review: no | cover/schema: **blocked until QA PASS**

## Blockers

1. **link-verify FAIL** — в `article.html` три CTA с буквальным `href="[REDACTED]"` (каталог×2 + Telegram×1). Placeholder попал из redacted brief/`[REDACTED]` в fact-bank/site-brief; это не валидный URL.

## FIX → Writer (cycle 2)

Обязательно до повторного GEO QA (text-only, **не** полный рерайт):

1. Заменить **все** `href="[REDACTED]"` на канонические CTA как в AS09 / site-brief brand (не копировать слово `[REDACTED]` из brief):
   - каталог: `https://avto-sales125.ru/`
   - Telegram: `https://t.me/avtosales125`
2. **Не** подставлять значение `PUBLIC_SITE_URL` / `WP_SITE_URL` из secrets, если домен отличается от brand `avto-sales125.ru` (риск secret-scan scrub).
3. Сохранить: action_markers ≥8, «Сделайте/Не делайте», char ~8500–9500, FAQ×6, без TOC, без статичных сумм пошлин, elpts URL без изменений.
4. Локально: `python3 scripts/excalibur_blog_link_verify.py article.html -o link-verify.json --site-base "$PUBLIC_SITE_URL"` → verdict **pass** (elpts soft warning допустим).

После FIX → повторный `excalibur-blog-geo-qa`. **Не** cover||schema до PASS.

## Paths

- `article.html`
- `article.meta.json`
- `article-qa.md`
- `research-notes-gate.json`
- `fact-check-report.json`
- `link-verify.json`
- `html-linter-report.json`
- `slop-detector-report.json`
- `cannibalization-report.json`
- `utility-gate-report.json`
- `human-voice-report.json`

## incident_report

`memory/pipeline-fix-queue.md#INC-20261005-1335-geo-qa-cta-href-redacted-placeholder`
