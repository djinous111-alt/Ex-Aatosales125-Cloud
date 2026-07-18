# Excalibur BLOG — WordPress publish contract

Excalibur BLOG готовит артефакты локально; публикация — через `scripts/excalibur_blog_wp_publish.py` и FTP bootstrap.

## Prerequisites

- `article.html`, `article.meta.json`, `article-qa.md` (verdict PASS)
- `schema.jsonld`
- `cover/cover.png` + `cover-registry.json` (alt)
- `link-verify.json` (verdict pass)
- `memory/site.env.local` — FTP + `FTP_ROOT` (корень WP, где `wp-load.php`) + `PUBLIC_SITE_URL` + `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`

## Скрипт

```bash
python scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/B01-slug/article.html \
  -o memory/blog/articles/B01-slug/link-verify.json \
  --site-base https://avtosales125.ru

python scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/B01-slug
```

`--dry-run` — проверка payload без FTP.

## Что делает publish

1. `wp_insert_post` / `wp_update_post` — title, slug, content, excerpt (только `post_type=post`)
2. Featured image из `cover/cover.png` + alt
3. **Inline images** — все локальные `<img src="cover/...">` загружаются в Media Library, `src` заменяется на WP URL
4. Post meta `_excalibur_blog_schema_jsonld` — JSON-LD для `single.php`
5. Post meta `_excalibur_blog_skip_theme_faq` = `1` — сигнал теме **не** добавлять глобальный FAQ-блок
6. **Post-verify (обязательно до ledger)** — public REST `GET /wp-json/wp/v2/posts/<id>` + slug search; без 200/`publish` → verdict fail, ledger не писать

## Post id / slug safety

- Previous `post_id` from meta/`wp-publish-result.json` используется **только** если WP подтверждает существующий `post` со status publish|draft|pending|future|private. Attachment / missing / wrong type → ignore + insert/update by slug among posts.
- Slug lookup: `get_page_by_path($slug, OBJECT, 'post')` only. If the same slug is owned by an **attachment**, bootstrap exits `ERR post: slug owned by attachment` (live URL would return image bytes, not HTML).
- After create/update, PHP requires `get_post_type === 'post'` and `post_status === publish`, иначе `ERR post` (no false `OK post=`).

## Дубли FAQ на live-странице (важно)

Excalibur кладёт в `post_content` **один** FAQ по теме (`<h2>Частые вопросы</h2>`).

Тема WordPress на avtosales125.ru может **дописывать** после контента глобальные блоки темы — это **не** часть `article.html`. Тематический FAQ пишет только Excalibur Writer.

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
- `❌ PUBLISH FAIL` — bootstrap `ERR post`, REST verify fail (404 / wrong type), attachment slug collision
- Production HTML не должен содержать MCP URLs — только WP media для featured image

Skill: `skills/publish-excalibur-blog/SKILL.md` (alias: `skills/excalibur-wp-publish/SKILL.md`)
