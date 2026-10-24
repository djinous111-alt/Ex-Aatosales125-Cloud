#!/usr/bin/env bash
# Safe git wrapper for Cloud Agents: sanitize secret-name lists, then run git.
# Usage:
#   source scripts/excalibur_git.sh
#   excalibur_git commit -m "..."
#   # or one-shot:
#   scripts/excalibur_git.sh commit -m "..."

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck disable=SC1091
source "$ROOT/scripts/excalibur_blog_filter_secret_names.sh"

excalibur_git() {
  # Re-filter in case env changed
  # shellcheck disable=SC1091
  source "$ROOT/scripts/excalibur_blog_filter_secret_names.sh"
  git "$@"
}

# If executed (not sourced), run git with remaining args
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  if [[ "$#" -eq 0 ]]; then
    echo "usage: scripts/excalibur_git.sh <git-args...>" >&2
    echo "   or: source scripts/excalibur_git.sh && excalibur_git <git-args...>" >&2
    exit 2
  fi
  exec git "$@"
fi
