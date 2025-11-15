---
layout: default
title: "FI Stock Report"
ticker: "FI"
date: 2025-11-15
generated_at: 2025-11-15T08:49:15.485305+00:00
runtime_seconds: 72.17
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-15T08:49:15.485305+00:00">2025-11-15 08:49 UTC</time> (runtime 1m 12s)
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — shares sit at a 3mo near-bottom and 1yr/5yr bottom with a 7d uptrend after a severe Q3-driven drop; macro froth visibility is limited in the provided data, and price is just above 60.95 support but well below the 20-DMA 85.95 and capped by 66.95 resistance.
  
  ## 1. The Biz
  
  1.1. **Activities:** Fiserv provides payments and financial services technology through two segments: Merchant Solutions and Financial Solutions. Offerings include merchant acquiring and digital commerce, Clover point-of-sale and business management, mobile payments, fraud/security, bill pay, P2P/A2A transfers, debit/credit/prepaid processing, core account processing, digital banking, ACH and real-time payments, card production/print, and professional/consulting services. It sells via direct teams and partners including ISVs, ISOs, financial institutions, and other strategic channels.
  
  1.2. **Profitable?:** Yes — it is profitable, with a ~17.05% profit margin, positive cumulative net income ($3.607B), and strong free cash flow ($4.19B).
  
  1.3. **Customer & Markets:** Primary customers include large enterprises and small businesses, banks and credit unions, large financial institutions, fintechs, public sector entities, and software providers. Markets span the United States, Europe, the Middle East and Africa, Latin America, the Asia-Pacific, and internationally.
  
  1.4. **Competition:** Competitors include Fidelity National Information Services (FIS), Automatic Data Processing (ADP), Paychex, and Broadridge Financial. Relative ranking versus these peers is not specified in the provided data.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** up — price bounced from the 60.95 local low/support toward 66.95 resistance, with recent closes around 63.8.
  
  2.2. **7d Buy/Sell Points?:** Good buys appeared near 60.95 (support/suggested buy zone), while sells or trims were near 66.95 (resistance/suggested sell zone).
  
  2.3.1. **7d Volume:** low
  
  2.3.2. **7d Volatility:** high
  
  ## 3. Longterm
  
  3.1. **Stability?:** Fiserv was incorporated in 1984 and operates globally across payments and core banking technology, indicating institutional longevity. It shows sustained profitability (~17% margin) and strong cash generation (operating cash flow $6.34B; free cash flow $4.19B). However, Q3 2025 results were labeled “abysmal,” prompting leadership changes and investigations, which elevate risk. Overall, it is a large, established provider rather than a fly-by-night, but recent volatility is high (ATR ~10.45% of price).
  
  3.2. **Innovating?:** It appears to be innovating with Clover POS, real-time payments, and pay-by-bank offerings, and posted strong earnings growth (40.4%) despite modest revenue growth (0.9%).
  
  ## 4. Context
  
  4.1. **News:** Recent headlines cite “abysmal” Q3 2025 results, a guidance reset, leadership changes, and a 43%–47% plunge that wiped out about $32B in shareholder value. Law firms (Scott+Scott; Bragar Eagel & Squire) launched investigations, and Senate Democrats are scrutinizing the former CEO’s role in guidance assumptions. In this setting, the ‘buy the rumor, sell the news’ adage did not apply; the negative news itself drove the selloff, and quick facts flag ‘Buy the rumor? no’ and ‘Sell the news? no’.
  
  4.2. **Tarrifs:** unknown
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$3.61B</td></tr>
  <tr><td>Price</td><td>63.42</td></tr>
  <tr><td>7d Resistance</td><td>66.95</td></tr>
  <tr><td>7d Support</td><td>60.95</td></tr>
  <tr><td>30d Resistance</td><td>128.78</td></tr>
  <tr><td>30d Support</td><td>60.95</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>up</td></tr>
  <tr><td>3mo</td><td>near-bottom</td></tr>
  <tr><td>1yr</td><td>bottom</td></tr>
  <tr><td>5yr</td><td>bottom</td></tr>
  <tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, company profile, fundamentals, earnings calendar</li>
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>The Guardian: business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for FI...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting FI prices from massive.com... (https://api.massive.com/v2/aggs/ticker/FI/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/FI/2025-11-14?apiKey=%2A%2A%2A
  Massive open-close: response 404 from https://api.massive.com/v1/open-close/FI/2025-11-14?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/FI/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/FI/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/FI?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/FI?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/FI?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/FI?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/FI?apiKey=%2A%2A%2A
  Massive profile: response 404 from https://api.massive.com/v3/reference/tickers/FI?apiKey=&lt;redacted&gt;
  Massive related companies: GET https://api.massive.com/v1/related-companies/FI?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/FI?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 0 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=FI&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=FI&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=FI&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=FI&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; FI core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; FI product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; FI business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI business model&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI business model&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; FI profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; FI earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; FI profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI profit outlook&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI profit outlook&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; FI target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; FI market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; FI market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI market expansion&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; FI competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; FI market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; FI competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI competitive landscape&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; FI rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; FI tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; FI rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; FI tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI tariff&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; FI latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI latest news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; FI latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; FI tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;FI tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=FI+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;FI tariffs&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=FI+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; FI tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-15T08:49:15.485305+00:00">2025-11-15 08:49 UTC</time> (runtime 1m 12s)

## 0. Entry Radar

0.1. **Long Entry?:** maybe — shares sit at a 3mo near-bottom and 1yr/5yr bottom with a 7d uptrend after a severe Q3-driven drop; macro froth visibility is limited in the provided data, and price is just above 60.95 support but well below the 20-DMA 85.95 and capped by 66.95 resistance.

## 1. The Biz

1.1. **Activities:** Fiserv provides payments and financial services technology through two segments: Merchant Solutions and Financial Solutions. Offerings include merchant acquiring and digital commerce, Clover point-of-sale and business management, mobile payments, fraud/security, bill pay, P2P/A2A transfers, debit/credit/prepaid processing, core account processing, digital banking, ACH and real-time payments, card production/print, and professional/consulting services. It sells via direct teams and partners including ISVs, ISOs, financial institutions, and other strategic channels.

1.2. **Profitable?:** Yes — it is profitable, with a ~17.05% profit margin, positive cumulative net income ($3.607B), and strong free cash flow ($4.19B).

1.3. **Customer & Markets:** Primary customers include large enterprises and small businesses, banks and credit unions, large financial institutions, fintechs, public sector entities, and software providers. Markets span the United States, Europe, the Middle East and Africa, Latin America, the Asia-Pacific, and internationally.

1.4. **Competition:** Competitors include Fidelity National Information Services (FIS), Automatic Data Processing (ADP), Paychex, and Broadridge Financial. Relative ranking versus these peers is not specified in the provided data.

## 2. Recent

2.1. **7d Trend?:** up — price bounced from the 60.95 local low/support toward 66.95 resistance, with recent closes around 63.8.

2.2. **7d Buy/Sell Points?:** Good buys appeared near 60.95 (support/suggested buy zone), while sells or trims were near 66.95 (resistance/suggested sell zone).

2.3.1. **7d Volume:** low

2.3.2. **7d Volatility:** high

## 3. Longterm

3.1. **Stability?:** Fiserv was incorporated in 1984 and operates globally across payments and core banking technology, indicating institutional longevity. It shows sustained profitability (~17% margin) and strong cash generation (operating cash flow $6.34B; free cash flow $4.19B). However, Q3 2025 results were labeled “abysmal,” prompting leadership changes and investigations, which elevate risk. Overall, it is a large, established provider rather than a fly-by-night, but recent volatility is high (ATR ~10.45% of price).

3.2. **Innovating?:** It appears to be innovating with Clover POS, real-time payments, and pay-by-bank offerings, and posted strong earnings growth (40.4%) despite modest revenue growth (0.9%).

## 4. Context

4.1. **News:** Recent headlines cite “abysmal” Q3 2025 results, a guidance reset, leadership changes, and a 43%–47% plunge that wiped out about $32B in shareholder value. Law firms (Scott+Scott; Bragar Eagel & Squire) launched investigations, and Senate Democrats are scrutinizing the former CEO’s role in guidance assumptions. In this setting, the ‘buy the rumor, sell the news’ adage did not apply; the negative news itself drove the selloff, and quick facts flag ‘Buy the rumor? no’ and ‘Sell the news? no’.

4.2. **Tarrifs:** unknown

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$3.61B</td></tr>
<tr><td>Price</td><td>63.42</td></tr>
<tr><td>7d Resistance</td><td>66.95</td></tr>
<tr><td>7d Support</td><td>60.95</td></tr>
<tr><td>30d Resistance</td><td>128.78</td></tr>
<tr><td>30d Support</td><td>60.95</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>up</td></tr>
<tr><td>3mo</td><td>near-bottom</td></tr>
<tr><td>1yr</td><td>bottom</td></tr>
<tr><td>5yr</td><td>bottom</td></tr>
<tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, company profile, fundamentals, earnings calendar</li>
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>The Guardian: business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for FI...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting FI prices from massive.com... (https://api.massive.com/v2/aggs/ticker/FI/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/FI/2025-11-14?apiKey=%2A%2A%2A
Massive open-close: response 404 from https://api.massive.com/v1/open-close/FI/2025-11-14?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/FI/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/FI/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/FI?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/FI?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/FI?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/FI?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/FI?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/FI?apiKey=%2A%2A%2A
Massive profile: response 404 from https://api.massive.com/v3/reference/tickers/FI?apiKey=&lt;redacted&gt;
Massive related companies: GET https://api.massive.com/v1/related-companies/FI?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/FI?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 0 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=FI&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=FI&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=FI&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=FI&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; FI core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; FI product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; FI business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI business model&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI business model&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; FI profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; FI earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; FI profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI profit outlook&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI profit outlook&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; FI target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; FI market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; FI market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI market expansion&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; FI competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; FI market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; FI competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI competitive landscape&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; FI rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; FI tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; FI rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; FI tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI tariff&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; FI latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI latest news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; FI latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; FI tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=FI+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;FI tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=FI+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;FI tariffs&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=FI+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; FI tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=FI+tariff+impact&amp;num=5
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
