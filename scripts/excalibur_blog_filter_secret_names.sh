#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers.
# Use before git commit when Cloud pre-commit fails with "invalid variable name".
# Usage: source scripts/excalibur_blog_filter_secret_names.sh
#    or: eval "$(scripts/excalibur_blog_filter_secret_names.sh --export)"

set -euo pipefail

EXPORT=0
if [[ "${1:-}" == "--export" ]]; then
  EXPORT=1
fi

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$raw" ]]; then
  if [[ "$EXPORT" -eq 1 ]]; then
    printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' ""
  fi
  exit 0
fi

IFS=',' read -ra NAMES <<< "$raw"
filtered=()
skipped=0
for name in "${NAMES[@]}"; do
  name="${name#"${name%%[![:space:]]*}"}"
  name="${name%"${name##*[![:space:]]}"}"
  [[ -z "$name" ]] && continue
  if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    filtered+=("$name")
  else
    skipped=$((skipped + 1))
  fi
done

joined=$(IFS=','; echo "${filtered[*]}")
export CLOUD_AGENT_INJECTED_SECRET_NAMES="$joined"

if [[ "$EXPORT" -eq 1 ]]; then
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$joined"
else
  echo "[excalibur] secret names kept=${#filtered[@]} skipped_invalid=$skipped" >&2
fi
