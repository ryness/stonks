from __future__ import annotations

import datetime as dt
import json
import math
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - hints only
    import pandas as pd


def _utcnow_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _maybe_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def _coerce_trading_day(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, dt.datetime):
        return value.date().isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    text = str(value).strip()
    if not text:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return dt.datetime.strptime(text[: len(fmt)], fmt).date().isoformat()
        except ValueError:
            continue
    return text


class StonksStorage:
    """Lightweight SQLite persistence for market data and derived metrics."""

    def __init__(self, path: Path | str = Path("data/stonks.db")) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_schema()

    @contextmanager
    def _connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.path))
        try:
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA foreign_keys = ON;")
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _ensure_schema(self) -> None:
        with self._connection() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS tickers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL UNIQUE,
                    name TEXT,
                    sector TEXT,
                    industry TEXT,
                    country TEXT,
                    homepage_url TEXT,
                    updated_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS source_runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticker_id INTEGER NOT NULL,
                    ticker_symbol TEXT NOT NULL,
                    started_at TEXT NOT NULL,
                    finished_at TEXT,
                    workflow_run_id TEXT,
                    status TEXT NOT NULL,
                    duration_seconds REAL,
                    error_message TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (ticker_id) REFERENCES tickers(id) ON DELETE CASCADE
                );

                CREATE TABLE IF NOT EXISTS price_bars (
                    ticker_id INTEGER NOT NULL,
                    trading_day TEXT NOT NULL,
                    provider TEXT NOT NULL,
                    open REAL,
                    high REAL,
                    low REAL,
                    close REAL,
                    volume REAL,
                    adjusted_close REAL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (ticker_id, trading_day, provider),
                    FOREIGN KEY (ticker_id) REFERENCES tickers(id) ON DELETE CASCADE
                );

                CREATE INDEX IF NOT EXISTS idx_price_bars_day
                    ON price_bars (ticker_id, trading_day DESC);

                CREATE TABLE IF NOT EXISTS tech_indicators (
                    ticker_id INTEGER NOT NULL,
                    trading_day TEXT NOT NULL,
                    source_run_id INTEGER NOT NULL,
                    sma50 REAL,
                    ema50 REAL,
                    macd REAL,
                    macd_signal REAL,
                    macd_hist REAL,
                    rsi14 REAL,
                    atr14 REAL,
                    raw_payload TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (ticker_id, trading_day, source_run_id),
                    FOREIGN KEY (ticker_id) REFERENCES tickers(id) ON DELETE CASCADE,
                    FOREIGN KEY (source_run_id) REFERENCES source_runs(id) ON DELETE CASCADE
                );

                CREATE TABLE IF NOT EXISTS daily_snapshots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticker_id INTEGER NOT NULL,
                    source_run_id INTEGER NOT NULL,
                    trading_day TEXT NOT NULL,
                    close REAL,
                    support_7d REAL,
                    resistance_7d REAL,
                    support_30d REAL,
                    resistance_30d REAL,
                    local_high REAL,
                    local_low REAL,
                    dma20 REAL,
                    volume_ratio_10d REAL,
                    volume_bucket TEXT,
                    volatility_bucket TEXT,
                    atr14 REAL,
                    atr_pct REAL,
                    trend_label TEXT,
                    suggested_buy_zone REAL,
                    suggested_sell_zone REAL,
                    price_data_source TEXT,
                    runtime_seconds REAL,
                    generated_at TEXT,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE (ticker_id, trading_day, source_run_id),
                    FOREIGN KEY (ticker_id) REFERENCES tickers(id) ON DELETE CASCADE,
                    FOREIGN KEY (source_run_id) REFERENCES source_runs(id) ON DELETE CASCADE
                );

                CREATE INDEX IF NOT EXISTS idx_daily_snapshots_day
                    ON daily_snapshots (ticker_id, trading_day DESC);

                CREATE INDEX IF NOT EXISTS idx_source_runs_started
                    ON source_runs (started_at DESC);
                """
            )

    def start_run(
        self,
        symbol: str,
        started_at: dt.datetime,
        workflow_run_id: Optional[str] = None,
    ) -> int:
        symbol_upper = symbol.strip().upper()
        with self._connection() as conn:
            ticker_id = self._ensure_ticker(conn, symbol_upper, None)
            cursor = conn.execute(
                """
                INSERT INTO source_runs (ticker_id, ticker_symbol, started_at, workflow_run_id, status)
                VALUES (?, ?, ?, ?, ?)
                """,
                (ticker_id, symbol_upper, started_at.isoformat(), workflow_run_id, "running"),
            )
            return int(cursor.lastrowid)

    def finish_run(
        self,
        run_id: int,
        finished_at: dt.datetime,
        status: str,
        duration_seconds: Optional[float] = None,
        error_message: Optional[str] = None,
    ) -> None:
        with self._connection() as conn:
            conn.execute(
                """
                UPDATE source_runs
                SET finished_at = ?, status = ?, duration_seconds = ?, error_message = ?
                WHERE id = ?
                """,
                (
                    finished_at.isoformat(),
                    status,
                    duration_seconds,
                    error_message,
                    run_id,
                ),
            )

    def persist_run_data(
        self,
        *,
        run_id: int,
        symbol: str,
        company: Mapping[str, Any],
        histories: Mapping[str, "pd.DataFrame"],
        price_provider: str,
        latest_trading_day: Optional[str],
        context: Mapping[str, Any],
        generated_at: dt.datetime,
        runtime_seconds: float,
    ) -> None:
        symbol_upper = symbol.strip().upper()
        with self._connection() as conn:
            ticker_id = self._ensure_ticker(conn, symbol_upper, company)
            conn.execute(
                "UPDATE source_runs SET ticker_id = ? WHERE id = ?",
                (ticker_id, run_id),
            )
            self._upsert_price_bars(conn, ticker_id, histories, price_provider)
            self._insert_technical_indicators(
                conn,
                ticker_id,
                run_id,
                latest_trading_day,
                context.get("massive_technicals"),
                context.get("volatility_assessment"),
            )
            self._insert_daily_snapshot(
                conn,
                ticker_id,
                run_id,
                latest_trading_day,
                context,
                histories,
                generated_at,
                runtime_seconds,
                price_provider,
            )

    def _ensure_ticker(
        self,
        conn: sqlite3.Connection,
        symbol: str,
        company: Optional[Mapping[str, Any]],
    ) -> int:
        now = _utcnow_iso()
        existing = conn.execute(
            "SELECT id, name, sector, industry, country, homepage_url FROM tickers WHERE symbol = ?",
            (symbol,),
        ).fetchone()
        name = None
        sector = None
        industry = None
        country = None
        homepage_url = None
        if company:
            name = company.get("long_name") or company.get("name")
            sector = company.get("sector")
            industry = company.get("industry")
            country = company.get("country")
            homepage_url = company.get("homepage_url")
        if existing:
            updates: Dict[str, Any] = {"updated_at": now}
            if name and name != existing["name"]:
                updates["name"] = name
            if sector and sector != existing["sector"]:
                updates["sector"] = sector
            if industry and industry != existing["industry"]:
                updates["industry"] = industry
            if country and country != existing["country"]:
                updates["country"] = country
            if homepage_url and homepage_url != existing["homepage_url"]:
                updates["homepage_url"] = homepage_url
            if updates:
                assignments = ", ".join(f"{key} = ?" for key in updates.keys())
                conn.execute(
                    f"UPDATE tickers SET {assignments} WHERE id = ?",
                    (*updates.values(), existing["id"]),
                )
            return int(existing["id"])
        cursor = conn.execute(
            """
            INSERT INTO tickers (symbol, name, sector, industry, country, homepage_url, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (symbol, name, sector, industry, country, homepage_url, now),
        )
        return int(cursor.lastrowid)

    def _upsert_price_bars(
        self,
        conn: sqlite3.Connection,
        ticker_id: int,
        histories: Mapping[str, "pd.DataFrame"],
        provider: str,
    ) -> None:
        history = histories.get("5y")
        if history is None or getattr(history, "empty", True):
            history = histories.get("1y")
        if history is None or getattr(history, "empty", True):
            return
        rows = []
        for index_value, row in history.iterrows():
            trading_day = _coerce_trading_day(getattr(index_value, "to_pydatetime", lambda: index_value)())
            if trading_day is None:
                continue
            adj = None
            for key in ("Adj Close", "AdjClose", "Adj_Close"):
                if key in row:
                    adj = _maybe_float(row.get(key))
                    break
            rows.append(
                (
                    ticker_id,
                    trading_day,
                    provider,
                    _maybe_float(row.get("Open")),
                    _maybe_float(row.get("High")),
                    _maybe_float(row.get("Low")),
                    _maybe_float(row.get("Close")),
                    _maybe_float(row.get("Volume")),
                    adj,
                )
            )
        if not rows:
            return
        conn.executemany(
            """
            INSERT INTO price_bars (
                ticker_id, trading_day, provider, open, high, low, close, volume, adjusted_close,
                created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            ON CONFLICT(ticker_id, trading_day, provider) DO UPDATE SET
                open = excluded.open,
                high = excluded.high,
                low = excluded.low,
                close = excluded.close,
                volume = excluded.volume,
                adjusted_close = excluded.adjusted_close,
                updated_at = CURRENT_TIMESTAMP
            """,
            rows,
        )

    def _extract_indicator_scalar(
        self,
        payload: Optional[Mapping[str, Any]],
        preferred_keys: Tuple[str, ...],
    ) -> Optional[float]:
        if not isinstance(payload, Mapping):
            return None
        values = payload.get("values")
        if isinstance(values, Mapping):
            for key in preferred_keys:
                if key in values:
                    return _maybe_float(values.get(key))
            for candidate in values.values():
                number = _maybe_float(candidate)
                if number is not None:
                    return number
        return _maybe_float(payload.get("value"))

    def _indicator_trading_day(self, indicators: Mapping[str, Any]) -> Optional[str]:
        for payload in indicators.values():
            if not isinstance(payload, Mapping):
                continue
            timestamp = payload.get("timestamp") or payload.get("time") or payload.get("t")
            day = _coerce_trading_day(timestamp)
            if day:
                return day
        return None

    def _insert_technical_indicators(
        self,
        conn: sqlite3.Connection,
        ticker_id: int,
        run_id: int,
        latest_trading_day: Optional[str],
        technicals: Optional[Mapping[str, Any]],
        volatility: Optional[Mapping[str, Any]],
    ) -> None:
        if not isinstance(technicals, Mapping):
            return
        indicators = technicals.get("indicators")
        if not isinstance(indicators, Mapping) or not indicators:
            return
        trading_day = latest_trading_day or self._indicator_trading_day(indicators)
        if trading_day is None:
            return
        sma50 = self._extract_indicator_scalar(indicators.get("sma"), ("value", "sma"))
        ema50 = self._extract_indicator_scalar(indicators.get("ema"), ("value", "ema"))
        macd = self._extract_indicator_scalar(indicators.get("macd"), ("macd", "value"))
        macd_signal = self._extract_indicator_scalar(
            indicators.get("macd"),
            ("signal", "signal_line", "macd_signal"),
        )
        macd_hist = self._extract_indicator_scalar(
            indicators.get("macd"),
            ("histogram", "hist", "macd_hist"),
        )
        rsi14 = self._extract_indicator_scalar(indicators.get("rsi"), ("value", "rsi"))
        atr14 = None
        if isinstance(volatility, Mapping):
            atr14 = _maybe_float(volatility.get("atr"))
        conn.execute(
            """
            INSERT INTO tech_indicators (
                ticker_id, trading_day, source_run_id,
                sma50, ema50, macd, macd_signal, macd_hist, rsi14, atr14, raw_payload
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(ticker_id, trading_day, source_run_id) DO UPDATE SET
                sma50 = excluded.sma50,
                ema50 = excluded.ema50,
                macd = excluded.macd,
                macd_signal = excluded.macd_signal,
                macd_hist = excluded.macd_hist,
                rsi14 = excluded.rsi14,
                atr14 = excluded.atr14,
                raw_payload = excluded.raw_payload
            """,
            (
                ticker_id,
                trading_day,
                run_id,
                sma50,
                ema50,
                macd,
                macd_signal,
                macd_hist,
                rsi14,
                atr14,
                json.dumps(dict(indicators), default=str),
            ),
        )

    def _insert_daily_snapshot(
        self,
        conn: sqlite3.Connection,
        ticker_id: int,
        run_id: int,
        latest_trading_day: Optional[str],
        context: Mapping[str, Any],
        histories: Mapping[str, "pd.DataFrame"],
        generated_at: dt.datetime,
        runtime_seconds: float,
        price_provider: str,
    ) -> None:
        snapshot = context.get("price_snapshot") or {}
        buy_sell = context.get("buy_sell_levels") or {}
        volume_view = context.get("volume_assessment") or {}
        volatility_view = context.get("volatility_assessment") or {}
        hist_3mo = histories.get("3mo")
        support_30d = None
        resistance_30d = None
        if hist_3mo is not None and not getattr(hist_3mo, "empty", True):
            window_30 = hist_3mo.tail(30)
            if not window_30.empty:
                resistance_30d = _maybe_float(window_30["High"].max())
                support_30d = _maybe_float(window_30["Low"].min())
        trading_day = latest_trading_day or generated_at.date().isoformat()
        conn.execute(
            """
            INSERT INTO daily_snapshots (
                ticker_id, source_run_id, trading_day,
                close, support_7d, resistance_7d,
                support_30d, resistance_30d,
                local_high, local_low, dma20,
                volume_ratio_10d, volume_bucket,
                volatility_bucket, atr14, atr_pct, trend_label,
                suggested_buy_zone, suggested_sell_zone,
                price_data_source, runtime_seconds, generated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(ticker_id, trading_day, source_run_id) DO UPDATE SET
                close = excluded.close,
                support_7d = excluded.support_7d,
                resistance_7d = excluded.resistance_7d,
                support_30d = excluded.support_30d,
                resistance_30d = excluded.resistance_30d,
                local_high = excluded.local_high,
                local_low = excluded.local_low,
                dma20 = excluded.dma20,
                volume_ratio_10d = excluded.volume_ratio_10d,
                volume_bucket = excluded.volume_bucket,
                volatility_bucket = excluded.volatility_bucket,
                atr14 = excluded.atr14,
                atr_pct = excluded.atr_pct,
                trend_label = excluded.trend_label,
                suggested_buy_zone = excluded.suggested_buy_zone,
                suggested_sell_zone = excluded.suggested_sell_zone,
                price_data_source = excluded.price_data_source,
                runtime_seconds = excluded.runtime_seconds,
                generated_at = excluded.generated_at
            """,
            (
                ticker_id,
                run_id,
                trading_day,
                _maybe_float(snapshot.get("close")),
                _maybe_float(snapshot.get("support")),
                _maybe_float(snapshot.get("resistance")),
                support_30d,
                resistance_30d,
                _maybe_float(snapshot.get("local_high")),
                _maybe_float(snapshot.get("local_low")),
                _maybe_float(snapshot.get("dma20")),
                _maybe_float(volume_view.get("ratio")),
                volume_view.get("label"),
                volatility_view.get("label"),
                _maybe_float(snapshot.get("atr14")),
                _maybe_float(volatility_view.get("atr_pct")),
                snapshot.get("trend_label"),
                _maybe_float(buy_sell.get("suggested_buy_zone")),
                _maybe_float(buy_sell.get("suggested_sell_zone")),
                price_provider or context.get("price_data_source"),
                runtime_seconds,
                generated_at.isoformat(),
            ),
        )
