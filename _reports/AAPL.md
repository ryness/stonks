---
layout: default
title: "AAPL Stock Report"
ticker: "AAPL"
date: 2025-11-12
generated_at: 2025-11-12T05:21:59.511254+00:00
runtime_seconds: 50.65
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-12T05:21:59.511254+00:00">2025-11-12 05:21 UTC</time> (runtime 50.65s)
  
  ![Apple Inc. logo](https://ryness.github.io/stonks/assets/logos/AAPL.svg)
  
  
  ## 1. The Biz
  
  1.1. **Activities:** Apple designs and sells consumer electronics like iPhone (the majority of sales), Mac, iPad, Apple Watch, and accessories, anchored by a tightly integrated software ecosystem. It also offers services including streaming video, subscription bundles, cloud, payments, and advertising, and designs its own software and semiconductors while manufacturing with partners such as Foxconn and TSMC. Sales are split between direct retail/online stores and a larger indirect channel through partners and distributors.
  
  1.2. **Profitable?:** Yes — it is highly profitable, with ~26.9% profit margin, $112.01B in net income over the last year, and strong free cash flow of about $78.9B.
  
  1.3. **Customer & Markets:** Its primary customers are consumers and small and mid-sized businesses, alongside education, enterprise, and government buyers. It reaches them via direct Apple Stores and online, with a majority of sales flowing through partners and distribution.
  
  1.4. **Competition:** Principal competitors include Microsoft, Alphabet (Google), Amazon, Meta, Netflix, and NVIDIA across operating systems, devices, services, and AI. Apple ranks among the largest companies globally by market value and scale.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** up — shares climbed from a ~266.51 local low to 275.25, testing 7d resistance near 275.91.
  
  2.2. **7d Buy/Sell Points?:** Buying near ~266.51 (support/suggested buy zone) offered favorable risk-reward, while selling around ~273.14 to ~275.91 (suggested sell zone/7d resistance) captured strength.
  
  2.3.1. **7d Volume:** med
  
  2.3.2. **7d Volatility:** low
  
  ## 3. Longterm
  
  3.1. **Stability?:** Apple is a long-established mega-cap and among the largest companies in the world. It demonstrates consistent profitability with $112.01B in net income and a ~26.9% margin, backed by $111.5B in operating cash flow and $78.9B in free cash flow. A diversified hardware, software, and services ecosystem and broad distribution support durability. Overall cash generation and scale indicate a stable institution rather than a fly-by-night operator.
  
  3.2. **Innovating?:** It is innovating and growing, adding services (streaming, bundles) and augmented reality while designing its own chips and software. Recent revenue and earnings growth (7.9% and 86.4%) underscore momentum.
  
  ## 4. Context
  
  4.1. **News:** Recent headlines focus on broader tech market context: rebounds after last week’s losses and concerns about S&P 500 concentration in mega-caps. Apple appeared in technology portfolio features and industry discussions about digital transformation and AI. Other items referenced promotions leveraging Apple products. With overbought readings and a ‘sell the news? yes’ flag in quick facts, positive headlines could prompt profit-taking consistent with the ‘buy the rumor, sell the news’ adage.
  
  4.2. **Tarrifs:** Tariff-related headlines indicate limited or mitigated impact overall: Apple rallied on tariff pauses/exemption hopes and continued to beat estimates despite worries. Some analysts warn higher tariffs could pressure gross margins, but recent reports suggest effects have often been buffered.
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$112.01B</td></tr>
  <tr><td>Price</td><td>275.25</td></tr>
  <tr><td>7d Resistance</td><td>275.91</td></tr>
  <tr><td>7d Support</td><td>265.99</td></tr>
  <tr><td>30d Resistance</td><td>277.05</td></tr>
  <tr><td>30d Support</td><td>243.76</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>yes</td></tr>
  <tr><td>7d Trend:</td><td>up</td></tr>
  <tr><td>3mo</td><td>middle</td></tr>
  <tr><td>1yr</td><td>peak</td></tr>
  <tr><td>5yr</td><td>peak</td></tr>
  <tr><td>Overbought/Sold?</td><td>overbought</td></tr>
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
  Gathering context for AAPL...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting AAPL prices from massive.com... (https://api.massive.com/v2/aggs/ticker/AAPL/range/1/day/2020-10-14/2025-11-12?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/AAPL/2025-11-11?apiKey=%2A%2A%2A
  Massive open-close: response 200 from https://api.massive.com/v1/open-close/AAPL/2025-11-11?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/AAPL/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/AAPL/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/AAPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/AAPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/AAPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/AAPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/AAPL?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/AAPL?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/AAPL.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/AAPL?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/AAPL?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 10 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=AAPL&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=AAPL&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=AAPL&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=AAPL&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; AAPL core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; AAPL product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; AAPL business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; AAPL profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; AAPL earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; AAPL profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; AAPL target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; AAPL market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; AAPL market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; AAPL competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; AAPL market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; AAPL competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; AAPL rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; AAPL tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; AAPL rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=AAPL+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=AAPL+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; AAPL tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; AAPL latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; AAPL latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; AAPL tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; AAPL tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-12T05:21:59.511254+00:00">2025-11-12 05:21 UTC</time> (runtime 50.65s)

![Apple Inc. logo](https://ryness.github.io/stonks/assets/logos/AAPL.svg)


## 1. The Biz

1.1. **Activities:** Apple designs and sells consumer electronics like iPhone (the majority of sales), Mac, iPad, Apple Watch, and accessories, anchored by a tightly integrated software ecosystem. It also offers services including streaming video, subscription bundles, cloud, payments, and advertising, and designs its own software and semiconductors while manufacturing with partners such as Foxconn and TSMC. Sales are split between direct retail/online stores and a larger indirect channel through partners and distributors.

1.2. **Profitable?:** Yes — it is highly profitable, with ~26.9% profit margin, $112.01B in net income over the last year, and strong free cash flow of about $78.9B.

1.3. **Customer & Markets:** Its primary customers are consumers and small and mid-sized businesses, alongside education, enterprise, and government buyers. It reaches them via direct Apple Stores and online, with a majority of sales flowing through partners and distribution.

1.4. **Competition:** Principal competitors include Microsoft, Alphabet (Google), Amazon, Meta, Netflix, and NVIDIA across operating systems, devices, services, and AI. Apple ranks among the largest companies globally by market value and scale.

## 2. Recent

2.1. **7d Trend?:** up — shares climbed from a ~266.51 local low to 275.25, testing 7d resistance near 275.91.

2.2. **7d Buy/Sell Points?:** Buying near ~266.51 (support/suggested buy zone) offered favorable risk-reward, while selling around ~273.14 to ~275.91 (suggested sell zone/7d resistance) captured strength.

2.3.1. **7d Volume:** med

2.3.2. **7d Volatility:** low

## 3. Longterm

3.1. **Stability?:** Apple is a long-established mega-cap and among the largest companies in the world. It demonstrates consistent profitability with $112.01B in net income and a ~26.9% margin, backed by $111.5B in operating cash flow and $78.9B in free cash flow. A diversified hardware, software, and services ecosystem and broad distribution support durability. Overall cash generation and scale indicate a stable institution rather than a fly-by-night operator.

3.2. **Innovating?:** It is innovating and growing, adding services (streaming, bundles) and augmented reality while designing its own chips and software. Recent revenue and earnings growth (7.9% and 86.4%) underscore momentum.

## 4. Context

4.1. **News:** Recent headlines focus on broader tech market context: rebounds after last week’s losses and concerns about S&P 500 concentration in mega-caps. Apple appeared in technology portfolio features and industry discussions about digital transformation and AI. Other items referenced promotions leveraging Apple products. With overbought readings and a ‘sell the news? yes’ flag in quick facts, positive headlines could prompt profit-taking consistent with the ‘buy the rumor, sell the news’ adage.

4.2. **Tarrifs:** Tariff-related headlines indicate limited or mitigated impact overall: Apple rallied on tariff pauses/exemption hopes and continued to beat estimates despite worries. Some analysts warn higher tariffs could pressure gross margins, but recent reports suggest effects have often been buffered.

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$112.01B</td></tr>
<tr><td>Price</td><td>275.25</td></tr>
<tr><td>7d Resistance</td><td>275.91</td></tr>
<tr><td>7d Support</td><td>265.99</td></tr>
<tr><td>30d Resistance</td><td>277.05</td></tr>
<tr><td>30d Support</td><td>243.76</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>yes</td></tr>
<tr><td>7d Trend:</td><td>up</td></tr>
<tr><td>3mo</td><td>middle</td></tr>
<tr><td>1yr</td><td>peak</td></tr>
<tr><td>5yr</td><td>peak</td></tr>
<tr><td>Overbought/Sold?</td><td>overbought</td></tr>
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
Gathering context for AAPL...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting AAPL prices from massive.com... (https://api.massive.com/v2/aggs/ticker/AAPL/range/1/day/2020-10-14/2025-11-12?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/AAPL/2025-11-11?apiKey=%2A%2A%2A
Massive open-close: response 200 from https://api.massive.com/v1/open-close/AAPL/2025-11-11?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/AAPL/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/AAPL/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/AAPL?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/AAPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/AAPL?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/AAPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/AAPL?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/AAPL?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/AAPL?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/AAPL.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/AAPL?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/AAPL?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 10 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=AAPL&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=AAPL&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=AAPL&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=AAPL&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; AAPL core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; AAPL product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; AAPL business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; AAPL profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; AAPL earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; AAPL profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; AAPL target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; AAPL market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; AAPL market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; AAPL competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; AAPL market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; AAPL competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; AAPL rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; AAPL tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; AAPL rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=AAPL+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=AAPL+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; AAPL tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; AAPL latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; AAPL latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; AAPL tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=AAPL+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; AAPL tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=AAPL+tariff+impact&amp;num=5
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
