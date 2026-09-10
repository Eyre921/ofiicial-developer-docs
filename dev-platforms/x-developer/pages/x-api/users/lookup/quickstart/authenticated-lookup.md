---
title: "Authenticated User Quickstart"
source: https://docs.x.com/x-api/users/lookup/quickstart/authenticated-lookup
path: x-api/users/lookup/quickstart/authenticated-lookup
---

This guide walks you through retrieving the currently authenticated user's profile using the. Reference for the X API v2 standard tier covering quickstart.

This guide walks you through retrieving the currently authenticated user's profile using the `/me` endpoint.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * User Access Token (OAuth 1.0a or OAuth 2.0 PKCE)
</Note>

***

## Get the authenticated user

Make a request to the `/me` endpoint with a User Access Token:

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/users/me?\
  user.fields=created_at,description,verified,public_metrics,profile_image_url" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN"
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_USER_ACCESS_TOKEN")

  # Get the authenticated user
  response = client.users.get_me(
      user_fields=["created_at", "description", "verified", "public_metrics", "profile_image_url"]
  )

  print(f"Username: {response.data.username}")
  print(f"ID: {response.data.id}")
  print(f"Followers: {response.data.public_metrics.followers_count}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ accessToken: "YOUR_USER_ACCESS_TOKEN" });

  // Get the authenticated user
  const response = await client.users.getMe({
    userFields: ["created_at", "description", "verified", "public_metrics", "profile_image_url"],
  });

  console.log(`Username: ${response.data?.username}`);
  console.log(`ID: ${response.data?.id}`);
  console.log(`Followers: ${response.data?.public_metrics?.followers_count}`);
  ```
</CodeGroup>

***

## Response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": {
    "id": "2244994945",
    "name": "X Developers",
    "username": "XDevelopers",
    "created_at": "2013-12-14T04:35:55.000Z",
    "description": "The voice of the X developer community",
    "verified": true,
    "profile_image_url": "https://pbs.twimg.com/profile_images/...",
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

## Use case

The `/me` endpoint is essential when:

* **Verifying authentication** — Confirm the user is properly authenticated
* **Getting the user ID** — Retrieve the authenticated user's ID for other API calls
* **Personalizing experiences** — Display the user's profile in your app
* **On behalf of requests** — Know who you're making requests for

***

## Include pinned Post

Request the user's pinned Post:

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/users/me?\
  user.fields=pinned_tweet_id&\
  expansions=pinned_tweet_id&\
  tweet.fields=created_at,text" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN"
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_USER_ACCESS_TOKEN")

  # Get authenticated user with pinned Post
  response = client.users.get_me(
      user_fields=["pinned_tweet_id"],
      expansions=["pinned_tweet_id"],
      tweet_fields=["created_at", "text"]
  )

  print(f"Username: {response.data.username}")
  # Pinned Post is in response.includes.tweets
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ accessToken: "YOUR_USER_ACCESS_TOKEN" });

  // Get authenticated user with pinned Post
  const response = await client.users.getMe({
    userFields: ["pinned_tweet_id"],
    expansions: ["pinned_tweet_id"],
    tweetFields: ["created_at", "text"],
  });

  console.log(`Username: ${response.data?.username}`);
  // Pinned Post is in response.includes?.tweets
  ```
</CodeGroup>

### Response with expansion

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": {
    "id": "2244994945",
    "name": "X Developers",
    "username": "XDevelopers",
    "pinned_tweet_id": "1234567890"
  },
  "includes": {
    "tweets": [
      {
        "id": "1234567890",
        "text": "Welcome to my profile!",
        "created_at": "2024-01-01T00:00:00.000Z"
      }
    ]
  }
}
```

***

## Available fields

| Field               | Description               |
| :------------------ | :------------------------ |
| `created_at`        | Account creation date     |
| `description`       | User bio                  |
| `profile_image_url` | Avatar URL                |
| `verified`          | Verification status       |
| `public_metrics`    | Follower/following counts |
| `location`          | User-defined location     |
| `url`               | User's website            |
| `protected`         | Protected account status  |
| `pinned_tweet_id`   | Pinned Post ID            |

***

## Authentication requirement

<Warning>
  The `/me` endpoint requires User Context authentication. App-Only (Bearer Token) authentication is not supported.
</Warning>

Use either:

* [OAuth 1.0a User Context](/resources/fundamentals/authentication)
* [OAuth 2.0 Authorization Code with PKCE](/resources/fundamentals/authentication#oauth-2-0-authorization-code-flow-with-pkce-2)

***

## Next steps

<CardGroup>
  <Card title="User lookup" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980" href="/x-api/users/lookup/quickstart/user-lookup">
    Look up other users
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/users/lookup/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/get-my-user">
    Full endpoint documentation
  </Card>
</CardGroup>
