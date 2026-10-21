# Promotion checklist — B01 kak-chitat-aukcionnyj-list-yaponiya-2026

Дата публикации: 2026-10-22  
Live URL: [REDACTED]/2026/10/12/kak-chitat-aukcionnyj-list-yaponiya-2026/  
WP post_id: 4086 · featured 4425 · inline 4430/4431/4432 · HEAD 200

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (HEAD 200; content+3 inline via wp-cli)
- [x] Schema meta `_excalibur_blog_schema_jsonld` на посте (len=11751; theme echo отдельно)
- [x] Проверить internal/CTA links (link-verify PASS pre-publish)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Смотришь только на 4.5 — и пропускаешь битый каркас?

• Лист читают по 5 зонам: ID → оценка → салон → схема → комментарий
• R/RA — про каркас, не про «подушки»
• XX на двери сам по себе R не даёт

Читать: [REDACTED]/2026/10/12/kak-chitat-aukcionnyj-list-yaponiya-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Auto-interlink run: 0 opportunities (AS08/AS09 — другие кластеры; suggestions пуст)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker --apply → 0 links applied; llms.txt + llms-full.txt regenerated (3 articles).
- Cover + Schema DONE до indexer; READY FOR PUBLISH.
- Publish 2026-10-22: SSH+HTTP 504 → REST/wp-cli reconstruct; upsert post 4086 (same slug); no republish.
