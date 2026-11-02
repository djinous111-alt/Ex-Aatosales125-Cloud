# Promotion checklist — AS02 encar-na-russkom-kak-chitat

Дата публикации: 2026-11-03  
Live URL: /blog/encar-na-russkom-kak-chitat/ (после WP publish)

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
Переводчик сказал «без аварий»? На схеме может быть W

• Официальной русской версии encar.com нет — перевод браузера на оригинале
• 무사고 = каркас, не идеальный кузов; манвон × 10 000
• VIN/лист до депозита; чужой сайт из выдачи — не Encar

Читать: /blog/encar-na-russkom-kak-chitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: AS02 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`, якорь «Trust Encar»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «encar на русском» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir … --site-base ${PUBLIC_SITE_URL}` — 1 link applied (AS02→AS09).
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir` (без `--blog-path`; open INC-20261103-0003-director-llms-blog-path).
- Report: `interlink-report.json` в article_dir.
