#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Prefer requirements.txt so SSH publish (paramiko) and image tools stay in sync.
if [[ -f requirements.txt ]]; then
  python3 -m pip install --break-system-packages --quiet -r requirements.txt \
    || python3 -m pip install --quiet -r requirements.txt
fi

# Explicit fallback if requirements.txt is missing or incomplete.
python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

python3 -c "import paramiko, PIL, numpy; print('[excalibur-cloud] deps ok: paramiko+Pillow+numpy')"

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
