# Article QA — B01 Exeed TXL из Китая

**topic_id:** B01  
**slug:** exeed-txl-iz-kitaya-komplektatsii-lovushki-2026  
**article_dir:** memory/blog/articles/B01-exeed-txl-iz-kitaya-komplektatsii-lovushki-2026  
**date:** 2026-10-31  
**verdict:** FAIL  
**score:** 78  
**author_id:** avtosales-editorial → `shared/authors-registry.json` ✓

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | warn technical_topic FP (`ии` in комплектации) |
| fact-check | PASS | 5 stats; 1 verified / 4 unverified vs fact-bank |
| link-verify | PASS | 2/2 HEAD 200 (`avto-sales125.ru`, `t.me`); CTA via env-expanded **temp copy**; committed HTML keeps `${CATALOG_URL}`/`${TELEGRAM_URL}` + allowlist pragma |
| html-linter | PASS | 0 errors; TOC в теле нет |
| slop-detector | PASS | 0 клише; 2 over-long; Flesch RU 82.6 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | **BLOCK** | action_markers **2 &lt; 8**; pain 9 / outcome 4 после restore policy lists |
| human-voice gate | PASS | `human-voice-report.json`; warn Fact Check template + exactly-5 lists |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 actionable; CTA×3; нет 2–3 blog internal |
| GEO / citability | 22/25 | Insight blockquote + таблица CN/РФ + FAQ×6; insight label всё ещё `TL;DR / Быстрый инсайт` (skill prefers без ярлыка) |
| CORE-EEAT lite | 18/20 | см. таблицу ниже |
| Human voice | 14/15 | Gate PASS; 0 AI-openers; soft warn template Fact Check |
| Fact safety | 12/15 | Факты в research-notes; часть stats unverified в fact-bank |
| Contract HTML | 8/10 | Whitelist PASS, FAQ, CTA placeholders; **utility action markers FAIL** |
| **Итого** | **78/100** | &lt;80 из‑за utility BLOCK |

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
| E02 | ✓ | «Делать / Не делать» в секциях (но маркеры utility ждут императив «сделайте/не делайте») |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 (placeholders) |
| Exp01 | ✓ | Mode B, без fake «я купил» |
| Exp02 | ✓ | Тон Авто-Сейлс / Владивосток |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Лимиты: прошивка, сервис, смета без фиксированных сумм |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Beginner-fit

- **Боль новичка:** депозит за «TXL 2.0» без сверки Prestige/Flagship vs Lingyun / привода / прошивки — названа в lead и в H2 «Боль:».
- **Решение:** таблица комплектаций → VIN/таблички → смета по строкам → папка «до депозита» / stop-go.
- **Первый результат до FAQ:** чеклист stop/go + папка документов до перевода денег.
- **Термины «на пальцах»:** 7DCT, 8AT, 两驱/四驱, СВХ, СБКТС, ЭПТС, Exeed Connect.
- **Verdict beginner-fit:** PASS (контент ок; блокирует только utility action-marker count).

## CTA handling

- Writer оставил `${CATALOG_URL}` ×2 + `${TELEGRAM_URL}` ×1 + `<!-- pragma: allowlist secret -->`.
- GEO QA: **temp copy** `/tmp/...` с подстановкой из env `CATALOG_URL`/`TELEGRAM_URL` только для `link-verify`; `article.html` **не** менялся (placeholders сохранены → secret-scan safe).
- link-verify.json: URL санитизированы до host/`[REDACTED]`; verdict pass 2/2.

## Link verify

- total: 2, failed: 0
- hosts: `avto-sales125.ru`, `t.me`
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 2
- Flesch RU: 82.6

## Schema ready

BlogPosting: pending | FAQPage: yes (6) | HowTo: yes (чеклисты) — cover/schema **не** стартовать до QA PASS.

## Blockers

1. **utility gate BLOCK:** `action_markers=2 < 8` (есть только «ориентир» + «чеклист»).
2. Gate overall FAIL → cover/schema/publish **запрещены**.

## FIX → Writer (цикл 1)

1. **Action markers (≥8)** из `recommendation_markers_ru`: заменить ярлыки «Делать:/Не делать:» на императивы **«Сделайте:/Не делайте:»** и/или добавить в тело ≥6 вхождений из: `проверьте`, `избегайте`, `используйте`, `шаг `, `сделайте`, `не делайте` (без раздувания char_count за 9500).
2. **Insight label (skill):** заменить `<b>TL;DR / Быстрый инсайт:</b>` на `<b>Инсайт до депозита:</b>` (html-linter сейчас PASS, но skill запрещает ярлык TL;DR / «Быстрый инсайт»).
3. Не трогать CTA placeholders `${CATALOG_URL}` / `${TELEGRAM_URL}` + allowlist pragma.
4. После правок — повтор GEO QA (utility + human-voice + article-qa).

## FIX (non-blocking / optional)

1. **Ept02:** 2–3 internal links на соседние посты после LIVE URL.
2. **human-voice warn:** варьировать Fact Check wording; один из двух списков ≠ ровно 5 пунктов.
3. **fact-check soft:** дописать ключевые цифры мощности в fact-bank.

## Gate checklist

- score ≥ 80 → **78** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✗ (**BLOCK** action markers)  
- human-voice-report.json PASS ✓  
- beginner-fit PASS ✓  

**Итог:** **FAIL** — вернуть Writer по FIX; cover \|\| schema не запускать.
