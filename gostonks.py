#!/usr/bin/env python3.11
"""Generate a stock analysis report powered by GPT-5."""

from __future__ import annotations

import argparse
import datetime as dt
import functools
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
from urllib.parse import urlencode, urlparse, parse_qs

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
from stonks_storage import StonksStorage
try:
    import yaml
except ImportError as exc:
    raise RuntimeError(
        "PyYAML is required to parse stock-expert_prompt.txt. Install with `pip install PyYAML`."
    ) from exc


PROMPT_PATH = Path("stock-expert_prompt.txt")
GODSEYE_PROMPT_PATH = Path("godseye_prompt.txt")
GODSEYE_TICKER = "GODSEYE"
MARKET_BENCHMARKS = [
    {"symbol": "^GSPC", "label": "S&P 500", "category": "index"},
    {"symbol": "^DJI", "label": "Dow 30", "category": "index"},
    {"symbol": "^IXIC", "label": "Nasdaq Composite", "category": "index"},
    {"symbol": "^RUT", "label": "Russell 2000", "category": "index"},
    {"symbol": "SPY", "label": "SPY ETF", "category": "etf"},
    {"symbol": "QQQ", "label": "QQQ ETF", "category": "etf"},
    {"symbol": "^VIX", "label": "VIX", "category": "volatility"},
    {"symbol": "ES=F", "label": "S&P Fut", "category": "futures"},
    {"symbol": "NQ=F", "label": "Nasdaq Fut", "category": "futures"},
    {"symbol": "YM=F", "label": "Dow Fut", "category": "futures"},
    {"symbol": "RTY=F", "label": "Russell Fut", "category": "futures"},
    {"symbol": "^TNX", "label": "10Y Treasury", "category": "treasury"},
    {"symbol": "GC=F", "label": "Gold Fut", "category": "commodity"},
    {"symbol": "CL=F", "label": "WTI Crude", "category": "commodity"},
    {"symbol": "DX-Y.NYB", "label": "US Dollar", "category": "fx"},
]
OPENAI_KEY_FILE = Path("apikey-openai.txt")
MASSIVE_KEY_FILE = Path("apikey-massive.txt")
GNEWS_KEY_FILE = Path("apikey-gnews.txt")
GUARDIAN_KEY_FILE = Path("apikey-guardian.txt")
DEFAULT_MASSIVE_KEY = "fAYaxuq5a46MwqYZYlYcsM0BccqrLXEM"
MASSIVE_API_BASE = "https://api.massive.com"
LOGO_DIR = Path("assets/logos")

CACHE_DIR = Path(".cache")
REPORTS_DIR = Path("_reports")
STATE_FILE = Path(".gostonks-state.json")
FOOTNOTE_MARKER = "^"
FOOTNOTE_NOTE = f"{FOOTNOTE_MARKER} indicates an API issue or empty result (see generation log{FOOTNOTE_MARKER})."
CACHE_TTL_SECONDS = 6 * 3600
GOOGLE_CSE_API_KEY = os.getenv("GOOGLE_CSE_API_KEY")
GOOGLE_CSE_ENGINE_ID = os.getenv("GOOGLE_CSE_ENGINE_ID")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY") or os.getenv("GNEWS_TOKEN")
GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY") or os.getenv("THE_GUARDIAN_API_KEY")
MAX_SEARCH_RESULTS = 5
SEARCH_PROVIDER_PRIORITY = {
    "google_custom_search": ["google_custom_search", "newsapi", "gnews", "guardian"],
    "newsapi": ["newsapi", "gnews", "guardian"],
    "gnews": ["gnews", "guardian"],
    "guardian": ["guardian"],
}

if not GNEWS_API_KEY and GNEWS_KEY_FILE.exists():
    GNEWS_API_KEY = GNEWS_KEY_FILE.read_text(encoding="utf-8").strip() or None
if not GUARDIAN_API_KEY and GUARDIAN_KEY_FILE.exists():
    GUARDIAN_API_KEY = GUARDIAN_KEY_FILE.read_text(encoding="utf-8").strip() or None

try:
    _site_config = yaml.safe_load(Path("_config.yml").read_text(encoding="utf-8"))
except Exception:
    _site_config = {}

SITE_URL = (_site_config.get("url") or "").rstrip("/")
SITE_BASEURL = (_site_config.get("baseurl") or "").strip()
if SITE_BASEURL and not SITE_BASEURL.startswith("/"):
    SITE_BASEURL = f"/{SITE_BASEURL}"
SITE_BASEURL = SITE_BASEURL.rstrip("/")
PUBLIC_BASE_PATH = SITE_BASEURL or ""
PUBLIC_BASE_URL = f"{SITE_URL}{PUBLIC_BASE_PATH}" if SITE_URL else ""

_run_log: List[str] = []
STORAGE = StonksStorage()


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


def _sanitize_message(message: str) -> str:
    if not message:
        return ""
    sanitized = message
    for pattern in ("key=", "apikey=", "apiKey=", "token=", "cx=", "client_id=", "client_secret="):
        sanitized = re.sub(rf"{pattern}[^&\s]+", f"{pattern}***", sanitized, flags=re.IGNORECASE)
    def _shorten(match) -> str:
        url = match.group(0)
        try:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            return base
        except Exception:
            return url
    sanitized = re.sub(r"https?://[^\s]+", _shorten, sanitized)
    return sanitized


def log_status(message: str) -> None:
    """Emit a progress update for long-running operations."""

    print(message, flush=True, file=sys.stderr)
    _run_log.append(message)


def discover_tickers() -> List[str]:
    """Return sorted tickers inferred from existing report filenames."""

    if not REPORTS_DIR.exists():
        return []
    tickers = {path.stem.upper() for path in REPORTS_DIR.glob("*.md")}
    return sorted(tickers)


def _parse_iso_datetime(value: Any) -> Optional[dt.datetime]:
    """Return an aware datetime parsed from a supported representation."""

    if isinstance(value, dt.datetime):
        candidate = value
    elif isinstance(value, (int, float)):
        return dt.datetime.fromtimestamp(float(value), tz=dt.timezone.utc)
    elif isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        normalized = text.replace("Z", "+00:00")
        try:
            candidate = dt.datetime.fromisoformat(normalized)
        except ValueError:
            try:
                candidate = dt.datetime.strptime(text, "%Y-%m-%d")
            except ValueError:
                return None
    else:
        return None
    if candidate.tzinfo is None:
        candidate = candidate.replace(tzinfo=dt.timezone.utc)
    return candidate


def _load_report_front_matter(ticker: str) -> Optional[Mapping[str, Any]]:
    path = REPORTS_DIR / f"{ticker}.md"
    try:
        raw_text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    lines = raw_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for idx, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            front_matter_text = "\n".join(lines[1:idx])
            try:
                data = yaml.safe_load(front_matter_text) or {}
            except Exception:
                return None
            return data if isinstance(data, Mapping) else None
    return None


