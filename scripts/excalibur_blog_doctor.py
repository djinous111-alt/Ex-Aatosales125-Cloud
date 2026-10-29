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
        "CATALOG_URL",
        "TELEGRAM_URL",
        "MAX_URL",
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


def check_research_tech_marker_regression(root: Path, errors: list[str], warnings: list[str]) -> None:
    """Auto/China how-to notes with reader_pain + комплектации must not look technical."""
    gate = root / "scripts/excalibur_blog_research_notes_gate.py"
    if not gate.is_file():
        check(False, "research_notes_gate.py present for tech-marker regression", errors, warnings)
        return
    scripts_dir = str(root / "scripts")
    sys.path.insert(0, scripts_dir)
    try:
        import excalibur_blog_research_notes_gate as gate_mod  # noqa: WPS433

        fake_context = {
            "topic": {
                "h1": "Geely Atlas из Китая: комплектации и ловушки 2026",
                "primary_query": "джили атлас из китая комплектации",
                "secondary_queries": ["boyue l vs atlas", "депозит комплектация"],
                "search_intent": "how_to",
                "slug": "geely-atlas-iz-kitaya-komplektatsii-lovushki-2026",
            }
        }
        notes = (
            "reader_pain: новичок путает комплектации Boyue L и боится депозита без чеклиста\n"
            "community_evidence: N/A for auto import niche (no code repos)\n"
            "pain_solution_map: боль: путаница | решение: сверка | результат: стоп до депозита\n"
        )
        technical = gate_mod.is_technical_topic(fake_context, notes)
        check(
            technical is False,
            "research tech markers: комплектации + reader_pain is not technical_topic",
            errors,
            warnings,
        )
        # Bare ai/ии must not be listed as TECH_MARKERS (substring false positives).
        bare = {m.lower() for m in gate_mod.TECH_MARKERS}
        check("ai" not in bare and "ии" not in bare, "TECH_MARKERS has no bare ai/ии", errors, warnings)
    except Exception as exc:  # noqa: BLE001
        check(False, f"research tech-marker regression runnable ({exc})", errors, warnings)
    finally:
        if scripts_dir in sys.path:
            sys.path.remove(scripts_dir)


