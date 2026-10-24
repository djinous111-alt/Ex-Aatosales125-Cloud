#!/usr/bin/env bash
# Git wrapper that sanitizes CLOUD_AGENT_*_SECRET_NAMES before hooks run.
# Prefer this over `git commit --no-verify` when pre-commit.cursor hits
# `invalid variable name` from non-bash-safe Dashboard secret names.
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
