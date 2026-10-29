# Article QA — B01

**topic_id:** B01  
**slug:** geely-atlas-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-geely-atlas-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-30  
**verdict:** PASS  
**score:** 87

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит «на красивое объявление»; путаница Atlas Pro / Boyue L / Atlas L → чужой мотор, экран, без AWD/зимних опций |
| Где решение | H2: поколение → ярлык vs опции → красные флаги → сверка карточки (ol×8) → чек-лист до депозита |
| Первый результат | Письменный мини-чек-лист в чате: поколение, мотор, привод, 8–12 опций, VIN/фото, план ЭПТС+СБКТС |
| Термины «на пальцах» | ЭПТС / СБКТС в lead; Flagship ≠ РФ Flagship; FWD типичен для Boyue L; Boyue L = экспортный Atlas |

**beginner-fit:** PASS — без тона «для профи», есть первый безопасный шаг (сверка до денег), термины объяснены сразу.

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date 2026-10-30; sources 32; pain_solution 7; action_outline 8; technical_topic false |
| fact-check | PASS | 12 extracted / 1 verified in fact-bank; габариты/мощность опираются на research (Geely PDF) — soft, не blocker |
| link-verify | PASS | 2/2 HEAD 200; `--site-base` из `PUBLIC_SITE_URL` |
| html-linter | PASS | whitelist OK; TOC нет; insight «Инсайт до депозита» (не TL;DR) |
| slop-detector | PASS | 0 клише; over-long 3; Flesch RU 74.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 16 / pain 8 / outcome 18; ol×8; FAQ×6; table×1 |
| human voice gate | PASS | pain/outcome markers OK; reader_story/pain/outcome/success overlap; exactly_five_lists=1 (не BLOCK) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «джили атлас из китая»; H2 actionable; CTA×3; нет 2–3 internal blog links |
| GEO / citability | 23/25 | Insight-блок, таблица Pro vs Boyue L, схема сверки, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | human-voice PASS; 0 AI openings; concrete markers |
| Fact safety | 13/15 | Цифры габаритов/л.с. не в fact-bank (есть в research); без чужих сумм «под ключ» |
| Contract HTML | 10/10 | Whitelist PASS; ~8955–9200; FAQ; CTA; без форм/`pre` |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в title_seo / description / lead |
| C02 | ✓ | Lead: боль депозита + ответ «сверить до денег» |
| C03 | ✓ | Читатель: новичок, заказ Atlas из Китая |
| C04 | ✓ | ЭПТС, СБКТС, Boyue L, FWD объяснены |
| O01 | ✓ | H2 = research action_outline |
| O02 | ✓ | Логика: поколение → опции → флаги → сверка → чеклист |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol 8 шагов + ul чеклисты + таблица; mode B |
| R01 | ✓ | Insight + схема → |
| R02 | ✓ | Габариты/моторы с пометкой офиц. Geely / ориентир |
| R03 | ✓ | Нет лотовых цен/% «под ключ» |
| R04 | ✓ | FAQ отвечает действием в 1-м предложении |
| E01 | ✓ | Угол «не отдать депозит за чужую машину» |
| E02 | ✓ | «Сделайте так / Не делайте так» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Гарантия РФ не переносится; меню CN; серые СБКТС |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 74.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (ol + чеклисты) | Review: no | cover/schema: вне зоны QA

## Blockers

- нет

## FIX (non-blocking / optional)

1. **Ept02:** после публикации соседних China-SUV постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** габариты Boyue L / Atlas Pro и ~177 л.с. — дописать в fact-bank.
3. **exactly_five_lists:** один список ровно из 5 пунктов — при желании разбить/расширить (human-voice не BLOCK).

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
