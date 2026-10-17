#!/usr/bin/env bash
# Safe git wrapper for Cloud Agent: sanitize SECRET_NAMES for pre-commit.cursor
# Hook splits CLOUD_AGENT_INJECTED_SECRET_NAMES on commas, then does ${!SECRET_NAME}.
# Space-separated lists or public CTA URLs break the hook / false-positive scan.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Public / non-secret CTA site values — exclude from secret scan list
EXCLUDE_RE='^(PUBLIC_SITE_URL|WP_HOME|WP_SITE_URL|CATALOG_URL|TELEGRAM_URL|MAX_URL|YANDEX_METRIKA_COUNTER_ID)$'

sanitize_secret_names() {
  local raw="${1:-}"
  local out=()
  local tok
  # Accept comma or whitespace separators
  raw="${raw//,/ }"
  for tok in $raw; do
    [[ "$tok" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || continue
    [[ "$tok" =~ $EXCLUDE_RE ]] && continue
    out+=("$tok")
  done
  local IFS=,
  printf '%s' "${out[*]}"
}

export CLOUD_AGENT_INJECTED_SECRET_NAMES
export CLOUD_AGENT_ALL_SECRET_NAMES
CLOUD_AGENT_INJECTED_SECRET_NAMES="$(sanitize_secret_names "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
CLOUD_AGENT_ALL_SECRET_NAMES="$(sanitize_secret_names "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"

exec git "$@"
