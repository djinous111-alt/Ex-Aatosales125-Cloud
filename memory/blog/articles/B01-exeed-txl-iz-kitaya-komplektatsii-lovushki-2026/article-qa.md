# Article QA — B01 Exeed TXL из Китая (recheck после Writer FIX)

**topic_id:** B01  
**slug:** exeed-txl-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-exeed-txl-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-31  
**verdict:** PASS  
**score:** 86  
**author_id:** avtosales-editorial → `shared/authors-registry.json` ✓  
**writer_fix_cycle:** 1 (recheck)

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn technical_topic FP (`ии` in комплектации); official docs 0 |
| fact-check | PASS | 5 stats; 1 verified / 4 unverified vs fact-bank |
| link-verify | PASS | 2/2 HEAD 200; CTA via env-expanded **temp copy**; committed HTML keeps `${CATALOG_URL}`/`${TELEGRAM_URL}` + allowlist pragma |
| html-linter | PASS | 0 errors; TOC в теле нет; whitelist OK |
| slop-detector | PASS | 0 клише; 2 over-long; Flesch RU 81.4 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | action_markers **17** (≥8); pain 9 / outcome 5; water 0 |
| human-voice gate | PASS | `human-voice-report.json`; warn Fact Check template + exactly-5 lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 actionable; CTA×3; нет 2–3 blog internal |
| GEO / citability | 23/25 | Insight `Инсайт до депозита` + таблица CN/РФ + FAQ×6 |
| CORE-EEAT lite | 18/20 | см. таблицу ниже |
| Human voice | 14/15 | Gate PASS; 0 AI-openers; soft warn template Fact Check |
| Fact safety | 12/15 | Факты в research-notes; часть stats unverified в fact-bank |
| Contract HTML | 10/10 | Whitelist PASS, FAQ, CTA placeholders, utility markers OK |
| **Итого** | **86/100** | ≥80 после FIX action_markers + insight label |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «как выбрать exeed txl из китая» в meta/H1 |
| C02 | ✓ | Lead — боль депозита / не та комплектация |
| C03 | ✓ | Новичок: заказ TXL из Китая до предоплаты |
| C04 | ✓ | Prestige/Flagship vs Lingyun 300T/400T, 两驱/四驱 объяснены |
| O01 | ✓ | H2 = how-to до депозита |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ ×6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Insight + схема/таблица + FAQ |
| R02 | ✓ | Мощность/КПП из research (КОЛЕСА / exeed.ru) |
| R03 | ✓ | Нет калькулятора пошлин; «цифры плавают» |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» + CN vs РФ нейминг |
| E02 | ✓ | «Сделайте / Не делайте» + императивы в теле (≥8 markers) |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 (placeholders) |
| Exp01 | ✓ | Mode B, без fake «я купил» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: прошивка, сервис, смета без фиксированных сумм |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

- **Боль новичка:** депозит за «TXL 2.0» без сверки Prestige/Flagship vs Lingyun / привода / прошивки — названа в lead.
- **Решение:** H2 «Сравните комплектации…» → VIN/таблички → смета по строкам → папка «до депозита» / stop-go.
- **Первый результат до FAQ:** чеклист stop/go + папка документов до перевода денег.
- **Термины «на пальцах»:** 7DCT, 8AT, 两驱/四驱, СВХ, СБКТС, ЭПТС, Exeed Connect.
- **Verdict beginner-fit:** PASS

## CTA handling

- Writer оставил `${CATALOG_URL}` ×2 + `${TELEGRAM_URL}` ×1 + `<!-- pragma: allowlist secret -->`.
- GEO QA recheck: **temp copy** `/tmp/...` с подстановкой из env `CATALOG_URL`/`TELEGRAM_URL` только для `link-verify`; `article.html` **не** менялся.
- link-verify.json: URL санитизированы; verdict pass 2/2.

## Link verify

- total: 2, failed: 0
- hosts: `avto-sales125.ru`, `t.me`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 2
- Flesch RU: 81.4

## Schema ready

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (чеклисты) — cover/schema может стартовать после этого PASS (Директор).

## Blockers

нет

## Soft / non-blocking

1. **Ept02:** 2–3 internal links на соседние посты после LIVE URL (Indexer).
2. **human-voice warn:** варьировать Fact Check wording; один из двух списков ≠ ровно 5 пунктов.
3. **fact-check soft:** дописать ключевые цифры мощности в fact-bank.

## Gate checklist

- score ≥ 80 → **86** ✓  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓ (action_markers 17)  
- human-voice-report.json PASS ✓  
- beginner-fit PASS ✓  

**Итог:** **PASS** — cover \|\| schema можно запускать Директору. Publish не из GEO QA.
