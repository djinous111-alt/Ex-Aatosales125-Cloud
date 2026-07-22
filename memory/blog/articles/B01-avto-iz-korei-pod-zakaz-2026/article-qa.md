# Article QA — B01

**topic_id:** B01  
**slug:** avto-iz-korei-pod-zakaz-2026  
**article_dir:** memory/blog/articles/B01-avto-iz-korei-pod-zakaz-2026  
**date:** 2026-07-23  
**cycle:** GEO QA re-run после Writer FIX1 + Fixer policy  
**verdict:** PASS  
**score:** 92

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | `technical_topic=false`; sources 18; pain_solution 4; action_outline 9 |
| fact-check | PASS | 5 stats; verified 2; unverified 2024 / 2027 / 160 (есть в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/схемы/чеклист); Flesch RU 71.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 27≥8; pain 6≥2; outcome 5≥3; water=[] |
| human-voice | PASS | WARN: Fact Check template; WARN: 2× exactly-5-step lists |

## Beginner-fit

**PASS.** Боль новичка («с чего начать / не сжечь бюджет на депозите») в lead; термины Encar / СВХ / СБКТС / ЭПТС / RoRo объяснены; первый безопасный шаг — чек-лист до депозита + расчёт в каталоге.

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка | Цена лота Encar ≠ под ключ; депозит до VIN/истории; фильтры 2,0 л / 160 л.с. неизвестны |
| Где решение | H2: бюджет/фильтры → лоты Encar → проверка до депозита → сравнение → оплата → маршрут → чеклист |
| Первый результат | Заполненный чеклист до первого платежа + запрос письменного расчёта |
| Термины «на пальцах» | Encar, «под заказ», СВХ, СБКТС, ЭПТС, RoRo/контейнер, Performance Record, Carhistory |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA каталог×2 + Telegram; мало blog-internal |
| GEO / citability | 24/25 | Инсайт без TL;DR-ярлыка; схемы+таблица+FAQ×7+чеклист |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 13/15 | Gate PASS; template Fact Check + 2×5-step (WARN) |
| Fact safety | 12/15 | Unverified 2024/2027/160 вне fact-bank |
| Contract HTML / utility | 10/10 | Whitelist PASS; utility PASS (27/6/5) |
| **Итого** | **92/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из кореи под заказ» в title/H1 |
| C02 | ✓ | Lead: ловушка цены лота → маршрут до выдачи |
| C03 | ✓ | Новичок / заказ из Кореи / риск депозита |
| C04 | ✓ | Encar, Carhistory, СВХ, СБКТС, ЭПТС объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный путь до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + table + checklists, mode B |
| R01 | ✓ | Инсайт, схемы, чеклист, FAQ |
| R02 | ✓ | 2,0 л / 160 л.с. / 24.02.2024 / мораторий ЭРА — в research-notes |
| R03 | ✓ | Нет статичного калькулятора пошлин; персональный расчёт |
| R04 | ✓ | FAQ отвечает с первого предложения |
| E01 | ✓ | Угол «фильтры + до депозита + маршрут» |
| E02 | ✓ | Литералы «Сделайте: / Не делайте:» |
| E03 | ✓ | CTA каталог + Telegram |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты сроков, мораторий, риски X/W |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 71.9

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | cover/schema: **можно запускать** (QA PASS)

## Soft / optional (не блокируют PASS)

1. Разнообразить Fact Check Box (human-voice WARN template).
2. Сделать один из 5-step `<ol>` длины ≠5.
3. Ept02: 2–3 internal links на соседние посты блога с `anchor_variants` после появления URL.
4. fact-bank: 24.02.2024, 31.12.2027, 160 л.с. для verified.

## Gate checklist

- score ≥ 80 → **92** ✓  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — директор может запускать cover \|\| schema.

`incident_report:` none
