#!/usr/bin/env python3
"""Tiny JSONC helpers for Excalibur BLOG artifacts.

Cursor secret-scan may block commits when public brand URLs equal Cloud Secret
values (PUBLIC_SITE_URL, CATALOG_URL, TELEGRAM_URL, MAX_URL). Agents may keep
those URLs in committed files by appending trailing
`// pragma: allowlist secret` (JSONC) or `<!-- // pragma: allowlist secret -->`
(HTML/markdown). Strip pragmas before treating content as strict JSON / WP meta.
"""
from __future__ import annotations

import json
import re
from typing import Any

JSONC_ALLOWLIST_PRAGMA_RE = re.compile(r"[ \t]*// pragma: allowlist secret")
HTML_ALLOWLIST_PRAGMA_RE = re.compile(
    r"[ \t]*<!--\s*//\s*pragma:\s*allowlist\s+secret\s*-->",
    flags=re.I,
)


def strip_allowlist_pragmas(text: str) -> str:
    """Remove trailing secret-scan allowlist pragmas from JSONC/HTML text."""
    cleaned = JSONC_ALLOWLIST_PRAGMA_RE.sub("", text)
    cleaned = HTML_ALLOWLIST_PRAGMA_RE.sub("", cleaned)
    return cleaned.strip()


def jsonc_loads(text: str) -> Any:
    """Parse JSON that may contain trailing allowlist pragmas on URL lines."""
    return json.loads(strip_allowlist_pragmas(text))
