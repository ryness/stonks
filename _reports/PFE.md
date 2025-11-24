---
layout: default
title: "PFE Stock Report"
ticker: "PFE"
date: 2025-11-21
generated_at: 2025-11-21T20:23:39.711143+00:00
runtime_seconds: 92.41
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-21T20:23:39.711143+00:00">2025-11-21 20:23 UTC</time> (runtime 1m 32s)
  
  ![Pfizer Inc. logo](https://ryness.github.io/stonks/assets/logos/PFE.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — shares sit near a 5yr near-bottom/middle of the 1yr range, suggesting value per quick facts; macro froth cues are limited per quick facts; price is just above the 20-DMA/SMA/EMA (24.65/24.82/24.85) and near support 24.28 with resistance at 26.48
  
  ## 1. The Biz
  
  1.1. **Activities:** Pfizer develops and sells prescription drugs and vaccines, generating roughly $60 billion in annual sales. Top products include the pneumococcal vaccine Prevnar 13, cancer therapy Ibrance, and cardiovascular treatment Eliquis. Its portfolio spans multiple therapeutic areas with a global footprint.
  
  1.2. **Profitable?:** yes — it is profitable, with positive net income (sum ~$9.83B), a profit margin of ~15.7%, and strong free cash flow.
  
  1.3. **Customer & Markets:** Pfizer serves global markets for prescription drugs and vaccines, with international sales representing 40% of total revenue. Emerging markets are a major contributor, and key therapeutic areas include vaccines, oncology, and cardiovascular.
  
  1.4. **Competition:** Major competitors include JNJ, MRK, LLY, ABBV, BMY, AMGN, GILD, MRNA, NVAX, and VTRS; Pfizer ranks among the world’s largest pharmaceutical firms.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** down — 7d Trend: down with price capped by 26.48 resistance and testing the 24.28 support area intraday.
  
  2.2. **7d Buy/Sell Points?:** Good buy levels appeared near support around 24.28; trims or sells looked better near resistance around 26.48.
  
  2.3.1. **7d Volume:** low
  
  2.3.2. **7d Volatility:** med
  
  ## 3. Longterm
  
  3.1. **Stability?:** Pfizer is a long-established, large-cap pharmaceutical company with roughly $60B in annual sales, indicating durable scale. It generates solid operating cash flow and free cash flow (~$14.3B) alongside positive net income and a mid-teens profit margin. While recent revenue and earnings growth are negative, its cash generation supports ongoing operations and obligations. A headline also notes a high dividend yield being characterized as safe for now, underscoring perceived stability.
  
  3.2. **Innovating?:** Innovating — a Phase 3 mRNA flu vaccine showed superior efficacy to traditional shots, and news flow highlights continued activity in key therapeutic areas. This, alongside its broad portfolio, indicates ongoing development rather than stagnation.
  
  ## 4. Context
  
  4.1. **News:** Recent news highlights a Phase 3 mRNA flu vaccine outperforming traditional shots (with higher short-term side effects), and commentary on the sustainability of Pfizer’s 6.9% dividend amid post-COVID demand normalization. Industry deal reports on collaborations/licensing provide broader context on partnering dynamics. Together, the clinical update could be a positive catalyst, but quick facts indicate no clear ‘buy the rumor’ or ‘sell the news’ setup. Investors may remain focused on execution and pipeline readouts rather than trading headlines.
  
  4.2. **Tarrifs:** Tariffs have added costs (Pfizer cited about $150 million from existing tariffs) and management flagged vulnerability to potential European tariffs; however, reports of exemptions/landmark deals and being fairly insulated from tariff impacts suggest the net effect may be moderated.
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$9.83B</td></tr>
  <tr><td>Price</td><td>25.05</td></tr>
  <tr><td>7d Resistance</td><td>26.48</td></tr>
  <tr><td>7d Support</td><td>24.28</td></tr>
  <tr><td>30d Resistance</td><td>26.48</td></tr>
  <tr><td>30d Support</td><td>23.73</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>down</td></tr>
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
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>NewsAPI: business model, profit outlook, market expansion, tariff, latest news, tariffs</li>
  <li>The Guardian: competitive landscape, rumor</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for PFE...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting PFE prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PFE/range/1/day/2020-10-23/2025-11-21?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/PFE/2025-11-21?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/PFE/2025-11-21?apiKey=&lt;redacted&gt;
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
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PFE product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PFE business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; PFE profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PFE earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PFE profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; PFE target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PFE market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PFE market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 2 result(s)
    google_custom_search search -&gt; PFE competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PFE market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PFE competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; PFE rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; PFE tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PFE rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=PFE+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=PFE+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; PFE tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; PFE latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; PFE latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; PFE tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; PFE tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-21T20:23:39.711143+00:00">2025-11-21 20:23 UTC</time> (runtime 1m 32s)

![Pfizer Inc. logo](https://ryness.github.io/stonks/assets/logos/PFE.svg)


## 0. Entry Radar

0.1. **Long Entry?:** maybe — shares sit near a 5yr near-bottom/middle of the 1yr range, suggesting value per quick facts; macro froth cues are limited per quick facts; price is just above the 20-DMA/SMA/EMA (24.65/24.82/24.85) and near support 24.28 with resistance at 26.48

## 1. The Biz

1.1. **Activities:** Pfizer develops and sells prescription drugs and vaccines, generating roughly $60 billion in annual sales. Top products include the pneumococcal vaccine Prevnar 13, cancer therapy Ibrance, and cardiovascular treatment Eliquis. Its portfolio spans multiple therapeutic areas with a global footprint.

1.2. **Profitable?:** yes — it is profitable, with positive net income (sum ~$9.83B), a profit margin of ~15.7%, and strong free cash flow.

1.3. **Customer & Markets:** Pfizer serves global markets for prescription drugs and vaccines, with international sales representing 40% of total revenue. Emerging markets are a major contributor, and key therapeutic areas include vaccines, oncology, and cardiovascular.

1.4. **Competition:** Major competitors include JNJ, MRK, LLY, ABBV, BMY, AMGN, GILD, MRNA, NVAX, and VTRS; Pfizer ranks among the world’s largest pharmaceutical firms.

## 2. Recent

2.1. **7d Trend?:** down — 7d Trend: down with price capped by 26.48 resistance and testing the 24.28 support area intraday.

2.2. **7d Buy/Sell Points?:** Good buy levels appeared near support around 24.28; trims or sells looked better near resistance around 26.48.

2.3.1. **7d Volume:** low

2.3.2. **7d Volatility:** med

## 3. Longterm

3.1. **Stability?:** Pfizer is a long-established, large-cap pharmaceutical company with roughly $60B in annual sales, indicating durable scale. It generates solid operating cash flow and free cash flow (~$14.3B) alongside positive net income and a mid-teens profit margin. While recent revenue and earnings growth are negative, its cash generation supports ongoing operations and obligations. A headline also notes a high dividend yield being characterized as safe for now, underscoring perceived stability.

3.2. **Innovating?:** Innovating — a Phase 3 mRNA flu vaccine showed superior efficacy to traditional shots, and news flow highlights continued activity in key therapeutic areas. This, alongside its broad portfolio, indicates ongoing development rather than stagnation.

## 4. Context

4.1. **News:** Recent news highlights a Phase 3 mRNA flu vaccine outperforming traditional shots (with higher short-term side effects), and commentary on the sustainability of Pfizer’s 6.9% dividend amid post-COVID demand normalization. Industry deal reports on collaborations/licensing provide broader context on partnering dynamics. Together, the clinical update could be a positive catalyst, but quick facts indicate no clear ‘buy the rumor’ or ‘sell the news’ setup. Investors may remain focused on execution and pipeline readouts rather than trading headlines.

4.2. **Tarrifs:** Tariffs have added costs (Pfizer cited about $150 million from existing tariffs) and management flagged vulnerability to potential European tariffs; however, reports of exemptions/landmark deals and being fairly insulated from tariff impacts suggest the net effect may be moderated.

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$9.83B</td></tr>
<tr><td>Price</td><td>25.05</td></tr>
<tr><td>7d Resistance</td><td>26.48</td></tr>
<tr><td>7d Support</td><td>24.28</td></tr>
<tr><td>30d Resistance</td><td>26.48</td></tr>
<tr><td>30d Support</td><td>23.73</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>down</td></tr>
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
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>NewsAPI: business model, profit outlook, market expansion, tariff, latest news, tariffs</li>
<li>The Guardian: competitive landscape, rumor</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for PFE...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting PFE prices from massive.com... (https://api.massive.com/v2/aggs/ticker/PFE/range/1/day/2020-10-23/2025-11-21?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/PFE/2025-11-21?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/PFE/2025-11-21?apiKey=&lt;redacted&gt;
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
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PFE product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PFE business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; PFE profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PFE earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PFE profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; PFE target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PFE market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PFE market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 2 result(s)
  google_custom_search search -&gt; PFE competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PFE market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PFE competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=PFE+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PFE+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; PFE rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; PFE tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PFE rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=PFE+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=PFE+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; PFE tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; PFE latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; PFE latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; PFE tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=PFE+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; PFE tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=PFE+tariff+impact&amp;num=5
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
