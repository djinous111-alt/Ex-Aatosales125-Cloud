#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy

# Fallback for environments where apt python3-numpy is preferred
if ! python3 -c "import numpy" >/dev/null 2>&1; then
  if command -v apt-get >/dev/null 2>&1; then
    apt-get update -qq && apt-get install -y --no-install-recommends python3-numpy \
      && apt-get clean && rm -rf /var/lib/apt/lists/* || true
  fi
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
