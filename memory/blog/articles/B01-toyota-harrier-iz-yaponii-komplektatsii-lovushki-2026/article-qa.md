# Article QA — B01

**topic_id:** B01  
**slug:** toyota-harrier-iz-yaponii-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-toyota-harrier-iz-yaponii-komplektatsii-lovushki-2026  
**date:** 2026-10-22  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-22; source table / pain_solution / reader_story OK |
| fact-check | PASS | 7 extracted; 1 verified vs fact-bank; годы/л.с. покрыты research-notes (Toyota Global / JP manuals) |
| link-verify | PASS | 2/2 OK (каталог avto-sales125.ru ×2 unique + t.me/avtosales125); после QA-fix literal `[REDACTED]` href |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 76.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | article gate: action/pain/outcome markers; H2×6+FAQ; table×1; numbered lists OK |
| human-voice-gate | PASS | warnings: 3× exactly-5-step lists (не blocker) |

## Beginner-fit / pain → solution → result

| Поле | Содержание |
|------|------------|
| Боль новичка | Путает «2.0» кузовов 60/80, не знает льготный порог по л.с., боится R/RA и гибрид-пометок до ставки |
| Где решение | H2: бюджет под ключ → коды кузова/таблица → грейды G/Z → красные флаги листа → чек-лист до депозита |
| Первый результат | Карточка лота (код/мотор/л.с./привод/флаги) + письменный расчёт под ключ до депозита |
| Термины «на пальцах» | Код кузова, льготный порог ≤160 л.с., R/RA, E-Four, HV/SOH, грейды S/G/Z |

**Beginner-fit:** PASS

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «тойота харриер из японии» в title/H1; H2 how-to; CTA×3; нет 2–3 internal blog links |
| GEO / citability | 23/25 | TL;DR, схема до ставки, таблица кодов, FAQ×7, чек-листы |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; reader_story Алексей; 0 AI-slop hits |
| Fact safety | 13/15 | Числа л.с./годы в research-notes; не все в fact-bank; суммы утиля не выдуманы |
| Contract HTML | 10/10 | Whitelist PASS, ~9494 знаков, FAQ×7, CTA≤3, без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: боль + чек-лист до ставки |
| C03 | ✓ | Читатель: новичок, заказ Harrier из Японии |
| C04 | ✓ | Коды кузова / R/RA / E-Four / HV объяснены |
| O01 | ✓ | H2 = outline research (бюджет → кузова → комплектация → флаги → чек-лист → FAQ) |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | TL;DR, схема, FAQ |
| R02 | ✓ | ~151 / ~171 л.с., июнь 2020, грейды S/G/Z в research-notes |
| R03 | ✓ | Суммы утиля/ставки не фиксированы; «сначала расчёт» |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до ставки / до депозита» |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: лист ≠ SOH батареи; RA ≠ «мелочь» |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0
- see `link-verify.json`
- QA fix: writer оставил `href="[REDACTED]"` ×3 → восстановлены URL из `memory/brief/conversion-map.md` / канон AS08–AS09

## AI-slop scan

- cliches: 0
- over-long: 4
- Flesch RU: 76.6

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. **Сделано QA:** literal `[REDACTED]` в 3 CTA `href` → рабочие URL каталога и Telegram; link-verify PASS.
2. Writer cycle не требуется (score ≥80, все gates PASS).
3. Optional follow-up (не blocker): indexer добавит 2–3 internal blog links; writer может варьировать размер списков (сейчас 3× ровно 5 шагов).
