---
layout: default
title: "PFE Stock Report"
ticker: "PFE"
date: 2025-11-14
generated_at: 2025-11-14T22:45:32.035207+00:00
runtime_seconds: 108.73
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-14T22:45:32.035207+00:00">2025-11-14 22:45 UTC</time> (runtime 1m 49s)
  
  ![Pfizer Inc. logo](https://ryness.github.io/stonks/assets/logos/PFE.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — 5yr positioning is near-bottom with a 7d uptrend and overbought/sold reading in the middle; macro froth cues are limited in the provided data, and price 25.06 is above the 20DMA 24.48 and between support 23.91 and resistance 26.48
  
  ## 1. The Biz
  
  1.1. **Activities:** Pfizer is one of the world’s largest pharmaceutical companies focused on prescription drugs and vaccines. Key products include the pneumococcal vaccine Prevnar 13, cancer therapy Ibrance, and cardiovascular treatment Eliquis. It operates across global markets with a significant international footprint.
  
  1.2. **Profitable?:** yes — it shows a 15.7% profit margin with positive recent net income and strong free cash flow.
  
  1.3. **Customer & Markets:** Pfizer sells prescription drugs and vaccines globally, with international sales representing 40% of total sales. Emerging markets are a major contributor. Primary customer types are not specified in the provided data.
  
  1.4. **Competition:** Primary competitors include large drug makers such as MRNA, MRK, JNJ, NVAX, LLY, ABBV, BMY, AMGN, GILD, and VTRS; Pfizer ranks among the world’s largest pharmaceutical firms.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** up — price has risen off 7d support 23.91 toward resistance 26.48 and sits above the 20DMA 24.48.
  
  2.2. **7d Buy/Sell Points?:** Buy dips near 23.91; sell or trim into strength around 26.48.
  
  2.3.1. **7d Volume:** med
  
  2.3.2. **7d Volatility:** med
  
  ## 3. Longterm
  
  3.1. **Stability?:** Pfizer appears to be a stable, mature institution, described as one of the world’s largest pharmaceutical firms. It generates substantial operating cash flow and free cash flow, and maintains positive profitability. Global diversification is significant, with 40% of sales from international markets and notable exposure to emerging markets. While revenue and earnings growth are currently negative, the company’s scale and cash generation support overall stability.
  
  3.2. **Innovating?:** It is actively reshaping and investing in its portfolio, highlighted by a proposed acquisition of Metsera and an exit from its BioNTech stake. Despite negative near-term growth metrics, these actions indicate ongoing innovation and strategic repositioning.
  
  ## 4. Context
  
  4.1. **News:** Recent headlines note Pfizer’s plan to sell its remaining BioNTech stake via an overnight block trade (~$508M), signaling portfolio reallocation. Pfizer is the proposed buyer of Metsera at $47.50 per share, though a law firm is investigating the deal’s fairness, adding some uncertainty. Novo Nordisk’s price cut for Wegovy in India after losing Metsera to Pfizer underscores competitive dynamics in obesity treatments. An Investing.com piece frames Pfizer as a discounted stock heading into 2026. Given quick facts showing ‘Buy the rumor? no’ and ‘Sell the news? no,’ these events may not fit a classic rumor/news trade setup.
  
  4.2. **Tarrifs:** unknown
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$9.83B</td></tr>
  <tr><td>Price</td><td>25.06</td></tr>
  <tr><td>7d Resistance</td><td>26.48</td></tr>
  <tr><td>7d Support</td><td>23.91</td></tr>
  <tr><td>30d Resistance</td><td>26.89</td></tr>
  <tr><td>30d Support</td><td>23.73</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>up</td></tr>
  <tr><td>3mo</td><td>middle</td></tr>
  <tr><td>1yr</td><td>middle</td></tr>
  <tr><td>5yr</td><td>near-bottom</td></tr>
  <tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>The Guardian: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact, business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for PFE...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting PFE prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PFE/range/1/day/2020-10-16/2025-11-14?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/PFE/2025-11-14?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/PFE/2025-11-14?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/PFE/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/PFE/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/PFE?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/PFE?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/PFE?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/PFE?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/PFE?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/PFE?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/PFE.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/PFE?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/PFE?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 10 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=PFE&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=PFE&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=PFE&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=PFE&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; PFE core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+core+business&amp;num=5
  Google Custom Search failed for &#x27;PFE core business&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+core+business&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE core business&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+core+business&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE core business&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+core+business&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+product+portfolio&amp;num=5
  Google Custom Search failed for &#x27;PFE product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+product+portfolio&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+product+portfolio&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE product portfolio&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+product+portfolio&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE business model&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE business model&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+profitability&amp;num=5
  Google Custom Search failed for &#x27;PFE profitability&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+profitability&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE profitability&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+profitability&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE profitability&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+profitability&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+earnings+trend&amp;num=5
  Google Custom Search failed for &#x27;PFE earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+earnings+trend&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+earnings+trend&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE earnings trend&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+earnings+trend&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE profit outlook&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE profit outlook&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+target+customers&amp;num=5
  Google Custom Search failed for &#x27;PFE target customers&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+target+customers&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE target customers&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+target+customers&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE target customers&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+target+customers&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+segments&amp;num=5
  Google Custom Search failed for &#x27;PFE market segments&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+segments&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE market segments&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+market+segments&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE market segments&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+market+segments&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE market expansion&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+competitors&amp;num=5
  Google Custom Search failed for &#x27;PFE competitors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+competitors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE competitors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+competitors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE competitors&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+competitors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+share&amp;num=5
  Google Custom Search failed for &#x27;PFE market share&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+share&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE market share&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+market+share&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE market share&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+market+share&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE competitive landscape&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+rumors&amp;num=5
  Google Custom Search failed for &#x27;PFE rumors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+rumors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE rumors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+rumors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE rumors&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+rumors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariffs+news&amp;num=5
  Google Custom Search failed for &#x27;PFE tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariffs+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariffs+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE tariffs news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariffs+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE tariff&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE latest news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+latest+rumor&amp;num=5
  Google Custom Search failed for &#x27;PFE latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+latest+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+latest+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE latest rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+latest+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; PFE tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE tariffs&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariff+impact&amp;num=5
  Google Custom Search failed for &#x27;PFE tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariff+impact&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PFE tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariff+impact&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;PFE tariff impact&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariff+impact&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
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

**Generated:** <time class="js-local-time" datetime="2025-11-14T22:45:32.035207+00:00">2025-11-14 22:45 UTC</time> (runtime 1m 49s)

![Pfizer Inc. logo](https://ryness.github.io/stonks/assets/logos/PFE.svg)


## 0. Entry Radar

0.1. **Long Entry?:** maybe — 5yr positioning is near-bottom with a 7d uptrend and overbought/sold reading in the middle; macro froth cues are limited in the provided data, and price 25.06 is above the 20DMA 24.48 and between support 23.91 and resistance 26.48

## 1. The Biz

1.1. **Activities:** Pfizer is one of the world’s largest pharmaceutical companies focused on prescription drugs and vaccines. Key products include the pneumococcal vaccine Prevnar 13, cancer therapy Ibrance, and cardiovascular treatment Eliquis. It operates across global markets with a significant international footprint.

1.2. **Profitable?:** yes — it shows a 15.7% profit margin with positive recent net income and strong free cash flow.

1.3. **Customer & Markets:** Pfizer sells prescription drugs and vaccines globally, with international sales representing 40% of total sales. Emerging markets are a major contributor. Primary customer types are not specified in the provided data.

1.4. **Competition:** Primary competitors include large drug makers such as MRNA, MRK, JNJ, NVAX, LLY, ABBV, BMY, AMGN, GILD, and VTRS; Pfizer ranks among the world’s largest pharmaceutical firms.

## 2. Recent

2.1. **7d Trend?:** up — price has risen off 7d support 23.91 toward resistance 26.48 and sits above the 20DMA 24.48.

2.2. **7d Buy/Sell Points?:** Buy dips near 23.91; sell or trim into strength around 26.48.

2.3.1. **7d Volume:** med

2.3.2. **7d Volatility:** med

## 3. Longterm

3.1. **Stability?:** Pfizer appears to be a stable, mature institution, described as one of the world’s largest pharmaceutical firms. It generates substantial operating cash flow and free cash flow, and maintains positive profitability. Global diversification is significant, with 40% of sales from international markets and notable exposure to emerging markets. While revenue and earnings growth are currently negative, the company’s scale and cash generation support overall stability.

3.2. **Innovating?:** It is actively reshaping and investing in its portfolio, highlighted by a proposed acquisition of Metsera and an exit from its BioNTech stake. Despite negative near-term growth metrics, these actions indicate ongoing innovation and strategic repositioning.

## 4. Context

4.1. **News:** Recent headlines note Pfizer’s plan to sell its remaining BioNTech stake via an overnight block trade (~$508M), signaling portfolio reallocation. Pfizer is the proposed buyer of Metsera at $47.50 per share, though a law firm is investigating the deal’s fairness, adding some uncertainty. Novo Nordisk’s price cut for Wegovy in India after losing Metsera to Pfizer underscores competitive dynamics in obesity treatments. An Investing.com piece frames Pfizer as a discounted stock heading into 2026. Given quick facts showing ‘Buy the rumor? no’ and ‘Sell the news? no,’ these events may not fit a classic rumor/news trade setup.

4.2. **Tarrifs:** unknown

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$9.83B</td></tr>
<tr><td>Price</td><td>25.06</td></tr>
<tr><td>7d Resistance</td><td>26.48</td></tr>
<tr><td>7d Support</td><td>23.91</td></tr>
<tr><td>30d Resistance</td><td>26.89</td></tr>
<tr><td>30d Support</td><td>23.73</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>up</td></tr>
<tr><td>3mo</td><td>middle</td></tr>
<tr><td>1yr</td><td>middle</td></tr>
<tr><td>5yr</td><td>near-bottom</td></tr>
<tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>The Guardian: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact, business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for PFE...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting PFE prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PFE/range/1/day/2020-10-16/2025-11-14?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/PFE/2025-11-14?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/PFE/2025-11-14?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/PFE/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/PFE/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/PFE?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/PFE?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/PFE?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/PFE?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/PFE?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/PFE?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/PFE?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/PFE.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/PFE?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/PFE?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 10 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=PFE&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=PFE&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=PFE&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=PFE&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; PFE core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+core+business&amp;num=5
Google Custom Search failed for &#x27;PFE core business&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+core+business&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE core business&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+core+business&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE core business&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+core+business&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+product+portfolio&amp;num=5
Google Custom Search failed for &#x27;PFE product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+product+portfolio&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+product+portfolio&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE product portfolio&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+product+portfolio&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE business model&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE business model&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+profitability&amp;num=5
Google Custom Search failed for &#x27;PFE profitability&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+profitability&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE profitability&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+profitability&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE profitability&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+profitability&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+earnings+trend&amp;num=5
Google Custom Search failed for &#x27;PFE earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+earnings+trend&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+earnings+trend&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE earnings trend&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+earnings+trend&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE profit outlook&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE profit outlook&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+target+customers&amp;num=5
Google Custom Search failed for &#x27;PFE target customers&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+target+customers&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE target customers&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+target+customers&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE target customers&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+target+customers&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+segments&amp;num=5
Google Custom Search failed for &#x27;PFE market segments&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+segments&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE market segments&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+market+segments&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE market segments&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+market+segments&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE market expansion&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+competitors&amp;num=5
Google Custom Search failed for &#x27;PFE competitors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+competitors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE competitors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+competitors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE competitors&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+competitors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+share&amp;num=5
Google Custom Search failed for &#x27;PFE market share&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+share&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE market share&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+market+share&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE market share&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+market+share&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE competitive landscape&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+rumors&amp;num=5
Google Custom Search failed for &#x27;PFE rumors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+rumors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE rumors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+rumors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE rumors&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+rumors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariffs+news&amp;num=5
Google Custom Search failed for &#x27;PFE tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariffs+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariffs+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE tariffs news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariffs+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE tariff&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE latest news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+latest+rumor&amp;num=5
Google Custom Search failed for &#x27;PFE latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+latest+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+latest+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE latest rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+latest+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; PFE tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE tariffs&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariff+impact&amp;num=5
Google Custom Search failed for &#x27;PFE tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariff+impact&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PFE tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PFE+tariff+impact&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;PFE tariff impact&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=PFE+tariff+impact&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
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
