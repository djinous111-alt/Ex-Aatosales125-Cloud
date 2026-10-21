# Promotion checklist — B01 kia-carnival-iz-korei-komplektatsii-lovushki-2026

Дата публикации: (после publish)  
Live URL: /blog/kia-carnival-iz-korei-komplektatsii-lovushki-2026/

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
Carnival 2026 на дизеле? Сверь мотор до депозита

• Новый MY2026 в Корее — только 3.5 и гибрид 1.6; дизель 2.2 живёт в б/у на Encar
• До денег: год, топливо, trim, 7/9 мест, VIN + Carhistory
• Prestige / Signature / X-Line — про семью, не про «самое дорогое слово»

Читать: /blog/kia-carnival-iz-korei-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (corpus AS08/AS09/B01; exact keyword match, targets=[])

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «киа карнивал из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir memory/blog/articles/B01-kia-carnival-iz-korei-komplektatsii-lovushki-2026 --site-base $PUBLIC_SITE_URL` → interlink_count=0, targets=[].
- llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (без `--blog-path`; doctor/skill stale).
- llms.txt / llms-full.txt обновлены в `memory/blog/`; B01 в индексе.
- Publish: не запускался (зона Indexer).
