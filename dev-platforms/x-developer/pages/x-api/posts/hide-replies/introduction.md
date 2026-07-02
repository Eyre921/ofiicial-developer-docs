---
title: "Hide Replies"
source: https://docs.x.com/x-api/posts/hide-replies/introduction
path: x-api/posts/hide-replies/introduction
---

Use the X API v2 Hide Replies endpoint to hide or unhide replies to Posts authored by the authenticated user and moderate conversations on X.

The Hide Replies endpoint lets you hide or unhide replies to Posts authored by the authenticated user. Hidden replies are still accessible but require an extra click to view.

## Overview

<CardGroup>
  <Card title="Hide reply" icon="eye-slash">
    Hide a reply to your Post
  </Card>

  <Card title="Unhide reply" icon="eye">
    Unhide a previously hidden reply
  </Card>

  <Card title="Conversation control" icon="comments">
    Moderate discussions on your Posts
  </Card>
</CardGroup>

***

## Endpoint

| Method | Endpoint                                                | Description            |
| :----- | :------------------------------------------------------ | :--------------------- |
| PUT    | [`/2/tweets/:tweet_id/hidden`](/x-api/posts/hide-reply) | Hide or unhide a reply |

***

## How it works

Send a PUT request with `hidden: true` to hide a reply, or `hidden: false` to unhide it:

```json theme={null}
{
  "hidden": true
}
```

***

## Example: Hide a reply

```bash theme={null}
curl -X PUT "https://api.x.com/2/tweets/1234567890/hidden" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"hidden": true}'
```

## Example response

```json theme={null}
{
  "data": {
    "hidden": true
  }
}
```

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * User Access Tokens via [OAuth 2.0 PKCE](/resources/fundamentals/authentication#oauth-2-0-authorization-code-flow-with-pkce-2)
</Note>

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/x-api/posts/hide-replies/quickstart">
    Hide your first reply
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/posts/hide-replies">
    Full endpoint documentation
  </Card>
</CardGroup>
