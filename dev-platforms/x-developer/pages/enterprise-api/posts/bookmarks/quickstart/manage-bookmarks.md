---
title: "Manage Bookmarks"
source: https://docs.x.com/enterprise-api/posts/bookmarks/quickstart/manage-bookmarks
path: enterprise-api/posts/bookmarks/quickstart/manage-bookmarks
---

This guide walks you through adding and removing bookmarks using the X API. Reference for the Enterprise X API tier covering quickstart.

This guide walks you through adding and removing bookmarks using the X API.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * User Access Token with `bookmark.write` scope (OAuth 2.0 PKCE)
</Note>

***

## Add a bookmark

<Steps>
  <Step title="Get your user ID">
    You need your authenticated user's ID. You can find it using the `/2/users/me` endpoint or the [user lookup endpoint](/x-api/users/lookup/introduction).
  </Step>

  <Step title="Get the Post ID">
    Find the Post ID in the URL when viewing a Post:

    ```
    https://x.com/XDevelopers/status/1460323737035677698
                                    └── This is the Post ID
    ```
  </Step>

  <Step title="Add the bookmark">
    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST "https://api.x.com/2/users/2244994945/bookmarks" \
        -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"tweet_id": "1460323737035677698"}'
      ```

      ```python Python SDK theme={null}
      from xdk import Client

      client = Client(bearer_token="YOUR_USER_ACCESS_TOKEN")

      # Add a bookmark
      response = client.bookmarks.create(
          user_id="2244994945",
          tweet_id="1460323737035677698"
      )

      print(f"Bookmarked: {response.data.bookmarked}")
      ```

      ```javascript JavaScript SDK theme={null}
      import { Client } from "@xdevplatform/xdk";

      const client = new Client({ accessToken: "YOUR_USER_ACCESS_TOKEN" });

      // Add a bookmark
      const response = await client.bookmarks.create("2244994945", {
        tweetId: "1460323737035677698",
      });

      console.log(`Bookmarked: ${response.data?.bookmarked}`);
      ```
    </CodeGroup>
  </Step>

  <Step title="Review the response">
    ```json theme={null}
    {
      "data": {
        "bookmarked": true
      }
    }
    ```
  </Step>
</Steps>

***

## Remove a bookmark

Delete a Post from your bookmarks:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE "https://api.x.com/2/users/2244994945/bookmarks/1460323737035677698" \
    -H "Authorization: Bearer $USER_ACCESS_TOKEN"
  ```

  ```python Python SDK theme={null}
  from xdk import Client

  client = Client(bearer_token="YOUR_USER_ACCESS_TOKEN")

  # Remove a bookmark
  response = client.bookmarks.delete(
      user_id="2244994945",
      tweet_id="1460323737035677698"
  )

  print(f"Bookmarked: {response.data.bookmarked}")
  ```

  ```javascript JavaScript SDK theme={null}
  import { Client } from "@xdevplatform/xdk";

  const client = new Client({ accessToken: "YOUR_USER_ACCESS_TOKEN" });

  // Remove a bookmark
  const response = await client.bookmarks.delete("2244994945", "1460323737035677698");

  console.log(`Bookmarked: ${response.data?.bookmarked}`);
  ```
</CodeGroup>

**Response:**

```json theme={null}
{
  "data": {
    "bookmarked": false
  }
}
```

***

## Required scopes

When using OAuth 2.0 PKCE, your access token must have these scopes:

| Scope            | Description              |
| :--------------- | :----------------------- |
| `bookmark.write` | Add and remove bookmarks |
| `tweet.read`     | Read Post data           |
| `users.read`     | Read user data           |

***

## Next steps

<CardGroup>
  <Card title="Bookmarks lookup" icon="bookmark" href="/x-api/posts/bookmarks/quickstart/bookmarks-lookup">
    Get your bookmarked Posts
  </Card>

  <Card title="API Reference" icon="code" href="/x-api/users/create-bookmark">
    Full endpoint documentation
  </Card>
</CardGroup>
