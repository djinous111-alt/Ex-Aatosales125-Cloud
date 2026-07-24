# Promotion checklist — B03 avto-iz-korei-ili-kitaya-2026

Дата публикации: 2026-07-24  
Live URL: ${PUBLIC_SITE_URL}/blog/avto-iz-korei-ili-kitaya-2026/

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
Корея или Китай — до депозита, не из чата

• Один бюджет «под ключ» → сценарий → страна одной фразой
• Корея: Encar + Carhistory до аванса; Китай: дата регистрации и ~180 дней
• Нет пакета проверок — нет депозита

Читать: ${PUBLIC_SITE_URL}/blog/avto-iz-korei-ili-kitaya-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Writer уже вставил ссылку B03 → AS09 (`/blog/trust-encar-carhistory-proverka-do-depozita/`)
- [x] Interlinker `--apply`: 0 новых opportunities (pool=3; suggestions=[])

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «авто из кореи или китая» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir .../B03-avto-iz-korei-ili-kitaya-2026 --site-base $PUBLIC_SITE_URL` — opportunities_found=0.
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir` + `--out-dir` (без устаревшего `--blog-path`).
- Publish: pending (следующий шаг пайплайна).
