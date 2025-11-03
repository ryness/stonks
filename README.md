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
- `MASSIVE_API_KEY` – optional override for the default Massive search key.

With the secrets in place, the new/rerun links on GitHub Pages will open a prefilled workflow page; click **Run workflow** to kick off `gostonks.yml`. The workflow installs dependencies, runs `gostonks.py <TICKER>`, and commits the updated `_reports/` Markdown back to the default branch, triggering a Pages rebuild.

## Local Report Generation

To create a report locally, ensure the API key files or environment variables are present, then run:

```bash
python gostonks.py AAPL
```

Generated markdown lands in `_reports/`. You can commit/push manually or let the workflow handle it.
