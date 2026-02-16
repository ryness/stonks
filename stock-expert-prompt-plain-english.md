---
layout: default
title: LLM Prompts (Sent to OpenAI)
---

# LLM Prompts (What OpenAI Actually Receives)

This page shows the prompt shape that is actually sent to OpenAI by `src/gostonks.py`, with runtime fields shown as placeholders.

## Shared OpenAI Request Envelope

Both stock reports and GodsEye use the same API call wrapper:

```text
{
  "model": "gpt-5.1",
  "input": [
    {
      "role": "system",
      "content": "You are an expert stock analyst. Produce grounded, concise answers."
    },
    {
      "role": "user",
      "content": "Use the structured data to answer the specified report bullets.\nReturn a VALID JSON object with exactly the keys listed below and no extra commentary.\n{SCHEMA_LINES_FROM_PROMPT_CONFIG}\nRules:\n- Provide plain text answers without numbering or markdown.\n- Do not insert newline characters inside individual values.\n- If information is unavailable, respond with the string \"unknown\".\n- Ground every statement in the provided data; do not speculate.\n\nContext JSON:\n<json>\n{RUNTIME_CONTEXT_JSON}\n</json>"
    }
  ]
}
```

`{SCHEMA_LINES_FROM_PROMPT_CONFIG}` is built from the YAML in `config/stock-expert_prompt.txt` or `config/godseye_prompt.txt`.

`{RUNTIME_CONTEXT_JSON}` is built from live data gathered in code (prices, technicals, headlines, searches, quick facts, etc.).

## Stock Expert: Schema Lines Sent

For ticker reports, the keys below are required in the model's JSON response:

```text
- "0.1": string answering "Long Entry?" based on "Given the stock's history, macro bubble/froth risks, and where it sits versus its averages/support, is this a good moment to initiate or add to a long position?". Return one sentence formatted as '<verdict> — <supporting clause>; <supporting clause>' referencing the provided data only. Instruction: Lead with 'yes', 'no', or 'maybe', then cite specific historical positioning, macro froth cues (or lack thereof), and placement relative to moving averages or support/resistance.
- "1.1": string answering "Activities" based on "What does the company do?". Respond in 2-3 sentences describing the core products, services, and segments.
- "1.2": string answering "Profitable?" based on "Is it profitable? If not, when does it become profitable?". Answer yes or no with a brief justification referencing profitability or path to profitability.
- "1.3": string answering "Customer & Markets" based on "Who are its primary customers and what are its markets?". Summarize the key customer types and geographic/industry markets in 2-3 sentences.
- "1.4": string answering "Competition" based on "Who are its primary competitors and where does it rank among them?". Describe principal competitors and any relative positioning in 1-2 sentences.
- "2.1": string answering "7d Trend?" based on "Over the last 3–7 trading days, what trend is it on?". Return 'up', 'down', or 'flat' and add a concise clause citing supporting price action.
- "2.2": string answering "7d Buy/Sell Points?" based on "What values during this time were good points to buy and to sell?". Highlight notable buy and sell levels in 1-2 sentences.
- "2.3.1": string answering "7d Volume" based on "What relative degree of volume over the last 3–7 trading days?". Return only 'high', 'med', 'low', or 'unknown'. If unclear, return 'unknown'.
- "2.3.2": string answering "7d Volatility" based on "What relative degree of volatility over the last 3–7 trading days?". Return only 'high', 'med', 'low', or 'unknown'.
- "3.1": string answering "Stability?" based on "Is this a fly-by-night or a stable institution?". Provide 3-5 sentences discussing longevity, balance sheet, and overall stability.
- "3.2": string answering "Innovating?" based on "Is it innovating and growing or stale?". Respond in 1-2 sentences indicating whether innovation/growth is evident, citing specifics.
- "4.1": string answering "News" based on "Summarize recent context, news, and rumor considering the 'buy the rumor, sell the news' adage.". Produce 3-5 sentences referencing only supplied headlines and data; note implications for the adage.
- "4.2": string answering "Tarrifs" based on "What are the effects of tariffs on this company's stock?". Provide 1-2 sentences summarizing tariff impacts, or state 'unknown' if not covered in data.
```

## Stock Expert: Context JSON Shape Sent

