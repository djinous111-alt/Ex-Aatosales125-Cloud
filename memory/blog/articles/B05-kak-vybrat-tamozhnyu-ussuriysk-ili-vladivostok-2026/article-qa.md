# Article QA — B05 (recheck #2)

**topic_id:** B05  
**slug:** kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026  
**article_dir:** memory/blog/articles/B05-kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026  
**date:** 2026-10-02  
**verdict:** FAIL  
**score:** 78  
**human_voice:** BLOCK  
**utility:** PASS  
**fix_cycle:** 2 (вернуть writer — Fact Check hard markers)

## Scripts (full re-run from scratch)

| Script | Verdict | Notes |
|--------|---------|-------|
| research-notes-gate | PASS | `research_date=2026-10-02`; technical_topic=false |
| fact-check | PASS | 11 stats; 1 verified in fact-bank; 10 unverified — в research-notes |
| link-verify | PASS | 2/2 OK (каталог + Telegram CTA) |
| html-linter | PASS | whitelist OK; TOC нет; pre/code нет |
| slop-detector | PASS | 0 клише; 3 over-long; Flesch RU 56.4 |
| cannibalization | PASS | 0 issues (`--blog-dir memory/blog/articles`) |
| utility gate | **PASS** | action_markers=29; pain=6; outcome=6 (после fixer+writer) |
| human-voice-gate | **BLOCK** | Fact Check Box missing «Материал проверен»; WARN: 3× exactly-5 lists |

## Beginner-fit

**PASS.** Статья для новичка до депозита.

- Боль новичка: не понимает, чем Уссурийск отличается от Владивостока, и можно ли оформляться «не там, где живёшь», пока брокер торопит депозит/перегон.
- Решение: H2 сравнение маршрута → зона 178н → чеклист до оплаты → ошибки → пакет на вызов → 10 пунктов.
- Первый результат до FAQ: таблица «страна/доставка → прибытие → зона → пост/транзит»; депозит и перегон не оплачены.
- Термины «на пальцах»: ПТД, СВХ, КТС, приказ 178н, код ЦЭД 10720020.

## Pain / solution map (editorial)

| Боль | Где в тексте | Решение |
|------|--------------|---------|
| Выбор поста по чату про очереди | Lead + insight | Маршрут + 178н до депозита |
| «Какой город лучше» | H2 сравнение + таблица | Лучше тот, куда приехала машина и где зона |
| Оплата перегона ~98 км | H2 критерии / ошибки | Стоп-правило без сверки зоны |
| Вызов на пост / паника | H2 пакет | Пакет документов; транзит вместо билета «на всякий» |

## Scores

| Блок | Балл | Комментарий |
|------|------|-------------|
| SEO structure | 16/20 | Primary в title/H1; H2 action; CTA×3; нет 2–3 blog internal |
| GEO / citability | 22/25 | Insight, схема, таблица, FAQ×6, чеклисты |
| CORE-EEAT lite | 14/15 | 18/20 |
| Human voice | 5/15 | **BLOCK**: нет «Материал проверен» + нет name_ru реестра |
| Fact safety | 12/15 | Цифры в research-notes; мало в fact-bank |
| Contract HTML | 9/10 | Whitelist + utility PASS |
| **Итого** | **78/100** | ниже порога 80 из-за human_voice BLOCK |

## CORE-EEAT lite: 18/20

| ID | Result | Comment |
|----|--------|---------|
| C01 | ✓ | Primary в title/H1 |
| C02 | ✓ | Lead: пост по маршруту и 178н |
| C03 | ✓ | Новичок до депозита |
| C04 | ✓ | ПТД / СВХ / КТС / 178н объяснены |
| O01 | ✓ | H2 = comparison → 178н → критерии → ошибки → пакет → чеклист |
| O02 | ✓ | Логичный outline |
| O03 | ✓ | FAQ 6 |
| O04 | ✓ | ol/ul + таблица + чеклисты, mode B |
| R01 | ✓ | Insight + схема + FAQ |
| R02 | ✓ | Объёмы I пол. 2026, код 10720020, 178н |
| R03 | ✓ | Нет фейковых «пошлин дешевле» |
| R04 | ✓ | FAQ отвечает в 1-м предложении |
| E01 | ✓ | Угол «до депозита» |
| E02 | ✓ | «Сделайте / Не делайте» + action markers 29 |
| E03 | ✓ | CTA: каталог×2 + Telegram×1 |
| Exp01 | ✓ | Mode B |
| Exp02 | ✓ | Тон Авто-Сейлс |
| Exp03 | ✓ | Slop hits = 0 |
| Ept01 | ✓ | Оговорки по 178н и коду |
| Ept02 | ✗ | Нет 2–3 внутренних ссылок на другие посты блога |

**Target:** ≥16/20 ✓ (18/20) · veto (R03 / Exp01 / slop≥2): нет

## Link verify

- total: 2, failed: 0
- see `link-verify.json`

## AI-slop scan

- cliches: 0
- over-long: 3
- Flesch RU: 56.4

## Schema ready (после PASS)

BlogPosting: yes | FAQPage: yes (6) | HowTo: yes | Review: no  
**Не запускать cover/schema** пока verdict ≠ PASS.

## Blockers

1. **Human voice BLOCK** — Fact Check box перед FAQ заменён на «Проверка редакции» / «команда Авто-Сейлс». Gate требует:
   - `<blockquote>` с точной фразой **«Материал проверен»**;
   - имя из registry: **«Редакция Авто-Сейлс»** (`author_id=avtosales-editorial`).

## FIX для writer (обязательно)

1. Вернуть Fact Check Box **перед** `<h2>Частые вопросы</h2>` с обязательными маркерами:
   ```html
   <blockquote>
     <b>Материал проверен:</b> Редакция Авто-Сейлс (эксперты по авто под заказ из Японии, Кореи и Китая, Владивосток).<br>
     <b>База фактов на 2026-10-02:</b> загрузка постов – Newsvl, UssurMedia, TKS; зоны – приказ Минфина № 178н; код ЦЭД 10720020 – Альта-Софт (с 15.07.2026). Кластеры Wordstat – съём 2026-10-02. Платежи – в каталоге под лот.
   </blockquote>
   ```
2. **Не** убирать «Материал проверен» ради soft-warn про template. Soft-warn срабатывает только если в том же blockquote есть и «материал проверен», и «достоверность данных». Варьируйте вторую строку (как «База фактов…»), opener не трогайте.
3. Не трогать cover/schema; после правки — повтор GEO QA.

## FIX soft (не блокируют сами по себе)

1. Human voice WARN: 3 списка ровно на 5 пунктов — сделайте один на 4 или 6+ (часть уже 6 в «Что дальше»).
2. Ept02: 2–3 internal blog links (Indexer может закрыть позже).
3. Fact-bank: дописать ключевые цифры B05 для verified.

## Gate checklist

- score ≥ 80 → **78** ✗  
- CORE-EEAT ≥ 16/20 → **18/20** ✓  
- link-verify pass ✓  
- research-notes-gate PASS ✓  
- utility gate PASS ✓  
- human voice PASS ✗  
- beginner-fit PASS ✓  

**Итог:** FAIL — cover || schema **не** запускать. Writer: восстановить Fact Check hard markers → повтор GEO QA.
