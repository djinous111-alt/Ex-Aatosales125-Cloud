#!/usr/bin/env bash
# Safe git wrapper for Cloud Agents: sanitize secret-name injection before hooks.
# Usage: scripts/excalibur_git.sh commit -m "..."
#        scripts/excalibur_git.sh push -u origin <branch>
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck source=/dev/null
source "$ROOT/scripts/excalibur_blog_filter_secret_names.sh"

exec git "$@"
