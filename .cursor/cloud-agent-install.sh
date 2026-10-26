#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt \
    || python3 -m pip install --quiet -r requirements.txt
else
  python3 -m pip install --break-system-packages --quiet \
    requests pillow numpy paramiko python-dotenv \
    || python3 -m pip install --quiet requests pillow numpy paramiko python-dotenv
fi

# Fail fast if SSH publish dependency is still missing.
python3 -c "import paramiko, PIL, numpy; print('[excalibur-cloud] deps ok: paramiko+Pillow+numpy')"

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
