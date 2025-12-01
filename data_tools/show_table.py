#!/usr/bin/env python3
"""
Print rows from a table in the stonks SQLite database.

Usage:
  python data_tools/show_table.py [--table runs] [--db data/stonks.db] [--limit 20]
"""

import argparse
import sqlite3
from pathlib import Path
from typing import Iterable, List


def list_tables(conn: sqlite3.Connection) -> List[str]:
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    )
    return [row[0] for row in cursor.fetchall()]


def fetch_rows(conn: sqlite3.Connection, table: str, limit: int) -> Iterable[sqlite3.Row]:
    query = f"SELECT * FROM '{table}' LIMIT ?"
    cursor = conn.execute(query, (limit,))
    return cursor.fetchall()


def main() -> None:
    parser = argparse.ArgumentParser(description="Show table content from stonks.db")
    parser.add_argument("--db", default="data/stonks.db", help="Path to SQLite db (default: data/stonks.db)")
    parser.add_argument("--table", help="Table name to display (optional; will prompt if omitted)")
    parser.add_argument("--limit", type=int, default=20, help="Max rows to display (default: 20)")
    args = parser.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        raise SystemExit(f"Database not found: {db_path}")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    with conn:
        tables = list_tables(conn)
        if not tables:
            raise SystemExit("No tables found in the database.")

        table = args.table
        if table and table not in tables:
            raise SystemExit(f"Table not found: {table}. Available: {', '.join(tables)}")

        if not table:
            print("Select a table:")
            for idx, name in enumerate(tables, start=1):
                print(f"{idx}. {name}")
            selection = input(f"Enter number (1-{len(tables)}) or table name [1]: ").strip()
            if not selection:
                table = tables[0]
            elif selection.isdigit():
                choice = int(selection)
                if choice < 1 or choice > len(tables):
                    raise SystemExit("Invalid selection.")
                table = tables[choice - 1]
            elif selection in tables:
                table = selection
            else:
                raise SystemExit(f"Invalid selection: {selection}")

        rows = list(fetch_rows(conn, table, args.limit))
        if not rows:
            print(f"No rows in {table}.")
            return

        columns = rows[0].keys()
        print(f"Table: {table} (showing up to {args.limit} rows)")
        print("\t".join(columns))
        for row in rows:
            print("\t".join(str(row[col]) if row[col] is not None else "" for col in columns))


if __name__ == "__main__":
    main()
