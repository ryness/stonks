# Stonks Reports

Static site that renders AI-generated stock reports via Jekyll. The “new” and “rerun” links on the Pages site just open the `gostonks` GitHub Actions workflow with prefilled inputs.

## Prerequisites

- Ruby 3.x with Bundler for local Jekyll builds (`bundle install`, then `bundle exec jekyll serve`).
- Python 3.11 for the report generator (`python3.11 -m venv .venv && source .venv/bin/activate`).
- Install Python deps: `pip install -r requirements.txt`.

## GitHub Actions Setup

The workflow depends on several API keys. Add these repository secrets so the workflow dispatch links succeed:

- `OPENAI_API_KEY` – required for report generation.
- `GOOGLE_CSE_API_KEY` and `GOOGLE_CSE_ENGINE_ID` – optional, but enable Google Custom Search snippets.
- `NEWSAPI_KEY` – optional, adds recent news context.
- `GNEWS_API_KEY` – optional fallback for headline snippets (or place the key in `apikey-gnews.txt`).
- `GUARDIAN_API_KEY` – optional secondary fallback via The Guardian Open Platform (or use `apikey-guardian.txt`).
- `MASSIVE_API_KEY` – optional override for the default Massive search key.

With the secrets in place, the new/rerun links on GitHub Pages will open a prefilled workflow page; click **Run workflow** to kick off `gostonks.yml`. The workflow installs dependencies, runs `gostonks.py <TICKER>`, and commits the updated `_reports/` Markdown (plus the rotation state file) back to the default branch.

### GitHub Pages deployment

Pages now builds from GitHub Actions. In **Settings → Pages** set “Build and deployment” to **GitHub Actions**, then rely on `.github/workflows/pages.yml`. That workflow:

- checks out `main` and installs gems via Bundler (Ruby 3.3),
- runs `bundle exec jekyll build --destination _site`,
- uploads `_site/` as a Pages artifact, and
- deploys with `actions/deploy-pages@v4`.

Whenever `main` changes—or you run the workflow manually—the site is rebuilt and deployed without committing `_site/` back to the repo. A successful run of `gostonks.yml` also triggers this deployment automatically via a `workflow_run` hook.

### Historical data storage

Each run now appends structured market data to `data/stonks.db` (SQLite). The database tracks the raw OHLCV bars pulled from Massive.com/yfinance, the technical indicator payloads, and the derived snapshot metrics written into each report. `gostonks.yml` adds the database to its commit so the history stays with the repo; locally you can inspect it with commands like `sqlite3 data/stonks.db 'SELECT * FROM daily_snapshots ORDER BY trading_day DESC LIMIT 5'`.

### Scheduled rotation

The action also runs automatically every four hours. When invoked without a specific ticker it calls `gostonks.py --cycle`, which:

- looks at `_reports/*.md` to determine the sorted ticker list,
- reads/writes `.gostonks-state.json` to remember progress, and
- generates the next ticker in the queue before pushing the updated report.

## Local Report Generation

To create a report locally, ensure the API key files or environment variables are present, then run:

```bash
python gostonks.py AAPL
```

You can drop optional provider keys into text files in the repo root (`apikey-openai.txt`, `apikey-massive.txt`, `apikey-gnews.txt`, `apikey-guardian.txt`) if you prefer not to export environment variables. The search pipeline will try Google first, then fall back to NewsAPI, GNews, and finally The Guardian whenever earlier providers rate-limit or return no matches.

Generated markdown lands in `_reports/`. You can commit/push manually or let the workflow handle it.

To mimic the scheduled behaviour locally (cycling through tracked tickers), run:

```bash
python gostonks.py --cycle
```

### GodsEye (market overview)

Run `python gostonks.py GodsEye` to build the aggregate *GodsEye Market Report*. It fetches one-, seven-, and thirty-day change data for major equity indices, ETFs, futures, volatility, treasuries, commodities, and the US dollar, then summarises the tone with an LLM plus curated headlines aimed at the next 24 hours. The resulting Markdown lives in `_reports/GODSEYE.md`, complete with a QuickRef table showing the precomputed change stack so you can tweak the prompt later if needed.
# stonks
## Setup

Use the provided setup scripts to install both Python and Ruby dependencies locally (Python venv + Bundler to `vendor/bundle`).

- Windows (PowerShell): `./bin/setup.ps1`
  - If scripts are blocked: `Set-ExecutionPolicy -Scope Process RemoteSigned`
- macOS/Linux: `bash bin/setup.sh`

This will:
- Create `.venv` and install `requirements.txt` via pip
- Install Bundler (version from `Gemfile.lock`) and run `bundle install`

Serve the site: `bundle exec jekyll serve` then open http://127.0.0.1:4000

Notes:
- Ruby version is pinned via `.ruby-version` (3.3). Use your preferred version manager (rbenv/asdf) on macOS/Linux, or RubyInstaller on Windows.
- Gems are installed to `vendor/bundle` (configured by `.bundle/config` and ignored by `.gitignore`).
