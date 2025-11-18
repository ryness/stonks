---
layout: default
title: "GLD Stock Report"
ticker: "GLD"
date: 2025-11-18
generated_at: 2025-11-18T01:28:45.923066+00:00
runtime_seconds: 106.47
raw_markdown: |
  **Generated:** <time class="js-local-time" datetime="2025-11-18T01:28:45.923066+00:00">2025-11-18 01:28 UTC</time> (runtime 1m 46s)
  
  ## 0. Entry Radar
  
  0.1. **Long Entry?:** maybe — 1yr and 5yr positioning are near-peak, suggesting limited historical discount; macro froth visibility is limited in the supplied data; price is around the 20DMA (372.51) and just above 7d support (366.42) but below 7d resistance/sell zone (388.18).
  
  ## 1. The Biz
  
  1.1. **Activities:** SPDR Gold Trust (SPDR Gold Shares) holds physical gold bars, issuing and redeeming Baskets in exchange for deposits and redemptions of gold. Its objective is for the shares to reflect the price performance of gold bullion, less trust expenses. The Sponsor positions the shares as a cost-effective way for investors to gain gold exposure.
  
  1.2. **Profitable?:** unknown
  
  1.3. **Customer & Markets:** Primary customers are investors seeking exposure to the price of gold bullion. The market served is investment exposure to physical gold via exchange-traded shares that track bullion, less expenses.
  
  1.4. **Competition:** It competes with other gold-focused ETFs; sponsor materials note GLD is the largest gold ETF and the first US-listed ETF backed by a physical asset, though lower-cost competitors have emerged. Thus, it ranks as a leading fund among gold ETFs.
  
  ## 2. Recent
  
  2.1. **7d Trend?:** up — trend labeled an uptrend with price moving from a 7d/local low of 361.39 toward a local high of 388.18 and hovering near the 20DMA.
  
  2.2. **7d Buy/Sell Points?:** Buying near 361.39 (7d/local low) and selling near 388.18 (7d resistance/local high) were favorable levels. The 7d support at 366.42 also marked a constructive buy-on-dips area.
  
  2.3.1. **7d Volume:** med
  
  2.3.2. **7d Volatility:** low
  
  ## 3. Longterm
  
  3.1. **Stability?:** This is a physically backed trust that holds gold bars and processes creations/redemptions in Baskets, anchoring it to bullion rather than operating cash flows. That structure points to an institutional vehicle rather than a fly-by-night entity. While detailed financial statements are not provided here, its value is tied to gold holdings, and recent volatility is labeled low with medium volume. Overall, it presents as a stable physically backed product whose risk mirrors gold price movements.
  
  3.2. **Innovating?:** It is a passive vehicle designed to track gold bullion less expenses, with no evidence in the provided data of innovation beyond that mandate. Growth, if any, would stem from gold prices and assets tracking behavior rather than new products.
  
  ## 4. Context
  
  4.1. **News:** Recent headlines tie GLD’s setup to macro catalysts: ETF strategies for 2H24 around elections and rate cuts, market caution ahead of PCE, and notes of gold rebounding while chipmakers struggled. Zacks highlighted potential for gold strength on geopolitical tensions, rate-cut odds, and central bank buying, with ETFs like GLD in focus. Such narratives can invite ‘buy the rumor’ behavior into inflation prints or rate decisions, suggesting caution on chasing follow-through after news. Quick facts here also flag ‘Buy the rumor? no’ and ‘Sell the news? no,’ implying no strong rumor/news skew in the supplied context.
  
  4.2. **Tarrifs:** Reports indicate tariff threats have supported gold and GLD, with an etf.com piece noting GLD rising as tariffs loomed and NPR citing tariffs making gold ‘hotter.’ In short, tariff uncertainty has tended to be a positive driver for GLD via safe-haven demand.
  
  ## 5. QuickRef
  
  <div class="quickref-table">
  <table>
  <thead><tr><th>Metric</th><th>Answer</th></tr></thead>
  <tbody>
  <tr><td>Last Q4</td><td>unknown</td></tr>
  <tr><td>Price</td><td>371.65</td></tr>
  <tr><td>7d Resistance</td><td>388.18</td></tr>
  <tr><td>7d Support</td><td>366.42</td></tr>
  <tr><td>30d Resistance</td><td>403.30</td></tr>
  <tr><td>30d Support</td><td>360.12</td></tr>
  <tr><td>Buy the dip?</td><td>yes</td></tr>
  <tr><td>Buy the rumor?</td><td>no</td></tr>
  <tr><td>Sell the news?</td><td>no</td></tr>
  <tr><td>7d Trend:</td><td>up</td></tr>
  <tr><td>3mo</td><td>middle</td></tr>
  <tr><td>1yr</td><td>near-peak</td></tr>
  <tr><td>5yr</td><td>near-peak</td></tr>
  <tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
  </tbody></table>
  </div>
  
  
  <div class="sources-list">
  <strong>Sources</strong>
  <ul>
  <li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
  <li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
  <li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
  <li>NewsAPI: business model, profit outlook, tariff, latest news, tariffs</li>
  <li>The Guardian: market expansion, competitive landscape, rumor</li>
  </ul>
  </div>
  
  
  <details class="cli-log">
  <summary>Show generation log^</summary>
  <pre><code>
  Gathering context for GLD...
  Gathering market data...
  Checking massive.com quota and fetching price history...
  Requesting GLD prices from massive.com... (https://api.massive.com/v2/aggs/ticker/GLD/range/1/day/2020-10-20/2025-11-18?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
  massive.com request failed (massive.com returned no price data); switching to yfinance...
  Requesting prices from yfinance fallback...
  Price data acquired from yfinance.
  Massive open-close: GET https://api.massive.com/v1/open-close/GLD/2025-11-17?apiKey=%2A%2A%2A
  Massive open-close: response 403 from https://api.massive.com/v1/open-close/GLD/2025-11-17?apiKey=&lt;redacted&gt;
  Massive previous close: GET https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=%2A%2A%2A
  Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive SMA: GET https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive EMA: GET https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive MACD: GET https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive MACD: response 200 from https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Massive RSI: GET https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
  Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
  Calculating technical snapshot...
  Fetching company profile (massive.com)...
  Massive profile: GET https://api.massive.com/v3/reference/tickers/GLD?apiKey=%2A%2A%2A
  Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/GLD?apiKey=&lt;redacted&gt;
  Massive profile: company metadata retrieved successfully.
  Massive related companies: GET https://api.massive.com/v1/related-companies/GLD?apiKey=%2A%2A%2A
  Massive related companies: response 200 from https://api.massive.com/v1/related-companies/GLD?apiKey=&lt;redacted&gt;
  Massive related companies: retrieved 0 entries.
  Fetching company fundamentals...
  Retrieving earnings calendar...
  Massive earnings: attempting request with key 2QGS***XN
  Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=%2A%2A%2A
  Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=&lt;redacted&gt;
  Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
  Assembling quick facts...
  Collecting latest headlines (massive.com)...
  Massive news: GET https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
  Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
  Massive news: collected 5 articles.
    massive.com returned 5 headlines
  Running supplementary searches...
    google_custom_search search -&gt; GLD core business (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+core+business&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+product+portfolio&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD business model (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 2 result(s)
    google_custom_search search -&gt; GLD profitability (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+profitability&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+earnings+trend&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD profit outlook (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 2 result(s)
    google_custom_search search -&gt; GLD target customers (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+target+customers&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD market segments (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+segments&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD market expansion (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=GLD+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=GLD+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; GLD competitors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+competitors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD market share (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+share&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD competitive landscape (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=GLD+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=GLD+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    google_custom_search search -&gt; GLD rumors (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+rumors&amp;num=5
      google_custom_search: 5 result(s)
    google_custom_search search -&gt; GLD tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariffs+news&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD rumor (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
  GNews search: GET https://gnews.io/api/v4/search?q=GLD+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
  Guardian search: GET https://content.guardianapis.com/search?q=GLD+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
      newsapi: 0 result(s)
      gnews: 0 result(s)
      guardian: 5 result(s)
    newsapi search -&gt; GLD tariff (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 4 result(s)
    newsapi search -&gt; GLD latest news (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 1 result(s)
    google_custom_search search -&gt; GLD latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+latest+rumor&amp;num=5
      google_custom_search: 5 result(s)
    newsapi search -&gt; GLD tariffs (priority: newsapi, gnews, guardian)
  NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
      newsapi: 2 result(s)
    google_custom_search search -&gt; GLD tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
  Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariff+impact&amp;num=5
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

**Generated:** <time class="js-local-time" datetime="2025-11-18T01:28:45.923066+00:00">2025-11-18 01:28 UTC</time> (runtime 1m 46s)

## 0. Entry Radar

0.1. **Long Entry?:** maybe — 1yr and 5yr positioning are near-peak, suggesting limited historical discount; macro froth visibility is limited in the supplied data; price is around the 20DMA (372.51) and just above 7d support (366.42) but below 7d resistance/sell zone (388.18).

## 1. The Biz

1.1. **Activities:** SPDR Gold Trust (SPDR Gold Shares) holds physical gold bars, issuing and redeeming Baskets in exchange for deposits and redemptions of gold. Its objective is for the shares to reflect the price performance of gold bullion, less trust expenses. The Sponsor positions the shares as a cost-effective way for investors to gain gold exposure.

1.2. **Profitable?:** unknown

1.3. **Customer & Markets:** Primary customers are investors seeking exposure to the price of gold bullion. The market served is investment exposure to physical gold via exchange-traded shares that track bullion, less expenses.

1.4. **Competition:** It competes with other gold-focused ETFs; sponsor materials note GLD is the largest gold ETF and the first US-listed ETF backed by a physical asset, though lower-cost competitors have emerged. Thus, it ranks as a leading fund among gold ETFs.

## 2. Recent

2.1. **7d Trend?:** up — trend labeled an uptrend with price moving from a 7d/local low of 361.39 toward a local high of 388.18 and hovering near the 20DMA.

2.2. **7d Buy/Sell Points?:** Buying near 361.39 (7d/local low) and selling near 388.18 (7d resistance/local high) were favorable levels. The 7d support at 366.42 also marked a constructive buy-on-dips area.

2.3.1. **7d Volume:** med

2.3.2. **7d Volatility:** low

## 3. Longterm

3.1. **Stability?:** This is a physically backed trust that holds gold bars and processes creations/redemptions in Baskets, anchoring it to bullion rather than operating cash flows. That structure points to an institutional vehicle rather than a fly-by-night entity. While detailed financial statements are not provided here, its value is tied to gold holdings, and recent volatility is labeled low with medium volume. Overall, it presents as a stable physically backed product whose risk mirrors gold price movements.

3.2. **Innovating?:** It is a passive vehicle designed to track gold bullion less expenses, with no evidence in the provided data of innovation beyond that mandate. Growth, if any, would stem from gold prices and assets tracking behavior rather than new products.

## 4. Context

4.1. **News:** Recent headlines tie GLD’s setup to macro catalysts: ETF strategies for 2H24 around elections and rate cuts, market caution ahead of PCE, and notes of gold rebounding while chipmakers struggled. Zacks highlighted potential for gold strength on geopolitical tensions, rate-cut odds, and central bank buying, with ETFs like GLD in focus. Such narratives can invite ‘buy the rumor’ behavior into inflation prints or rate decisions, suggesting caution on chasing follow-through after news. Quick facts here also flag ‘Buy the rumor? no’ and ‘Sell the news? no,’ implying no strong rumor/news skew in the supplied context.

4.2. **Tarrifs:** Reports indicate tariff threats have supported gold and GLD, with an etf.com piece noting GLD rising as tariffs loomed and NPR citing tariffs making gold ‘hotter.’ In short, tariff uncertainty has tended to be a positive driver for GLD via safe-haven demand.

## 5. QuickRef

<div class="quickref-table">
<table>
<thead><tr><th>Metric</th><th>Answer</th></tr></thead>
<tbody>
<tr><td>Last Q4</td><td>unknown</td></tr>
<tr><td>Price</td><td>371.65</td></tr>
<tr><td>7d Resistance</td><td>388.18</td></tr>
<tr><td>7d Support</td><td>366.42</td></tr>
<tr><td>30d Resistance</td><td>403.30</td></tr>
<tr><td>30d Support</td><td>360.12</td></tr>
<tr><td>Buy the dip?</td><td>yes</td></tr>
<tr><td>Buy the rumor?</td><td>no</td></tr>
<tr><td>Sell the news?</td><td>no</td></tr>
<tr><td>7d Trend:</td><td>up</td></tr>
<tr><td>3mo</td><td>middle</td></tr>
<tr><td>1yr</td><td>near-peak</td></tr>
<tr><td>5yr</td><td>near-peak</td></tr>
<tr><td>Overbought/Sold?</td><td>in the middle</td></tr>
</tbody></table>
</div>


<div class="sources-list">
<strong>Sources</strong>
<ul>
<li>massive.com: company profile &amp; branding, technical indicators, headlines (5 items)</li>
<li>yfinance: prices &amp; technicals, fundamentals, earnings calendar</li>
<li>Google Custom Search: core business, product portfolio, profitability, earnings trend, target customers, market segments, competitors, market share, rumors, tariffs news, latest rumor, tariff impact</li>
<li>NewsAPI: business model, profit outlook, tariff, latest news, tariffs</li>
<li>The Guardian: market expansion, competitive landscape, rumor</li>
</ul>
</div>


<details class="cli-log">
<summary>Show generation log^</summary>
<pre><code>
Gathering context for GLD...
Gathering market data...
Checking massive.com quota and fetching price history...
Requesting GLD prices from massive.com... (https://api.massive.com/v2/aggs/ticker/GLD/range/1/day/2020-10-20/2025-11-18?adjusted=true&amp;sort=asc&amp;limit=5000&amp;apiKey=%2A%2A%2A)
massive.com request failed (massive.com returned no price data); switching to yfinance...
Requesting prices from yfinance fallback...
Price data acquired from yfinance.
Massive open-close: GET https://api.massive.com/v1/open-close/GLD/2025-11-17?apiKey=%2A%2A%2A
Massive open-close: response 403 from https://api.massive.com/v1/open-close/GLD/2025-11-17?apiKey=&lt;redacted&gt;
Massive previous close: GET https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=%2A%2A%2A
Massive previous close: response 200 from https://api.massive.com/v2/aggs/ticker/GLD/prev?adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive SMA: GET https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive SMA: response 200 from https://api.massive.com/v1/indicators/sma/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive EMA: GET https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive EMA: response 200 from https://api.massive.com/v1/indicators/ema/GLD?timespan=day&amp;window=50&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive MACD: GET https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive MACD: response 200 from https://api.massive.com/v1/indicators/macd/GLD?timespan=day&amp;series_type=close&amp;fast=12&amp;slow=26&amp;signal=9&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Massive RSI: GET https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=%2A%2A%2A
Massive RSI: response 429 from https://api.massive.com/v1/indicators/rsi/GLD?timespan=day&amp;window=14&amp;series_type=close&amp;order=desc&amp;limit=1&amp;adjusted=true&amp;apiKey=&lt;redacted&gt;
Calculating technical snapshot...
Fetching company profile (massive.com)...
Massive profile: GET https://api.massive.com/v3/reference/tickers/GLD?apiKey=%2A%2A%2A
Massive profile: response 200 from https://api.massive.com/v3/reference/tickers/GLD?apiKey=&lt;redacted&gt;
Massive profile: company metadata retrieved successfully.
Massive related companies: GET https://api.massive.com/v1/related-companies/GLD?apiKey=%2A%2A%2A
Massive related companies: response 200 from https://api.massive.com/v1/related-companies/GLD?apiKey=&lt;redacted&gt;
Massive related companies: retrieved 0 entries.
Fetching company fundamentals...
Retrieving earnings calendar...
Massive earnings: attempting request with key 2QGS***XN
Massive earnings: GET https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=%2A%2A%2A
Massive earnings: response 403 from https://api.massive.com/benzinga/v1/earnings?ticker=GLD&amp;limit=4&amp;apiKey=&lt;redacted&gt;
Massive earnings: access denied (403) - You are not entitled to this data. Please upgrade your plan at https://polygon.io/pricing
Assembling quick facts...
Collecting latest headlines (massive.com)...
Massive news: GET https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=%2A%2A%2A
Massive news: response 200 from https://api.massive.com/v2/reference/news?ticker=GLD&amp;limit=5&amp;order=desc&amp;apiKey=&lt;redacted&gt;
Massive news: collected 5 articles.
  massive.com returned 5 headlines
Running supplementary searches...
  google_custom_search search -&gt; GLD core business (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+core+business&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD product portfolio (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+product+portfolio&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD business model (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+business+model&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 2 result(s)
  google_custom_search search -&gt; GLD profitability (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+profitability&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD earnings trend (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+earnings+trend&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD profit outlook (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+profit+outlook&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 2 result(s)
  google_custom_search search -&gt; GLD target customers (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+target+customers&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD market segments (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+segments&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD market expansion (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+market+expansion&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=GLD+market+expansion&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=GLD+market+expansion&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; GLD competitors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+competitors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD market share (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+market+share&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD competitive landscape (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+competitive+landscape&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=GLD+competitive+landscape&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=GLD+competitive+landscape&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  google_custom_search search -&gt; GLD rumors (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+rumors&amp;num=5
    google_custom_search: 5 result(s)
  google_custom_search search -&gt; GLD tariffs news (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariffs+news&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD rumor (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+rumor&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
GNews search: GET https://gnews.io/api/v4/search?q=GLD+rumor&amp;lang=en&amp;max=5&amp;token=%2A%2A%2A
Guardian search: GET https://content.guardianapis.com/search?q=GLD+rumor&amp;api-key=%2A%2A%2A&amp;page-size=5&amp;order-by=newest&amp;show-fields=trailText
    newsapi: 0 result(s)
    gnews: 0 result(s)
    guardian: 5 result(s)
  newsapi search -&gt; GLD tariff (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariff&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 4 result(s)
  newsapi search -&gt; GLD latest news (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+latest+news&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 1 result(s)
  google_custom_search search -&gt; GLD latest rumor (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+latest+rumor&amp;num=5
    google_custom_search: 5 result(s)
  newsapi search -&gt; GLD tariffs (priority: newsapi, gnews, guardian)
NewsAPI search: GET https://newsapi.org/v2/everything?q=GLD+tariffs&amp;pageSize=5&amp;language=en&amp;sortBy=publishedAt&amp;apiKey=%2A%2A%2A
    newsapi: 2 result(s)
  google_custom_search search -&gt; GLD tariff impact (priority: google_custom_search, newsapi, gnews, guardian)
Google Custom Search: GET https://www.googleapis.com/customsearch/v1?key=%2A%2A%2A&amp;cx=46c4e3bbc6b31470f&amp;q=GLD+tariff+impact&amp;num=5
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
