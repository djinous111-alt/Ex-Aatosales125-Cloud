#!/usr/bin/env bash
# Git wrapper that sanitizes CLOUD_AGENT_*_SECRET_NAMES before hooks run.
# Usage: bash scripts/excalibur_git.sh commit -m "..."
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck disable=SC1091
source "$ROOT/scripts/sanitize_cloud_secret_names.sh"
exec git "$@"
