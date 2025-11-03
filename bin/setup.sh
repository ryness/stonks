#!/usr/bin/env bash
set -euo pipefail

# Cross-platform friendly project setup for macOS/Linux.
# - Creates .venv and installs requirements.txt
# - Installs Bundler (matching Gemfile.lock) and runs bundle install

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
cd "$SCRIPT_DIR/.."

if [[ ! -f Gemfile ]]; then
  echo "[warn] Gemfile not found. Are you in the repo root?" >&2
fi

echo "==> Setting up Python virtual environment (.venv)"
if [[ ! -d .venv ]]; then
  if command -v python3 >/dev/null 2>&1; then
    python3 -m venv .venv || python -m venv .venv
  elif command -v python >/dev/null 2>&1; then
    python -m venv .venv
  else
    echo "[warn] Python not found on PATH. Install Python 3.12+ and rerun." >&2
  fi
fi

if [[ -x .venv/bin/python ]]; then
  .venv/bin/python -m pip install -U pip setuptools wheel
  if [[ -f requirements.txt ]]; then
    echo "==> Installing Python requirements"
    .venv/bin/python -m pip install -r requirements.txt
  fi
else
  echo "[warn] Skipping Python deps; .venv/bin/python not found" >&2
fi

echo "==> Setting up Ruby gems with Bundler"
if ! command -v ruby >/dev/null 2>&1; then
  echo "[warn] Ruby not found. Install Ruby (e.g., rbenv or brew install ruby) then rerun." >&2
else
  bundler_version="2.7.1" # from Gemfile.lock
  if ! gem list -i bundler -v "$bundler_version" >/dev/null 2>&1; then
    echo "==> Installing bundler $bundler_version"
    gem install bundler -v "$bundler_version" >/dev/null
  fi
  echo "==> Installing Ruby gems (vendor/bundle)"
  bundle install
fi

echo
echo "All set. Common commands:"
echo "  - Activate Python:  source .venv/bin/activate"
echo "  - Serve Jekyll:    bundle exec jekyll serve"

