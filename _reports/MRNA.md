---
layout: default
title: "MRNA Stock Report"
ticker: "MRNA"
date: 2025-11-24
generated_at: 2025-11-24T01:42:41.098728+00:00
runtime_seconds: 50.40
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-24T01:42:41.098728+00:00">2025-11-24 01:42 UTC</time> (runtime 50.40s)
  
  ![Moderna, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/MRNA.svg)
  
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** no — at a 1yr near-bottom and 5yr bottom with a 7d downtrend per quick facts; macro froth visibility is limited in the provided data, and shares sit below the 20-DMA 25.03/EMA 25.70/SMA 25.87 and under 26.20 resistance, hovering just above 22.28 support
  
  ## 1. The Biz
  
  1.1. **Activities:** Moderna is a commercial-stage biotech built around an mRNA platform, validated by its COVID-19 vaccine authorized in December 2020. It develops and commercializes mRNA-based vaccines and therapeutics, with 35 clinical-stage candidates as of August 2025. Programs span infectious diseases, oncology, cardiovascular disease, and rare genetic disorders.
  
  1.2. **Profitable?:** No — it is currently unprofitable with -$3.12B in the last quarter, a -139.6% profit margin, and negative free cash flow, and no timeline to profitability is provided.
  
  1.3. **Customer & Markets:** unknown
  
  1.4. **Competition:** Primary competitors include Pfizer (PFE), Novavax (NVAX), Johnson & Johnson (JNJ), Merck (MRK), CureVac (CVAC), and Regeneron (REGN). Moderna is a commercial-stage mRNA leader with a broad pipeline validated by its COVID-19 vaccine, though the data does not quantify market rank.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** down — fell from a local high of 25.06 toward support at 22.28 and closed at 23.72
  
  2.2. **7d Buy/Sell Points?:** Buy near 22.28–24.18 (support and suggested buy zone); sell near 25.06–26.20 (local high and resistance).
  
  2.3.1. **7d Volume:** med
  
  2.3.2. **7d Volatility:** high
  
  ## 3. Longterm
  
  3.1. **Stability?:** Moderna was founded in 2010 and IPO’d in 2018, making it a well-established public biotech. Its mRNA platform was validated with a U.S.-authorized COVID-19 vaccine, indicating commercial execution. However, recent financials show sustained losses (net income sum -$3.116B), negative operating cash flow (-$1.978B), and negative free cash flow, which weigh on financial resilience. The stock sits near its 1yr near-bottom and 5yr bottom, reflecting elevated risk. Overall, it is not a fly-by-night startup but carries typical biotech volatility and cash burn.
  
  3.2. **Innovating?:** Yes — it is advancing 35 mRNA candidates across infectious disease, oncology, cardiovascular, and rare diseases, though it recently discontinued its CMV program after a Phase 3 miss.
  
  ## 4. Context
  
  4.1. **News:** Moderna discontinued its CMV vaccine program after a Phase 3 failure to prevent infection, which likely pressured sentiment. Separately, coverage highlighted potential long-term upside tied to its mRNA platform and cancer vaccine mRNA-4157. Sector peers posted oncology progress (e.g., Immatics data and CytomX presentations), adding broader context to modality momentum. Quick facts indicate no clear ‘buy the rumor’ or ‘sell the news’ setup recently, suggesting limited tradable catalysts per the adage.
  
  4.2. **Tarrifs:** unknown
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>$-3.12B</td></tr>
  <tr><td>Price</td><td>23.72</td></tr>
  <tr><td>7d Resistance</td><td>26.20</td></tr>
  <tr><td>7d Support</td><td>22.28</td></tr>
  <tr><td>30d Resistance</td><td>29.20</td></tr>
  <tr><td>30d Support</td><td>22.28</td></tr>
  <tr><td>Buy the dip?</td><td>no</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>down</td></tr>
  <tr><td>3mo</td><td>middle</td></tr>
  <tr><td>1yr</td><td>near-bottom</td></tr>
  <tr><td>5yr</td><td>bottom</td></tr>
  <tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>NewsAPI: business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for MRNA...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting MRNA prices from massive.com... (https://api.massive.com/v2/aggs/ticker/MRNA/range/1/day/2020-10-26/2025-11-24?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/MRNA/2025-11-21?apiKey=%2A%2A%2A
  Massive open-close: response 200 from https://api.massive.com/v1/open-close/MRNA/2025-11-21?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/MRNA/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/MRNA/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/MRNA?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/MRNA?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/MRNA?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/MRNA?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/MRNA?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/MRNA?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/MRNA.svg
  Massive related companies: GET https://api.massive.com/v1/related-companies/MRNA?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/MRNA?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 10 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=MRNA&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=MRNA&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=MRNA&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=MRNA&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; MRNA core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; MRNA product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; MRNA business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; MRNA profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; MRNA earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; MRNA profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; MRNA target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; MRNA market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; MRNA market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; MRNA competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; MRNA market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; MRNA competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; MRNA rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; MRNA tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; MRNA rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 1 result(s)
    newsapi search -&gt; MRNA tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    newsapi search -&gt; MRNA latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 2 result(s)
    google_custom_search search -&gt; MRNA latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; MRNA tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 5 result(s)
    google_custom_search search -&gt; MRNA tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-24T01:42:41.098728+00:00">2025-11-24 01:42 UTC</time> (runtime 50.40s)

![Moderna, Inc. Common Stock logo](https://ryness.github.io/stonks/assets/logos/MRNA.svg)


## 0. Entry Radar

0.1. **Long Entry?:** no — at a 1yr near-bottom and 5yr bottom with a 7d downtrend per quick facts; macro froth visibility is limited in the provided data, and shares sit below the 20-DMA 25.03/EMA 25.70/SMA 25.87 and under 26.20 resistance, hovering just above 22.28 support

## 1. The Biz

1.1. **Activities:** Moderna is a commercial-stage biotech built around an mRNA platform, validated by its COVID-19 vaccine authorized in December 2020. It develops and commercializes mRNA-based vaccines and therapeutics, with 35 clinical-stage candidates as of August 2025. Programs span infectious diseases, oncology, cardiovascular disease, and rare genetic disorders.

1.2. **Profitable?:** No — it is currently unprofitable with -$3.12B in the last quarter, a -139.6% profit margin, and negative free cash flow, and no timeline to profitability is provided.

1.3. **Customer & Markets:** unknown

1.4. **Competition:** Primary competitors include Pfizer (PFE), Novavax (NVAX), Johnson & Johnson (JNJ), Merck (MRK), CureVac (CVAC), and Regeneron (REGN). Moderna is a commercial-stage mRNA leader with a broad pipeline validated by its COVID-19 vaccine, though the data does not quantify market rank.

## 2. Recent

2.1. **7d Trend?:** down — fell from a local high of 25.06 toward support at 22.28 and closed at 23.72

2.2. **7d Buy/Sell Points?:** Buy near 22.28–24.18 (support and suggested buy zone); sell near 25.06–26.20 (local high and resistance).

2.3.1. **7d Volume:** med

2.3.2. **7d Volatility:** high

## 3. Longterm

3.1. **Stability?:** Moderna was founded in 2010 and IPO’d in 2018, making it a well-established public biotech. Its mRNA platform was validated with a U.S.-authorized COVID-19 vaccine, indicating commercial execution. However, recent financials show sustained losses (net income sum -$3.116B), negative operating cash flow (-$1.978B), and negative free cash flow, which weigh on financial resilience. The stock sits near its 1yr near-bottom and 5yr bottom, reflecting elevated risk. Overall, it is not a fly-by-night startup but carries typical biotech volatility and cash burn.

3.2. **Innovating?:** Yes — it is advancing 35 mRNA candidates across infectious disease, oncology, cardiovascular, and rare diseases, though it recently discontinued its CMV program after a Phase 3 miss.

## 4. Context

4.1. **News:** Moderna discontinued its CMV vaccine program after a Phase 3 failure to prevent infection, which likely pressured sentiment. Separately, coverage highlighted potential long-term upside tied to its mRNA platform and cancer vaccine mRNA-4157. Sector peers posted oncology progress (e.g., Immatics data and CytomX presentations), adding broader context to modality momentum. Quick facts indicate no clear ‘buy the rumor’ or ‘sell the news’ setup recently, suggesting limited tradable catalysts per the adage.

4.2. **Tarrifs:** unknown

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>$-3.12B</td></tr>
<tr><td>Price</td><td>23.72</td></tr>
<tr><td>7d Resistance</td><td>26.20</td></tr>
<tr><td>7d Support</td><td>22.28</td></tr>
<tr><td>30d Resistance</td><td>29.20</td></tr>
<tr><td>30d Support</td><td>22.28</td></tr>
<tr><td>Buy the dip?</td><td>no</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>down</td></tr>
<tr><td>3mo</td><td>middle</td></tr>
<tr><td>1yr</td><td>near-bottom</td></tr>
<tr><td>5yr</td><td>bottom</td></tr>
<tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>NewsAPI: business model, profit outlook, market expansion, competitive landscape, rumor, tariff, latest news, tariffs</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for MRNA...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting MRNA prices from massive.com... (https://api.massive.com/v2/aggs/ticker/MRNA/range/1/day/2020-10-26/2025-11-24?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/MRNA/2025-11-21?apiKey=%2A%2A%2A
Massive open-close: response 200 from https://api.massive.com/v1/open-close/MRNA/2025-11-21?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/MRNA/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/MRNA/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/MRNA?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/MRNA?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 429 from https://api.massive.com/v1/indicators/macd/MRNA?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/MRNA?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/MRNA?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/MRNA?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/MRNA?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive logo: using cached asset /home/runner/work/stonks/stonks/assets/logos/MRNA.svg
Massive related companies: GET https://api.massive.com/v1/related-companies/MRNA?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/MRNA?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 10 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=MRNA&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=MRNA&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=MRNA&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=MRNA&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; MRNA core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; MRNA product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; MRNA business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; MRNA profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; MRNA earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; MRNA profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; MRNA target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; MRNA market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; MRNA market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; MRNA competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; MRNA market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; MRNA competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; MRNA rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; MRNA tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; MRNA rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 1 result(s)
  newsapi search -&gt; MRNA tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  newsapi search -&gt; MRNA latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 2 result(s)
  google_custom_search search -&gt; MRNA latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; MRNA tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=MRNA+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 5 result(s)
  google_custom_search search -&gt; MRNA tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=MRNA+tariff+impact&amp;num=5
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
