# Promotion checklist — B01 rastamozhka-avto-iz-kitaya-2026

Дата публикации: (pending publish)  
Live URL: https://avtosales125.ru/blog/rastamozhka-avto-iz-kitaya-2026/ // pragma: allowlist secret

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
Красивая цена из чата — а смета во Владивостоке?

• Сначала 5 параметров авто (год, объём, мощность, тип, физлицо)
• Три платежа государству ≠ «цена под ключ»
• «Растаможили» без ЭПТС — ещё рано на учёт

Читать: https://avtosales125.ru/blog/rastamozhka-avto-iz-kitaya-2026/ // pragma: allowlist secret
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (корпус 3 статьи; релевантных якорей не найдено)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как растаможить авто из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir memory/blog/articles/B01-rastamozhka-avto-iz-kitaya-2026 --site-base $PUBLIC_SITE_URL` — 0 links applied; report `memory/blog/interlink-suggestions.json`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-name «Авто-Сейлс»; B01 первая в индексе).
- CLI note: `excalibur_blog_llms_generator.py` принимает `--blog-dir`, не `--blog-path` (первый вызов с `--blog-path /` упал → retry без флага).
