#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Pillow: cover apply/split decode; numpy: cover quad split geometry helpers.
# Doctor treats both as required for a healthy cover path.
python3 -m pip install --break-system-packages --quiet \
  requests pillow numpy python-dotenv 2>/dev/null \
  || python3 -m pip install --quiet requests pillow numpy python-dotenv

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
