# Promotion checklist — B01 kia-mohave-iz-korei-komplektatsii-lovushki-2026

Дата публикации: YYYY-MM-DD (после WP publish)  
Live URL: /blog/kia-mohave-iz-korei-komplektatsii-lovushki-2026/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200) — AS08 soft suspension, AS09 Trust Encar/Carhistory, catalog, Telegram
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Gravity на Encar — ещё не максималка

• Сначала ветка Platinum или Masters, потом суффикс Gravity
• Места 5/6/7 фиксируйте до брони — салон после выкупа не переиграете
• Дизель ~257 л.с. выше льготы 160 л.с.; депозит только после VIN + сметы

Читать: /blog/kia-mohave-iz-korei-komplektatsii-lovushki-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Writer уже вставил AS08 + AS09; локальный interlinker `--apply`: 0 новых opportunities (corpus=3)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать киа мохаве из кореи» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-kia-mohave-… --site-base $PUBLIC_SITE_URL` → opportunities_found=0.
- llms.txt / llms-full.txt: `--blog-dir memory/blog/articles --out-dir memory/blog` (без `--blog-path`).
- Publish: не выполнялся (роль Indexer).
