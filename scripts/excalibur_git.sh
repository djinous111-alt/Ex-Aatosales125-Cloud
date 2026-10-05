#!/usr/bin/env bash
# Sanitize Cloud Agent secret-name env lists, then run git.
# Fixes pre-commit.cursor "invalid variable name" when CLOUD_AGENT_*_SECRET_NAMES
# contains placeholders like [REDACTED] that are not valid bash identifiers.
#
# Usage: bash scripts/excalibur_git.sh commit -m "..."
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck disable=SC1091
source "$ROOT/scripts/sanitize_cloud_secret_names.sh"

exec git "$@"
