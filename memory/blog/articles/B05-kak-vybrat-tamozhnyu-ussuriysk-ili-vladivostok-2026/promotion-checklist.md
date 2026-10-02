# Promotion checklist — B05 kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026

Дата публикации: 2026-10-02  
Live URL: https://example.com/2026/10/02/kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026/

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
Пост не по чату про очереди

• Пошлины в Уссурийске и Владивостоке одинаковые
• До депозита: маршрут ввоза + зона по приказу 178н
• Нет совпадения — таможенный транзит, не перегон «ради очереди»

Читать: https://example.com/2026/10/02/kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (B05 vs AS08/AS09 — разные кластеры; suggestions пустые)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как выбрать таможню уссурийск или владивосток» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/B05-… --site-base $PUBLIC_SITE_URL` — 0 links applied; report `memory/blog/interlink-suggestions.json`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir` (без `--blog-path`). Live URLs в git — placeholder `example.com` из‑за secret-scan PUBLIC_SITE_URL (runtime publish подставит origin).
- Publish: ещё не выполнялся (Indexer only).
