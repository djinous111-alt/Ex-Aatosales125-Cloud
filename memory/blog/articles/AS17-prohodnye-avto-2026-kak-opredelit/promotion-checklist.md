# Promotion checklist — AS17 prohodnye-avto-2026-kak-opredelit

Дата публикации: 2026-07-21  
Live URL: /2026/07/21/prohodnye-avto-2026-kak-opredelit/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Год в объявлении ≠ месяц выпуска

• «Проходное» в 2026 — два слоя: возраст 3–5 лет + обычно ≤160 л.с.
• Считайте дату производства и запас на доставку до декларации
• До депозита: месяц выпуска, страна, мощность комплектации

Читать: /2026/07/21/prohodnye-avto-2026-kak-opredelit/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (в memory 3 статьи, пересечений якорей не найдено)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «какие авто проходные» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir ...` — 0 links (OK при малом корпусе).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir memory/blog/articles`, без `--blog-path`; git-safe relative `/blog/<slug>/`).
- Publish: PASS post_id=3577; Live URL /2026/07/21/prohodnye-avto-2026-kak-opredelit/; на deploy пересобрать llms с абсолютным site-base.
