#!/usr/bin/env python3.11
"""Generate a stock analysis report powered by GPT-5."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import math
import os
import re
import shutil
import statistics
import sys
import time
from collections import OrderedDict, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

try:
    import pandas as pd
except ImportError as pandas_error:
    main_module = sys.modules.get("__main__")
    running_as_main = (
        getattr(main_module, "__file__", None)
        and Path(main_module.__file__).resolve() == Path(__file__).resolve()
    )
    if sys.version_info < (3, 11) and running_as_main:
        python311 = shutil.which("python3.11")
        if python311:
            script_path = Path(__file__).resolve()
            sys.stderr.write(
                "pandas failed to import under the current interpreter; "
                "retrying with python3.11 for better Apple Silicon support.\n"
            )
            os.execv(python311, [python311, str(script_path), *sys.argv[1:]])
    raise pandas_error

import requests
import yfinance as yf
from openai import OpenAI
try:
    import yaml
except ImportError as exc:
    raise RuntimeError(
        "PyYAML is required to parse stock-expert_prompt.txt. Install with `pip install PyYAML`."
    ) from exc


PROMPT_PATH = Path("stock-expert_prompt.txt")
OPENAI_KEY_FILE = Path("apikey-openai.txt")
MASSIVE_KEY_FILE = Path("apikey-massive.txt")
DEFAULT_MASSIVE_KEY = "fAYaxuq5a46MwqYZYlYcsM0BccqrLXEM"

CACHE_DIR = Path(".cache")
CACHE_TTL_SECONDS = 6 * 3600
GOOGLE_CSE_API_KEY = os.getenv("GOOGLE_CSE_API_KEY")
GOOGLE_CSE_ENGINE_ID = os.getenv("GOOGLE_CSE_ENGINE_ID")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
MAX_SEARCH_RESULTS = 5

_run_log: List[str] = []


@dataclass(frozen=True)
class LLMInstruction:
    response_type: str
    guidance: Optional[str] = None
    min_paragraphs: Optional[int] = None
    max_paragraphs: Optional[int] = None


@dataclass(frozen=True)
class BulletSpec:
    number: str
    prompt: str
    label: Optional[str]
    instruction: Optional[str]
    llm: Optional[LLMInstruction]
    role: str = "analysis"
    searches: Dict[str, List[str]] = field(default_factory=dict)


@dataclass(frozen=True)
class SectionSpec:
    number: str
    title: str
    summary_number: Optional[str]
    item_numbers: List[str]
    notes: List[str]
    searches: Dict[str, List[str]] = field(default_factory=dict)


@dataclass(frozen=True)
class PromptConfig:
    sections: List[SectionSpec]
    bullets: Dict[str, BulletSpec]
    llm_tasks: List[BulletSpec]
    quick_fact_numbers: List[str]


def _cache_path(key: str) -> Path:
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return CACHE_DIR / f"{digest}.json"


def _cache_read(key: str, ttl: int = CACHE_TTL_SECONDS) -> Optional[Any]:
    path = _cache_path(key)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    timestamp = data.get("timestamp")
    if not isinstance(timestamp, (int, float)):
        return None
    if time.time() - timestamp > ttl:
        return None
    return data.get("payload")


def _cache_write(key: str, payload: Any) -> None:
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path = _cache_path(key)
        path.write_text(json.dumps({"timestamp": time.time(), "payload": payload}), encoding="utf-8")
    except Exception:
        pass


def log_status(message: str) -> None:
    """Emit a progress update for long-running operations."""

    print(message, flush=True, file=sys.stderr)
    _run_log.append(message)


def _parse_llm_instruction(config: Optional[Mapping[str, Any]]) -> Optional[LLMInstruction]:
    if not config:
        return None
    response_type = config.get("type")
    if response_type not in {"string", "paragraphs"}:
        raise ValueError(f"Unsupported LLM response type: {response_type}")
    return LLMInstruction(
        response_type=response_type,
        guidance=config.get("guidance"),
        min_paragraphs=config.get("min_paragraphs") or config.get("min"),
        max_paragraphs=config.get("max_paragraphs") or config.get("max"),
    )


def _parse_searches(raw: Optional[Mapping[str, Any]]) -> Dict[str, List[str]]:
    searches: Dict[str, List[str]] = {}
    if not raw:
        return searches
    for provider, value in raw.items():
        if isinstance(value, str):
            phrases = [value]
        elif isinstance(value, list):
            phrases = [str(item) for item in value if str(item).strip()]
        else:
            continue
        if phrases:
            searches[str(provider)] = phrases
    return searches


def load_prompt() -> PromptConfig:
    """Load the YAML prompt specification into structured configuration."""

    raw = yaml.safe_load(PROMPT_PATH.read_text(encoding="utf-8"))
    sections: List[SectionSpec] = []
    bullets: Dict[str, BulletSpec] = {}
    llm_tasks: List[BulletSpec] = []
    quick_fact_numbers: List[str] = []

    for section_cfg in raw.get("sections", []):
        section_number = str(section_cfg["number"])
        title = section_cfg.get("title", "").strip()
        notes = section_cfg.get("notes", []) or []
        section_searches = _parse_searches(section_cfg.get("searches"))

        summary_number: Optional[str] = None
        summary_cfg = section_cfg.get("summary")
        if summary_cfg:
            summary_number = str(summary_cfg.get("number", section_number))
            summary_searches = _parse_searches(summary_cfg.get("searches"))
            summary_bullet = BulletSpec(
                number=summary_number,
                prompt=summary_cfg.get("prompt", title),
                label=summary_cfg.get("label"),
                instruction=summary_cfg.get("instruction"),
                llm=_parse_llm_instruction(summary_cfg.get("llm")),
                searches=summary_searches,
                role="summary",
            )
            bullets[summary_number] = summary_bullet
            if summary_bullet.llm:
                llm_tasks.append(summary_bullet)

        item_numbers: List[str] = []
        for item in section_cfg.get("items", []):
            item_number = str(item["number"])
            llm_instruction = _parse_llm_instruction(item.get("llm"))
            bullet = BulletSpec(
                number=item_number,
                prompt=item.get("prompt", ""),
                label=item.get("label"),
                instruction=item.get("instruction"),
                llm=llm_instruction,
                role=item.get("role", "analysis"),
                searches=_parse_searches(item.get("searches")),
            )
            bullets[item_number] = bullet
            item_numbers.append(item_number)
            if bullet.role == "quick_fact":
                quick_fact_numbers.append(item_number)
            if bullet.llm:
                llm_tasks.append(bullet)

        sections.append(
            SectionSpec(
                number=section_number,
                title=title,
                summary_number=summary_number,
                item_numbers=item_numbers,
                notes=notes,
                searches=section_searches,
            )
        )

    return PromptConfig(
        sections=sections,
        bullets=bullets,
        llm_tasks=llm_tasks,
        quick_fact_numbers=quick_fact_numbers,
    )


def validate_prompt(config: PromptConfig) -> None:
    if not config.sections:
        raise RuntimeError("Prompt template defines no sections.")
    if not config.llm_tasks:
        raise RuntimeError("Prompt template defines no LLM tasks.")
    if not config.quick_fact_numbers:
        raise RuntimeError("Prompt template defines no quick facts; at least one is required.")


def _google_custom_search(query: str, num: int = MAX_SEARCH_RESULTS) -> List[Dict[str, Any]]:
    if not GOOGLE_CSE_API_KEY or not GOOGLE_CSE_ENGINE_ID:
        return []
    cache_key = f"google_cse::{query}::{num}"
    cached = _cache_read(cache_key)
    if cached is not None:
        return cached
    params = {
        "key": GOOGLE_CSE_API_KEY,
        "cx": GOOGLE_CSE_ENGINE_ID,
        "q": query,
        "num": num,
    }
    try:
        response = requests.get(
            "https://www.googleapis.com/customsearch/v1",
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        log_status(f"Google Custom Search failed for '{query}': {exc}")
        return []
    items: List[Dict[str, Any]] = []
    for item in data.get("items", [])[:num]:
        items.append(
            {
                "title": item.get("title"),
                "summary": item.get("snippet"),
                "url": item.get("link"),
                "displayLink": item.get("displayLink"),
            }
        )
    _cache_write(cache_key, items)
    return items


def _newsapi_search(query: str, num: int = MAX_SEARCH_RESULTS) -> List[Dict[str, Any]]:
    if not NEWSAPI_KEY:
        return []
    cache_key = f"newsapi::{query}::{num}"
    cached = _cache_read(cache_key)
    if cached is not None:
        return cached
    params = {
        "q": query,
        "pageSize": num,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_KEY,
    }
    try:
        response = requests.get(
            "https://newsapi.org/v2/everything",
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        log_status(f"NewsAPI search failed for '{query}': {exc}")
        return []
    articles: List[Dict[str, Any]] = []
    for article in data.get("articles", [])[:num]:
        articles.append(
            {
                "title": article.get("title"),
                "summary": article.get("description"),
                "url": article.get("url"),
                "source": (article.get("source") or {}).get("name"),
                "published": article.get("publishedAt"),
            }
        )
    _cache_write(cache_key, articles)
    return articles


def _execute_search_tasks(ticker: str, config: PromptConfig) -> Dict[str, List[Dict[str, Any]]]:
    tasks: List[Tuple[str, str, str]] = []
    placeholder_values = {
        "ticker": ticker.upper(),
        "ticker_lower": ticker.lower(),
    }

    def add_tasks(search_map: Dict[str, List[str]], source: str) -> None:
        for provider, phrases in search_map.items():
            for phrase in phrases:
                try:
                    formatted = phrase.format(**placeholder_values)
                except Exception:
                    formatted = phrase
                tasks.append((provider, formatted, source))

    for section in config.sections:
        add_tasks(section.searches, f"section:{section.number}")
        if section.summary_number:
            summary_bullet = config.bullets.get(section.summary_number)
            if summary_bullet:
                add_tasks(summary_bullet.searches, f"bullet:{summary_bullet.number}")
        for number in section.item_numbers:
            bullet = config.bullets.get(number)
            if bullet:
                add_tasks(bullet.searches, f"bullet:{number}")

    results: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    seen: set[Tuple[str, str]] = set()
    for provider, query, source in tasks:
        key = (provider, query)
        if key in seen:
            continue
        seen.add(key)
        provider_lower = provider.lower()
        log_status(f"  {provider_lower} search -> {query}")
        if provider_lower == "google_custom_search":
            data = _google_custom_search(query)
        elif provider_lower == "newsapi":
            data = _newsapi_search(query)
        else:
            log_status(f"Unknown search provider '{provider}' for query '{query}'")
            data = []
        log_status(f"    -> {len(data)} results")
        results[provider_lower].append(
            {
                "query": query,
                "source": source,
                "results": data,
            }
        )

    return results


def _load_openai_api_key() -> Optional[str]:
    """Return the OpenAI API key from env or repo file."""

    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY")
    if api_key:
        api_key = api_key.strip()
    if not api_key and OPENAI_KEY_FILE.exists():
        api_key = OPENAI_KEY_FILE.read_text(encoding="utf-8").strip()
    if api_key:
        return api_key or None
    return None


def create_openai_client() -> OpenAI:
    """Create a configured OpenAI client or guide the user to set credentials."""

    api_key = _load_openai_api_key()
    if not api_key:
        raise RuntimeError(
            "Missing OpenAI API key. Set OPENAI_API_KEY in the environment or place the key in apikey-openai.txt."
        )
    return OpenAI(api_key=api_key)


def _load_massive_api_key() -> Optional[str]:
    """Return the Polygon API key from env or repo file, or fall back to the demo key."""

    api_key = os.getenv("MASSIVE_API_KEY")
    if api_key:
        api_key = api_key.strip()
    if not api_key and MASSIVE_KEY_FILE.exists():
        api_key = MASSIVE_KEY_FILE.read_text(encoding="utf-8").strip()
    if api_key:
        return api_key or None
    return DEFAULT_MASSIVE_KEY


@dataclass
class PriceSnapshot:
    """Container for short-term price context."""

    close: float
    resistance: float
    support: float
    local_high: float
    local_low: float
    dma20: float
    atr14: float
    volume: float
    avg_volume10: float
    trend_label: str


def humanize_dollar(value: Optional[float]) -> str:
    """Format large dollar values with readable suffixes."""

    if value is None or math.isnan(value):
        return "unknown"
    magnitude = abs(value)
    units = [
        (1_000_000_000_000, "T"),
        (1_000_000_000, "B"),
        (1_000_000, "M"),
        (1_000, "k"),
    ]
    for threshold, suffix in units:  # Pick the largest matching unit for consistency.
        if magnitude >= threshold:
            return f"${value / threshold:.2f}{suffix}"
    return f"${value:.2f}"


def format_duration(seconds: float) -> str:
    """Convert a duration in seconds into a compact human-readable string."""

    if seconds < 0:
        seconds = 0
    if seconds < 60:
        return f"{seconds:.2f}s"
    minutes, remainder = divmod(seconds, 60)
    if minutes < 60:
        secs = int(round(remainder))
        mins = int(minutes)
        if secs == 60:
            mins += 1
            secs = 0
        return f"{mins}m {secs}s"
    hours, minutes = divmod(minutes, 60)
    secs = int(round(remainder))
    mins = int(minutes)
    hrs = int(hours)
    if secs == 60:
        mins += 1
        secs = 0
    if mins == 60:
        hrs += 1
        mins = 0
    return f"{hrs}h {mins}m {secs}s"


def classify_trend(closes: Sequence[float], lookback: int = 7) -> str:
    """Determine whether closes trend up, down, or range over the lookback window."""

    window = list(closes[-lookback:]) if len(closes) >= lookback else list(closes)
    if len(window) < 2:  # Without at least two points there is no slope to measure.
        return "range"
    xs = range(len(window))
    xm = statistics.mean(xs)
    ym = statistics.mean(window)
    numerator = sum((x - xm) * (y - ym) for x, y in zip(xs, window))
    denominator = sum((x - xm) ** 2 for x in xs)
    slope = numerator / denominator if denominator else 0.0
    if slope > 0:
        return "uptrend"
    if slope < 0:
        return "downtrend"
    return "range"


def calculate_atr(df: pd.DataFrame, period: int = 14) -> Optional[float]:
    """Compute the Average True Range for the supplied window."""

    if df.empty:
        return None
    work = df.copy()
    work["prev_close"] = work["Close"].shift(1)
    ranges = pd.concat(
        [
            work["High"] - work["Low"],
            (work["High"] - work["prev_close"]).abs(),
            (work["Low"] - work["prev_close"]).abs(),
        ],
        axis=1,
    )
    true_range = ranges.max(axis=1)
    tail = true_range.tail(period)
    if tail.empty:
        return None
    return float(tail.mean())


def detect_local_extrema(series_high: Sequence[float], series_low: Sequence[float]) -> Tuple[Optional[float], Optional[float]]:
    """Identify the latest swing high and swing low."""

    highs, lows = list(series_high), list(series_low)
    local_high: Optional[float] = None
    local_low: Optional[float] = None
    for idx in range(1, len(highs) - 1):  # Skip endpoints where neighbors are missing.
        if highs[idx] > highs[idx - 1] and highs[idx] > highs[idx + 1]:
            local_high = highs[idx]
        if lows[idx] < lows[idx - 1] and lows[idx] < lows[idx + 1]:
            local_low = lows[idx]
    if local_high is None and highs:
        local_high = max(highs)
    if local_low is None and lows:
        local_low = min(lows)
    return local_high, local_low


def compute_price_snapshot(hist: pd.DataFrame) -> PriceSnapshot:
    """Summarize the latest sessions into support, resistance, and volatility metrics."""

    last_10 = hist.tail(10)
    closes = last_10["Close"].tolist()
    highs = last_10["High"].tolist()
    lows = last_10["Low"].tolist()
    resistance = max(highs[-7:]) if highs else float("nan")
    support = min(lows[-7:]) if lows else float("nan")
    local_high, local_low = detect_local_extrema(highs, lows)
    dma20 = hist["Close"].tail(20).mean() if len(hist) >= 20 else hist["Close"].mean()
    atr14 = calculate_atr(hist.tail(40))
    trend_label = classify_trend(closes)
    volume = float(last_10["Volume"].iloc[-1]) if not last_10.empty else float("nan")
    avg_volume10 = float(last_10["Volume"].mean()) if not last_10.empty else float("nan")
    return PriceSnapshot(
        close=float(closes[-1]) if closes else float("nan"),
        resistance=float(resistance),
        support=float(support),
        local_high=float(local_high) if local_high is not None else float("nan"),
        local_low=float(local_low) if local_low is not None else float("nan"),
        dma20=float(dma20) if not math.isnan(dma20) else float("nan"),
        atr14=float(atr14) if atr14 is not None else float("nan"),
        volume=volume,
        avg_volume10=avg_volume10,
        trend_label=trend_label,
    )


def classify_position(cur: float, prices: Sequence[float]) -> str:
    """State whether the current price is near the top, bottom, or middle of a range."""

    if not prices or math.isnan(cur):
        return "unknown"
    lo, hi = float(min(prices)), float(max(prices))
    if math.isclose(hi, lo):
        return "middle"
    pct = (cur - lo) / (hi - lo)
    if pct >= 0.98:
        return "peak"
    if pct >= 0.80:
        return "near-peak"
    if pct <= 0.02:
        return "bottom"
    if pct <= 0.20:
        return "near-bottom"
    return "middle"


def fetch_polygon_histories(ticker: str, api_key: str) -> Dict[str, pd.DataFrame]:
    """Retrieve 5 years of daily bars from massive.com (Polygon) and derive shorter windows."""

    log_status(f"Requesting {ticker.upper()} prices from massive.com (Polygon API)...")
    base_url = "https://api.polygon.io/v2/aggs/ticker"
    today = dt.date.today()
    start = today - dt.timedelta(days=5 * 365 + 30)
    params = {
        "adjusted": "true",
        "sort": "asc",
        "limit": 5000,
        "apiKey": api_key,
    }
    url = f"{base_url}/{ticker.upper()}/range/1/day/{start.isoformat()}/{today.isoformat()}"
    try:
        response = requests.get(url, params=params, timeout=30)
    except requests.RequestException as exc:
        raise RuntimeError("massive.com request failed") from exc
    if response.status_code != 200:
        raise RuntimeError(f"massive.com request failed with status {response.status_code}")
    payload = response.json()
    if payload.get("status") != "OK" or not payload.get("results"):
        raise RuntimeError("massive.com returned no price data")
    df = pd.DataFrame(payload["results"])
    df["timestamp"] = pd.to_datetime(df["t"], unit="ms")
    df = df.rename(
        columns={
            "o": "Open",
            "h": "High",
            "l": "Low",
            "c": "Close",
            "v": "Volume",
        }
    )
    df = df[["timestamp", "Open", "High", "Low", "Close", "Volume"]]
    df = df.sort_values("timestamp").set_index("timestamp")

    def slice_days(days: int) -> pd.DataFrame:
        cutoff = df.index.max() - pd.Timedelta(days=days)
        return df[df.index >= cutoff].copy()

    hist_5y = df.copy()
    hist_1y = slice_days(370)
    hist_3mo = slice_days(120)
    if hist_3mo.empty:
        raise RuntimeError("massive.com data insufficient for 3-month window")
    hist_10d = hist_3mo.tail(40).copy()
    if hist_10d.empty:
        raise RuntimeError("massive.com data insufficient for 10-day window")
    histories = {
        "5y": hist_5y,
        "1y": hist_1y if not hist_1y.empty else hist_5y.copy(),
        "3mo": hist_3mo,
        "10d": hist_10d,
    }
    return histories


def fetch_yfinance_histories(ticker_obj: yf.Ticker) -> Dict[str, pd.DataFrame]:
    """Fallback price histories using yfinance."""

    log_status("Requesting prices from yfinance fallback...")
    return {
        "10d": ticker_obj.history(period="1mo", interval="1d"),
        "3mo": ticker_obj.history(period="3mo", interval="1d"),
        "1y": ticker_obj.history(period="1y", interval="1d"),
        "5y": ticker_obj.history(period="5y", interval="1d"),
    }


def get_price_histories(ticker: str) -> Tuple[Dict[str, pd.DataFrame], str]:
    """Attempt to fetch prices from massive.com, falling back to yfinance if needed."""

    api_key = _load_massive_api_key()
    last_error: Optional[Exception] = None
    if api_key:
        try:
            log_status("Checking massive.com quota and fetching price history...")
            histories = fetch_polygon_histories(ticker, api_key)
            log_status("Price data acquired from massive.com.")
            return histories, "massive.com (Polygon API)"
        except Exception as exc:  # Reserve fallback for exhausted quota or other issues.
            last_error = exc
            log_status(f"massive.com request failed ({exc}); switching to yfinance...")
    ticker_obj = yf.Ticker(ticker)
    histories = fetch_yfinance_histories(ticker_obj)
    if any(df.empty for df in histories.values()):
        message = (
            f"Failed to obtain price history from massive.com and yfinance for {ticker}."
        )
        if last_error:
            message += f" massive.com error: {last_error}"  # Provide context for debugging.
        raise RuntimeError(message)
    log_status("Price data acquired from yfinance.")
    return histories, "yfinance"


def guess_competitors(industry: Optional[str], sector: Optional[str]) -> List[str]:
    """Provide a simple competitor list to guide the LLM."""

    industry_lower = (industry or "").lower()
    sector_lower = (sector or "").lower()
    if "internet" in industry_lower or "social" in industry_lower:
        return ["Alphabet", "Snap", "Pinterest", "TikTok"]
    if "software" in industry_lower:
        return ["Snowflake", "Databricks", "C3.ai", "Microsoft Azure"]
    if "semiconductor" in industry_lower:
        return ["NVIDIA", "AMD", "Intel", "Qualcomm"]
    if "financial" in sector_lower:
        return ["Goldman Sachs", "Morgan Stanley", "JPMorgan Chase"]
    if "health" in sector_lower:
        return ["UnitedHealth", "CVS Health", "HCA Healthcare"]
    return []


def evaluate_volume_label(snapshot: PriceSnapshot) -> Dict[str, Optional[float]]:
    """Rate volume as high/med/low relative to the 10-day average."""

    volume = snapshot.volume
    avg = snapshot.avg_volume10
    if math.isnan(volume) or math.isnan(avg) or avg == 0:
        return {"label": "unknown", "ratio": None}
    ratio = volume / avg
    if ratio >= 1.5:
        label = "high"
    elif ratio <= 0.67:
        label = "low"
    else:
        label = "med"
    return {"label": label, "ratio": ratio}


def evaluate_volatility_label(snapshot: PriceSnapshot) -> Dict[str, Optional[float]]:
    """Translate ATR into a high/med/low volatility signal."""

    if math.isnan(snapshot.atr14) or math.isnan(snapshot.close) or snapshot.close == 0:
        return {"label": "unknown", "atr": None, "atr_pct": None}
    atr_pct = snapshot.atr14 / snapshot.close * 100
    if atr_pct >= 4:
        label = "high"
    elif atr_pct <= 2:
        label = "low"
    else:
        label = "med"
    return {"label": label, "atr": snapshot.atr14, "atr_pct": atr_pct}


def extract_financial_metrics(info: Dict[str, Any], ticker_obj: yf.Ticker) -> Dict[str, Any]:
    """Pull profitability metrics and upcoming earnings information."""

    financials = ticker_obj.quarterly_financials
    net_income_values: List[float] = []
    for label in (
        "Net Income",
        "Net Income Applicable To Common Shares",
        "Net Income Common Stockholders",
    ):
        if label in financials.index:
            net_income_values = [
                float(v)
                for v in financials.loc[label].iloc[:4].tolist()
                if pd.notna(v)
            ]
            break
    upcoming: Optional[dt.datetime] = None
    earnings_dates = info.get("earningsDate") or []
    if isinstance(earnings_dates, (list, tuple)) and earnings_dates:
        parsed: List[dt.datetime] = []
        for value in earnings_dates:
            if isinstance(value, dt.datetime):
                parsed.append(value)
            elif isinstance(value, dt.date):
                parsed.append(dt.datetime.combine(value, dt.time()))
        if parsed:
            upcoming = min(parsed)
    return {
        "net_income_values": net_income_values,
        "net_income_sum": sum(net_income_values),
        "profit_margin": info.get("profitMargins"),
        "revenue_growth": info.get("revenueGrowth"),
        "earnings_growth": info.get("earningsQuarterlyGrowth"),
        "free_cash_flow": info.get("freeCashflow"),
        "operating_cash_flow": info.get("operatingCashflow"),
        "upcoming_earnings": upcoming,
    }


def fetch_polygon_earnings_calendar(ticker: str, api_key: Optional[str], limit: int = 4) -> List[Dict[str, Any]]:
    if not api_key:
        return []
    params = {"limit": limit, "apiKey": api_key}
    url = f"https://api.polygon.io/v1/reference/earnings/{ticker.upper()}"
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        log_status(f"Polygon earnings lookup failed: {exc}")
        return []
    results = []
    for item in data.get("results", [])[:limit]:
        results.append(
            {
                "report_date": item.get("reportDate"),
                "eps_estimate": item.get("epsEstimate"),
                "eps_actual": item.get("epsActual"),
                "revenue_estimate": item.get("revenueEstimate"),
                "revenue_actual": item.get("revenueActual"),
            }
        )
    return results


def fetch_yfinance_earnings_calendar(ticker_obj: yf.Ticker, limit: int = 4) -> List[Dict[str, Any]]:
    try:
        df = ticker_obj.get_earnings_dates(limit=limit)
    except Exception:
        df = None
    results: List[Dict[str, Any]] = []
    if df is not None and not df.empty:
        for idx, row in df.head(limit).iterrows():
            date_value = idx
            if isinstance(date_value, (dt.datetime, dt.date)):
                report_date = date_value.isoformat()
            else:
                report_date = str(date_value)
            results.append(
                {
                    "report_date": report_date,
                    "eps_estimate": row.get("EPS Estimate"),
                    "eps_actual": row.get("Reported EPS"),
                    "revenue_estimate": row.get("Revenue Estimate"),
                    "revenue_actual": row.get("Reported Revenue"),
                }
            )
    return results


def build_quick_facts(
    snapshot: PriceSnapshot,
    histories: Dict[str, pd.DataFrame],
    financial_metrics: Dict[str, Any],
    prompt_config: PromptConfig,
) -> "OrderedDict[str, Dict[str, str]]":
    """Format the Quick Facts responses keyed by bullet number."""

    quick_fact_numbers = prompt_config.quick_fact_numbers
    net_income_values = financial_metrics["net_income_values"]

    def position_for(period: str) -> str:
        history = histories.get(period)
        if history is None or history.empty:
            return "unknown"
        return classify_position(snapshot.close, history["Close"].tolist())

    close = snapshot.close
    support = snapshot.support
    resistance = snapshot.resistance
    buy_dip = (
        "yes"
        if close and support and not math.isnan(close) and not math.isnan(support)
        and (close - support) / close <= 0.05
        else "no"
    )
    upcoming = financial_metrics["upcoming_earnings"]
    days_to_earnings = (
        (upcoming - dt.datetime.utcnow()).days
        if isinstance(upcoming, dt.datetime)
        else None
    )
    buy_rumor = (
        "yes"
        if days_to_earnings is not None and 0 <= days_to_earnings <= 14
        else "no"
    )
    sell_news = (
        "yes"
        if close and resistance and not math.isnan(close) and not math.isnan(resistance)
        and close / resistance >= 0.97
        else "no"
    )
    trend_lower = (snapshot.trend_label or "").lower()
    if "up" in trend_lower:
        trend_answer = "up"
    elif "down" in trend_lower:
        trend_answer = "down"
    else:
        trend_answer = "flat"

    computed: Dict[str, str] = {}
    if prompt_config.quick_fact_numbers:
        first_key = prompt_config.quick_fact_numbers[0]
        computed[first_key] = humanize_dollar(sum(net_income_values)) if net_income_values else "unknown"
    mappings = {
        "Price": f"{close:.2f}" if close and not math.isnan(close) else "unknown",
        "7d Resistance": f"{resistance:.2f}" if resistance and not math.isnan(resistance) else "unknown",
        "7d Support": f"{support:.2f}" if support and not math.isnan(support) else "unknown",
        "Buy the dip?": buy_dip,
        "Buy the rumor?": buy_rumor,
        "Sell the news?": sell_news,
        "7d Trend:": trend_answer,
        "3mo": position_for("3mo"),
        "1yr": position_for("1y"),
        "5yr": position_for("5y"),
    }

    facts: "OrderedDict[str, Dict[str, str]]" = OrderedDict()
    for number in quick_fact_numbers:
        bullet = prompt_config.bullets.get(number)
        label = (bullet.label if bullet else None) or (bullet.prompt if bullet else None) or number
        value = computed.get(number)
        if value is None:
            value = mappings.get(label, "unknown")
        facts[number] = {"label": label, "value": value}
    return facts


def collect_news(ticker_obj: yf.Ticker, limit: int = 5) -> List[Dict[str, Optional[str]]]:
    """Fetch a handful of the latest headlines for the LLM to summarize."""

    items: List[Dict[str, Optional[str]]] = []
    for entry in ticker_obj.news[:limit]:
        content = entry.get("content", {})
        title = content.get("title") or entry.get("title")
        summary = content.get("summary") or entry.get("summary")
        if not title:
            continue
        items.append({
            "title": title,
            "summary": summary,
            "published": content.get("pubDate") or entry.get("providerPublishTime"),
        })
    return items


def gather_context(ticker: str, prompt_config: PromptConfig) -> Dict[str, Any]:
    """Collect pricing, fundamentals, and news data for the LLM."""

    log_status("Gathering market data...")
    histories, price_source = get_price_histories(ticker)
    hist_10d = histories["10d"]
    if hist_10d.empty:
        raise RuntimeError("No historical price data returned.")
    log_status("Calculating technical snapshot...")
    snapshot = compute_price_snapshot(hist_10d)
    log_status("Fetching company fundamentals...")
    ticker_obj = yf.Ticker(ticker)
    info = ticker_obj.info or {}
    financial_metrics = extract_financial_metrics(info, ticker_obj)
    log_status("Retrieving earnings calendar...")
    polygon_api_key = _load_massive_api_key()
    polygon_calendar = fetch_polygon_earnings_calendar(ticker, polygon_api_key)
    if polygon_calendar:
        earnings_calendar = polygon_calendar
        earnings_calendar_source = "massive.com (Polygon API)"
    else:
        earnings_calendar = fetch_yfinance_earnings_calendar(ticker_obj)
        earnings_calendar_source = "yfinance"
    log_status("Assembling quick facts...")
    quick_facts = build_quick_facts(snapshot, histories, financial_metrics, prompt_config)
    log_status("Collecting latest headlines (yfinance)...")
    news_items = collect_news(ticker_obj)
    log_status(f"  yfinance returned {len(news_items)} headlines")
    log_status("Running supplementary searches...")
    search_results = _execute_search_tasks(ticker, prompt_config)
    volume_metrics = evaluate_volume_label(snapshot)
    volatility_metrics = evaluate_volatility_label(snapshot)
    quick_fact_map = {meta["label"]: meta["value"] for meta in quick_facts.values()}
    prompt_notes = {
        "sections": [
            {"number": section.number, "title": section.title, "notes": section.notes}
            for section in prompt_config.sections
            if section.notes
        ],
        "bullet_instructions": [
            {"number": bullet.number, "instruction": bullet.instruction}
            for bullet in prompt_config.bullets.values()
            if bullet.instruction
        ],
    }

    data_sources: List[str] = []
    data_sources.append(f"Prices & technicals: {price_source}")
    data_sources.append("Fundamentals & company profile: yfinance")
    data_sources.append(f"Earnings calendar: {earnings_calendar_source}")
    data_sources.append("Headlines: yfinance")
    provider_labels = {
        "google_custom_search": "Google Custom Search",
        "newsapi": "NewsAPI.org",
    }
    for provider, provider_results in search_results.items():
        label = provider_labels.get(provider, provider)
        if provider_results and any(item.get("results") for item in provider_results):
            data_sources.append(f"Supplementary search: {label}")
        else:
            data_sources.append(f"Supplementary search: {label} (no results)")

    return {
        "ticker": ticker.upper(),
        "company": {
            "long_name": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "country": info.get("country"),
            "summary": info.get("longBusinessSummary"),
            "competitor_candidates": guess_competitors(info.get("industry"), info.get("sector")),
        },
        "financials": {
            "net_income_values": financial_metrics["net_income_values"],
            "net_income_sum": financial_metrics["net_income_sum"],
            "profit_margin": financial_metrics["profit_margin"],
            "revenue_growth": financial_metrics["revenue_growth"],
            "earnings_growth": financial_metrics["earnings_growth"],
            "free_cash_flow": financial_metrics["free_cash_flow"],
            "operating_cash_flow": financial_metrics["operating_cash_flow"],
            "upcoming_earnings": (
                financial_metrics["upcoming_earnings"].isoformat()
                if isinstance(financial_metrics["upcoming_earnings"], dt.datetime)
                else None
            ),
        },
        "price_snapshot": {
            "close": snapshot.close,
            "resistance": snapshot.resistance,
            "support": snapshot.support,
            "local_high": snapshot.local_high,
            "local_low": snapshot.local_low,
            "dma20": snapshot.dma20,
            "atr14": snapshot.atr14,
            "trend_label": snapshot.trend_label,
        },
        "buy_sell_levels": {
            "suggested_buy_zone": snapshot.local_low if not math.isnan(snapshot.local_low) else snapshot.support,
            "suggested_sell_zone": snapshot.local_high if not math.isnan(snapshot.local_high) else snapshot.resistance,
        },
        "volume_assessment": volume_metrics,
        "volatility_assessment": volatility_metrics,
        "news": news_items,
        "earnings": {"calendar": earnings_calendar},
        "quick_facts": quick_fact_map,
        "quick_fact_rows": [
            {"number": number, "label": data["label"], "value": data["value"]}
            for number, data in quick_facts.items()
        ],
        "search_results": search_results,
        "prompt_notes": prompt_notes,
        "price_data_source": price_source,
        "data_sources": data_sources,
    }


def _extract_json_object(raw_text: str) -> Dict[str, Any]:
    """Attempt to parse a JSON object from raw model output."""

    cleaned = raw_text.strip()
    try:
        parsed = json.loads(cleaned)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        candidate = match.group(0)
        try:
            parsed_candidate = json.loads(candidate)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"LLM returned malformed JSON: {cleaned}") from exc
        if isinstance(parsed_candidate, dict):
            return parsed_candidate
    raise RuntimeError(f"LLM returned invalid JSON:\n{cleaned}")


def call_llm(context: Dict[str, Any], prompt_config: PromptConfig) -> Dict[str, Any]:
    """Invoke GPT-5 and obtain structured answers for targeted bullets."""

    log_status("Preparing OpenAI request...")
    client = create_openai_client()
    system_prompt = "You are an expert stock analyst. Produce grounded, concise answers."

    schema_lines: List[str] = []
    for task in prompt_config.llm_tasks:
        if not task.llm:
            continue
        instruction = task.llm
        base_text = task.prompt or task.label or task.number
        label = task.label or base_text
        if instruction.response_type == "paragraphs":
            min_p = instruction.min_paragraphs or 1
            max_p = instruction.max_paragraphs or min_p
            line = (
                f'"{task.number}": array of {min_p}-{max_p} paragraph strings covering "{base_text}". '
                "Each paragraph must be a complete thought."
            )
        else:
            line = f'"{task.number}": string answering "{label}" based on "{base_text}".'
        if instruction.guidance:
            line += f" {instruction.guidance}"
        if task.instruction:
            line += f" Instruction: {task.instruction}."
        schema_lines.append(f"- {line}")

    if not schema_lines:
        raise RuntimeError("No LLM requests configured; cannot generate report.")

    data_json = json.dumps(context, indent=2, default=str)
    schema_text = "\n".join(schema_lines)
    user_prompt = (
        "Use the structured data to answer the specified report bullets.\n"
        "Return a VALID JSON object with exactly the keys listed below and no extra commentary.\n"
        f"{schema_text}\n"
        "Rules:\n"
        "- Provide plain text answers without numbering or markdown.\n"
        "- Do not insert newline characters inside individual values.\n"
        '- If information is unavailable, respond with the string "unknown".\n'
        "- Ground every statement in the provided data; do not speculate.\n\n"
        f"Context JSON:\n```json\n{data_json}\n```"
    )

    if prompt_config.llm_tasks:
        log_status("Dispatching bullets to OpenAI:")
        for task in prompt_config.llm_tasks:
            instruction = task.instruction
            description = task.label or task.prompt or ""
            if instruction:
                description = f"{description} [{instruction}]" if description else f"[{instruction}]"
            log_status(f"  - {task.number} {description}".rstrip())

    log_status("Asking OpenAI for analysis...")
    response = client.responses.create(
        model="gpt-5",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    log_status("Received response from OpenAI.")
    raw_output = response.output_text.strip()
    parsed = _extract_json_object(raw_output)

    sanitized: Dict[str, Any] = {}
    for task in prompt_config.llm_tasks:
        instruction = task.llm
        if instruction is None:
            continue
        value = parsed.get(task.number)
        if instruction.response_type == "paragraphs":
            paragraphs: List[str]
            if isinstance(value, list):
                paragraphs = [
                    str(entry).strip()
                    for entry in value
                    if isinstance(entry, (str, int, float)) and str(entry).strip()
                ]
            elif isinstance(value, (str, int, float)):
                paragraphs = [str(value).strip()]
            else:
                paragraphs = []
            if not paragraphs:
                paragraphs = ["unknown"]
            sanitized[task.number] = paragraphs
        else:
            text_value = str(value).strip() if value is not None else ""
            sanitized[task.number] = text_value if text_value else "unknown"

    return sanitized


def format_report(
    context: Dict[str, Any],
    prompt_config: PromptConfig,
    llm_answers: Mapping[str, Any],
) -> str:
    """Format the final report text with numbering and labels."""

    quick_fact_lookup = {
        row["number"]: row
        for row in context.get("quick_fact_rows", [])
        if isinstance(row, Mapping) and row.get("number")
    }

    lines: List[str] = []
    for section in prompt_config.sections:
        heading_text = section.title or section.number
        if lines:
            lines.append("")
        lines.append(f"## {section.number}. {heading_text}".rstrip())
        lines.append("")

        if section.summary_number:
            summary_value = llm_answers.get(section.summary_number, [])
            paragraphs = summary_value
            if isinstance(summary_value, str):
                paragraphs = [summary_value]
            for paragraph in paragraphs or []:
                paragraph_text = str(paragraph).strip()
                if paragraph_text:
                    lines.append(paragraph_text)
                    lines.append("")

        bullets = [prompt_config.bullets.get(num) for num in section.item_numbers]
        if bullets and all(bullet and bullet.role == "quick_fact" for bullet in bullets):
            lines.append("| Metric | Answer |")
            lines.append("| --- | --- |")
            for bullet in bullets:
                if bullet is None:
                    continue
                row = quick_fact_lookup.get(bullet.number, {})
                label_text = bullet.label or bullet.prompt or bullet.number
                value_text = row.get("value", "unknown")
                lines.append(f"| {label_text} | {value_text} |")
            lines.append("")
            continue

        for bullet in bullets:
            if bullet is None:
                continue
            raw_value = llm_answers.get(bullet.number, "unknown")
            if isinstance(raw_value, list):
                value_text = " ".join(str(entry).strip() for entry in raw_value if str(entry).strip())
            else:
                value_text = str(raw_value).strip()
            if not value_text:
                value_text = "unknown"
            label = (bullet.label or "").rstrip(":")
            prefix = f"**{label}:** " if label else ""
            lines.append(f"{bullet.number}. {prefix}{value_text}")
            lines.append("")
        if lines and lines[-1] == "":
            lines.pop()

    lines.append("")
    data_sources = context.get("data_sources") or []
    if data_sources:
        lines.append("**Sources**")
        for entry in data_sources:
            lines.append(f"- {entry}")
    else:
        lines.append(f"Price data source: {context['price_data_source']}")
    cli_log = context.get("cli_log")
    if cli_log:
        log_block = "\n".join(html.escape(entry) for entry in cli_log)
        lines.append("")
        lines.append("<div class=\"cli-log\"><pre><code>")
        lines.append(log_block)
        lines.append("</code></pre></div>")
    return "\n".join(lines).strip()


def build_report(ticker: str, prompt_config: PromptConfig) -> str:
    """Assemble context, call GPT-5 for targeted bullets, and format the report."""

    _run_log.clear()
    log_status(f"Gathering context for {ticker.upper()}...")
    context = gather_context(ticker, prompt_config)
    log_status("Synthesizing narrative from OpenAI response...")
    llm_answers = call_llm(context, prompt_config)
    context["cli_log"] = list(_run_log)
    log_status("Formatting final report...")
    return format_report(context, prompt_config, llm_answers)


def write_jekyll_report(
    ticker: str,
    report_body: str,
    generated_at: dt.datetime,
    elapsed_seconds: float,
    output_path: Path,
) -> None:
    sanitized = report_body.strip()
    raw_lines = sanitized.splitlines()
    front_matter_lines = [
        "---",
        "layout: default",
        f'title: "{ticker.upper()} Stock Report"',
        f'ticker: "{ticker.upper()}"',
        f"date: {generated_at.date().isoformat()}",
        f"generated_at: {generated_at.isoformat()}",
        f"runtime_seconds: {elapsed_seconds:.2f}",
        "raw_markdown: |",
    ]
    front_matter_lines.extend(f"  {line}" for line in raw_lines or [""])
    front_matter_lines.extend(["---", "", sanitized, ""])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(front_matter_lines), encoding="utf-8")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Configure command-line arguments (ticker only)."""

    parser = argparse.ArgumentParser(description="Generate a Jekyll-ready GPT-5 stock report.")
    parser.add_argument("ticker", nargs="?", help="Ticker symbol to analyse")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point that generates and writes the Markdown report."""

    args = parse_args(argv)
    log_status("Loading prompt template...")
    prompt_config = load_prompt()
    validate_prompt(prompt_config)
    ticker = args.ticker or input("Enter ticker symbol: ").strip()
    if not ticker:
        raise SystemExit("Ticker symbol is required.")
    log_status(f"Starting report generation for {ticker.upper()}...")
    start_time = time.perf_counter()
    report = build_report(ticker, prompt_config)
    elapsed_seconds = time.perf_counter() - start_time
    generated_at = dt.datetime.now(dt.timezone.utc)
    timestamp_display = generated_at.strftime("%Y-%m-%d %H:%M %Z")
    duration_display = format_duration(elapsed_seconds)
    header_line = f"**Generated:** {timestamp_display} (runtime {duration_display})"
    trimmed_body = report.strip()
    if trimmed_body:
        report = f"{header_line}\n\n{trimmed_body}"
    else:
        report = header_line
    output_path = Path("_reports") / f"{ticker.upper()}.md"
    write_jekyll_report(ticker, report, generated_at, elapsed_seconds, output_path)
    print(f"Saved Jekyll report to {output_path}")
    return 0


if __name__ == "__main__":  # Allow the script to be executed directly.
    raise SystemExit(main())
