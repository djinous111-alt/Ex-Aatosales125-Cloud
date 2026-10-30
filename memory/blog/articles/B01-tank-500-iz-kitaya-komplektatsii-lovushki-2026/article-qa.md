# Article QA — B01 Tank 500 из Китая

**topic_id:** B01  
**slug:** tank-500-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-tank-500-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-30  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: technical_topic false-positive (ии in «комплектации»); GitHub noise only |
| utility gate | PASS | action 11 / pain 7 / outcome 8; table×1; FAQ×6; ol/ul OK |
| human-voice gate | PASS | pain×4; outcome×5; reader_story/pain/outcome overlap OK; warn rhythm 0.31 |
| fact-check | PASS | 13 extracted; 1 verified in fact-bank; 12 soft (цены/кВт в research-notes + Fact Check Box) |
| link-verify | PASS | 2/2 HEAD 200 (каталог + Telegram); `--site-base` from PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK; insight без TL;DR |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU 68.5 — не блок |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |

## Beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит «за премиум как у дилера» → приезжает другой китайский код (Hi4-T Smart 5 мест вместо 7) + сюза утильсбора после оплаты |
| Где решение | H2: Сити/Техно/Оникс vs Hi4-T/3.0T/Hi4-Z (таблица); утиль без льготы; must-have; чек-лист 10 шагов до оплаты |
| Первый результат | Одностраничный чек-лист + фраза «ставлю / жду / отказываюсь» до депозита |
| Термины «на пальцах» | Hi4-T / 3.0T / Hi4-Z; мягкий vs подключаемый гибрид; 30-мин мощность электромотора; ОТТС/СБКТС/ЭПТС; льготный утильсбор |

**beginner-fit:** PASS (не профи-жаргон IT; безопасный первый шаг = не платить без кода и сметы)

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «танк 500 комплектации» в title/H1; H2 how-to; CTA×3; нет 2–3 internal blog |
| GEO / citability | 24/25 | Инсайт, схема, таблица соответствий, FAQ×6, чек-лист, критерий успеха |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | PASS; rhythm warn; concrete markers OK |
| Fact safety | 13/15 | Ориентиры ¥/₽ помечены; точный расчёт только под лот; soft vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; ~9k chars; FAQ; CTA; без форм; author из registry |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «танк 500 комплектации» в meta title / H1 |
| C02 | ✓ | Lead — история Сергея + боль депозита, без «в этой статье» |
| C03 | ✓ | Читатель: заказ Tank 500 из Китая, риск комплектации/утиля |
| C04 | ✓ | Hi4-T/3.0T/Hi4-Z, ОТТС/СБКТС/ЭПТС, мягкий vs PHEV объяснены |
| O01 | ✓ | H2 = сценарий → коды → утиль → must-have → чек-лист → дилер vs Китай |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 6 = реальные queries (комплектации РФ/КНР, Hi4-T, утиль 3.0, 500 vs 300, 7 мест, давление продавца) |
| O04 | ✓ | table + ul + ol×2 + Делать/Не делать |
| R01 | ✓ | Инсайт, схема до депозита, FAQ-блоки |
| R02 | ✓ | BitAuto 27款 + tank.ru ориентиры + утиль полосы; источники в Fact Check Box |
| R03 | ✓ | Цены как ориентиры/не оферта; калькулятор пошлин в статье не публикуем |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол: русские ярлыки ≠ китайские коды; утиль без льготы |
| E02 | ✓ | «Делать / Не делать» в каждой H2-секции |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B; без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Льготы нет; вилка утиля; стоп-лист оплаты |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain → solution → result (GEO)

- **Lead pain:** перепутать Сити/Техно/Оникс с Hi4-T и узнать утиль после депозита.
- **H2 solutions:** таблица соответствий; закрыть утиль до оплаты; must-have; чек-лист документов.
- **До FAQ:** критерий успеха — в договоре зафиксированы китайский код, силовая, места, план осмотра.

## Link verify

- total: 2 unique OK (каталог встречается 2× + Telegram) — report: 2 links, failed 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (таблица/схема + плотные абзацы)
- Flesch RU: 68.5

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T Author: pending (schema вне зоны QA)

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних B01 — 2–3 internal links с `anchor_variants`.
2. **fact-bank soft:** ориентиры BitAuto ¥ / tank.ru ₽ / утиль полосы — дописать в fact-bank для verified.
3. **CTA hygiene:** в HTML уже абсолютные URL каталога/Telegram (не `${CATALOG_URL}`); для git-гигиены предпочтительны placeholders + pragma — не блок, link-verify PASS.
4. **slop over-long:** укоротить 1–2 абзаца при следующем FIX-цикле writer (не требуется сейчас).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema (параллельно).
