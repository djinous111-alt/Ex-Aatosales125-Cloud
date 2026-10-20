# Article QA — B01

**topic_id:** B01  
**slug:** kia-k3-iz-korei-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-kia-k3-iz-korei-komplektatsii-lovushki-2026  
**date:** 2026-10-20  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | WARN: technical topic / no obvious official docs URL (ожидаемо для авто-импорта) |
| utility gate | PASS | action_markers 27; pain 7; outcome 12; FAQ×7; table×1; ol items 15 |
| human-voice-gate | PASS | WARN: multiple exactly-5-step lists; pain/outcome/story overlap OK |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| link-verify | PASS | 2/2 OK (каталог + Telegram); failed_count 0 |
| fact-check | PASS | 9 stats; 1 verified in fact-bank (2026); 8 soft-unverified (л.с./л/годы — в research-notes) |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка table/ul/blockquote парсером); Flesch RU 72.9 Easy |
| cannibalization | PASS | 0 issues; угол «до депозита» не дублирует AS09 Trust/Carhistory |

## Beginner-fit / pain → solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Перепутать корейский K3 с китайским «близнецом» или GT; не понять trim на Encar; депозит без VIN/истории/фото опций |
| Где решение | H2: страна/мотор → trim vs пакеты → пробег/история → красные флаги → чеклист Владивосток → shortlist сегодня |
| Первый результат | Заполненный чеклист + shortlist 2–3 лотов к разговору в каталоге / Telegram |
| Критерий успеха (до FAQ) | H2 «Сделайте сегодня…»: чеклист закрыт → депозит; иначе фильтр |
| Термины «на пальцах» | IVT (вариатор), Encar, Performance Check, Carhistory, flood-check, СВХ |

**beginner-fit:** PASS (не тон для профи; первый безопасный шаг без команды)

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary how-to в H1/title; H2 actionable; CTA каталог×2 + TG×1; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт-blockquote, таблица KR/CN/GT, схема до депозита, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 14/15 | PASS; WARN ровно-5 шагов; живые маркеры («на практике», история Ивана) |
| Fact safety | 12/15 | Цифры в research-notes; fact-bank почти пуст по K3-спекам |
| Contract HTML | 10/10 | Whitelist PASS, ~9.5k chars, FAQ, CTA≤3, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать kia k3 из кореи» в H1 / meta |
| C02 | ✓ | Lead: боль депозита + чеклист/shortlist без «в этой статье» |
| C03 | ✓ | Новичок заказа из Кореи через Владивосток |
| C04 | ✓ | IVT, Encar, Performance Check, Carhistory, СВХ объяснены |
| O01 | ✓ | H2 = research action_outline / pain_solution_map |
| O02 | ✓ | Логичный outline до shortlist |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + table + схема, mode B |
| R01 | ✓ | Инсайт-box, таблица, схема → депозит, FAQ |
| R02 | ✓ | Спеки KR/CN/GT + trim уровни из research-notes |
| R03 | ✓ | Нет цен лотов / % пошлин; расчёт только в каталоге |
| R04 | ✓ | FAQ: ответ-действие в 1-м предложении |
| E01 | ✓ | Угол trim vs пакеты + Korea/China/GT до депозита (не клон AS09) |
| E02 | ✓ | «Сделайте так / Не делайте так» в H2 |
| E03 | ✓ | CTA ≤3: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Human voice PASS; story Ивана / Новосибирск |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Такси вне отчёта, нет VIN → стоп, давление оплаты |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0, verdict: pass
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт table/списков)
- Flesch RU: 72.9 Easy

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты/шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется (все обязательные gates PASS)

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних URL — 2–3 internal links (напр. AS09 Trust/Carhistory) с `anchor_variants`.
2. **fact-check soft:** дописать в fact-bank спеки K3 KR/CN (123/115 л.с., 502/482 л, годы 2022–2023).
3. **human-voice WARN:** разнести размеры списков (сейчас два блока «ровно 5»).
4. **docs conflict (не FAIL):** writing-contract пример использует ярлык `TL;DR / Быстрый инсайт:`, geo-qa skill просит его избегать — выровнять контракты (см. incident).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research notes PASS ✓  
- utility article PASS ✓  
- human voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
