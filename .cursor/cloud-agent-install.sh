#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Prefer requirements.txt (paramiko required for SSH publish); also install
# common Cloud runtime deps used by cover/QA helpers.
python3 -m pip install --break-system-packages --quiet \
  -r requirements.txt requests python-dotenv 2>/dev/null \
  || python3 -m pip install --quiet -r requirements.txt requests python-dotenv

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
