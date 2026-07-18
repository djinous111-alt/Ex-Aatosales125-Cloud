# Kie GPT Image 2 API Contract

Primary Cloud path for Excalibur BLOG cover generation.

## Why

Cursor Cloud can terminate long sync MCP tool calls before GPT Image 2 finishes
2K image-to-image generation. Sync MCP `gpt-image-2` often returns client timeout
`-32001` on complex 2K image-to-image quad prompts (simple text-only t2i may still
complete in ~50s). The direct Kie API is asynchronous:

```text
createTask -> taskId -> recordInfo polling -> resultUrls[0]
```

This keeps waiting in the shell process instead of a single MCP request.

**Cover agent order:** Kie async API first → sync MCP `gpt-image-2` only as legacy
fallback when `KIE_API_KEY` is unavailable **and** async MCP start/status tools are
absent. Do not retry sync `gpt-image-2` blindly after `-32001`.

## Auth

- Env var: **`KIE_API_KEY`** (Kie bearer key for `api.kie.ai`)
- **MUST** be set in Cursor Dashboard → Cloud Agents → Secrets for Cloud cover runs.
- **`MCP_KV_TOKEN` is not `KIE_API_KEY`:** it is the MCP SSE endpoint URL for
  `user-mcp-kv`, not a Kie API bearer token.
- Store only in Cursor Cloud Secrets / environment.
- Never commit, print, or copy the key into handoff, PR bodies, article files, or logs.

Preflight (no secret output):

```bash
python3 scripts/excalibur_blog_kie_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --dry-run
# Without KIE_API_KEY the real run exits 1 with: KIE API BLOCKER
```

## Cover command

```bash
python scripts/excalibur_blog_kie_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

The script reads:

- `cover/quad-mcp-batch.json` -> `jobs[0].mcp_args`

The script writes:

- `cover/kie-image-task.json` -> `task_id` and non-secret status
- `cover/quad-mcp-result.json` -> generated URL, compatible with `quad_apply`

Then run:

```bash
python3 scripts/excalibur_blog_quad_apply.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --inject-html
```

(`quad_apply` reads `cover/quad-mcp-result.json` when `--url` is omitted.)

## Reference URL for `input_urls`

Kie fetches `input_urls[0]` server-side. For reliable i2i:

- Use **`reference_url_hosted` from `memory/cover/blog-hero.json`** — must be **HTTPS**.
- Prefer a **small compressed hero JPEG** (face crop, roughly ≤500 KB) over a large PNG;
  rehost with `scripts/excalibur_blog_hero_reference_url.py` if fetch fails.
- Site-hosted HTTPS URLs on the public catalog domain are preferred over ephemeral hosts
  when Kie can reach them; if Kie cannot fetch the site URL, rehost and update
  `reference_url_hosted` before createTask.

## API shape

Create:

```json
{
  "model": "gpt-image-2-image-to-image",
  "input": {
    "prompt": "...",
    "input_urls": ["https://.../ava.jpg"],
    "aspect_ratio": "16:9",
    "resolution": "2K"
  }
}
```

Poll:

```text
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>
```

Terminal states:

- `success`: parse `data.resultJson` and use `resultUrls[0]`
- `fail`: stop with `KIE API BLOCKER`
- timeout without URL: stop with `KIE API BLOCKER`

## Guardrails

- One API task per article cover run, not four separate images.
- `input_urls` is required; text-only generation is a cover blocker.
- Do not retry createTask blindly after a network ambiguity if a `taskId` is known; poll the known task.
