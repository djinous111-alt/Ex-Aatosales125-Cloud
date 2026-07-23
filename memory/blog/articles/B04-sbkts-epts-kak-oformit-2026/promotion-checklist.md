# Promotion checklist — B04 sbkts-epts-kak-oformit-2026

Дата публикации: 2026-07-23 (planned)  
Live URL: [REDACTED]/2026/07/23/sbkts-epts-kak-oformit-2026/

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
Растаможили — а в ГИБДД разворачивают?

• Сначала СБКТС в аккредитованной лаборатории, потом ЭПТС
• На учёт только со статусом «действующий» на portal.elpts.ru
• Для физлиц ЭРА-ГЛОНАСС часто не нужна до 31.12.2027

Читать: [REDACTED]/2026/07/23/sbkts-epts-kak-oformit-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (корпус AS08/AS09/B04; тематика СБКТС/ЭПТС не пересекается с comfort/Encar)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как оформить эптс» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir .../B04-sbkts-epts-kak-oformit-2026 --site-base [REDACTED]` — opportunities_found=0; article.html без новых internal links.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (B04 в индексе; CLI: `--blog-dir` + `--out-dir`, `--site-base [REDACTED]` для secret-scan).
- Canonical blog path: [REDACTED]/blog/sbkts-epts-kak-oformit-2026/
