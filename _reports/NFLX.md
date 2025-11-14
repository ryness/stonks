---
layout: default
title: "NFLX Stock Report"
ticker: "NFLX"
date: 2025-11-14
generated_at: 2025-11-14T17:40:51.145088+00:00
runtime_seconds: 72.48
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-14T17:40:51.145088+00:00">2025-11-14 17:40 UTC</time> (runtime 1m 12s)
  
  ![NetFlix Inc logo](https://ryness.github.io/stonks/assets/logos/NFLX.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — history shows 5yr near-peak but 3mo near-bottom and 1yr middle; macro froth visibility is limited and price sits above 7d support 1085.13 but below the 20-DMA/EMA (close 1118.81 vs 1124.46/1162.11) with resistance at 1167.33
  
  ## 1. The Biz
  
  1.1. **Activities:** Netflix runs a global subscription streaming service focused on on-demand TV series, films, and documentaries. It added ad-supported plans in 2022, creating an advertising revenue stream alongside subscriptions. The company serves over 300 million subscribers worldwide.
  
  1.2. **Profitable?:** Yes — it is profitable with ~24% profit margin, consistent positive net income, and strong free cash flow.
  
  1.3. **Customer & Markets:** Primary customers are consumers streaming television entertainment and advertisers using its ad-supported tier. Netflix operates in the U.S. and across international markets, reaching most of the world outside China and serving 300M+ subscribers.
  
  1.4. **Competition:** Competitors include Disney, Amazon, Alphabet/YouTube, Apple, Warner Bros. Discovery, Comcast, Roku, and Meta. Netflix ranks as the leader by subscriber base in the U.S. and collectively internationally.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** up — price held above 7d support 1085.13 and tested 1167.33 resistance with an uptrend label
  
  2.2. **7d Buy/Sell Points?:** Buy levels were near 1085.13–1073.37; sell levels were near 1167.33.
  
  2.3.1. **7d Volume:** low
  
  2.3.2. **7d Volatility:** med
  
  ## 3. Longterm
  
  3.1. **Stability?:** Netflix is a large, established streaming leader with over 300 million subscribers and global reach outside China. Financials show stability with positive net income totaling $10.43B across recent periods, 17.2% revenue growth, and $23.36B in free cash flow. Its recurring subscription model is augmented by advertising since 2022. These metrics indicate a durable, cash-generative institution rather than a fly-by-night operator.
  
  3.2. **Innovating?:** It is innovating and growing, adding ad-supported plans in 2022 and posting 17.2% revenue growth. Recent reporting also highlights strong ad engagement (ads reaching 190 million viewers in October).
  
  ## 4. Context
  
  4.1. **News:** Recent headlines focus on a 10-for-1 stock split (with pieces advocating buying before the Nov. 17 split) and continued global growth and ad-tier momentum. Yahoo reported ads reaching 190 million viewers in October, underscoring advertising expansion. Competitor developments (Paramount Skydance’s $3B plan and Disney’s Q4 2025 preview) frame a competitive backdrop. Quick facts indicate “Buy the rumor? no” and “Sell the news? no,” suggesting limited classic rumor/news trading effects.
  
  4.2. **Tarrifs:** Proposed 100% tariffs on foreign-made films pressured media stocks and were cited as potential headwinds to Netflix, with reports flagging possible EPS and cost impacts if enacted. These tariff risks therefore represent a negative overhang for the stock.
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$10.43B</td></tr>
  <tr><td>Price</td><td>1118.81</td></tr>
  <tr><td>7d Resistance</td><td>1167.33</td></tr>
  <tr><td>7d Support</td><td>1085.13</td></tr>
  <tr><td>30d Resistance</td><td>1248.60</td></tr>
  <tr><td>30d Support</td><td>1073.37</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>up</td></tr>
  <tr><td>3mo</td><td>near-bottom</td></tr>
  <tr><td>1yr</td><td>middle</td></tr>
  <tr><td>5yr</td><td>near-peak</td></tr>
  <tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>NewsAPI: business model, profit outlook, market expansion, competitive landscape, tariff, latest news, tariffs</li>
  <li>The Guardian: rumor</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for NFLX...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting NFLX prices from massive.com... (https://api.massive.com/v2/aggs/ticker/NFLX/range/1/day/2020-10-16/2025-11-14?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/NFLX/2025-11-14?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/NFLX/2025-11-14?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/NFLX/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/NFLX/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/NFLX?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/NFLX?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/NFLX?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/NFLX?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/NFLX?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/NFLX?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/NFLX.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/NFLX?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/NFLX?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 10 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=NFLX&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=NFLX&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=NFLX&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=NFLX&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; NFLX core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NFLX product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NFLX business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 3 result(s)
    google_custom_search search -&gt; NFLX profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NFLX earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NFLX profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; NFLX target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NFLX market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NFLX market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; NFLX competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NFLX market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NFLX competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 1 result(s)
    google_custom_search search -&gt; NFLX rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NFLX tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NFLX rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=NFLX+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=NFLX+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; NFLX tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; NFLX latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; NFLX latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NFLX tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; NFLX tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+tariff+impact&amp;num=5
      google_custom_search: 5 result(s)
  Synthesizing narrative from OpenAI response...
  Preparing OpenAI request...
  Dispatching bullets to OpenAI:
    - 0.1 Long Entry? [Lead with &#x27;yes&#x27;, &#x27;no&#x27;, or &#x27;maybe&#x27;, then cite specific historical positioning, macro froth cues (or lack thereof), and placement relative to moving averages or support/resistance.]
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

**Generated:** <time class="js-local-time" datetime="2025-11-14T17:40:51.145088+00:00">2025-11-14 17:40 UTC</time> (runtime 1m 12s)

![NetFlix Inc logo](https://ryness.github.io/stonks/assets/logos/NFLX.svg)


## 0. Entry Radar

0.1. **Long Entry?:** maybe — history shows 5yr near-peak but 3mo near-bottom and 1yr middle; macro froth visibility is limited and price sits above 7d support 1085.13 but below the 20-DMA/EMA (close 1118.81 vs 1124.46/1162.11) with resistance at 1167.33

## 1. The Biz

1.1. **Activities:** Netflix runs a global subscription streaming service focused on on-demand TV series, films, and documentaries. It added ad-supported plans in 2022, creating an advertising revenue stream alongside subscriptions. The company serves over 300 million subscribers worldwide.

1.2. **Profitable?:** Yes — it is profitable with ~24% profit margin, consistent positive net income, and strong free cash flow.

1.3. **Customer & Markets:** Primary customers are consumers streaming television entertainment and advertisers using its ad-supported tier. Netflix operates in the U.S. and across international markets, reaching most of the world outside China and serving 300M+ subscribers.

1.4. **Competition:** Competitors include Disney, Amazon, Alphabet/YouTube, Apple, Warner Bros. Discovery, Comcast, Roku, and Meta. Netflix ranks as the leader by subscriber base in the U.S. and collectively internationally.

## 2. Recent

2.1. **7d Trend?:** up — price held above 7d support 1085.13 and tested 1167.33 resistance with an uptrend label

2.2. **7d Buy/Sell Points?:** Buy levels were near 1085.13–1073.37; sell levels were near 1167.33.

2.3.1. **7d Volume:** low

2.3.2. **7d Volatility:** med

## 3. Longterm

3.1. **Stability?:** Netflix is a large, established streaming leader with over 300 million subscribers and global reach outside China. Financials show stability with positive net income totaling $10.43B across recent periods, 17.2% revenue growth, and $23.36B in free cash flow. Its recurring subscription model is augmented by advertising since 2022. These metrics indicate a durable, cash-generative institution rather than a fly-by-night operator.

3.2. **Innovating?:** It is innovating and growing, adding ad-supported plans in 2022 and posting 17.2% revenue growth. Recent reporting also highlights strong ad engagement (ads reaching 190 million viewers in October).

## 4. Context

4.1. **News:** Recent headlines focus on a 10-for-1 stock split (with pieces advocating buying before the Nov. 17 split) and continued global growth and ad-tier momentum. Yahoo reported ads reaching 190 million viewers in October, underscoring advertising expansion. Competitor developments (Paramount Skydance’s $3B plan and Disney’s Q4 2025 preview) frame a competitive backdrop. Quick facts indicate “Buy the rumor? no” and “Sell the news? no,” suggesting limited classic rumor/news trading effects.

4.2. **Tarrifs:** Proposed 100% tariffs on foreign-made films pressured media stocks and were cited as potential headwinds to Netflix, with reports flagging possible EPS and cost impacts if enacted. These tariff risks therefore represent a negative overhang for the stock.

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$10.43B</td></tr>
<tr><td>Price</td><td>1118.81</td></tr>
<tr><td>7d Resistance</td><td>1167.33</td></tr>
<tr><td>7d Support</td><td>1085.13</td></tr>
<tr><td>30d Resistance</td><td>1248.60</td></tr>
<tr><td>30d Support</td><td>1073.37</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>up</td></tr>
<tr><td>3mo</td><td>near-bottom</td></tr>
<tr><td>1yr</td><td>middle</td></tr>
<tr><td>5yr</td><td>near-peak</td></tr>
<tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>NewsAPI: business model, profit outlook, market expansion, competitive landscape, tariff, latest news, tariffs</li>
<li>The Guardian: rumor</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for NFLX...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting NFLX prices from massive.com... (https://api.massive.com/v2/aggs/ticker/NFLX/range/1/day/2020-10-16/2025-11-14?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/NFLX/2025-11-14?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/NFLX/2025-11-14?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/NFLX/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/NFLX/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/NFLX?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/NFLX?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/NFLX?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/NFLX?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/NFLX?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/NFLX?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/NFLX?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/NFLX.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/NFLX?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/NFLX?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 10 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=NFLX&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=NFLX&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=NFLX&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=NFLX&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; NFLX core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NFLX product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NFLX business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 3 result(s)
  google_custom_search search -&gt; NFLX profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NFLX earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NFLX profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; NFLX target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NFLX market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NFLX market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; NFLX competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NFLX market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NFLX competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 1 result(s)
  google_custom_search search -&gt; NFLX rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NFLX tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NFLX rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=NFLX+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=NFLX+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; NFLX tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; NFLX latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; NFLX latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NFLX tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NFLX+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; NFLX tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NFLX+tariff+impact&amp;num=5
    google_custom_search: 5 result(s)
Synthesizing narrative from OpenAI response...
Preparing OpenAI request...
Dispatching bullets to OpenAI:
  - 0.1 Long Entry? [Lead with &#x27;yes&#x27;, &#x27;no&#x27;, or &#x27;maybe&#x27;, then cite specific historical positioning, macro froth cues (or lack thereof), and placement relative to moving averages or support/resistance.]
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
