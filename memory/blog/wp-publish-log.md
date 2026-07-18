# WP publish log — Авто-Сейлс

Сайт: [REDACTED]/
FTP/SFTP: djinoum7.beget.tech → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-07-17 — AS08 samye-komfortnye-avto-myagkaya-podveska-2026

- **verdict:** PASS
- **post_id:** 3342
- **permalink:** [REDACTED]/2026/07/17/samye-komfortnye-avto-myagkaya-podveska-2026/
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
- **permalink:** [REDACTED]/2026/07/17/trust-encar-carhistory-proverka-do-depozita/
- **featured_image:** 3386
- **inline_images:** 3387 (`inline-01.png`), 3388 (`inline-02.png`), 3389 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** FTP upload + curl fallback (local HTTP trigger timeout 15s; WebFetch wait 120s empty; curl `--max-time 300` OK)
- **note:** `FTP_ROOT=/`; remote `excalibur-blog-publish-once.php` удалён после curl
- **result:** `memory/blog/articles/AS09-trust-encar-carhistory-proverka-do-depozita/wp-publish-result.json`

## 2026-07-19 — AS07 dokumenty-na-avto-iz-kitaya (FALSE PASS — superseded)

- **verdict:** FALSE PASS (superseded)
- **reported_post_id:** 3194 (actually **attachment**, not post)
- **permalink_reported:** [REDACTED]/dokumenty-na-avto-iz-kitaya/ → served **PNG**, not HTML
- **featured_image:** 3466 (orphaned parent=3194)
- **inline_images:** 3467–3469 (orphaned)
- **incident:** `memory/pipeline-memory-queue.md#INC-20260718-2148-publish-false-pass-missing-post`
- **note:** bootstrap `wp_update_post` on stale/attachment id without `post_type=post` check; script printed OK without REST verify

## 2026-07-19 — AS07 dokumenty-na-avto-iz-kitaya (REPUBLISH)

- **verdict:** PASS (REST+HTML verified)
- **post_id:** 3470
- **permalink:** [REDACTED]/2026/07/19/dokumenty-na-avto-iz-kitaya/
- **featured_image:** 3471
- **inline_images:** 3472 (`inline-01.png`), 3473 (`inline-02.png`), 3474 (`inline-03.png`)
- **schema_meta:** ok (`_excalibur_blog_schema_jsonld`)
- **skip_theme_faq_meta:** ok
- **method:** SSH (paramiko) bootstrap + HTTP trigger OK; preflight freed slug from attachment 3194 → `dokumenty-na-avto-iz-kitaya-orphan-media-3194`
- **rest_verify:** GET `/wp-json/wp/v2/posts/3470` → 200 status=publish type=post; slug search count=1; permalink text/html with title
- **result:** `memory/blog/articles/AS07-dokumenty-na-avto-iz-kitaya/wp-publish-result.json`

