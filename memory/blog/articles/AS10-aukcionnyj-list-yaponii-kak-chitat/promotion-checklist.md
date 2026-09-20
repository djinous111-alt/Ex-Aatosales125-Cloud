# Promotion checklist — AS10 aukcionnyj-list-yaponii-kak-chitat

Дата публикации: 2026-07-20  
Live URL: [REDACTED]/2026/07/20/aukcionnyj-list-yaponii-kak-chitat/

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
Красивая «4» без схемы — лотерея до депозита

• Читайте связку: общая оценка + салон A–E + схема W/X/XX/S/C + примечания
• Одна и та же «4.5» на TAA часто строже, чем на USS
• Депозит — только после решения одним предложением: беру / не беру / уточнение

Читать: [REDACTED]/2026/07/20/aukcionnyj-list-yaponii-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08/AS09 тематически далеки; keyword overlap не найден)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как читать аукционный лист японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir memory/blog/articles/AS10-aukcionnyj-list-yaponii-kak-chitat --site-base [REDACTED]` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (CLI: `--blog-dir`, без `--blog-path`).
- Publish: pending (Director запускает после Indexer).
