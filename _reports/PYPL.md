---
layout: default
title: "PYPL Stock Report"
ticker: "PYPL"
date: 2025-11-10
generated_at: 2025-11-10T20:25:39.349641+00:00
runtime_seconds: 71.93
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-10T20:25:39.349641+00:00">2025-11-10 20:25 UTC</time> (runtime 1m 12s)
  
  ![PayPal Holdings, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/PYPL.svg)
  
  
  ## 1. The Biz
  
  1.1. **Activities:** PayPal provides electronic payment solutions for merchants and consumers, focused on online transactions. Core offerings include the PayPal digital wallet and checkout, merchant payment processing, and Venmo for person-to-person payments, serving 434 million active accounts as of 2024.
  
  1.2. **Profitable?:** Yes — PayPal is profitable, with positive net income each recent quarter (totaling about $4.68B across the last four) and a 14.96% profit margin alongside 23.6% earnings growth.
  
  1.3. **Customer & Markets:** Primary customers are online merchants and consumers using digital wallets and P2P payments (Venmo). The company operates globally, processing transactions in more than 200 markets and over 100 currencies.
  
  1.4. **Competition:** Competitors include Apple (Apple Pay), Amazon, Shopify, Affirm, Coinbase, and Visa. PayPal remains a large-scale incumbent in online payments with 434 million active accounts but faces strong competition across wallets, checkout, BNPL, and crypto.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** down — shares pulled back from a local high of 68.21 toward support at 64.78 and closed at 66.29 below the 20-DMA (68.44).
  
  2.2. **7d Buy/Sell Points?:** Buying near support around 64.78 looked attractive, while selling or trimming into 68.21–70.35 (local high/resistance) offered favorable risk-reward.
  
  2.3.1. **7d Volume:** low
  
  2.3.2. **7d Volatility:** high
  
  ## 3. Longterm
  
  3.1. **Stability?:** PayPal is a seasoned fintech, spun off from eBay in 2015, with 434 million active accounts and consistent profitability. It generates strong cash flows (operating cash flow ~$6.43B and free cash flow ~$3.13B), supporting ongoing operations and shareholder returns. These metrics indicate a stable institution rather than a fly-by-night company.
  
  3.2. **Innovating?:** It is innovating and growing, highlighted by its first-ever dividend and AI partnerships with Google and OpenAI, plus new “agentic commerce” services. Revenue and earnings growth (7.3% and 23.6%) reinforce this trajectory.
  
  ## 4. Context
  
  4.1. **News:** Recent headlines frame PayPal as a cheap growth stock, note its crypto functionality among alternative trading venues, and highlight bullish reactions to Q3 results along with the first-ever dividend and AI tie-ups with Google and OpenAI. Coverage suggests improving sentiment despite prior underperformance. With quick facts indicating “Buy the rumor? no” and “Sell the news? no,” recent news has not produced classic rumor-driven surges or post-news selloffs. This points to muted reactions and potential interest in buying dips rather than chasing headlines.
  
  4.2. **Tarrifs:** Reports in April 2025 said fintech stocks including PayPal fell on concerns tariffs would curb consumer spending, with analysts warning of recession risk; impacts are chiefly indirect via sentiment and transaction volumes rather than direct tariff costs.
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$4.68B</td></tr>
  <tr><td>Price</td><td>66.29</td></tr>
  <tr><td>7d Resistance</td><td>70.35</td></tr>
  <tr><td>7d Support</td><td>64.78</td></tr>
  <tr><td>30d Resistance</td><td>79.21</td></tr>
  <tr><td>30d Support</td><td>64.78</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>down</td></tr>
  <tr><td>3mo</td><td>near-bottom</td></tr>
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
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>NewsAPI: business model, profit outlook, market expansion, tariff, latest news, tariffs</li>
  <li>The Guardian: competitive landscape, rumor</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for PYPL...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting PYPL prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PYPL/range/1/day/2020-10-12/2025-11-10?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/PYPL/2025-11-10?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/PYPL/2025-11-10?apiKey=&lt;redacted&gt;
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
  Massive logo: using cached asset assets/logos/PYPL.svg
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
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PYPL product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PYPL business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 3 result(s)
    google_custom_search search -&gt; PYPL profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PYPL earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PYPL profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 3 result(s)
    google_custom_search search -&gt; PYPL target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PYPL market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PYPL market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; PYPL competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PYPL market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PYPL competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PYPL rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PYPL tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PYPL rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=PYPL+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PYPL+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PYPL tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; PYPL latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; PYPL latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PYPL tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; PYPL tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-10T20:25:39.349641+00:00">2025-11-10 20:25 UTC</time> (runtime 1m 12s)

