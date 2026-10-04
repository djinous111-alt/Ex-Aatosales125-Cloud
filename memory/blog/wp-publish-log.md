# WP publish log — Авто-Сейлс

Сайт: [PUBLIC_SITE_URL]/
FTP/SFTP: djinoum7.beget.tech → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** [PUBLIC_SITE_URL]/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
- **featured_image:** 3349
- **inline_images:** 3351 (`inline-01.png`), 3355 (`inline-02.png`), 3358 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch timeout; curl `--max-time 300` OK)
- **note:** в `article.meta.json` добавлены `title`/`h1`/`description`/`cover_alt` для payload; `FTP_ROOT` исправлен на `/`
- **result:** `memory/blog/articles/AS08-samye-komfortnye-avto-myagkaya-podveska-2026/wp-publish-result.json`

## 2026-07-17 — AS09 trust-encar-carhistory-proverka-do-depozita

- **verdict:** PASS
- **post_id:** 3364
- **permalink:** [PUBLIC_SITE_URL]/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-10-04 — B02 postanovka-na-uchet-avto-iz-yaponii-2026

- **verdict:** PASS (soft-success)
- **post_id:** 3589
- **permalink:** [PUBLIC_SITE_URL]/2026/07/21/postanovka-na-uchet-avto-iz-yaponii-2026/
- **featured_image:** 4014
- **inline_images:** 4011 (`inline-01.png`), 4012 (`inline-02.png`), 4013 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`, len=13245)
- **skip_theme_faq_meta:** ok
- **method:** SSH upload + HTTP/curl 504; soft-success via WP REST + SSH meta-check
- **note:** updated existing slug post (not new); did NOT touch B01 3991; orphan media from overlapping triggers: 4010, 4015, 4016, 4017
- **result:** `memory/blog/articles/B02-postanovka-na-uchet-avto-iz-yaponii-2026/wp-publish-result.json`

