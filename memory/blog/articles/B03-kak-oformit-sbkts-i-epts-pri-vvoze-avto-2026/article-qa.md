# Article QA — B03 (cycle 2)

**topic_id:** B03  
**slug:** kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026  
**article_dir:** memory/blog/articles/B03-kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026  
**date:** 2026-10-06  
**verdict:** PASS  
**score:** 92  
**fix_cycle:** 2/2 — Writer FIX cycle 1 принят

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | `research-notes-gate.json`; research_date=2026-10-06 |
| fact-check | PASS | 7 stats; verified 2; unverified 5 (ГОСТ 33670-2015, ТР ТС 018/2011, годы/пошлина) — в research-notes |
| link-verify | PASS | failed_count=0/8; CTA catalog×2 + Telegram×1 → 200; elpts.ru + elpts-info×2 → 200; internal×3 → 200 |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK; ярлыка TL;DR нет |
| slop-detector | PASS | 0 клише; 4 over-long (склейка table/ol парсером); Flesch RU 64.2 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers 23; pain 4; outcome 13; FAQ×6; table×1 |
| human-voice gate | PASS | `human-voice-report.json`; warn: 2× exactly-5-step lists (мягко) |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | После таможни стена аббревиатур + риск посредника «по фото» и ЭПТС «Незавершённый» |
| Где решение | H2: порядок → пакет → РАЛ → ЭПТС «Действующий» → ЭРА отдельно → чек-лист |
| Первый результат | Чек-лист + номер лаборатории в РАЛ + статус ЭПТС «Действующий» до ГИБДД |
| Термины «на пальцах» | СБКТС, ЭПТС, ОТТС, РАЛ, СЭП, ИЛ, ЭРА объяснены в lead/H2 |
| Beginner-fit | PASS — не профи-тон; безопасный первый шаг без команды разработчиков |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 19/20 | Primary в title/H1; H2 how-to; internal blog + рабочие CTA |
| GEO / citability | 23/25 | Схема/таблица/FAQ×6/чеклист; инсайт без запрещённого ярлыка |
| CORE-EEAT lite | 15/15 | 20/20 (E03 CTA URL восстановлены) |
| Human voice | 14/15 | 0 slop; warn ровно-5 шагов ×2 |
| Fact safety | 13/15 | Ориентиры цен/пошлин с пометкой; unverified годы норм в notes |
| Contract HTML | 10/10 | CTA href рабочие; TL;DR убран; FSA plain text; elpts→elpts.ru |
| **Итого** | **92/100** | |

## CORE-EEAT lite: 20/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как оформить СБКТС и ЭПТС» в title/H1 |
| C02 | ✓ | Lead — боль после таможни + порядок |
| C03 | ✓ | Новичок после выпуска ТД/ТПО, Владивосток |
| C04 | ✓ | СБКТС/ЭПТС/ОТТС/РАЛ/СЭП объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный порядок до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + blockquote, mode B |
| R01 | ✓ | Инсайт «Коротко по цепочке» / схема / чеклист / FAQ |
| R02 | ✓ | ГОСТ 33670, РАЛ, elpts, ориентиры цен в notes |
| R03 | ✓ | Нет цен лотов; сметы — ориентиры |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол after-customs Vladivostok; конфликт «по фото» vs очный осмотр |
| E02 | ✓ | «Сделайте / Не делайте» по секциям |
| E03 | ✓ | CTA каталог×2 + Telegram×1 с рабочими URL (env CATALOG/TELEGRAM) |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски посредника, «Незавершённый», светотехника RHD |
| Ept02 | ✓ | Internal: ЭРА LIVE + таможня + растаможка CN |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate link-verify:** PASS

## Link verify

- total unique checked: 8, failed: 0
- see `link-verify.json`
- Internals: 3 blog posts → 200
- CTA: catalog×2 + Telegram×1 → 200 (из env; в Cloud UI могут отображаться как `[REDACTED]`)
- Externals: elpts.ru, elpts-info×2 → 200
- FSA РАЛ: plain text `pub.fsa.gov.ru/ral` (без href) — осознанный FIX cycle 1 из-за SSL timeout

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт table/list)
- Flesch RU: 64.2

## Schema ready

BlogPosting: ready for schema agent | FAQPage: yes (6) | HowTo: yes (чеклисты) | cover/schema: **можно** стартовать после Director handoff PASS

## Writer FIX cycle 1 — verification

| FIX item | Status |
|----------|--------|
| CTA href из CATALOG_URL/TELEGRAM_URL | ✓ link-verify 200 |
| Убран ярлык TL;DR / Быстрый инсайт | ✓ «Коротко по цепочке» |
| portal.elpts.ru → elpts.ru (+ elpts-info guides) | ✓ 200 |
| FSA RAL plain text | ✓ нет битого href |
| char_count ~9352 | ✓ meta 9352 |

## Soft notes (non-blocking)

1. **human-voice warn:** два списка ровно по 5 пунктов — варьировать 4/6/7 при следующем редактировании.
2. **fact-check soft:** дописать в fact-bank ГОСТ 33670-2015, ТР ТС 018/2011, ориентир пошлины 600 ₽.
3. **slop over-long:** артефакт парсера table/ol — не критично.

## Gate

- score ≥ 80 → **92** ✓  
- CORE-EEAT ≥ 16/20 → **20/20** ✓  
- link-verify pass → ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — Director может запускать cover || schema. FIX list для writer не требуется.
