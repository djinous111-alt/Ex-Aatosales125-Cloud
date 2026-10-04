# Article QA — B01

**topic_id:** B01  
**slug:** kak-zakazat-avto-iz-yaponii-pod-klyuch-2026  
**article_dir:** memory/blog/articles/B01-kak-zakazat-avto-iz-yaponii-pod-klyuch-2026  
**date:** 2026-10-04  
**verdict:** PASS  
**score:** 87

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит «чтобы не ушла» без ауклиста/месяца выпуска/сметы; непонятные этапы и термины |
| Где решение | H2: рамка → лот до депозита → этапы ролкер/СВХ → смета «под ключ» → чеклист 12 пунктов |
| Первый результат | Карта сделки + заполненный чек-лист до первой оплаты; расчёт — в каталоге/Telegram |
| Термины «на пальцах» | Ауклист, R/RA, ролкер, СВХ, СБКТС, ЭПТС, проходной год/месяц выпуска |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-04; source_table/accessed_at OK |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified 3–5 лет / 8 недель / 160 л.с. — есть в research-notes |
| link-verify | PASS | 2 unique URL / 3 CTA (каталог×2 + Telegram); failed=0 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схема); Flesch RU 58.4 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 15; pain 4; outcome 4; ol/FAQ/table OK |
| human-voice gate | PASS | story/pain/outcome overlap; warning: ≥2 списков с ≥5 `<li>` (regex soft) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «заказ авто из японии» в title/H1; H2 how-to; CTA×3; нет 2–3 internal blog links |
| GEO / citability | 24/25 | TL;DR, схема под ключ, comparison-таблица, FAQ×7, чеклист 12 |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | reader_story Игорь/Camry; 0 AI-slop; concrete markers OK |
| Fact safety | 12/15 | Цифры из research-notes; не все в fact-bank; готовых сумм пошлин нет |
| Contract HTML | 10/10 | Whitelist PASS, ~9.0k символов, FAQ×7, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: боль депозита + цепочка + результат чек-листа |
| C03 | ✓ | Читатель: новичок заказа JP под ключ |
| C04 | ✓ | Ауклист / ролкер / СВХ / СБКТС / ЭПТС объяснены |
| O01 | ✓ | H2 = action_outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + схема, mode B |
| R01 | ✓ | TL;DR + схема + FAQ |
| R02 | ✓ | 3–8 недель, ~160 л.с., 3–5 лет — в research-notes |
| R03 | ✓ | Нет готовых сумм пошлин/утиля |
| R04 | ✓ | FAQ отвечает действием в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + карта сделки |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: персональный расчёт, простой СВХ, месяц выпуска |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0, verdict: pass
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (таблица/схема/длинный lead)
- Flesch RU: 58.4

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты/схема) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требовался: все обязательные gates PASS с первого прогона

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних URL — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 160 л.с. / 3–8 недель / 3–5 лет — дописать в fact-bank для verified.
3. **human-voice warning:** regex считает ol с ≥5 li как «exactly-5»; editorial OK.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-report PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
