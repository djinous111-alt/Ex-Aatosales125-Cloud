# Excalibur BLOG — WordPress publish contract

Excalibur BLOG готовит артефакты локально; публикация — через `scripts/excalibur_blog_wp_publish.py` и FTP bootstrap.

## Prerequisites

- `article.html`, `article.meta.json`, `article-qa.md` (verdict PASS)
- `schema.jsonld`
- `cover/cover.png` + `cover-registry.json` (alt)
- `link-verify.json` (verdict pass; catalog DNS soft-pass allowed)
- Publish transport: **SSH** (`SSH_HOST` / optional `SSH_HOST_IP`, `SSH_USER`, `SSH_PASS`/`SSH_PASSWORD`, `SSH_ROOT` or `SSH_PATH`)
- `PUBLIC_SITE_URL` + `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`
- `paramiko` installed (pinned via `requirements.txt` / cloud-agent-install)

## Скрипт

```bash
python3 scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/AS02-slug/article.html \
  -o memory/blog/articles/AS02-slug/link-verify.json \
  --site-base "${PUBLIC_SITE_URL}"

python3 scripts/excalibur_blog_wp_publish.py --env-check
python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/AS02-slug \
  --dry-run
python3 scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/AS02-slug
```

`--env-check` probes SSH DNS (`getaddrinfo`) / `SSH_HOST_IP` and `paramiko` without printing secrets.
If DNS fails and `SSH_HOST_IP` is unset → publish blocker (human restores Beget DNS or adds IP secret with TCP/22).
Never use `PUBLIC_SITE_URL` resolved IP as SSH fallback.
`--dry-run` — проверка payload без LIVE write.

## Что делает publish

1. `wp_insert_post` / `wp_update_post` — title, slug, content, excerpt
2. Featured image из `cover/cover.png` + alt
3. **Inline images** — все локальные `<img src="cover/...">` загружаются в Media Library, `src` заменяется на WP URL
4. Post meta `_excalibur_blog_schema_jsonld` — JSON-LD для `single.php`
5. Post meta `_excalibur_blog_skip_theme_faq` = `1` — сигнал теме **не** добавлять глобальный FAQ-блок

## Дубли FAQ на live-странице (важно)

Excalibur кладёт в `post_content` **один** FAQ по теме (`<h2>Частые вопросы</h2>`).

Тема WordPress может **дописывать** после контента глобальные блоки темы — это **не** часть `article.html`. Тематический FAQ пишет только Excalibur Writer.

**Исправление в теме WordPress** (`single.php` или фильтр `the_content`):

```php
$skip_theme_faq = get_post_meta(get_the_ID(), '_excalibur_blog_skip_theme_faq', true);
if ($skip_theme_faq === '1') {
    // не выводить глобальный FAQ-блок темы для постов Excalibur BLOG
}
```

Publish-скрипт выставляет meta `_excalibur_blog_skip_theme_faq` автоматически при каждой публикации.

## Артефакты после publish

```text
memory/blog/articles/<topic_id>-<slug>/wp-publish-result.json
memory/blog/wp-publish-log.md
```

## Schema в теме WP

```php
$schema = get_post_meta(get_the_ID(), '_excalibur_blog_schema_jsonld', true);
if ($schema) {
    echo '<script type="application/ld+json">' . wp_kses_post($schema) . '</script>';
}
```

## Blockers

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет credentials
- Production HTML не должен содержать MCP URLs — только WP media для featured image

Skill: `skills/publish-excalibur-blog/SKILL.md` (alias: `skills/excalibur-wp-publish/SKILL.md`)
