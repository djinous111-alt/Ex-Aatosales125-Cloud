# Article QA — AS20

**topic_id:** AS20  
**slug:** levyj-rul-iz-korei-2026-kak-kupit  
**article_dir:** memory/blog/articles/AS20-levyj-rul-iz-korei-2026-kak-kupit  
**date:** 2026-07-22  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-07-22; source_table 17; pain_solution 8 |
| fact-check | PASS | 1/1 verified (2026 in fact-bank) |
| link-verify | PASS | 2 unique CTA OK (каталог + Telegram); `--site-base` from env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы/чеклист); Flesch RU 69.6 |
| cannibalization | PASS | 0 issues |
| utility gate | PASS | action_markers 30 (≥8); pain 5; outcome 10; FAQ×7; table×1 |
| human-voice gate | PASS | pain≥2; outcome≥3; story/pain/outcome overlap OK; warn: multi 5+ ol |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Давление «кинь депозит сегодня» по красивой карточке Encar → риск Rent/скрытого ремонта/сюрприза по мощности |
| Где решение | H2: Корея vs Япония → Encar руль/VIN → Performance Check → Carhistory → договор до перевода → Владивосток/СВХ → чеклист 12 пунктов |
| Первый результат | Решение да/нет по лоту до депозита по 12 пунктам (VIN, X/W, Rent, договор с юрлицом) |
| Термины «на пальцах» | Encar, Performance Check (X/W), Carhistory, СВХ, утильсбор — объяснены в секциях |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 actionable; CTA×3; мало blog-internal |
| GEO / citability | 23/25 | инсайт, таблица, схемы →, FAQ×7, чеклист 12 |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 14/15 | PASS; warn multi-ol ≥5 |
| Fact safety | 14/15 | без готовых сумм пошлин; факты из research |
| Contract HTML | 10/10 | whitelist PASS, ~9986 знаков, FAQ, CTA ≤ лимитов |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «левый руль из кореи» в title / H1 |
| C02 | ✓ | Lead: боль депозита + чеклист до перевода |
| C03 | ✓ | Читатель: новичок, лот Encar, риск депозита |
| C04 | ✓ | Encar / Performance Check / Carhistory / СВХ объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклист, mode B |
| R01 | ✓ | инсайт, схемы, FAQ |
| R02 | ✓ | без выдуманных сумм пошлин; ссылка на расчёт |
| R03 | ✓ | нет фейковых цен лотов/% |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | угол «до депозита», разведение с AS09 |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | тон Авто-Сейлс / research |
| Exp03 | ✓ | slop hits = 0 |
| Ept01 | ✓ | лимиты: X/W, Rent, давление, физлицо |
| Ept02 | ✗ | нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

- PASS: не тон «для профи»; термины с пояснением; первый безопасный шаг — чеклист до депозита без команды разработчиков.

## Link verify

- total unique: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схем)
- Flesch RU: 69.6

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. Utility + human-voice BLOCK → lead: «боль/проблема/ошибка»; «Сделайте/Не делайте»; «чеклист»; «шаг N / ориентир / используйте / избегайте / проверьте»; CTA href восстановлены с литерала `[REDACTED]`; ol длины 6/4/12/6. Повтор: utility PASS, human-voice PASS.

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних URL — 2–3 internal links (AS09 Trust Encar и др.) с `anchor_variants`.
2. **human-voice warn:** уменьшить число `<ol>` с ≥5 пунктами (часть в `<ul>`).
3. **slop over-long:** артефакт таблицы; не критично.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
