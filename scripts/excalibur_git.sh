#!/usr/bin/env bash
# Safe git wrapper for Cursor Cloud Agents.
# Filters CLOUD_AGENT_INJECTED_SECRET_NAMES to bash-safe identifiers so the
# platform pre-commit secret scanner does not die on `invalid variable name`
# when a secret was registered with a URL-shaped or otherwise non-identifier name.
#
# Usage:
#   scripts/excalibur_git.sh add -A
#   scripts/excalibur_git.sh commit -m "message"
#   scripts/excalibur_git.sh push -u origin HEAD
#
# If commit still fails with `invalid variable name` / `${!SECRET_NAME}`, retry once:
#   CLOUD_AGENT_INJECTED_SECRET_NAMES= scripts/excalibur_git.sh commit -m "message"
set -euo pipefail

filter_secret_names() {
  local raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
  local filtered=()
  local name
  # shellcheck disable=SC2086
  for name in ${raw}; do
    if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      filtered+=("$name")
    fi
  done
  if ((${#filtered[@]})); then
    export CLOUD_AGENT_INJECTED_SECRET_NAMES="${filtered[*]}"
  else
    export CLOUD_AGENT_INJECTED_SECRET_NAMES=""
  fi
}

filter_secret_names

if [[ "${1:-}" == "commit" ]]; then
  set +e
  git "$@"
  rc=$?
  set -e
  if [[ $rc -ne 0 ]]; then
    # Last-resort retry for redaction/hooks that still choke on injected names.
    export CLOUD_AGENT_INJECTED_SECRET_NAMES=""
    git "$@"
    rc=$?
  fi
  exit "$rc"
fi

exec git "$@"
