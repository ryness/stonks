#!/usr/bin/env python3
"""
Print table and column structure for the stonks SQLite database.

Usage:
  python data_tools/show_schema.py [--db data/stonks.db] [--table runs]
"""

import argparse
import sqlite3
from pathlib import Path
from typing import List, Tuple


def list_tables(conn: sqlite3.Connection) -> List[str]:
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    )
    return [row[0] for row in cursor.fetchall()]


def describe_table(conn: sqlite3.Connection, table: str) -> List[Tuple[str, str, int, str]]:
    cursor = conn.execute(f"PRAGMA table_info('{table}')")
    return [(row[1], row[2], row[3], row[4]) for row in cursor.fetchall()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Show table/column structure for stonks.db")
    parser.add_argument("--db", default="data/stonks.db", help="Path to SQLite db (default: data/stonks.db)")
    parser.add_argument("--table", help="Optional table name to describe")
    args = parser.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        raise SystemExit(f"Database not found: {db_path}")

    conn = sqlite3.connect(db_path)
    with conn:
        tables = list_tables(conn)
        if not tables:
            print("No tables found.")
            return

        if args.table:
            if args.table not in tables:
                raise SystemExit(f"Table not found: {args.table}. Available: {', '.join(tables)}")
            print(f"Table: {args.table}")
            print("column\t\ttype\tnot_null\tdefault")
            for name, col_type, not_null, default in describe_table(conn, args.table):
                print(f"{name}\t\t{col_type}\t{not_null}\t{default or ''}")
        else:
            print("Tables:")
            for table in tables:
                cols = describe_table(conn, table)
                col_list = ", ".join(col for col, *_ in cols) if cols else "<no columns>"
                print(f"- {table}: {col_list}")


if __name__ == "__main__":
    main()
