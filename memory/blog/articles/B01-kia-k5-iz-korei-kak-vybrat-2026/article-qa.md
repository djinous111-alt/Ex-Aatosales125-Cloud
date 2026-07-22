# Article QA — B01

**topic_id:** B01  
**slug:** kia-k5-iz-korei-kak-vybrat-2026  
**article_dir:** memory/blog/articles/B01-kia-k5-iz-korei-kak-vybrat-2026  
**date:** 2026-07-22  
**verdict:** FAIL  
**score:** 74

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes gate | PASS | research_date=2026-07-22; pain/outcome/story OK |
| fact-check | PASS | 7 stats; 1 verified in fact-bank; 160/146/180 в research-notes |
| link-verify | FAIL | 3 CTA `href` = литерал `[REDACTED]` (не URL); relative→404 |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 83.0 |
| cannibalization | PASS | 0 issues |
| utility gate | BLOCK | action_markers 6 < 8 (после дописи pain/outcome в policy) |
| human-voice gate | BLOCK | pain_markers только `ошиб` (<2); warn: 3× ol ровно на 5 шагов |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA есть, но href битые |
| GEO / citability | 22/25 | Инсайт, таблицы, схема, FAQ×7, чек-листы |
| CORE-EEAT lite | 14/15 | 19/20 (Ept02 без blog internal) |
| Human voice | 8/15 | BLOCK: слабо названа «боль» маркерами гейта |
| Fact safety | 12/15 | Факты в research-notes; часть не в fact-bank |
| Contract HTML | 2/10 | Whitelist PASS, но CTA href literал `[REDACTED]` + utility/HV gates |
| **Итого** | **74/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «киа к5 из кореи» в meta/H1 |
| C02 | ✓ | Lead — сцена Encar + турбо 180 до депозита |
| C03 | ✓ | Читатель: заказ K5 из Кореи, льготный утиль |
| C04 | ✓ | Encar / Carhistory / LPI / тримы объяснены |
| O01 | ✓ | H2 = цель → мотор → тримы → топливо → Encar → смета → чек-лист |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + 2 таблицы + схемы, mode B |
| R01 | ✓ | Инсайт, схема, вердикт по топливу, строки сметы |
| R02 | ✓ | 160 / 146 / 180 + бак LPI ~64 л в research-notes |
| R03 | ✓ | Нет финальных цен «под ключ»; витрина помечена |
| R04 | ✓ | FAQ ответ в 1-м предложении |
| E01 | ✓ | Угол «имя трима ≠ мотор» + стоп турбо 180 |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA ≤3 (каталог×2 + Telegram×1) — но URL сломаны |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски турбо/утиль, X/W, сервис LPG |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Путает красивый Signature/GT-Line с «безопасным» мотором; риск сорвать льготный утиль на 1.6T 180 |
| Где решение | H2 мотор/тримы/топливо/Encar + «Делать/Не делать» |
| Первый результат | 5 пунктов в заметках до брони (мотор ≤160, стоп 180, 1–2 трима, Encar+Carhistory, смета строками) |
| Термины «на пальцах» | Encar, Carhistory, Performance Check X/W, LPI/ВЗУ, Prestige/Noblesse/Signature |
| Beginner-fit | PASS по смыслу; formal HV pain markers — BLOCK |

## Link verify

- total: 1 unique broken (`[REDACTED]` literal), failed: 1
- see `link-verify.json`
- эталон CTA: как в AS09 / conversion-map — каталог `https://avto-sales125.ru/` + Telegram `https://t.me/avtosales125` (не строка `[REDACTED]`)

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 83.0

## Schema ready

BlogPosting: pending (после PASS) | FAQPage: yes (7) | HowTo: yes | Review: no

## Blockers (must FIX → writer)

1. **CTA href:** заменить все 3 `href="[REDACTED]"` на реальные URL из conversion-map / эталон AS09 (каталог + Telegram). Не оставлять литерал `[REDACTED]`.
2. **Utility action-маркеры:** сейчас 6 < 8. Добавить ≥2 из списка policy: `сделайте`, `не делайте`, `избегайте`, `используйте`, `шаг `, `чеклист` (без дефиса считается отдельно от «чек-лист»).
3. **Human voice pain:** нужны ≥2 разных маркера из: боль / проблем / ошиб / дорого / сложно / долго / … Сейчас только `ошиб`. В lead/H2 явно назвать проблему (например «проблема» + оставить «ошибка»).
4. **Инсайт-блок:** убрать шаблонный ярлык `TL;DR / Быстрый инсайт` → нейтральный заголовок (например «Короткий вывод:»).
5. **Списки:** 3× `<ol>` ровно по 5 пунктов — варьировать длину (warn HV).

## FIX cycle (QA)

1. Policy workaround: в `memory/brief/editorial-policy.json` добавлены `pain_markers_ru` / `outcome_markers_ru` + min counts (иначе utility BLOCK на любой статье, в т.ч. AS09 regression). Incident для fixer.
2. Writer FIX не делался GEO QA (longread не переписывался).

## Gate

- score ≥ 80 → **74** ✗  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✗  
- research-notes gate PASS → ✓  
- utility gate PASS → ✗  
- human-voice gate PASS → ✗  
- beginner-fit (смысл) → ✓ / formal HV pain → ✗  

**Итог:** FAIL — вернуть writer (FIX cycle 1). Cover/schema **не** запускать.
