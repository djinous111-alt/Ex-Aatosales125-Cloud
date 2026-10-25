# Conversion map — Excalibur BLOG (Авто-Сейлс)


| CTA | URL / action | Max mentions per article | Notes |
| --- | --- | --- | --- |
| Каталог авто | https://avto-sales125.ru/ | 3 | главный оффер; расчёты и подбор только здесь |
| Telegram avtosales125 | https://t.me/avtosales125 | 2 | детали заказа, ответы менеджера |
| MAX | https://max.ru/id2508140890_biz | 1 | альтернативный мессенджер |
| Отзывы 2GIS | https://2gis.ru/vladivostok/search/авто%20сейлс%20владивосток/firm/70000001090415417/131.924668%2C43.140033/tab/reviews | 1 | доверие / E-E-A-T |
| Instagram | https://www.instagram.com/avtosales_rf | 1 | опционально, если релевантно |
| Адрес офиса | Владивосток, Днепровская 40а стр. 4 | 1 | в футере/блоке компании, не как CTA-кнопка |

## CTA href + secret-scan (Writer)

- В `article.html` подставляй живые URL из Cloud Secrets / env: `CATALOG_URL`, `TELEGRAM_URL`, `MAX_URL` (не оставляй `[REDACTED]` в href).
- Если CTA совпадает с secret value, на той же HTML-строке обязателен `<!-- pragma: allowlist secret -->`, иначе pre-commit secret-scan блокирует commit.
- Перед commit: `bash scripts/excalibur_git.sh commit …`.
