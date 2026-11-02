#!/usr/bin/env bash
# Safe git wrapper for Excalibur BLOG agents.
# Always filters CLOUD_AGENT_*_SECRET_NAMES to bash identifiers before commit/hooks.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck disable=SC1091
source "$ROOT/scripts/excalibur_blog_filter_commit_secret_env.sh"

usage() {
  cat <<'EOF'
Usage:
  scripts/excalibur_git.sh commit [git commit args...]
  scripts/excalibur_git.sh status|add|push|diff|log|...  — passthrough to git after filter

Examples:
  bash scripts/excalibur_git.sh commit -m "fix: ..."
  eval "$(bash scripts/excalibur_blog_filter_commit_secret_env.sh && declare -p CLOUD_AGENT_INJECTED_SECRET_NAMES CLOUD_AGENT_ALL_SECRET_NAMES 2>/dev/null)"
EOF
}

if [[ $# -lt 1 ]]; then
  usage
  exit 2
fi

cmd="$1"
shift || true

case "$cmd" in
  -h|--help|help)
    usage
    exit 0
    ;;
  commit)
    exec git commit "$@"
    ;;
  *)
    exec git "$cmd" "$@"
    ;;
esac
