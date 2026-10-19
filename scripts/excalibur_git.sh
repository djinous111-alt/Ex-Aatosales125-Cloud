#!/usr/bin/env bash
# Git wrapper that filters invalid CLOUD_AGENT_* secret names before hooks run.
# Prefer this over `git commit --no-verify` when pre-commit.cursor hits
# `invalid variable name` from non-bash-safe Dashboard secret names.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck source=excalibur_blog_filter_commit_secret_env.sh
source "$ROOT/scripts/excalibur_blog_filter_commit_secret_env.sh"

exec git "$@"
