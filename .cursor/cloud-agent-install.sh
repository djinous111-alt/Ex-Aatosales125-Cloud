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

# Harden Cloud secret-scan pre-commit (skip invalid names; marketing URL allowlist).
HOOK_SRC="scripts/pre-commit.cursor"
if [[ -f "$HOOK_SRC" ]]; then
  for hooks_dir in /root/.cursor/agent-hooks/*/ ; do
    [[ -d "$hooks_dir" ]] || continue
    cp "$HOOK_SRC" "${hooks_dir}pre-commit.cursor"
    chmod +x "${hooks_dir}pre-commit.cursor"
    echo "[excalibur-cloud] installed pre-commit.cursor → ${hooks_dir}"
  done
fi

echo "[excalibur-cloud] install ok"
