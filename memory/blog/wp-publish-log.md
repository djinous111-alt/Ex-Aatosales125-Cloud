# WP publish log — Авто-Сейлс

Сайт: ${PUBLIC_SITE_URL}/
FTP/SFTP: ${SSH_HOST} → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

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

## 2026-11-01 — AS02 encar-na-russkom-kak-chitat

- **verdict:** PASS
- **post_id:** 3394 (update existing same-slug LIVE; denylist 4717/4711/4699/… untouched)
- **permalink:** ${PUBLIC_SITE_URL}/2026/07/18/encar-na-russkom-kak-chitat/
- **featured_image:** 4724
- **inline_images:** 4725 (`inline-01.png`), 4726 (`inline-02.png`), 4727 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **HEAD:** 200
- **method:** SSH upload (`SSH_ROOT=.`) + HTTP trigger OK (~124s, no WebFetch)
- **preflight:** link-verify pass; dry-run PHP ~6.7MB; slug already LIVE as 3394 (same AS02 title)
- **env notes:** recreated `memory/site.env.local` from Cloud Secrets; `SSH_PATH`→`SSH_ROOT=.`; pip install paramiko; schema `${ENV}` hydrated then restored
- **result:** `memory/blog/articles/AS02-encar-na-russkom-kak-chitat/wp-publish-result.json`
