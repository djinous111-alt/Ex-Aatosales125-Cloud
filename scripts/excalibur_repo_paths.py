"""Repo-relative paths for JSON reports (no local usernames in git)."""

from __future__ import annotations

from pathlib import Path


def project_root_from(anchor: Path) -> Path:
    return anchor.resolve().parents[1]


def repo_relative(path: Path, root: Path | None = None) -> str:
    p = path.resolve()
    base = (root or project_root_from(Path(__file__))).resolve()
    try:
        return p.relative_to(base).as_posix()
    except ValueError:
        return p.as_posix()


def resolve_gate_output(output: Path, article_dir: Path, root: Path) -> Path:
    """Resolve -o/--output for article gates.

    Bare filename (``human-voice-report.json``) → under ``article_dir``.
    Paths with separators (``memory/blog/.../report.json``) → under project
    root / CWD, never nested as ``article_dir / memory/blog/...``.
    """
    if output.is_absolute():
        return output
    if len(output.parts) == 1:
        return article_dir / output
    as_posix = output.as_posix()
    root_candidate = root / output
    cwd_candidate = Path.cwd() / output
    if as_posix.startswith(("memory/", "scripts/", ".cursor/", "shared/")):
        return root_candidate
    if cwd_candidate.parent.exists() and not root_candidate.parent.exists():
        return cwd_candidate
    if root_candidate.parent.exists() or as_posix.startswith(article_dir.name):
        return root_candidate
    return root_candidate
