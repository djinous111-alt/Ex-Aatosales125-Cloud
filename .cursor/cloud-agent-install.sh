#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  -r requirements.txt 2>/dev/null \
  || python3 -m pip install --break-system-packages --quiet \
    requests pillow python-dotenv numpy paramiko \
  || python3 -m pip install --quiet requests pillow python-dotenv numpy paramiko

# Harden platform pre-commit: skip non-bash-identifier entries in
# CLOUD_AGENT_INJECTED_SECRET_NAMES (URLs mistakenly injected as "names"
# make ${!SECRET_NAME} abort with "invalid variable name").
# Also normalize space-separated lists → comma-separated before the hook runs
# by wrapping the secret-name split when possible.
harden_precommit_secret_names() {
  local hook
  for hook in /root/.cursor/agent-hooks/*/pre-commit.cursor /root/.cursor/agent-hooks/*/commit-msg.cursor; do
    [[ -f "$hook" ]] || continue
    if grep -q 'EXCALIBUR_SECRET_NAME_ID_GUARD' "$hook"; then
      continue
    fi
    if grep -q 'for SECRET_NAME in "\${SECRET_NAMES\[@\]}"; do' "$hook"; then
      python3 - "$hook" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
needle = 'for SECRET_NAME in "${SECRET_NAMES[@]}"; do\n'
guard = (
    needle
    + '    # EXCALIBUR_SECRET_NAME_ID_GUARD\n'
    + '    if [[ ! "$SECRET_NAME" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then\n'
    + '        continue\n'
    + '    fi\n'
)
if needle in text and "EXCALIBUR_SECRET_NAME_ID_GUARD" not in text:
    path.write_text(text.replace(needle, guard, 1), encoding="utf-8")
    print(f"[excalibur-cloud] patched secret-name guard into {path}")
PY
    fi
    # Normalize space-separated CLOUD_AGENT_*SECRET_NAMES to comma-separated
    # before IFS=',' read (INC-0930).
    if grep -q 'IFS=.,. read -ra SECRET_NAMES' "$hook" || grep -q "IFS=',' read -ra SECRET_NAMES" "$hook"; then
      if ! grep -q 'EXCALIBUR_SECRET_NAMES_NORMALIZE' "$hook"; then
        python3 - "$hook" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
marker = "EXCALIBUR_SECRET_NAMES_NORMALIZE"
if marker in text:
    raise SystemExit(0)
needle = 'IFS=\',\' read -ra SECRET_NAMES <<< "$CLOUD_AGENT_INJECTED_SECRET_NAMES"'
if needle not in text:
    raise SystemExit(0)
replacement = (
    "# " + marker + "\n"
    + '_excalibur_raw="${CLOUD_AGENT_INJECTED_SECRET_NAMES:-}"\n'
    + '_excalibur_norm="$(printf \'%s\' "$_excalibur_raw" | tr \' \\t\' \',\' | tr -s \',\' | sed \'s/^,//;s/,$//\')"\n'
    + 'CLOUD_AGENT_INJECTED_SECRET_NAMES="$_excalibur_norm"\n'
    + needle
)
path.write_text(text.replace(needle, replacement, 1), encoding="utf-8")
print(f"[excalibur-cloud] patched secret-names normalize into {path}")
PY
      fi
    fi
  done
}
harden_precommit_secret_names || true

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Materialize gitignored publish env from Cloud Secrets when missing (no secrets printed).
if [[ ! -f memory/site.env.local ]]; then
  python3 - <<'PY' || true
from pathlib import Path
import os
root = Path(".")
try:
    import sys
    sys.path.insert(0, "scripts")
    from excalibur_blog_wp_publish import ensure_site_env_local
    ensure_site_env_local(root)
except Exception:
    pass
PY
fi

echo "[excalibur-cloud] install ok"
