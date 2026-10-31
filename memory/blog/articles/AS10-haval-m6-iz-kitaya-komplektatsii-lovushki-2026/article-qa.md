# Article QA — AS10

**topic_id:** AS10  
**slug:** haval-m6-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS10-haval-m6-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-31  
**verdict:** PASS  
**score:** 88

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warnings: technical topic без official docs URL |
| fact-check | PASS | 8 stats; verified 2 (2026, 12 месяцев); unverified 110/143/150/218/180 — в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram); `--site-base` из PUBLIC_SITE_URL |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 5 over-long (склейка таблицы/списков парсером); Flesch RU 71.3 |
| cannibalization | PASS | 0 issues (3 meta в blog-dir) |
| utility gate | PASS | action_markers 34; FAQ×6; table×1; ol/ul OK |
| human-voice | PASS | warnings: rhythm 0.34; «exactly-5-step lists» (soft) |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «как выбрать хавал м6 из китая» в H1/lead; H2 checklist; CTA; нет 2–3 blog internal |
| GEO / citability | 24/25 | TL;DR, таблица Оптимум vs Plus, схема workflow, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop hits |
| Fact safety | 13/15 | кВт/порог/180 дней в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, ~9425 знаков, FAQ, CTA×3, без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary how-to в H1 / lead / meta |
| C02 | ✓ | Lead: боль депозита на «красивое объявление» + стоп-правило |
| C03 | ✓ | Читатель: новичок с лотом M6/M6 Plus из Китая до депозита |
| C04 | ✓ | Оптимум vs Plus, кВт/льгота, 6MT/7DCT, ЭПТС/СБКТС «на пальцах» |
| O01 | ✓ | H2 = pain→solution outline research |
| O02 | ✓ | Логичный checklist до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + схема, mode B |
| R01 | ✓ | TL;DR, схема workflow, FAQ |
| R02 | ✓ | 110 кВт, 117,68, 180 дней, GW4G15M из research |
| R03 | ✓ | Суммы утиля/пошлин не публикуются; РРЦ как ориентир дилера |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита / перед Владивостоком» |
| E02 | ✓ | «Сделайте / Не делайте» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: льгота не «вшита», гарантия РФ нет, меню CN |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |
| Exp04 soft | ✗ | Инсайт начинается с ярлыка «TL;DR / Быстрый инсайт» (linter/HV PASS; optional polish) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Депозит на «максималку» без сверки кВт/опций/языка ГУ/гарантии |
| Где решение | H2: Оптимум vs Plus → кВт/утиль → КПП → опции по фото → русификация → красные флаги → финальный чеклист |
| Первый результат | Зелёный чеклист по одному лоту; депозит не переведён при любом красном пункте |
| Термины «на пальцах» | кВт vs л.с., 6MT/7DCT, ЭПТС/СБКТС, льготный утиль ≤117,68, CN-меню |
| Beginner-fit | PASS — безопасный первый шаг до оплаты, без «только для профи» |

## Link verify

- total: 2, failed: 0
- see link-verify.json

## AI-slop scan

- cliches: 0
- over-long: 5 (артефакт таблицы/списков)
- Flesch RU: 71.3

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требовался (все script gates PASS с первой прогонки)

## FIX (non-blocking / optional)

1. **Ept02:** после publish соседних постов — 2–3 internal links с `anchor_variants`.
2. **fact-check soft:** 110 кВт / 117,68 / 180 дней / GW4G15M — дописать в fact-bank.
3. **insight label:** по желанию убрать шаблонный префикс «TL;DR / Быстрый инсайт» (gates уже PASS).
4. **human-voice soft:** чуть разнообразить длину абзацев (variance 0.34).

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
