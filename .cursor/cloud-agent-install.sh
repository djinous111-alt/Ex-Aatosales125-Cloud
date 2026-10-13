#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

# Publish SSH transport needs paramiko; Pillow/numpy for cover/QA.
# PEP 668: prefer --break-system-packages on Cloud images.
python3 -m pip install --break-system-packages --quiet \
  -r requirements.txt \
  requests python-dotenv \
  2>/dev/null \
  || python3 -m pip install --break-system-packages --quiet \
    Pillow numpy paramiko requests python-dotenv \
  || python3 -m pip install --quiet \
    Pillow numpy paramiko requests python-dotenv

python3 - <<'PY'
import importlib
for name in ("PIL", "numpy", "paramiko"):
    importlib.import_module(name)
    print(f"[excalibur-cloud] ok import {name}")
PY

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md
chmod +x scripts/excalibur_git.sh 2>/dev/null || true

echo "[excalibur-cloud] install ok"
