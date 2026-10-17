#!/usr/bin/env bash
# Filter CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers before git commit.
#
# Cloud inject may append non-identifiers (URLs, "[REDACTED]", empty pieces). The
# Cursor pre-commit.cursor hook does `${!SECRET_NAME}` and aborts with
# "invalid variable name" when a token is not a legal identifier.
#
# Usage (same shell as commit):
#   eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
#   git commit -m "..."
#
# Prints only export lines suitable for eval; no secret values.

set -euo pipefail

raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"
if [[ -z "$raw" ]]; then
  printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=\n'
  exit 0
fi

filtered=()
IFS=',' read -ra parts <<< "$raw"
for name in "${parts[@]}"; do
  # trim whitespace
  name="${name#"${name%%[![:space:]]*}"}"
  name="${name%"${name##*[![:space:]]}"}"
  if [[ -z "$name" ]]; then
    continue
  fi
  if [[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    filtered+=("$name")
  fi
done

joined="$(IFS=','; echo "${filtered[*]}")"
# %q keeps the export safe for eval even if empty
printf 'export CLOUD_AGENT_INJECTED_SECRET_NAMES=%q\n' "$joined"
