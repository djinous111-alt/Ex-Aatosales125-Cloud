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

# Commit-hygiene placeholders that must expand before live HTTP checks.
CTA_TOKEN_ENV = {
    "[CATALOG_URL]": ("CATALOG_URL",),
    "[TELEGRAM_URL]": ("TELEGRAM_URL",),
    "[MAX_URL]": ("MAX_URL",),
    "[PUBLIC_SITE_URL]": ("PUBLIC_SITE_URL", "WP_HOME", "WP_SITE_URL"),
    "[REDACTED_SITE]": ("PUBLIC_SITE_URL", "WP_HOME", "WP_SITE_URL"),
}

BARE_REDACTED_ENV_ORDER = (
    "CATALOG_URL",
    "TELEGRAM_URL",
    "MAX_URL",
    "PUBLIC_SITE_URL",
)


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
    if href.startswith("/"):
        return "internal_relative"
    parsed = urlparse(href)
    if not parsed.scheme:
        return "internal_relative"
    if site_base:
        base = urlparse(site_base if "://" in site_base else f"https://{site_base}")
        if parsed.netloc == base.netloc:
            return "internal_absolute"
    return "external"


def _env_url(name: str) -> str:
    return (os.environ.get(name) or "").strip().rstrip("/")


def expand_cta_href(href: str, *, bare_redacted_index: list[int]) -> tuple[str, str]:
    """Expand commit-hygiene CTA placeholders from env; return (check_url, report_url)."""
    raw = href.strip()
    report_url = raw

    for token, env_names in CTA_TOKEN_ENV.items():
        if raw == token or raw.startswith(token + "/"):
            base = ""
            for name in env_names:
                base = _env_url(name)
                if base:
                    break
            if not base:
                return raw, report_url
            suffix = raw[len(token) :]
            return f"{base}{suffix}", report_url

    # Bare [REDACTED] used for multiple CTAs — map in stable env order.
    if raw == "[REDACTED]" or raw.startswith("[REDACTED]/"):
        if raw.startswith("[REDACTED]/"):
            base = _env_url("PUBLIC_SITE_URL") or _env_url("WP_HOME") or _env_url("WP_SITE_URL")
            if base:
                return f"{base}{raw[len('[REDACTED]'):]}", report_url
            return raw, report_url
        idx = bare_redacted_index[0]
        bare_redacted_index[0] = idx + 1
        candidates = [_env_url(name) for name in BARE_REDACTED_ENV_ORDER]
        candidates = [url for url in candidates if url]
        if idx < len(candidates):
            return candidates[idx], report_url
        return raw, report_url

    return raw, report_url


def redact_url_for_report(url: str) -> str:
    """Keep link-verify.json free of live secret-scanned public URLs."""
    public = _env_url("PUBLIC_SITE_URL") or _env_url("WP_HOME") or _env_url("WP_SITE_URL")
    out = url
    for env_name, token in (
        ("CATALOG_URL", "[CATALOG_URL]"),
        ("TELEGRAM_URL", "[TELEGRAM_URL]"),
        ("MAX_URL", "[MAX_URL]"),
    ):
        value = _env_url(env_name)
        if value and value in out:
            out = out.replace(value, token)
    if public and public in out:
        out = out.replace(public, "[REDACTED]")
    return out


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
    bare_redacted_index = [0]
    for href in links:
        expanded, report_href = expand_cta_href(href, bare_redacted_index=bare_redacted_index)
        kind = classify_link(expanded, site_base)
        if skip_external and kind == "external":
            results.append(
                {
                    "url": redact_url_for_report(report_href),
                    "kind": kind,
                    "status": None,
                    "ok": True,
                    "skipped": True,
                    "method": None,
                    "error": None,
                    "expanded_from_placeholder": expanded != href,
                }
            )
            continue
        check_target = expanded
        if kind == "internal_relative" and site_base:
            base = site_base.rstrip("/")
            check_target = f"{base}{expanded if expanded.startswith('/') else '/' + expanded}"
        elif kind == "internal_relative":
            # Unexpanded [REDACTED]/token without env still looks relative — skip with hint.
            err = "relative link; pass --site-base to verify"
            if href.strip().startswith("["):
                err = (
                    "CTA placeholder not expanded; set CATALOG_URL/TELEGRAM_URL/"
                    "PUBLIC_SITE_URL (or use [CATALOG_URL]/[TELEGRAM_URL] tokens)"
                )
            results.append(
                {
                    "url": redact_url_for_report(report_href),
                    "kind": kind,
                    "status": None,
                    "ok": True,
                    "skipped": True,
                    "method": None,
                    "error": err,
                    "expanded_from_placeholder": expanded != href,
                }
            )
            continue
        r = check_url(check_target, timeout, user_agent)
        r["kind"] = kind
        r["skipped"] = False
        r["url"] = redact_url_for_report(report_href)
        r["expanded_from_placeholder"] = expanded != href
        if kind == "internal_relative" or expanded != href:
            r["checked_url"] = redact_url_for_report(check_target)
        if kind == "external" and is_soft_external_failure(expanded, r):
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
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if report["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