```json
{
  "ticker": "<TICKER>",
  "company": {
    "long_name": "<COMPANY_NAME>",
    "sector": "<SECTOR>",
    "industry": "<INDUSTRY>",
    "country": "<COUNTRY>",
    "summary": "<BUSINESS_SUMMARY>",
    "homepage_url": "<WEBSITE_URL>",
    "logo_url": "<LOGO_URL>",
    "logo_path": "<LOCAL_LOGO_PATH>",
    "icon_url": "<ICON_URL>",
    "competitor_candidates": ["<PEER_1>", "<PEER_2>"],
    "related_companies": ["<RELATED_1>", "<RELATED_2>"]
  },
  "financials": {
    "net_income_values": ["<Q_VALUES...>"],
    "net_income_sum": "<SUM>",
    "profit_margin": "<PROFIT_MARGIN>",
    "revenue_growth": "<REVENUE_GROWTH>",
    "earnings_growth": "<EARNINGS_GROWTH>",
    "free_cash_flow": "<FCF>",
    "operating_cash_flow": "<OCF>",
    "upcoming_earnings": "<ISO_DATETIME_OR_NULL>"
  },
  "price_snapshot": {
    "close": "<LAST_CLOSE>",
    "resistance": "<7D_RESISTANCE>",
    "support": "<7D_SUPPORT>",
    "local_high": "<LOCAL_HIGH>",
    "local_low": "<LOCAL_LOW>",
    "dma20": "<20DMA>",
    "atr14": "<ATR14>",
    "trend_label": "<UPTREND|DOWNTREND|RANGE>"
  },
  "price_low_lines_chart": "<INLINE_SVG_OR_NULL>",
  "buy_sell_levels": {
    "suggested_buy_zone": "<BUY_LEVEL>",
    "suggested_sell_zone": "<SELL_LEVEL>"
  },
  "volume_assessment": "<VOLUME_OBJECT>",
  "volatility_assessment": "<VOLATILITY_OBJECT>",
  "massive_technicals": {
    "latest_open_close": "<MASSIVE_OPEN_CLOSE>",
    "previous_close": "<MASSIVE_PREV_CLOSE>",
    "indicators": "<MASSIVE_INDICATORS>"
  },
  "news": ["<HEADLINE_OBJECTS...>"],
  "news_source": "<massive.com|yfinance|offline>",
  "latest_news": ["<RECENT_FILTERED_HEADLINES...>"],
  "earnings": {
    "calendar": ["<EARNINGS_ROWS...>"]
  },
  "quick_facts": {
    "<LABEL>": "<VALUE>"
  },
  "quick_fact_rows": [
    {
      "number": "<5.x>",
      "label": "<QUICK_FACT_LABEL>",
      "value": "<QUICK_FACT_VALUE>"
    }
  ],
  "search_results": {
    "google_custom_search": ["<QUERY_RESULTS...>"],
    "newsapi": ["<QUERY_RESULTS...>"],
    "gnews": ["<QUERY_RESULTS...>"],
    "guardian": ["<QUERY_RESULTS...>"]
  },
  "prompt_notes": {
    "sections": ["<SECTION_NOTES_FROM_YAML>"],
    "bullet_instructions": ["<BULLET_INSTRUCTIONS_FROM_YAML>"]
  },
  "price_data_source": "<massive.com|yfinance|offline>",
  "data_sources": ["<SOURCE_SUMMARY_LINES...>"]
}
```

## GodsEye: Schema Lines Sent

For GodsEye (`ticker = GODSEYE`), the keys below are required:

```text
- "1.0": array of 2-3 paragraph strings covering "Summarize the current tone across equities, volatility, futures, and rates.". Each paragraph must be a complete thought. Highlight whether risk appetite is improving or fading and quantify using provided metrics.
- "1.1": string answering "Market Health" based on "How healthy is the market right now based on the benchmark changes?". Reference breadth, average index change, and volatility/treasury context in 3-4 sentences.
- "1.2": string answering "Leadership" based on "Which benchmarks are leading or lagging over the last day and week?". Name at least one positive and one negative standout with their 1d % move.
- "2.1": array of 2-3 paragraph strings covering "What macro or geopolitical themes are driving tape?". Each paragraph must be a complete thought. Tie each catalyst to potential impact (risk-on/off) using provided news summaries.
- "2.2": string answering "Upcoming Triggers" based on "What events or data releases over the next 24h could move the market?". List concrete events (earnings, data, policy) with a short note on expected effect.
- "3.1": string answering "Next 24h Bias" based on "Given everything provided, what is the most likely market direction in the next 24 hours?". Ground the call in benchmark changes plus catalysts. Instruction: Respond with 'up', 'down', or 'flat' followed by confidence % and reasoning.
- "3.2": array of 2-3 paragraph strings covering "What should traders watch overnight and into the next session?". Each paragraph must be a complete thought. Include levels, sectors, or macro prints that align with the predicted move.
```

## GodsEye: Context JSON Shape Sent

```json
{
  "ticker": "GODSEYE",
  "company": {
    "long_name": "GodsEye Market Monitor",
    "sector": "Macro Overview",
    "industry": "Multi-asset",
    "summary": "Aggregate read on equities, futures, rates, commodities, and volatility."
  },
  "market_metrics": ["<BENCHMARK_SERIES_WITH_1D_7D_30D_CHANGES...>"],
  "market_health": {
    "breadth": {
      "up": "<COUNT>",
      "down": "<COUNT>",
      "flat": "<COUNT>"
    },
    "avg_index_change_1d": "<FLOAT_OR_NULL>",
    "vix": "<VIX_METRIC_OBJECT_OR_NULL>",
    "treasury_10y": "<TNX_METRIC_OBJECT_OR_NULL>"
  },
  "market_notes": {
    "missing_series": ["<MISSING_TICKERS...>"]
  },
  "news": ["<MACRO_HEADLINES...>"],
  "news_source": "<PROVIDERS_USED>",
  "quick_facts": {
    "<LABEL>": "<1d|7d|30d|last summary>"
  },
  "quick_fact_rows": [
    {
      "number": "<4.x>",
      "label": "<QUICK_FACT_LABEL>",
      "value": "<QUICK_FACT_VALUE>"
    }
  ],
  "search_results": {
    "newsapi": ["<QUERY_RESULTS...>"],
    "google_custom_search": ["<QUERY_RESULTS...>"]
  },
  "prompt_notes": {
    "sections": ["<SECTION_NOTES_FROM_YAML>"],
    "bullet_instructions": ["<BULLET_INSTRUCTIONS_FROM_YAML>"]
  },
  "data_sources": ["<SOURCE_SUMMARY_LINES...>"],
  "price_data_source": "yfinance",
  "price_snapshot": {},
  "buy_sell_levels": {},
  "volume_assessment": {},
  "volatility_assessment": {},
  "massive_technicals": {},
  "market_prediction_window_hours": 24
}
```

## YAML Sources Used To Build These Prompts

- `config/stock-expert_prompt.txt`
- `config/godseye_prompt.txt`
- Prompt assembly logic: `src/gostonks.py:2828`
