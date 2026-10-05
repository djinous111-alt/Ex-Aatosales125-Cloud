#!/usr/bin/env python3
"""Validate schema.jsonld: no [REDACTED]/env tokens; URL keys must be https (or expandable)."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


REDACTED_RE = re.compile(r"\[REDACTED\]", re.I)
ENV_TOKEN_RE = re.compile(r"\[([A-Z][A-Z0-9_]*)\]")
URL_KEYS = {"url", "@id", "sameas", "image", "logo", "contenturl", "thumbnailurl"}
ENV_ALIASES = {
    "PUBLIC_SITE_URL": ("PUBLIC_SITE_URL", "WP_SITE_URL", "WP_HOME"),
    "CATALOG_URL": ("CATALOG_URL", "PUBLIC_CATALOG_URL"),
    "TELEGRAM_URL": ("TELEGRAM_URL", "PUBLIC_TELEGRAM_URL"),
    "MAX_URL": ("MAX_URL", "PUBLIC_MAX_URL"),
}


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def env_value(token: str) -> str:
    for name in ENV_ALIASES.get(token, (token,)):
        value = (os.environ.get(name) or "").strip()
        if value:
            return value.rstrip("/")
    return ""


def expand_env_tokens(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []

    def repl(match: re.Match[str]) -> str:
        token = match.group(1)
        value = env_value(token)
        if not value:
            notes.append(f"missing env for [{token}]")
            return match.group(0)
        notes.append(f"expanded [{token}]")
        return value

    return ENV_TOKEN_RE.sub(repl, text), notes


def walk(node: Any, key: str | None = None, path: str = "$") -> list[tuple[str, str | None, str]]:
    found: list[tuple[str, str | None, str]] = []
    if isinstance(node, dict):
        for child_key, value in node.items():
            found.extend(walk(value, child_key, f"{path}.{child_key}"))
    elif isinstance(node, list):
        for idx, value in enumerate(node):
            found.extend(walk(value, key, f"{path}[{idx}]"))
    elif isinstance(node, str):
        found.append((path, key, node))
    return found


def validate_schema(data: Any) -> list[str]:
    errors: list[str] = []
    for path, key, value in walk(data):
        if REDACTED_RE.search(value):
            errors.append(f"{path}: contains [REDACTED] literal")
            continue
        if ENV_TOKEN_RE.search(value):
            errors.append(f"{path}: contains unresolved env token (use real https or --expand-env)")
            continue
        key_l = (key or "").lower()
        if key_l not in URL_KEYS:
            continue
        if not value:
            errors.append(f"{path}: empty URL field")
            continue
        # relative asset paths (pre-publish cover) are allowed for image/logo only
        if key_l in {"image", "logo"} and "://" not in value and not value.startswith("["):
            continue
        if value.startswith(("#",)):
            continue
        if not value.startswith(("http://", "https://")):
            errors.append(f"{path}: expected http(s) URL")
    return errors


def load_schema_text(text: str) -> Any:
    cleaned = re.sub(r"[ \t]*// pragma: allowlist secret", "", text)
    return json.loads(cleaned)


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate schema.jsonld for REDACTED / URL hygiene")
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument(
        "--expand-env",
        action="store_true",
        help="Expand [PUBLIC_SITE_URL]/[CATALOG_URL]/… from env before validate (diagnostics)",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    path = article_dir / "schema.jsonld"
    if not path.is_file():
        print(f"ERROR: missing {path}", file=sys.stderr)
        return 1

    raw = path.read_text(encoding="utf-8")
    if args.expand_env:
        raw, notes = expand_env_tokens(raw)
        for note in notes:
            print(f"NOTE: {note}")

    try:
        data = load_schema_text(raw)
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON-LD: {exc}", file=sys.stderr)
        return 1

    errors = validate_schema(data)
    if errors:
        print("Schema validate: FAIL")
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print("Schema validate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
