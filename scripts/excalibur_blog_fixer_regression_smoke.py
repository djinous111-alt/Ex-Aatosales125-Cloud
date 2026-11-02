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
    topics = (r / "memory/topics/blog-topics.md").read_text(encoding="utf-8")
    if re.search(r"^##\s+AS\d+", topics, flags=re.M):
        if "Total topics in pool (blog-topics.md): 0" in helper.stdout:
            fail("scout_helper still reports 0 topics despite AS* cards")
        if not re.search(r"Next available topic ID: AS\d+", helper.stdout):
            fail("scout_helper should suggest next AS* id when AS pool exists")
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

    # 4) cover corner brand + kie hero rehost
    split = (r / "scripts/excalibur_blog_cover_quad_split.py").read_text(encoding="utf-8")
    if "stamp_corner_brand" not in split and "ensure_corner_brand" not in split:
        fail("cover quad split missing corner brand stamp")
    ok("cover corner brand stamp present")

    kie = (r / "scripts/excalibur_blog_kie_gpt_image2_api.py").read_text(encoding="utf-8")
    if "file-base64-upload" not in kie or "ensure_reachable_input_urls" not in kie:
        fail("kie api missing local hero file-base64 rehost")
    ok("kie hero file-base64 rehost present")

    # 5) link-verify catalog soft-pass + publish DNS probe
    link = (r / "scripts/excalibur_blog_link_verify.py").read_text(encoding="utf-8")
    if "catalog_dns" not in link or "CATALOG_HOST_SUFFIXES" not in link:
        fail("link-verify missing catalog_dns soft-pass")
    ok("link-verify catalog_dns soft-pass present")

    pub = (r / "scripts/excalibur_blog_wp_publish.py").read_text(encoding="utf-8")
    for needle in ("probe_ssh_dns", "probe_ssh_tcp22", "SSH_HOST_IP", "paramiko", "ssh_tcp22_timeout"):
        if needle not in pub:
            fail(f"publish script missing {needle}")
    ok("publish SSH DNS + TCP/22 probe + SSH_HOST_IP + paramiko present")

    # 6) research gate counts table rows under pain_solution_map
    gate = (r / "scripts/excalibur_blog_research_notes_gate.py").read_text(encoding="utf-8")
    if "pain_section" not in gate and r"pain[_\s-]*solution" not in gate:
        fail("research-notes gate missing pain_solution_map section parse")
    ok("research-notes gate pain_solution_map row counter present")

    # 7) git secret-name filter wrapper
    if not (r / "scripts/excalibur_git.sh").is_file():
        fail("scripts/excalibur_git.sh missing")
    if not (r / "scripts/excalibur_blog_filter_commit_secret_env.sh").is_file():
        fail("scripts/excalibur_blog_filter_commit_secret_env.sh missing")
    ok("excalibur_git secret-name filter present")

    # 8) unit: probe_ssh_dns without network secrets
    sys.path.insert(0, str(r / "scripts"))
    import excalibur_blog_wp_publish as pubmod  # noqa: E402

    dns_missing = pubmod.probe_ssh_dns({})
    if dns_missing.get("blocker") != "missing_ssh_host":
        fail(f"probe_ssh_dns empty host unexpected: {dns_missing}")
    dns_ip = pubmod.probe_ssh_dns({"SSH_HOST": "example.invalid", "SSH_HOST_IP": "203.0.113.10"})
    if not dns_ip.get("resolved") or dns_ip.get("resolver") != "SSH_HOST_IP":
        fail(f"probe_ssh_dns SSH_HOST_IP override failed: {dns_ip}")
    ok("publish probe_ssh_dns unit checks")

    tcp_skip = pubmod.probe_ssh_tcp22({}, dns_missing)
    if tcp_skip.get("blocker") != "ssh_dns_unresolved":
        fail(f"probe_ssh_tcp22 should skip when DNS unresolved: {tcp_skip}")
    ok("publish probe_ssh_tcp22 unit checks")

    # 9) utility gate skips empty marker lists
    util = (r / "scripts/excalibur_blog_utility_gate.py").read_text(encoding="utf-8")
    if "if pain_markers and pain_count" not in util:
        fail("utility gate must skip empty pain_markers_ru")
    ok("utility gate empty-marker fail-soft present")

    # 10) cover prompt allows Kie tempfile hosts
    cover_prompt = (r / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
    if "ALLOWED_REFERENCE_HOST_SUFFIXES" not in cover_prompt or "redpandaai.co" not in cover_prompt:
        fail("cover prompt must allow Kie tempfile reference hosts")
    ok("cover prompt allows Kie tempfile hosts")

    print("SUMMARY smoke PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
