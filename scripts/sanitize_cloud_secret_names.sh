#!/usr/bin/env bash
# Filter Cloud Agent injected secret name lists to valid bash identifiers.
# Source before git commit when pre-commit.cursor expands ${!SECRET_NAME}:
#   source scripts/sanitize_cloud_secret_names.sh
#
# Cloud injects COMMA-separated names; some entries are not identifiers
# (e.g. URL-like values or placeholder tokens like [REDACTED]).
# Those break: bash: invalid variable name
#
# Safe to source: does not change set -e/-u/-o of the caller.

_excalibur_filter_secret_names() {
  local raw="${1:-}"
  # Normalize commas to spaces, then tokenize.
  raw="${raw//,/ }"
  local out=()
  local name
  local -a names=()
  # shellcheck disable=SC2206
  names=($raw)
  for name in "${names[@]}"; do
    # Trim accidental whitespace/CR
    name="${name#"${name%%[![:space:]]*}"}"
    name="${name%"${name##*[![:space:]]}"}"
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$name")
    fi
  done
  local IFS=','
  printf '%s' "${out[*]}"
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES+x}" ]]; then
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_filter_secret_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
  export CLOUD_AGENT_INJECTED_SECRET_NAMES
fi

if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES+x}" ]]; then
  CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_filter_secret_names "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"
  export CLOUD_AGENT_ALL_SECRET_NAMES
fi