![PayPal Holdings, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/PYPL.svg)


## 1. The Biz

1.1. **Activities:** PayPal provides electronic payment solutions for merchants and consumers, focused on online transactions. Core offerings include the PayPal digital wallet and checkout, merchant payment processing, and Venmo for person-to-person payments, serving 434 million active accounts as of 2024.

1.2. **Profitable?:** Yes — PayPal is profitable, with positive net income each recent quarter (totaling about $4.68B across the last four) and a 14.96% profit margin alongside 23.6% earnings growth.

1.3. **Customer & Markets:** Primary customers are online merchants and consumers using digital wallets and P2P payments (Venmo). The company operates globally, processing transactions in more than 200 markets and over 100 currencies.

1.4. **Competition:** Competitors include Apple (Apple Pay), Amazon, Shopify, Affirm, Coinbase, and Visa. PayPal remains a large-scale incumbent in online payments with 434 million active accounts but faces strong competition across wallets, checkout, BNPL, and crypto.

## 2. Recent

2.1. **7d Trend?:** down — shares pulled back from a local high of 68.21 toward support at 64.78 and closed at 66.29 below the 20-DMA (68.44).

2.2. **7d Buy/Sell Points?:** Buying near support around 64.78 looked attractive, while selling or trimming into 68.21–70.35 (local high/resistance) offered favorable risk-reward.

2.3.1. **7d Volume:** low

2.3.2. **7d Volatility:** high

## 3. Longterm

3.1. **Stability?:** PayPal is a seasoned fintech, spun off from eBay in 2015, with 434 million active accounts and consistent profitability. It generates strong cash flows (operating cash flow ~$6.43B and free cash flow ~$3.13B), supporting ongoing operations and shareholder returns. These metrics indicate a stable institution rather than a fly-by-night company.

3.2. **Innovating?:** It is innovating and growing, highlighted by its first-ever dividend and AI partnerships with Google and OpenAI, plus new “agentic commerce” services. Revenue and earnings growth (7.3% and 23.6%) reinforce this trajectory.

## 4. Context

4.1. **News:** Recent headlines frame PayPal as a cheap growth stock, note its crypto functionality among alternative trading venues, and highlight bullish reactions to Q3 results along with the first-ever dividend and AI tie-ups with Google and OpenAI. Coverage suggests improving sentiment despite prior underperformance. With quick facts indicating “Buy the rumor? no” and “Sell the news? no,” recent news has not produced classic rumor-driven surges or post-news selloffs. This points to muted reactions and potential interest in buying dips rather than chasing headlines.

4.2. **Tarrifs:** Reports in April 2025 said fintech stocks including PayPal fell on concerns tariffs would curb consumer spending, with analysts warning of recession risk; impacts are chiefly indirect via sentiment and transaction volumes rather than direct tariff costs.

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$4.68B</td></tr>
<tr><td>Price</td><td>66.29</td></tr>
<tr><td>7d Resistance</td><td>70.35</td></tr>
<tr><td>7d Support</td><td>64.78</td></tr>
<tr><td>30d Resistance</td><td>79.21</td></tr>
<tr><td>30d Support</td><td>64.78</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>down</td></tr>
<tr><td>3mo</td><td>near-bottom</td></tr>
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
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>NewsAPI: business model, profit outlook, market expansion, tariff, latest news, tariffs</li>
<li>The Guardian: competitive landscape, rumor</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for PYPL...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting PYPL prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PYPL/range/1/day/2020-10-12/2025-11-10?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/PYPL/2025-11-10?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/PYPL/2025-11-10?apiKey=&lt;redacted&gt;
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
Massive logo: using cached asset assets/logos/PYPL.svg
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
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PYPL product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PYPL business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 3 result(s)
  google_custom_search search -&gt; PYPL profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PYPL earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PYPL profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 3 result(s)
  google_custom_search search -&gt; PYPL target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PYPL market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PYPL market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; PYPL competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PYPL market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PYPL competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PYPL rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PYPL tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PYPL rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=PYPL+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PYPL+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PYPL tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; PYPL latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; PYPL latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PYPL tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PYPL+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; PYPL tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PYPL+tariff+impact&amp;num=5
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
