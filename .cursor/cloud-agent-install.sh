#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

# Keep Dockerfile + requirements.txt in sync: paramiko is required for SSH publish.
python3 - <<'PY'
import importlib.util
missing = [name for name in ("PIL", "numpy", "paramiko") if importlib.util.find_spec(name) is None]
if missing:
    raise SystemExit(f"missing python modules after install: {missing}")
print("OK python modules: Pillow numpy paramiko")
PY

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
