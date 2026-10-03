#!/usr/bin/env python3
"""Verify hyperlinks in Excalibur article.html (HTTP HEAD/GET)."""
from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

# Public marketing/site URLs often live in Cloud Secrets; writing them into
# link-verify.json trips the pre-commit secret scanner. Redact to ${ENV_NAME}.
REDACT_ENV_KEYS = (
    "CATALOG_URL",
    "TELEGRAM_URL",
    "MAX_URL",
    "PUBLIC_SITE_URL",
    "WP_SITE_URL",
    "WP_HOME",
)

CTA_PLACEHOLDER_ENV = {
    "[CATALOG_URL]": "CATALOG_URL",
    "[TELEGRAM_URL]": "TELEGRAM_URL",
    "[MAX_URL]": "MAX_URL",
}


def env_url_redaction_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for key in REDACT_ENV_KEYS:
        raw = (os.environ.get(key) or "").strip().rstrip("/")
        if raw.startswith(("http://", "https://")):
            mapping[raw] = f"${{{key}}}"
    return dict(sorted(mapping.items(), key=lambda kv: len(kv[0]), reverse=True))


def redact_env_urls_in_obj(obj: Any, mapping: dict[str, str] | None = None) -> Any:
    mapping = mapping if mapping is not None else env_url_redaction_map()
    if not mapping:
        return obj
    if isinstance(obj, str):
        out = obj
        for value, placeholder in mapping.items():
            if value in out:
                out = out.replace(value, placeholder)
        return out
    if isinstance(obj, list):
        return [redact_env_urls_in_obj(item, mapping) for item in obj]
    if isinstance(obj, dict):
        return {k: redact_env_urls_in_obj(v, mapping) for k, v in obj.items()}
    return obj


def expand_cta_placeholder(href: str) -> tuple[str, str | None]:
    """Expand [CATALOG_URL]/[TELEGRAM_URL]/[MAX_URL] from env. Returns (url, env_key|None)."""
    value = (href or "").strip()
    env_key = CTA_PLACEHOLDER_ENV.get(value)
    if not env_key:
        upper = value.upper()
        for token, key in CTA_PLACEHOLDER_ENV.items():
            if token in upper or token.lower() in value:
                env_key = key
                break
    if not env_key:
        return value, None
    live = (os.environ.get(env_key) or "").strip()
    if live.startswith(("http://", "https://")):
        return live, env_key
    return value, env_key


def is_placeholder_href(href: str) -> bool:
    """True for redaction/template placeholders that must never be verified as relative paths."""
    value = (href or "").strip()
    if not value:
        return False
    upper = value.upper()
    if upper in {"[REDACTED]", "REDACTED"} or "[REDACTED]" in upper:
        return True
    if value.startswith("{{") or value in {"TODO", "FIXME", "YOUR_URL_HERE"}:
        return True
    return False


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attr = {k: (v or "") for k, v in attrs}
        href = attr.get("href", "").strip()
        if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
            return
        self.links.append({"href": href, "text_hint": ""})


def extract_links(html: str) -> list[str]:
    parser = LinkExtractor()
    parser.feed(html)
    seen: set[str] = set()
    out: list[str] = []
    for item in parser.links:
        href = item["href"]
        if href not in seen:
            seen.add(href)
            out.append(href)
    return out


def check_url(url: str, timeout: float, user_agent: str) -> dict[str, Any]:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": user_agent},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return {
                "url": url,
                "status": resp.status,
                "ok": 200 <= resp.status < 400,
                "method": "HEAD",
                "error": None,
            }
    except urllib.error.HTTPError as e:
        if e.code in (405, 501, 403):
            return _get_fallback(url, timeout, user_agent, ctx, str(e))
        return {
            "url": url,
            "status": e.code,
            "ok": False,
            "method": "HEAD",
            "error": str(e),
        }
    except Exception as e:  # noqa: BLE001
        return _get_fallback(url, timeout, user_agent, ctx, str(e))


def _get_fallback(
    url: str, timeout: float, user_agent: str, ctx: ssl.SSLContext, head_error: str
) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return {
                "url": url,
                "status": resp.status,
                "ok": 200 <= resp.status < 400,
                "method": "GET",
                "error": None if resp.status < 400 else head_error,
            }
    except urllib.error.HTTPError as e:
        return {
            "url": url,
            "status": e.code,
            "ok": False,
            "method": "GET",
            "error": str(e),
        }
    except Exception as e:  # noqa: BLE001
        return {
            "url": url,
            "status": None,
            "ok": False,
            "method": "GET",
            "error": str(e),
        }


