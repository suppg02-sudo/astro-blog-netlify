#!/bin/bash
set -euo pipefail
# Wrapper: calls the Python sync script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$SCRIPT_DIR/sync-posts.py" "$@"
