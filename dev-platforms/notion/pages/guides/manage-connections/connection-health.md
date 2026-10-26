---
title: "Connection health"
source: https://developers.notion.com/guides/manage-connections/connection-health
path: guides/manage-connections/connection-health
---

See how many API requests a connection sent in the last 24 hours, how many failed, and why.

The **Health** tab shows a connection's API requests from the last 24 hours, including how many failed and why. It's available for internal and public connections.

To open it, go to the [Developer portal](https://app.notion.com/developers/connections), select a connection, and select **Health**. The data updates every hour. For a public connection, it includes requests from every workspace that installed the connection.

## What the Health tab shows

**Requests** and **Failed requests** show the totals for the last 24 hours. **Requests by hour** shows when the connection sent requests and which ones failed. **Endpoints** lists the endpoints the connection called, busiest first, with the number of failures for each.

When requests fail, **Failed requests by type** sorts them into blocked requests, client errors (4xx), rate-limit responses (429), and server errors (5xx). **Error codes** lists the `code` values from error responses. See [Status codes](/reference/status-codes) for what each code means. **Rate limits** shows which limits the connection reached. See [Request limits](/reference/request-limits) for how to handle each one.

The Health tab counts every failed request and a sample of successful requests. Numbers that include successful requests, such as **Requests** and the share of requests that failed, are estimates and start with `~`. When a connection has less traffic, the tab may not have enough data to show these estimates. Failed requests still show.

## Warnings

When a connection's recent requests need attention, a warning appears at the top of its page in the Developer portal. An icon also appears next to the connection in your list of connections.

| Warning | What to do |
| :- | :- |
| **High API error volume detected** | The connection received a lot of client errors. Check your logs for the failed requests and make sure they use a current API version. See [Status codes](/reference/status-codes) and [Versioning](/reference/versioning). |
| **High API rate-limit volume detected** | The connection received a lot of rate-limit responses. Wait for the `Retry-After` time before sending more requests. See [Retry rate-limited requests](/reference/request-limits#retry-rate-limited-requests). |
| **API requests blocked** | The connection's API access was restricted, so retrying won't help. If requests are still blocked, contact [Notion support](https://www.notion.com/help). |
