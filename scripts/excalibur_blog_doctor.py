#!/usr/bin/env python3
"""Preflight checks for Excalibur BLOG pipeline."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def check(condition: bool, label: str, errors: list[str], warnings: list[str], *, warn: bool = False) -> None:
    if condition:
        print(f"OK {label}")
        return
    if warn:
        warnings.append(label)
        print(f"WARN {label}")
    else:
        errors.append(label)
        print(f"FAIL {label}")


def module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def read_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


def merged_publish_env(root: Path) -> dict[str, str]:
    keys = {
        "PUBLIC_SITE_URL",
        "WP_HOME",
        "WP_SITE_URL",
        "SSH_HOST",
        "SSH_PORT",
        "SSH_USER",
        "SSH_PASS",
        "SSH_PASSWORD",
        "SSH_ROOT",
        "EXCALIBUR_BLOG_ALLOW_PUBLISH",
    }
    env = read_env_file(root / "memory/site.env.local")
    for key in keys:
        value = os.environ.get(key)
        if value:
            env[key] = value
    if not env.get("SSH_PASS") and env.get("SSH_PASSWORD"):
        env["SSH_PASS"] = env["SSH_PASSWORD"]
    return env


def git_ls_files(root: Path, pathspec: str) -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", pathspec],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return []
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Excalibur BLOG preflight doctor")
    parser.add_argument("--publish", action="store_true", help="Require publish credentials and allow flag")
    args = parser.parse_args()

    root = project_root()
    errors: list[str] = []
    warnings: list[str] = []

    print(f"EXCALIBUR_ROOT={root}")

    check((root / "AGENTS.md").is_file(), "AGENTS.md exists", errors, warnings)
    check((root / ".cursor-plugin/plugin.json").is_file(), ".cursor-plugin/plugin.json exists", errors, warnings)
    check((root / ".cursor/agents").is_dir(), ".cursor/agents exists", errors, warnings)
    check((root / ".cursor/skills").is_dir(), ".cursor/skills exists", errors, warnings)
    check((root / "shared/excalibur-blog-handoff.template.md").is_file(), "handoff template exists", errors, warnings)
    check(
        not git_ls_files(root, "shared/excalibur-blog-handoff.md"),
        "runtime shared/excalibur-blog-handoff.md is not tracked",
        errors,
        warnings,
    )
    check(
        ".cursor/excalibur-blog-handoff.md" in (root / ".gitignore").read_text(encoding="utf-8"),
        ".cursor handoff ignored",
        errors,
        warnings,
    )

    check(module_available("PIL"), "Pillow available", errors, warnings)
    check(module_available("numpy"), "numpy available", errors, warnings)

    interlinker = root / "scripts/excalibur_blog_interlinker.py"
    help_proc = subprocess.run(
        [sys.executable, str(interlinker), "--help"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    check("--article-dir" in help_proc.stdout, "interlinker supports --article-dir", errors, warnings)

    llms = root / "scripts/excalibur_blog_llms_generator.py"
    llms_help = subprocess.run(
        [sys.executable, str(llms), "--help"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    check("--blog-path" in llms_help.stdout, "llms generator supports --blog-path", errors, warnings)
    check(
        "--relative-urls" in llms_help.stdout,
        "llms generator supports --relative-urls",
        errors,
        warnings,
    )

    today_src = (root / "scripts/excalibur_blog_today.py").read_text(encoding="utf-8")
    scout_src = (root / "scripts/excalibur_blog_scout_helper.py").read_text(encoding="utf-8")
    as_b_token = r"((?:AS|B)\d+)"
    as_b_composed = 'TOPIC_ID_PREFIX_RE = r"(?:AS|B)"' in scout_src and "TOPIC_ID_RE" in scout_src
    check(as_b_token in today_src, "today.py topic regex includes AS|B", errors, warnings)
    check(
        as_b_token in scout_src or as_b_composed,
        "scout_helper topic regex includes AS|B",
        errors,
        warnings,
    )

    topics_path = root / "memory/topics/blog-topics.md"
    if topics_path.is_file():
        topic_ids = re.findall(
            r"##\s+((?:AS|B)\d+)\s+—",
            topics_path.read_text(encoding="utf-8"),
        )
        check(bool(topic_ids), "blog-topics.md yields AS|B topic ids", errors, warnings)
        check(
            any(tid.upper().startswith("AS") for tid in topic_ids),
            "blog-topics.md discovers at least one AS* topic",
            errors,
            warnings,
        )
    else:
        check(False, "memory/topics/blog-topics.md exists", errors, warnings)

    policy_path = root / "memory/brief/editorial-policy.json"
    if policy_path.is_file():
        policy = json.loads(policy_path.read_text(encoding="utf-8"))
        pain = policy.get("pain_markers_ru") or []
        outcome = policy.get("outcome_markers_ru") or []
        check(bool(policy.get("_markers_pinned")), "editorial-policy _markers_pinned", errors, warnings)
        check(len(pain) >= 5, "editorial-policy pain_markers_ru pinned (≥5)", errors, warnings)
        check(len(outcome) >= 5, "editorial-policy outcome_markers_ru pinned (≥5)", errors, warnings)
        req = policy.get("article_required_signals") or {}
        check("min_pain_markers" in req, "editorial-policy min_pain_markers present", errors, warnings)
        check("min_outcome_markers" in req, "editorial-policy min_outcome_markers present", errors, warnings)
    else:
        check(False, "memory/brief/editorial-policy.json exists", errors, warnings)

    link_verify_src = (root / "scripts/excalibur_blog_link_verify.py").read_text(encoding="utf-8")
    for needle in (
        "def classify_soft_pass",
        "catalog_ssl",
        "catalog_dns",
        "catalog_5xx",
        "site_ssl",
        "def redact_report_urls",
    ):
        check(needle in link_verify_src, f"link_verify pins {needle}", errors, warnings)

    cover_src = (root / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
    check(
        "ALLOWED_FALLBACK_REFERENCE_HOST_SUFFIXES" in cover_src
        and "tempfile.redpandaai.co" in cover_src,
        "cover_quad_prompt allows Kie tempfile reference URLs",
        errors,
        warnings,
    )
    hero_src = (root / "scripts/excalibur_blog_hero_reference_url.py").read_text(encoding="utf-8")
    check(
        "upload_kie_base64" in hero_src and "file-base64-upload" in hero_src,
        "hero_reference_url supports Kie file-base64-upload",
        errors,
        warnings,
    )
    git_sh = root / "scripts/excalibur_git.sh"
    filter_sh = root / "scripts/excalibur_blog_filter_commit_secret_env.sh"
    check(git_sh.is_file(), "scripts/excalibur_git.sh present", errors, warnings)
    check(filter_sh.is_file(), "scripts/excalibur_blog_filter_commit_secret_env.sh present", errors, warnings)

    pub_src = (root / "scripts/excalibur_blog_wp_publish.py").read_text(encoding="utf-8")
    check("def ssh_host_tcp22_probe" in pub_src, "publish env-check has TCP/22 probe", errors, warnings)
    check("config PASS ≠ DNS/TCP PASS" in pub_src or "config_pass_note" in pub_src, "publish env-check documents config≠TCP", errors, warnings)

    notes_gate_src = (root / "scripts/excalibur_blog_research_notes_gate.py").read_text(encoding="utf-8")
    check("_tech_marker_hit" in notes_gate_src, "research_notes_gate uses token-boundary tech markers", errors, warnings)
    check("notes_without_github_evidence" in notes_gate_src, "research_notes_gate ignores github_evidence for tech heuristic", errors, warnings)

    hv_src = (root / "scripts/excalibur_blog_human_voice_gate.py").read_text(encoding="utf-8")
    check("быстрый инсайт" in hv_src and "TL;DR" in hv_src, "human_voice bans TL;DR insight labels", errors, warnings)

    check(module_available("paramiko"), "paramiko available", errors, warnings, warn=True)

    denylist_path = root / "shared/wp-slug-denylist.json"
    if denylist_path.is_file():
        try:
            denylist = json.loads(denylist_path.read_text(encoding="utf-8"))
            slugs = denylist.get("slugs") if isinstance(denylist, dict) else denylist
            check(
                isinstance(slugs, list) and len(slugs) >= 100,
                "shared/wp-slug-denylist.json has ≥100 slugs (fail-closed)",
                errors,
                warnings,
            )
        except json.JSONDecodeError:
            check(False, "shared/wp-slug-denylist.json parses as JSON", errors, warnings)
    else:
        check(False, "shared/wp-slug-denylist.json exists (fail-closed)", errors, warnings)

    env = merged_publish_env(root)
    has_public = bool(env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or env.get("WP_SITE_URL"))
    check(has_public, "PUBLIC_SITE_URL/WP_SITE_URL configured", errors, warnings, warn=not args.publish)
    check(bool(env.get("SSH_HOST")), "SSH host configured", errors, warnings, warn=not args.publish)
    check(bool(env.get("SSH_USER")), "SSH user configured", errors, warnings, warn=not args.publish)
    check(
        bool(env.get("SSH_PASS") or env.get("SSH_PASSWORD")),
        "SSH password configured",
        errors,
        warnings,
        warn=not args.publish,
    )
    check(
        env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() == "yes",
        "EXCALIBUR_BLOG_ALLOW_PUBLISH=yes",
        errors,
        warnings,
        warn=not args.publish,
    )

    print(f"SUMMARY errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
