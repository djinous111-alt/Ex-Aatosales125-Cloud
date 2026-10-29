# Promotion checklist — B01 toyota-rav4-iz-yaponii-komplektatsii-lovushki-2026

Дата публикации: 2026-10-29 (pending publish)  
Live URL: /blog/toyota-rav4-iz-yaponii-komplektatsii-lovushki-2026/

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
RAV4 из Японии: сначала код кузова, потом ставка

• «Престиж» на аукционе ≠ грейд X/G/Adventure
• Hybrid и ~1986 см³ с 09.08.2023 — стоп для РФ до сверки
• Чек-лист 12 пунктов до любой ставки

Читать: /blog/toyota-rav4-iz-yaponii-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (corpus=3; suggestions=[])

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «тойота рав 4 комплектации» (ручная проверка / Wordstat)

## Notes

- Indexer: `python3 scripts/excalibur_blog_interlinker.py --apply --article-dir memory/blog/articles/B01-toyota-rav4-iz-yaponii-komplektatsii-lovushki-2026 --site-base $PUBLIC_SITE_URL` → 0 links.
- llms: `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL --out-dir memory/blog` (без `--blog-path`; CLI его не принимает).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (3 articles indexed, B01 included).
- Publish: не запускался (зона Indexer).
