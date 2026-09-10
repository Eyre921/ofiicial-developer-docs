---
title: "List Lookup"
source: https://docs.x.com/x-api/lists/list-lookup/introduction
path: x-api/lists/list-lookup/introduction
---

The List lookup endpoints let you retrieve information about Lists. Reference for the X API v2 standard tier covering list lookup.

The List lookup endpoints let you retrieve information about Lists. Look up a specific List by ID or get all Lists owned by a user.

## Overview

<CardGroup>
  <Card title="By ID" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5">
    Get details for a specific List
  </Card>

  <Card title="By owner" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305">
    Get all Lists owned by a user
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                                   | Description               |
| :----- | :--------------------------------------------------------- | :------------------------ |
| GET    | [`/2/lists/:id`](/x-api/lists/get-list-by-id)              | Get List by ID            |
| GET    | [`/2/users/:id/owned_lists`](/x-api/users/get-owned-lists) | Get Lists owned by a user |

***

## Response fields

By default, the response includes `id` and `name`. Request additional fields:

| Field            | Description             |
| :--------------- | :---------------------- |
| `description`    | List description        |
| `owner_id`       | Owner's user ID         |
| `private`        | Whether List is private |
| `follower_count` | Number of followers     |
| `member_count`   | Number of members       |
| `created_at`     | List creation date      |

### Example request

```bash theme={null}
curl "https://api.x.com/2/lists/1234567890?\
list.fields=description,owner_id,member_count,follower_count" \
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
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/lists/list-lookup/quickstart">
    Make your first List lookup request
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/lists/list-lookup/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/lists/list-lookup-by-list-id">
    Full endpoint documentation
  </Card>

  <Card title="Sample code" icon="github" href="https://github.com/xdevplatform/Twitter-API-v2-sample-code">
    Working code examples
  </Card>
</CardGroup>
