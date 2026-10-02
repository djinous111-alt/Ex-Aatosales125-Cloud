#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to valid bash identifiers.
# Cloud pre-commit fails with "invalid variable name" when a token is not a valid name.
# Usage: source scripts/sanitize_cloud_secret_names.sh

_sanitize_secret_names_list() {
  local raw="$1"
  local out="" part
  IFS=',' read -r -a _parts <<< "$raw"
  for part in "${_parts[@]}"; do
    part="${part// /}"
    [[ -z "$part" ]] && continue
    if [[ "$part" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      if [[ -z "$out" ]]; then
        out="$part"
      else
        out="$out,$part"
      fi
    fi
  done
  printf '%s' "$out"
}

if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES="$(_sanitize_secret_names_list "$CLOUD_AGENT_ALL_SECRET_NAMES")"
fi
if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_sanitize_secret_names_list "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
fi

unset -f _sanitize_secret_names_list
