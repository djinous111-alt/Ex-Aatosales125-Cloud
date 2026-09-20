#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Install publish/runtime deps from requirements.txt (paramiko, Pillow, numpy).
# PEP 668: Cloud VMs often need --break-system-packages; fall back to --user.
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt \
    || python3 -m pip install --user --quiet -r requirements.txt
fi

# Extra helpers used by research/doctor (not always in requirements.txt).
python3 -m pip install --break-system-packages --quiet \
  requests python-dotenv 2>/dev/null \
  || python3 -m pip install --user --quiet requests python-dotenv

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Smoke-check paramiko so publish does not fail at first SSH call.
python3 -c "import paramiko; print('[excalibur-cloud] paramiko ok')" \
  || echo "[excalibur-cloud] WARN: paramiko import failed — publish will need pip install paramiko"

echo "[excalibur-cloud] install ok"
