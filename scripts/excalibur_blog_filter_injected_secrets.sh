#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to bash-safe identifiers before pre-commit.
# Usage: source scripts/excalibur_blog_filter_injected_secrets.sh
# Safe to call multiple times; does not print secret values.

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  _filtered=""
  IFS=',' read -r -a _secret_names <<< "${CLOUD_AGENT_INJECTED_SECRET_NAMES}"
  for _name in "${_secret_names[@]}"; do
    _name="$(echo "${_name}" | xargs 2>/dev/null || true)"
    if [[ "${_name}" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      if [[ -z "${_filtered}" ]]; then
        _filtered="${_name}"
      else
        _filtered="${_filtered},${_name}"
      fi
    fi
  done
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="${_filtered}"
fi
