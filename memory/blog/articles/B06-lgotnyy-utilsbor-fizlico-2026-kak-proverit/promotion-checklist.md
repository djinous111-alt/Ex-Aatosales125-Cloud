# Promotion checklist — B06 lgotnyy-utilsbor-fizlico-2026-kak-proverit

Дата публикации: 2026-07-25  
Live URL: [REDACTED]/2026/07/25/lgotnyy-utilsbor-fizlico-2026-kak-proverit/

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
Льгота? Сначала чеклист

• «Я физлицо» ≠ автоматический льготный утильсбор
• Сверяйте мощность в кВт, гибрид/электро и лимит 1 авто/год
• До депозита — 10 галочек, иначе риск коммерческого тарифа

Читать: [REDACTED]/2026/07/25/lgotnyy-utilsbor-fizlico-2026-kak-proverit/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: opportunities_found=0 (AS08/AS09 ↔ B06 — нет якорей/overlap)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «льготный утильсбор» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B06-… --site-base <PUBLIC_SITE_URL>` — links_applied=0.
- llms.txt / llms-full.txt: relative `/blog/<slug>/` URLs (secret-scan safe; same-origin when hosted on site).
- Publish: PASS — post_id=3742; featured=3743; inline=3744/3745/3746; schema_meta=ok; live HEAD 200.
