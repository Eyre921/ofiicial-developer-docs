---
title: "Quickstart"
source: https://docs.x.com/x-api/posts/lookup/quickstart
path: x-api/posts/lookup/quickstart
---

This guide walks you through making your first Post lookup request using the X API v2. Reference for the X API v2 standard tier covering lookup.

This guide walks you through making your first Post lookup request using the X API v2.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * Your App's Bearer Token (found in the Developer Console under "Keys and tokens")
</Note>

***

<Steps>
  <Step title="Find a Post ID">
    Every Post has a unique ID. You can find it in the Post's URL:

    ```
    https://x.com/XDevelopers/status/1228393702244134912
                                    └── This is the Post ID
    ```
  </Step>

  <Step title="Make a request">
    <CodeGroup>
      ```bash cURL theme={null}
      curl "https://api.x.com/2/tweets/1228393702244134912" \
        -H "Authorization: Bearer $BEARER_TOKEN"
      ```

      ```python Python SDK theme={null}
      from xdk import Client

      client = Client(bearer_token="YOUR_BEARER_TOKEN")

      # Get a single Post by ID
      response = client.posts.get("1228393702244134912")
      print(response.data)
      ```

      ```javascript JavaScript SDK theme={null}
      import { Client } from "@xdevplatform/xdk";

      const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

      const response = await client.posts.get("1228393702244134912");
      console.log(response.data);
      ```
    </CodeGroup>
  </Step>

  <Step title="Review the response">
    The default response includes the Post's `id`, `text`, and `edit_history_tweet_ids`:

    ```json theme={null}
    {
      "data": {
        "id": "1228393702244134912",
        "text": "What did the developer write in their Valentine's card?\n\nwhile(true) {\n    I = Love(You);\n}",
        "edit_history_tweet_ids": ["1228393702244134912"]
      }
    }
    ```
  </Step>

  <Step title="Request additional fields">
    Use query parameters to get more data:

    <CodeGroup>
      ```bash cURL theme={null}
      curl "https://api.x.com/2/tweets/1228393702244134912?\
      tweet.fields=created_at,public_metrics,author_id&\
      expansions=author_id&\
      user.fields=username,verified" \
        -H "Authorization: Bearer $BEARER_TOKEN"
      ```

      ```python title="Python SDK" lines wrap icon="python" theme={null}
      from xdk import Client

      client = Client(bearer_token="YOUR_BEARER_TOKEN")

      # Get a Post with additional fields and expansions
      response = client.posts.get(
          "1228393702244134912",
          tweet_fields=["created_at", "public_metrics", "author_id"],
          expansions=["author_id"],
          user_fields=["username", "verified"]
      )

      print(response.data)
      print(response.includes)  # Contains author user object
      ```

      ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
      import { Client } from "@xdevplatform/xdk";

      const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

      const response = await client.posts.get("1228393702244134912", {
        tweetFields: ["created_at", "public_metrics", "author_id"],
        expansions: ["author_id"],
        userFields: ["username", "verified"],
      });

      console.log(response.data);
      console.log(response.includes); // Contains author user object
      ```
    </CodeGroup>

    **Response:**

    ```json title="Example response" lines wrap icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-brackets.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=ed2428e77bab43e57800e1a590e982fa" theme={null}
    {
      "data": {
        "id": "1228393702244134912",
        "text": "What did the developer write in their Valentine's card?...",
        "created_at": "2020-02-14T19:00:55.000Z",
        "author_id": "2244994945",
        "public_metrics": {
          "retweet_count": 156,
          "reply_count": 23,
          "like_count": 892,
          "quote_count": 12
        },
        "edit_history_tweet_ids": ["1228393702244134912"]
      },
      "includes": {
        "users": [
          {
            "id": "2244994945",
            "username": "XDevelopers",
            "verified": true
          }
        ]
      }
    }
    ```
  </Step>

  <Step title="Look up multiple Posts">
    Retrieve up to 100 Posts in a single request:

    <CodeGroup>
      ```bash cURL theme={null}
      curl "https://api.x.com/2/tweets?\
      ids=1228393702244134912,1227640996038684673,1199786642791452673&\
      tweet.fields=created_at,author_id" \
        -H "Authorization: Bearer $BEARER_TOKEN"
      ```

      ```python title="Python SDK" lines wrap icon="python" theme={null}
      from xdk import Client

      client = Client(bearer_token="YOUR_BEARER_TOKEN")

      # Get multiple Posts by IDs
      response = client.posts.get_posts(
          ids=["1228393702244134912", "1227640996038684673", "1199786642791452673"],
          tweet_fields=["created_at", "author_id"]
      )

      for post in response.data:
          print(f"{post.id}: {post.text[:50]}...")
      ```

      ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
      import { Client } from "@xdevplatform/xdk";

      const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

      const response = await client.posts.getPosts({
        ids: ["1228393702244134912", "1227640996038684673", "1199786642791452673"],
        tweetFields: ["created_at", "author_id"],
      });

      response.data?.forEach((post) => {
        console.log(`${post.id}: ${post.text?.slice(0, 50)}...`);
      });
      ```
    </CodeGroup>
  </Step>
</Steps>

***

## Next steps

<CardGroup>
  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/posts/lookup/integrate">
    Learn authentication, rate limits, and best practices
  </Card>

  <Card title="Fields and expansions" icon="sliders" href="/x-api/fundamentals/fields">
    Master the fields and expansions system
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/posts/get-post-by-id">
    See all available parameters
  </Card>

  <Card title="Sample code" icon="github" href="https://github.com/xdevplatform/Twitter-API-v2-sample-code">
    Explore more examples
  </Card>
</CardGroup>
