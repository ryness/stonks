---
layout: default
title: "META Stock Report"
ticker: "META"
date: 2025-11-15
generated_at: 2025-11-15T03:54:14.181882+00:00
runtime_seconds: 94.38
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-15T03:54:14.181882+00:00">2025-11-15 03:54 UTC</time> (runtime 1m 34s)
  
  ![Meta Platforms, Inc. Class A Common Stock logo](https://ryness.github.io/stonks/assets/logos/META.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — at a 3mo bottom with 1yr/5yr in the middle and AI-froth cautions in headlines; price is near 7d support 595.20 but well below the 20-DMA/EMA/SMA (673.44/697.51/716.58) and under 7d resistance 636.00
  
  ## 1. The Biz
  
  1.1. **Activities:** Meta operates the largest social media network globally through its Family of Apps: Facebook, Instagram, Messenger, and WhatsApp. It monetizes by packaging data from these apps to sell digital advertising. The company also invests heavily in Reality Labs, though it is a small portion of overall sales.
  
  1.2. **Profitable?:** Yes — it posts a 30.9% profit margin with multi‑billion net income and positive free and operating cash flow, despite a negative earnings growth metric.
  
  1.3. **Customer & Markets:** Primary customers are digital advertisers seeking to reach billions of end users across Meta’s apps. End users worldwide use the platforms for communication, entertainment, and business activity, enabling global, cross‑industry ad markets.
  
  1.4. **Competition:** Key competitors include Alphabet/Google and Snap for digital ads and attention, with broader competition from megacaps like Amazon, Apple, Microsoft, and Nvidia. Meta ranks as the largest social media platform by users, indicating a leading position.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** down — slipped from a local high near 635.00 to close at 609.46, tagging a low at 595.20
  
  2.2. **7d Buy/Sell Points?:** Buying near 601.20 down to support at 595.20 looked favorable, while selling or trimming into 635.00–636.00 aligned with resistance.
  
  2.3.1. **7d Volume:** med
  
  2.3.2. **7d Volatility:** med
  
  ## 3. Longterm
  
  3.1. **Stability?:** Meta appears to be a stable institution, operating the largest social platform with close to 4 billion monthly active users. It generates strong profitability (30.9% margin) and substantial cash flow, including $107.57B operating cash flow and positive free cash flow. Net income has been in the tens of billions across recent periods. While it invests heavily in Reality Labs, that segment remains a small share of sales, supporting overall stability.
  
  3.2. **Innovating?:** It is innovating and growing, with 26.2% revenue growth and heavy investment in Reality Labs. News also cites major AI infrastructure engagements (e.g., Broadcom and a $3B deal via Nebius), underscoring ongoing AI initiatives.
  
  ## 4. Context
  
  4.1. **News:** Recent coverage shows mixed sentiment: a congressman favored other megacaps over Meta, while Broadcom highlighted significant AI accelerator deals with Meta and others. Nebius’ stock fell despite a $3B deal with Meta amid a cooling AI trade, and headlines warn of AI demand outpacing infrastructure. This backdrop suggests that supplier news can trigger ‘sell the news’ behavior, but Meta-specific quick facts flag ‘Sell the news? no’. Overall, AI buildout ties support the long-term story while near-term AI froth concerns may mute rumor-driven pops.
  
  4.2. **Tarrifs:** unknown
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$58.53B</td></tr>
  <tr><td>Price</td><td>609.46</td></tr>
  <tr><td>7d Resistance</td><td>636.00</td></tr>
  <tr><td>7d Support</td><td>595.20</td></tr>
  <tr><td>30d Resistance</td><td>759.16</td></tr>
  <tr><td>30d Support</td><td>595.20</td></tr>
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
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>NewsAPI: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact, business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for META...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting META prices from massive.com... (https://api.massive.com/v2/aggs/ticker/META/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/META/2025-11-14?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/META/2025-11-14?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/META/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/META/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/META?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/META?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/META?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/META?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/META?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/META?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/META.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/META?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/META?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 10 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=META&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=META&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=META&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=META&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; META core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+core+business&amp;num=5
  Google Custom Search failed for &#x27;META core business&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+core+business&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    google_custom_search search -&gt; META product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+product+portfolio&amp;num=5
  Google Custom Search failed for &#x27;META product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+product+portfolio&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    newsapi search -&gt; META business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; META profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+profitability&amp;num=5
  Google Custom Search failed for &#x27;META profitability&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+profitability&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 4 result(s)
    google_custom_search search -&gt; META earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+earnings+trend&amp;num=5
  Google Custom Search failed for &#x27;META earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+earnings+trend&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    newsapi search -&gt; META profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; META target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+target+customers&amp;num=5
  Google Custom Search failed for &#x27;META target customers&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+target+customers&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    google_custom_search search -&gt; META market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+market+segments&amp;num=5
  Google Custom Search failed for &#x27;META market segments&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+market+segments&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    newsapi search -&gt; META market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; META competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+competitors&amp;num=5
  Google Custom Search failed for &#x27;META competitors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+competitors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 4 result(s)
    google_custom_search search -&gt; META market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+market+share&amp;num=5
  Google Custom Search failed for &#x27;META market share&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+market+share&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    newsapi search -&gt; META competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; META rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+rumors&amp;num=5
  Google Custom Search failed for &#x27;META rumors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+rumors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    google_custom_search search -&gt; META tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+tariffs+news&amp;num=5
  Google Custom Search failed for &#x27;META tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariffs+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
    newsapi search -&gt; META rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; META tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; META latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; META latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+latest+rumor&amp;num=5
  Google Custom Search failed for &#x27;META latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+latest+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 4 result(s)
    newsapi search -&gt; META tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; META tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+tariff+impact&amp;num=5
  Google Custom Search failed for &#x27;META tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
  NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariff+impact&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
      newsapi: 5 result(s)
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

**Generated:** <time class="js-local-time" datetime="2025-11-15T03:54:14.181882+00:00">2025-11-15 03:54 UTC</time> (runtime 1m 34s)

![Meta Platforms, Inc. Class A Common Stock logo](https://ryness.github.io/stonks/assets/logos/META.svg)


## 0. Entry Radar

0.1. **Long Entry?:** maybe — at a 3mo bottom with 1yr/5yr in the middle and AI-froth cautions in headlines; price is near 7d support 595.20 but well below the 20-DMA/EMA/SMA (673.44/697.51/716.58) and under 7d resistance 636.00

## 1. The Biz

1.1. **Activities:** Meta operates the largest social media network globally through its Family of Apps: Facebook, Instagram, Messenger, and WhatsApp. It monetizes by packaging data from these apps to sell digital advertising. The company also invests heavily in Reality Labs, though it is a small portion of overall sales.

1.2. **Profitable?:** Yes — it posts a 30.9% profit margin with multi‑billion net income and positive free and operating cash flow, despite a negative earnings growth metric.

1.3. **Customer & Markets:** Primary customers are digital advertisers seeking to reach billions of end users across Meta’s apps. End users worldwide use the platforms for communication, entertainment, and business activity, enabling global, cross‑industry ad markets.

1.4. **Competition:** Key competitors include Alphabet/Google and Snap for digital ads and attention, with broader competition from megacaps like Amazon, Apple, Microsoft, and Nvidia. Meta ranks as the largest social media platform by users, indicating a leading position.

## 2. Recent

2.1. **7d Trend?:** down — slipped from a local high near 635.00 to close at 609.46, tagging a low at 595.20

2.2. **7d Buy/Sell Points?:** Buying near 601.20 down to support at 595.20 looked favorable, while selling or trimming into 635.00–636.00 aligned with resistance.

2.3.1. **7d Volume:** med

2.3.2. **7d Volatility:** med

## 3. Longterm

3.1. **Stability?:** Meta appears to be a stable institution, operating the largest social platform with close to 4 billion monthly active users. It generates strong profitability (30.9% margin) and substantial cash flow, including $107.57B operating cash flow and positive free cash flow. Net income has been in the tens of billions across recent periods. While it invests heavily in Reality Labs, that segment remains a small share of sales, supporting overall stability.

3.2. **Innovating?:** It is innovating and growing, with 26.2% revenue growth and heavy investment in Reality Labs. News also cites major AI infrastructure engagements (e.g., Broadcom and a $3B deal via Nebius), underscoring ongoing AI initiatives.

## 4. Context

4.1. **News:** Recent coverage shows mixed sentiment: a congressman favored other megacaps over Meta, while Broadcom highlighted significant AI accelerator deals with Meta and others. Nebius’ stock fell despite a $3B deal with Meta amid a cooling AI trade, and headlines warn of AI demand outpacing infrastructure. This backdrop suggests that supplier news can trigger ‘sell the news’ behavior, but Meta-specific quick facts flag ‘Sell the news? no’. Overall, AI buildout ties support the long-term story while near-term AI froth concerns may mute rumor-driven pops.

4.2. **Tarrifs:** unknown

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$58.53B</td></tr>
<tr><td>Price</td><td>609.46</td></tr>
<tr><td>7d Resistance</td><td>636.00</td></tr>
<tr><td>7d Support</td><td>595.20</td></tr>
<tr><td>30d Resistance</td><td>759.16</td></tr>
<tr><td>30d Support</td><td>595.20</td></tr>
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
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>NewsAPI: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact, business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for META...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting META prices from massive.com... (https://api.massive.com/v2/aggs/ticker/META/range/1/day/2020-10-17/2025-11-15?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/META/2025-11-14?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/META/2025-11-14?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/META/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/META/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/META?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/META?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/META?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/META?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/META?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/META?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/META?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/META.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/META?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/META?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 10 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=META&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=META&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=META&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=META&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; META core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+core+business&amp;num=5
Google Custom Search failed for &#x27;META core business&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+core+business&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  google_custom_search search -&gt; META product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+product+portfolio&amp;num=5
Google Custom Search failed for &#x27;META product portfolio&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+product+portfolio&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  newsapi search -&gt; META business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; META profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+profitability&amp;num=5
Google Custom Search failed for &#x27;META profitability&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+profitability&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 4 result(s)
  google_custom_search search -&gt; META earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+earnings+trend&amp;num=5
Google Custom Search failed for &#x27;META earnings trend&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+earnings+trend&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  newsapi search -&gt; META profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; META target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+target+customers&amp;num=5
Google Custom Search failed for &#x27;META target customers&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+target+customers&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  google_custom_search search -&gt; META market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+market+segments&amp;num=5
Google Custom Search failed for &#x27;META market segments&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+market+segments&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  newsapi search -&gt; META market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; META competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+competitors&amp;num=5
Google Custom Search failed for &#x27;META competitors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+competitors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 4 result(s)
  google_custom_search search -&gt; META market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+market+share&amp;num=5
Google Custom Search failed for &#x27;META market share&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+market+share&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  newsapi search -&gt; META competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; META rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+rumors&amp;num=5
Google Custom Search failed for &#x27;META rumors&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+rumors&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  google_custom_search search -&gt; META tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+tariffs+news&amp;num=5
Google Custom Search failed for &#x27;META tariffs news&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariffs+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
  newsapi search -&gt; META rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; META tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; META latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; META latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+latest+rumor&amp;num=5
Google Custom Search failed for &#x27;META latest rumor&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+latest+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 4 result(s)
  newsapi search -&gt; META tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; META tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=META+tariff+impact&amp;num=5
Google Custom Search failed for &#x27;META tariff impact&#x27;: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
NewsAPI search: GET https://newsapi.org/v2/everything?q=META+tariff+impact&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    google_custom_search: error: 429 Client Error: Too Many Requests for url: https://www.googleapis.com/customsearch/v1
    newsapi: 5 result(s)
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
