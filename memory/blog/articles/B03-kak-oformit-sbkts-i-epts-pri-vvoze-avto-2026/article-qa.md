# Article QA — B03

**topic_id:** B03  
**slug:** kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026  
**article_dir:** memory/blog/articles/B03-kak-oformit-sbkts-i-epts-pri-vvoze-avto-2026  
**date:** 2026-10-06  
**verdict:** FAIL  
**score:** 76  
**fix_cycle:** 1/2 → вернуть Writer

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | `research-notes-gate.json`; research_date=2026-10-06 |
| fact-check | PASS | 7 stats; verified 2; unverified 5 (ГОСТ 33670-2015, ТР ТС 018/2011, 2025, 2027) — в research-notes |
| link-verify | FAIL | failed_count=5/8: 3× literal `href="[REDACTED]"` (404); `pub.fsa.gov.ru` SSL timeout; `portal.elpts.ru` DNS NXDOMAIN; `dp.elpts.ru`/`help.elpts.ru` 403/redirect |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (склейка table/ol парсером); Flesch RU 66.0 |
| cannibalization | PASS | 0 issues (3 article meta в blog-dir) |
| utility gate | PASS | action_markers 23; pain 4; outcome 13; FAQ×6; table×1 |
| human-voice gate | PASS | `human-voice-report.json`; warn: 2× exactly-5-step lists |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | После таможни стена аббревиатур + риск посредника «по фото» и ЭПТС «Незавершённый» |
| Где решение | H2: порядок → пакет → РАЛ → ЭПТС «Действующий» → ЭРА отдельно → чек-лист |
| Первый результат | Чек-лист + номер лаборатории в РАЛ + статус ЭПТС «Действующий» до ГИБДД |
| Термины «на пальцах» | СБКТС, ЭПТС, ОТТС, РАЛ, СЭП, ИЛ, ЭРА объяснены в lead/H2 |
| Beginner-fit | PASS — не профи-тон; есть безопасный первый шаг без команды разработчиков |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; internal blog links OK; CTA href сломаны |
| GEO / citability | 21/25 | Схема/таблица/FAQ×6/чеклист; инсайт с ярлыком `TL;DR / Быстрый инсайт` (запрет skill) |
| CORE-EEAT lite | 13/15 | 18/20 (E03 CTA URL broken) |
| Human voice | 14/15 | 0 slop; warn ровно-5 шагов ×2 |
| Fact safety | 12/15 | Ориентиры цен/пошлин с пометкой; unverified годы норм в notes |
| Contract HTML | 0/10 | 3× literal `[REDACTED]` в href CTA; link-verify FAIL |
| **Итого** | **76/100** | |

## CORE-EEAT lite: 18/20

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
| R01 | ✓ | Инсайт/схема/чеклист/FAQ (ярлык TL;DR — отдельный FIX) |
| R02 | ✓ | ГОСТ 33670, РАЛ, elpts, ориентиры цен в notes |
| R03 | ✓ | Нет цен лотов; сметы — ориентиры |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол after-customs Vladivostok; конфликт «по фото» vs очный осмотр |
| E02 | ✓ | «Сделайте / Не делайте» по секциям |
| E03 | ✗ | CTA каталог×2 + Telegram×1 есть текстом, но `href="[REDACTED]"` |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски посредника, «Незавершённый», светотехника RHD |
| Ept02 | ✓ | Internal: ЭРА LIVE + таможня + растаможка CN |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Hard gate link-verify:** FAIL → overall FAIL

## Link verify

- total: 8, failed: 5
- see `link-verify.json`
- Working: 3 internal blog posts (200)
- Broken CTA: 3× literal `[REDACTED]` → 404 as site-relative
- Externals flaky from Cloud: FSA SSL timeout; portal.elpts.ru NXDOMAIN; dp/help bot/redirect issues (dp отвечает 200 с browser UA)

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт table/list)
- Flesch RU: 66.0

## Schema ready

BlogPosting: pending (после PASS) | FAQPage: yes (6) | HowTo: yes (чеклисты) | cover/schema: **не стартовать** до PASS

## Blockers

1. **link-verify FAIL** — обязательный gate.
2. **CTA href = literal `[REDACTED]`** (3 места: каталог в H2 РАЛ + каталог/Telegram в «Что дальше»).
3. **Инсайт-блок** начинается с `TL;DR / Быстрый инсайт` — запрет GEO QA skill.

## FIX для Writer (обязательно, cycle 1)

1. **CTA URLs:** заменить все `href="[REDACTED]"` на рабочие URL из `memory/brief/conversion-map.md` / `site-brief.md` (как в AS09): каталог `https://avto-sales125.ru/` (×2), Telegram `https://t.me/avtosales125` (×1). Не оставлять плейсхолдер `[REDACTED]` в HTML.
2. **Инсайт-блок:** убрать ярлык `TL;DR` / `Быстрый инсайт`; оставить смысл цепочки в `<blockquote>` без шаблонного префикса.
3. **Внешние порталы (проверить вручную / альтернативы):**
   - `https://portal.elpts.ru/` — с этой среды DNS NXDOMAIN; подтвердить актуальный URL СЭП (рабочий якорь `https://elpts.ru/` отвечает 200) или оставить как текст+один рабочий URL.
   - `https://help.elpts.ru/` — redirect loop / 403 для бота; сверить актуальный help URL или формулировку «заявка через оформителя».
   - `https://pub.fsa.gov.ru/ral` — SSL handshake timeout из Cloud; URL канонический, оставить, но после фикса CTA перепроверить link-verify (возможен soft/env incident).
4. **Human-voice warn (мягко):** два списка ровно по 5 пунктов — варьировать длину (4/6/7), если правите соседние блоки.

## FIX (non-blocking / optional)

1. **fact-check soft:** дописать в fact-bank ГОСТ 33670-2015, ТР ТС 018/2011, ориентир пошлины 600 ₽.
2. **slop over-long:** артефакт парсера table/ol — не критично.

## Gate

- score ≥ 80 → **76** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass → ✗  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** FAIL — cover || schema **не** запускать. Вернуть Writer с FIX выше, затем GEO QA cycle 2.
