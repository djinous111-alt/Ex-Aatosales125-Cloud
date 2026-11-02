# Article QA — AS10

**topic_id:** AS10  
**slug:** kak-vybrat-toyota-sienta-iz-yaponii-2026  
**article_dir:** memory/blog/articles/AS10-kak-vybrat-toyota-sienta-iz-yaponii-2026  
**date:** 2026-11-02  
**verdict:** FAIL  
**score:** 74  
**beginner_fit:** PASS

## Pain / solution / result (обязательная связка)

| Вопрос | Оценка | Где в статье |
|--------|--------|-------------|
| Какая боль новичка решена? | OK | Lead: семья почти кидает депозит на Hybrid с grade 3.5 / скрипом дверей, не понимая маршрут METI и состав «под ключ» |
| Где показано решение? | OK | H2: сценарий → код кузова → бензин/гибрид через маршрут → лист → смета этапов → Freed-таблица → чек-лист |
| Какой первый результат до FAQ? | OK | «Пройдите чек-лист перед депозитом»: код/маршрут/лист/смета без ставки вслепую |
| Термины «на пальцах»? | OK | код кузова, аукционный лист/grade, METI, СВХ, ЭПТС/СБКТС, E-Four, CVT — без брокеровского жаргона |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings=[] |
| utility gate | **BLOCK** | action_markers **4 < 8** (pain=3 / outcome=7 после дописывания списков в `editorial-policy.json`) |
| human-voice | PASS | WARN: 4 списка ровно по 5 пунктов — разнообразить длину |
| fact-check | PASS | 9 stats; 1 verified vs fact-bank; 8 unverified (даты/габариты в research-notes) |
| link-verify | **FAIL** | 1/1 failed: в `article.html` три `href="[REDACTED]"` (literal); DNS `avto-sales125.ru` / `avtosales125.ru` в этом run = Temporary failure in name resolution |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | WARNING | 0 клише; 6 over-long (склейка таблиц/схем); Flesch RU 71.2 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; FAQ×6; CTA сломаны literal REDACTED |
| GEO / citability | 20/25 | Схемы/таблицы/FAQ; инсайт с запрещённым ярлыком `TL;DR / Быстрый инсайт` |
| CORE-EEAT lite | 12/15 | 17/20 (см. ниже) |
| Human voice | 14/15 | human-voice PASS; WARN списки×5 |
| Fact safety | 12/15 | METI/Toyota в research; часть цифр не в fact-bank |
| Contract HTML | 5/10 | whitelist PASS, но CTA href = `[REDACTED]`; utility action markers fail |
| **Итого** | **74/100** | |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать toyota sienta из японии» в title/H1 |
| C02 | ✓ | Lead сразу про депозит/Hybrid/маршрут |
| C03 | ✓ | Читатель: семья/регионы, компактвэн из Японии |
| C04 | ✓ | Коды кузова, grade, METI объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный how-to |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + таблицы + чек-лист, mode B |
| R01 | ✓ | Инсайт + схемы + FAQ (ярлык TL;DR — contract smell) |
| R02 | ✓ | Даты METI/Toyota + размеры из research |
| R03 | ✓ | Нет чужих «итого под ключ» как прайс Авто-Сейлс |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «не гонитесь за Hybrid на табличке» |
| E02 | ✓ | «Делать / Не делать» (но не совпадает с recommendation markers «сделайте/не делайте») |
| E03 | ✗ | CTA href literal `[REDACTED]` — битые ссылки |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: нет фиксированной цены, срок «уточнять в смете» |
| Ept02 | ✗ | Нет internal blog links (только каталог/Telegram — и те битые) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** utility BLOCK · link-verify FAIL · score 74 < 80

## Link verify

- total: 1 (парсер схлопнул/увидел битый href), failed: 1
- disk: 3× `href="[REDACTED]"` , 0× `https`
- env note: DNS к каталогу в этом run не резолвится; `t.me` резолвится

## AI-slop scan

- cliches: 0
- over-long: 6
- Flesch RU: 71.2

## Schema ready

BlogPosting: deferred (FAIL) | FAQPage: deferred | cover/schema: **не запускать** до PASS

## Blockers

1. utility gate: action_markers 4 < 8  
2. link-verify: literal `[REDACTED]` в href + DNS каталога  
3. score 74 < 80  
4. contract: инсайт-блок с ярлыком `TL;DR / Быстрый инсайт`

## FIX cycle → writer (точечно, без полного рерайта)

1. **CTA href:** заменить все `href="[REDACTED]"` на реальные URL из `CATALOG_URL` / `TELEGRAM_URL` (или `memory/brief/conversion-map.md`). На диске сейчас 0 `https`. Лимиты: каталог ≤3, Telegram ≤2.
2. **Action-маркеры (≥8):** сейчас бьют только `проверьте`×1 + `ориентир`×3. Формулировки «Делать:» / «Не делать:» **не** считаются. Точечно:
   - заменить на «**Сделайте:**» / «**Не делайте:**» в H2-секциях; **или**
   - добавить 4+ вхождения из списка policy: `сделайте`, `не делайте`, `избегайте`, `чеклист`, `шаг `, `используйте`.
3. **Инсайт-блок:** убрать ярлык `TL;DR / Быстрый инсайт:` — оставить смысл без шаблонного префикса (skill GEO QA).
4. **Списки:** 4× ровно по 5 пунктов → сделать хотя бы два списка длины 4/6/7 (human-voice WARN).
5. **После правок:** не трогать cover/schema; вернуть geo-qa на re-gate.

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass → ✗  
- utility gate PASS → ✗  
- human-voice PASS → ✓  
- research-notes-gate PASS → ✓  
- beginner-fit PASS → ✓  

**Итог:** FAIL — cover \|\| schema **не** запускать; вернуть writer по FIX выше.
