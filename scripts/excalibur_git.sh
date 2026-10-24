#!/usr/bin/env bash
# Thin git wrapper: normalize Cloud secret-name env, then exec git.
#
# Usage:
#   bash scripts/excalibur_git.sh commit -m "..."
#   bash scripts/excalibur_git.sh status
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# shellcheck disable=SC1091
eval "$(bash "$ROOT/scripts/excalibur_blog_filter_commit_secret_env.sh")"

exec git "$@"
