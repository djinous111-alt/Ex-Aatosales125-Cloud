# Article QA — B01 Chery Tiggo 8 Pro из Китая

**topic_id:** B01  
**slug:** chery-tiggo-8-pro-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-chery-tiggo-8-pro-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-30  
**verdict:** PASS  
**score:** 87

## Beginner-fit

- **Боль новичка:** боюсь перевести депозит за «тот самый» Tiggo 8 Pro, а приедет другая комплектация / мотор / машина без бумаг на вывоз.
- **Где решение:** H2 про ветку Plus/Pro/Pro Max → кВт до утиля → список опций → VIN/документы → маршрут до СВХ → чеклист 12 пунктов.
- **Первый результат:** до депозита собран чеклист из 12 пунктов; VIN/кВт/опции/маршрут сверены.
- **Термины «на пальцах»:** trim, кВт, VIN, C-DM/PHEV, ADAS/ACC/AEB, СВХ, СБКТС, ЭПТС.

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn: technical_topic без official docs URL (FP для авто-темы) |
| utility gate | PASS | action 22 / pain 2 / outcome 6; ol 24 / H2 7 / FAQ 6 / table 1 |
| human-voice | PASS | pain×2; outcome×5; warn exactly-5 lists (≥5 li в ol) |
| fact-check | PASS | 10 stats; unverified vs fact-bank — цифры из research-notes |
| link-verify | PASS | 2/2 HEAD 200 (каталог + Telegram) |
| html-linter | PASS | whitelist OK; TOC нет; insight без TL;DR |
| slop-detector | WARNING | 0 клише; 6 over-long; Flesch RU 77.2 |
| cannibalization | PASS | 0 issues |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary how-to в title/H1; H2 actionable; CTA каталог+Telegram |
| GEO / citability | 23/25 | Insight, таблица, схемы →, FAQ×6, чеклист 12 |
| CORE-EEAT lite | 19/20 | см. ниже |
| Human voice | 14/15 | PASS; warn по спискам ≥5 |
| Fact safety | 13/15 | кВт/naming из research; без статичных цен утиля |
| Contract HTML | 10/10 | Whitelist PASS, ~9202 chars, FAQ, CTA≤3 |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать chery tiggo 8 pro из китая» в meta/H1 |
| C02 | ✓ | Lead называет боль депозита без VIN/кВт |
| C03 | ✓ | Читатель: семья / новичок заказа из Китая |
| C04 | ✓ | Plus≠Pro naming, кВт CN≠RU, 180 дней объяснены |
| O01 | ✓ | H2 = action outline research |
| O02 | ✓ | Логичный порядок до депозита |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol + table + blockquote workflows, mode B |
| R01 | ✓ | Insight + схемы + FAQ |
| R02 | ✓ | 145/137 кВт, 117,68 кВт, 180 дней в research |
| R03 | ✓ | Нет статичных цен пошлин/утиля в ₽ |
| R04 | ✓ | FAQ — ответы-действия |
| E01 | ✓ | Угол «не платите, пока не сверили бумажки» |
| E02 | ✓ | Сделайте / Не делайте в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake first-person |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop cliches = 0 |
| Ept01 | ✓ | Риски naming, кВт, C-DM, 180 дней, карта физлица |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## QA fixes this run

1. Restored `pain_markers_ru` / `outcome_markers_ru` (+ mins) in `memory/brief/editorial-policy.json` after rebrand wipe (иначе utility всегда BLOCK).
2. Insight label: `Инсайт до депозита` (убран шаблон `TL;DR / Быстрый инсайт`).
3. Усилены pain/outcome/action маркеры; финальный CTA-список 4 пункта; Fact Check — «Редакция Авто-Сейлс».

## Blockers

- нет

## Next

cover || schema (Director parallel) — только после этого PASS.
