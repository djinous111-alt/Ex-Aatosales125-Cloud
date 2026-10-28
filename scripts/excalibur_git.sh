#!/usr/bin/env bash
# Safe git helpers for Excalibur BLOG Cloud agents.
# Filters invalid Cloud-injected secret *names* before pre-commit.cursor expands ${!NAME}.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Valid bash identifiers only — URL tokens / garbage in CLOUD_AGENT_*_SECRET_NAMES
# otherwise abort commits with "invalid variable name" (INC-20261027-0025).
filter_commit_secret_env() {
  local var name filtered
  for var in CLOUD_AGENT_INJECTED_SECRET_NAMES CLOUD_AGENT_ALL_SECRET_NAMES; do
    if [[ -z "${!var-}" ]]; then
      continue
    fi
    filtered=""
    # shellcheck disable=SC2086
    for name in ${!var}; do
      if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
        filtered+="${filtered:+ }${name}"
      else
        echo "[excalibur_git] skip invalid secret name (not a bash identifier)" >&2
      fi
    done
    export "$var=$filtered"
  done
}

usage() {
  cat <<'EOF'
Usage:
  bash scripts/excalibur_git.sh filter-env
  bash scripts/excalibur_git.sh commit [git commit args...]
  eval "$(bash scripts/excalibur_git.sh print-filter)"

filter-env / print-filter sanitize CLOUD_AGENT_*_SECRET_NAMES for pre-commit.cursor.
commit runs filter then git commit with the remaining args.
EOF
}

cmd="${1:-}"
case "$cmd" in
  filter-env)
    filter_commit_secret_env
    echo "CLOUD_AGENT_INJECTED_SECRET_NAMES filtered for commit"
    ;;
  print-filter)
    # Emit a snippet callers can eval in the current shell.
    cat <<'EOF'
filter_commit_secret_env() {
  local var name filtered
  for var in CLOUD_AGENT_INJECTED_SECRET_NAMES CLOUD_AGENT_ALL_SECRET_NAMES; do
    if [[ -z "${!var-}" ]]; then
      continue
    fi
    filtered=""
    for name in ${!var}; do
      if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
        filtered+="${filtered:+ }${name}"
      fi
    done
    export "$var=$filtered"
  done
}
filter_commit_secret_env
EOF
    ;;
  commit)
    shift
    filter_commit_secret_env
    git commit "$@"
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
