---
title: "Quote Posts"
source: https://docs.x.com/enterprise-api/posts/quote-tweets/introduction
path: enterprise-api/posts/quote-tweets/introduction
---

The Quote Posts endpoint lets you retrieve Posts that quote a specific Post. Reference for the Enterprise X API tier covering quote tweets.

The Quote Posts endpoint lets you retrieve Posts that quote a specific Post. See how users are commenting on and sharing content.

## Overview

<CardGroup>
  <Card title="Quote lookup" icon="quote-right">
    Get all Quote Posts for a Post
  </Card>

  <Card title="Engagement insight" icon="chart-line">
    See how content is being discussed
  </Card>
</CardGroup>

***

## Endpoint

| Method | Endpoint                                                      | Description                |
| :----- | :------------------------------------------------------------ | :------------------------- |
| GET    | [`/2/tweets/:id/quote_tweets`](/x-api/posts/get-quoted-posts) | Get Quote Posts for a Post |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/tweets/1234567890/quote_tweets?\
tweet.fields=created_at,author_id,public_metrics&\
expansions=author_id&\
user.fields=username" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

## Example response

```json theme={null}
{
  "data": [
    {
      "id": "9876543210",
      "text": "Great point! This is exactly what we need.",
      "author_id": "1111111111",
      "created_at": "2024-01-15T10:30:00.000Z"
    }
  ],
  "includes": {
    "users": [
      {
        "id": "1111111111",
        "username": "example_user"
      }
    ]
  },
  "meta": {
    "result_count": 1
  }
}
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
  <Card title="Quickstart" icon="rocket" href="/x-api/posts/quote-tweets/quickstart">
    Get Quote Posts for a Post
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/posts/get-quoted-posts">
    Full endpoint documentation
  </Card>
</CardGroup>
