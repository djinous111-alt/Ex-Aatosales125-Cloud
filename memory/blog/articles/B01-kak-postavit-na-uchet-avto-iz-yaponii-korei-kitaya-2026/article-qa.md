# Article QA — B01

**topic_id:** B01  
**slug:** kak-postavit-na-uchet-avto-iz-yaponii-korei-kitaya-2026  
**article_dir:** memory/blog/articles/B01-kak-postavit-na-uchet-avto-iz-yaponii-korei-kitaya-2026  
**date:** 2026-10-06  
**author_id:** avtosales-editorial  
**verdict:** PASS  
**score:** 87

## Pain / solution / beginner-fit

| Вопрос | Ответ |
|--------|--------|
| Боль новичка | Едет в МРЭО после «ЭПТС готов», статус «незавершённый» → отказ; путает ОСАГО/ЭРА с пакетом учёта |
| Где решение | H2: статус ЭПТС → чек-лист документов → Япония/Корея/Китай → Госуслуги/осмотр → ОСАГО/ЭРА/10 дней → финальный чек |
| Первый результат | Папка «всё зелёное» + СТС и номера; критерий успеха до FAQ |
| Термины «на пальцах» | ЭПТС, СБКТС, МРЭО, ТПО/ДТ, УВЭОС/ЭРА-ГЛОНАСС объяснены при первом появлении |
| Beginner-fit | PASS — чек-лист для частника после растаможки, без jargon-only тона |

## Scripts

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | research_date=2026-10-06; technical_topic true |
| fact-check | PASS | 11 stats; 2 verified / 9 unverified vs thin fact-bank — даты/пошлины в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram); после FIX CTA |
| html-linter | PASS | whitelist OK; TOC в теле нет |
| slop-detector | PASS | 0 клише; 4 over-long (таблица/схема); Flesch RU 56.0 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | PASS | article gate PASS; action/pain/outcome markers OK |
| human-voice gate | PASS | warnings: rhythm variance 0.33; exactly-5-step lists×3 — non-blocking |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 17/20 | Primary в title/H1; H2 how-to; CTA×3; нет 2–3 blog internal |
| GEO / citability | 23/25 | Инсайт, схема, таблица JP/KR/CN, FAQ×7, чеклисты |
| CORE-EEAT lite | 14/15 | 19/20 (см. ниже) |
| Human voice | 14/15 | Gate PASS; rhythm/list warnings |
| Fact safety | 12/15 | Факты в research-notes; fact-bank неполный |
| Contract HTML | 10/10 | Whitelist PASS; ~9436 chars text; FAQ; CTA; без форм |
| **Итого** | **87/100** | |

## CORE-EEAT lite: 19/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary «постановка на учет авто из японии» в title/H1 |
| C02 | ✓ | Lead: сценарий отказа + прямой ответ «что проверить до записи» |
| C03 | ✓ | Читатель: частник после растаможки JP/KR/CN |
| C04 | ✓ | ЭПТС / СБКТС / МРЭО объяснены |
| O01 | ✓ | H2 = research action outline |
| O02 | ✓ | Логичный outline до FAQ |
| O03 | ✓ | FAQ 7 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Инсайт, схема, финальный чек, FAQ |
| R02 | ✓ | ОСАГО 01.03.2025; ЭРА до 31.12.2027; пошлины — в research-notes |
| R03 | ✓ | Пошлины как ориентир; без выдуманных % |
| R04 | ✓ | FAQ: ответ в 1-м предложении |
| E01 | ✓ | Угол «после ЭПТС / статус действующий», не калькулятор ввоза |
| E02 | ✓ | «Делать / Не делать» в H2 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B, без fake «я сделал» |
| Exp02 | ✓ | Тон Авто-Сейлс / research voice_angle |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Отказы, правки ЭПТС, срок 10 дней, мифы ОСАГО/ЭРА |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total unique: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 4 (артефакт таблицы/схемы)
- Flesch RU: 56.0

## Schema ready

BlogPosting: yes | FAQPage: yes (7) | HowTo: yes (чеклисты) | Review: no | E-E-A-T SameAs Author: pending (cover/schema вне зоны QA)

## Blockers

- нет

## FIX cycle (QA)

1. **link-verify FAIL:** в `article.html` все CTA были `href="[REDACTED]"` (литерал) → 404 на internal_relative. Восстановил `CATALOG_URL`×2 + `TELEGRAM_URL`×1 из runtime env. Повтор: PASS.
2. **Insight label:** убран шаблонный ярлык `TL;DR / Быстрый инсайт` → `Коротко:` (контракт GEO QA skill). Human-voice остаётся PASS.

## FIX (non-blocking / optional)

1. **Ept02:** после публикации AS/B-постов — 2–3 internal blog links с `anchor_variants`.
2. **fact-check soft:** дописать пошлины/даты ОСАГО/ЭРА в fact-bank.
3. **human-voice warnings:** разнообразить длину абзацев / размер списков.

## Gate

- score ≥ 80 → **87** ✓  
- CORE-EEAT ≥ 16/20 → **19/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human-voice gate PASS ✓  
- beginner-fit PASS ✓  

**Итог:** PASS — можно cover || schema.
