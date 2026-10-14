#!/usr/bin/env bash
# Safe git wrapper for Cloud Agents.
# Filters CLOUD_AGENT_INJECTED_SECRET_NAMES so pre-commit.cursor does not abort on
# non-identifier entries (e.g. a bare URL mistakenly listed as a "secret name").
set -euo pipefail

filter_injected_secret_names() {
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
  [[ -z "$raw" ]] && return 0
  local -a kept=()
  local part trimmed
  IFS=',' read -ra parts <<< "$raw"
  for part in "${parts[@]}"; do
    trimmed="${part#"${part%%[![:space:]]*}"}"
    trimmed="${trimmed%"${trimmed##*[![:space:]]}"}"
    if [[ "$trimmed" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      kept+=("$trimmed")
    fi
  done
  local IFS=','
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="${kept[*]-}"
}

filter_injected_secret_names
exec git "$@"
