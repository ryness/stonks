---
layout: default
title: "PYPL Stock Report"
ticker: "PYPL"
date: 2025-11-15
generated_at: 2025-11-15T04:30:06.261641+00:00
runtime_seconds: 89.10
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-15T04:30:06.261641+00:00">2025-11-15 04:30 UTC</time> (runtime 1m 29s)
  
  ![PayPal Holdings, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/PYPL.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — at a 1yr/5yr near-bottom with oversold readings per quick facts and a 7d downtrend; macro froth visibility is limited, and price sits at 62.81 on 62.75 support and well below the ~20-DMA/EMA (~68) with nearby resistance ~68.07.
  
  ## 1. The Biz
  
  1.1. **Activities:** PayPal provides electronic payment solutions for merchants and consumers focused on online transactions. Its platform includes checkout, digital wallets, and processing, and it owns Venmo for person-to-person payments. The company reported 434 million active accounts at the end of 2024.
  
  1.2. **Profitable?:** Yes — it is profitable, with recent positive net income totaling about $4.92B, a ~15% profit margin, and positive free cash flow.
  
  1.3. **Customer & Markets:** Primary customers are merchants/e-commerce sellers and consumers transacting online via PayPal and Venmo. It serves online retail and digital services markets, with operations based in the United States.
  
  1.4. **Competition:** Competitors include Apple (AAPL), Visa (V), Shopify (SHOP), Coinbase (COIN), and Affirm (AFRM). With 434M active accounts, it is one of the large players in online payments among these rivals.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** down — shares closed at 62.81 below the 20-day average (~68.04) and near 7d support at 62.75.
  
  2.2. **7d Buy/Sell Points?:** Buys near 64.78 or the 62.75 support looked favorable; sells into 67.99–68.07 resistance offered exits.
  
  2.3.1. **7d Volume:** high
  
  2.3.2. **7d Volatility:** high
  
  ## 3. Longterm
  
  3.1. **Stability?:** PayPal is a standalone company since its 2015 spin-off from eBay, with 434 million active accounts indicating scale. It generates solid profitability ($4.92B recent net income) and strong cash flow ($6.43B operating and $3.13B free cash flow), supporting durability. As a U.S.-based Financial Services firm in Credit Services, it operates at scale across online payments. While balance sheet specifics aren’t provided, sustained profits and cash generation point to a generally stable institution.
  
  3.2. **Innovating?:** It is innovating and growing, evidenced by Venmo and support for crypto buy/sell via PayPal, alongside 7.3% revenue growth and 23.6% earnings growth.
  
  ## 4. Context
  
  4.1. **News:** Recent mentions frame PayPal as a cheap growth stock and note that users can buy and sell cryptocurrency via PayPal. Prior coverage urged caution into its late-October earnings given past post-report drops. Quick facts indicate “Buy the rumor? no” and “Sell the news? no,” suggesting limited rumor-driven spikes. In this context, the adage cautions against chasing headlines, and recent news hasn’t consistently produced sell-the-news reactions.
  
  4.2. **Tarrifs:** unknown
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$4.92B</td></tr>
  <tr><td>Price</td><td>62.81</td></tr>
  <tr><td>7d Resistance</td><td>68.07</td></tr>
  <tr><td>7d Support</td><td>62.75</td></tr>
  <tr><td>30d Resistance</td><td>79.21</td></tr>
  <tr><td>30d Support</td><td>62.75</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>down</td></tr>
  <tr><td>3mo</td><td>bottom</td></tr>
  <tr><td>1yr</td><td>near-bottom</td></tr>
  <tr><td>5yr</td><td>near-bottom</td></tr>
  <tr><td>Overbought/Sold?</td><td>oversold</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>NewsAPI: core business, profitability, earnings trend, target customers, business model, profit outlook</li>
  <li>The Guardian: product portfolio, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for PYPL...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting PYPL prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PYPL/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/PYPL/2025-11-14?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/PYPL/2025-11-14?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/PYPL/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/PYPL/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/PYPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/PYPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/PYPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/PYPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/PYPL?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/PYPL?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/PYPL.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/PYPL?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/PYPL?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 10 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=PYPL&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=PYPL&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=PYPL&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=PYPL&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; PYPL core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+core+business&amp;num=5
  Google Custom Search failed for &#x27;PYPL core business&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+core+business&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    google_custom_search search -&gt; PYPL product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+product+portfolio&amp;num=5
  Google Custom Search failed for &#x27;PYPL product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+product+portfolio&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+product+portfolio&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+product+portfolio&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 3 result(s)
    google_custom_search search -&gt; PYPL profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+profitability&amp;num=5
  Google Custom Search failed for &#x27;PYPL profitability&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+profitability&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    google_custom_search search -&gt; PYPL earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+earnings+trend&amp;num=5
  Google Custom Search failed for &#x27;PYPL earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+earnings+trend&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 4 result(s)
    newsapi search -&gt; PYPL profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 3 result(s)
    google_custom_search search -&gt; PYPL target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+target+customers&amp;num=5
  Google Custom Search failed for &#x27;PYPL target customers&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+target+customers&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 4 result(s)
    google_custom_search search -&gt; PYPL market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+segments&amp;num=5
  Google Custom Search failed for &#x27;PYPL market segments&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+segments&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL market segments&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+market+segments&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+market+segments&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PYPL competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+competitors&amp;num=5
  Google Custom Search failed for &#x27;PYPL competitors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+competitors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL competitors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+competitors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+competitors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PYPL market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+share&amp;num=5
  Google Custom Search failed for &#x27;PYPL market share&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+share&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL market share&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+market+share&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+market+share&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PYPL rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+rumors&amp;num=5
  Google Custom Search failed for &#x27;PYPL rumors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+rumors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL rumors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+rumors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+rumors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PYPL tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariffs+news&amp;num=5
  Google Custom Search failed for &#x27;PYPL tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariffs+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariffs+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariffs+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PYPL latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+latest+rumor&amp;num=5
  Google Custom Search failed for &#x27;PYPL latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+latest+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+latest+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+latest+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PYPL tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariff+impact&amp;num=5
  Google Custom Search failed for &#x27;PYPL tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariff+impact&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;PYPL tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariff+impact&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariff+impact&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: 0 result(s)
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

**Generated:** <time class="js-local-time" datetime="2025-11-15T04:30:06.261641+00:00">2025-11-15 04:30 UTC</time> (runtime 1m 29s)

![PayPal Holdings, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/PYPL.svg)


## 0. Entry Radar

0.1. **Long Entry?:** maybe — at a 1yr/5yr near-bottom with oversold readings per quick facts and a 7d downtrend; macro froth visibility is limited, and price sits at 62.81 on 62.75 support and well below the ~20-DMA/EMA (~68) with nearby resistance ~68.07.

## 1. The Biz

1.1. **Activities:** PayPal provides electronic payment solutions for merchants and consumers focused on online transactions. Its platform includes checkout, digital wallets, and processing, and it owns Venmo for person-to-person payments. The company reported 434 million active accounts at the end of 2024.

1.2. **Profitable?:** Yes — it is profitable, with recent positive net income totaling about $4.92B, a ~15% profit margin, and positive free cash flow.

1.3. **Customer & Markets:** Primary customers are merchants/e-commerce sellers and consumers transacting online via PayPal and Venmo. It serves online retail and digital services markets, with operations based in the United States.

1.4. **Competition:** Competitors include Apple (AAPL), Visa (V), Shopify (SHOP), Coinbase (COIN), and Affirm (AFRM). With 434M active accounts, it is one of the large players in online payments among these rivals.

## 2. Recent

2.1. **7d Trend?:** down — shares closed at 62.81 below the 20-day average (~68.04) and near 7d support at 62.75.

2.2. **7d Buy/Sell Points?:** Buys near 64.78 or the 62.75 support looked favorable; sells into 67.99–68.07 resistance offered exits.

2.3.1. **7d Volume:** high

2.3.2. **7d Volatility:** high

## 3. Longterm

3.1. **Stability?:** PayPal is a standalone company since its 2015 spin-off from eBay, with 434 million active accounts indicating scale. It generates solid profitability ($4.92B recent net income) and strong cash flow ($6.43B operating and $3.13B free cash flow), supporting durability. As a U.S.-based Financial Services firm in Credit Services, it operates at scale across online payments. While balance sheet specifics aren’t provided, sustained profits and cash generation point to a generally stable institution.

3.2. **Innovating?:** It is innovating and growing, evidenced by Venmo and support for crypto buy/sell via PayPal, alongside 7.3% revenue growth and 23.6% earnings growth.

## 4. Context

4.1. **News:** Recent mentions frame PayPal as a cheap growth stock and note that users can buy and sell cryptocurrency via PayPal. Prior coverage urged caution into its late-October earnings given past post-report drops. Quick facts indicate “Buy the rumor? no” and “Sell the news? no,” suggesting limited rumor-driven spikes. In this context, the adage cautions against chasing headlines, and recent news hasn’t consistently produced sell-the-news reactions.

4.2. **Tarrifs:** unknown

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$4.92B</td></tr>
<tr><td>Price</td><td>62.81</td></tr>
<tr><td>7d Resistance</td><td>68.07</td></tr>
<tr><td>7d Support</td><td>62.75</td></tr>
<tr><td>30d Resistance</td><td>79.21</td></tr>
<tr><td>30d Support</td><td>62.75</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>down</td></tr>
<tr><td>3mo</td><td>bottom</td></tr>
<tr><td>1yr</td><td>near-bottom</td></tr>
<tr><td>5yr</td><td>near-bottom</td></tr>
<tr><td>Overbought/Sold?</td><td>oversold</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>NewsAPI: core business, profitability, earnings trend, target customers, business model, profit outlook</li>
<li>The Guardian: product portfolio, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for PYPL...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting PYPL prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PYPL/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/PYPL/2025-11-14?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/PYPL/2025-11-14?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/PYPL/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/PYPL/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/PYPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/PYPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/PYPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/PYPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/PYPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/PYPL?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/PYPL?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/PYPL.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/PYPL?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/PYPL?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 10 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=PYPL&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=PYPL&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=PYPL&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=PYPL&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; PYPL core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+core+business&amp;num=5
Google Custom Search failed for &#x27;PYPL core business&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+core+business&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  google_custom_search search -&gt; PYPL product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+product+portfolio&amp;num=5
Google Custom Search failed for &#x27;PYPL product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+product+portfolio&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+product+portfolio&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+product+portfolio&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 3 result(s)
  google_custom_search search -&gt; PYPL profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+profitability&amp;num=5
Google Custom Search failed for &#x27;PYPL profitability&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+profitability&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  google_custom_search search -&gt; PYPL earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+earnings+trend&amp;num=5
Google Custom Search failed for &#x27;PYPL earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+earnings+trend&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 4 result(s)
  newsapi search -&gt; PYPL profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 3 result(s)
  google_custom_search search -&gt; PYPL target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+target+customers&amp;num=5
Google Custom Search failed for &#x27;PYPL target customers&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+target+customers&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 4 result(s)
  google_custom_search search -&gt; PYPL market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+segments&amp;num=5
Google Custom Search failed for &#x27;PYPL market segments&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+segments&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL market segments&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+market+segments&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+market+segments&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PYPL competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+competitors&amp;num=5
Google Custom Search failed for &#x27;PYPL competitors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+competitors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL competitors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+competitors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+competitors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PYPL market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+share&amp;num=5
Google Custom Search failed for &#x27;PYPL market share&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+share&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL market share&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+market+share&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+market+share&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PYPL rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+rumors&amp;num=5
Google Custom Search failed for &#x27;PYPL rumors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+rumors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL rumors&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+rumors&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+rumors&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PYPL tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariffs+news&amp;num=5
Google Custom Search failed for &#x27;PYPL tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariffs+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariffs+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariffs+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PYPL latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+latest+rumor&amp;num=5
Google Custom Search failed for &#x27;PYPL latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+latest+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+latest+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+latest+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PYPL tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariff+impact&amp;num=5
Google Custom Search failed for &#x27;PYPL tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariff+impact&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;PYPL tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+tariff+impact&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+tariff+impact&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: 0 result(s)
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
