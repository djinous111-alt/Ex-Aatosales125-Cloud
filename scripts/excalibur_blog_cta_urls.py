#!/usr/bin/env python3
"""Commit-safe CTA/site URL redact + publish/QA reinject helpers.

Contract:
- In git artifacts use placeholders, never live PUBLIC_SITE_URL / CATALOG_URL /
  TELEGRAM_URL / MAX_URL values (secret-scan).
- Prefer typed placeholders: [REDACTED:PUBLIC_SITE_URL], [REDACTED:CATALOG_URL], …
- Plain [REDACTED] means site base (PUBLIC_SITE_URL / WP_HOME / WP_SITE_URL).
- Publish and GEO QA reinject from env before link-verify / WP upload; redact again
  before commit if needed.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

PLACEHOLDER = "[REDACTED]"
TYPED_PREFIX = "[REDACTED:"
SECRET_URL_ENV_KEYS = (
    "PUBLIC_SITE_URL",
    "CATALOG_URL",
    "TELEGRAM_URL",
    "MAX_URL",
    "WP_HOME",
    "WP_SITE_URL",
)
SITE_BASE_KEYS = ("PUBLIC_SITE_URL", "WP_HOME", "WP_SITE_URL")


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _read_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


def load_cta_env(root: Path | None = None) -> dict[str, str]:
    root = root or project_root()
    env = _read_env_file(root / "memory/site.env.local")
    for key in SECRET_URL_ENV_KEYS:
        value = os.environ.get(key)
        if value:
            env[key] = value.strip()
    return env


def site_base_url(env: dict[str, str]) -> str:
    for key in SITE_BASE_KEYS:
        value = (env.get(key) or "").strip().rstrip("/")
        if value:
            return value
    return ""


def typed_placeholder(key: str) -> str:
    return f"{TYPED_PREFIX}{key}]"


def _url_variants(url: str) -> list[str]:
    url = url.strip()
    if not url:
        return []
    variants = {url, url.rstrip("/")}
    if not url.endswith("/"):
        variants.add(url + "/")
    return sorted(variants, key=len, reverse=True)


def redact_text(text: str, env: dict[str, str] | None = None) -> str:
    """Replace live secret URL values with typed placeholders (then plain site base).

    When a variant ends with `/`, keep a slash after the placeholder so
    `https://host/wp-content/...` becomes `[REDACTED]/wp-content/...`, not
    `[REDACTED]wp-content/...`.
    """
    env = env or load_cta_env()
    out = text
    for key in SECRET_URL_ENV_KEYS:
        raw = (env.get(key) or "").strip()
        if not raw or raw == PLACEHOLDER or raw.startswith(TYPED_PREFIX):
            continue
        token = typed_placeholder(key)
        for variant in _url_variants(raw):
            replacement = token + "/" if variant.endswith("/") else token
            out = out.replace(variant, replacement)
    # Collapse site-base typed keys to plain [REDACTED] for shorter HTML (optional hygiene)
    for key in SITE_BASE_KEYS:
        out = out.replace(typed_placeholder(key), PLACEHOLDER)
    # De-dupe accidental double slashes after collapse: [REDACTED]//path → [REDACTED]/path
    out = out.replace(PLACEHOLDER + "//", PLACEHOLDER + "/")
    return out


def reinject_text(text: str, env: dict[str, str] | None = None) -> str:
    """Expand typed and plain placeholders using env URLs."""
    env = env or load_cta_env()
    out = text
    for key in SECRET_URL_ENV_KEYS:
        raw = (env.get(key) or "").strip().rstrip("/")
        if not raw:
            continue
        out = out.replace(typed_placeholder(key), raw)
    base = site_base_url(env)
    if base:
        # Plain [REDACTED] /path → https://site/path ; bare [REDACTED] → site base
        out = re.sub(
            re.escape(PLACEHOLDER) + r"(?=/)",
            base,
            out,
        )
        out = out.replace(PLACEHOLDER, base)
    return out


def process_file(path: Path, *, mode: str, env: dict[str, str], write: bool) -> str:
    original = path.read_text(encoding="utf-8")
    updated = redact_text(original, env) if mode == "redact" else reinject_text(original, env)
    if write and updated != original:
        path.write_text(updated, encoding="utf-8")
    return updated


def main() -> int:
    ap = argparse.ArgumentParser(description="Redact or reinject CTA/site URLs")
    ap.add_argument("paths", nargs="+", type=Path, help="Files to process")
    ap.add_argument("--redact", action="store_true", help="Replace live env URLs with placeholders")
    ap.add_argument("--reinject", action="store_true", help="Expand placeholders from env")
    ap.add_argument("--write", action="store_true", help="Write changes in place")
    ap.add_argument("--dry-run", action="store_true", help="Print whether file would change")
    args = ap.parse_args()
    if args.redact == args.reinject:
        print("Specify exactly one of --redact or --reinject", file=sys.stderr)
        return 2
    mode = "redact" if args.redact else "reinject"
    root = project_root()
    env = load_cta_env(root)
    missing = [k for k in ("PUBLIC_SITE_URL", "CATALOG_URL", "TELEGRAM_URL") if not (env.get(k) or "").strip()]
    if mode == "reinject" and not site_base_url(env):
        print("BLOCKER: PUBLIC_SITE_URL (or WP_HOME/WP_SITE_URL) required for reinject", file=sys.stderr)
        return 1
    if missing and mode == "reinject":
        print(f"WARN: missing optional CTA env: {', '.join(missing)}", file=sys.stderr)

    rc = 0
    for rel in args.paths:
        path = rel if rel.is_absolute() else root / rel
        if not path.is_file():
            print(f"FAIL missing file: {path}", file=sys.stderr)
            rc = 1
            continue
        original = path.read_text(encoding="utf-8")
        updated = process_file(path, mode=mode, env=env, write=args.write and not args.dry_run)
        changed = updated != original
        status = "CHANGED" if changed else "OK"
        print(f"{status} {mode} {path.relative_to(root) if root in path.parents else path}")
        if args.dry_run and changed:
            print(f"  would_write={args.write}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
