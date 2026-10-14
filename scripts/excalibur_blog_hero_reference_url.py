#!/usr/bin/env python3
"""Ensure blog hero reference has a public URL for MCP gpt-image-2 input_urls."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _multipart_upload(url: str, fields: list[tuple[str, str]], file_field: str, image_path: Path, timeout: float) -> str:
    boundary = "----ExcaliburHeroBoundary"
    chunks: list[bytes] = []
    for name, value in fields:
        chunks.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
                f"{value}\r\n"
            ).encode("utf-8")
        )
    chunks.append(
        (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{file_field}"; filename="{image_path.name}"\r\n'
            f"Content-Type: image/png\r\n\r\n"
        ).encode("utf-8")
    )
    chunks.append(image_path.read_bytes())
    chunks.append(f"\r\n--{boundary}--\r\n".encode("utf-8"))
    body = b"".join(chunks)
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "ExcaliburBlogHero/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        result = response.read().decode("utf-8", errors="replace").strip()
    if not result.startswith("https://"):
        raise RuntimeError(f"upload to {url} failed: {result[:200]}")
    return result


def upload_catbox(image_path: Path, timeout: float = 180.0) -> str:
    return _multipart_upload(
        "https://catbox.moe/user/api.php",
        [("reqtype", "fileupload")],
        "fileToUpload",
        image_path,
        timeout,
    )


def upload_0x0(image_path: Path, timeout: float = 180.0) -> str:
    return _multipart_upload(
        "https://0x0.st",
        [],
        "file",
        image_path,
        timeout,
    )


def resolve_reference_path(root: Path, hero: dict) -> Path:
    rel = hero.get("reference_image") or "memory/cover/assets/blog-hero-reference.png"
    path = Path(rel)
    if not path.is_absolute():
        path = root / path
    return path


def try_providers(image_path: Path, providers: list[str], retries: int = 2) -> tuple[str, str]:
    last_error: Exception | None = None
    for provider in providers:
        for attempt in range(1, retries + 1):
            try:
                url = upload_catbox(image_path) if provider == "catbox" else upload_0x0(image_path)
                return url, provider
            except (urllib.error.URLError, RuntimeError, TimeoutError, OSError) as exc:
                last_error = exc
                print(f"WARN upload via {provider} attempt {attempt}/{retries} failed: {exc}", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(str(last_error) if last_error else "all hero host providers failed")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hero-json", default="memory/cover/blog-hero.json")
    ap.add_argument("--force", action="store_true", help="Re-upload even if URL exists")
    ap.add_argument("--provider", choices=("catbox", "0x0", "auto"), default="auto")
    args = ap.parse_args()

    root = project_root()
    hero_path = Path(args.hero_json)
    if not hero_path.is_absolute():
        hero_path = root / hero_path
    if not hero_path.is_file():
        print(f"❌ HERO BLOCKER: missing {hero_path}", file=sys.stderr)
        return 1

    hero = load_json(hero_path)
    ref_path = resolve_reference_path(root, hero)
    if not ref_path.is_file():
        print(f"❌ HERO BLOCKER: reference image not found: {ref_path}", file=sys.stderr)
        return 1

    existing = (hero.get("reference_url_hosted") or "").strip()
    if existing and not args.force:
        print(f"OK reference_url_hosted={existing}")
        return 0

    env_url = os.environ.get("BLOG_HERO_REFERENCE_URL", "").strip()
    if env_url:
        hero["reference_url_hosted"] = env_url
        hero["reference_url_source"] = "env:BLOG_HERO_REFERENCE_URL"
        hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        save_json(hero_path, hero)
        print(f"OK reference_url_hosted={env_url}")
        return 0

    providers = ["catbox", "0x0"] if args.provider == "auto" else [args.provider]
    try:
        url, provider = try_providers(ref_path, providers, retries=2)
        hero["reference_url_hosted"] = url
        hero["reference_url_source"] = provider
        hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        save_json(hero_path, hero)
        print(f"OK reference_url_hosted={url}")
        return 0
    except RuntimeError as exc:
        if existing:
            # Keep prior hosted URL instead of blocking cover when rehost fails.
            print(
                f"WARN rehost failed ({exc}); keeping existing reference_url_hosted",
                file=sys.stderr,
            )
            print(f"OK reference_url_hosted={existing}")
            return 0
        print(
            f"❌ HERO BLOCKER: could not host reference: {exc}. "
            "Set BLOG_HERO_REFERENCE_URL or upload via WP media and pass the public URL.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
