#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Keep in sync with requirements.txt / .cursor/Dockerfile (paramiko required for SSH publish).
python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko numpy 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko numpy

python3 - <<'PY'
import importlib.util
import sys

need = []
for mod in ("PIL", "numpy", "paramiko", "dotenv", "requests"):
    if importlib.util.find_spec(mod) is None:
        need.append(mod)
if need:
    print("[excalibur-cloud] MISSING modules after install:", ", ".join(need), file=sys.stderr)
    sys.exit(1)
print("[excalibur-cloud] verified: PIL numpy paramiko dotenv requests")
PY

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