def _report_generated_timestamp(ticker: str) -> Optional[float]:
    metadata = _load_report_front_matter(ticker)
    if isinstance(metadata, Mapping):
        for key in ("generated_at", "generated", "date"):
            if key in metadata:
                dt_value = _parse_iso_datetime(metadata[key])
                if dt_value is not None:
                    return dt_value.timestamp()
    return None


def _load_cycle_state() -> Dict[str, Any]:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_cycle_state(state: Mapping[str, Any]) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def select_next_ticker() -> str:
    """Return the ticker whose report was generated longest ago."""

    tickers = discover_tickers()
    if not tickers:
        raise RuntimeError(
            "No reports found in _reports/. Add at least one report before using --cycle."
        )

    def recency_key(ticker: str) -> Tuple[float, str]:
        timestamp = _report_generated_timestamp(ticker)
        if timestamp is None:
            path = REPORTS_DIR / f"{ticker}.md"
            try:
                timestamp = path.stat().st_mtime
            except FileNotFoundError:
                timestamp = float("-inf")
            except OSError:
                timestamp = float("inf")
        return (timestamp, ticker)

    return min(tickers, key=recency_key)


def update_cycle_state(ticker: str) -> None:
    """Record the most recently generated ticker so future cycles advance correctly."""

    ticker_upper = ticker.upper()
    tickers = discover_tickers()
    if ticker_upper not in tickers:
        tickers.append(ticker_upper)
        tickers.sort()
    state = dict(_load_cycle_state())
    state["tickers"] = tickers
    state["last_index"] = tickers.index(ticker_upper)
    _save_cycle_state(state)


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


def _parse_prompt_payload(raw: Mapping[str, Any]) -> PromptConfig:
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


