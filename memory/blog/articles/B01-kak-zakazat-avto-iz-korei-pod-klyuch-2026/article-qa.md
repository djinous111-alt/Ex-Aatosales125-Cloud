# Article QA — B01

**topic_id:** B01  
**slug:** kak-zakazat-avto-iz-korei-pod-klyuch-2026  
**article_dir:** memory/blog/articles/B01-kak-zakazat-avto-iz-korei-pod-klyuch-2026  
**date:** 2026-09-28  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-09-28; errors=[] |
| fact-check | PASS | 11 stats; verified 2; unverified 9 (в research-notes: ПП № 1713, экспорт >2,0 л с 2024, цикл 30–55 дн.) |
| link-verify | PASS | 2/2 OK (каталог + Telegram; дубль каталога схлопнут); `--site-base [REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING (non-blocking) | 0 клише; 6 over-long (таблица/схемы парсером); Flesch RU 72.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 13 (≥8); FAQ×7; table×1; numbered 20; pain 9 / outcome 4 |
| human-voice gate | PASS | warnings: 2× exactly-5-step lists; reader_story/pain/outcome/success overlap OK |

## Pain → solution → result (обязательный чеклист)

| Вопрос | Ответ |
|--------|--------|
| Какая боль новичка решена? | Путает цену Encar со сметой «под ключ»; рискует депозитом без VIN/договора; не знает двойной коридор ≤2,0 л / ≤160 л.с. |
| Где показано решение? | Lead (история Алексея) → H2 рамка → H2 VIN/отчёты → H2 договор → H2 путь → H2 чек-лист из 10 пунктов |
| Какой первый результат до FAQ? | Рамка на бумаге + светофор из 10 пунктов «стоп / можно платить» + 4 шага в «Что дальше» |
| Какие термины «на пальцах»? | Encar, VIN, инвойс, коносамент, СВХ, СБКТС, ЭПТС, утильсбор, Performance Check, Carhistory, Rent/Lease |

**Beginner-fit:** PASS — не профи-жаргон без объяснений; первый безопасный шаг = рамка до заявки; нет требования «собери команду брокеров».

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «авто из кореи под ключ» в title/H1; H2 how-to; CTA каталог×2 + Telegram; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, таблица Encar vs под ключ, схемы пути, FAQ×7, чек-лист×10 |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 15/15 | human-voice-report PASS; slop hits = 0 |
| Fact safety | 13/15 | Факты в research-notes; часть не в fact-bank (soft) |
| Contract HTML | 10/10 | Whitelist PASS, ~9488 символов, FAQ, CTA, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «авто из кореи под ключ» в meta title / H1 |
| C02 | ✓ | Lead — история ловушки + прямой план, без «в этой статье» |
| C03 | ✓ | Читатель: новичок, заказ из Кореи, страх депозита |
| C04 | ✓ | Мини-словарь + Encar/отчёты объяснены при первом появлении |
| O01 | ✓ | H2 = how-to outline research (смысл под ключ → рамка → лот → договор → путь → чек-лист → FAQ) |
| O02 | ✓ | Логичный outline до оплаты → после оплаты |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | TL;DR, итоговый вердикт, схема до оплаты, путь авто |
| R02 | ✓ | ПП № 1713 / 160 л.с.; экспорт >2,0 л с 2024; цикл 30–55 дн. — в research-notes |
| R03 | ✓ | Нет жёстких цен лотов/%; «2,4 млн» — сюжетная ловушка, расчёт → каталог |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «двойной коридор + чек-лист до депозита», не клон SERP |
| E02 | ✓ | «Делать / Не делать» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски: запрет экспорта, утиль >160, депозит без VIN, задержки СБКТС |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2 unique, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схем)
- Flesch RU: 72.5

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты/шаги) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после URL соседних постов на сайте — 2–3 internal links с `anchor_variants` (Indexer может закрыть).
2. **fact-check soft:** ПП № 1713 / 160 л.с. / экспорт >2,0 л с 2024 / 30–55 дн. — дописать в fact-bank для verified.
3. **slop over-long / human-voice warn:** 2 списка ровно по 5 пунктов — при следующем редактировании варьировать длину; over-long — артефакт таблицы.
4. **TL;DR label:** ярлык `TL;DR / Быстрый инсайт` соответствует writing-contract; skill GEO QA упоминает избегание шаблона — расхождение контрактов (не блокирует; scripts PASS).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice-report PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
