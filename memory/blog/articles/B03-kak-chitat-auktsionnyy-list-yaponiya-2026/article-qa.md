# Article QA — B03

**topic_id:** B03  
**slug:** kak-chitat-auktsionnyy-list-yaponiya-2026  
**article_dir:** memory/blog/articles/B03-kak-chitat-auktsionnyy-list-yaponiya-2026  
**date:** 2026-10-02  
**verdict:** PASS  
**score:** 87

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: нет official docs URL (ожидаемо для аукционных листов) |
| fact-check | PASS | 9 stats; 3 verified; 6 unverified (пороги пробега 50–130 тыс. км — в research-notes, не в fact-bank) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); после FIX CTA href из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/легенда/чек-лист); Flesch RU 78.3 |
| cannibalization | PASS | 0 issues (3 article meta в blog-dir) |
| utility gate | PASS | action_markers 21; pain 8; outcome 8; FAQ×7; table×1; numbered 24 |
| human voice gate | PASS | WARN: 2 списка ровно по 5 шагов; story/pain/outcome overlap OK |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «как читать аукционный лист» в title/H1; H2 how-to; CTA×каталог/TG; нет 2–3 blog internal |
| GEO / citability | 24/25 | Инсайт-блок, таблица оценок, FAQ×7, чек-лист×10, порядок чтения |
| CORE-EEAT lite | 14/15 | 19/20 (Ept02) |
| Human voice | 15/15 | 0 AI-slop; reader_story Андрей/Prius |
| Fact safety | 12/15 | Пороги пробега в research-notes, не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9103 знака, FAQ 7, CTA без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как читать аукционный лист» в meta title / H1 |
| C02 | ✓ | Lead: боль новичка + порядок чтения до ставки |
| C03 | ✓ | Читатель: первый заказ с японского аукциона, риск депозита |
| C04 | ✓ | R / RA / 99 / XX / 修復歴 объяснены «на пальцах» |
| O01 | ✓ | H2 = action outline research (якоря → оценка/пробег → R/RA → схема → фото → дома → чек-лист) |
| O02 | ✓ | Логичный outline сверху вниз |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт-блок, таблица, FAQ |
| R02 | ✓ | Пороги 4.5/~100 тыс. км, R/RA — в research-notes |
| R03 | ✓ | Нет цен лотов/%; ориентиры с пометкой «легенда дома» |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «10 символов и порядок чтения», не словарь японского |
| E02 | ✓ | «Сделайте / Не делайте» в H2-секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски R/RA, W3, 99, претензии после экспорта |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit: PASS

- Боль новичка в lead: лист пугает буквами, ставка вслепую / депозит без разбора.
- Решение в H2: четыре якоря → оценка+пробег → R/RA/99 → схема → сверка с фото → чек-лист.
- Первый результат до FAQ: вердикт «беру / пропускаю / нужна проверка эксперта» по любому листу.
- Термины на пальцах: R, RA, 99, XX, W3, 修復歴, USS/TAA/HAA.

## Pain / solution map

| Боль | Где закрыта | Результат |
|------|-------------|-----------|
| Не понимает 4.5 и буквы | H2 оценка+пробег, таблица | Знает коридор 4–4.5 и лимит пробега |
| Путает XX с R | H2 R/RA + схема | XX на двери ≠ ремонт каркаса |
| Торопят с депозитом | H2 сверка фото + FAQ | Депозит только после «лист = фото» |

## Link verify

- total unique: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/легенды/чек-листа)
- Flesch RU: 78.3

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. **link-verify FAIL** — в `article.html` CTA `href` были литералы `[REDACTED]` (writer secret-scan workaround) → восстановлены `CATALOG_URL` / `TELEGRAM_URL` из env; повтор: PASS 2/2.
2. **insight label** — ярлык `TL;DR / Быстрый инсайт` заменён на `Коротко до ставки` (требование GEO QA skill vs пример writing-contract).

## FIX (non-blocking / optional)

1. **Ept02:** после известных URL соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** пороги пробега 4.5/~100 тыс. км — дописать в fact-bank.
3. **human-voice WARN:** варьировать длину списков (сейчас 2× ровно 5 пунктов).
4. **meta.char_count:** обновить 9108 → 9103 после FIX ярлыка.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
