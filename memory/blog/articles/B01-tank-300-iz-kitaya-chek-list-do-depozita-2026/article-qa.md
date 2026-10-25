# Article QA — B01

**topic_id:** B01  
**slug:** tank-300-iz-kitaya-chek-list-do-depozita-2026  
**article_dir:** memory/blog/articles/B01-tank-300-iz-kitaya-chek-list-do-depozita-2026  
**date:** 2026-10-25  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN: technical_topic + no official docs URL (harmless for auto niche) |
| fact-check | PASS | 13 extracted / 1 verified vs fact-bank; цифры ТХ/180 дней/утиль в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (склейка table/ul/blockquote парсером); Flesch RU 65.3 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |
| utility gate | PASS | action 23 / pain 10 / outcome 22; FAQ×6; table×1; lists OK |
| human-voice gate | PASS | human-voice-report.json status PASS; reader_story / pain / outcome overlap OK |

## Beginner-fit

**PASS.** Статья для новичка до депозита, не для профи/разработчиков.  
Термины на пальцах: Part-time/ToD, СВХ, СБКТС, ЭПТС, ШГУ, порог утиля ~160 л.с.  
Первый безопасный шаг: 10-пунктовый чеклист + stop-флаги до перевода аванса; суммы пошлин — только в каталоге.

## Pain → solution → result

| Элемент | Где в статье |
|---------|--------------|
| Боль новичка | Lead: депозит по скрину → 180 дней / мощность / дизель / VIN |
| Решение в H2 | Дилер vs Китай; проверка лота; путь Владивосток; документы/ловушки; чеклист 10 |
| Первый результат до FAQ | «Критерий результата»: 10 пунктов отмечены + расчёт в каталоге |
| Сложные термины | СВХ/СБКТС/ЭПТС, Part-time vs ToD, ШГУ — объяснены в теле |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «танк 300 из китая» в title/H1; H2 how-to; CTA каталог×2 + TG×1; нет 2–3 blog internal |
| GEO / citability | 23/25 | Insight blockquote, таблица дилер vs Китай, workflow, FAQ×6, чеклист 10 |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop hits |
| Fact safety | 13/15 | Нет статичных сумм пошлин; цифры ТХ/даты в research-notes, слабо в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9166 chars, FAQ×6, CTA, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «танк 300 из китая» в title / H1 / meta |
| C02 | ✓ | Lead — история депозита + риски, без «в этой статье» |
| C03 | ✓ | Новичок боится предоплаты за лот из Китая |
| C04 | ✓ | СВХ/СБКТС/ЭПТС/Part-time/ToD/ШГУ объяснены при появлении |
| O01 | ✓ | H2 = research outline (задача → дилер vs Китай → лот → путь → документы → чеклист → FAQ) |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 6 (в коридоре 5–7) |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | Insight, вердикт дилер/Китай, workflow blockquote, критерий результата |
| R02 | ✓ | АВТОТОР май 2026 + ТХ/порог утиля с опорой на research-notes |
| R03 | ✓ | Нет готовых сумм пошлин/% цен лотов; расчёт → каталог |
| R04 | ✓ | FAQ: ответ в 1-м предложении |
| E01 | ✓ | Угол «стоп до депозита» + surprising_fact АВТОТОР после мая 2026 |
| E02 | ✓ | «Делать / Не делать» в ключевых H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / эксперт Владивостока |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | 180 дней, мощность/утиль, серый ввоз, stop-флаги |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт table/ul/blockquote)
- Flesch RU: 65.3

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все gates PASS с первого прогона GEO QA)

## FIX (non-blocking / optional)

1. **Ept02:** после публикации смежных Bxx/AS* — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** дописать в fact-bank ТХ Tank 300 / АВТОТОР май 2026 / порог ~160 л.с. для verified_count.
3. **geo-qa skill vs writing contract:** skill запрещает ярлык `TL;DR / Быстрый инсайт`, writing-contract его приводит как пример; automated gates PASS — правку article.html не делал.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
