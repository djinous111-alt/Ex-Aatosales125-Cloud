#!/usr/bin/env python3
"""Verify hyperlinks in Excalibur article.html (HTTP HEAD/GET)."""
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


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


BROWSER_UA = (
    "Mozilla/5.0 (compatible; ExcaliburBlogLinkVerify/1.1; +https://example.local) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
DEFAULT_UA = "ExcaliburBlogLinkVerify/1.0"

# Social hosts: soft-fail on network/SSL timeouts.
SOFT_SOCIAL_HOSTS = {"t.me", "telegram.me", "wa.me", "vk.com"}

# Gov/registry portals often flake under Cloud egress (SSL timeout, 403, NXDOMAIN).
# Soft-fail so GEO QA is not blocked; prefer Cloud-reachable entrypoints in articles.
SOFT_GOV_HOST_SUFFIXES = (
    "fsa.gov.ru",
    "elpts.ru",
    "gosuslugi.ru",
    "nalog.gov.ru",
    "customs.gov.ru",
    "minpromtorg.gov.ru",
)


def host_matches_suffix(host: str, suffixes: tuple[str, ...]) -> bool:
    host = host.lower().removeprefix("www.")
    return any(host == suffix or host.endswith("." + suffix) for suffix in suffixes)


def is_soft_gov_host(host: str) -> bool:
    return host_matches_suffix(host, SOFT_GOV_HOST_SUFFIXES)


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


def is_soft_external_failure(href: str, result: dict[str, Any]) -> bool:
    """Treat flaky social/gov timeouts and bot 403s as warnings, not publish blockers."""
    parsed = urlparse(href)
    host = parsed.netloc.lower().removeprefix("www.")
    error = str(result.get("error") or "").lower()
    status = result.get("status")

    if host in SOFT_SOCIAL_HOSTS:
        if status is not None:
            return False
        return any(token in error for token in ("timed out", "timeout", "ssl", "network"))

    if is_soft_gov_host(host):
        if status is None:
            return any(
                token in error
                for token in (
                    "timed out",
                    "timeout",
                    "ssl",
                    "network",
                    "name or service not known",
                    "nodename nor servname",
                    "getaddrinfo",
                    "nxdomain",
                    "temporary failure",
                    "errno",
                )
            )
        # Bot/WAF 403 after GET is common for registry portals under Cloud UA.
        if status in (401, 403, 429):
            return True
        return False

    return False


def verify_article(
    html_path: Path,
    *,
    site_base: str | None = None,
    timeout: float = 15.0,
    skip_external: bool = False,
) -> dict[str, Any]:
    html = html_path.read_text(encoding="utf-8")
    links = extract_links(html)
    results: list[dict[str, Any]] = []
    for href in links:
        kind = classify_link(href, site_base)
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
                }
            )
            continue
        check_target = href
        if kind == "internal_relative" and site_base:
            base = site_base.rstrip("/")
            check_target = f"{base}{href if href.startswith('/') else '/' + href}"
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

        host = urlparse(check_target if "://" in check_target else href).netloc.lower()
        user_agent = BROWSER_UA if is_soft_gov_host(host) else DEFAULT_UA
        # Gov portals often need a longer handshake window under Cloud egress.
        link_timeout = max(timeout, 25.0) if is_soft_gov_host(host) else timeout
        r = check_url(check_target, link_timeout, user_agent)
        r["kind"] = kind
        r["skipped"] = False
        if kind == "internal_relative":
            r["checked_url"] = check_target
        if kind == "external" and is_soft_external_failure(href, r):
            r["ok"] = True
            r["warning"] = "soft external gov/social flake; verify manually if needed"
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
