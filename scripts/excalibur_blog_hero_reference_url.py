#!/usr/bin/env python3
"""Ensure blog hero reference has a public HTTPS URL for gpt-image-2 / Kie input_urls."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_KIE_UPLOAD_URL = "https://kieai.redpandaai.co/api/file-base64-upload"
DEFAULT_API_KEY_ENV = "KIE_API_KEY"


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_https_url(url: str) -> str:
    """Plain http:// media URLs often break Kie i2i createTask fetch."""
    text = (url or "").strip()
    if text.startswith("http://"):
        return "https://" + text[len("http://") :]
    return text


def upload_catbox(image_path: Path) -> str:
    boundary = "----ExcaliburHeroBoundary"
    body_prefix = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="reqtype"\r\n\r\n'
        f"fileupload\r\n"
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="fileToUpload"; filename="{image_path.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8")
    body_suffix = f"\r\n--{boundary}--\r\n".encode("utf-8")
    file_bytes = image_path.read_bytes()
    body = body_prefix + file_bytes + body_suffix

    request = urllib.request.Request(
        "https://catbox.moe/user/api.php",
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "ExcaliburBlogHero/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        url = response.read().decode("utf-8", errors="replace").strip()
    if not url.startswith("https://"):
        raise RuntimeError(f"catbox upload failed: {url[:200]}")
    return url


def upload_0x0(image_path: Path) -> str:
    boundary = "----ExcaliburHero0x0"
    body_prefix = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{image_path.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8")
    body_suffix = f"\r\n--{boundary}--\r\n".encode("utf-8")
    body = body_prefix + image_path.read_bytes() + body_suffix
    request = urllib.request.Request(
        "https://0x0.st",
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "ExcaliburBlogHero/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        url = response.read().decode("utf-8", errors="replace").strip()
    if not url.startswith("https://"):
        raise RuntimeError(f"0x0 upload failed: {url[:200]}")
    return url


def upload_kie_base64(image_path: Path) -> str:
    """Kie tempfile host when catbox/0x0/WP media fetch fail from Cloud egress."""
    api_key = (os.environ.get(DEFAULT_API_KEY_ENV) or "").strip()
    if not api_key:
        raise RuntimeError(f"{DEFAULT_API_KEY_ENV} not set for kie file-base64-upload")

    raw = image_path.read_bytes()
    b64 = base64.b64encode(raw).decode("ascii")
    payload = {
        "base64Data": f"data:image/png;base64,{b64}",
        "uploadPath": "excalibur/blog-hero",
        "fileName": image_path.name or "blog-hero-reference.png",
    }
    endpoint = (os.environ.get("KIE_FILE_UPLOAD_URL") or DEFAULT_KIE_UPLOAD_URL).strip()
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "ExcaliburBlogHero/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        body = json.loads(response.read().decode("utf-8", errors="replace"))
    data = body.get("data") if isinstance(body, dict) else None
    url = ""
    if isinstance(data, dict):
        url = str(data.get("downloadUrl") or data.get("url") or "").strip()
    if not url and isinstance(body, dict):
        url = str(body.get("downloadUrl") or body.get("url") or "").strip()
    url = normalize_https_url(url)
    if not url.startswith("https://"):
        msg = ""
        if isinstance(body, dict):
            msg = str(body.get("msg") or body.get("message") or "")[:200]
        raise RuntimeError(f"kie file-base64-upload failed: {msg or 'no downloadUrl'}")
    return url


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
        choices=("catbox", "0x0", "kie", "auto"),
        default="auto",
        help="auto = catbox → 0x0 → kie file-base64-upload",
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

    existing = normalize_https_url((hero.get("reference_url_hosted") or "").strip())
    if existing and existing != (hero.get("reference_url_hosted") or "").strip():
        hero["reference_url_hosted"] = existing
        hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        save_json(hero_path, hero)
        print("WARN upgraded reference_url_hosted http→https", file=sys.stderr)
    if existing and not args.force:
        if not existing.startswith("https://"):
            print(f"❌ HERO BLOCKER: reference_url_hosted must be HTTPS, got: {existing}", file=sys.stderr)
            return 1
        print(f"OK reference_url_hosted={existing}")
        return 0

    env_url = normalize_https_url(os.environ.get("BLOG_HERO_REFERENCE_URL", "").strip())
    if env_url:
        if not env_url.startswith("https://"):
            print(f"❌ HERO BLOCKER: BLOG_HERO_REFERENCE_URL must be HTTPS, got: {env_url}", file=sys.stderr)
            return 1
        hero["reference_url_hosted"] = env_url
        hero["reference_url_source"] = "env:BLOG_HERO_REFERENCE_URL"
        hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        save_json(hero_path, hero)
        print(f"OK reference_url_hosted={env_url}")
        return 0

    if args.provider == "auto":
        providers = ["catbox", "0x0", "kie"]
    else:
        providers = [args.provider]

    uploaders = {
        "catbox": upload_catbox,
        "0x0": upload_0x0,
        "kie": upload_kie_base64,
    }
    last_error: Exception | None = None
    for provider in providers:
        try:
            url = normalize_https_url(uploaders[provider](ref_path))
            if not url.startswith("https://"):
                raise RuntimeError(f"{provider} returned non-HTTPS URL")
            hero["reference_url_hosted"] = url
            hero["reference_url_source"] = provider if provider != "kie" else "kie-file-base64-upload"
            hero["reference_url_updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            save_json(hero_path, hero)
            print(f"OK reference_url_hosted={url}")
            return 0
        except (urllib.error.URLError, RuntimeError, TimeoutError, json.JSONDecodeError, KeyError) as exc:
            last_error = exc
            print(f"WARN upload via {provider} failed: {exc}", file=sys.stderr)

    print(f"❌ HERO BLOCKER: could not host reference: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
