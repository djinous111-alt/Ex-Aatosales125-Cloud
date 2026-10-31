# Article QA — AS02

**topic_id:** AS02  
**slug:** encar-na-russkom-kak-chitat  
**article_dir:** memory/blog/articles/AS02-encar-na-russkom-kak-chitat  
**date:** 2026-11-01  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | re-check; warning technical_topic без /docs (non-blocking) |
| fact-check | PASS | 7 stats; verified 2 (90 дней, 20 минут); unverified 5 (2021, 10 000, 24 500 000, 2450, 2 200) — есть в research-notes |
| link-verify | PASS | 3/3 OK (`encar.com`, `avto-sales125.ru`, `t.me/avtosales125`) |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (таблица/схема + lead); Flesch RU 73.0 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 8; pain 5; outcome 5; ol 23; H2 7; FAQ×6; table×1 |
| human-voice gate | PASS | pain/outcome/story/success overlap OK; warn: 4× exactly-5-step lists |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Гуглит «encar на русском» → клон/кривой перевод; путает 만원, 연식, «без ДТП» |
| Где решение | H2: оригинал encar.com → цена 만원 → 연식 vs выпуск → схема X/W + страховая → Carhistory → чеклист 8 шагов |
| Первый результат | 15–20 мин на лот: цена в вонах, VIN, флаги на схеме; при флагах — стоп до депозита |
| Термины «на пальцах» | Encar = авторынок с «паспортом»; 万円×10 000; 무사고 = каркас; X/W объяснены |

**beginner_fit:** PASS

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «encar на русском» в title/H1; H2/H3; CTA; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт, схема →, таблица полей, FAQ×6, чеклист |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | 0 AI-slop; reader_story (Игорь/Tucson); surprising_fact в первых 30% |
| Fact safety | 14/15 | Факты в research-notes; часть не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~8959, FAQ, CTA×3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «encar на русском» в meta title / H1 |
| C02 | ✓ | Lead: ловушка клона/перевода + обещание чеклиста до депозита |
| C03 | ✓ | Читатель: новичок заказа из Кореи |
| C04 | ✓ | 만원, 연식, 무사고, X/W, Carhistory объяснены |
| O01 | ✓ | H2 = outline research (клон → цена → год → ДТП → Carhistory → чеклист) |
| O02 | ✓ | Логичный how-to |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + workflow, mode B |
| R01 | ✓ | Инсайт-блок, схема лота, FAQ |
| R02 | ✓ | 만원×10 000, ~2200₩, 90 дней — в research-notes |
| R03 | ✓ | Нет выдуманных цен лотов/% пошлин |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «меню на чужом языке перед дорогим заказом» |
| E02 | ✓ | Делать / Не делать в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я лично купил» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты 무사고, страховой базы, перевода |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/схемы + lead)
- Flesch RU: 73.0

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет (после restore `pain_markers_ru` / `outcome_markers_ru` в `memory/brief/editorial-policy.json` — rebrand wipe)

## FIX cycle (QA)

1. Utility gate first run BLOCK: `pain_markers=0`, `outcome_markers=0` при пустых списках маркеров в policy после rebrand. Статья не правилась. Restore маркеров из pin-коммита → utility PASS (pain 5 / outcome 5).

## FIX (non-blocking / optional)

1. **Инсайт-ярлык:** заменить `TL;DR / Быстрый инсайт` на нейтральный (`Инсайт до депозита` / `Коротко`).
2. **Ept02:** после LIVE соседних AS* — 2–3 internal links с `anchor_variants`.
3. **fact-check soft:** 만원×10 000 / 2 200₩ — дописать в fact-bank.
4. **exactly-5-step lists:** варьировать длину списков (human-voice warning).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
