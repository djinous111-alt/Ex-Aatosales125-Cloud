# Article QA — B04

**topic_id:** B04  
**slug:** kak-zakazat-avto-iz-kitaya-pod-klyuch-2026  
**article_dir:** memory/blog/articles/B04-kak-zakazat-avto-iz-kitaya-pod-klyuch-2026  
**date:** 2026-09-30  
**verdict:** PASS  
**score:** 87  
**runner:** generalPurpose fallback (excalibur-blog-geo-qa)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-09-30; pain/outcome/voice brief OK |
| fact-check | PASS | 7 stats; 1 verified (2026); 6 unverified (160 л.с., 180 дней, сроки) — есть в research-notes |
| link-verify | PASS | 6/6 OK (3 internal blog + catalog + Telegram + 2GIS); `--site-base` из env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 65.0 |
| cannibalization | PASS | 0 issues (3 article meta в blog-dir) |
| utility gate | PASS | action=8, pain=5, outcome=8; ol/FAQ/table OK |
| human-voice | PASS | warnings: Fact Check template; 3× exactly-5-step lists |

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Цена в объявлении ≠ ключи; риск депозита в WeChat без договора/сметы/мощности |
| Где решение | H2: «под ключ» vs сам → страна → мощность → пакет до депозита → цепочка Вл → стоп-лист |
| Первый результат | Заполненный стоп-лист до депозита + 6–8 этапов + куда идти за расчётом (до FAQ) |
| Термины «на пальцах» | Под ключ, утильсбор, СВХ, СБКТС, ЭПТС, правило 180 дней |
| Beginner-fit | PASS — не профиль разработчика; первый безопасный шаг = не платить без пакета |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1/lead; H2 actionable; CTA catalog×2 + Telegram×1 |
| GEO / citability | 23/25 | Инсайт, схемы, таблица CN/KR/JP, FAQ×6, стоп-лист |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 14/15 | PASS gate; soft warn Fact Check + одинаковые 5-step |
| Fact safety | 12/15 | Числа в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist, ~9113 plain chars, FAQ, без forms/pre/code |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как заказать авто из китая» в meta/H1/lead |
| C02 | ✓ | Lead = история Андрея + прямой ответ, без «в этой статье» |
| C03 | ✓ | Новичок, первый заказ из КНР, риск предоплаты |
| C04 | ✓ | Утильсбор, СВХ, СБКТС, ЭПТС, 180 дней объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логика: смысл → страна → мощность → пакет → цепочка → стоп → CTA → FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблицы + схемы, mode B |
| R01 | ✓ | Инсайт, вердикт стран, схемы, FAQ |
| R02 | ✓ | 160 л.с. / 180 дней / сроки в research-notes |
| R03 | ✓ | Нет цен лотов и выдуманных %; суммы — в каталоге |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол «цена ≠ ключи» + 180 дней ≠ запрет ФТС |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA ≤3 основного офера (каталог×2, Telegram×1) + 2GIS отзывы |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон research / Авто-Сейлс Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Риски WeChat, мощности, тишины в чате, 180 дней |
| Ept02 | ✓ | Internal: Япония под ключ, VIN CN, СБКТС/ЭПТС |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Blockers

- нет (после recovery: CTA href из env, 2GIS percent-encode, pain/outcome в editorial-policy)

## FIX (non-blocking / optional)

1. **human-voice soft:** варьировать формулировку блока «Достоверность данных»; один из 5-step списков сделать 4 или 6 пунктов.
2. **fact-check soft:** дописать в fact-bank 160 л.с. / 01.12.2025 / правило 180 дней для полного verified.
3. **CTA/git:** secret-scan может снова задеть Telegram href при commit — см. INC-20260930-0918 (restore at publish vs allowlist).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- research-notes-gate PASS ✓  
- link-verify pass ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
