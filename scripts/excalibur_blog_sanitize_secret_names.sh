#!/usr/bin/env bash
# Sanitize Cloud Agent secret-name lists before git commit.
# Cursor pre-commit may inject invalid names like literal [REDACTED] into
# CLOUD_AGENT_INJECTED_SECRET_NAMES / CLOUD_AGENT_*_SECRET_NAMES; bash then
# fails on ${!SECRET_NAME} with "invalid variable name".
#
# Usage (before git commit in Cloud):
#   source scripts/excalibur_blog_sanitize_secret_names.sh
#   # or:
#   eval "$(bash scripts/excalibur_blog_sanitize_secret_names.sh --export)"
set -euo pipefail

_excalibur_sanitize_secret_names() {
  local raw="${1:-}"
  local out=()
  local name
  # Split on commas or whitespace; keep only valid bash identifiers.
  IFS=$' ,\t\n' read -r -a parts <<< "${raw}"
  for name in "${parts[@]}"; do
    [[ -z "${name}" ]] && continue
    if [[ "${name}" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("${name}")
    fi
  done
  # Re-join with commas (Cloud hooks expect comma lists; space-join breaks them).
  local IFS=,
  printf '%s' "${out[*]}"
}

_excalibur_apply_secret_name_sanitize() {
  local var
  for var in \
    CLOUD_AGENT_INJECTED_SECRET_NAMES \
    CLOUD_AGENT_SYNCED_SECRET_NAMES \
    CLOUD_AGENT_SECRET_NAMES
  do
    if [[ -n "${!var-}" ]]; then
      export "${var}=$(_excalibur_sanitize_secret_names "${!var}")"
    fi
  done
}

if [[ "${1:-}" == "--export" ]]; then
  _excalibur_apply_secret_name_sanitize
  for var in \
    CLOUD_AGENT_INJECTED_SECRET_NAMES \
    CLOUD_AGENT_SYNCED_SECRET_NAMES \
    CLOUD_AGENT_SECRET_NAMES
  do
    if [[ -n "${!var-}" ]]; then
      printf 'export %s=%q\n' "${var}" "${!var}"
    fi
  done
  exit 0
fi

# When sourced, sanitize in current shell.
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
  _excalibur_apply_secret_name_sanitize
fi
