#!/usr/bin/env bash
# Sanitize CLOUD_AGENT_INJECTED_SECRET_NAMES before Cursor pre-commit secret-scan.
#
# Usage (before git commit that embeds public marketing URLs in schema/JSON-LD):
#   eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
#
# Effects:
# - Drops non-identifier tokens (e.g. "[REDACTED]") that crash `${!NAME}` expansion
# - Omits public marketing URL secret names whose values legitimately appear in
#   BlogPosting / author sameAs JSON-LD (not private credentials)
# - Re-exports a comma-separated list (Cursor hook format)
#
# Does NOT print secret values.

set -euo pipefail

PUBLIC_URL_SECRET_NAMES_REGEX='^(PUBLIC_SITE_URL|WP_SITE_URL|WP_HOME|CATALOG_URL|TELEGRAM_URL|MAX_URL|INSTAGRAM_URL)$'

is_shell_identifier() {
  local name="$1"
  [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]
}

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$raw" ]]; then
  printf 'true\n'
  exit 0
fi

filtered=()
dropped_public=()
dropped_invalid=()

# Normalize separators to newlines, then read lines
normalized="$(printf '%s' "$raw" | tr ', \t' '\n\n\n')"
while IFS= read -r name; do
  name="${name//$'\r'/}"
  name="$(printf '%s' "$name" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  [[ -z "$name" ]] && continue

  if ! is_shell_identifier "$name"; then
    dropped_invalid+=("$name")
    continue
  fi

  if [[ "$name" =~ $PUBLIC_URL_SECRET_NAMES_REGEX ]]; then
    dropped_public+=("$name")
    continue
  fi

  filtered+=("$name")
done <<< "$normalized"

# Comma-separated export (matches Cursor CLOUD_AGENT_INJECTED_SECRET_NAMES format)
joined=""
if ((${#filtered[@]})); then
  joined="$(IFS=','; echo "${filtered[*]}")"
fi
printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$joined"

if ((${#dropped_invalid[@]})); then
  echo "[excalibur-secret-filter] dropped non-identifier secret names: ${dropped_invalid[*]}" >&2
fi
if ((${#dropped_public[@]})); then
  echo "[excalibur-secret-filter] omitted public URL secret names for commit scan: ${dropped_public[*]}" >&2
fi
