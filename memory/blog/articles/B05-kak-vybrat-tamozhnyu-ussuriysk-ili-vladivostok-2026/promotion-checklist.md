# Promotion checklist — B05 kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026

Дата публикации: 2026-10-02  
Live URL: [REDACTED]/2026/10/02/kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026/  
WP post_id: 3937 · featured: 3938 · inline: 3939/3940/3941 · schema_meta: ok

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [x] Открыть live URL — title, excerpt, featured image, FAQ (HEAD 200; REST id 3937)
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [x] Проверить internal links из статьи (200) — CTA catalog+Telegram OK pre-publish
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

Читать: [REDACTED]/2026/10/02/kak-vybrat-tamozhnyu-ussuriysk-ili-vladivostok-2026/
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
- Publish PASS: post 3937; SSH+HTTP; no WebFetch fallback; do not republish.
