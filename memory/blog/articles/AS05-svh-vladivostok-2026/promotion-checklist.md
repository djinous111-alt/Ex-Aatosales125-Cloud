# Promotion checklist — AS05 svh-vladivostok-2026

Дата публикации: 2026-07-19  
Live URL: [REDACTED]/2026/07/19/svh-vladivostok-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (REST: post 3523 publish; featured 3524)
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
СВХ – не бесплатная парковка

• Закон: до 4 месяцев хранения
• Льгота склада: обычно 5–10 суток с выгрузки
• До депозита: 5 вопросов (льгота / ПРР / перестой / кто платит / слот)

Читать: [REDACTED]/2026/07/19/svh-vladivostok-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS05 ↔ AS08/AS09 — нет пересечения якорей/queries в тексте)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «свх владивосток» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS05-svh-vladivostok-2026 --site-base [REDACTED]` — links_applied=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (`--blog-dir memory/blog/articles`, без `--blog-path`).
- Site base в llms + interlink-suggestions redact → `[REDACTED]` перед коммитом.
