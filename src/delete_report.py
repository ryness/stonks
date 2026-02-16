#!/usr/bin/env python3
"""Delete a ticker report and related local artifacts."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "_reports"
LOGOS_DIR = ROOT_DIR / "assets" / "logos"
DB_PATH = ROOT_DIR / "data" / "stonks.db"


def normalize_ticker(raw: str) -> str:
    ticker = (raw or "").strip().upper()
    if not ticker:
        raise ValueError("Ticker is required.")
    return ticker


def delete_report_file(ticker: str) -> bool:
    report_path = REPORTS_DIR / f"{ticker}.md"
    if not report_path.exists():
        return False
    report_path.unlink()
    return True


def delete_logo_files(ticker: str) -> int:
    if not LOGOS_DIR.exists():
        return 0
    deleted = 0
    for path in LOGOS_DIR.glob(f"{ticker}.*"):
        if path.is_file():
            path.unlink()
            deleted += 1
    return deleted


def delete_db_rows(ticker: str) -> int:
    if not DB_PATH.exists():
        return 0
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.execute("DELETE FROM tickers WHERE symbol = ?", (ticker,))
        conn.commit()
        return int(cursor.rowcount or 0)


def main() -> int:
    parser = argparse.ArgumentParser(description="Delete a ticker report and related data.")
    parser.add_argument("ticker", help="Ticker symbol to delete, e.g. AAPL")
    args = parser.parse_args()

    try:
        ticker = normalize_ticker(args.ticker)
    except ValueError as error:
        print(str(error))
        return 2

    report_deleted = delete_report_file(ticker)
    logos_deleted = delete_logo_files(ticker)
    ticker_rows_deleted = delete_db_rows(ticker)

    if not report_deleted and logos_deleted == 0 and ticker_rows_deleted == 0:
        print(f"No data found for {ticker}; nothing to delete.")
        return 0

    print(
        f"Deleted {ticker}: "
        f"report={'yes' if report_deleted else 'no'}, "
        f"logos={logos_deleted}, "
        f"db_rows={ticker_rows_deleted}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
