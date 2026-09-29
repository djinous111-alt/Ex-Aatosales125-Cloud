#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.
# Prevents pre-commit.cursor `${!SECRET_NAME}` → "invalid variable name".
# Usage: source scripts/sanitize_cloud_secret_names.sh
set +u
_raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
_filtered=""
IFS=',' read -r -a _names <<< "${_raw}"
for _name in "${_names[@]}"; do
  _name="$(echo "${_name}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
  [[ -z "${_name}" ]] && continue
  if [[ "${_name}" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    if [[ -z "${_filtered}" ]]; then
      _filtered="${_name}"
    else
      _filtered="${_filtered},${_name}"
    fi
  fi
done
export CLOUD_AGENT_INJECTED_SECRET_NAMES="${_filtered}"
unset _raw _filtered _names _name
