# Article QA — B01

**topic_id:** B01  
**slug:** sbkts-i-epts-2026-kak-oformit  
**article_dir:** memory/blog/articles/B01-sbkts-i-epts-2026-kak-oformit  
**date:** 2026-09-29  
**verdict:** FIX  
**score:** 76  
**fix_cycle:** 0 → return to Writer (max 2)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-09-29; sources/action/pain map OK |
| fact-check | PASS | 4 stats; verified 1 (2026); soft unverified: 2011 (ТР ТС), 2027 (FAQ caveat), «15 минут» |
| link-verify | FAIL | 2/4 fail: `dp.elpts.ru` HTTP 403; `pub.fsa.gov.ru/ral` SSL handshake timeout. Catalog OK. Telegram CTA OK (@avtosales125; scrubbed in reports) |
| html-linter | PASS | 0 errors; TOC нет; whitelist OK |
| slop-detector | WARNING | 0 клише; 6 over-long (таблица/чеклисты); Flesch RU 63.9 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | BLOCK | pain_markers=0&lt;2; outcome_markers=0&lt;3 — см. FIX + incident (policy без списков маркеров) |
| human-voice gate | BLOCK | pain_markers только `ошиб` (&lt;2); warn: 2× exactly-5-step lists |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|-------|
| Боль новичка | После таможни/СВХ путает СБКТС и ЭПТС, боится «серой» лаборатории и приезда в ГИБДД без пакета |
| Где решение | H2: отличие СБКТС/ЭПТС → порядок после таможни → чеклист → реестр ФСА → отказы → статус «действующий» → «что сделать сегодня» |
| Первый результат | Чеклист документов + 1–2 лаборатории в реестре + доступ в СЭП; критерий: «действующий» + выписка + ОСАГО |
| Термины «на пальцах» | СБКТС / ЭПТС / СЭП / ТД·ТПО / утильсбор / СТС vs ЭПТС — объяснены |
| Beginner-fit | PASS по смыслу (не профиль для разработчиков); lexical gates — FAIL |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 action; CTA каталог×2 + Telegram; мало internal blog |
| GEO / citability | 22/25 | Insight-blockquote, таблица, схема →, FAQ×6, чеклисты |
| CORE-EEAT lite | 19/20 | см. ниже |
| Human voice | 8/15 | Сюжет/история есть; lexical pain gate BLOCK |
| Fact safety | 12/15 | Fact-check PASS; 3 soft unverified; без выдуманных цен |
| Contract HTML | 10/10 | Linter PASS; char_count 8653; CTA OK |
| **Итого** | **76/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «сбктс и эптс» в meta/H1 |
| C02 | ✓ | Lead = боль + порядок без «в этой статье» |
| C03 | ✓ | Читатель: первый ввоз из Азии, СВХ Владивосток |
| C04 | ✓ | СБКТС/ЭПТС/СЭП объяснены |
| O01 | ✓ | H2 = action-outline research |
| O02 | ✓ | Логичный пайплайн |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + table + blockquote, mode B |
| R01 | ✓ | Короткий блок + схема + FAQ |
| R02 | ✓ | Источники в Fact Check + research-notes |
| R03 | ✓ | Цены не в статье → каталог |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «не по фото / сначала реестр» |
| E02 | ✓ | «Делать / Не делать» |
| E03 | ✓ | Telegram CTA @avtosales125 + каталог×2 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Лимиты: ЭРА-ГЛОНАСС не фиксируем; сроки ориентир |
| Ept02 | ✗ | Нет 2–3 internal blog links |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет  
**Gate blockers:** human-voice BLOCK, utility BLOCK, link-verify FAIL → overall FIX

## FIX list (Writer — cycle 1)

1. **Human-voice pain lexicon (blocker):** в lead и/или H2 про лабораторию явно назвать боль словами из gate-списка (≥2 разных): например `проблема`, `боль`, `сложно`, `долго`, `дорого` (сейчас в тексте только корень `ошиб`). Не размывать сюжет СВХ/«по фото».
2. **Telegram CTA:** уже OK (`@avtosales125`); в коммитимых отчётах URL scrubbed — не вставлять сырой TELEGRAM_URL.
3. **Списки (warning):** один из двух `<ol>` ровно на 5 пунктов сделать на 4 или 6 (human-voice warn `exactly_five_lists=2`).
4. **Utility outcome/pain (после Fixer policy):** после появления `pain_markers_ru` / `outcome_markers_ru` в `editorial-policy.json` — убедиться, что в теле есть ≥2 pain и ≥3 outcome маркера политики (часто пересекаются с human-voice: `результат`, `проверьте`, `соберите`, `выберите`, `чеклист`).
5. **Optional soft:** укоротить 1–2 самых длинных абзаца (slop over-long); internal blog links — после Indexer/URL других постов.

## FIX / durable (Director → Fixer, не Writer)

1. **`editorial-policy.json`:** добавить `pain_markers_ru`, `outcome_markers_ru` и при необходимости `min_pain_markers` / `min_outcome_markers` в `article_required_signals`. Сейчас списков нет → `pain_markers=0`, `outcome_markers=0` всегда → false BLOCK utility на любой статье.
2. **`excalibur_blog_link_verify.py`:** soft-fail / retry для официальных `pub.fsa.gov.ru`, `dp.elpts.ru` при 403/SSL timeout (как soft social), иначе B01 не сможет получить link-verify PASS при живых официальных ссылках.
3. **Typed Task:** Cloud API не принимает `excalibur-blog-geo-qa` — использован `generalPurpose` fallback (incident ниже).

## Gate checklist

- score ≥ 80 → **76** ✗  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass → ✗  
- research notes gate PASS → ✓  
- utility gate PASS → ✗  
- human voice gate PASS → ✗  
- beginner-fit PASS (смысл) → ✓ / lexical → ✗  

**Итог:** FIX — cover \|\| schema **не** запускать. Вернуть Writer + параллельно Fixer по policy/link-verify.
