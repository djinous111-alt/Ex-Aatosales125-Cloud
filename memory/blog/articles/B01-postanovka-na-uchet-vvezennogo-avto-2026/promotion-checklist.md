# Promotion checklist — B01 postanovka-na-uchet-vvezennogo-avto-2026

Дата публикации: 2026-09-30 (planned; до publish)  
Live URL: [REDACTED]/blog/postanovka-na-uchet-vvezennogo-avto-2026/

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
Таможня закрыта — это ещё не финиш

• Пакет в ГИБДД ≠ документы для ввоза: проверьте статус ЭПТС до записи
• С 01.03.2025 ОСАГО для окна не обязательно; полис нужен для дороги своим ходом
• Цель: СТС и номера с первого визита в срок 10 дней

Читать: [REDACTED]/blog/postanovka-na-uchet-vvezennogo-avto-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (корпус memory: B01, AS08, AS09 — темы не пересекаются; AS01–AS07 на live — вручную после publish)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «постановка на учет авто из японии» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B01-… --site-base '[REDACTED]'` — opportunities_found=0, article.html без изменений.
- llms.txt / llms-full.txt обновлены в `memory/blog/` с commit-safe `--site-base '[REDACTED]'` (B01 в индексе).
- Publish: pending (Indexer не публикует).
- Incident: memory/pipeline-fix-queue.md#INC-20260930-1804-indexer-llms-public-site-url-commit
