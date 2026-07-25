# Article QA — B01

**topic_id:** B01  
**slug:** kak-rastamozhit-avto-iz-korei-2026  
**article_dir:** memory/blog/articles/B01-kak-rastamozhit-avto-iz-korei-2026  
**date:** 2026-07-25  
**verdict:** PASS  
**score:** 88  
**fix_cycle:** 1/2 applied → re-QA PASS

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | re-check; research_date=2026-07-25 |
| fact-check | PASS | 5 stats; 4 unverified vs fact-bank (2025, 30 дней, 1713, 1291) — в research-notes / ПП |
| link-verify | PASS | 3/3 OK (AS09 internal + каталог + Telegram) |
| html-linter | PASS | 0 errors; один FAQ H2 = «Частые вопросы» |
| slop-detector | PASS | 0 клише; 5 over-long; Flesch RU 57.4 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues |
| utility gate | PASS | action_markers 20; pain 7; outcome 12 |
| human-voice gate | PASS | outcome ≥3; exactly_five_lists=1; errors=[] |

## Pain / solution / beginner-fit

| Проверка | Статус | Комментарий |
|----------|--------|-------------|
| Боль новичка | ✓ | Lead: Антон / СВХ / растущий счёт; «Боль новичка – куча букв…» |
| Решение в H2 | ✓ | этапы, владелец, депозит, СВХ, платежи, СБКТС/ЭПТС, чек-лист |
| Результат до FAQ | ✓ | «Итог и результат… получите рабочий пакет… сможете спокойно ждать» |
| Термины «на пальцах» | ✓ | СВХ / СБКТС / ЭПТС / утильсбор |
| Beginner-fit | PASS | первый безопасный шаг; тон не для IT-профи |

**Боль:** застрять на СВХ без депозита/пакета, путаница этапов и льготы.  
**Решение:** чек-лист депозит → СВХ → выпуск → СБКТС/ЭПТС → ГИБДД.  
**Первый результат:** пакет документов + депозит до судна + персональный расчёт в каталоге.

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 action; CTA; +1 internal blog |
| GEO / citability | 23/25 | Коротко-блок, схема, таблица, FAQ×7, чеклисты |
| CORE-EEAT lite | 18/20 | 18/20 см. ниже |
| Human voice | 15/15 | gate PASS, 0 AI-slop |
| Fact safety | 12/15 | без статичных сумм; soft unverified № ПП |
| Contract HTML | 10/10 | whitelist PASS, ~9485, FAQ, CTA |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «растаможка авто из кореи» в title/H1 |
| C02 | ✓ | Lead: боль + чеклист + «сможете не застрять» |
| C03 | ✓ | Читатель: первый ввоз из Кореи через Владивосток |
| C04 | ✓ | СВХ/СБКТС/ЭПТС/утильсбор объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Порядок до/на/после СВХ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + table + mode B |
| R01 | ✓ | insight + схема + чек-лист |
| R02 | ✓ | сроки/ПП из research (ориентиры) |
| R03 | ✓ | нет готовых сумм пошлин/утиля |
| R04 | ✓ | FAQ ответ в 1-м предложении |
| E01 | ✓ | угол «не застрять на СВХ» |
| E02 | ✓ | Сделайте/Не делайте + Делать/Не делать |
| E03 | ✓ | CTA каталог + @avtosales125 |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | автор registry avtosales-editorial |
| Exp03 | ✓ | slop hits = 0 |
| Ept01 | ✓ | риски льготы / самодельной декларации |
| Ept02 | ✗ | 1 internal (AS09); целевые 2–3 — опционально второй позже |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 3, failed: 0
- internal: `/blog/trust-encar-carhistory-proverka-do-depozita/` → 200
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5
- Flesch RU: 57.4

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes | Review: no  
**Итог:** PASS — можно cover \|\| schema.

## Blockers

- нет

## FIX cycle (QA)

1. Cycle 0 → FAIL 68 (FAQ в H2, action_markers, human-voice outcome).
2. Writer FIX 1/2 → re-QA: все гейты PASS, score 88.

## FIX (non-blocking / optional)

1. **Ept02:** ещё 1–2 internal blog links (AS08 и др.) при наличии URL.
2. **fact-check soft:** ПП 1713 / сроки — дописать в fact-bank.
3. **slop over-long:** укоротить lead при удобном случае.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
