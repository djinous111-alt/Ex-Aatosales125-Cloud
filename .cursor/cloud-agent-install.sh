#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko numpy 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko numpy

# Optional: if requirements.txt exists, keep install aligned.
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt 2>/dev/null \
    || python3 -m pip install --quiet -r requirements.txt || true
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
