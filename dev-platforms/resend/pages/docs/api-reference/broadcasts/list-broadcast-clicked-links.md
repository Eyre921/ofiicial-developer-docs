---
title: "List Clicked Links"
source: https://resend.com/docs/api-reference/broadcasts/list-broadcast-clicked-links
path: docs/api-reference/broadcasts/list-broadcast-clicked-links
---

GET /broadcasts/:broadcast_id/clicked-links
Retrieve the links clicked in a broadcast.

<Warning>
  Broadcast metrics and recipients are currently in private beta and only
  available to a limited number of users. APIs might change before it is generally available.
  [Get in touch](https://resend.com/contact) if you're interested in testing
  this feature.

  <span />

  Once you have access, upgrade your Resend SDK to use the methods on this
  page:

  <CodeGroup>
    ```bash Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install resend@6.19.0-preview-headless-dashboard.3
    ```
  </CodeGroup>
</Warning>

Retrieve every link clicked in a broadcast, ranked by total clicks. Results are
paginated with cursors. See [Pagination](/docs/api-reference/pagination) for how
`after` and `before` work.

<Info>
  Responses are cached for up to 15 minutes, so requesting the same page again
  may return slightly stale data within that window.
</Info>

## Path Parameters

<ResendParamField type="string">
  The broadcast ID.
</ResendParamField>

## Query Parameters

<ResendParamField type="number">
  Number of links to return. Between `1` and `100`. Defaults to `20`.
</ResendParamField>

<ResendParamField type="string">
  Cursor to fetch the page after this link. Cannot be used with `before`.
</ResendParamField>

<ResendParamField type="string">
  Cursor to fetch the page before this link. Cannot be used with `after`.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `list`.
</ParamField>

<ParamField type="boolean">
  Whether more links exist beyond this page.
</ParamField>

<ParamField type="array">
  The clicked links, ordered by total clicks, descending.

  <Expandable title="properties">
    <ParamField type="string">
      An opaque cursor for this row, used only for pagination. It does not
      identify any entity in Resend.
    </ParamField>

    <ParamField type="string">
      The URL that was clicked.
    </ParamField>

    <ParamField type="number">
      Total clicks on this link, including repeat clicks by the same
      recipient.
    </ParamField>

    <ParamField type="number">
      The number of distinct recipients who clicked this link.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/broadcasts/559ac32e-9ef5-46fb-82a1-b76b840c0f7b/clicked-links?limit=20' \
       -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": true,
    "data": [
      {
        "id": "b2Zmc2V0OjA",
        "url": "https://resend.com/pricing",
        "clicks": 42,
        "unique_clicks": 30
      },
      {
        "id": "b2Zmc2V0OjE",
        "url": "https://resend.com/docs",
        "clicks": 17,
        "unique_clicks": 15
      }
    ]
  }
  ```
</ResponseExample>
