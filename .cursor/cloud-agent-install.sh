#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  -r requirements.txt 2>/dev/null \
  || python3 -m pip install --quiet -r requirements.txt \
  || python3 -m pip install --break-system-packages --quiet \
       requests pillow python-dotenv numpy paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

# Fail fast if publish transport dependency is still missing
python3 -c "import paramiko" 2>/dev/null \
  || echo "[excalibur-cloud] WARN: paramiko missing; doctor --publish will FAIL until pip install paramiko"

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
