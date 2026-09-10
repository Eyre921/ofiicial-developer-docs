---
title: "User Search"
source: https://docs.x.com/x-api/users/search/introduction
path: x-api/users/search/introduction
---

Search X users by keyword with the X API v2 User search endpoint to find accounts by name, handle, bio terms, and other public profile fields and metadata.

The User Search endpoint lets you search for users by keyword. Find users by name, username, or content in their bio.

## Overview

<CardGroup>
  <Card title="Keyword search" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-search.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=8c11ad89387b7c09ced1553d5c232834">
    Search by name, username, or bio
  </Card>

  <Card title="Discover users" icon="user-plus">
    Find relevant accounts
  </Card>
</CardGroup>

***

## Endpoint

| Method | Endpoint                                       | Description      |
| :----- | :--------------------------------------------- | :--------------- |
| GET    | [`/2/users/search`](/x-api/users/search-users) | Search for users |

***

## Example request

```bash theme={null}
curl "https://api.x.com/2/users/search?\
query=python%20developer&\
user.fields=description,verified,public_metrics" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

## Example response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": [
    {
      "id": "1234567890",
      "name": "Python Developer",
      "username": "pythondev",
      "description": "Building cool things with Python",
      "verified": false,
      "public_metrics": {
        "followers_count": 5000,
        "following_count": 200,
        "tweet_count": 1500
      }
    }
  ],
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
  <Card title="User lookup" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305" href="/x-api/users/lookup/introduction">
    Look up users by ID or username
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/user-search">
    Full endpoint documentation
  </Card>
</CardGroup>
