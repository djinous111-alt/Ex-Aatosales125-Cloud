#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES to bash-safe identifiers only.
# Cloud sometimes injects a URL as a "secret name"; `${!NAME}` then fails with
# `invalid variable name` and blocks git commit hooks.
#
# Usage (before git commit/push in Cloud Agent shells):
#   source scripts/sanitize_cloud_secret_names.sh
#
# Safe to source multiple times. Does not print secret values.

_excalibur_filter_secret_names() {
  local raw="$1"
  local out=()
  local tok
  # shellcheck disable=SC2206
  for tok in ${raw}; do
    if [[ "$tok" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$tok")
    fi
  done
  printf '%s' "${out[*]}"
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_filter_secret_names "$CLOUD_AGENT_INJECTED_SECRET_NAMES")"
  export CLOUD_AGENT_INJECTED_SECRET_NAMES
fi

if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES:-}" ]]; then
  CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_filter_secret_names "$CLOUD_AGENT_ALL_SECRET_NAMES")"
  export CLOUD_AGENT_ALL_SECRET_NAMES
fi

unset -f _excalibur_filter_secret_names 2>/dev/null || true
