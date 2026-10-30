# Article QA — B01

**topic_id:** B01  
**slug:** changan-cs75-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-changan-cs75-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-30  
**verdict:** PASS  
**score:** 87

## Beginner-fit / pain → solution → outcome

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Хочет CS75 Plus дешевле дилера и тянется к депозиту, путает Plus/Pro и не знает про кВт на шильдике |
| Где решение | H2: салон vs Китай → развести линейки → шильдик/утиль → чек-лист до депозита → маршрут СВХ → красные флаги |
| Первый результат | Заполненный стоп-лист: линейка, кВт, VIN, документы; депозит только после пакета |
| Термины «на пальцах» | Шильдик, 117,68 кВт / 160 л.с., СВХ, СБКТС, ЭПТС, Plus NEW vs Pro |

**beginner-fit:** PASS (не профи-тон; первый безопасный шаг — проверки до денег)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical topic / no official docs URL (false-positive auto-topic; см. INC research) |
| fact-check | PASS | 16 stats; verified 4 / unverified 12 vs fact-bank; цифры есть в research-notes |
| link-verify | PASS | 2/2 OK (уникальные URL: каталог + Telegram; 3 href с дедупом каталога) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 7 over-long; Flesch RU 77.9 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action_markers 20 (≥8); ol×9, FAQ×6, table×1, pain/outcome OK |
| human voice gate | PASS | pain/outcome/story overlap; 0 AI openings; H2 без шаблона |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «changan cs75 комплектации» в title/H1; H2 how-to; CTA каталог×2 + TG×1; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт-блок, таблица линеек, FAQ×6, чеклисты, схема маршрута |
| CORE-EEAT lite | 14/15 | 18/20 (см. таблицу ниже) |
| Human voice | 15/15 | human-voice PASS; slop hits = 0 |
| Fact safety | 12/15 | fact-check PASS; часть л.с./кВт/180 дней не в fact-bank (есть в research-notes) |
| Contract HTML | 10/10 | Whitelist PASS, ~9.1–9.4k, FAQ, CTA≤3, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary query в meta title / H1 |
| C02 | ✓ | Lead: боль депозита без шильдика + Plus vs Pro |
| C03 | ✓ | Читатель: новичок, заказ из Китая vs салон |
| C04 | ✓ | СВХ / СБКТС / ЭПТС / кВт объяснены |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт-блок + схема маршрута + FAQ |
| R02 | ✓ | Порог 117,68 кВт, спеки Plus/Pro в research-notes |
| R03 | ✓ | Нет выдуманных цен лотов; смета → каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + ловушка мощности |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: без шильдика / сроки ориентиры / не считать утиль по «лошадям» |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 7 (мягкий WARNING, не блокер)
- Flesch RU: 77.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после LIVE URL соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** занести в fact-bank порог 117,68 кВт / 160 л.с., спеки Plus NEW 235 / Pro 181, ориентир ~180 дней.
3. **slop over-long:** при следующем рерайте укоротить 2–3 длинных абзаца (не обязательно сейчас).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
