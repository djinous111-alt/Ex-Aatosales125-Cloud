# Article QA — B01 VW Tharu из Китая

**topic_id:** B01  
**slug:** vw-tharu-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-vw-tharu-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-31  
**verdict:** PASS  
**score:** 87  
**author_id:** avtosales-editorial (registry OK)

## Beginner-fit / pain → solution → result

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Перепутать Tharu и Tharu XR, кинуть депозит за турбо «160 сил» с коммерческим утильсбором и китайской ГУ без русского |
| Где решение | H2: развести платформы → мотор по кВт (117,68) → комплектации XR → ловушки → русификация CNS3.0 → карточка лота → Владивосток → чеклист |
| Первый результат | Заполненный чеклист до депозита; выбор Tharu vs XR и мотора без расчёта пошлин «из статьи» |
| Термины «на пальцах» | утильсбор, кВт vs л.с., DQ200/6AT, CNS3.0/SFD2, СВХ, СБКТС, ЭПТС |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | re-check; research_date=2026-10-31 |
| utility gate | PASS | action 25 / pain 9 / outcome 12; FAQ×6; table×1; ol×7 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| link-verify | PASS | 2/2 OK (каталог + Telegram); URLs sanitized in report |
| cannibalization | PASS | 0 issues (3 meta loaded) |
| human-voice | PASS | `human-voice-report.json`; overlap pain/outcome/story OK |
| slop-detector | PASS | 0 клише; 2 over-long (ol/workflow склейка); Flesch RU 73.7 |
| fact-check | PASS | 10 extracted / 1 verified vs fact-bank; цифры Tharu/XR/кВт в research-notes |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; CTA каталог×2 + TG×1; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт-блок, таблица моторов, workflow, FAQ×6, чеклист |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop |
| Fact safety | 13/15 | Порог 117,68 / XR 2024 / мощности в research-notes; soft unverified vs fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; объём 9009; FAQ; без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать фольксваген тару из китая» в meta/H1 |
| C02 | ✓ | Lead: боль депозита / «не тот Tharu» |
| C03 | ✓ | Новичок под заказ из Китая через Владивосток |
| C04 | ✓ | Tharu vs XR, кВт, CNS3.0 объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + workflow; mode B |
| R01 | ✓ | Инсайт, таблица, FAQ, чеклист |
| R02 | ✓ | Цифры с опорой на research-notes / ПП / SAIC-VW |
| R03 | ✓ | Нет сумм пошлин/цен лотов в статье |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол checklist до депозита |
| E02 | ✓ | «Сделайте так / Не делайте» |
| E03 | ✓ | CTA каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: льготы зависят от условий; платежи только в каталоге |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Gate checklist

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice PASS ✓  
- beginner-fit PASS ✓  
- link-verify pass ✓  

## FIX cycle (QA)

1. Инсайт-блок: ярлык `TL;DR / Быстрый инсайт` → `Инсайт до депозита` (контракт GEO QA skill). Повтор gates: все PASS.

## Blockers

- нет

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты/ol) | cover/schema: вне зоны QA

**Итог:** PASS — можно cover \|\| schema.
