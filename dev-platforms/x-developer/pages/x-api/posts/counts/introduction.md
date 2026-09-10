---
title: "Post Counts"
source: https://docs.x.com/x-api/posts/counts/introduction
path: x-api/posts/counts/introduction
---

The Post counts endpoints return the volume of Posts matching a query over time, without returning. Reference for the X API v2 standard tier covering counts.

The Post counts endpoints return the volume of Posts matching a query over time, without returning the Posts themselves. Use these endpoints to analyze trends, understand conversation size, and refine queries before searching.

## Overview

<CardGroup>
  <Card title="Volume analysis" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bar-chart.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=e2a41caa858b122416f0005a55a8f143">
    Build trendlines and visualizations showing Post volume over time
  </Card>

  <Card title="Query refinement" icon="https://mintcdn.com/x-preview/szd6PKNMlRQoyyAo/icons/xds/icon-filter.svg?fit=max&auto=format&n=szd6PKNMlRQoyyAo&q=85&s=5d59aff402c1f2aeae0e9e44bb23400e">
    Estimate result size before running full search queries
  </Card>

  <Card title="Event detection" icon="calendar">
    Identify when conversations peaked around events
  </Card>

  <Card title="Efficient research" icon="gauge-high">
    Understand conversation scale without retrieving all Posts
  </Card>
</CardGroup>

***

## Endpoints

| Endpoint                                                                | Description                       | Access                  |
| :---------------------------------------------------------------------- | :-------------------------------- | :---------------------- |
| GET [`/2/tweets/counts/recent`](/x-api/posts/get-count-of-recent-posts) | Count Posts from last 7 days      | All developers          |
| GET [`/2/tweets/counts/all`](/x-api/posts/get-count-of-all-posts)       | Count Posts from complete archive | Pay-per-use, Enterprise |

***

## Granularity options

Specify how counts are grouped using the `granularity` parameter:

| Granularity | Description               | Use case             |
| :---------- | :------------------------ | :------------------- |
| `minute`    | Counts per minute         | Real-time monitoring |
| `hour`      | Counts per hour (default) | Daily analysis       |
| `day`       | Counts per day            | Long-term trends     |

***

## Recent counts

Count Posts from the **last 7 days**. Available to all developers.

### Features

* Counts grouped by minute, hour, or day
* Same query operators as recent search
* 512-character query length

### Example response

```json theme={null}
{
  "data": [
    { "start": "2024-01-15T00:00:00.000Z", "end": "2024-01-15T01:00:00.000Z", "tweet_count": 1523 },
    { "start": "2024-01-15T01:00:00.000Z", "end": "2024-01-15T02:00:00.000Z", "tweet_count": 1247 },
    { "start": "2024-01-15T02:00:00.000Z", "end": "2024-01-15T03:00:00.000Z", "tweet_count": 892 }
  ],
  "meta": {
    "total_tweet_count": 3662
  }
}
```

<CardGroup>
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/posts/counts/quickstart/recent-tweet-counts">
    Make your first recent counts request
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/posts/get-count-of-recent-posts">
    Full endpoint documentation
  </Card>
</CardGroup>

***

## Full-archive counts

Count Posts from the **complete archive** back to 2006.

<Note>
  Full-archive counts are available to pay-per-use and Enterprise customers.
</Note>

### Features

* Count historical Posts from any time period
* All query operators available
* 1,024-character query length (4,096 for Enterprise)

### Pagination

Results paginate at 31 days per response:

* **Day granularity**: 31 days per page
* **Hour granularity**: 744 hours (31 days) per page
* **Minute granularity**: 44,640 minutes (31 days) per page

<CardGroup>
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/posts/counts/quickstart/full-archive-tweet-counts">
    Make your first full-archive counts request
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/posts/get-count-of-all-posts">
    Full endpoint documentation
  </Card>
</CardGroup>

***

## Query operators

Post counts use the same query syntax as search endpoints:

```
python lang:en -is:retweet
```

<Card title="Build a query" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-search.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=8c11ad89387b7c09ced1553d5c232834" href="/x-api/posts/counts/integrate/build-a-query">
  Learn query syntax and operators
</Card>

***

## Important notes

<Note>
  **Counts vs search results**

  Counts may not exactly match search results. Search endpoints apply additional compliance filtering that counts endpoints do not perform.
</Note>

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * Your App's [Bearer Token](/resources/fundamentals/authentication)
</Note>

<CardGroup>
  <Card title="Recent counts quickstart" icon="clock" href="/x-api/posts/counts/quickstart/recent-tweet-counts">
    Count Posts from the last 7 days
  </Card>

  <Card title="Full-archive quickstart" icon="vault" href="/x-api/posts/counts/quickstart/full-archive-tweet-counts">
    Count historical Posts
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/posts/counts/integrate/overview">
    Key concepts and best practices
  </Card>

  <Card title="Sample code" icon="github" href="https://github.com/xdevplatform/Twitter-API-v2-sample-code">
    Working code examples
  </Card>
</CardGroup>
