#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# numpy required by doctor/cover tooling; apt python3-numpy preferred in Dockerfile,
# pip fallback keeps warm Cloud VMs / install-only updates healthy.
if ! python3 -c "import numpy" 2>/dev/null; then
  apt-get update -qq && apt-get install -y --no-install-recommends python3-numpy \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    || true
fi
python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
