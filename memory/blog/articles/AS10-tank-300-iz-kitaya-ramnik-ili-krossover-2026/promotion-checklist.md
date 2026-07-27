# Promotion checklist — AS10 tank-300-iz-kitaya-ramnik-ili-krossover-2026

Дата публикации: 2026-07-27 (план; WP не опубликован — ❌ PUBLISH BLOCKER cover.png)  
Live URL: — (ожидает cover + publish)

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
Квадратный кузов ≠ рама

• Tank 300 – лестничный рамник; Jetour T2 / Haval Dargo – несущий кузов
• Сначала сценарий на неделю, потом тип машины и привод
• Депозит – только после VIN, осмотра и фиксации комплектации

Читать: [REDACTED]/blog/tank-300-iz-kitaya-ramnik-ili-krossover-2026/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker: 0 opportunities (AS08 comfort / AS09 Encar — слабый topical overlap с Tank/рамник)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «танк 300 из китая» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS10-… --blog-dir memory/blog/articles --site-base $PUBLIC_SITE_URL` — 0 links applied; report `memory/blog/interlink-suggestions.json`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (CLI: `--blog-dir` + `--out-dir`, без `--blog-path`).
- Cover: BLOCKER CREDITS — `cover.png` missing; featured image на publish отложен до top-up Kie / resume cover.
- Schema: PASS (`schema.jsonld` BlogPosting + FAQPage + HowTo).
