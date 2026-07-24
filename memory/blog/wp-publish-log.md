# WP publish log — Авто-Сейлс

Сайт: https://avtosales125.ru/
FTP/SFTP: djinoum7.beget.tech → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** https://avtosales125.ru/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
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
- **permalink:** https://avtosales125.ru/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-07-24 — B04 avtovoz-iz-vladivostoka-2026-kak-vybrat

- **verdict:** PASS
- **post_id:** 3713
- **permalink:** https://avtosales125.ru/2026/07/24/avtovoz-iz-vladivostoka-2026-kak-vybrat/
- **featured_image:** 3725
- **inline_images:** 3727 (`inline-01.png`), 3730 (`inline-02.png`), 3733 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`, FAQPage+HowTo in meta)
- **skip_theme_faq_meta:** ok
- **method:** SSH upload bootstrap; local HTTP + WebFetch + curl hit nginx 504 @120s; server-side PHP finished; verified via WP REST + HTTP meta probe
- **live_HEAD:** 200
- **note:** `SSH_ROOT` unset → relative cwd path; installed `paramiko` via pip `--break-system-packages`; duplicate media `-1/-2/-3` from concurrent retries (content uses `-3`)
- **result:** `memory/blog/articles/B04-avtovoz-iz-vladivostoka-2026-kak-vybrat/wp-publish-result.json`
- **incident:** `memory/pipeline-fix-queue.md#INC-20260724-1740-publish-http-504-paramiko`

