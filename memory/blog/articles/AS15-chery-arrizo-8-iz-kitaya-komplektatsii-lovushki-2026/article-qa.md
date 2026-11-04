# Article QA — AS15

**topic_id:** AS15  
**slug:** chery-arrizo-8-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/AS15-chery-arrizo-8-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-11-04  
**verdict:** PASS  
**score:** 88  
**author_id:** avtosales-editorial  
**article_mode:** B  
**char_count:** 8855  
**Cloud Task:** typed `excalibur-blog-geo-qa` unavailable → `Task(generalPurpose)` fallback

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Депозит на «красивую фотку» без VIN; путаница дилерских 150 л.с. с CN Conquer / PRO / Tenet |
| Где решение | H2: задача → линейка CN/РФ/PRO → мотор/КПП → trim по VIN → красные флаги → смета → чек-лист до депозита |
| Первый результат до FAQ | Папка «до депозита»: VIN + trim + кВт + смета; депозит не переведён без совпадения |
| Термины «на пальцах» | Conquer vs PRO vs РФ Active/Prime/Ultra; кВт vs л.с.; 7DCT vs 8AT; trim 智/睿/劲/御; утиль/ЭПТС без магических цен |

**beginner_fit:** PASS

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | re-run 2026-11-04; sources 27 / domains 13; human brief OK |
| utility gate | PASS | action 22 / pain 4 / outcome 7; lists+table+FAQ×6 |
| human-voice gate | PASS | `human-voice-report.json`; reader_story/pain/outcome overlap OK; insight ≠ TL;DR |
| fact-check | PASS | 12 stats; 1 verified in fact-bank; 11 soft unverified — все в research-notes (147/187/110/150/254/310/390/117,68/180) |
| link-verify | PASS | 2 unique links; Telegram 200; catalog `catalog_ssl` soft-pass (Cloud egress); placeholders `${CATALOG_URL}` / `${TELEGRAM_URL}` |
| html-linter | PASS | whitelist OK; TOC с якорями нет |
| slop-detector | PASS | 0 клише; 3 over-long; Flesch RU 87.5 |
| cannibalization | PASS | `--blog-dir memory/blog/articles`; 0 issues vs AS10–AS14 |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «арризо 8 комплектации» в title/H1/meta; H2 how-to; CTA catalog×2 + TG×1; нет 2–3 blog internal |
| GEO / citability | 24/25 | Инсайт до депозита, таблица линеек, FAQ×6, чек-листы, workflow blockquote |
| CORE-EEAT lite | 19/20 | см. таблицу ниже |
| Human voice | 15/15 | human-voice PASS; 0 AI-slop |
| Fact safety | 13/15 | Цифры моторов/утиля в research-notes; не все в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; 8855 в диапазоне; FAQ; CTA; без форм |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary query в title / H1 / description |
| C02 | ✓ | Lead: депозит без VIN + боль путаницы trim/мощности |
| C03 | ✓ | Читатель: новичок заказывает седан из Китая до депозита |
| C04 | ✓ | Conquer / PRO / Tenet / кВт / DCT объяснены без жаргона профи |
| O01 | ✓ | H2 = research action outline (задача→линейка→мотор→VIN→флаги→смета→чек-лист) |
| O02 | ✓ | Логичный how-to outline |
| O03 | ✓ | FAQ 6 (в диапазоне 5–7) |
| O04 | ✓ | ol/ul + таблица + workflow; mode B |
| R01 | ✓ | Инсайт-блок + чек-лист результата + FAQ |
| R02 | ✓ | 147/187 кВт, 110 кВт/150 л.с., порог 117,68 кВт — в research-notes |
| R03 | ✓ | Нет магических цен под ключ / выдуманных % |
| R04 | ✓ | FAQ отвечает в первом предложении |
| E01 | ✓ | Угол «до депозита» + разведение CN vs РФ vs PRO |
| E02 | ✓ | «Делайте / Не делайте» + стоп-правила |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person эксперта |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: утиль по документам, ~180 дней с оговоркой, язык ПО |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога (только каталог + Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0, verdict: pass
- soft_pass: `catalog_ssl` (допустимо по контракту Cloud egress)
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 87.5

## Schema ready

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

- не требуется: `article.html` / `article.meta.json` не правились

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice PASS ✓  
- beginner-fit PASS ✓  
- link-verify pass (catalog SSL soft-pass OK) ✓  

**Итог:** PASS — директор может запускать cover \|\| schema.
