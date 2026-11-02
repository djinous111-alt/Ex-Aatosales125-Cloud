#!/usr/bin/env python3
"""Preflight checks for Excalibur BLOG pipeline."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
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
        "SSH_HOST_IP",
        "SSH_PORT",
        "SSH_USER",
        "SSH_PASS",
        "SSH_PASSWORD",
        "SSH_ROOT",
        "SSH_PATH",
        "EXCALIBUR_BLOG_ALLOW_PUBLISH",
    }
    env = read_env_file(root / "memory/site.env.local")
    for key in keys:
        value = os.environ.get(key)
        if value:
            env[key] = value
    if not env.get("SSH_PASS") and env.get("SSH_PASSWORD"):
        env["SSH_PASS"] = env["SSH_PASSWORD"]
    if not (env.get("SSH_ROOT") or "").strip() and (env.get("SSH_PATH") or "").strip():
        env["SSH_ROOT"] = env["SSH_PATH"].strip()
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
    check(module_available("paramiko"), "paramiko available", errors, warnings, warn=not args.publish)

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
    # Canonical flag is --blog-dir; --blog-path is a supported alias.
    has_blog_dir = "--blog-dir" in llms_help.stdout
    has_blog_path = "--blog-path" in llms_help.stdout
    check(
        has_blog_dir and has_blog_path,
        "llms generator supports --blog-dir and --blog-path alias",
        errors,
        warnings,
    )

    today_src = (root / "scripts/excalibur_blog_today.py").read_text(encoding="utf-8")
    scout_src = (root / "scripts/excalibur_blog_scout_helper.py").read_text(encoding="utf-8")
    check("AS|B" in today_src and "AS|B" in scout_src, "today/scout accept AS|B topic IDs", errors, warnings)

    split_src = (root / "scripts/excalibur_blog_cover_quad_split.py").read_text(encoding="utf-8")
    check(
        "stamp_corner_brand" in split_src or "ensure_corner_brand" in split_src,
        "cover quad split stamps corner brand",
        errors,
        warnings,
    )

    link_src = (root / "scripts/excalibur_blog_link_verify.py").read_text(encoding="utf-8")
    check(
        "catalog_dns" in link_src and "CATALOG_HOST_SUFFIXES" in link_src,
        "link-verify soft-pass catalog_dns pinned",
        errors,
        warnings,
    )

    utility_src = (root / "scripts/excalibur_blog_utility_gate.py").read_text(encoding="utf-8")
    check(
        "if pain_markers and pain_count" in utility_src or "if pain_markers and" in utility_src,
        "utility gate skips empty pain/outcome marker lists",
        errors,
        warnings,
    )

    research_gate_src = (root / "scripts/excalibur_blog_research_notes_gate.py").read_text(encoding="utf-8")
    check(
        "pain_section" in research_gate_src or r"pain[_\s-]*solution" in research_gate_src,
        "research-notes gate counts pain_solution_map table rows",
        errors,
        warnings,
    )

    kie_src = (root / "scripts/excalibur_blog_kie_gpt_image2_api.py").read_text(encoding="utf-8")
    check(
        "file-base64-upload" in kie_src and "ensure_reachable_input_urls" in kie_src,
        "kie api auto-rehosts local hero via file-base64",
        errors,
        warnings,
    )

    publish_src = (root / "scripts/excalibur_blog_wp_publish.py").read_text(encoding="utf-8")
    check(
        "probe_ssh_dns" in publish_src and "SSH_HOST_IP" in publish_src,
        "publish --env-check probes SSH DNS / SSH_HOST_IP",
        errors,
        warnings,
    )

    check(
        (root / "scripts/excalibur_git.sh").is_file(),
        "scripts/excalibur_git.sh present (secret-name filter wrapper)",
        errors,
        warnings,
    )

    policy_path = root / "memory/brief/editorial-policy.json"
    if policy_path.is_file():
        try:
            policy = json.loads(policy_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            policy = {}
            check(False, "editorial-policy.json parses as JSON", errors, warnings)
        else:
            check(True, "editorial-policy.json parses as JSON", errors, warnings)
            pain = policy.get("pain_markers_ru") or []
            outcome = policy.get("outcome_markers_ru") or []
            check(bool(policy.get("_markers_pinned")), "editorial-policy _markers_pinned=true", errors, warnings)
            check(
                isinstance(pain, list) and len(pain) >= 5,
                "editorial-policy pain_markers_ru non-empty (≥5)",
                errors,
                warnings,
            )
            check(
                isinstance(outcome, list) and len(outcome) >= 5,
                "editorial-policy outcome_markers_ru non-empty (≥5)",
                errors,
                warnings,
            )
    else:
        check(False, "memory/brief/editorial-policy.json exists", errors, warnings)

    env = merged_publish_env(root)
    local_env = root / "memory/site.env.local"
    check(
        local_env.is_file()
        or bool(env.get("SSH_HOST"))
        or bool(os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL")),
        "site.env.local or Cloud publish env present",
        errors,
        warnings,
        warn=not args.publish,
    )
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

    # Soft note: MCP-KV / Wordstat cannot be probed offline; warn only.
    check(
        True,
        "MCP-KV/Wordstat: verify live discovery before Research/Cover (offline doctor skip)",
        errors,
        warnings,
    )

    print(f"SUMMARY errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
