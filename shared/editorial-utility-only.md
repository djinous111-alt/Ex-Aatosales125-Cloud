# Excalibur BLOG — только полезные статьи (utility-only)

Канон: `memory/brief/editorial-policy.json` · ниша: `memory/brief/site-brief.md` (**AVTO SALES**)

## Принцип

**Публикуем только то, что даёт действие.** После прочтения читатель знает *что сделать до депозита/ставки/оплаты* — не «вообще про модель».

Фильтр канала: **покупатель-first**. Статья полезна человеку без опыта импорта авто из Японии/Кореи/Китая. Если угол только для профи-перекупа без чеклиста для обычного клиента — тему не берём.

| ✅ Берём | ❌ Не берём |
|---------|------------|
| How-to выбора комплектации / двигателя | Новости рынка без действия |
| Чеклист до депозита (Encar, Carhistory, лист) | Мнение без инструкции |
| Comparison стран/кузовов/версий с таблицей | «Что такое X» без шагов |
| Troubleshooting ловушек растаможки/логистики | Trend-посты, мотивация |
| Workflow: подбор → проверка → ставка → СВХ | Корпоративная вода |
| Утильсбор/документы 2026 как чеклист (без выдуманных сумм) | Cursor/n8n/Make/AI-агенты, чужой SEO/AI template |

## Gate 1 — тема (`blog-topics.md`)

```bash
python3 scripts/excalibur_blog_utility_gate.py --topic-id B01
```

**Blocker `UTILITY TOPIC BLOCKER`** — тему не пускаем.

Обязательные поля:

- `search_intent`: `how_to` | `checklist` | `comparison` | `troubleshooting` | `workflow` | `parent_guide`
- `article_mode`: **B**
- `h1` / `primary_query`: глагол действия («как…», «чек-лист…»)
- понятный первый результат для покупателя до оплаты

## Gate 2 — research

В `research-notes.md`:

- `utility_verdict: PASS`
- `research_date` = `today_iso`
- source table: в каждой строке ячейка вида `accessed_at: YYYY-MM-DD` (**двоеточие обязательно** для gate)
- ≥5 вхождений `accessed_at:`
- `pain_solution_map`: в каждой строке слова pain|solution|result|боль|решение|результат (удобно префиксы `pain:` / `solution:` / `result:`)
- литерал `prefer_sources_after` даты из freshness window
- `github_evidence` — секция нужна; для **авто-тем** GitHub ≥3 не требуется (technical_topic ловит только реальный tech/automation; заголовок `github_evidence` сам по себе не должен включать tech-режим)
- `reader_pain` / `reader_outcome` / `success_criteria` / `voice_angle` / `reader_story` / `surprising_fact`
- `action_outline`: 5–9 шагов

```bash
python3 scripts/excalibur_blog_research_notes_gate.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  -o research-notes-gate.json
```

## Gate 3 — writer

Контракт: `shared/excalibur-article-writing-contract.md`

- Каждый H2 = подзадача + **Делать / Не делать**
- Минимум **5** шагов ИЛИ чеклист 10+
- Таблица/workflow до FAQ
- Lead = боль → H2 = решения из `pain_solution_map` → до FAQ критерий результата
- CTA ≤ 3 (каталог + Telegram), без форм на странице

## Gate 4 — GEO QA

```bash
python3 scripts/excalibur_blog_utility_gate.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Плюс human-voice, link-verify, slop. Cover/schema только после PASS.

## Чеклист редактора

1. Island test по H2  
2. So what test по абзацу  
3. Lead: боль + ответ + результат  
4. Нет режима A  
5. Цифры только из research / fact-bank  
6. CTA ≤ 3  

## Связанные файлы

- `memory/brief/site-brief.md`
- `shared/wp-slug-denylist.json`
- `skills/excalibur/references/article-archetypes.md`
- `skills/excalibur/references/ai-slop-blocklist.md`
- `shared/quality-blog.md`
