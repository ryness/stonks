---
layout: default
title: "NVO Stock Report"
ticker: "NVO"
date: 2025-11-15
generated_at: 2025-11-15T10:25:30.003229+00:00
runtime_seconds: 62.96
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-15T10:25:30.003229+00:00">2025-11-15 10:25 UTC</time> (runtime 1m 3s)
  
  ![Novo-Nordisk A/S logo](https://ryness.github.io/stonks/assets/logos/NVO.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — shares sit near-bottom on 3mo/1yr/5yr markers and no clear macro froth cues are provided; price is below the 20-DMA (50.33) and SMA/EMA (~54.55/53.44) while holding above 45.15 support and below 50.43 resistance
  
  ## 1. The Biz
  
  1.1. **Activities:** Novo Nordisk is the leading provider of diabetes care products, manufacturing and marketing human and modern insulins, GLP-1 injectable therapies, oral antidiabetic agents, and obesity treatments. It also operates a smaller biopharmaceutical/Rare Disease segment (<10% of revenue) focused on protein therapies for hemophilia and other disorders.
  
  1.2. **Profitable?:** yes — it is profitable, with a 32.88% profit margin, sustained positive net income, and positive free cash flow.
  
  1.3. **Customer & Markets:** Primary customers are patients with diabetes, obesity, and select rare diseases. The company serves global markets, holding roughly one-third of the global branded diabetes treatment market across its Diabetes and Obesity Care and Rare Disease segments.
  
  1.4. **Competition:** Key competitors include Eli Lilly and large pharma peers such as Sanofi, AstraZeneca, Novartis, and GSK; Novo Nordisk ranks as a leader in diabetes care with roughly one-third of the global branded diabetes market.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** up — 7d Trend: up, with price rebounding off 45.15 support toward 48.26 and a local high near 50.43.
  
  2.2. **7d Buy/Sell Points?:** Buying near 45.15 support was favorable; selling or trimming near 50.43 resistance offered good exits.
  
  2.3.1. **7d Volume:** low
  
  2.3.2. **7d Volatility:** med
  
  ## 3. Longterm
  
  3.1. **Stability?:** Novo Nordisk is a long-established, Denmark-based healthcare company and the leading global diabetes player. It shows strong stability with a 32.88% profit margin, robust operating cash flow (123.78B), and positive free cash flow (34.55B). Net income has been consistently positive over multiple periods. These metrics indicate a stable institution rather than a fly-by-night.
  
  3.2. **Innovating?:** It is innovating and growing, evidenced by positive Phase 2 data for Coramitug in ATTR-CM and competitive moves like cutting Wegovy prices in India.
  
  ## 4. Context
  
  4.1. **News:** Recent news includes a board candidate withdrawing, positive Phase 2 results for Coramitug, and a strategic Wegovy price cut in India, while Novo rose despite losing the Metsera bid to Pfizer. Competitive context intensified as Eli Lilly pursued discounted Medicare access for weight-loss drugs and telehealth offerings expanded access to GLP-1s. These items suggest active pipeline and pricing strategies amid competitive pressure. Given quick facts signaling 'no' on buy-the-rumor/sell-the-news, recent headlines have not clearly triggered that dynamic.
  
  4.2. **Tarrifs:** Mixed signals: management commentary indicates limited concern about proposed tariffs, while other reports highlight potential pricing/tariff risks; overall stock impact in the provided data is uncertain.
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$103.77B</td></tr>
  <tr><td>Price</td><td>48.26</td></tr>
  <tr><td>7d Resistance</td><td>50.43</td></tr>
  <tr><td>7d Support</td><td>45.15</td></tr>
  <tr><td>30d Resistance</td><td>60.90</td></tr>
  <tr><td>30d Support</td><td>45.15</td></tr>
  <tr><td>Buy the dip?</td><td>no</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>up</td></tr>
  <tr><td>3mo</td><td>near-bottom</td></tr>
  <tr><td>1yr</td><td>near-bottom</td></tr>
  <tr><td>5yr</td><td>near-bottom</td></tr>
  <tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>The Guardian: business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for NVO...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting NVO prices from massive.com... (https://api.massive.com/v2/aggs/ticker/NVO/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/NVO/2025-11-14?apiKey=%2A%2A%2A
  Massive open-close: response 200 from https://api.massive.com/v1/open-close/NVO/2025-11-14?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/NVO/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/NVO/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/NVO?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/NVO?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/NVO?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/NVO?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/NVO?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/NVO?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/NVO.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/NVO?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/NVO?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 0 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=NVO&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=NVO&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=NVO&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=NVO&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; NVO core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NVO product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NVO business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO business model&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO business model&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; NVO profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NVO earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NVO profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO profit outlook&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO profit outlook&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; NVO target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NVO market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NVO market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO market expansion&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; NVO competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NVO market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NVO competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO competitive landscape&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; NVO rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; NVO tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NVO rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; NVO tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO tariff&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    newsapi search -&gt; NVO latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO latest news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; NVO latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; NVO tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  NewsAPI search failed for &#x27;NVO tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
  GNews search: GET https://gnews.io/api/v4/search?q=NVO+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  GNews search failed for &#x27;NVO tariffs&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
  Guardian search: GET https://content.guardianapis.com/search?q=NVO+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
      gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
      guardian: 5 result(s)
    google_custom_search search -&gt; NVO tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-15T10:25:30.003229+00:00">2025-11-15 10:25 UTC</time> (runtime 1m 3s)

![Novo-Nordisk A/S logo](https://ryness.github.io/stonks/assets/logos/NVO.svg)


## 0. Entry Radar

0.1. **Long Entry?:** maybe — shares sit near-bottom on 3mo/1yr/5yr markers and no clear macro froth cues are provided; price is below the 20-DMA (50.33) and SMA/EMA (~54.55/53.44) while holding above 45.15 support and below 50.43 resistance

## 1. The Biz

1.1. **Activities:** Novo Nordisk is the leading provider of diabetes care products, manufacturing and marketing human and modern insulins, GLP-1 injectable therapies, oral antidiabetic agents, and obesity treatments. It also operates a smaller biopharmaceutical/Rare Disease segment (<10% of revenue) focused on protein therapies for hemophilia and other disorders.

1.2. **Profitable?:** yes — it is profitable, with a 32.88% profit margin, sustained positive net income, and positive free cash flow.

1.3. **Customer & Markets:** Primary customers are patients with diabetes, obesity, and select rare diseases. The company serves global markets, holding roughly one-third of the global branded diabetes treatment market across its Diabetes and Obesity Care and Rare Disease segments.

1.4. **Competition:** Key competitors include Eli Lilly and large pharma peers such as Sanofi, AstraZeneca, Novartis, and GSK; Novo Nordisk ranks as a leader in diabetes care with roughly one-third of the global branded diabetes market.

## 2. Recent

2.1. **7d Trend?:** up — 7d Trend: up, with price rebounding off 45.15 support toward 48.26 and a local high near 50.43.

2.2. **7d Buy/Sell Points?:** Buying near 45.15 support was favorable; selling or trimming near 50.43 resistance offered good exits.

2.3.1. **7d Volume:** low

2.3.2. **7d Volatility:** med

## 3. Longterm

3.1. **Stability?:** Novo Nordisk is a long-established, Denmark-based healthcare company and the leading global diabetes player. It shows strong stability with a 32.88% profit margin, robust operating cash flow (123.78B), and positive free cash flow (34.55B). Net income has been consistently positive over multiple periods. These metrics indicate a stable institution rather than a fly-by-night.

3.2. **Innovating?:** It is innovating and growing, evidenced by positive Phase 2 data for Coramitug in ATTR-CM and competitive moves like cutting Wegovy prices in India.

## 4. Context

4.1. **News:** Recent news includes a board candidate withdrawing, positive Phase 2 results for Coramitug, and a strategic Wegovy price cut in India, while Novo rose despite losing the Metsera bid to Pfizer. Competitive context intensified as Eli Lilly pursued discounted Medicare access for weight-loss drugs and telehealth offerings expanded access to GLP-1s. These items suggest active pipeline and pricing strategies amid competitive pressure. Given quick facts signaling 'no' on buy-the-rumor/sell-the-news, recent headlines have not clearly triggered that dynamic.

4.2. **Tarrifs:** Mixed signals: management commentary indicates limited concern about proposed tariffs, while other reports highlight potential pricing/tariff risks; overall stock impact in the provided data is uncertain.

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$103.77B</td></tr>
<tr><td>Price</td><td>48.26</td></tr>
<tr><td>7d Resistance</td><td>50.43</td></tr>
<tr><td>7d Support</td><td>45.15</td></tr>
<tr><td>30d Resistance</td><td>60.90</td></tr>
<tr><td>30d Support</td><td>45.15</td></tr>
<tr><td>Buy the dip?</td><td>no</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>up</td></tr>
<tr><td>3mo</td><td>near-bottom</td></tr>
<tr><td>1yr</td><td>near-bottom</td></tr>
<tr><td>5yr</td><td>near-bottom</td></tr>
<tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>The Guardian: business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for NVO...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting NVO prices from massive.com... (https://api.massive.com/v2/aggs/ticker/NVO/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/NVO/2025-11-14?apiKey=%2A%2A%2A
Massive open-close: response 200 from https://api.massive.com/v1/open-close/NVO/2025-11-14?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/NVO/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/NVO/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/NVO?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/NVO?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/NVO?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/NVO?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/NVO?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/NVO?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/NVO?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/NVO.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/NVO?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/NVO?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 0 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=NVO&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=NVO&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=NVO&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=NVO&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; NVO core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NVO product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NVO business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO business model&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+business+model&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO business model&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+business+model&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; NVO profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NVO earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NVO profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO profit outlook&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+profit+outlook&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO profit outlook&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+profit+outlook&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; NVO target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NVO market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NVO market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO market expansion&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO market expansion&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; NVO competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NVO market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NVO competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO competitive landscape&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO competitive landscape&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; NVO rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; NVO tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NVO rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO rumor&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO rumor&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; NVO tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO tariff&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+tariff&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO tariff&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+tariff&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  newsapi search -&gt; NVO latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO latest news&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+latest+news&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO latest news&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+latest+news&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; NVO latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; NVO tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=NVO+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
NewsAPI search failed for &#x27;NVO tariffs&#x27;: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
GNews search: GET https://gnews.io/api/v4/search?q=NVO+tariffs&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
GNews search failed for &#x27;NVO tariffs&#x27;: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
Guardian search: GET https://content.guardianapis.com/search?q=NVO+tariffs&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: error: 429 Client Error: Too Many Requests for url: https://newsapi.org/v2/everything
    gnews: error: 403 Client Error: Forbidden for url: https://gnews.io/api/v4/search
    guardian: 5 result(s)
  google_custom_search search -&gt; NVO tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=NVO+tariff+impact&amp;num=5
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
