#!/usr/bin/env python3
"""Lightweight regression smoke for durable fixer invariants (no network/publish)."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


def root() -> Path:
    return Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    print(f"FAIL {msg}", file=sys.stderr)
    raise SystemExit(1)


def ok(msg: str) -> None:
    print(f"OK {msg}")


def main() -> int:
    r = root()

    # 1) Topic ID regex accepts AS* and B*
    today = (r / "scripts/excalibur_blog_today.py").read_text(encoding="utf-8")
    scout = (r / "scripts/excalibur_blog_scout_helper.py").read_text(encoding="utf-8")
    if "AS|B" not in today or "AS|B" not in scout:
        fail("today/scout_helper must accept AS|B topic IDs")
    ok("AS|B topic regex present in today+scout_helper")

    helper = subprocess.run(
        [sys.executable, str(r / "scripts/excalibur_blog_scout_helper.py"), "--suggest-next"],
        cwd=r,
        capture_output=True,
        text=True,
        check=False,
    )
    if helper.returncode != 0:
        fail(f"scout_helper --suggest-next exit {helper.returncode}: {helper.stderr}")
    if "Total topics in pool" not in helper.stdout:
        fail("scout_helper did not print pool summary")
    # Pool must see AS* cards when present on disk.
    topics = (r / "memory/topics/blog-topics.md").read_text(encoding="utf-8")
    if re.search(r"^##\s+AS\d+", topics, flags=re.M):
        if "Total topics in pool (blog-topics.md): 0" in helper.stdout:
            fail("scout_helper still reports 0 topics despite AS* cards")
        ok("scout_helper sees AS* topic pool")
    else:
        ok("no AS* cards in pool (skip pool>0 assert)")

    # 2) llms CLI has --blog-dir and --blog-path alias
    llms_help = subprocess.run(
        [sys.executable, str(r / "scripts/excalibur_blog_llms_generator.py"), "--help"],
        cwd=r,
        capture_output=True,
        text=True,
        check=False,
    )
    if "--blog-dir" not in llms_help.stdout:
        fail("llms generator missing --blog-dir")
    if "--blog-path" not in llms_help.stdout:
        fail("llms generator missing --blog-path alias")
    ok("llms generator --blog-dir + --blog-path")

    # 3) editorial markers pinned
    policy = json.loads((r / "memory/brief/editorial-policy.json").read_text(encoding="utf-8"))
    if not policy.get("_markers_pinned"):
        fail("_markers_pinned missing/false")
    if len(policy.get("pain_markers_ru") or []) < 5:
        fail("pain_markers_ru too short")
    if len(policy.get("outcome_markers_ru") or []) < 5:
        fail("outcome_markers_ru too short")
    ok("editorial-policy pain/outcome markers pinned")

    # 4) cover prompt must not hardcode white hoodie outfit lock
    prompt_src = (r / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
    if "Outfit lock: thick heavyweight white hoodie" in prompt_src:
        fail("cover prompt still hardcodes white hoodie outfit lock")
    ok("cover prompt has no fixed white-hoodie outfit lock")

    # 5) publish helpers: hydrate + redact + TCP probe
    pub = (r / "scripts/excalibur_blog_wp_publish.py").read_text(encoding="utf-8")
    for needle in (
        "def hydrate_env_placeholders",
        "def redact_public_site_url",
        "paramiko",
        "def ssh_host_tcp22_probe",
        "ssh_tcp22",
    ):
        if needle not in pub:
            fail(f"publish script missing {needle}")
    ok("publish hydrate/redact/TCP helpers present")

    cover = (r / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
    if "tempfile.redpandaai.co" not in cover:
        fail("cover_quad_prompt missing tempfile.redpandaai.co fallback host")
    ok("cover tempfile reference host allowed")

    split_src = (r / "scripts/excalibur_blog_cover_quad_split.py").read_text(encoding="utf-8")
    if "def apply_corner_brand_stamp" not in split_src or "avto-sales125.ru" not in split_src:
        fail("cover_quad_split missing post-split corner brand stamp")
    if "--no-corner-brand" not in split_src:
        fail("cover_quad_split missing --no-corner-brand flag")
    ok("cover_quad_split corner brand stamp present")

    notes = (r / "scripts/excalibur_blog_research_notes_gate.py").read_text(encoding="utf-8")
    if "_tech_marker_hit" not in notes or "notes_without_github_evidence" not in notes:
        fail("research_notes_gate missing token-boundary tech marker helpers")
    ok("research_notes_gate tech marker boundaries")

    hv = (r / "scripts/excalibur_blog_human_voice_gate.py").read_text(encoding="utf-8")
    if "быстрый инсайт" not in hv or "TL;DR" not in hv:
        fail("human_voice missing TL;DR insight ban")
    ok("human_voice TL;DR ban present")

    lv = (r / "scripts/excalibur_blog_link_verify.py").read_text(encoding="utf-8")
    for needle in ("catalog_ssl", "site_ssl", "def classify_soft_pass", "def redact_report_urls"):
        if needle not in lv:
            fail(f"link_verify missing {needle}")
    ok("link_verify catalog/site soft-pass pinned")

    if not (r / "scripts/excalibur_git.sh").is_file():
        fail("scripts/excalibur_git.sh missing")
    if not (r / "scripts/excalibur_blog_filter_commit_secret_env.sh").is_file():
        fail("filter_commit_secret_env.sh missing")
    ok("excalibur_git.sh + secret-name filter present")

    # 6) unit-ish hydrate/redact without network
    sys.path.insert(0, str(r / "scripts"))
    import excalibur_blog_wp_publish as pubmod  # noqa: E402

    hydrated = pubmod.hydrate_env_placeholders(
        '{"url":"${PUBLIC_SITE_URL}/x","cta":"${CATALOG_URL|TELEGRAM_URL}"}',
        {"PUBLIC_SITE_URL": "https://example.test", "CATALOG_URL": "https://catalog.test"},
    )
    if "https://example.test/x" not in hydrated or "https://catalog.test" not in hydrated:
        fail(f"hydrate failed: {hydrated}")
    redacted = pubmod.redact_public_site_url(
        "https://example.test/2026/07/18/slug/",
        "https://example.test",
    )
    if redacted != "${PUBLIC_SITE_URL}/2026/07/18/slug/":
        fail(f"redact failed: {redacted}")
    ok("publish hydrate+redact unit checks")

    print("SUMMARY smoke PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
