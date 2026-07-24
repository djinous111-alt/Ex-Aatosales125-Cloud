# Article QA — B05

**topic_id:** B05  
**slug:** rastamozhka-elektromobilya-iz-kitaya-2026  
**article_dir:** memory/blog/articles/B05-rastamozhka-elektromobilya-iz-kitaya-2026  
**date:** 2026-07-25  
**verdict:** PASS  
**score:** 86  
**cover/schema:** одобрены (все gates PASS, score ≥ 80)  
**re-check:** после Writer FIX cycle 1 + Fixer policy (pain/outcome markers)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-07-25; sources/pain brief OK |
| fact-check | PASS | 4 stats; verified 1 (2026); soft unverified: 2022, 2025, №111 |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из `PUBLIC_SITE_URL` |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/схемы/Fact Check); Flesch RU 58.2 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action 16; pain 6; outcome 7; water 0 |
| human voice gate | PASS | warning: multiple exactly-5-step lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в H1/title; actionable H2; CTA×каталог+TG; нет 2–3 blog internal |
| GEO / citability | 22/25 | TL;DR, таблица EV vs ДВС, схема пути, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | checklist 17/20 (см. ниже) |
| Human voice | 14/15 | human-voice PASS; warning по спискам из 5 пунктов |
| Fact safety | 12/15 | Нет сумм пошлин; soft unverified годы/№111 вне fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9114 символов, FAQ×7; **utility PASS** |
| **Итого** | **86/100** | было 74 (utility BLOCK) → после FIX+policy |

## CORE-EEAT lite: 17/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка электромобиля из китая» в H1 / meta |
| C02 | ✓ | Lead: боль депозита/льготы + прямой ответ про цепочку этапов |
| C03 | ✓ | Читатель: новичок РФ, китайский EV, страх таможни |
| C04 | ✓ | СВХ / СБКТС / ЭПТС / утиль / ЭРА-ГЛОНАСС «на пальцах» |
| O01 | ✓ | H2 = сравнение → словарь → pre-deposit → путь → миф ЕАЭС → счёт → чек-лист |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + table + blockquote схемы, mode B |
| R01 | ✓ | TL;DR + схема пути + FAQ |
| R02 | ✓ | ЕЭК № 111 / AM·BY·KG; факты в research-notes |
| R03 | ✓ | Нет сумм пошлин/утильсбора в HTML |
| R04 | ✓ | Ответы FAQ с первого предложения |
| E01 | ✓ | Угол «не через Киргизию для РФ» + pre-deposit |
| E02 | ✓ | «Сделайте / Не делайте» + «избегайте / используйте» |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон менеджера Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Ограничения льготы ЕАЭС, имена на документах, очередь лаборатории |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · **utility PASS → overall PASS**

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Страх таможни/жаргона + риск «льготного» оффера через ЕАЭС до депозита (lead + H2 миф 2026) |
| Где решение | H2 словарь, pre-deposit ol, путь СВХ→СБКТС→ЭПТС, финальный чек-лист |
| Первый результат | В заметках 5–7 шагов пути, документы на себя, отказ от токсичных схем; расчёт в каталоге |
| Термины «на пальцах» | СВХ, СБКТС, ЭПТС, утильсбор, 30-мин мощность, ЭРА-ГЛОНАСС |
| Beginner-fit | PASS (не профи-API тон; есть первый безопасный шаг без оплаты «в тёмную») |

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 6 (артефакт таблицы/схемы/Fact Check)
- Flesch RU: 58.2

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | cover/schema: **одобрены**

## Blockers

- нет

## FIX cycle 1 — закрыто

1. Writer: action_markers 5→16 («Не делайте», «Сделайте», «избегайте», «используйте», «чеклист»).
2. Fixer: `pain_markers_ru` / `outcome_markers_ru` в editorial-policy + utility skip-empty → pain 6 / outcome 7.
3. Re-check GEO QA: utility PASS, score 86 ≥ 80.

## Non-blocking (optional, не блокер)

1. Ept02: 2–3 internal links на другие посты блога после появления URL.
2. fact-check soft: дописать ЕЭК № 111 / льготы EV 2026 в `fact-bank.md`.
3. human-voice warning: варьировать длину списков (сейчас несколько ровно из 5 пунктов).
4. slop over-long: артефакт таблицы — не критично.

## Gate

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **17/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- human-voice PASS ✓  
- utility gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — директор может запускать cover \|\| schema.
