# Article QA — B01 (re-QA after writer FIX cycle 1)

**topic_id:** B01  
**slug:** avto-iz-korei-pod-klyuch-chto-vhodit-2026  
**article_dir:** memory/blog/articles/B01-avto-iz-korei-pod-klyuch-chto-vhodit-2026  
**date:** 2026-10-15  
**verdict:** PASS  
**score:** 88  
**char_count:** 9475  
**fix_cycle:** re-QA after writer FIX 1 + Director policy restore (`pain_markers_ru` / `outcome_markers_ru`)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-15; technical_topic=false; github_urls=0 OK |
| fact-check | PASS | 1/1 verified |
| link-verify | PASS | 1/1 OK (`t.me/Djinous`); failed=0 |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 65.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | **PASS** | action 28; pain 9; outcome 12; water=[] |
| human-voice gate | **PASS** | Fact Check «Материал проверен» + Редакция Авто-Сейлс; WARN: exactly-5 lists (soft) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA Telegram×2; нет 2–3 blog internal |
| GEO / citability | 22/25 | инсайт, таблица финишей, workflow-цепочка, FAQ×7, чеклисты |
| CORE-EEAT lite | 15/15 | 19/20 |
| Human voice | 12/15 | story/pain/outcome OK; gate PASS; soft WARN lists |
| Fact safety | 13/15 | без статичных пошлин; fact-check PASS |
| Contract HTML | 10/10 | whitelist PASS, FAQ, CTA |
| Utility markers | 10/10 | gate PASS (policy markers restored + writer FIX) |
| **Итого** | **88/100** | ≥80 ✓ + mandatory gates PASS |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из кореи под ключ» в meta/H1 |
| C02 | ✓ | Lead: депозит vs сюрприз в порту |
| C03 | ✓ | Читатель: заказ из Кореи, страх доплат |
| C04 | ✓ | Encar / СВХ / СБКТС / ЭПТС / ЭРА-ГЛОНАСС объяснены |
| O01 | ✓ | H2 = action outline до депозита |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + workflow, mode B |
| R01 | ✓ | инсайт + чеклисты + FAQ |
| R02 | ✓ | grounded в research-notes (без фейковых сумм) |
| R03 | ✓ | нет статичного калькулятора пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «докажи строками до депозита» |
| E02 | ✓ | «Сделайте / Не делайте» + policy markers |
| E03 | ✓ | CTA Telegram @Djinous ×2 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | slop hits = 0 |
| Ept01 | ✓ | лимиты: нет единой «под ключ», дыры СВХ/лаборатории |
| Ept02 | ✗ | нет 2–3 внутренних ссылок на другие посты блога |
| Ept02b | ✓ | Fact Check: «Материал проверен» + Редакция Авто-Сейлс |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · **mandatory gates:** PASS

## Pain / solution / beginner-fit

| Критерий | Статус | Где |
|----------|--------|-----|
| Боль новичка | ✓ | Lead: депозит по рекламе «под ключ» → доплаты СВХ/лаборатория/автовоз |
| Решение в H2 | ✓ | финиш услуги → строки сметы → дыры → документы → график денег → чеклист |
| Первый результат до FAQ | ✓ | заполненный лист зелёных/красных строк + шаблон в @Djinous |
| Термины «на пальцах» | ✓ | Encar, СВХ, СБКТС, ЭПТС, ЭРА-ГЛОНАСС |
| Beginner-fit | PASS | не профи-жаргон без объяснений; первый шаг безопасный (смета до депозита) |

## Link verify

- total: 1, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 4 (таблица/цепочка/достоверность)
- Flesch RU: 65.5

## Schema ready

BlogPosting: ready for schema agent | FAQPage: yes (7) | HowTo: yes | Review: no | cover/schema: **можно** после этого PASS

## Gate checklist

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✓  
- research-notes-gate PASS → ✓  
- utility gate PASS → ✓  
- human voice gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** PASS — cover \|\| schema можно запускать параллельно.
