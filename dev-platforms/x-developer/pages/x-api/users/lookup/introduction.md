---
title: "User Lookup"
source: https://docs.x.com/x-api/users/lookup/introduction
path: x-api/users/lookup/introduction
---

The User lookup endpoints let you retrieve profile information for one or more users. Reference for the X API v2 standard tier covering lookup.

The User lookup endpoints let you retrieve profile information for one or more users. Look up users by their ID, username, or get details for the currently authenticated user.

## Overview

<CardGroup>
  <Card title="By ID" icon="fingerprint">
    Look up users by their unique user ID
  </Card>

  <Card title="By username" icon="at">
    Look up users by their @handle
  </Card>

  <Card title="Multiple users" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980">
    Retrieve up to 100 users per request
  </Card>

  <Card title="Authenticated user" icon="user-check">
    Get details for the current user
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                                              | Description                        |
| :----- | :-------------------------------------------------------------------- | :--------------------------------- |
| GET    | [`/2/users/:id`](/x-api/users/get-user-by-id)                         | Get user by ID                     |
| GET    | [`/2/users`](/x-api/users/get-users-by-ids)                           | Get users by IDs (up to 100)       |
| GET    | [`/2/users/by/username/:username`](/x-api/users/get-user-by-username) | Get user by username               |
| GET    | [`/2/users/by`](/x-api/users/get-users-by-usernames)                  | Get users by usernames (up to 100) |
| GET    | [`/2/users/me`](/x-api/users/get-my-user)                             | Get authenticated user             |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/users/by/username/XDevelopers?\
user.fields=created_at,description,public_metrics,verified" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

## Example response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": {
    "id": "2244994945",
    "name": "X Developers",
    "username": "XDevelopers",
    "created_at": "2013-12-14T04:35:55.000Z",
    "description": "The voice of the X developer community",
    "verified": true,
    "public_metrics": {
      "followers_count": 583423,
      "following_count": 2048,
      "tweet_count": 14052,
      "listed_count": 1672
    }
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
  <Card title="User lookup quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/users/lookup/quickstart/user-lookup">
    Look up users by ID or username
  </Card>

  <Card title="Authenticated user quickstart" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305" href="/x-api/users/lookup/quickstart/authenticated-lookup">
    Get the current user's profile
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/users/lookup/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/get-user-by-id">
    Full endpoint documentation
  </Card>
</CardGroup>
