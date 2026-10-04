#!/usr/bin/env bash
# Sanitize CLOUD_AGENT_*_SECRET_NAMES for pre-commit / shell hooks.
#
# Cloud injects secret *names* into env vars. Sometimes the list contains
# non-identifiers (bare URLs, "[REDACTED]", etc.) which break hooks with
# `invalid variable name`. Source this before every git commit in Cloud:
#
#   source scripts/sanitize_cloud_secret_names.sh
#
# Safe to re-source; never prints secret values.

_excalibur_sanitize_secret_names() {
  local raw="$1"
  local out=()
  local tok
  # split on comma / whitespace
  for tok in $(printf '%s' "$raw" | tr ',[:space:]' ' '); do
    # keep only POSIX shell identifiers (also allow empty skip)
    if [[ "$tok" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$tok")
    fi
  done
  if ((${#out[@]})); then
    local IFS=,
    printf '%s' "${out[*]}"
  fi
}

for _excalibur_secret_names_var in \
  CLOUD_AGENT_INJECTED_SECRET_NAMES \
  CLOUD_AGENT_SECRET_NAMES \
  CURSOR_CLOUD_AGENT_INJECTED_SECRET_NAMES
do
  if [[ -n "${!_excalibur_secret_names_var+x}" ]]; then
    _excalibur_sanitized="$(_excalibur_sanitize_secret_names "${!_excalibur_secret_names_var}")"
    export "$_excalibur_secret_names_var=$_excalibur_sanitized"
  fi
done

unset _excalibur_secret_names_var _excalibur_sanitized
unset -f _excalibur_sanitize_secret_names 2>/dev/null || true
