#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv numpy paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

# Non-secret publish default: SSH login cwd. Secrets still come from Cloud env.
mkdir -p memory
if [[ ! -f memory/site.env.local ]]; then
  printf 'SSH_ROOT=.\n' > memory/site.env.local
  echo "[excalibur-cloud] created memory/site.env.local with SSH_ROOT=."
elif ! grep -q '^SSH_ROOT=' memory/site.env.local 2>/dev/null; then
  printf '\nSSH_ROOT=.\n' >> memory/site.env.local
  echo "[excalibur-cloud] appended SSH_ROOT=. to memory/site.env.local"
fi

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

echo "[excalibur-cloud] install ok"
