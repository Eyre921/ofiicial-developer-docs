---
title: "Usage and Billing"
source: https://docs.x.com/x-api/fundamentals/post-cap
path: x-api/fundamentals/post-cap
---

X API v2 uses pay-per-usage pricing. You're charged based on actual API consumption, tracked at the app level. Pay-per-usage plans are subject to a monthly.

X API v2 uses **pay-per-usage** pricing. You're charged based on actual API consumption, tracked at the app level.

***

## How billing works

| Concept                 | Description                                           |
| :---------------------- | :---------------------------------------------------- |
| **Credit-based**        | Purchase credits upfront, deducted as you use the API |
| **Per-request pricing** | Different endpoints have different costs              |
| **Real-time tracking**  | Monitor usage in the Developer Console                |

<Note>
  Pay-per-usage plans are subject to a monthly cap of 3 million Post reads. If you need higher volume, consider an [Enterprise plan](/forms/enterprise-api-interest).
</Note>

***

## Tracked endpoints

Posts retrieved from these endpoints count toward usage:

| Category        | Endpoints                                                                                                                     |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Post lookup** | [GET /2/tweets](/x-api/posts/lookup/introduction)                                                                             |
| **Search**      | [Recent search](/x-api/posts/search/introduction), [Full-archive search](/x-api/posts/search/introduction)                    |
| **Streaming**   | [Filtered stream](/x-api/posts/filtered-stream/introduction), [Filtered stream webhooks](/x-api/webhooks/stream/introduction) |
| **Timelines**   | [User posts](/x-api/posts/timelines/introduction), [User mentions](/x-api/posts/timelines/introduction)                       |
| **Engagement**  | [Liked posts](/x-api/posts/likes/introduction), [Bookmarks](/x-api/posts/bookmarks/introduction)                              |
| **Lists**       | [List posts](/x-api/lists/list-tweets/introduction)                                                                           |
| **Spaces**      | [Spaces lookup](/x-api/spaces/lookup/introduction)                                                                            |

***

## Deduplication

<Note>
  **Daily deduplication**: If the same post is returned from multiple queries within a day, it only counts once for billing.
</Note>

This means:

* Retrieving the same post multiple times in one day = 1 charge
* Retrieving a post again the next day = 1 additional charge
* Different posts in the same request = each counts separately

***

## Monitoring usage

Track your usage in the [Developer Console](https://console.x.com):

| Metric             | Description                           |
| :----------------- | :------------------------------------ |
| **Total usage**    | Posts retrieved in the billing period |
| **By endpoint**    | Breakdown by endpoint type            |
| **By app**         | Usage per developer app               |
| **Cost tracking**  | Real-time cost calculations           |
| **Credit balance** | Remaining prepaid credits             |

***

## Managing costs

<CardGroup>
  <Card title="Set budgets" icon="wallet">
    Configure spending limits in the Developer Console.
  </Card>

  <Card title="Monitor alerts" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bell.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=5e0b3dcfbb39ba3d4619931d7cd927d1">
    Get notified before hitting budget thresholds.
  </Card>

  <Card title="Use caching" icon="database">
    Cache responses to avoid re-fetching the same posts.
  </Card>

  <Card title="Optimize queries" icon="https://mintcdn.com/x-preview/szd6PKNMlRQoyyAo/icons/xds/icon-filter.svg?fit=max&auto=format&n=szd6PKNMlRQoyyAo&q=85&s=5d59aff402c1f2aeae0e9e44bb23400e">
    Use precise filters to retrieve only needed posts.
  </Card>
</CardGroup>

***

## Pricing details

For current pricing per endpoint and operation, visit the [Developer Console](https://console.x.com).

Pricing may vary by:

* Endpoint type (search vs. lookup vs. stream)
* Operation (read vs. write)
* Data scope (recent vs. full-archive)

***

## Enterprise options

For high-volume needs with custom pricing:

* Dedicated support
* Volume discounts
* Custom rate limits
* Complete data access

<CardGroup>
  <Card title="Contact Enterprise Sales" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bank.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=6dd9ad48fa88936abb112b49e022abff" href="/enterprise/forms/enterprise-api-interest">
    Discuss custom solutions for your needs.
  </Card>
</CardGroup>

***

## FAQs

<Accordion title="What happens if I run out of credits?">
  API requests will fail until you purchase more credits. Set up balance alerts to avoid interruption.
</Accordion>

<Accordion title="Are there monthly minimums?">
  No. Pay only for what you use. You can have months with zero usage and zero cost.
</Accordion>

<Accordion title="How is streaming billed?">
  Each unique post delivered through filtered stream counts toward usage, subject to daily deduplication.
</Accordion>

<Accordion title="Do failed requests count?">
  No. Only successful responses that return data are billed.
</Accordion>

***

## Next steps

<CardGroup>
  <Card title="Developer Console" icon="grid-2" href="https://console.x.com">
    View pricing and purchase credits.
  </Card>

  <Card title="Rate limits" icon="gauge-high" href="/x-api/fundamentals/rate-limits">
    Understand request limits (separate from billing).
  </Card>
</CardGroup>
