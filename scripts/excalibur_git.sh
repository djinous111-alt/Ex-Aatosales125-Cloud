#!/usr/bin/env bash
# Safe git wrapper for Cursor Cloud Agents.
# Filters CLOUD_AGENT_*SECRET_NAMES so values that look like URLs/secrets
# are not treated as bash namerefs (${!SECRET_NAME}) in pre-commit hooks.
set -euo pipefail

is_valid_secret_name() {
  # Valid bash identifier only (no :, /, ., -, spaces, etc.)
  [[ "$1" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]
}

filter_secret_names() {
  local raw="${1:-}"
  local -a keep=()
  local part trimmed
  # Support comma- and whitespace-separated lists
  IFS=$' \t\n,' read -r -a parts <<< "$raw"
  for part in "${parts[@]}"; do
    trimmed="${part//[$'\t\r\n']/}"
    trimmed="${trimmed#"${trimmed%%[![:space:]]*}"}"
    trimmed="${trimmed%"${trimmed##*[![:space:]]}"}"
    [[ -z "$trimmed" ]] && continue
    if is_valid_secret_name "$trimmed"; then
      keep+=("$trimmed")
    else
      echo "[excalibur_git] skip invalid secret name entry: <redacted non-identifier>" >&2
    fi
  done
  if ((${#keep[@]})); then
    local IFS=','
    echo "${keep[*]}"
  else
    echo ""
  fi
}

for var in CLOUD_AGENT_INJECTED_SECRET_NAMES CLOUD_AGENT_SECRET_NAMES; do
  if [[ -n "${!var:-}" ]]; then
    filtered="$(filter_secret_names "${!var}")"
    export "$var=$filtered"
  fi
done

exec git "$@"