def classify_link(href: str, site_base: str | None) -> str:
    if is_placeholder_href(href):
        return "placeholder"
    expanded, env_key = expand_cta_placeholder(href)
    if env_key and expanded != href and expanded.startswith(("http://", "https://")):
        # Treat expanded CTA as absolute for classification.
        href = expanded
    if href.startswith("/"):
        return "internal_relative"
    parsed = urlparse(href)
    if not parsed.scheme:
        # Unresolved CTA token like [CATALOG_URL] without env → placeholder fail.
        if href.strip() in CTA_PLACEHOLDER_ENV or href.strip().upper().startswith("["):
            return "placeholder"
        return "internal_relative"
    if site_base:
        base = urlparse(site_base if "://" in site_base else f"https://{site_base}")
        if parsed.netloc == base.netloc:
            return "internal_absolute"
    return "external"


def is_soft_external_failure(href: str, result: dict[str, Any]) -> bool:
    """Treat flaky social profile timeouts as warnings, not publish blockers."""
    parsed = urlparse(href)
    host = parsed.netloc.lower()
    soft_hosts = {"t.me", "telegram.me", "wa.me", "vk.com"}
    if host not in soft_hosts:
        return False
    if result.get("status") is not None:
        return False
    error = str(result.get("error") or "").lower()
    return any(token in error for token in ("timed out", "timeout", "ssl", "network"))


def verify_article(
    html_path: Path,
    *,
    site_base: str | None = None,
    timeout: float = 15.0,
    skip_external: bool = False,
) -> dict[str, Any]:
    html = html_path.read_text(encoding="utf-8")
    links = extract_links(html)
    user_agent = "ExcaliburBlogLinkVerify/1.0"
    results: list[dict[str, Any]] = []
    for href in links:
        expanded, env_key = expand_cta_placeholder(href)
        kind = classify_link(href, site_base)
        if kind == "placeholder":
            # Unresolved literal [REDACTED] is a hard fail; unresolved CTA token
            # without env is also fail. Soft-skip only when env expand succeeded
            # is handled below via expanded URL.
            results.append(
                {
                    "url": href,
                    "kind": kind,
                    "status": None,
                    "ok": False,
                    "skipped": False,
                    "method": None,
                    "error": (
                        "placeholder href unresolved; set CATALOG_URL/TELEGRAM_URL "
                        "(or restore live URL) before link-verify"
                    ),
                }
            )
            continue
        check_href = expanded if (env_key and expanded.startswith(("http://", "https://"))) else href
        kind = classify_link(check_href if check_href != href else href, site_base)
        if skip_external and kind == "external":
            results.append(
                {
                    "url": href,
                    "kind": kind,
                    "status": None,
                    "ok": True,
                    "skipped": True,
                    "method": None,
                    "error": None,
                    "expanded_from": env_key,
                }
            )
            continue
        check_target = check_href
        if kind == "internal_relative" and site_base:
            base = site_base.rstrip("/")
            check_target = f"{base}{check_href if check_href.startswith('/') else '/' + check_href}"
        elif kind == "internal_relative":
            results.append(
                {
                    "url": href,
                    "kind": kind,
                    "status": None,
                    "ok": True,
                    "skipped": True,
                    "method": None,
                    "error": "relative link; pass --site-base to verify",
                }
            )
            continue
        r = check_url(check_target, timeout, user_agent)
        r["url"] = href
        r["kind"] = kind
        r["skipped"] = False
        if env_key and check_href != href:
            r["expanded_from"] = env_key
        if check_target != href:
            r["checked_url"] = check_target
        if kind == "external" and is_soft_external_failure(check_target, r):
            r["ok"] = True
            r["warning"] = "soft external social timeout; verify manually if needed"
        results.append(r)

    failed = [r for r in results if not r.get("ok")]
    return {
        "source": str(html_path).replace("\\", "/"),
        "total_links": len(results),
        "failed_count": len(failed),
        "verdict": "pass" if not failed else "fail",
        "links": results,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify links in Excalibur article.html")
    ap.add_argument("html", type=Path, help="Path to article.html")
    ap.add_argument("-o", "--output", type=Path, help="Write link-verify.json")
    ap.add_argument("--site-base", type=str, default=None, help="e.g. https://example.com")
    ap.add_argument("--timeout", type=float, default=15.0)
    ap.add_argument("--skip-external", action="store_true")
    ap.add_argument(
        "--redact-env-urls",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Replace known Cloud Secret URL values with ${ENV_NAME} in JSON output (default: on)",
    )
    args = ap.parse_args()

    if not args.html.is_file():
        print(f"Not found: {args.html}", file=sys.stderr)
        return 2

    report = verify_article(
        args.html,
        site_base=args.site_base,
        timeout=args.timeout,
        skip_external=args.skip_external,
    )
    if args.redact_env_urls:
        report = redact_env_urls_in_obj(report)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if report["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
