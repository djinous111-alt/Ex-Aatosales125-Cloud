# Conversion map — Excalibur BLOG (Авто-Сейлс)


| CTA | URL / action | Max mentions per article | Notes |
| --- | --- | --- | --- |
| Каталог авто | [from env CATALOG_URL] | 3 | главный оффер; расчёты и подбор только здесь |
| Telegram Авто-Сейлс | [from env TELEGRAM_URL] | 2 | детали заказа, ответы менеджера |
| MAX | [from env MAX_URL] | 1 | альтернативный мессенджер |
| Отзывы 2GIS | https://2gis.ru/vladivostok/search/авто%20сейлс%20владивосток/firm/70000001090415417/131.924668%2C43.140033/tab/reviews | 1 | доверие / E-E-A-T |
| Instagram | https://www.instagram.com/avtosales_rf | 1 | опционально, если релевантно |
| Адрес офиса | Владивосток, Днепровская 40а стр. 4 | 1 | в футере/блоке компании, не как CTA-кнопка |

## Commit / secret-scan

URL каталога и Telegram часто хранятся как Cloud Secrets (`CATALOG_URL`, `TELEGRAM_URL`). В `article.html` на строках с этими href ставь `<!-- pragma: allowlist secret -->`, иначе Cursor secret-scan блокирует commit.
