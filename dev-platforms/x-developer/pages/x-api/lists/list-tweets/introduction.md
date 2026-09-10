---
title: "List Posts"
source: https://docs.x.com/x-api/lists/list-tweets/introduction
path: x-api/lists/list-tweets/introduction
---

The List Posts endpoint lets you retrieve Posts from a List's timeline. Reference for the X API v2 standard tier covering list tweets.

The List Posts endpoint lets you retrieve Posts from a List's timeline. Get the latest Posts from all members of a List.

## Overview

<CardGroup>
  <Card title="List timeline" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5">
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
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/lists/list-tweets/quickstart">
    Get Posts from a List
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/lists/list-tweets/integrate">
    Key concepts and best practices
  </Card>

  <Card title="List lookup" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5" href="/x-api/lists/list-lookup/introduction">
    Get List details
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/lists/get-list-posts">
    Full endpoint documentation
  </Card>
</CardGroup>
