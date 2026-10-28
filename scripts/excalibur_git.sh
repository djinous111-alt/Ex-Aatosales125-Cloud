#!/usr/bin/env bash
# Safe git wrapper for Excalibur Cloud Agents.
# Filters CLOUD_AGENT_INJECTED_SECRET_NAMES to valid shell identifiers so the
# Cursor pre-commit secret-scan does not crash on a masked name like [REDACTED].
set -euo pipefail

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}" ]]; then
  filtered=""
  IFS=',' read -r -a _excalibur_secret_names <<< "${CLOUD_AGENT_INJECTED_SECRET_NAMES}"
  for name in "${_excalibur_secret_names[@]}"; do
    name="${name// /}"
    [[ -z "$name" ]] && continue
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      if [[ -n "$filtered" ]]; then
        filtered+=",${name}"
      else
        filtered="${name}"
      fi
    else
      echo "[excalibur_git] skip non-identifier secret name: ${name}" >&2
    fi
  done
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$filtered"
fi

exec git "$@"
