#!/usr/bin/env python3
"""Regression: empty pain/outcome marker lists must not hard-BLOCK articles."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_utility_gate import count_markers  # noqa: E402


def _simulate_pain_outcome_enforce(policy: dict, plain: str) -> list[str]:
    """Mirror enforce logic from validate path (empty lists → skip)."""
    errors: list[str] = []
    req = policy.get("article_required_signals") or {}
    pain_markers = policy.get("pain_markers_ru") or []
    outcome_markers = policy.get("outcome_markers_ru") or []
    pain_count = count_markers(plain, pain_markers) if pain_markers else 0
    outcome_count = count_markers(plain, outcome_markers) if outcome_markers else 0

    if pain_markers:
        min_pain = int(req.get("min_pain_markers") or 2)
        if pain_count < min_pain:
            errors.append(f"pain_markers={pain_count} < {min_pain}")
    if outcome_markers:
        min_outcome = int(req.get("min_outcome_markers") or 3)
        if outcome_count < min_outcome:
            errors.append(f"outcome_markers={outcome_count} < {min_outcome}")
    return errors


def main() -> int:
    plain = "статья без явных pain/outcome маркеров из пустых списков"
    empty_policy = {
        "article_required_signals": {"min_pain_markers": 2, "min_outcome_markers": 3},
        "pain_markers_ru": [],
        "outcome_markers_ru": [],
    }
    errs = _simulate_pain_outcome_enforce(empty_policy, plain)
    assert errs == [], f"empty lists must skip enforce, got {errs}"

    missing_keys_policy = {
        "article_required_signals": {"min_pain_markers": 2, "min_outcome_markers": 3},
    }
    errs2 = _simulate_pain_outcome_enforce(missing_keys_policy, plain)
    assert errs2 == [], f"missing marker keys must skip, got {errs2}"

    configured = {
        "article_required_signals": {"min_pain_markers": 1, "min_outcome_markers": 1},
        "pain_markers_ru": ["боль читателя"],
        "outcome_markers_ru": ["получите результат"],
    }
    errs3 = _simulate_pain_outcome_enforce(configured, plain)
    assert len(errs3) == 2, f"configured non-empty lists must enforce, got {errs3}"

    ok_plain = "тут боль читателя и вы получите результат сразу"
    errs4 = _simulate_pain_outcome_enforce(configured, ok_plain)
    assert errs4 == [], f"matching text must PASS, got {errs4}"

    print("OK: utility gate empty pain/outcome marker regression")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
