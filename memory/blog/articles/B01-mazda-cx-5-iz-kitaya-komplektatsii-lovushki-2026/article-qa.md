# Article QA — B01

**topic_id:** B01  
**slug:** mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-mazda-cx-5-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-23  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL (ожидаемо для auto) |
| fact-check | PASS | 2 extracted; verified 1 (`2026`); unverified `360` (камеры 360°, false positive vs fact-bank) |
| link-verify | PASS | 3/3 OK (VIN-гайд internal + каталог + Telegram); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long (lead + склейка таблицы парсером + outcome); Flesch RU 67.7 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |
| utility gate | PASS | action_markers 26; FAQ×6; table×1; ol 7; pain/outcome OK |
| human-voice gate | PASS | pain/outcome/story/success_criteria overlap OK; 0 AI openings |

## Beginner-fit / pain → solution → result

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит за «максималку» по фото → Comfort/Zhishang без 360/кожи/ассистентов; путаница Smart/Elegant/Zhishang/Zhiya/Pro |
| Где решение | H2: маркеры версий на видео; ловушки Smart/Elegant/Black Pack; VIN+карточка; чеклист 10 пунктов; workflow до денег |
| Первый результат | Сравнить 2–3 лота; чеклист зелёный или депозит отложен |
| Термины «на пальцах» | Comfort/Zhishang/Zhiya/Pro, Black Pack, VIN (17 символов), заводская карточка, LHD/RHD, keyless, 360 |

**Beginner-fit:** PASS — тон для новичка, без требования команды разработчиков; безопасный первый шаг до депозита.

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1/description; H2 под outline; CTA каталог×2 + TG; 1 internal blog (VIN) |
| GEO / citability | 23/25 | TL;DR, таблица версий, workflow, FAQ×6, чеклист×10, блок достоверности |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | human-voice-report PASS; slop 0 |
| Fact safety | 12/15 | Факты в research-notes; `360` не в fact-bank (soft) |
| Contract HTML | 10/10 | Whitelist PASS, ~9277 символов, FAQ, CTA, mode B |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «мазда сх5 из китая комплектации» отражена в title/H1/meta |
| C02 | ✓ | Lead = боль депозита + путь сравнения до денег |
| C03 | ✓ | Читатель: новичок, заказ CX-5 из Китая |
| C04 | ✓ | Версии, Black Pack, VIN, карточка объяснены |
| O01 | ✓ | H2 = research outline (фото → версии → ловушки → VIN → чеклист → результат → FAQ) |
| O02 | ✓ | Логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + ul + table, mode B |
| R01 | ✓ | TL;DR, workflow blockquote, чеклист, FAQ |
| R02 | ✓ | Surprising fact: Zhiya дороже ≠ Pro-ассистенты; ярлыки Changan |
| R03 | ✓ | Без статичных цен «под ключ»; расчёт → каталог |
| R04 | ✓ | Ответы FAQ с первого предложения |
| E01 | ✓ | Угол «до депозита», не обзор ради обзора |
| E02 | ✓ | «Не делайте / запросите / стоп» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон редакции Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты VIN, пустые РФ-базы, маркетинговый год |
| Ept02 | ✗ | Только 1 internal blog link (VIN-гайд); желательно 2–3 после публикации соседних постов |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблицы + lead)
- Flesch RU: 67.7

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (ol + чеклист) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требовался (все gates PASS с первого прогона)

## FIX (non-blocking / optional)

1. **Ept02:** добавить 2–3 internal links на соседние посты после публикации.
2. **fact-check soft:** «камеры 360» — не число для fact-bank; при желании уточнить парсер.
3. **slop over-long:** артефакт таблицы; правки не критичны.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
