# MCP Image Async Contract

Для image generation в Cursor Cloud нельзя полагаться на один долгий sync MCP call: Cursor MCP client может оборвать соединение раньше, чем backend дождётся Kie.ai.

## Required tools

Рекомендуемый контракт для `user-mcp-kv`:

1. `gpt-image-2-create` / `gpt-image-2-start`
   - input: тот же JSON, что у sync `gpt-image-2` (`prompt`, `input_urls`, `aspect_ratio`, `resolution`)
   - output за короткое время: `{ "task_id": "...", "status": "queued|running" }`
   - должен быть idempotent по `request_id`/hash prompt+input_urls, чтобы агент не создавал дубли

2. `gpt-image-2-status` / `gpt-image-2-result`
   - input: `{ "task_id": "..." }`
   - output: `{ "status": "queued|running|succeeded|failed", "url": "...", "error": "..." }`
   - агент вызывает каждые 10–15 секунд до `status=succeeded` и `url`

## Agent rule

Cover agent (Cloud default):

1. **Предпочтительный путь:** прямой Kie async API через
   `python3 scripts/excalibur_blog_kie_gpt_image2_api.py --article-dir <dir>`
   (createTask → recordInfo, `task_id` сразу, poll в shell). Аргументы = `jobs[0].api_args` / тот же prompt+input_urls.
2. Sync MCP `gpt-image-2` — **legacy fallback** только если нет `KIE_API_KEY` и нет async MCP tools.
3. Если sync MCP всё же вызван: максимум **1** попытка; после `HTTP MCP -32001 Request timed out` не делать blind retry sync create; искать URL/task_id в MCP logs.
4. Если нет URL/task_id и нет status/result tool — `COVER MCP ASYNC BLOCKER` или сразу Kie fallback (если ключ есть).

## Why

`KIE_IMAGE_MAX_WAIT_SECONDS` и nginx `proxy_read_timeout` не гарантируют, что Cursor MCP client будет держать один tool call так же долго. Async start/status/result убирает зависимость от длинного соединения и позволяет агенту получить URL через время без дублей.
