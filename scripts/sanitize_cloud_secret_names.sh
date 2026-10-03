#!/usr/bin/env bash
# Filter Cloud Agent secret-name lists to valid bash identifiers.
# Source before git commit when pre-commit expands ${!SECRET_NAME}:
#   source scripts/sanitize_cloud_secret_names.sh
#
# CLOUD_AGENT_INJECTED_SECRET_NAMES / CLOUD_AGENT_ALL_SECRET_NAMES may contain
# comma-separated junk (URLs, [REDACTED], placeholders) that abort bash with
# "invalid variable name". Drop anything that is not ^[A-Za-z_][A-Za-z0-9_]*$.

_excalibur_sanitize_secret_name_list() {
  local raw="${1:-}"
  local -a kept=()
  local part trimmed
  local IFS=','
  # shellcheck disable=SC2086
  for part in ${raw}; do
    trimmed="${part#"${part%%[![:space:]]*}"}"
    trimmed="${trimmed%"${trimmed##*[![:space:]]}"}"
    if [[ "$trimmed" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
      kept+=("$trimmed")
    fi
  done
  if ((${#kept[@]} == 0)); then
    printf ''
    return 0
  fi
  local IFS=','
  printf '%s' "${kept[*]}"
}

if [[ -n "${CLOUD_AGENT_INJECTED_SECRET_NAMES+x}" ]]; then
  export CLOUD_AGENT_INJECTED_SECRET_NAMES="$(_excalibur_sanitize_secret_name_list "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
fi
if [[ -n "${CLOUD_AGENT_ALL_SECRET_NAMES+x}" ]]; then
  export CLOUD_AGENT_ALL_SECRET_NAMES="$(_excalibur_sanitize_secret_name_list "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"
fi
