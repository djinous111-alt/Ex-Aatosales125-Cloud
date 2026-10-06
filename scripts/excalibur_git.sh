#!/usr/bin/env bash
# Excalibur BLOG — safe git wrapper for Cloud Agent commits.
#
# Why:
# 1) CLOUD_AGENT_INJECTED_SECRET_NAMES sometimes includes URL-shaped "names"
#    that crash bash `${!name}` with "invalid variable name".
# 2) PUBLIC_SITE_URL / WP_SITE_URL / WP_HOME are public site bases; committed
#    artifacts intentionally use placeholders. Scanning them as secrets causes
#    false positives on llms.txt / schema / ledger.
#
# Usage:
#   bash scripts/excalibur_git.sh commit -m "message"
#   bash scripts/excalibur_git.sh status
#   bash scripts/excalibur_git.sh add path...
#   bash scripts/excalibur_git.sh push ...
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

is_bash_identifier() {
  [[ "$1" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]
}

sanitize_secret_name_list() {
  local raw="${1:-}"
  local -a kept=()
  local name
  local IFS=','
  # shellcheck disable=SC2206
  local -a names=(${raw})
  for name in "${names[@]}"; do
    name="${name#"${name%%[![:space:]]*}"}"
    name="${name%"${name##*[![:space:]]}"}"
    if [ -z "$name" ]; then
      continue
    fi
    if ! is_bash_identifier "$name"; then
      echo "[excalibur_git] skip non-identifier secret name: ${name:0:48}" >&2
      continue
    fi
    case "$name" in
      PUBLIC_SITE_URL|WP_SITE_URL|WP_HOME)
        echo "[excalibur_git] skip public-site secret name from scan: $name" >&2
        continue
        ;;
    esac
    kept+=("$name")
  done
  (IFS=','; printf '%s' "${kept[*]}")
}

export CLOUD_AGENT_INJECTED_SECRET_NAMES
export CLOUD_AGENT_ALL_SECRET_NAMES
CLOUD_AGENT_INJECTED_SECRET_NAMES="$(sanitize_secret_name_list "${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}")"
CLOUD_AGENT_ALL_SECRET_NAMES="$(sanitize_secret_name_list "${CLOUD_AGENT_ALL_SECRET_NAMES:-}")"

if [ "$#" -eq 0 ]; then
  echo "Usage: bash scripts/excalibur_git.sh <git-args...>" >&2
  echo "Example: bash scripts/excalibur_git.sh commit -m \"fix: ...\"" >&2
  exit 2
fi

exec git "$@"
