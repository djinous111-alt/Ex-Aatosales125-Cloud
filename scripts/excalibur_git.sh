#!/usr/bin/env bash
# Safe git wrapper for Excalibur Cloud commits: sanitize injected secret names
# before commit hooks expand ${!SECRET_NAME}.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck source=sanitize_cloud_secret_names.sh
source "$ROOT/scripts/sanitize_cloud_secret_names.sh"
sanitize_cloud_secret_names

if [[ "${1:-}" == "commit" ]]; then
  shift
  exec git commit "$@"
fi

exec git "$@"