def check_llms_blog_path(root: Path, errors: list[str], warnings: list[str]) -> None:
    llms = root / "scripts/excalibur_blog_llms_generator.py"
    llms_help = subprocess.run(
        [sys.executable, str(llms), "--help"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    check("--blog-path" in llms_help.stdout, "llms generator supports --blog-path", errors, warnings)
    check("--blog-dir" in llms_help.stdout, "llms generator supports --blog-dir", errors, warnings)
    check("--out-dir" in llms_help.stdout, "llms generator supports --out-dir", errors, warnings)
    # Default --site-base must be empty (relative URLs), not a live host.
    # argparse often omits empty defaults from --help; assert in source.
    llms_src = llms.read_text(encoding="utf-8") if llms.is_file() else ""
    site_base_block = ""
    m = re.search(r'add_argument\(\s*"--site-base"[\s\S]*?\)', llms_src)
    if m:
        site_base_block = m.group(0)
    check(
        'default=""' in site_base_block or "default=''" in site_base_block,
        "llms --site-base default is empty",
        errors,
        warnings,
    )
    scripts_dir = str(root / "scripts")
    sys.path.insert(0, scripts_dir)
    try:
        import excalibur_blog_llms_generator as llms_mod  # noqa: WPS433

        url = llms_mod.article_url("", "/", "geely-atlas-iz-kitaya-komplektatsii-lovushki-2026")
        check(
            url == "/geely-atlas-iz-kitaya-komplektatsii-lovushki-2026/",
            "llms article_url(blog_path=/) → /{slug}/",
            errors,
            warnings,
        )
        url_blog = llms_mod.article_url("", "/blog", "demo-slug")
        check(url_blog == "/blog/demo-slug/", "llms article_url(blog_path=/blog) → /blog/{slug}/", errors, warnings)
    except Exception as exc:  # noqa: BLE001
        check(False, f"llms article_url regression runnable ({exc})", errors, warnings)
    finally:
        if scripts_dir in sys.path:
            sys.path.remove(scripts_dir)


def check_cover_no_hoodie_lock(root: Path, errors: list[str], warnings: list[str]) -> None:
    prompt_py = root / "scripts/excalibur_blog_cover_quad_prompt.py"
    manifest_py = root / "scripts/excalibur_blog_quad_manifest.py"
    if not prompt_py.is_file():
        check(False, "cover_quad_prompt.py present", errors, warnings)
        return
    prompt_src = prompt_py.read_text(encoding="utf-8")
    check(
        "Outfit lock: thick heavyweight white hoodie" not in prompt_src,
        "cover prompt has no white-hoodie Outfit lock",
        errors,
        warnings,
    )
    check(
        "NEVER lock white hoodie" in prompt_src or "NOT white hoodie" in prompt_src,
        "cover prompt forbids white-hoodie lock",
        errors,
        warnings,
    )
    if manifest_py.is_file():
        man_src = manifest_py.read_text(encoding="utf-8")
        check(
            "белое плотное худи" not in man_src,
            "quad_manifest default scene has no white-hoodie lock",
            errors,
            warnings,
        )
        check(
            "Outfit lock: thick heavyweight white hoodie" not in man_src,
            "quad_manifest has no Outfit lock white hoodie",
            errors,
            warnings,
        )


def check_publish_schema_expand(root: Path, errors: list[str], warnings: list[str]) -> None:
    publish = root / "scripts/excalibur_blog_wp_publish.py"
    if not publish.is_file():
        check(False, "wp_publish.py present", errors, warnings)
        return
    src = publish.read_text(encoding="utf-8")
    check("def expand_env_placeholders" in src, "wp_publish expand_env_placeholders defined", errors, warnings)
    check("${PUBLIC_SITE_URL}" in src or "PUBLIC_SITE_URL" in src, "wp_publish knows PUBLIC_SITE_URL", errors, warnings)
    scripts_dir = str(root / "scripts")
    sys.path.insert(0, scripts_dir)
    try:
        import excalibur_blog_wp_publish as pub  # noqa: WPS433

        expanded = pub.expand_env_placeholders(
            '{"url":"${PUBLIC_SITE_URL}/x/","sameAs":["${CATALOG_URL}","${TELEGRAM_URL}","${MAX_URL}"]}',
            {
                "PUBLIC_SITE_URL": "https://example.test",
                "CATALOG_URL": "https://catalog.example",
                "TELEGRAM_URL": "https://t.me/example",
                "MAX_URL": "https://max.example",
            },
        )
        check(
            "https://example.test/x/" in expanded
            and "https://catalog.example" in expanded
            and "${PUBLIC_SITE_URL}" not in expanded,
            "wp_publish expands schema CTA placeholders",
            errors,
            warnings,
        )
    except Exception as exc:  # noqa: BLE001
        check(False, f"wp_publish expand regression runnable ({exc})", errors, warnings)
    finally:
        if scripts_dir in sys.path:
            sys.path.remove(scripts_dir)


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

    policy_path = root / "memory/brief/editorial-policy.json"
    check(policy_path.is_file(), "editorial-policy.json exists", errors, warnings)
    if policy_path.is_file():
        try:
            policy = json.loads(policy_path.read_text(encoding="utf-8"))
            pain = policy.get("pain_markers_ru") or []
            outcome = policy.get("outcome_markers_ru") or []
            req = policy.get("article_required_signals") or {}
            check(
                isinstance(pain, list) and len(pain) >= 3,
                "editorial-policy pain_markers_ru non-empty",
                errors,
                warnings,
            )
            check(
                isinstance(outcome, list) and len(outcome) >= 3,
                "editorial-policy outcome_markers_ru non-empty",
                errors,
                warnings,
            )
            check(int(req.get("min_pain_markers") or 0) >= 1, "editorial-policy min_pain_markers set", errors, warnings)
            check(
                int(req.get("min_outcome_markers") or 0) >= 1,
                "editorial-policy min_outcome_markers set",
                errors,
                warnings,
            )
            check(bool(policy.get("_markers_pinned")), "editorial-policy _markers_pinned true", errors, warnings)
        except Exception as exc:  # noqa: BLE001
            check(False, f"editorial-policy.json parses ({exc})", errors, warnings)

    git_sh = root / "scripts/excalibur_git.sh"
    filter_commit_sh = root / "scripts/excalibur_blog_filter_commit_secret_env.sh"
    filter_names_sh = root / "scripts/excalibur_blog_filter_secret_names.sh"
    check(git_sh.is_file(), "excalibur_git.sh present", errors, warnings)
    check(filter_commit_sh.is_file(), "excalibur_blog_filter_commit_secret_env.sh present", errors, warnings)
    check(filter_names_sh.is_file(), "excalibur_blog_filter_secret_names.sh present", errors, warnings)

    interlinker = root / "scripts/excalibur_blog_interlinker.py"
    help_proc = subprocess.run(
        [sys.executable, str(interlinker), "--help"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    check("--article-dir" in help_proc.stdout, "interlinker supports --article-dir", errors, warnings)

    check_llms_blog_path(root, errors, warnings)
    check_research_tech_marker_regression(root, errors, warnings)
    check_cover_no_hoodie_lock(root, errors, warnings)
    check_publish_schema_expand(root, errors, warnings)

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
