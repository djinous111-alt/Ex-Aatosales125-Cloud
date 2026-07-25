# Promotion checklist — B01 svh-vladivostok-kak-ne-pereplatit-2026

Дата публикации: 2026-07-25 (pending WP publish)  
Live URL: (pending publish permalink)

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
«Машина в порту» ≠ СВХ бесплатно

• Льгота склада обычно 5–10 суток, не 4 месяца по ТК ЕАЭС
• До судна: название СВХ, аванс ФТС, пакет документов
• День 1: дата старта льготы и ступени тарифа письменно

Читать: (pending Live URL)
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (B01 vs AS08/AS09 — нет пересечения якорей)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «свх владивосток» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-svh-vladivostok-kak-ne-pereplatit-2026 --site-base $PUBLIC_SITE_URL` — 0 links applied.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles; CLI: `--blog-dir`, без `--blog-path` / `--url-mode`).
- Publish: Live URL и дату в шапке обновит excalibur-blog-publish.
