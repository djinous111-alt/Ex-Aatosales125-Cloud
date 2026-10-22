# Article QA — B01

**topic_id:** B01  
**slug:** geely-monjaro-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-geely-monjaro-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-22  
**verdict:** PASS  
**score:** 90

## Beginner-fit / pain → solution → result

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Перепутать китайский Xingyue L с дилерским Monjaro, отдать депозит за не ту комплектацию/привод и узнать про коммерческий утильсбор после оплаты |
| Где решение | H2: задача поездок → ветки i-HEV/Changfeng/Dongfang Yao → кВт/возраст/утиль → сверка лота → смета по строкам → чеклист 10 пунктов |
| Первый результат | Карточка лота (5 блоков) + зелёный/красный чеклист до депозита; понятно «платить нельзя» при красных пунктах |
| Термины «на пальцах» | Xingyue L vs Monjaro, FWD/AWD/Wangyue, i-HEV (без розетки), утильсбор/льгота ~117,68 кВт, СБКТС/ЭПТС/ЭРА-ГЛОНАСС |

**Beginner-fit:** PASS (не jargon-for-devs; есть первый безопасный шаг до оплаты)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | errors=0; warning technical_topic false-positive (`ai` in pain) |
| fact-check | PASS | 9 stats; verified 3 / unverified 6 (в research-notes; не в fact-bank) |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` from env |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long (склейка таблиц/схем); Flesch RU 77.0 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action=45, pain=4, outcome=14; ol_li=14; FAQ×6; tables×2 |
| human-voice gate | PASS | warnings=0; Fact Check author = Редакция Авто-Сейлс (`avtosales-editorial`) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary «джили монжаро из китая» в title/H1; H2 how-to; CTA каталог×2 + TG×1 |
| GEO / citability | 24/25 | Инсайт-box, таблицы, схема ветки/сметы, FAQ×6, чеклист 10 |
| CORE-EEAT lite | 14/15 | 18/20 (см. ниже) |
| Human voice | 15/15 | 0 AI-slop; concrete markers; pain/outcome overlap |
| Fact safety | 13/15 | Ориентиры мощности/утиля в research; без статичных цен |
| Contract HTML | 10/10 | Whitelist PASS, ~9158 символов, FAQ, CTA, без форм |
| **Итого** | **90/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta title / H1 |
| C02 | ✓ | Lead: боль депозита + чеклист до оплаты |
| C03 | ✓ | Читатель: новичок почти у кнопки «оплатить» |
| C04 | ✓ | Ветки/привод/утиль объяснены просто |
| O01 | ✓ | H2 = outline research (задача→линейка→кВт→лот→смета→чеклист→FAQ) |
| O02 | ✓ | Логичный how-to |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + 2 таблицы + схемы, mode B |
| R01 | ✓ | Инсайт-box, workflow сметы, FAQ |
| R02 | ✓ | 8 версий, кВт/л.с., порог льготы — в research-notes |
| R03 | ✓ | Нет статичных цен/калькулятора сумм |
| R04 | ✓ | Ответ FAQ в 1-м предложении |
| E01 | ✓ | Угол Владивосток / до депозита |
| E02 | ✓ | «Сделайте / Проверьте / Избегайте» в секциях |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Автор Fact Check = registry `avtosales-editorial` |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: льгота не «подарок», CN-гарантия ≠ ОД |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3 (артефакт таблицы/схемы)
- Flesch RU: 77.0

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не потребовался (все гейты PASS с первого прогона)

## FIX (non-blocking / optional)

1. **Ept02:** после URL соседних постов — 2–3 internal links с `anchor_variants` (Indexer).
2. **fact-check soft:** 218/272/238 л.с., 5 лет / 150 000 км, «3 года» — дописать в fact-bank при желании verified.
3. **skill vs writing-contract:** skill запрещает ярлык `TL;DR / Быстрый инсайт`, writing-contract приводит его как пример; гейты не блокируют — оставить как у AS09 или согласовать контракты в fixer.

## Gate

- score ≥ 80 → **90** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
