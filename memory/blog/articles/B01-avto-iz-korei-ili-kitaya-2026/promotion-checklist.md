# Promotion checklist — B01 avto-iz-korei-ili-kitaya-2026

Дата публикации: 2026-10-13 (pending publish)  
Live URL: (заполнит Publish; ожидаемый slug `avto-iz-korei-ili-kitaya-2026`)

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
Корея или Китай — не выбирай по красивому фото

• Растаможка одинакова при тех же характеристиках — миф про «дешёвую страну»
• Сначала задача и порог 160 л.с., потом две сметы под ключ
• Депозит — только после договора и списка статей

Читать: [URL после publish]
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (corpus: AS08, AS09, B01; suggestions=[])

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «авто из кореи и китая» (ручная проверка / Wordstat)

## Notes

- Indexer: `interlinker --apply --article-dir memory/blog/articles/B01-avto-iz-korei-ili-kitaya-2026` — opportunities_found=0; `article.html` без новых internal links.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (CLI: `--blog-dir`, без `--blog-path`).
- Cover + schema готовы до Indexer; Publish — следующий шаг.
