#!/usr/bin/env bash
# Excalibur BLOG — safe git helper for Cloud Agents.
# Filters CLOUD_AGENT_*_SECRET_NAMES so pre-commit.cursor does not crash on
# invalid bash identifiers (INC-20261027-1326).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

_is_valid_bash_ident() {
  [[ "$1" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]
}

filter_secret_name_lists() {
  local name filtered=""
  if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
    filtered=""
    for name in ${CLOUD_AGENT_INJECTED_SECRET_NAMES}; do
      if _is_valid_bash_ident "$name"; then
        filtered+="${name} "
      else
        echo "[excalibur_git] skip invalid injected secret name (not a bash identifier)" >&2
      fi
    done
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${filtered%" "}"
  fi
  if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]]; then
    filtered=""
    for name in ${CLOUD_AGENT_ALL_SECRET_NAMES}; do
      if _is_valid_bash_ident "$name"; then
        filtered+="${name} "
      else
        echo "[excalibur_git] skip invalid all-secret name (not a bash identifier)" >&2
      fi
    done
    export CLOUD_AGENT_ALL_SECRET_NAMES="${filtered%" "}"
  fi
}

usage() {
  cat <<'EOF'
Usage:
  bash scripts/excalibur_git.sh status
  bash scripts/excalibur_git.sh add [paths...]
  bash scripts/excalibur_git.sh commit -m "message"
  bash scripts/excalibur_git.sh push [branch]

Filters CLOUD_AGENT_INJECTED_SECRET_NAMES / CLOUD_AGENT_ALL_SECRET_NAMES to
valid bash identifiers before commit (pre-commit.cursor secret scanner).
Does not print secret values or invalid secret names.
EOF
}

cmd="${1:-}"
shift || true

case "$cmd" in
  status)
    git status --short
    ;;
  add)
    if [[ "$#" -eq 0 ]]; then
      echo "excalibur_git add: pass paths" >&2
      exit 2
    fi
    git add "$@"
    ;;
  commit)
    filter_secret_name_lists
    if [[ "$#" -eq 0 ]]; then
      echo "excalibur_git commit: pass git commit args (e.g. -m \"msg\")" >&2
      exit 2
    fi
    git commit "$@"
    ;;
  push)
    branch="${1:-}"
    if [[ -z "$branch" ]]; then
      branch="$(git symbolic-ref --short HEAD)"
    fi
    git push -u origin "$branch"
    ;;
  ""|-h|--help|help)
    usage
    ;;
  *)
    echo "Unknown command: $cmd" >&2
    usage >&2
    exit 2
    ;;
esac
