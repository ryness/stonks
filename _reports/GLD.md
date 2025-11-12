---
layout: default
title: "GLD Stock Report"
ticker: "GLD"
date: 2025-11-12
generated_at: 2025-11-12T20:25:07.016704+00:00
runtime_seconds: 116.97
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-12T20:25:07.016704+00:00">2025-11-12 20:25 UTC</time> (runtime 1m 57s)
  
  ## 1. The Biz
  
  1.1. **Activities:** SPDR Gold Trust holds physical gold bars and issues/redeems Baskets in exchange for deposits of gold so its Shares reflect the price of gold bullion, less expenses. Its core product is SPDR Gold Shares, providing investors a cost-effective, physically backed exposure to gold.
  
  1.2. **Profitable?:** No — it is not a traditional profit-seeking operating company; its objective is to mirror gold bullion’s price less expenses, and no profitability metrics are provided.
  
  1.3. **Customer & Markets:** Primary customers are investors seeking cost-effective exposure to gold prices. The market is the gold bullion market via exchange-traded Shares, with demand driven by investor allocation to gold.
  
  1.4. **Competition:** It competes with other physically backed gold funds such as iShares Gold Trust (IAU), SPDR Gold MiniShares (GLDM), and Perth Mint Physical Gold ETF (AAAU). It is positioned alongside these major gold-backed products.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** up — price advanced from support near 361.39 toward 387.46 resistance and sits above the 20-day moving average.
  
  2.2. **7d Buy/Sell Points?:** Buying near 361.39 (support/suggested buy zone) looked favorable, while selling into 370.84 and up toward 387.46 resistance offered attractive exits.
  
  2.3.1. **7d Volume:** med
  
  2.3.2. **7d Volatility:** low
  
  ## 3. Longterm
  
  3.1. **Stability?:** This is a physically backed trust that holds gold bars and issues/redeems Baskets, indicating a straightforward, established structure rather than a fly-by-night operation. Its objective is to track gold prices less expenses, implying a balance sheet dominated by bullion holdings. Operational complexity appears low, with stability primarily tied to movements in the underlying gold price. No leverage or cash flow details are provided in the supplied data.
  
  3.2. **Innovating?:** It is a passive vehicle designed to track gold; no specific innovation or growth initiatives are noted in the provided data.
  
  ## 4. Context
  
  4.1. **News:** Recent coverage focuses on macro drivers: PCE inflation reports and rate-cut expectations, with traders cautious ahead of data while gold and bitcoin rebounded (Benzinga). Zacks highlighted gold ETFs amid talk of gold potentially breaking higher on geopolitical tensions and possible rate cuts, and offered ETF strategies for 2H 2024. This backdrop suggests rallies can build on anticipation of favorable data, but once news lands, moves may fade, aligning with the ‘buy the rumor, sell the news’ dynamic observed in the headlines.
  
  4.2. **Tarrifs:** Headlines indicate tariff threats have supported safe-haven demand for gold, with GLD rising as tariffs were discussed (etf.com). Overall, tariff-related uncertainty has been a positive catalyst for GLD in the cited coverage.
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>unknown</td></tr>
  <tr><td>Price</td><td>385.93</td></tr>
  <tr><td>7d Resistance</td><td>387.46</td></tr>
  <tr><td>7d Support</td><td>361.39</td></tr>
  <tr><td>30d Resistance</td><td>403.30</td></tr>
  <tr><td>30d Support</td><td>351.40</td></tr>
  <tr><td>Buy the dip?</td><td>no</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>yes</td></tr>
  <tr><td>7d Trend:</td><td>up</td></tr>
  <tr><td>3mo</td><td>near-peak</td></tr>
  <tr><td>1yr</td><td>near-peak</td></tr>
  <tr><td>5yr</td><td>near-peak</td></tr>
  <tr><td>Overbought/Sold?</td><td>overbought</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>NewsAPI: business model, profit outlook, market expansion, tariff, latest news, tariffs</li>
  <li>The Guardian: competitive landscape, rumor</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for GLD...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting GLD prices from massive.com... (https://api.massive.com/v2/aggs/ticker/GLD/range/1/day/2020-10-14/2025-11-12?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/GLD/2025-11-12?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/GLD/2025-11-12?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/GLD?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/GLD?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive related companies: GET https://api.massive.com/v1/related-companies/GLD?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/GLD?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 0 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; GLD core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 3 result(s)
    google_custom_search search -&gt; GLD profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 3 result(s)
    google_custom_search search -&gt; GLD target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 1 result(s)
    google_custom_search search -&gt; GLD competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=GLD+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=GLD+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; GLD rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=GLD+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=GLD+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; GLD tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; GLD latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 2 result(s)
    google_custom_search search -&gt; GLD latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; GLD tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariff+impact&amp;num=5
      google_custom_search: 5 result(s)
  Synthesizing narrative from OpenAI response...
  Preparing OpenAI request...
  Dispatching bullets to OpenAI:
    - 1.1 Activities
    - 1.2 Profitable?
    - 1.3 Customer &amp; Markets
    - 1.4 Competition
    - 2.1 7d Trend?
    - 2.2 7d Buy/Sell Points?
    - 2.3.1 7d Volume
    - 2.3.2 7d Volatility
    - 3.1 Stability?
    - 3.2 Innovating?
    - 4.1 News
    - 4.2 Tarrifs
  Asking OpenAI for analysis...
  Received response from OpenAI.
  </code></pre>
  </details>
---

**Generated:** <time class="js-local-time" datetime="2025-11-12T20:25:07.016704+00:00">2025-11-12 20:25 UTC</time> (runtime 1m 57s)

## 1. The Biz

1.1. **Activities:** SPDR Gold Trust holds physical gold bars and issues/redeems Baskets in exchange for deposits of gold so its Shares reflect the price of gold bullion, less expenses. Its core product is SPDR Gold Shares, providing investors a cost-effective, physically backed exposure to gold.

1.2. **Profitable?:** No — it is not a traditional profit-seeking operating company; its objective is to mirror gold bullion’s price less expenses, and no profitability metrics are provided.

1.3. **Customer & Markets:** Primary customers are investors seeking cost-effective exposure to gold prices. The market is the gold bullion market via exchange-traded Shares, with demand driven by investor allocation to gold.

1.4. **Competition:** It competes with other physically backed gold funds such as iShares Gold Trust (IAU), SPDR Gold MiniShares (GLDM), and Perth Mint Physical Gold ETF (AAAU). It is positioned alongside these major gold-backed products.

## 2. Recent

2.1. **7d Trend?:** up — price advanced from support near 361.39 toward 387.46 resistance and sits above the 20-day moving average.

2.2. **7d Buy/Sell Points?:** Buying near 361.39 (support/suggested buy zone) looked favorable, while selling into 370.84 and up toward 387.46 resistance offered attractive exits.

2.3.1. **7d Volume:** med

2.3.2. **7d Volatility:** low

## 3. Longterm

3.1. **Stability?:** This is a physically backed trust that holds gold bars and issues/redeems Baskets, indicating a straightforward, established structure rather than a fly-by-night operation. Its objective is to track gold prices less expenses, implying a balance sheet dominated by bullion holdings. Operational complexity appears low, with stability primarily tied to movements in the underlying gold price. No leverage or cash flow details are provided in the supplied data.

3.2. **Innovating?:** It is a passive vehicle designed to track gold; no specific innovation or growth initiatives are noted in the provided data.

## 4. Context

4.1. **News:** Recent coverage focuses on macro drivers: PCE inflation reports and rate-cut expectations, with traders cautious ahead of data while gold and bitcoin rebounded (Benzinga). Zacks highlighted gold ETFs amid talk of gold potentially breaking higher on geopolitical tensions and possible rate cuts, and offered ETF strategies for 2H 2024. This backdrop suggests rallies can build on anticipation of favorable data, but once news lands, moves may fade, aligning with the ‘buy the rumor, sell the news’ dynamic observed in the headlines.

4.2. **Tarrifs:** Headlines indicate tariff threats have supported safe-haven demand for gold, with GLD rising as tariffs were discussed (etf.com). Overall, tariff-related uncertainty has been a positive catalyst for GLD in the cited coverage.

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>unknown</td></tr>
<tr><td>Price</td><td>385.93</td></tr>
<tr><td>7d Resistance</td><td>387.46</td></tr>
<tr><td>7d Support</td><td>361.39</td></tr>
<tr><td>30d Resistance</td><td>403.30</td></tr>
<tr><td>30d Support</td><td>351.40</td></tr>
<tr><td>Buy the dip?</td><td>no</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>yes</td></tr>
<tr><td>7d Trend:</td><td>up</td></tr>
<tr><td>3mo</td><td>near-peak</td></tr>
<tr><td>1yr</td><td>near-peak</td></tr>
<tr><td>5yr</td><td>near-peak</td></tr>
<tr><td>Overbought/Sold?</td><td>overbought</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>NewsAPI: business model, profit outlook, market expansion, tariff, latest news, tariffs</li>
<li>The Guardian: competitive landscape, rumor</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for GLD...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting GLD prices from massive.com... (https://api.massive.com/v2/aggs/ticker/GLD/range/1/day/2020-10-14/2025-11-12?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/GLD/2025-11-12?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/GLD/2025-11-12?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/GLD?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/GLD?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive related companies: GET https://api.massive.com/v1/related-companies/GLD?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/GLD?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 0 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; GLD core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 3 result(s)
  google_custom_search search -&gt; GLD profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 3 result(s)
  google_custom_search search -&gt; GLD target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 1 result(s)
  google_custom_search search -&gt; GLD competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=GLD+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=GLD+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; GLD rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=GLD+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=GLD+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; GLD tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; GLD latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 2 result(s)
  google_custom_search search -&gt; GLD latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; GLD tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariff+impact&amp;num=5
    google_custom_search: 5 result(s)
Synthesizing narrative from OpenAI response...
Preparing OpenAI request...
Dispatching bullets to OpenAI:
  - 1.1 Activities
  - 1.2 Profitable?
  - 1.3 Customer &amp; Markets
  - 1.4 Competition
  - 2.1 7d Trend?
  - 2.2 7d Buy/Sell Points?
  - 2.3.1 7d Volume
  - 2.3.2 7d Volatility
  - 3.1 Stability?
  - 3.2 Innovating?
  - 4.1 News
  - 4.2 Tarrifs
Asking OpenAI for analysis...
Received response from OpenAI.
</code></pre>
</details>
