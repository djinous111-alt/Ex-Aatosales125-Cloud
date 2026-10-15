#!/usr/bin/env bash
# Idempotent update command for Cursor Cloud Agents (Excalibur BLOG).
set -euo pipefail

echo "[excalibur-cloud] install start"
python3 --version
git --version

python3 -m pip install --break-system-packages --quiet \
  requests pillow python-dotenv paramiko 2>/dev/null \
  || python3 -m pip install --quiet requests pillow python-dotenv paramiko

mkdir -p .cursor/excalibur-blog-fragments
touch .cursor/excalibur-blog-handoff.md

# Materialize memory/site.env.local from Cloud Secrets when missing.
# Values are shell-quoted; never echo secret values.
SITE_ENV="memory/site.env.local"
if [[ ! -f "$SITE_ENV" ]]; then
  mkdir -p memory
  {
    echo "# Auto-generated from Cloud Secrets by cloud-agent-install.sh"
    echo "# Do not commit."
    for key in \
      PUBLIC_SITE_URL WP_HOME WP_SITE_URL \
      SSH_HOST SSH_PORT SSH_USER SSH_PASS SSH_PASSWORD SSH_ROOT \
      EXCALIBUR_BLOG_ALLOW_PUBLISH \
      CATALOG_URL TELEGRAM_URL MAX_URL \
      KIE_API_KEY
    do
      # indirect expansion; empty if unset
      val="${!key-}"
      if [[ -n "${val}" ]]; then
        printf '%s=%q\n' "$key" "$val"
      fi
    done
    if [[ -z "${SSH_ROOT-}" ]]; then
      echo "SSH_ROOT=."
    fi
  } > "$SITE_ENV"
  echo "[excalibur-cloud] wrote $SITE_ENV from Cloud Secrets (keys only logged)"
  awk -F= '/^[A-Z_]+=/{print $1}' "$SITE_ENV" | sed 's/^/[excalibur-cloud] site.env key: /'
else
  echo "[excalibur-cloud] $SITE_ENV already present"
fi

echo "[excalibur-cloud] install ok"
