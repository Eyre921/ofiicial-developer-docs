---
title: "User Search"
source: https://docs.x.com/enterprise-api/users/search/introduction
path: enterprise-api/users/search/introduction
---

Search X users by keyword with the Enterprise tier User search endpoint to find accounts by name, handle, bio terms, and other public profile fields.

The User Search endpoint lets you search for users by keyword. Find users by name, username, or content in their bio.

## Overview

<CardGroup>
  <Card title="Keyword search" icon="magnifying-glass">
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

```json theme={null}
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
  <Card title="User lookup" icon="user" href="/x-api/users/lookup/introduction">
    Look up users by ID or username
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/users/user-search">
    Full endpoint documentation
  </Card>
</CardGroup>
