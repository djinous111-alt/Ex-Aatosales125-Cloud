#!/usr/bin/env bash
# Sanitize Cloud Agent secret-name env lists, then run git.
# Fixes pre-commit.cursor "invalid variable name" when CLOUD_AGENT_*_SECRET_NAMES
# contains placeholders like [REDACTED] that are not valid bash identifiers.
set -euo pipefail

filter_secret_names() {
  local raw="${1:-}"
  local -a kept=()
  local name
  IFS=',' read -ra names <<< "$raw"
  for name in "${names[@]}"; do
    name="${name#"${name%%[![:space:]]*}"}"
    name="${name%"${name##*[![:space:]]}"}"
    if [[ -n "$name" && "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      kept+=("$name")
    fi
  done
  local IFS=','
  printf '%s' "${kept[*]-}"
}

export CLOUD_AGENT_INJECTED_SECRET_NAMES
export CLOUD_AGENT_ALL_SECRET_NAMES
CLOUD_AGENT_INJECTED_SECRET_NAMES="$(filter_secret_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
CLOUD_AGENT_ALL_SECRET_NAMES="$(filter_secret_names "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"

exec git "$@"
