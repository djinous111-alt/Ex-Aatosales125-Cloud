#!/usr/bin/env python3
"""Ensure blog hero reference has a public URL for MCP gpt-image-2 input_urls."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_url_bytes(url: str, *, timeout: int = 60) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ExcaliburBlogHero/1.0"},
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def hosted_matches_local(url: str, local_path: Path) -> bool:
    """Return True when remote bytes match local PNG (safe reuse after --force upload fail)."""
    try:
        remote = fetch_url_bytes(url)
        local = local_path.read_bytes()
        return sha256_bytes(remote) == sha256_bytes(local)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"WARN hosted hash-check failed for {url}: {exc}", file=sys.stderr)
        return False


def _multipart(fields: list[tuple[str, str | None, bytes | None, str | None]], boundary: str) -> bytes:
    chunks: list[bytes] = []
    for name, filename, content, content_type in fields:
        chunks.append(f"--{boundary}\r\n".encode("utf-8"))
        if filename is None:
            chunks.append(
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("utf-8")
            )
            chunks.append((content or b""))
            chunks.append(b"\r\n")
        else:
            chunks.append(
                (
                    f'Content-Disposition: form-data; name="{name}"; '
                    f'filename="{filename}"\r\n'
                    f"Content-Type: {content_type or 'application/octet-stream'}\r\n\r\n"
                ).encode("utf-8")
            )
            chunks.append(content or b"")
            chunks.append(b"\r\n")
    chunks.append(f"--{boundary}--\r\n".encode("utf-8"))
    return b"".join(chunks)


def _post_multipart(url: str, body: bytes, boundary: str, *, timeout: int = 120) -> str:
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
        return response.read().decode("utf-8", errors="replace").strip()


def upload_catbox(image_path: Path) -> str:
    boundary = "----ExcaliburHeroBoundary"
    body = _multipart(
        [
            ("reqtype", None, b"fileupload", None),
            ("fileToUpload", image_path.name, image_path.read_bytes(), "image/png"),
        ],
        boundary,
    )
    url = _post_multipart("https://catbox.moe/user/api.php", body, boundary)
    if not url.startswith("https://"):
        raise RuntimeError(f"catbox upload failed: {url[:200]}")
    return url


def upload_0x0(image_path: Path) -> str:
    boundary = "----ExcaliburHero0x0"
    body = _multipart(
        [("file", image_path.name, image_path.read_bytes(), "image/png")],
        boundary,
    )
    url = _post_multipart("https://0x0.st", body, boundary)
    if not url.startswith("https://"):
        raise RuntimeError(f"0x0 upload failed: {url[:200]}")
    return url


def upload_litterbox(image_path: Path) -> str:
    """catbox litterbox temporary host (72h)."""
    boundary = "----ExcaliburHeroLitter"
    body = _multipart(
        [
            ("reqtype", None, b"fileupload", None),
            ("time", None, b"72h", None),
            ("fileToUpload", image_path.name, image_path.read_bytes(), "image/png"),
        ],
        boundary,
    )
    url = _post_multipart("https://litterbox.catbox.moe/resources/internals/api.php", body, boundary)
    if not url.startswith("https://"):
        raise RuntimeError(f"litterbox upload failed: {url[:200]}")
    return url


def upload_tmpfiles(image_path: Path) -> str:
    boundary = "----ExcaliburHeroTmpfiles"
    body = _multipart(
        [("file", image_path.name, image_path.read_bytes(), "image/png")],
        boundary,
    )
    raw = _post_multipart("https://tmpfiles.org/api/v1/upload", body, boundary)
    # Response is JSON: {"status":"success","data":{"url":"https://tmpfiles.org/123/name.png"}}
    try:
        payload = json.loads(raw)
        url = (payload.get("data") or {}).get("url") or ""
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"tmpfiles non-JSON: {raw[:200]}") from exc
    if not url.startswith("https://"):
        raise RuntimeError(f"tmpfiles upload failed: {raw[:200]}")
    # Direct download variant is more reliable for MCP fetchers.
    if "tmpfiles.org/" in url and "/dl/" not in url:
        url = url.replace("tmpfiles.org/", "tmpfiles.org/dl/", 1)
    return url


def upload_uguu(image_path: Path) -> str:
    boundary = "----ExcaliburHeroUguu"
    body = _multipart(
        [("files[]", image_path.name, image_path.read_bytes(), "image/png")],
        boundary,
    )
    raw = _post_multipart("https://uguu.se/upload.php", body, boundary)
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"uguu non-JSON: {raw[:200]}") from exc
    files = payload.get("files") or []
    url = ""
    if files and isinstance(files[0], dict):
        url = (files[0].get("url") or "").strip()
    if not url.startswith("https://"):
        raise RuntimeError(f"uguu upload failed: {raw[:200]}")
    return url


PROVIDERS = {
    "catbox": upload_catbox,
    "0x0": upload_0x0,
    "litterbox": upload_litterbox,
    "tmpfiles": upload_tmpfiles,
    "uguu": upload_uguu,
}

# Prefer durable hosts first; fall back to temporary hosts used successfully in Cloud runs.
AUTO_ORDER = ["catbox", "0x0", "litterbox", "tmpfiles", "uguu"]


def resolve_reference_path(root: Path, hero: dict) -> Path:
    rel = hero.get("reference_image") or "memory/cover/assets/blog-hero-reference.png"
    path = Path(rel)
    if not path.is_absolute():
        path = root / path
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hero-json", default="memory/cover/blog-hero.json")
    ap.add_argument("--force", action="store_true", help="Re-upload even if URL exists")
    ap.add_argument(
        "--provider",
        choices=(*PROVIDERS.keys(), "auto"),
        default="auto",
    )
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

    providers = AUTO_ORDER if args.provider == "auto" else [args.provider]
    last_error: Exception | None = None
    for provider in providers:
        try:
            url = PROVIDERS[provider](ref_path)
            hero["reference_url_hosted"] = url
            hero["reference_url_source"] = provider
            hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={url}")
            return 0
        except (urllib.error.URLError, RuntimeError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            last_error = exc
            print(f"WARN upload via {provider} failed: {exc}", file=sys.stderr)

    # --force upload failed: reuse existing hosted URL if byte-identical to local PNG.
    if args.force and existing and hosted_matches_local(existing, ref_path):
        print(
            f"OK reference_url_hosted={existing} (reused after --force upload fail; sha256 match)",
            file=sys.stderr,
        )
        print(f"OK reference_url_hosted={existing}")
        return 0

    print(f"❌ HERO BLOCKER: could not host reference: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
