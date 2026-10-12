# Article QA — B01

**topic_id:** B01  
**slug:** levyj-rul-iz-korei-kak-vybrat-2026  
**article_dir:** memory/blog/articles/B01-levyj-rul-iz-korei-kak-vybrat-2026  
**date:** 2026-10-12  
**verdict:** PASS  
**score:** 92  
**writer_fix:** no  
**human_voice:** PASS  
**beginner_fit:** PASS  
**re_run:** after Writer FIX cycle 1 + Fixer (utility policy)

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка решена? | Путает цену Encar со сметой под ключ, давит «платите сегодня», нет решения «беру / мимо» до депозита |
| Где показано решение? | H2: Корея vs Япония → потолок бюджета → чеклист Encar (Шаг 1–6) → мотор/утиль → цепочка → чеклист 12 пунктов до FAQ |
| Какой первый результат? | По одному лоту сказать «беру в работу / мимо» до перевода; пакет VIN + схема + осмотр |
| Термины «на пальцах» | LHD/RHD, Encar, Performance Check (X/W), Carhistory, СВХ, СБКТС, ЭПТС — объяснены в теле |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | status PASS; research_date 2026-10-12 |
| utility gate | PASS | action=17, pain=3, outcome=6; water_hits=[] |
| human-voice | PASS | concrete + story/pain/outcome overlap OK |
| html-linter | PASS | whitelist OK; TOC нет |
| link-verify | PASS | 3/3 OK (внутренний пост 2026-10-03, каталог, Telegram) |
| cannibalization | PASS | 0 issues |
| fact-check | PASS | 9 stats; 2 verified / 7 unverified vs fact-bank (есть в research-notes) |
| slop-detector | WARNING | 0 клише; 9 over-long (таблица/схемы/чеклист); Flesch RU 66.5 |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | primary в H1/title; H2 actionable; 1 blog internal + CTA |
| GEO / citability | 22/25 | insight «Коротко», table, workflow→, FAQ×6, чеклист |
| CORE-EEAT lite | 17/20 | см. ниже |
| Human voice | 15/15 | gate PASS |
| Fact safety | 12/15 | факты в research; часть не в fact-bank |
| Contract HTML | 10/10 | whitelist PASS; utility PASS |
| **Итого** | **92/100** | ≥80 ✓ |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «левый руль из кореи» в H1/meta |
| C02 | ✓ | Lead — боль + разбор до депозита |
| C03 | ✓ | Новичок / заказ LHD из Кореи |
| C04 | ✓ | Encar / VIN / утиль / цепочка объяснены |
| O01 | ✓ | H2 = pain_solution_map outline |
| O02 | ✓ | Логичный порядок до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol×6 + ul×12 + table + workflow |
| R01 | ✓ | Insight + схемы + чеклист результата |
| R02 | ✓ | 2,0 л / 3400–5200 / ПП №1713 / 30–55 дней в research |
| R03 | ✓ | Нет калькулятора пошлин в теле; расчёт → каталог |
| R04 | ✓ | FAQ с «Действие:» в 1-м предложении |
| E01 | ✓ | Угол LHD (не дубль «под ключ») |
| E02 | ✓ | «Сделайте/Избегайте/Используйте/Не делайте» + «Шаг N:» |
| E03 | ✓ | CTA каталог ≤3 + Telegram ≤2 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты экспорта 2,0 л, X/W, утиль |
| Ept02 | ✗ | Мало внутренних blog-links (1 live post + каталог) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · **utility gate: PASS**

## Link verify

- total: 3, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 9 (артефакт table/blockquote/ul)
- Flesch RU: 66.5

## Schema ready

BlogPosting: ready for cover/schema | FAQPage: yes (6) | HowTo: yes | Review: no  
**Можно запускать cover||schema** (GEO QA PASS).

## Blockers

none

## Gate

- score ≥ 80 → **92** ✓  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- utility gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — cover||schema можно стартовать.
