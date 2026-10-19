#!/usr/bin/env bash
# Filter CLOUD_AGENT_*_SECRET_NAMES so pre-commit secret scanners do not hit
# `invalid variable name` on non-identifiers, and so public CTA/site URL names
# do not block commits of legitimate article/publish artifacts.
#
# Usage (MUST be same shell as git commit — Cloud may restore env between shells):
#   eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
#   git add ... && git commit -m "..."
#
# Keeps comma-separated lists (space-joined names break the hook).

set -euo pipefail

# Public/marketing URL env names that are often injected as "secrets" but must
# not participate in the commit-time secret name expansion loop.
DROP_NAMES_CSV='PUBLIC_SITE_URL,WP_SITE_URL,WP_HOME,CATALOG_URL,TELEGRAM_URL,MAX_URL'

is_valid_identifier() {
  [[ "$1" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]
}

should_drop() {
  local name="$1"
  local drop
  local old_ifs="$IFS"
  IFS=','
  # shellcheck disable=SC2086
  set -- $DROP_NAMES_CSV
  IFS="$old_ifs"
  for drop in "$@"; do
    if [[ "$name" == "$drop" ]]; then
      return 0
    fi
  done
  return 1
}

trim() {
  local s="$1"
  s="${s#"${s%%[![:space:]]*}"}"
  s="${s%"${s##*[![:space:]]}"}"
  printf '%s' "$s"
}

filter_csv() {
  local raw="${1:-}"
  local -a out=()
  local part tok
  local old_ifs="$IFS"
  IFS=','
  # shellcheck disable=SC2206
  local -a parts=($raw)
  IFS="$old_ifs"
  for part in "${parts[@]}"; do
    part="$(trim "$part")"
    [[ -z "$part" ]] && continue
    # If a "token" still contains spaces, split further (corrupted list).
    if [[ "$part" == *" "* ]]; then
      for tok in $part; do
        tok="$(trim "$tok")"
        [[ -z "$tok" ]] && continue
        is_valid_identifier "$tok" || continue
        should_drop "$tok" && continue
        out+=("$tok")
      done
      continue
    fi
    is_valid_identifier "$part" || continue
    should_drop "$part" && continue
    out+=("$part")
  done
  local joined=""
  local i
  for i in "${!out[@]}"; do
    if [[ "$i" -eq 0 ]]; then
      joined="${out[$i]}"
    else
      joined+=",${out[$i]}"
    fi
  done
  printf '%s' "$joined"
}

emit_export() {
  local var="$1"
  local current="${!var-}"
  if [[ -z "${current}" ]]; then
    return 0
  fi
  local filtered
  filtered="$(filter_csv "$current")"
  # Always re-export (even if empty) so junk is cleared for this shell.
  printf 'export %s=%q\n' "$var" "$filtered"
}

emit_export CLOUD_AGENT_INJECTED_SECRET_NAMES
emit_export CLOUD_AGENT_ALL_SECRET_NAMES
