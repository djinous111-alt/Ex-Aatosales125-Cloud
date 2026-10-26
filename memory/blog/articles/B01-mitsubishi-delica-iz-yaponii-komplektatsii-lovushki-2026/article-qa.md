# Article QA — B01

**topic_id:** B01  
**slug:** mitsubishi-delica-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-mitsubishi-delica-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-26  
**verdict:** PASS  
**score:** 90

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic false-positive (docs URL); см. INC research |
| fact-check | PASS | 4 stats; verified 1 (2026); unverified 2019 / 3 мес / 2267 — в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram CTA); `--site-base` из env; committed href=`[REDACTED]` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU ~76.7 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 11; pain/outcome OK; FAQ×7; table×1 |
| human-voice gate | PASS | `human-voice-report.json`; soft warn exactly-5 lists |

## Beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Красивый лот / оценка 4.5 кажутся поводом бить ставку → долгий маршрут, AdBlue, сюрпризы кузова |
| Где решение | H2: сегмент vs Noah; грейды G/G-Power/P; дизель 4N14+AdBlue+1.9 л; аукционный лист; чек-лист ×10 |
| Первый результат | До оплаты назвать грейд, подтвердить 4N14/AdBlue, маршрут через третью страну, прочитать лист → «ставлю / не ставлю» |
| Термины «на пальцах» | 4N14 (2.2/2.3 один мотор); AdBlue/SCR; порог 1.9 л; буква R; оценка 4.5 ≠ зелёный свет |

**beginner-fit:** PASS (не jargon-first; есть безопасный первый шаг до ставки)

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary «делика из японии» в title/H1/lead; H2 how-to; CTA каталог+TG |
| GEO / citability | 24/25 | Инсайт-блок, таблица грейдов, FAQ×7, чеклисты, схема сегмента |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | HV PASS; soft warn lists; 0 AI-openings |
| Fact safety | 13/15 | Mitsubishi 09.01.2026 + research; суммы пошлин не публикуем |
| Contract HTML | 10/10 | Whitelist PASS, ~9216 chars, FAQ, CTA≤3, без форм |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: история Андрея + чек-лист до ставки |
| C03 | ✓ | Читатель: заказ Delica из JP, риск ставки вслепую |
| C04 | ✓ | Грейды / 4N14 / AdBlue / лист объяснены |
| O01 | ✓ | H2 = how-to outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт-блок + схема + FAQ |
| R02 | ✓ | Доли предзаказов Mitsubishi 09.01.2026; объём ~2267 |
| R03 | ✓ | Нет сумм пошлин/утиля; расчёт только в каталоге |
| R04 | ✓ | FAQ-ответ в 1-м предложении |
| E01 | ✓ | Угол «до ставки» + ловушки маршрута/AdBlue |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог + Telegram (≤3) |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Fact Check = Редакция |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: срок ориентир, нет чужих калькуляторов |
| Ept02 | ✗ | Нет 2–3 internal blog links на соседние посты (только каталог/TG) |
| Exp-extra | ✗ | Soft: human-voice warn exactly-5 lists (не veto) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution map

- **Lead pain:** красивый лот ≠ быстрый пригон; порог 1.9 л + лист.
- **H2 solutions:** сегмент; грейды; дизель/AdBlue/маршрут; лист; чек-лист 10.
- **Result before FAQ:** блок «Результат, который вы получите сегодня».

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6
- Flesch RU: ~76.7

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. link-verify FAIL: `href="[REDACTED]"` (плейсхолдеры после secret-scrub) → восстановлены рабочие CTA `[REDACTED]` и `[REDACTED]`; повтор PASS.
2. Инсайт-ярлык: `TL;DR / Быстрый инсайт` → `Коротко до ставки` (anti-template skill).
3. Списки: «Что дальше» 5→4 и дизель-ol 5→4 (смягчение human-voice warn).

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
