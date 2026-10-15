#!/usr/bin/env bash
# Alias / dual-mode wrapper around filter_commit_secret_env.
#
# Preferred before Cloud git commit:
#   eval "$(bash scripts/excalibur_blog_sanitize_secret_names.sh --export)"
#   git commit ...
#
# Also accepted:
#   eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh)"
#   source scripts/excalibur_blog_sanitize_secret_names.sh   # mutates current shell
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILTER="${SCRIPT_DIR}/excalibur_blog_filter_commit_secret_env.sh"

if [[ "${1:-}" == "--export" || "${1:-}" == "-e" ]]; then
  bash "$FILTER"
  exit 0
fi

# sourced or executed without --export: apply into current environment
# shellcheck disable=SC1090
eval "$(bash "$FILTER")"
