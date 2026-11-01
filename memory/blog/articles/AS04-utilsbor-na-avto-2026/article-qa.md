# Article QA — AS04

**topic_id:** AS04  
**slug:** utilsbor-na-avto-2026  
**article_dir:** memory/blog/articles/AS04-utilsbor-na-avto-2026  
**date:** 2026-11-01  
**verdict:** PASS  
**score:** 88  
**cycle:** FIX-1 re-run

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warning: technical_topic false-positive (official docs) |
| fact-check | WARNING | 15 stats; verified 2 / unverified 13 vs fact-bank (цифры в research-notes) |
| link-verify | PASS | 2/2 OK (каталог + Telegram) |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | PASS | 0 клише; 3 over-long; Flesch RU 67.9 |
| cannibalization | PASS | 0 issues |
| utility gate | **PASS** | action 31; pain 4; outcome 12 |
| human voice gate | **PASS** | outcome lexicon ≥3; exactly-five lists = 1; 0 errors/warnings |

## Beginner-fit

- **PASS:** утильсбор / кВт / 30-минутная мощность / ТПО / льгота объяснены «на пальцах».
- **Боль новичка:** посчитать утильсбор «на глаз» / по чужому скрину и переплатить из‑за порога 160 л.с.
- **Решение:** H2 чеклист льготы + поля + каталог; **первый результат** до FAQ — фильтр «льгота / не льгота» + свежая цифра по лоту.

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 actionable; CTA каталог×2+TG; мало blog internal |
| GEO / citability | 23/25 | Коротко по делу, схема, таблица KR/CN/JP, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | Gate PASS; story Алексей; без TL;DR-ярлыка |
| Fact safety | 12/15 | Факты в research-notes; fact-bank soft |
| Contract HTML | 10/10 | Whitelist PASS, char_count 9000, FAQ, CTA, без форм |
| Utility / gates | 10/10 | utility + human-voice PASS |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «утильсбор на авто 2026» в title/H1 |
| C02 | ✓ | Lead: боль + «Проверьте пять полей… сможете понять» |
| C03 | ✓ | Физлицо, ввоз KR/CN/JP, Владивосток |
| C04 | ✓ | кВт, льгота, коммерция, 30-мин мощность |
| O01 | ✓ | H2 = action outline |
| O02 | ✓ | Логика → страны → льгота → ошибки → миф → поля → дальше |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + blockquote; mode B |
| R01 | ✓ | Insight «Коротко по делу» + схема + FAQ |
| R02 | ✓ | 3400/5200, 117,68 кВт, ПП 1291/1713 — в notes |
| R03 | ✓ | Без статичной таблицы коммерческих миллионов |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Страна ≠ ставка; порог 160 л.с. |
| E02 | ✓ | «Сделайте / Не делайте» + policy markers |
| E03 | ✓ | CTA каталог×2 + Telegram |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop = 0 |
| Ept01 | ✓ | Миф 01.04.2026, лимиты льготы |
| Ept02 | ✗ | Нет 2–3 internal links на другие посты блога |

**Target:** ≥16/20 ✓ · veto gates: нет

## Pain / solution

| Боль | Решение | Результат |
|------|---------|-----------|
| Скрин без своих кВт | Lead + H2 поля/чеклист | Пакет до депозита |
| Миф «из Кореи дешевле» | H2 сравнение | Формула одна |
| Льгота vs коммерция | H2 чеклист 3400/5200 | Ясный контур |
| Гибрид/EV мощность | H2 ошибки | 30-мин кВт из документов |
| Миф 1 апреля 2026 | H2 ЕАЭС | Не путать с прямым ввозом |

## Link verify

- total: 2, failed: 0

## AI-slop scan

- cliches: 0 · over-long: 3 · Flesch RU: 67.9

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes | cover/schema: **можно стартовать**

## Blockers

- нет

## FIX cycle (закрыто)

1. Writer FIX-1: action/outcome markers, insight label, list sizes → utility + human-voice PASS.
2. Director: restored `pain_markers_ru` / `outcome_markers_ru` in editorial-policy.

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links на опубликованные посты с `anchor_variants`.
2. **fact-bank:** дописать льготные ориентиры / порог 160 л.с. для verified.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify / research-notes / utility / human-voice → PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
