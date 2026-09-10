---
title: "Quickstart"
source: https://docs.x.com/x-api/users/follows/quickstart
path: x-api/users/follows/quickstart
---

This guide walks you through retrieving followers and following lists, and managing follows. Reference for the X API v2 standard tier covering follows.

This guide walks you through retrieving followers and following lists, and managing follows.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * Your App's Bearer Token (for lookups)
  * User Access Token (for managing follows)
</Note>

***

## Get a user's followers

Retrieve the list of users following a specific user:

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/users/2244994945/followers?\
  user.fields=username,verified,public_metrics&\
  max_results=100" \
    -H "Authorization: Bearer $BEARER_TOKEN"
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_BEARER_TOKEN")

  # Get a user's followers with pagination
  for page in client.users.get_followers(
      "2244994945",
      user_fields=["username", "verified", "public_metrics"],
      max_results=100
  ):
      for user in page.data:
          print(f"{user.username} - Followers: {user.public_metrics.followers_count}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

  // Get a user's followers with pagination
  const paginator = client.users.getFollowers("2244994945", {
    userFields: ["username", "verified", "public_metrics"],
    maxResults: 100,
  });

  for await (const page of paginator) {
    page.data?.forEach((user) => {
      console.log(`${user.username} - Followers: ${user.public_metrics?.followers_count}`);
    });
  }
  ```
</CodeGroup>

### Response

```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
{
  "data": [
    {
      "id": "1234567890",
      "name": "Developer",
      "username": "dev_user",
      "verified": false,
      "public_metrics": {
        "followers_count": 500,
        "following_count": 200,
        "tweet_count": 1500
      }
    }
  ],
  "meta": {
    "result_count": 1,
    "next_token": "abc123"
  }
}
```

***

## Get who a user follows

Retrieve the list of users that a specific user follows:

<CodeGroup>
  ```bash cURL theme={null}
  curl "https://api.x.com/2/users/2244994945/following?\
  user.fields=username,verified&\
  max_results=100" \
    -H "Authorization: Bearer $BEARER_TOKEN"
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_BEARER_TOKEN")

  # Get users that a user follows
  for page in client.users.get_following(
      "2244994945",
      user_fields=["username", "verified"],
      max_results=100
  ):
      for user in page.data:
          print(f"{user.username} - Verified: {user.verified}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

  // Get users that a user follows
  const paginator = client.users.getFollowing("2244994945", {
    userFields: ["username", "verified"],
    maxResults: 100,
  });

  for await (const page of paginator) {
    page.data?.forEach((user) => {
      console.log(`${user.username} - Verified: ${user.verified}`);
    });
  }
  ```
</CodeGroup>

***

## Follow a user

Follow a user on behalf of the authenticated user:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.x.com/2/users/123456789/following" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"target_user_id": "2244994945"}'
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client
  from xdk.oauth1_auth import OAuth1

  oauth1 = OAuth1(
      api_key="YOUR_API_KEY",
      api_secret="YOUR_API_SECRET",
      access_token="YOUR_ACCESS_TOKEN",
      access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
  )

  client = Client(auth=oauth1)

  # Follow a user
  response = client.users.follow(
      source_user_id="123456789",
      target_user_id="2244994945"
  )
  print(f"Following: {response.data.following}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client, OAuth1 } from "@xdevplatform/xdk";

  const oauth1 = new OAuth1({
    apiKey: "YOUR_API_KEY",
    apiSecret: "YOUR_API_SECRET",
    accessToken: "YOUR_ACCESS_TOKEN",
    accessTokenSecret: "YOUR_ACCESS_TOKEN_SECRET",
  });

  const client = new Client({ oauth1 });

  // Follow a user
  const response = await client.users.follow("123456789", {
    targetUserId: "2244994945",
  });
  console.log(`Following: ${response.data?.following}`);
  ```
</CodeGroup>

### Response

```json theme={null}
{
  "data": {
    "following": true,
    "pending_follow": false
  }
}
```

<Note>
  If the target account is protected, `pending_follow` will be `true` until the follow request is approved.
</Note>

***

## Unfollow a user

Unfollow a user on behalf of the authenticated user:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE "https://api.x.com/2/users/123456789/following/2244994945" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN"
  ```

  ```python title="Python SDK" lines wrap icon="python" theme={null}
  from xdk import Client
  from xdk.oauth1_auth import OAuth1

  oauth1 = OAuth1(
      api_key="YOUR_API_KEY",
      api_secret="YOUR_API_SECRET",
      access_token="YOUR_ACCESS_TOKEN",
      access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
  )

  client = Client(auth=oauth1)

  # Unfollow a user
  response = client.users.unfollow(
      source_user_id="123456789",
      target_user_id="2244994945"
  )
  print(f"Following: {response.data.following}")
  ```

  ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
  import { Client, OAuth1 } from "@xdevplatform/xdk";

  const oauth1 = new OAuth1({
    apiKey: "YOUR_API_KEY",
    apiSecret: "YOUR_API_SECRET",
    accessToken: "YOUR_ACCESS_TOKEN",
    accessTokenSecret: "YOUR_ACCESS_TOKEN_SECRET",
  });

  const client = new Client({ oauth1 });

  // Unfollow a user
  const response = await client.users.unfollow("123456789", "2244994945");
  console.log(`Following: ${response.data?.following}`);
  ```
</CodeGroup>

### Response

```json theme={null}
{
  "data": {
    "following": false
  }
}
```

***

## Common parameters

| Parameter          | Description                            |
| :----------------- | :------------------------------------- |
| `max_results`      | Results per page (1-1000, default 100) |
| `pagination_token` | Token for next page                    |
| `user.fields`      | Additional user fields                 |
| `expansions`       | Related objects to include             |

***

## Next steps

<CardGroup>
  <Card title="User lookup" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305" href="/x-api/users/lookup/introduction">
    Look up user profiles
  </Card>

  <Card title="Blocks" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-block.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=702a65b4001948aebcc42635b8e2eac7" href="/x-api/users/blocks/introduction">
    Block and unblock users
  </Card>

  <Card title="Mutes" icon="volume-xmark" href="/x-api/users/mutes/introduction">
    Mute and unmute users
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/users/get-followers">
    Full endpoint documentation
  </Card>
</CardGroup>
