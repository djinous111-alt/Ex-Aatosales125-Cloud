# Article QA — B01

**topic_id:** B01  
**slug:** kak-rusifitsirovat-avto-iz-kitaya-2026  
**article_dir:** memory/blog/articles/B01-kak-rusifitsirovat-avto-iz-kitaya-2026  
**date:** 2026-10-02  
**verdict:** PASS  
**score:** 91  
**qa_cycle:** re-run after Writer FIX cycle 1

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: technical_topic / no OEM docs URL (non-blocking) |
| utility gate | PASS | action_markers=26; pain_markers=4; outcome_markers=8 |
| human-voice | PASS | pain: проблем/ошиб/сложно; outcome: результат/сможете/проверьте/выберите; warn: multiple exactly-5-step lists |
| fact-check | PASS | 4 stats; 3 verified; 1 unverified soft (`150` в вилке 50–150) |
| link-verify | PASS | 2/2 OK (`--site-base` из `PUBLIC_SITE_URL`; URLs redacted) |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 3 over-long (склейка таблиц/blockquote); Flesch RU 61.3 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Beginner-fit / pain→solution

| Вопрос | Ответ QA |
|--------|----------|
| Какая боль новичка решена? | Депозит «вслепую» при иероглифах на приборке, мёртвых картах и отсутствии CarPlay |
| Где показано решение? | H2: слои → вопросы до депозита → смета → анти-DIY/OTA → чек-лист выдачи → «Что дальше» |
| Первый результат читателя? | Письменный список вопросов продавцу + видео этой VIN до денег; зелёный чек-лист при выдаче |
| Термины «на пальцах»? | Слои русификации, OTA («как на смартфоне»), CarPlay-модуль vs «допрошивка» — объяснены |
| Beginner-fit | PASS (чек-лист покупателя, без DIY-прошивки; pain/outcome маркеры PASS) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1/lead; H2 actionable; нет 2–3 blog internal |
| GEO / citability | 22/25 | Инсайт без TL;DR-ярлыка; 2 таблицы; FAQ×7; workflow → |
| CORE-EEAT lite | 19/20 | см. ниже; минус Ept02 |
| Human voice | 13/15 | gate PASS; warn: ≥2 lists with 5+ `<li>` |
| Fact safety | 12/15 | вилки в research; `150` unverified vs fact-bank |
| Contract HTML | 10/10 | whitelist PASS, ~9412 chars, FAQ, CTA≤3 |
| Utility gates | PASS | utility + human-voice без veto |
| **Итого** | **91/100** | ≥80 ✓ |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «русификация авто из китая» в meta/H1 |
| C02 | ✓ | Lead: депозит vs реальность на выдаче |
| C03 | ✓ | Читатель: заказ авто из Китая, риск депозита |
| C04 | ✓ | Слои / OTA / CarPlay объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логика до депозита → выдача → OTA |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol + таблицы + workflow →, mode B |
| R01 | ✓ | Инсайт-блок + критерий результата до FAQ |
| R02 | ✓ | Вилки цен / Changan / OTA в research-notes |
| R03 | ✓ | Цены как ориентир рынка, не прайс Авто-Сейлс |
| R04 | ✓ | FAQ отвечает действием в 1-м предложении |
| E01 | ✓ | Угол чек-лист покупателя, не DIY |
| E02 | ✓ | «Сделайте / Не делайте / Проверьте / Избегайте» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я прошил» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | OTA-сброс, DIY-риски, лимиты CarPlay |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |
| HV01 | ✓ | human-voice PASS (pain≥2, outcome≥) |
| U01 | ✓ | utility PASS (action/pain/outcome thresholds) |

**Target CORE-EEAT ≥16/20:** 19/20 ✓  
**Veto:** нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблиц/схем)
- Flesch RU: 61.3

## Schema ready

BlogPosting: pending (после PASS → cover\|\|schema) | FAQPage: yes (7) | HowTo: yes (чеклисты)

## Blockers

- нет

## FIX history

1. **Cycle 1 (Writer):** action markers ≥8; human-voice pain ≥2; убран ярлык `TL;DR / Быстрый инсайт`; финальный ol=6; outcome «сможете». Utility + human-voice → PASS на re-run.

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links на смежные посты блога с `anchor_variants`.
2. **fact-check soft:** дописать `150` (вилка 50–150) в fact-bank.
3. **human-voice warn:** варьировать размеры длинных списков (сейчас 7/12/6 + табличные артефакты).

## Gate

- score ≥ 80 → **91** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- research-notes-gate PASS ✓  
- link-verify pass ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
