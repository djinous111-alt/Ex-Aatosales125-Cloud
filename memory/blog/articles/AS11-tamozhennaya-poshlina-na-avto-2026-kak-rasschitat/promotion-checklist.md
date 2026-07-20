# Promotion checklist — AS11 tamozhennaya-poshlina-na-avto-2026-kak-rasschitat

Дата публикации: 2026-07-20  
Live URL: https://avtosales125.ru/2026/07/20/tamozhennaya-poshlina-na-avto-2026-kak-rasschitat/  
Canonical blog path (llms/interlink): https://avtosales125.ru/blog/tamozhennaya-poshlina-na-avto-2026-kak-rasschitat/

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
Калькулятор показал одну цифру — в смете три строки

• Таможенная пошлина ≠ утильсбор ≠ таможенный сбор
• Соберите «паспорт данных»: возраст, см³, мощность, инвойс, курс ЦБ
• Для 3+ лет ставка ЕТС от объёма, не от цены аукциона

Читать: https://avtosales125.ru/2026/07/20/tamozhennaya-poshlina-na-avto-2026-kak-rasschitat/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Локальный interlinker `--apply`: 0 opportunities (в memory только AS08, AS09, AS11; keyword overlap нет)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «таможенная пошлина на авто» (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --article-dir …/AS11-… --site-base $PUBLIC_SITE_URL` — Found 0 internal linking opportunities (Loaded 3 articles).
- llms.txt / llms-full.txt обновлены в `memory/blog/` через `--blog-dir memory/blog/articles` (без `--blog-path`; CLI его не принимает).
- AS11 включён в llms index (3 articles).
- Publish: PASS — WP post_id=3535; featured=3536; inline=3537/3538/3539; schema_meta=1; live HEAD 200.
