---
title: "List Recipients"
source: https://resend.com/docs/api-reference/broadcasts/list-broadcast-recipients
path: docs/api-reference/broadcasts/list-broadcast-recipients
---

GET /broadcasts/:broadcast_id/recipients
Retrieve the recipients of a broadcast for a given event type.

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
    npm install resend@6.19.0-preview-headless-dashboard.1
    ```
  </CodeGroup>
</Warning>

Retrieve the recipients of a broadcast, filtered by a single event `type` (for
example everyone who `opened`, `clicked`, or `bounced`). Results are paginated
with cursors. See [Pagination](/docs/api-reference/pagination) for how `after` and
`before` work.

<Info>
  Responses are cached for up to 15 minutes, so requesting the same page again
  may return slightly stale data within that window.
</Info>

## Path Parameters

<ResendParamField type="string">
  The broadcast ID.
</ResendParamField>

## Query Parameters

<ResendParamField type="string">
  The event to filter recipients by. One of `sent`, `delivered`, `opened`,
  `clicked`, `bounced`, `complained`, `unsubscribed`, or `suppressed`.
</ResendParamField>

<ResendParamField type="number">
  Number of recipients to return. Between `1` and `100`. Defaults to `20`.
</ResendParamField>

<ResendParamField type="string">
  Cursor to fetch the page after this recipient. Cannot be used with `before`.
</ResendParamField>

<ResendParamField type="string">
  Cursor to fetch the page before this recipient. Cannot be used with `after`.
</ResendParamField>

<ResendParamField type="string">
  Filter recipients whose email contains this value.
</ResendParamField>

<ResendParamField type="string">
  Filter by bounce classification. One of `permanent`, `transient`, or
  `undetermined`. Can only be used with `type=bounced`.
</ResendParamField>

## Response Fields

<ParamField type="string">
  Always `list`.
</ParamField>

<ParamField type="boolean">
  Whether more recipients exist beyond this page.
</ParamField>

<ParamField type="array">
  The recipients matching the requested `type`.

  <Expandable title="properties">
    <ParamField type="string">
      An opaque cursor for this row, used only for pagination. It does not
      identify any entity in Resend. Use `contact_id` to reference the contact.
    </ParamField>

    <ParamField type="string | null">
      The matching contact's ID. `null` when the recipient's email no longer
      maps to a contact.
    </ParamField>

    <ParamField type="string">
      The recipient's email address.
    </ParamField>

    <ParamField type="number">
      How many times the recipient triggered the event. Only returned for
      `type=opened` and `type=clicked`.
    </ParamField>

    <ParamField type="string | null">
      The bounce classification: `permanent`, `transient`, or `undetermined`.
      Only returned for `type=bounced`.
    </ParamField>

    <ParamField type="array">
      The links this recipient clicked. Only returned for `type=clicked`.

      <Expandable title="properties">
        <ParamField type="string">
          The URL that was clicked.
        </ParamField>

        <ParamField type="number">
          How many times the recipient clicked this link.
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.broadcasts.recipients(
    '559ac32e-9ef5-46fb-82a1-b76b840c0f7b',
    { type: 'clicked', limit: 20 },
  );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X GET 'https://api.resend.com/broadcasts/559ac32e-9ef5-46fb-82a1-b76b840c0f7b/recipients?type=clicked&limit=20' \
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
        "contact_id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
        "email": "carter@example.com",
        "count": 3,
        "clicked_links": [
          { "url": "https://resend.com/pricing", "clicks": 2 },
          { "url": "https://resend.com/docs", "clicks": 1 }
        ]
      },
      {
        "id": "b2Zmc2V0OjE",
        "contact_id": null,
        "email": "dana@example.com",
        "count": 1,
        "clicked_links": [{ "url": "https://resend.com/pricing", "clicks": 1 }]
      }
    ]
  }
  ```
</ResponseExample>
