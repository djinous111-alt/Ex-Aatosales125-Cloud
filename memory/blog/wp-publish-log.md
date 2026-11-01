# WP publish log — Авто-Сейлс

Сайт: ${PUBLIC_SITE_URL}
FTP/SFTP: [REDACTED]
Метрика Дзен: [REDACTED]

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** ${PUBLIC_SITE_URL}/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
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
- **permalink:** ${PUBLIC_SITE_URL}/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-11-01 — AS13 chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026

- **verdict:** PASS
- **post_id:** 4746 (NEW; slug FREE — denylist untouched)
- **permalink:** `${PUBLIC_SITE_URL}/2026/11/01/chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026/`
- **featured_image:** 4752
- **inline_images:** 4754 (`inline-01.png`), 4755 (`inline-02.png`), 4756 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** SSH_ROOT=.; HTTP trigger TimeoutError (120s) → WebFetch/urllib fallback once OK (~270s wall); HEAD 200
- **note:** paramiko missing on image → `pip install --break-system-packages paramiko`; schema `${…}` hydrated pre-publish then placeholders restored; inline media filenames ended with `-1.png` (known fallback side-effect; do not republish)
- **denylist:** 4740/3430/3394/4717/4711/4699/4687/4681/4675/4669/4663 untouched
- **result:** `memory/blog/articles/AS13-chery-tiggo-7-pro-iz-kitaya-komplektatsii-lovushki-2026/wp-publish-result.json`
