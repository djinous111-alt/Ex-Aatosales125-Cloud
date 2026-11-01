# Promotion checklist — AS12 jetour-t2-iz-kitaya-komplektatsii-lovushki-2026

Дата публикации: 2026-11-01  
Live URL: /2026/11/01/jetour-t2-iz-kitaya-komplektatsii-lovushki-2026/

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
Discovery на витрине ≠ железо в лоте

• РФ: Люкс/Престиж 7DCT AWD, Премиум 8AT AWD
• Китай Traveller: Exploration часто 1.5T FWD; Discovery/Traverse — 2.0T
• До депозита: мотор, КПП, привод, опции с фото, VIN

Читать: /2026/11/01/jetour-t2-iz-kitaya-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (corpus AS08/AS09/AS12; suggestions пустые)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «джетур т2 комплектации» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir … --site-base $PUBLIC_SITE_URL` — opportunities_found=0; report `memory/blog/interlink-suggestions.json` (site_base emptied for commit-safe).
- llms.txt / llms-full.txt: `--blog-dir memory/blog/articles --site-base "" --out-dir memory/blog` → relative `/blog/<slug>/` (нет `--blog-path` / `--relative-urls` в текущем CLI; known INC-20261101-1302).
- Publish: не запускался Indexer’ом.
