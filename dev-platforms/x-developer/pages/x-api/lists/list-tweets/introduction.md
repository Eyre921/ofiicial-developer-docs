---
title: "List Posts"
source: https://docs.x.com/x-api/lists/list-tweets/introduction
path: x-api/lists/list-tweets/introduction
---

The List Posts endpoint lets you retrieve Posts from a List's timeline. Reference for the X API v2 standard tier covering list tweets.

The List Posts endpoint lets you retrieve Posts from a List's timeline. Get the latest Posts from all members of a List.

## Overview

<CardGroup>
  <Card title="List timeline" icon="list">
    Get Posts from List members
  </Card>

  <Card title="Curated feed" icon="stream">
    Access your curated content feeds
  </Card>
</CardGroup>

***

## Endpoint

| Method | Endpoint                                             | Description           |
| :----- | :--------------------------------------------------- | :-------------------- |
| GET    | [`/2/lists/:id/tweets`](/x-api/lists/get-list-posts) | Get Posts from a List |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/lists/1234567890/tweets?\
tweet.fields=created_at,author_id,public_metrics&\
expansions=author_id&\
user.fields=username&\
max_results=100" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * Your App's [keys and tokens](/resources/fundamentals/authentication)
</Note>

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/x-api/lists/list-tweets/quickstart">
    Get Posts from a List
  </Card>

  <Card title="Integration guide" icon="book" href="/x-api/lists/list-tweets/integrate">
    Key concepts and best practices
  </Card>

  <Card title="List lookup" icon="list" href="/x-api/lists/list-lookup/introduction">
    Get List details
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/lists/get-list-posts">
    Full endpoint documentation
  </Card>
</CardGroup>
