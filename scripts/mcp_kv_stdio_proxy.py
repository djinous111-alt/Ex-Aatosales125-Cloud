#!/usr/bin/env python3
"""stdio MCP proxy for MCP KV.

Cursor Cloud treats https://mcp-kv.ru/mcp/sse/... as an OAuth resource.
The same URL accepts JSON-RPC over POST with the connector id in the path.
This process speaks newline-delimited JSON-RPC on stdin/stdout and forwards
each request to MCP_KV_TOKEN, which must be that full SSE URL.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request


def endpoint() -> str:
    url = os.environ.get("MCP_KV_TOKEN", "").strip()
    if not url.startswith("https://mcp-kv.ru/mcp/sse/"):
        print(
            "MCP_KV_TOKEN must be the https://mcp-kv.ru/mcp/sse/<id> connector URL",
            file=sys.stderr,
        )
        raise SystemExit(1)
    return url


def forward(url: str, message: dict) -> dict | None:
    if "id" not in message:
        return None
    payload = json.dumps(message, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read(500).decode("utf-8", "replace")
        return {
            "jsonrpc": "2.0",
            "id": message.get("id"),
            "error": {"code": -32000, "message": f"MCP KV HTTP {exc.code}: {detail[:240]}"},
        }
    except Exception as exc:  # noqa: BLE001 — surface transport failures to the MCP client
        return {
            "jsonrpc": "2.0",
            "id": message.get("id"),
            "error": {"code": -32000, "message": f"MCP KV transport error: {exc}"},
        }
    try:
        parsed = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError:
        return {
            "jsonrpc": "2.0",
            "id": message.get("id"),
            "error": {"code": -32700, "message": "MCP KV returned a non-JSON body"},
        }
    if isinstance(parsed, dict) and "id" not in parsed:
        parsed["id"] = message.get("id")
    return parsed if isinstance(parsed, dict) else None


def main() -> int:
    url = endpoint()
    for line in sys.stdin:
        raw = line.strip()
        if not raw:
            continue
        try:
            message = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(message, dict):
            continue
        reply = forward(url, message)
        if reply is None:
            continue
        sys.stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
