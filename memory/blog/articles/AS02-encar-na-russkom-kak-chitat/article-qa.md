# Article QA — AS02

**topic_id:** AS02  
**slug:** encar-na-russkom-kak-chitat  
**article_dir:** memory/blog/articles/AS02-encar-na-russkom-kak-chitat  
**date:** 2026-11-03  
**verdict:** PASS  
**score:** 88  
**CORE-EEAT lite:** 19/20  
**beginner_fit:** PASS

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date 2026-11-03; sources/pain/outcome OK |
| utility gate | PASS | action 15 / pain 5 / outcome 6; FAQ×6; table×1 |
| human-voice gate | PASS | warn: multiple exactly-5-step lists; insight label fixed |
| fact-check | PASS | 11 facts; verified 2; unverified 9 (в research-notes) |
| link-verify | PASS | soft_pass=`catalog_ssl`×2; Telegram HEAD 200 |
| html-linter | PASS | whitelist OK; TOC нет |
| slop-detector | PASS | 0 клише; over-long 5; Flesch RU 77.3 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | Encar на корейском + ярлык 무사고 «без аварий» → риск депозита за «кота в мешке» |
| Где решение | H2: переводчик+ID → 만원×10000 → схема X/W → CarHistory/Trust vs Diagnosis → красные флаги → чеклист |
| Первый результат | Вердикт ок/стоп/к подборщику + чеклист 8–10 пунктов до депозита |
| Термины «на пальцах» | 만원=10 000 вон; 무사고≈каркас; X/W; CarHistory; 엔카진단 vs Meetgo vs RU Trust |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary «encar на русском» в title/H1; H2 how-to; CTA catalog×2 + TG×1; 1 blog internal (AS09) |
| GEO / citability | 24/25 | Insight, таблица кодов, FAQ×6, чеклист, схема чтения лота |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 15/15 | concrete×5; pain/outcome видны; 0 AI-opening |
| Fact safety | 13/15 | Статы из research/Vinlid/CarHistory; часть не в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS; ~9k знаков; FAQ; без forms/pre |
| **Итого** | **88/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в meta/H1 |
| C02 | ✓ | Lead сразу про боль + вердикт до депозита |
| C03 | ✓ | Новичок читает Encar через переводчик |
| C04 | ✓ | 만원 / 무사고 / X/W / CarHistory / Diagnosis объяснены |
| O01 | ✓ | H2 = research outline |
| O02 | ✓ | Логичный поток до FAQ |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + blockquote, mode B |
| R01 | ✓ | Insight + схема + FAQ |
| R02 | ✓ | ~14.4% / 4 из 10 / ~2200 вон / 120 дней с оговорками |
| R03 | ✓ | Нет выдуманных «под ключ» сумм |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол: переводчик ≠ русский Encar; Trust ≠ Diagnosis |
| E02 | ✓ | «Делать / Не делать» в секциях |
| E03 | ✓ | CTA catalog×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты CarHistory, X/W, протокол |
| Ept02 | ✗ | Только 1 internal blog link (AS09); желательно 2–3 после publish соседних |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## QA FIX this run

1. Insight label `TL;DR / Быстрый инсайт` → `Короткий разбор` (human-voice ban).
2. Restored `scripts/excalibur_blog_link_verify.py` soft-pass (`catalog_ssl` / `site_ssl` + redact) — sanitizer wipe regression.
3. Restored insight TL;DR ban in `scripts/excalibur_blog_human_voice_gate.py`.
4. Writing-contract example updated: banned TL;DR labels → topical label.

## Gate

- score ≥ 80 → **88** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓ (soft catalog_ssl)  
- research-notes / utility / human-voice PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — директор может запускать cover \|\| schema (не publish из GEO QA).
