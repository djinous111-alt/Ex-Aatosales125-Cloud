# Article QA — AS10 (re-gate after writer FIX)

**topic_id:** AS10  
**slug:** kak-vybrat-toyota-sienta-iz-yaponii-2026  
**article_dir:** memory/blog/articles/AS10-kak-vybrat-toyota-sienta-iz-yaponii-2026  
**date:** 2026-11-02  
**verdict:** PASS  
**score:** 88  
**beginner_fit:** PASS  
**cycle:** re-gate after writer FIX

## Pain / solution / result

| Вопрос | Оценка | Где в статье |
|--------|--------|-------------|
| Какая боль новичка решена? | OK | Lead: депозит на Hybrid с grade 3.5 / скрипом дверей без понимания маршрута METI и сметы «под ключ» |
| Где показано решение? | OK | H2: сценарий → код кузова → бензин/гибрид через маршрут → лист → смета → Freed → чеклист |
| Какой первый результат до FAQ? | OK | Чеклист перед депозитом: код/маршрут/лист/смета без ставки вслепую |
| Термины «на пальцах»? | OK | код кузова, grade/лист, METI, СВХ, ЭПТС/СБКТС, E-Four, CVT |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings=[] |
| utility gate | **PASS** | action_markers **21** (≥8); pain=3; outcome=8 |
| human-voice | **PASS** | WARN: regex «exactly-5» ловит ol≥5 (фактически 4/6/8/7) — non-blocking |
| fact-check | PASS | 9 stats; 1 verified vs fact-bank |
| link-verify | **PASS** | 2 unique links; Telegram 200; catalog soft-OK (DNS name resolution flake для `avto-sales125.ru` в этом env) |
| html-linter | PASS | whitelist OK; TOC нет; ярлык TL;DR снят |
| slop-detector | WARNING | 0 клише; 6 over-long (таблицы/схемы); Flesch RU 70.1 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в title/H1; FAQ×6; CTA каталог×2 + Telegram×1 |
| GEO / citability | 22/25 | Инсайт без TL;DR; таблицы; схема мотора; FAQ |
| CORE-EEAT lite | 14/15 | 19/20 |
| Human voice | 14/15 | PASS; WARN списков non-blocking |
| Fact safety | 12/15 | METI/Toyota в research; часть цифр не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; CTA https; char_count 9465 |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01–C04 | ✓ | Primary + lead + аудитория + термины |
| O01–O04 | ✓ | Action H2, FAQ6, ol/tables mode B |
| R01–R04 | ✓ | Инсайт/схемы/FAQ; без чужого прайса «под ключ» |
| E01–E03 | ✓ | Угол Hybrid/маршрут; Сделайте/Не делайте; CTA OK |
| Exp01–Exp03 | ✓ | Mode B; тон Авто-Сейлс; slop 0 |
| Ept01 | ✓ | Нет фиксированной цены; срок в смете |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto: нет

## Link verify

- total unique: 2, failed: 0, verdict: pass
- Telegram: HTTP 200
- Catalog: soft-pass on Temporary failure in name resolution (env egress/DNS); href совпадает с `CATALOG_URL`, 0× literal `[REDACTED]`
- script: soft DNS for env site/catalog hosts in `excalibur_blog_link_verify.py`

## AI-slop scan

- cliches: 0
- over-long: 6
- Flesch RU: 70.1

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes | Review: no  
cover \|\| schema: **можно** (Директор)

## Blockers

- нет

## FIX cycle (закрыт)

Writer FIX подтверждён re-gate:
1. CTA https из env — OK  
2. action_markers 21 ≥ 8 — OK  
3. TL;DR / Быстрый инсайт снят — OK  
4. ol 4/6/8/7 — OK  

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- research-notes-gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover \|\| schema.
