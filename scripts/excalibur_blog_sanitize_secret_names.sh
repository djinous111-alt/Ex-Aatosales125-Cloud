#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.
#
# Cloud may inject raw URLs / non-identifiers into this comma-separated list.
# Pre-commit hooks that expand `${!SECRET_NAME}` then crash with
# `invalid variable name` before the content scan runs.
#
# Usage (before every Cloud git commit):
#   source scripts/excalibur_blog_sanitize_secret_names.sh
#
# Safe to source multiple times. Does not print secret values.

_excalibur_is_valid_bash_ident() {
  [[ "$1" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  _excalibur_filtered=()
  # Prefer comma-separated (Cloud hook IFS=','); also accept whitespace.
  _excalibur_raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES//,/ }"
  # shellcheck disable=SC2206
  _excalibur_names=( ${_excalibur_raw} )
  for _excalibur_n in "${_excalibur_names[@]}"; do
    if [[ -n "${_excalibur_n}" ]] && _excalibur_is_valid_bash_ident "${_excalibur_n}"; then
      _excalibur_filtered+=("${_excalibur_n}")
    fi
  done
  if ((${#_excalibur_filtered[@]})); then
    IFS=','
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${_excalibur_filtered[*]}"
    unset IFS
  else
    unset CLOUD_AGENT_INJECTED_SECRET_NAMES || true
  fi
  unset _excalibur_filtered _excalibur_raw _excalibur_names _excalibur_n
fi

unset -f _excalibur_is_valid_bash_ident 2>/dev/null || true