@functools.lru_cache(maxsize=None)
def _load_prompt_from_path(path_str: str) -> PromptConfig:
    path = Path(path_str)
    if not path.exists():
        raise RuntimeError(f"Prompt template not found: {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    return _parse_prompt_payload(raw or {})


def load_prompt(path: Path | str = PROMPT_PATH) -> PromptConfig:
    """Load the YAML prompt specification into structured configuration."""

    return _load_prompt_from_path(str(path))


def prompt_path_for_ticker(ticker: str) -> Path:
    """Return the correct prompt template for a ticker."""

    if ticker.strip().upper() == GODSEYE_TICKER:
        return GODSEYE_PROMPT_PATH
    return PROMPT_PATH


def load_prompt_for_ticker(ticker: str) -> PromptConfig:
    config = load_prompt(prompt_path_for_ticker(ticker))
    validate_prompt(config)
    return config


def validate_prompt(config: PromptConfig) -> None:
    if not config.sections:
        raise RuntimeError("Prompt template defines no sections.")
    if not config.llm_tasks:
        raise RuntimeError("Prompt template defines no LLM tasks.")
    if not config.quick_fact_numbers:
        raise RuntimeError("Prompt template defines no quick facts; at least one is required.")


def _google_custom_search(query: str, num: int = MAX_SEARCH_RESULTS) -> Tuple[List[Dict[str, Any]], str]:
    if not GOOGLE_CSE_API_KEY or not GOOGLE_CSE_ENGINE_ID:
        return [], "error: missing API key or engine id"
    cache_key = f"google_cse::{query}::{num}"
    cached = _cache_read(cache_key)
    if cached is not None:
        return cached, f"cached {len(cached)} result(s)"
    params = {
        "key": GOOGLE_CSE_API_KEY,
        "cx": GOOGLE_CSE_ENGINE_ID,
        "q": query,
        "num": num,
    }
    try:
        base_url = "https://www.googleapis.com/customsearch/v1"
        log_params = {k: v for k, v in params.items()}
        log_params["key"] = "***"
        log_status(f"Google Custom Search: GET {base_url}?{urlencode(log_params)}")
        response = requests.get(
            base_url,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        message = _sanitize_message(str(exc))
        log_status(f"Google Custom Search failed for '{query}': {message}")
        return [], f"error: {message}"
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
    return items, f"{len(items)} result(s)"


def _newsapi_search(query: str, num: int = MAX_SEARCH_RESULTS) -> Tuple[List[Dict[str, Any]], str]:
    if not NEWSAPI_KEY:
        return [], "error: missing API key"
    cache_key = f"newsapi::{query}::{num}"
    cached = _cache_read(cache_key)
    if cached is not None:
        return cached, f"cached {len(cached)} result(s)"
    params = {
        "q": query,
        "pageSize": num,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_KEY,
    }
    try:
        base_url = "https://newsapi.org/v2/everything"
        log_params = {k: v for k, v in params.items()}
        log_params["apiKey"] = "***"
        log_status(f"NewsAPI search: GET {base_url}?{urlencode(log_params)}")
        response = requests.get(
            base_url,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        message = _sanitize_message(str(exc))
        log_status(f"NewsAPI search failed for '{query}': {message}")
        return [], f"error: {message}"
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
    return articles, f"{len(articles)} result(s)"


def _gnews_search(query: str, num: int = MAX_SEARCH_RESULTS) -> Tuple[List[Dict[str, Any]], str]:
    if not GNEWS_API_KEY:
        return [], "error: missing API token"
    cache_key = f"gnews::{query}::{num}"
    cached = _cache_read(cache_key)
    if cached is not None:
        return cached, f"cached {len(cached)} result(s)"
    params = {
        "q": query,
        "lang": "en",
        "max": min(num, 10),
        "token": GNEWS_API_KEY,
    }
    try:
        base_url = "https://gnews.io/api/v4/search"
        log_params = {**params, "token": "***"}
        log_status(f"GNews search: GET {base_url}?{urlencode(log_params)}")
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        message = _sanitize_message(str(exc))
        log_status(f"GNews search failed for '{query}': {message}")
        return [], f"error: {message}"
    articles: List[Dict[str, Any]] = []
    for article in data.get("articles", [])[:num]:
        source_info = article.get("source") or {}
        articles.append(
            {
                "title": article.get("title"),
                "summary": article.get("description"),
                "url": article.get("url"),
                "source": source_info.get("name"),
                "published": article.get("publishedAt"),
            }
        )
    _cache_write(cache_key, articles)
    return articles, f"{len(articles)} result(s)"


def _guardian_search(query: str, num: int = MAX_SEARCH_RESULTS) -> Tuple[List[Dict[str, Any]], str]:
    if not GUARDIAN_API_KEY:
        return [], "error: missing API key"
    cache_key = f"guardian::{query}::{num}"
    cached = _cache_read(cache_key)
    if cached is not None:
        return cached, f"cached {len(cached)} result(s)"
    params = {
        "q": query,
        "api-key": GUARDIAN_API_KEY,
        "page-size": min(num, 10),
        "order-by": "newest",
        "show-fields": "trailText",
    }
    try:
        base_url = "https://content.guardianapis.com/search"
        log_params = {**params, "api-key": "***"}
        log_status(f"Guardian search: GET {base_url}?{urlencode(log_params)}")
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        message = _sanitize_message(str(exc))
        log_status(f"Guardian search failed for '{query}': {message}")
        return [], f"error: {message}"
    response_payload = data.get("response") or {}
    results = response_payload.get("results") or []
    articles: List[Dict[str, Any]] = []
    for item in results[:num]:
        fields = item.get("fields") or {}
        articles.append(
            {
                "title": item.get("webTitle"),
                "summary": fields.get("trailText"),
                "url": item.get("webUrl"),
                "source": "The Guardian",
                "published": item.get("webPublicationDate"),
            }
        )
    _cache_write(cache_key, articles)
    return articles, f"{len(articles)} result(s)"


def _run_search_with_priority(
    query: str, providers: Sequence[str]
) -> Tuple[List[Dict[str, Any]], Optional[str], List[Tuple[str, str]]]:
    attempts: List[Tuple[str, str]] = []
    for provider in providers:
        provider_lower = provider.lower()
        if provider_lower == "google_custom_search":
            results, status = _google_custom_search(query)
        elif provider_lower == "newsapi":
            results, status = _newsapi_search(query)
        elif provider_lower == "gnews":
            results, status = _gnews_search(query)
        elif provider_lower == "guardian":
            results, status = _guardian_search(query)
        else:
            status = "error: unknown provider"
            log_status(f"Unknown search provider '{provider}' for query '{query}'")
            results = []
        attempts.append((provider_lower, status))
        if results:
            return results, provider_lower, attempts
    fallback_provider = providers[-1].lower() if providers else None
    return [], fallback_provider, attempts


def _execute_search_tasks(
    ticker: str,
    config: PromptConfig,
    extra_placeholders: Optional[Mapping[str, str]] = None,
) -> Dict[str, List[Dict[str, Any]]]:
    tasks: List[Tuple[str, str, str]] = []
    placeholder_values = {
        "ticker": ticker.upper(),
        "ticker_lower": ticker.lower(),
    }
    if extra_placeholders:
        for key, value in extra_placeholders.items():
            try:
                placeholder_values[str(key)] = str(value)
            except Exception:
                continue

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
        priority_chain = SEARCH_PROVIDER_PRIORITY.get(provider_lower, [provider_lower])
        log_status(f"  {provider_lower} search -> {query} (priority: {', '.join(priority_chain)})")
        data, provider_used, attempts = _run_search_with_priority(query, priority_chain)
        for attempt_provider, attempt_status in attempts:
            log_status(f"    {attempt_provider}: {attempt_status}")
        results[provider_lower].append(
            {
                "query": query,
                "source": source,
                "results": data,
                "provider_used": provider_used,
                "attempts": attempts,
            }
        )

    return results


def gather_market_headlines(max_articles: int = 8) -> Tuple[List[Dict[str, Optional[str]]], List[str]]:
    queries = [
        "US stock market today",
        "S&P 500 futures outlook",
        "Wall Street catalysts next 24 hours",
    ]
    per_query = max(1, max_articles // len(queries) or 1)
    headlines: List[Dict[str, Optional[str]]] = []
    provider_notes: List[str] = []
    for query in queries:
        log_status(f"Market headlines search -> {query}")
        results, provider_used, attempts = _run_search_with_priority(query, ["newsapi", "gnews", "guardian"])
        for attempt_provider, status in attempts:
            log_status(f"    {attempt_provider}: {status}")
        if results:
            headlines.extend(results[:per_query])
            label = (provider_used or "unknown").lower()
            provider_notes.append(f"{label} ({query})")
        if len(headlines) >= max_articles:
            break
    return headlines[:max_articles], provider_notes


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


def massive_get(path: str, api_key: str, params: Optional[Dict[str, Any]] = None, timeout: int = 10) -> requests.Response:
    """Perform a GET request against the Massive API with shared auth handling."""

    query = dict(params or {})
    if api_key and "apiKey" not in query:
        query["apiKey"] = api_key
    url = f"{MASSIVE_API_BASE}{path}"
    return requests.get(url, params=query, timeout=timeout)


def describe_massive_request(path: str, params: Optional[Mapping[str, Any]] = None) -> str:
    """Return a sanitized URL string suitable for logging Massive requests."""

    query_items: List[Tuple[str, Any]] = []
    for key, value in (params or {}).items():
        if value is None:
            continue
        query_items.append((key, value))
    query_items.append(("apiKey", "***"))
    query_string = urlencode(query_items, doseq=True)
    return f"{MASSIVE_API_BASE}{path}" + (f"?{query_string}" if query_string else "")


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


def fetch_massive_histories(ticker: str, api_key: str) -> Dict[str, pd.DataFrame]:
    """Retrieve 5 years of daily bars from massive.com and derive shorter windows."""

    base_path = f"/v2/aggs/ticker/{ticker.upper()}/range/1/day"
    today = dt.date.today()
    start = today - dt.timedelta(days=5 * 365 + 30)
    params = {
        "adjusted": "true",
        "sort": "asc",
        "limit": 5000,
    }
    try:
        path = f"{base_path}/{start.isoformat()}/{today.isoformat()}"
        log_status(f"Requesting {ticker.upper()} prices from massive.com... ({describe_massive_request(path, params)})")
        response = massive_get(path, api_key, params=params, timeout=30)
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
            histories = fetch_massive_histories(ticker, api_key)
            log_status("Price data acquired from massive.com.")
            return histories, "massive.com"
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


def fetch_massive_earnings_calendar(ticker: str, api_key: Optional[str], limit: int = 4) -> List[Dict[str, Any]]:
    def mask(value: str) -> str:
        if len(value) <= 4:
            return "***"
        return f"{value[:4]}***{value[-2:]}"

    if not api_key:
        log_status("Massive earnings: no API key available; skipping lookup.")
        return []
    masked_key = mask(api_key)
    if api_key == DEFAULT_MASSIVE_KEY:
        log_status("Massive earnings: demo key detected; skipping lookup to avoid 404 spam.")
        return []
    params = {
        "ticker": ticker.upper(),
        "limit": limit,
    }
    path = "/benzinga/v1/earnings"
    log_status(f"Massive earnings: attempting request with key {masked_key}")
    log_status(f"Massive earnings: GET {describe_massive_request(path, params)}")
    try:
        response = massive_get(path, api_key, params=params, timeout=10)
    except Exception as exc:
        log_status(f"Massive earnings HTTP request failed: {exc}")
        return []
    sanitized_url = response.url.replace(api_key, "<redacted>")
    log_status(f"Massive earnings: response {response.status_code} from {sanitized_url}")
    if response.status_code == 401:
        log_status("Massive earnings: key rejected with 401 Unauthorized.")
        return []
    if response.status_code == 403:
        try:
            detail = response.json().get("message")
        except Exception:
            detail = None
        if detail:
            log_status(f"Massive earnings: access denied (403) - {detail}")
        else:
            log_status("Massive earnings: access denied with 403 Forbidden.")
        return []
    if response.status_code == 404:
        log_status("Massive earnings: endpoint returned 404; falling back to yfinance.")
        return []
    try:
        response.raise_for_status()
    except Exception as exc:
        log_status(f"Massive earnings lookup failed: {exc}")
        return []
    try:
        data = response.json()
    except ValueError as exc:
        log_status(f"Massive earnings: failed to parse JSON response: {exc}")
        return []
    raw_results = data.get("results", [])
    if not raw_results:
        log_status("Massive earnings: key accepted but no results returned.")
        return []
    log_status(f"Massive earnings: key accepted; received {len(raw_results)} records.")
    results: List[Dict[str, Any]] = []

    def sort_key(item: Dict[str, Any]) -> Tuple[Any, Any]:
        return (item.get("date") or "", item.get("time") or "")

    for item in sorted(raw_results, key=sort_key, reverse=True)[:limit]:
        results.append(
            {
                "report_date": item.get("date"),
                "eps_estimate": item.get("estimated_eps"),
                "eps_actual": item.get("actual_eps"),
                "revenue_estimate": item.get("estimated_revenue"),
                "revenue_actual": item.get("actual_revenue"),
            }
        )
    return results


def cache_massive_logo(ticker: str, logo_url: Optional[str], api_key: Optional[str]) -> Optional[str]:
    """Download the company logo from massive.com and store it within the repo."""

    if not logo_url:
        return None
    if not api_key:
        log_status("Massive logo: no API key available; skipping download.")
        return None
    try:
        parsed = urlparse(logo_url)
    except Exception as exc:
        log_status(f"Massive logo: invalid URL '{logo_url}': {exc}")
        return None
    extension = Path(parsed.path).suffix or ".png"
    if len(extension) > 10:
        extension = ".png"
    sanitized_extension = extension.lower()
    if sanitized_extension not in {".png", ".jpg", ".jpeg", ".svg", ".webp"}:
        sanitized_extension = ".png"
    filename = f"{ticker.upper()}{sanitized_extension}"
    cache_path = LOGO_DIR / filename
    relative_logo_path = (
        f"{PUBLIC_BASE_PATH}/assets/logos/{filename}"
        if PUBLIC_BASE_PATH
        else f"/assets/logos/{filename}"
    )
    web_path = (
        f"{PUBLIC_BASE_URL}/assets/logos/{filename}"
        if PUBLIC_BASE_URL
        else relative_logo_path
    )
    if cache_path.exists():
        log_status(f"Massive logo: using cached asset {cache_path.as_posix()}")
        return web_path

    params: Dict[str, Any] = {}
    query_map = parse_qs(parsed.query)
    for key, values in query_map.items():
        if not values:
            continue
        params[key] = values if len(values) > 1 else values[0]
    if parsed.netloc.endswith("massive.com") and "apikey" not in {key.lower() for key in params.keys()}:
        params["apiKey"] = api_key

    sanitized_params: Dict[str, Any] = {}
    for key, value in params.items():
        if key.lower() == "apikey":
            sanitized_params[key] = "***"
        else:
            sanitized_params[key] = value
    query_string = urlencode(sanitized_params, doseq=True)
    sanitized_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    if query_string:
        sanitized_url += f"?{query_string}"
    log_status(f"Massive logo: GET {sanitized_url}")

    try:
        response = requests.get(logo_url, params=params or None, timeout=20)
        response.raise_for_status()
    except Exception as exc:
        log_status(f"Massive logo download failed: {exc}")
        return None

    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_bytes(response.content)
    except Exception as exc:
        log_status(f"Massive logo write failed: {exc}")
        return None
    log_status(f"Massive logo: cached to {cache_path.as_posix()}")
    return web_path


def fetch_massive_company_profile(ticker: str, api_key: Optional[str]) -> Optional[Dict[str, Any]]:
    """Retrieve company metadata, including branding assets, from massive.com."""

    if not api_key:
        log_status("Massive profile: no API key available; skipping lookup.")
        return None
    path = f"/v3/reference/tickers/{ticker.upper()}"
    try:
        log_status(f"Massive profile: GET {describe_massive_request(path)}")
        response = massive_get(path, api_key)
    except Exception as exc:
        log_status(f"Massive profile HTTP request failed: {exc}")
        return None
    sanitized_url = response.url.replace(api_key, "<redacted>")
    log_status(f"Massive profile: response {response.status_code} from {sanitized_url}")
    if response.status_code != 200:
        return None
    try:
        payload = response.json()
    except ValueError as exc:
        log_status(f"Massive profile: failed to parse JSON response: {exc}")
        return None
    profile = payload.get("results") or payload.get("result")
    if not isinstance(profile, Mapping):
        log_status("Massive profile: no results returned.")
        return None
    branding = profile.get("branding") or {}
    address = profile.get("address") or {}
    log_status("Massive profile: company metadata retrieved successfully.")
    return {
        "ticker": profile.get("ticker"),
        "name": profile.get("name"),
        "market": profile.get("market"),
        "locale": profile.get("locale"),
        "primary_exchange": profile.get("primary_exchange"),
        "type": profile.get("type"),
        "sic_code": profile.get("sic_code"),
        "sic_description": profile.get("sic_description"),
        "description": profile.get("description"),
        "homepage_url": profile.get("homepage_url"),
        "total_employees": profile.get("total_employees"),
        "list_date": profile.get("list_date"),
        "market_cap": profile.get("market_cap"),
        "logo_url": branding.get("logo_url"),
        "icon_url": branding.get("icon_url"),
        "address": {
            "address1": address.get("address1"),
            "city": address.get("city"),
            "state": address.get("state"),
            "postal_code": address.get("postal_code"),
            "country": address.get("country"),
        },
    }


def fetch_massive_related_companies(ticker: str, api_key: Optional[str]) -> List[str]:
    """Fetch related companies/competitors from massive.com."""

    if not api_key:
        log_status("Massive related companies: no API key available; skipping lookup.")
        return []
    path = f"/v1/related-companies/{ticker.upper()}"
    try:
        log_status(f"Massive related companies: GET {describe_massive_request(path)}")
        response = massive_get(path, api_key)
    except Exception as exc:
        log_status(f"Massive related companies HTTP request failed: {exc}")
        return []
    sanitized_url = response.url.replace(api_key, "<redacted>")
    log_status(f"Massive related companies: response {response.status_code} from {sanitized_url}")
    if response.status_code != 200:
        return []
    try:
        payload = response.json()
    except ValueError as exc:
        log_status(f"Massive related companies: failed to parse JSON response: {exc}")
        return []
    results = payload.get("results") or payload.get("companies") or []
    competitors: List[str] = []
    for entry in results:
        if isinstance(entry, Mapping):
            name = entry.get("name") or entry.get("company_name")
            ticker_value = entry.get("ticker") or entry.get("symbol")
            label = name or ticker_value
            if label:
                competitors.append(str(label))
    log_status(f"Massive related companies: retrieved {len(competitors)} entries.")
    return competitors


def fetch_massive_open_close(ticker: str, date_value: str, api_key: Optional[str]) -> Optional[Dict[str, Any]]:
    """Obtain daily open/close summary for a specific date."""

    if not api_key:
        log_status("Massive open-close: no API key available; skipping lookup.")
        return None
    path = f"/v1/open-close/{ticker.upper()}/{date_value}"
    try:
        log_status(f"Massive open-close: GET {describe_massive_request(path)}")
        response = massive_get(path, api_key)
    except Exception as exc:
        log_status(f"Massive open-close HTTP request failed: {exc}")
        return None
    sanitized_url = response.url.replace(api_key, "<redacted>")
    log_status(f"Massive open-close: response {response.status_code} from {sanitized_url}")
    if response.status_code != 200:
        return None
    try:
        payload = response.json()
    except ValueError as exc:
        log_status(f"Massive open-close: failed to parse JSON response: {exc}")
        return None
    status = str(payload.get("status", "")).lower()
    if status not in {"ok", "success"}:
        log_status(f"Massive open-close: unexpected status '{status}'.")
        return None
    return payload


def fetch_massive_previous_close(ticker: str, api_key: Optional[str]) -> Optional[Dict[str, Any]]:
    """Retrieve previous-day OHLC information."""

    if not api_key:
        log_status("Massive previous close: no API key available; skipping lookup.")
        return None
    path = f"/v2/aggs/ticker/{ticker.upper()}/prev"
    params = {"adjusted": "true"}
    try:
        log_status(f"Massive previous close: GET {describe_massive_request(path, params)}")
        response = massive_get(path, api_key, params=params)
    except Exception as exc:
        log_status(f"Massive previous close HTTP request failed: {exc}")
        return None
    sanitized_url = response.url.replace(api_key, "<redacted>")
    log_status(f"Massive previous close: response {response.status_code} from {sanitized_url}")
    if response.status_code != 200:
        return None
    try:
        payload = response.json()
    except ValueError as exc:
        log_status(f"Massive previous close: failed to parse JSON response: {exc}")
        return None
    results = payload.get("results") or []
    if not results:
        log_status("Massive previous close: no results returned.")
        return None
    return results[0]


def _extract_indicator_payload(response: requests.Response, api_key: str, label: str) -> Optional[Dict[str, Any]]:
    sanitized_url = response.url.replace(api_key, "<redacted>")
    log_status(f"{label}: response {response.status_code} from {sanitized_url}")
    if response.status_code != 200:
        return None
    try:
        payload = response.json()
    except ValueError as exc:
        log_status(f"{label}: failed to parse JSON response: {exc}")
        return None
    raw_results = payload.get("results")
    if isinstance(raw_results, list):
        results = raw_results
    elif isinstance(raw_results, Mapping):
        values = raw_results.get("values")
        if isinstance(values, list) and values:
            results = values
        else:
            results = [raw_results]
    elif raw_results is None:
        results = []
    else:
        results = [raw_results]
    if not results:
        log_status(f"{label}: no results returned.")
        return None
    latest = results[0]
    if isinstance(latest, Mapping):
        values = latest.get("value")
        if values is None:
            values = {k: v for k, v in latest.items() if k != "timestamp"}
        timestamp = latest.get("timestamp") or latest.get("time") or latest.get("t")
    else:
        values = {"value": latest}
        timestamp = None
    if values is None:
        values = {"value": latest}
    return {"timestamp": timestamp, "values": values}


def fetch_massive_indicators(ticker: str, api_key: Optional[str]) -> Dict[str, Dict[str, Any]]:
    """Gather technical indicators (SMA, EMA, MACD, RSI) from massive.com."""

    if not api_key:
        log_status("Massive indicators: no API key available; skipping lookup.")
        return {}

    indicators: Dict[str, Dict[str, Any]] = {}
    indicator_requests = [
        (
            "Massive SMA",
            f"/v1/indicators/sma/{ticker.upper()}",
            {
                "timespan": "day",
                "window": 50,
                "series_type": "close",
                "order": "desc",
                "limit": 1,
                "adjusted": "true",
            },
            "sma",
        ),
        (
            "Massive EMA",
            f"/v1/indicators/ema/{ticker.upper()}",
            {
                "timespan": "day",
                "window": 50,
                "series_type": "close",
                "order": "desc",
                "limit": 1,
                "adjusted": "true",
            },
            "ema",
        ),
        (
            "Massive MACD",
            f"/v1/indicators/macd/{ticker.upper()}",
            {
                "timespan": "day",
                "series_type": "close",
                "fast": 12,
                "slow": 26,
                "signal": 9,
                "order": "desc",
                "limit": 1,
                "adjusted": "true",
            },
            "macd",
        ),
        (
            "Massive RSI",
            f"/v1/indicators/rsi/{ticker.upper()}",
            {
                "timespan": "day",
                "window": 14,
                "series_type": "close",
                "order": "desc",
                "limit": 1,
                "adjusted": "true",
            },
            "rsi",
        ),
    ]
    for label, path, params, slug in indicator_requests:
        try:
            log_status(f"{label}: GET {describe_massive_request(path, params)}")
            response = massive_get(path, api_key, params=params)
        except Exception as exc:
            log_status(f"{label}: HTTP request failed: {exc}")
            continue
        payload = _extract_indicator_payload(response, api_key, label)
        if payload:
            indicators[slug] = payload
    return indicators


def fetch_massive_news(ticker: str, api_key: Optional[str], limit: int = 5) -> List[Dict[str, Optional[str]]]:
    """Pull recent news articles from massive.com."""

    if not api_key:
        log_status("Massive news: no API key available; skipping lookup.")
        return []
    params = {
        "ticker": ticker.upper(),
        "limit": limit,
        "order": "desc",
    }
    path = "/v2/reference/news"
    try:
        log_status(f"Massive news: GET {describe_massive_request(path, params)}")
        response = massive_get(path, api_key, params=params)
    except Exception as exc:
        log_status(f"Massive news HTTP request failed: {exc}")
        return []
    sanitized_url = response.url.replace(api_key, "<redacted>")
    log_status(f"Massive news: response {response.status_code} from {sanitized_url}")
    if response.status_code != 200:
        return []
    try:
        payload = response.json()
    except ValueError as exc:
        log_status(f"Massive news: failed to parse JSON response: {exc}")
        return []
    results = payload.get("results") or []
    stories: List[Dict[str, Optional[str]]] = []
    for item in results[:limit]:
        if not isinstance(item, Mapping):
            continue
        title = item.get("title")
        if not title:
            continue
        stories.append(
            {
                "title": title,
                "summary": item.get("description"),
                "published": item.get("published_utc"),
                "url": item.get("article_url"),
                "source": item.get("publisher", {}).get("name") if isinstance(item.get("publisher"), Mapping) else None,
            }
        )
    log_status(f"Massive news: collected {len(stories)} articles.")
    return stories


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
    resistance_30d = float("nan")
    support_30d = float("nan")
    history_3mo = histories.get("3mo")
    if history_3mo is not None and not history_3mo.empty:
        window_30 = history_3mo.tail(30)
        if not window_30.empty:
            resistance_30d = float(window_30["High"].max())
            support_30d = float(window_30["Low"].min())
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
        "30d Resistance": f"{resistance_30d:.2f}" if resistance_30d and not math.isnan(resistance_30d) else "unknown",
        "30d Support": f"{support_30d:.2f}" if support_30d and not math.isnan(support_30d) else "unknown",
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


def _collect_prompt_notes(prompt_config: PromptConfig) -> Dict[str, Any]:
    return {
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


def _compute_market_metric(spec: Mapping[str, str]) -> Optional[Dict[str, Any]]:
    symbol = spec.get("symbol")
    label = spec.get("label") or symbol
    category = spec.get("category") or "other"
    if not symbol:
        return None
    ticker_obj = yf.Ticker(symbol)
    try:
        history = ticker_obj.history(period="2mo", interval="1d")
    except Exception as exc:
        log_status(f"Failed to fetch history for {label} ({symbol}): {exc}")
        return None
    if history.empty or "Close" not in history:
        log_status(f"No closing prices available for {label} ({symbol}); skipping.")
        return None
    closes = history["Close"].dropna()
    if closes.empty:
        log_status(f"All closing prices missing for {label} ({symbol}); skipping.")
        return None
    latest_close = float(closes.iloc[-1])
    latest_timestamp = closes.index[-1]
    if isinstance(latest_timestamp, dt.datetime):
        latest_date = latest_timestamp.date().isoformat()
    else:
        latest_date = str(latest_timestamp)
    changes: Dict[str, Dict[str, Optional[float]]] = {}
    for window, key in ((1, "1d"), (7, "7d"), (30, "30d")):
        if len(closes) <= window:
            changes[key] = {"absolute": None, "percent": None, "reference": None}
            continue
        prior = float(closes.iloc[-(window + 1)])
        absolute = latest_close - prior
        percent = (absolute / prior * 100) if prior else None
        changes[key] = {
            "absolute": absolute,
            "percent": percent,
            "reference": prior,
        }
    return {
        "symbol": symbol,
        "label": label,
        "category": category,
        "last_close": latest_close,
        "last_updated": latest_date,
        "changes": changes,
    }


def _describe_market_metric(metric: Mapping[str, Any]) -> str:
    def format_change(key: str) -> str:
        payload = metric.get("changes", {}).get(key) or {}
        pct = payload.get("percent")
        if pct is None or math.isnan(pct):
            return f"{key} n/a"
        return f"{key} {pct:+.2f}%"

    value_parts = [
        format_change("1d"),
        format_change("7d"),
        format_change("30d"),
    ]
    last_close = metric.get("last_close")
    if isinstance(last_close, (int, float)) and not math.isnan(last_close):
        value_parts.append(f"last {last_close:,.2f}")
    return " | ".join(value_parts)


def build_market_quick_facts(
    metrics: Sequence[Mapping[str, Any]],
    prompt_config: PromptConfig,
) -> "OrderedDict[str, Dict[str, str]]":
    lookup = {metric.get("label"): metric for metric in metrics}
    facts: "OrderedDict[str, Dict[str, str]]" = OrderedDict()
    for number in prompt_config.quick_fact_numbers:
        bullet = prompt_config.bullets.get(number)
        label = (bullet.label if bullet else None) or (bullet.prompt if bullet else None) or number
        metric = lookup.get(label)
        value = _describe_market_metric(metric) if metric else "unknown"
        facts[number] = {"label": label, "value": value}
    return facts


def gather_market_context(prompt_config: PromptConfig) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Collect multi-asset data for the GodsEye aggregate report."""

    log_status("Collecting benchmark performance for GodsEye...")
    metrics: List[Dict[str, Any]] = []
    missing_series: List[str] = []
    latest_trading_day: Optional[str] = None
    for spec in MARKET_BENCHMARKS:
        metric = _compute_market_metric(spec)
        if metric:
            metrics.append(metric)
            latest_trading_day = latest_trading_day or metric.get("last_updated")
        else:
            missing_series.append(spec.get("label") or spec.get("symbol"))
    if not metrics:
        raise RuntimeError("Failed to compute benchmark metrics for GodsEye.")

    log_status(f"Computed {len(metrics)} benchmark series; building quick facts...")
    quick_facts = build_market_quick_facts(metrics, prompt_config)
    quick_fact_map = {meta["label"]: meta["value"] for meta in quick_facts.values()}
    quick_fact_rows = [
        {"number": number, "label": data["label"], "value": data["value"]}
        for number, data in quick_facts.items()
    ]

    news_items, headline_notes = gather_market_headlines()
    news_source = ", ".join(
        sorted({note.split()[0].upper() for note in headline_notes if note})
    ) or "newsapi/gnews/guardian"

    search_results = _execute_search_tasks(
        GODSEYE_TICKER,
        prompt_config,
        extra_placeholders={"ticker": "market", "ticker_lower": "market"},
    )
    prompt_notes = _collect_prompt_notes(prompt_config)

    breadth_counts = {"up": 0, "down": 0, "flat": 0}
    index_changes: List[float] = []
    for metric in metrics:
        change = metric.get("changes", {}).get("1d", {}).get("percent")
        if change is None or math.isnan(change):
            continue
        if metric.get("category") in {"index", "etf"}:
            index_changes.append(change)
        if change > 0:
            breadth_counts["up"] += 1
        elif change < 0:
            breadth_counts["down"] += 1
        else:
            breadth_counts["flat"] += 1
    average_index_change = statistics.fmean(index_changes) if index_changes else None
    vix_metric = next((metric for metric in metrics if metric.get("symbol") == "^VIX"), None)
    treasury_metric = next((metric for metric in metrics if metric.get("symbol") == "^TNX"), None)

    market_health = {
        "breadth": breadth_counts,
        "avg_index_change_1d": average_index_change,
        "vix": vix_metric,
        "treasury_10y": treasury_metric,
    }

    data_sources = [
        "yfinance: benchmark closes & change calculations",
        f"market headlines: {news_source}",
    ]
    if missing_series:
        data_sources.append(f"missing series: {', '.join(missing_series)}")

    context = {
        "ticker": GODSEYE_TICKER,
        "company": {
            "long_name": "GodsEye Market Monitor",
            "sector": "Macro Overview",
            "industry": "Multi-asset",
            "summary": "Aggregate read on equities, futures, rates, commodities, and volatility.",
        },
        "market_metrics": metrics,
        "market_health": market_health,
        "market_notes": {"missing_series": missing_series},
        "news": news_items,
        "news_source": news_source,
        "quick_facts": quick_fact_map,
        "quick_fact_rows": quick_fact_rows,
        "search_results": search_results,
        "prompt_notes": prompt_notes,
        "data_sources": data_sources,
        "price_data_source": "yfinance",
        "price_snapshot": {},
        "buy_sell_levels": {},
        "volume_assessment": {},
        "volatility_assessment": {},
        "massive_technicals": {},
        "market_prediction_window_hours": 24,
    }
    storage_payload = {
        "histories": {},
        "latest_trading_day": latest_trading_day,
        "price_source": "yfinance",
    }
    return context, storage_payload


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


def gather_context(ticker: str, prompt_config: PromptConfig) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Collect pricing, fundamentals, and news data for the LLM and storage."""

    log_status("Gathering market data...")
    ticker_upper = ticker.upper()
    massive_api_key = _load_massive_api_key()
    histories, price_source = get_price_histories(ticker)
    hist_10d = histories["10d"]
    if hist_10d.empty:
        raise RuntimeError("No historical price data returned.")
    latest_session_ts = hist_10d.index.max()
    if isinstance(latest_session_ts, pd.Timestamp):
        latest_session_date = latest_session_ts.date().isoformat()
    elif latest_session_ts:
        latest_session_date = str(latest_session_ts)
    else:
        latest_session_date = None
    open_close_snapshot = (
        fetch_massive_open_close(ticker, latest_session_date, massive_api_key)
        if latest_session_date
        else None
    )
    previous_close_snapshot = fetch_massive_previous_close(ticker, massive_api_key)
    indicator_payloads = fetch_massive_indicators(ticker, massive_api_key)
    log_status("Calculating technical snapshot...")
    snapshot = compute_price_snapshot(hist_10d)
    log_status("Fetching company profile (massive.com)...")
    massive_profile = fetch_massive_company_profile(ticker, massive_api_key)
    if massive_profile:
        logo_local_path = cache_massive_logo(ticker, massive_profile.get("logo_url"), massive_api_key)
        massive_profile["logo_path"] = logo_local_path
    related_companies = fetch_massive_related_companies(ticker, massive_api_key)
    log_status("Fetching company fundamentals...")
    ticker_obj = yf.Ticker(ticker)
    info = ticker_obj.info or {}
    financial_metrics = extract_financial_metrics(info, ticker_obj)
    log_status("Retrieving earnings calendar...")
    massive_calendar = fetch_massive_earnings_calendar(ticker, massive_api_key)
    if massive_calendar:
        earnings_calendar = massive_calendar
        earnings_calendar_source = "massive.com"
    else:
        earnings_calendar = fetch_yfinance_earnings_calendar(ticker_obj)
        earnings_calendar_source = "yfinance"
    log_status("Assembling quick facts...")
    quick_facts = build_quick_facts(snapshot, histories, financial_metrics, prompt_config)
    log_status("Collecting latest headlines (massive.com)...")
    news_items = fetch_massive_news(ticker, massive_api_key)
    massive_news_note: Optional[str] = None
    if not massive_api_key:
        massive_news_note = "headlines skipped (missing API key)"
    if news_items:
        log_status(f"  massive.com returned {len(news_items)} headlines")
        news_source = "massive.com"
    else:
        log_status("  massive.com returned no headlines; falling back to yfinance.")
        news_items = collect_news(ticker_obj)
        log_status(f"  yfinance returned {len(news_items)} headlines")
        news_source = "yfinance"
        if massive_api_key and massive_news_note is None:
            massive_news_note = "headlines (none)"
    log_status("Running supplementary searches...")
    search_results = _execute_search_tasks(ticker, prompt_config)
    volume_metrics = evaluate_volume_label(snapshot)
    volatility_metrics = evaluate_volatility_label(snapshot)
    quick_fact_map = {meta["label"]: meta["value"] for meta in quick_facts.values()}
    prompt_notes = _collect_prompt_notes(prompt_config)

    source_notes: Dict[str, List[str]] = defaultdict(list)

    def add_source_note(source: Optional[str], description: str) -> None:
        if not source:
            source = "unknown"
        notes = source_notes[source]
        if description not in notes:
            notes.append(description)

    add_source_note(price_source, "prices & technicals")
    if massive_profile:
        add_source_note("massive.com", "company profile & branding")
    else:
        add_source_note("yfinance", "company profile")
    add_source_note("yfinance", "fundamentals")
    add_source_note(earnings_calendar_source, "earnings calendar")
    if indicator_payloads or open_close_snapshot or previous_close_snapshot:
        add_source_note("massive.com", "technical indicators")
    headlines_note = (
        f"headlines ({len(news_items)} items)" if news_items else "headlines (none)"
    )
    add_source_note(news_source, headlines_note)
    if massive_news_note and news_source != "massive.com":
        add_source_note("massive.com", massive_news_note)

    provider_labels = {
        "google_custom_search": "Google Custom Search",
        "newsapi": "NewsAPI",
        "gnews": "GNews",
        "guardian": "The Guardian",
    }

    ticker_pattern = re.compile(rf"\b{re.escape(ticker_upper)}\b", flags=re.IGNORECASE)

    for provider_results in search_results.values():
        for entry in provider_results:
            query = (entry.get("query") or "").strip()
            query_display = query
            if query_display:
                stripped = ticker_pattern.sub("", query_display)
                stripped = re.sub(r"\s{2,}", " ", stripped).strip(" ,;-")
                if stripped:
                    query_display = stripped
            results = entry.get("results") or []
            provider_used = entry.get("provider_used")
            if not results:
                continue
            friendly = provider_labels.get(provider_used, provider_used or "unknown")
            label = query_display or "(unspecified query)"
            add_source_note(friendly, label)

    data_sources: List[str] = []
    source_order = [
        "massive.com",
        "yfinance",
        "Google Custom Search",
        "NewsAPI",
        "GNews",
        "The Guardian",
    ]
    remaining_sources = [source for source in source_notes.keys() if source not in source_order]
    for source in source_order + sorted(remaining_sources):
        notes = source_notes.get(source)
        if not notes:
            continue
        data_sources.append(f"{source}: {', '.join(notes)}")

    context_data = {
        "ticker": ticker_upper,
        "company": {
            "long_name": (massive_profile or {}).get("name") or info.get("longName"),
            "sector": info.get("sector") or (massive_profile or {}).get("sic_description"),
            "industry": info.get("industry") or (massive_profile or {}).get("sic_description"),
            "country": info.get("country") or ((massive_profile or {}).get("address") or {}).get("country"),
            "summary": (massive_profile or {}).get("description") or info.get("longBusinessSummary"),
            "homepage_url": (massive_profile or {}).get("homepage_url") or info.get("website"),
            "logo_url": (massive_profile or {}).get("logo_url"),
            "logo_path": (massive_profile or {}).get("logo_path"),
            "icon_url": (massive_profile or {}).get("icon_url"),
            "competitor_candidates": related_companies or guess_competitors(info.get("industry"), info.get("sector")),
            "related_companies": related_companies,
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
        "massive_technicals": {
            "latest_open_close": open_close_snapshot,
            "previous_close": previous_close_snapshot,
            "indicators": indicator_payloads,
        },
        "news": news_items,
        "news_source": news_source,
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
    storage_payload = {
        "histories": histories,
        "latest_trading_day": latest_session_date,
        "price_source": price_source,
    }
    return context_data, storage_payload


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
    company_info = context.get("company") or {}
    logo_path = company_info.get("logo_path") or company_info.get("logo_url")
    if logo_path:
        alt_text = f"{company_info.get('long_name') or context.get('ticker') or 'Company'} logo"
        lines.append(f"![{alt_text}]({logo_path})")
        lines.append("")
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
            lines.append('<div class="quickref-table">')
            lines.append("<table>")
            lines.append("<thead><tr><th>Metric</th><th>Answer</th></tr></thead>")
            lines.append("<tbody>")
            for bullet in bullets:
                if bullet is None:
                    continue
                row = quick_fact_lookup.get(bullet.number, {})
                label_text = bullet.label or bullet.prompt or bullet.number
                value_text = row.get("value", "unknown")
                lines.append(
                    "<tr><td>{label}</td><td>{value}</td></tr>".format(
                        label=html.escape(label_text), value=html.escape(value_text)
                    )
                )
            lines.append("</tbody></table>")
            lines.append("</div>")
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
        lines.append('<div class="sources-list">')
        lines.append("<strong>Sources</strong>")
        lines.append("<ul>")
        for entry in data_sources:
            lines.append(f"<li>{html.escape(entry)}</li>")
        lines.append("</ul>")
        if any(FOOTNOTE_MARKER in entry for entry in data_sources):
            lines.append(f'<p class="sources-footnote">{html.escape(FOOTNOTE_NOTE)}</p>')
        lines.append("</div>")
        lines.append("")
    else:
        lines.append(f"Price data source: {context['price_data_source']}")
    cli_log = context.get("cli_log")
    if cli_log:
        log_block = "\n".join(html.escape(entry) for entry in cli_log)
        lines.append("")
        lines.append("<details class=\"cli-log\">")
        lines.append(f"<summary>Show generation log{FOOTNOTE_MARKER}</summary>")
        lines.append("<pre><code>")
        lines.append(log_block)
        lines.append("</code></pre>")
        lines.append("</details>")
    return "\n".join(lines).strip()


def build_report(
    ticker: str, prompt_config: PromptConfig
) -> Tuple[str, Dict[str, Any], Dict[str, Any]]:
    """Assemble context, call GPT-5 for targeted bullets, and prepare storage payload."""

    _run_log.clear()
    log_status(f"Gathering context for {ticker.upper()}...")
    if ticker.upper() == GODSEYE_TICKER:
        context, storage_payload = gather_market_context(prompt_config)
    else:
        context, storage_payload = gather_context(ticker, prompt_config)
    log_status("Synthesizing narrative from OpenAI response...")
    llm_answers = call_llm(context, prompt_config)
    context["cli_log"] = list(_run_log)
    log_status("Formatting final report...")
    report_body = format_report(context, prompt_config, llm_answers)
    return report_body, context, storage_payload


def write_jekyll_report(
    ticker: str,
    report_body: str,
    generated_at: dt.datetime,
    elapsed_seconds: float,
    output_path: Path,
    *,
    title: Optional[str] = None,
) -> None:
    sanitized = report_body.strip()
    raw_lines = sanitized.splitlines()
    display_title = title or f"{ticker.upper()} Stock Report"
    front_matter_lines = [
        "---",
        "layout: default",
        f'title: "{display_title}"',
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
    """Configure command-line arguments for the report generator."""

    parser = argparse.ArgumentParser(description="Generate a Jekyll-ready GPT-5 stock report.")
    parser.add_argument("ticker", nargs="?", help="Ticker symbol to analyse")
    parser.add_argument(
        "--cycle",
        action="store_true",
        help="Cycle through the next ticker discovered in _reports/ instead of prompting.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Regenerate reports for every ticker already present in _reports/.",
    )
    return parser.parse_args(argv)


def generate_report_for_ticker(ticker: str, prompt_config: PromptConfig) -> None:
    """Generate a report for a single ticker and write it to disk."""

    ticker_clean = ticker.strip().upper()
    if not ticker_clean:
        raise ValueError("Ticker symbol is required.")
    log_status(f"Starting report generation for {ticker_clean}...")
    run_started_at = dt.datetime.now(dt.timezone.utc)
    run_id = STORAGE.start_run(ticker_clean, run_started_at)
    start_time = time.perf_counter()
    elapsed_seconds: Optional[float] = None
    generated_at: Optional[dt.datetime] = None
    report_body: str
    context: Dict[str, Any] = {}
    storage_payload: Dict[str, Any] = {}
    try:
        report_body, context, storage_payload = build_report(ticker_clean, prompt_config)
        elapsed_seconds = time.perf_counter() - start_time
        generated_at = dt.datetime.now(dt.timezone.utc)
        timestamp_display = generated_at.strftime("%Y-%m-%d %H:%M %Z")
        timestamp_iso = generated_at.isoformat()
        duration_display = format_duration(elapsed_seconds)
        header_line = (
            f"**Generated:** <time class=\"js-local-time\" datetime=\"{timestamp_iso}\">{timestamp_display}</time> "
            f"(runtime {duration_display})"
        )
        trimmed_body = report_body.strip()
        if trimmed_body:
            report_body = f"{header_line}\n\n{trimmed_body}"
        else:
            report_body = header_line
        output_path = REPORTS_DIR / f"{ticker_clean}.md"
        report_title = f"{ticker_clean.upper()} Stock Report"
        if ticker_clean == GODSEYE_TICKER:
            report_title = "GodsEye Market Report"
        write_jekyll_report(
            ticker_clean,
            report_body,
            generated_at,
            elapsed_seconds,
            output_path,
            title=report_title,
        )
        log_status("Persisting structured data snapshot...")
        STORAGE.persist_run_data(
            run_id=run_id,
            symbol=ticker_clean,
            company=context.get("company") or {},
            histories=storage_payload.get("histories") or {},
            price_provider=storage_payload.get("price_source") or context.get("price_data_source") or "unknown",
            latest_trading_day=storage_payload.get("latest_trading_day"),
            context=context,
            generated_at=generated_at,
            runtime_seconds=elapsed_seconds,
        )
    except Exception as exc:
        STORAGE.finish_run(run_id, dt.datetime.now(dt.timezone.utc), "failed", error_message=str(exc))
        raise
    else:
        assert generated_at is not None and elapsed_seconds is not None
        STORAGE.finish_run(run_id, generated_at, "success", elapsed_seconds)
        update_cycle_state(ticker_clean)
        print(f"Saved Jekyll report to {output_path}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point that generates and writes the Markdown report."""

    args = parse_args(argv)
    if args.all and args.cycle:
        raise SystemExit("Do not combine --all with --cycle.")
    if args.cycle and args.ticker:
        raise SystemExit("Do not pass a ticker when using --cycle.")
    if args.all and args.ticker:
        raise SystemExit("Do not pass a ticker when using --all.")
    if args.all:
        tickers = discover_tickers()
        if not tickers:
            raise SystemExit("No existing reports found in _reports/ to rebuild.")
        exit_code = 0
        for ticker in tickers:
            try:
                prompt_config = load_prompt_for_ticker(ticker)
                generate_report_for_ticker(ticker, prompt_config)
            except Exception as exc:  # pylint: disable=broad-except
                exit_code = 1
                log_status(f"Error generating report for {ticker}: {exc}")
        return exit_code

    if args.cycle:
        ticker = select_next_ticker()
        log_status(f"Cycling to next tracked ticker: {ticker}")
    else:
        ticker = args.ticker or input("Enter ticker symbol: ").strip()
    if not ticker:
        raise SystemExit("Ticker symbol is required.")
    prompt_config = load_prompt_for_ticker(ticker)
    generate_report_for_ticker(ticker, prompt_config)
    return 0


if __name__ == "__main__":  # Allow the script to be executed directly.
    raise SystemExit(main())
