#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to bash-safe identifiers before git commit.
# Platform pre-commit.cursor does `${!SECRET_NAME}` and aborts on invalid names.
# Usage: source this file, or run via scripts/excalibur_git.sh
set -euo pipefail

_excalibur_filter_secret_names() {
  local raw="${1:-}"
  local -a kept=()
  local name
  IFS=',' read -ra _names <<< "$raw"
  for name in "${_names[@]}"; do
    name="${name#"${name%%[![:space:]]*}"}"
    name="${name%"${name##*[![:space:]]}"}"
    [[ -z "$name" ]] && continue
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      kept+=("$name")
    fi
  done
  local IFS=','
  printf '%s' "${kept[*]-}"
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_filter_secret_names "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
fi
if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES
  CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_filter_secret_names "$CLOUD_AGENT_ALL_SECRET_NAMES")"
fi
