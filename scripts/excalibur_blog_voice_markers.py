"""Shared pain/outcome voice markers for utility and human-voice gates."""

from __future__ import annotations

from typing import Sequence

# Keep in sync with memory/brief/editorial-policy.json (pain_markers_ru / outcome_markers_ru).
DEFAULT_PAIN_MARKERS_RU: tuple[str, ...] = (
    "боль",
    "проблем",
    "ошиб",
    "ломает",
    "не работает",
    "теряет",
    "дорого",
    "долго",
    "рутин",
    "хаос",
    "застр",
    "сложно",
)

DEFAULT_OUTCOME_MARKERS_RU: tuple[str, ...] = (
    "результат",
    "получите",
    "сможете",
    "сэконом",
    "проверьте",
    "запустите",
    "соберите",
    "настройте",
    "исправьте",
    "выберите",
)


def resolve_marker_lists(
    policy: dict | None,
    *,
    pain_key: str = "pain_markers_ru",
    outcome_key: str = "outcome_markers_ru",
) -> tuple[list[str], list[str]]:
    """Return pain/outcome markers from policy, falling back to shared defaults."""
    policy = policy or {}
    pain = policy.get(pain_key) or list(DEFAULT_PAIN_MARKERS_RU)
    outcome = policy.get(outcome_key) or list(DEFAULT_OUTCOME_MARKERS_RU)
    if not isinstance(pain, list) or not pain:
        pain = list(DEFAULT_PAIN_MARKERS_RU)
    if not isinstance(outcome, list) or not outcome:
        outcome = list(DEFAULT_OUTCOME_MARKERS_RU)
    return [str(x) for x in pain], [str(x) for x in outcome]


def as_tuple(markers: Sequence[str]) -> tuple[str, ...]:
    return tuple(str(m) for m in markers)
