#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Skip non-identifier secret names in Cursor agent git hooks (URL-as-name → invalid variable name).
if [[ -x scripts/excalibur_blog_patch_agent_hooks.sh ]]; then
  bash scripts/excalibur_blog_patch_agent_hooks.sh || echo "[excalibur-cloud] WARN: agent-hooks patch skipped"
fi

echo "[excalibur-cloud] install ok"
