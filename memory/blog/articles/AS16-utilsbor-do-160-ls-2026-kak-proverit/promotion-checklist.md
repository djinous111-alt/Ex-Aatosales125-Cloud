# Promotion checklist — AS16 utilsbor-do-160-ls-2026-kak-proverit

Дата публикации: 2026-07-21 (pending publish)  
Live URL: /blog/utilsbor-do-160-ls-2026-kak-proverit/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (+ HowTo)
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
Encar пишет 159–160 л.с., а таможня смотрит кВт

• Льгота утильсбора — до 117,68 кВт включительно
• От 117,69 кВт — другая ставка; «ровно 160» часто маркетинг
• Депозит — только после шильдика/техпаспорта и расчёта по лоту

Читать: /blog/utilsbor-do-160-ls-2026-kak-proverit/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [ ] После publish: inbound с live AS04 (`utilsbor-na-avto-2026`) — в memory/blog/articles локально только AS08/AS09/AS16, interlinker opportunities=0
- [x] Локальный interlinker `--apply`: 0 links (нет keyword overlap AS08/AS09 ↔ AS16)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «утильсбор до 160 лс» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir … --site-base ""` (relative `/blog/…/` for secret hygiene) — 0 opportunities / 0 applied.
- llms.txt / llms-full.txt: `memory/blog/` via `--blog-dir memory/blog/articles` (без `--blog-path`); site-base `""` → relative paths; 3 articles indexed including AS16.
- Publish: pending (Indexer does not publish).
