#!/usr/bin/env bash
# Excalibur BLOG — safe git wrapper for Cloud Agent commits.
#
# Why:
# 1) CLOUD_AGENT_INJECTED_SECRET_NAMES sometimes includes URL-shaped "names"
#    that crash bash `${!name}` with "invalid variable name".
# 2) Prefer this wrapper (or filter_secret_names.py --export) over --no-verify.
#
# Usage:
#   bash scripts/excalibur_git.sh commit -m "message"
#   bash scripts/excalibur_git.sh status
#   bash scripts/excalibur_git.sh add path...
#   bash scripts/excalibur_git.sh push ...
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# shellcheck source=sanitize_cloud_secret_names.sh
source "$ROOT/scripts/sanitize_cloud_secret_names.sh"

if [ "$#" -eq 0 ]; then
  echo "Usage: bash scripts/excalibur_git.sh <git-args...>" >&2
  echo "Example: bash scripts/excalibur_git.sh commit -m \"fix: ...\"" >&2
  exit 2
fi

exec git "$@"
