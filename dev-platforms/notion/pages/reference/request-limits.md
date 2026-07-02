---
title: "Request limits"
source: https://developers.notion.com/reference/request-limits
path: reference/request-limits
---

To ensure a consistent developer experience for all API users, the Notion API is rate limited and basic size limits apply to request parameters.

## Rate limits

The Notion API enforces two rate limits:

* **Per connection** — an average of three requests per second, with some bursts beyond the average allowed.
* **Per workspace** — shared across all of the workspace's connections and scaled to the workspace's plan.

Requests that exceed either limit return a `"rate_limited"` error code and an HTTP 429 response, with `additional_data.rate_limit_reason` indicating which limit was exceeded (for example, `public_api_request_rate_limit` or `public_api_space_request_rate_limit`).

Connections should accommodate variable rate limits by handling HTTP 429 and 529 responses and respecting the Retry-After response [header value](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html), which is set as an integer number of seconds (in decimal). (A 529 carries the `"service_overload"` code and means Notion is temporarily overloaded; handle it the same way.) Requests made after waiting this minimum amount of time should no longer be rate limited.

Alternatively, rate limits can be accommodated by backing off (or slowing down) the speed of future requests. A common way to implement this is using one or several queues for pending requests, which can be consumed by sending requests as long as Notion does not respond with an HTTP 429 or 529.

<Warning>
  **Rate limits may change**

  In the future, Notion plans to adjust rate limits to balance for demand and reliability.
</Warning>

## Size limits

Notion limits the size of certain parameters, and the depth of children in requests. A requests that exceeds any of these limits will return `"validation_error"` error code (HTTP response status 400) and contain more specific details in the `"message"` property.

Connections should avoid sending requests beyond these limits proactively. It may be helpful to use test data in your own test suite which intentionally contains large parameters to verify that the errors are handled appropriately. For example, if the connection reads a URL from an external system to put into a Notion page property, the connection should have a plan to deal with URLs that are beyond the length limit of 2000 characters. The connection might choose to log the error, or send an alert to the user who set up the connection via an email, or some other action.

Note that in addition to the property limits below, payloads have a maximum size of 1000 block elements and 500KB overall.

### Limits for property values

| Property value type                                                                                   | Inner property        | Size limit        |
| :---------------------------------------------------------------------------------------------------- | :-------------------- | :---------------- |
| [Rich text object](/reference/rich-text)                                                              | `text.content`        | 2000 characters   |
| [Rich text object](/reference/rich-text)                                                              | `text.link.url`       | 2000 characters   |
| [Rich text object](/reference/rich-text)                                                              | `equation.expression` | 1000 characters   |
| Any array of all [block](/reference/block) types, including [rich text objects](/reference/rich-text) |                       | 100 elements      |
| Any URL                                                                                               |                       | 2000 characters   |
| Any email                                                                                             |                       | 200 characters    |
| Any phone number                                                                                      |                       | 200 characters    |
| Any multi-select                                                                                      |                       | 100 options       |
| Any relation                                                                                          |                       | 100 related pages |
| Any people                                                                                            |                       | 100 users         |

<Note>
  **Request size limits**

  These cap the size of a single request, not how much a property can hold. A relation property can contain far more than 100 related pages — the limit only governs how many you add or set in one request. Responses have separate limits; use [Retrieve a page property item](/reference/retrieve-a-page-property) to paginate through large values.
</Note>
