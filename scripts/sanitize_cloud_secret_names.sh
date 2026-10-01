#!/usr/bin/env bash
# Filter Cloud Agent secret-name lists before git commit / pre-commit.cursor.
#
# Cloud sometimes injects a literal "[REDACTED]" into:
#   CLOUD_AGENT_INJECTED_SECRET_NAMES
#   CLOUD_AGENT_ALL_SECRET_NAMES
# Indirect expansion `${!SECRET_NAME}` then fails with:
#   [REDACTED]: invalid variable name
#
# Usage (before every commit in Cloud):
#   source scripts/sanitize_cloud_secret_names.sh
#
# Safe to source repeatedly. Does not print secret values.

_excalibur_sanitize_secret_name_list() {
  local input="${1-}"
  local name
  local -a out=()
  for name in $input; do
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      out+=("$name")
    fi
  done
  if ((${#out[@]})); then
    printf '%s' "${out[*]}"
  else
    printf ''
  fi
}

if [ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES+x}" ]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES
  CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_sanitize_secret_name_list "${CLOUD_AGENT_INJECTED_SECRET_NAMES-}")"
fi

if [ -n "${CLOUD_AGENT_ALL_SECRET_NAMES+x}" ]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES
  CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_sanitize_secret_name_list "${CLOUD_AGENT_ALL_SECRET_NAMES-}")"
fi

unset -f _excalibur_sanitize_secret_name_list
