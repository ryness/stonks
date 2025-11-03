<#
Cross-platform friendly project setup for Windows PowerShell.

Does:
- Ensures a local Python venv at .venv and installs requirements.txt
- Ensures Bundler (matching Gemfile.lock) and installs Ruby gems to vendor/bundle

Run:  ./bin/setup.ps1
If script execution is blocked: Set-ExecutionPolicy -Scope Process RemoteSigned
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Info($msg) { Write-Host "==> $msg" -ForegroundColor Cyan }
function Write-Warn($msg) { Write-Host "!!  $msg" -ForegroundColor Yellow }

# Ensure we run from repo root
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent
Set-Location $repoRoot
if (-not (Test-Path Gemfile)) { Write-Warn "Gemfile not found. Are you in the repo root? ($repoRoot)" }

# --- Python ---
Write-Info "Setting up Python virtual environment (.venv)"
if (-not (Test-Path '.venv')) {
  if (Get-Command python -ErrorAction SilentlyContinue) {
    python -m venv .venv
  } else {
    Write-Warn "Python not found on PATH. Install Python 3.12+ and rerun."
  }
}

$venvPython = Join-Path '.venv' 'Scripts/python.exe'
if (Test-Path $venvPython) {
  & $venvPython -m pip install -U pip setuptools wheel
  if (Test-Path 'requirements.txt') {
    Write-Info "Installing Python requirements"
    & $venvPython -m pip install -r requirements.txt
  }
} else {
  Write-Warn "Skipping Python deps; .venv Python not found at $venvPython"
}

# --- Ruby / Bundler ---
Write-Info "Setting up Ruby gems with Bundler"
if (-not (Get-Command ruby -ErrorAction SilentlyContinue)) {
  Write-Warn "Ruby not found. Install Ruby (Windows: winget install -e --id RubyInstallerTeam.RubyWithDevKit.3.3) then rerun."
} else {
  $bundlerVersion = '2.7.1' # from Gemfile.lock
  $hasBundler = & gem list -i bundler -v $bundlerVersion 2>$null
  if (-not $hasBundler) {
    Write-Info "Installing bundler $bundlerVersion"
    & gem install bundler -v $bundlerVersion | Out-Null
  }
  Write-Info "Installing Ruby gems (vendor/bundle)"
  & bundle install
}

Write-Host "\nAll set. Common commands:" -ForegroundColor Green
Write-Host "  - Activate Python:  .\\.venv\\Scripts\\Activate.ps1"
Write-Host "  - Serve Jekyll:    bundle exec jekyll serve"

