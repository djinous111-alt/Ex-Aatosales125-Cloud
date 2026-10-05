# Article QA — B01 (retry #2 after CTA restore)

**topic_id:** B01  
**slug:** rastamozhka-avto-iz-kitaya-vladivostok-2026  
**article_dir:** memory/blog/articles/B01-rastamozhka-avto-iz-kitaya-vladivostok-2026  
**date:** 2026-10-05  
**retry:** #2 after Director CTA restore from conversion-map  
**verdict:** PASS  
**score:** 92  
**human_voice:** PASS  
**beginner_fit:** PASS  

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | errors=[]; research_date=2026-10-05 |
| fact-check | PASS | 5 extracted; verified 1 (`2026`); soft: `180 дней`, `180`, `160`, `2025` not in fact-bank |
| link-verify | PASS | unique=3; failed_count=0; elpts soft-pass warning (403 bot-block, ok=true); catalog host `avto-sales125.ru` → 200; Telegram host `t.me` → 200 |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 cliches; 7 over-long; Flesch RU 58.4 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers=34; pain_markers=6; outcome_markers=13 |
| human voice gate | PASS | errors=[]; warnings=[] |

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
| SEO structure | 17/20 | Primary в title/H1; H2 actionable; CTA catalog×2 + Telegram×1 живые; нет 2–3 internal blog links |
| GEO / citability | 22/25 | TL;DR, схемы, таблицы, FAQ×6, критерий успеха; 7 over-long |
| CORE-EEAT lite | 15/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice-report PASS |
| Fact safety | 13/15 | Нет статичных сумм; link-verify PASS; soft unverified 180/160/2025 |
| Contract HTML | 10/10 | html-linter PASS + utility PASS + link-verify PASS |
| **Итого** | **92/100** | |

## CORE-EEAT lite: 19/20

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
| E03 | ✓ | CTA catalog (`avto-sales125.ru`) ×2 + Telegram (`t.me/avtosales125`) ×1, link-verify 200 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Риски СВХ, 180 дней, мощность, посредник |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gates:** research-notes PASS · utility PASS · human-voice PASS · link-verify PASS · beginner-fit PASS · score ≥80 ✓

## Link verify

- total unique: 3; failed_count: 0; verdict: **pass**
- elpts `dp.elpts.ru/portal`: soft-pass warning (403, ok=true)
- catalog host `avto-sales125.ru`: 200 (×2 in HTML)
- Telegram host `t.me`: 200 (×1 in HTML)
- placeholder CTA href: **нет** (проверка: литерал-placeholder отсутствует в `article.html` и `link-verify.json`)

## AI-slop scan

- cliches: 0
- over-long: 7
- Flesch RU: 58.4

## Schema ready

BlogPosting: **ready for schema agent** | FAQPage: yes (6) | HowTo: yes | Review: no  
**QA PASS — можно cover\|\|schema**

## Blockers

none

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

none
