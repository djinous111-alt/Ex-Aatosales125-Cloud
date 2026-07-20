# Conversion map — Excalibur BLOG (Авто-Сейлс)


| CTA | URL / action | Max mentions per article | Notes |
| --- | --- | --- | --- |
| Каталог авто | env `CATALOG_URL` | 3 | главный оффер; расчёты и подбор только здесь |
| Telegram Авто-Сейлс | env `TELEGRAM_URL` | 2 | детали заказа, ответы менеджера |
| MAX | env `MAX_URL` если задан | 1 | альтернативный мессенджер |
| Отзывы 2GIS | https://2gis.ru/vladivostok/search/авто%20сейлс%20владивосток/firm/70000001090415417/131.924668%2C43.140033/tab/reviews | 1 | доверие / E-E-A-T |
| Instagram | https://www.instagram.com/avtosales_rf | 1 | опционально, если релевантно |
| Адрес офиса | Владивосток, Днепровская 40а стр. 4 | 1 | в футере/блоке компании, не как CTA-кнопка |

## CTA URL rules (writer / GEO QA)

- Реальные `href` только из env: `CATALOG_URL`, `TELEGRAM_URL` (опционально `MAX_URL`).
- Резолв: `python3 scripts/excalibur_blog_cta_urls.py --json` (не копируй плейсхолдер `[REDACTED]` из brief/site-brief в HTML).
- После подстановки Telegram CTA в `article.html` добавь на ту же строку `<!-- pragma: allowlist secret -->` — Cursor secret-scan часто блокирует публичный `t.me/...`, если `TELEGRAM_URL` в Dashboard Secrets.
- `link-verify` hard-fail на литерал `[REDACTED]` в href.
