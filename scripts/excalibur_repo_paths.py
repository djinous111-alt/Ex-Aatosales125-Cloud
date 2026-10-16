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


def resolve_gate_output(output: Path, *, article_dir: Path, root: Path) -> Path:
    """Resolve gate -o path: bare filename → article_dir; multi-part relative → root."""
    if output.is_absolute():
        return output
    if len(output.parts) == 1:
        return article_dir / output
    return root / output
