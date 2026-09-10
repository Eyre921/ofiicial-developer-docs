---
title: "Quickstart"
source: https://docs.x.com/x-api/lists/list-tweets/quickstart
path: x-api/lists/list-tweets/quickstart
---

This guide walks you through retrieving Posts from a List timeline. Reference for the X API v2 standard tier covering list tweets.

This guide walks you through retrieving Posts from a List timeline.

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * Your App's Bearer Token
</Note>

***

<Steps>
  <Step title="Find a List ID" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5">
    You can find a List ID in the URL when viewing a List on x.com:

    ```
    https://x.com/i/lists/84839422
                          └── This is the List ID
    ```
  </Step>

  <Step title="Request the List timeline" icon="terminal">
    <CodeGroup>
      ```bash cURL theme={null}
      curl "https://api.x.com/2/lists/84839422/tweets?\
      tweet.fields=created_at,public_metrics,author_id&\
      expansions=author_id&\
      user.fields=username,verified&\
      max_results=10" \
        -H "Authorization: Bearer $BEARER_TOKEN"
      ```

      ```python title="Python SDK" lines wrap icon="python" theme={null}
      from xdk import Client

      client = Client(bearer_token="YOUR_BEARER_TOKEN")

      # Get Posts from a List with pagination
      for page in client.lists.get_tweets(
          "84839422",
          tweet_fields=["created_at", "public_metrics", "author_id"],
          expansions=["author_id"],
          user_fields=["username", "verified"],
          max_results=10
      ):
          for post in page.data:
              print(f"{post.text[:50]}... - Likes: {post.public_metrics.like_count}")
      ```

      ```javascript title="JavaScript SDK" lines wrap icon="square-js" theme={null}
      import { Client } from "@xdevplatform/xdk";

      const client = new Client({ bearerToken: "YOUR_BEARER_TOKEN" });

      // Get Posts from a List with pagination
      const paginator = client.lists.getTweets("84839422", {
        tweetFields: ["created_at", "public_metrics", "author_id"],
        expansions: ["author_id"],
        userFields: ["username", "verified"],
        maxResults: 10,
      });

      for await (const page of paginator) {
        page.data?.forEach((post) => {
          console.log(`${post.text?.slice(0, 50)}... - Likes: ${post.public_metrics?.like_count}`);
        });
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Review the response" icon="eye">
    ```json theme={null}
    {
      "data": [
        {
          "id": "1458172421115101189",
          "text": "Check out our latest announcement...",
          "author_id": "4172587277",
          "created_at": "2024-01-15T10:30:00.000Z",
          "public_metrics": {
            "retweet_count": 42,
            "reply_count": 5,
            "like_count": 156,
            "quote_count": 3
          },
          "edit_history_tweet_ids": ["1458172421115101189"]
        }
      ],
      "includes": {
        "users": [
          {
            "id": "4172587277",
            "username": "TechNews",
            "verified": true
          }
        ]
      },
      "meta": {
        "result_count": 1,
        "next_token": "7140dibdnow9c7btw3z2vwioavpvutgzrzm9icis4ndix"
      }
    }
    ```
  </Step>

  <Step title="Paginate through results" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-arrow-right.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=88e933002782dbdeb204043cedef033e">
    The SDKs handle pagination automatically. For cURL, use the `next_token` from the response to get more Posts:

    ```bash theme={null}
    curl "https://api.x.com/2/lists/84839422/tweets?\
    max_results=10&\
    pagination_token=7140dibdnow9c7btw3z2vwioavpvutgzrzm9icis4ndix" \
      -H "Authorization: Bearer $BEARER_TOKEN"
    ```
  </Step>
</Steps>

<Note>
  This endpoint returns up to 800 of the most recent Posts from the List.
</Note>

***

## Next steps

<CardGroup>
  <Card title="List lookup" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5" href="/x-api/lists/list-lookup/quickstart">
    Get List details
  </Card>

  <Card title="List members" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980" href="/x-api/lists/list-members/introduction">
    Get List members
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/lists/list-tweets/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/lists/get-list-posts">
    Full endpoint documentation
  </Card>
</CardGroup>
