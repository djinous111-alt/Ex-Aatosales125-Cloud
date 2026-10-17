# Article QA — B01 (re-run after FIX cycle 1)

**topic_id:** B01  
**slug:** vremennaya-registratsiya-vladivostok-rastamozhka-avto-2026  
**article_dir:** memory/blog/articles/B01-vremennaya-registratsiya-vladivostok-rastamozhka-avto-2026  
**date:** 2026-10-17  
**re_run:** after writer FIX cycle 1 (CTA href)  
**verdict:** PASS  
**score:** 91  
**char_count:** 9286  

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date 2026-10-17; source_table OK; pain/outcome/criteria OK |
| fact-check | PASS | 5 stats; verified 3; unverified 2 (27.02.2025 / МВД № 553 — в research-notes, не в fact-bank) |
| link-verify | **PASS** | unique external=2; failed_count=0; CATALOG_URL + TELEGRAM_URL → HTTP 200 |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 4 over-long; Flesch RU 50.5 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles` → cannibalization-report.json) |
| utility gate | PASS | action_markers 39; pain 5; outcome 14; FAQ×7; table×1 |
| human-voice gate | PASS | warning: 2× exactly-5-step lists (не блокирует) |

## Beginner-fit / pain→solution

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Иногородний боится, что «прописка во Владивостоке» — развод / без неё не оформят, и рискует купить фиктивный адрес (lead: Иван из Казани) |
| Где решение | H2: зачем адрес в ДФО → три пути (таблица) → документы → шаги Госуслуги → анти-фрод → чеклист до депозита |
| Первый результат | Чеклист из 7 вопросов компании до перевода денег; критерий «готов к оплате / пауза» до FAQ |
| Термины «на пальцах» | ДФО, регистрация по месту пребывания vs постоянная, СВХ, ETA, ЭПТС, фиктивная регистрация, таможенный транзит |

**beginner-fit:** PASS

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 18/20 | Primary в H1/meta OK; CTA live; −2 нет 2–3 internal blog links |
| GEO / citability | 23/25 | Коротко-блок, схема выбора, таблица путей, FAQ×7, чеклисты |
| CORE-EEAT lite | 15/15 | 19/20 (E03 CTA clickable; Ept02 soft) |
| Human voice | 14/15 | human-voice PASS; soft warn 5-step lists |
| Fact safety | 12/15 | 2 unverified vs fact-bank (есть в research-notes) |
| Contract HTML | 9/10 | whitelist PASS; объём ~9.3k; CTA env URLs OK |
| **Итого** | **91/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «временная регистрация…растаможки» в title/H1 |
| C02 | ✓ | Lead — боль Ивана + три пути + чеклист |
| C03 | ✓ | Читатель: иногородний, депозит, Владивосток |
| C04 | ✓ | ДФО / пребывание / транзит / СВХ объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логика: зачем → пути → документы → шаги → фрод → чеклист → дальше → FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Коротко-блок + схема + FAQ |
| R02 | ✓ | Минфин 178н / МВД 553 / дела о фиктивной регистрации в notes |
| R03 | ✓ | Нет цен лотов/% гарантий |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + анти-фрод |
| E02 | ✓ | «Делайте / Не делайте» в секциях |
| E03 | ✓ | CTA×3 кликабельны: CATALOG_URL×2 + TELEGRAM_URL×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Красная линия фиктивных адресов, план B |
| Ept02 | ✗ | Нет 2–3 internal blog links (только каталог/Telegram) |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет · hard veto: нет

## Re-run notes

- Предыдущий verdict FIX (score 72): литерал `href="[REDACTED]"` → link-verify FAIL.
- Writer FIX cycle 1: заменил 3 CTA на CATALOG_URL×2 + TELEGRAM_URL×1; lead/H2/FAQ не трогал.
- Re-QA: все 8 gates PASS; link-verify failed_count=0.

## Gate

cover \|\| schema — **разрешены** (GEO QA PASS).
