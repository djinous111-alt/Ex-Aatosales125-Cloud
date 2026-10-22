#!/usr/bin/env bash
# Safe git wrapper for Excalibur Cloud Agents.
# Filters CLOUD_AGENT_INJECTED_SECRET_NAMES to valid bash identifiers before
# invoking git, so Cursor pre-commit hooks do not die on `${!SECRET_NAME}`
# when Dashboard injects URL-like / redacted "names".
#
# Usage:
#   scripts/excalibur_git.sh status
#   scripts/excalibur_git.sh add -A
#   scripts/excalibur_git.sh commit -m "message"
#   scripts/excalibur_git.sh push -u origin HEAD
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -f scripts/excalibur_blog_filter_secret_names.sh ]]; then
  # shellcheck disable=SC1091
  eval "$(bash scripts/excalibur_blog_filter_secret_names.sh | sed -n 's/^CLOUD_AGENT_INJECTED_SECRET_NAMES=/export CLOUD_AGENT_INJECTED_SECRET_NAMES=/p')"
fi

exec git "$@"
