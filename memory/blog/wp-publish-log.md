# WP publish log — Авто-Сейлс

Сайт: https://avtosales125.ru/
FTP/SFTP: djinoum7.beget.tech → `/` (FTP chroot = public_html WP; `FTP_ROOT=/`)
Метрика Дзен: 109566711

Лог публикаций начинается с нуля после перенастройки под AVTO SALES (2026-07-17).

## 2026-11-02 — AS10 kak-vybrat-toyota-sienta-iz-yaponii-2026

- **verdict:** FAIL / ❌ PUBLISH BLOCKER
- **post_id:** (none — not published)
- **permalink:** (none)
- **featured_image / inline_images / schema_meta:** not uploaded
- **slug:** `kak-vybrat-toyota-sienta-iz-yaponii-2026` (NEW; denylist-safe — did not touch WP 4711 Haval M6)
- **preflight:** link-verify pass; env-check allow=true; dry-run PHP ~6324760 bytes; `wp_post_id` absent in meta
- **method attempted:** SSH bootstrap only (`SSH_ROOT=.`); paramiko installed via pip workaround
- **error:** `socket.gaierror` resolving `SSH_HOST` (`*.beget.tech`) — empty/SERVFAIL A globally (check-host empty A); site IP has no :22
- **ledger:** left `in_progress` (not marked published)
- **result:** `memory/blog/articles/AS10-kak-vybrat-toyota-sienta-iz-yaponii-2026/wp-publish-result.json`
- **incident:** `memory/pipeline-fix-queue.md#INC-20261102-1035-publish-ssh-host-dns-empty-as10`

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
