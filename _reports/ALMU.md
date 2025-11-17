---
layout: default
title: "ALMU Stock Report"
ticker: "ALMU"
date: 2025-11-17
generated_at: 2025-11-17T15:24:52.199129+00:00
runtime_seconds: 141.55
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-17T15:24:52.199129+00:00">2025-11-17 15:24 UTC</time> (runtime 2m 22s)
  
  ![Aeluma, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/ALMU.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — 3mo position is at the bottom with 1yr in the middle and overbought/sold in the middle; macro froth visibility is limited and price sits near 12.97 support while below the 20-DMA (~15.19), SMA/EMA (~16.4–16.6) and 15.80 resistance.
  
  ## 1. The Biz
  
  1.1. **Activities:** Aeluma is a semiconductor company specializing in optoelectronic sensors and communications devices. It develops high-performance compound semiconductor devices on large-diameter substrates for sensing and communications in mobile devices and vehicles. Its applications span mobile, automotive, AI, defense and aerospace, communications, AR/VR, and quantum computing.
  
  1.2. **Profitable?:** no — it is currently unprofitable (profit margin -67.97% and negative operating/free cash flow) despite strong revenue growth.
  
  1.3. **Customer & Markets:** Primary customers include government and R&D contract partners and companies across mobile, automotive, defense and aerospace, communications, and AR/VR sectors. Based in the United States, it markets sensor and communications technology for applications also touching AI and quantum computing.
  
  1.4. **Competition:** Competitors include NVIDIA, AMD, Intel, and Qualcomm; Aeluma is a smaller, specialized sensor/optoelectronics player relative to these large incumbents.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** down — slid from a local high near 15.80 toward 12.97 support with the close (~13.34) below the 20-DMA (~15.19).
  
  2.2. **7d Buy/Sell Points?:** Buy near 12.97 support/suggested buy zone; sell or trim into 15.80 resistance/suggested sell zone.
  
  2.3.1. **7d Volume:** low
  
  2.3.2. **7d Volatility:** high
  
  ## 3. Longterm
  
  3.1. **Stability?:** Aeluma is an emerging semiconductor company rather than a long-established giant. It strengthened liquidity via an oversubscribed $25.4M public offering, bringing cash to $39.2M. However, it remains unprofitable with a -67.97% profit margin and negative operating and free cash flow. Trading shows high volatility (ATR ~8.3% of price) and low volume, though recent NASDAQ uplisting and government contracts were noted in coverage.
  
  3.2. **Innovating?:** It is innovating and growing, evidenced by a 366.7% YoY revenue jump in fiscal Q4 and the acquisition of capital equipment to accelerate wafer-scale testing and manufacturing readiness.
  
  ## 4. Context
  
  4.1. **News:** Recent headlines show momentum: fiscal Q4 revenue up 366.7% YoY driven by R&D contracts and significant government wins. The company closed an oversubscribed $25.4M offering at $13.00, lifting cash to $39.2M to fund commercialization. It also acquired major capital equipment to enhance prototyping and wafer-scale testing for its go-to-market strategy. With quick facts indicating 'Buy the rumor? no' and 'Sell the news? no', the pattern suggests steady execution rather than rumor-driven spikes or post-news selloffs.
  
  4.2. **Tarrifs:** unknown
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$-2.29M</td></tr>
  <tr><td>Price</td><td>13.34</td></tr>
  <tr><td>7d Resistance</td><td>15.80</td></tr>
  <tr><td>7d Support</td><td>12.97</td></tr>
  <tr><td>30d Resistance</td><td>22.18</td></tr>
  <tr><td>30d Support</td><td>12.97</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>down</td></tr>
  <tr><td>3mo</td><td>bottom</td></tr>
  <tr><td>1yr</td><td>middle</td></tr>
  <tr><td>5yr</td><td>middle</td></tr>
  <tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (4 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>NewsAPI: market expansion</li>
  <li>The Guardian: business model, profit outlook, competitive landscape, rumor, tariff, latest news, tariffs</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for ALMU...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting ALMU prices from massive.com... (https://api.massive.com/v2/aggs/ticker/ALMU/range/1/day/2020-10-19/2025-11-17?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/ALMU/2025-11-17?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/ALMU/2025-11-17?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/ALMU/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/ALMU/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/ALMU?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/ALMU?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/ALMU?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/ALMU?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/ALMU?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/ALMU?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/ALMU.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/ALMU?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/ALMU?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 0 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=ALMU&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=ALMU&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=ALMU&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=ALMU&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 4 articles.
    massive.com returned 4 headlines
  Running supplementary searches...
    google_custom_search search -&gt; ALMU core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; ALMU product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; ALMU business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=ALMU+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=ALMU+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; ALMU profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; ALMU earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; ALMU profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=ALMU+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=ALMU+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; ALMU target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; ALMU market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; ALMU market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 2 result(s)
    google_custom_search search -&gt; ALMU competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; ALMU market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; ALMU competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=ALMU+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=ALMU+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; ALMU rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; ALMU tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; ALMU rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=ALMU+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=ALMU+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; ALMU tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=ALMU+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=ALMU+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; ALMU latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=ALMU+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=ALMU+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; ALMU latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; ALMU tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=ALMU+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=ALMU+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; ALMU tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-17T15:24:52.199129+00:00">2025-11-17 15:24 UTC</time> (runtime 2m 22s)

![Aeluma, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/ALMU.svg)


## 0. Entry Radar

0.1. **Long Entry?:** maybe — 3mo position is at the bottom with 1yr in the middle and overbought/sold in the middle; macro froth visibility is limited and price sits near 12.97 support while below the 20-DMA (~15.19), SMA/EMA (~16.4–16.6) and 15.80 resistance.

## 1. The Biz

1.1. **Activities:** Aeluma is a semiconductor company specializing in optoelectronic sensors and communications devices. It develops high-performance compound semiconductor devices on large-diameter substrates for sensing and communications in mobile devices and vehicles. Its applications span mobile, automotive, AI, defense and aerospace, communications, AR/VR, and quantum computing.

1.2. **Profitable?:** no — it is currently unprofitable (profit margin -67.97% and negative operating/free cash flow) despite strong revenue growth.

1.3. **Customer & Markets:** Primary customers include government and R&D contract partners and companies across mobile, automotive, defense and aerospace, communications, and AR/VR sectors. Based in the United States, it markets sensor and communications technology for applications also touching AI and quantum computing.

1.4. **Competition:** Competitors include NVIDIA, AMD, Intel, and Qualcomm; Aeluma is a smaller, specialized sensor/optoelectronics player relative to these large incumbents.

## 2. Recent

2.1. **7d Trend?:** down — slid from a local high near 15.80 toward 12.97 support with the close (~13.34) below the 20-DMA (~15.19).

2.2. **7d Buy/Sell Points?:** Buy near 12.97 support/suggested buy zone; sell or trim into 15.80 resistance/suggested sell zone.

2.3.1. **7d Volume:** low

2.3.2. **7d Volatility:** high

## 3. Longterm

3.1. **Stability?:** Aeluma is an emerging semiconductor company rather than a long-established giant. It strengthened liquidity via an oversubscribed $25.4M public offering, bringing cash to $39.2M. However, it remains unprofitable with a -67.97% profit margin and negative operating and free cash flow. Trading shows high volatility (ATR ~8.3% of price) and low volume, though recent NASDAQ uplisting and government contracts were noted in coverage.

3.2. **Innovating?:** It is innovating and growing, evidenced by a 366.7% YoY revenue jump in fiscal Q4 and the acquisition of capital equipment to accelerate wafer-scale testing and manufacturing readiness.

## 4. Context

4.1. **News:** Recent headlines show momentum: fiscal Q4 revenue up 366.7% YoY driven by R&D contracts and significant government wins. The company closed an oversubscribed $25.4M offering at $13.00, lifting cash to $39.2M to fund commercialization. It also acquired major capital equipment to enhance prototyping and wafer-scale testing for its go-to-market strategy. With quick facts indicating 'Buy the rumor? no' and 'Sell the news? no', the pattern suggests steady execution rather than rumor-driven spikes or post-news selloffs.

4.2. **Tarrifs:** unknown

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$-2.29M</td></tr>
<tr><td>Price</td><td>13.34</td></tr>
<tr><td>7d Resistance</td><td>15.80</td></tr>
<tr><td>7d Support</td><td>12.97</td></tr>
<tr><td>30d Resistance</td><td>22.18</td></tr>
<tr><td>30d Support</td><td>12.97</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>down</td></tr>
<tr><td>3mo</td><td>bottom</td></tr>
<tr><td>1yr</td><td>middle</td></tr>
<tr><td>5yr</td><td>middle</td></tr>
<tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (4 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>NewsAPI: market expansion</li>
<li>The Guardian: business model, profit outlook, competitive landscape, rumor, tariff, latest news, tariffs</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for ALMU...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting ALMU prices from massive.com... (https://api.massive.com/v2/aggs/ticker/ALMU/range/1/day/2020-10-19/2025-11-17?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/ALMU/2025-11-17?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/ALMU/2025-11-17?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/ALMU/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/ALMU/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/ALMU?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/ALMU?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/ALMU?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/ALMU?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/ALMU?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/ALMU?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/ALMU?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/ALMU.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/ALMU?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/ALMU?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 0 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=ALMU&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=ALMU&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=ALMU&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=ALMU&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 4 articles.
  massive.com returned 4 headlines
Running supplementary searches...
  google_custom_search search -&gt; ALMU core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; ALMU product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; ALMU business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=ALMU+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=ALMU+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; ALMU profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; ALMU earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; ALMU profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=ALMU+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=ALMU+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; ALMU target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; ALMU market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; ALMU market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 2 result(s)
  google_custom_search search -&gt; ALMU competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; ALMU market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; ALMU competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=ALMU+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=ALMU+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; ALMU rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; ALMU tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; ALMU rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=ALMU+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=ALMU+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; ALMU tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=ALMU+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=ALMU+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; ALMU latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=ALMU+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=ALMU+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; ALMU latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; ALMU tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=ALMU+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=ALMU+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=ALMU+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; ALMU tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=ALMU+tariff+impact&amp;num=5
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
