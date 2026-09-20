#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Prefer requirements.txt (includes paramiko for SSH publish); fallback to explicit pins.
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt 2>/dev/null \
    || python3 -m pip install --quiet -r requirements.txt
else
  python3 -m pip install --break-system-packages --quiet \
    requests pillow python-dotenv numpy paramiko 2>/dev/null \
    || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko
fi

# Ensure SSH publish transport is importable even if requirements.txt was trimmed.
python3 -m pip install --break-system-packages --quiet paramiko 2>/dev/null \
  || python3 -m pip install --quiet paramiko

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
