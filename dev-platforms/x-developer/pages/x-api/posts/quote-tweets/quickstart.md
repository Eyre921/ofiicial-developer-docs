---
title: "Quickstart"
source: https://docs.x.com/x-api/posts/quote-tweets/quickstart
path: x-api/posts/quote-tweets/quickstart
---

This guide walks you through retrieving Quote Posts (Posts that quote another Post). Reference for the X API v2 standard tier covering quote tweets.

This guide walks you through retrieving Quote Posts (Posts that quote another Post).

<Note>
  **Prerequisites**

  Before you begin, you'll need:

  * A [developer account](https://developer.x.com/en/portal/petition/essential/basic-info) with an approved App
  * Your App's Bearer Token
</Note>

***

<Steps>
  <Step title="Find the Post ID" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=9fde7d51b4f18c96d3a38a81d519761f">
    Get the ID of the Post you want to find quotes for. You can find it in the Post's URL:

    ```
    https://x.com/XDevelopers/status/1409931481552543749
                                    └── This is the Post ID
    ```
  </Step>

  <Step title="Request Quote Posts" icon="terminal">
    <CodeGroup>
      ```bash cURL theme={null}
      curl "https://api.x.com/2/tweets/1409931481552543749/quote_tweets?\
      tweet.fields=created_at,public_metrics,author_id&\
      expansions=author_id&\
      user.fields=username,verified&\
      max_results=10" \
        -H "Authorization: Bearer $BEARER_TOKEN"
      ```

      ```python title="Python SDK" lines wrap icon="python" theme={null}
      from xdk import Client

      client = Client(bearer_token="YOUR_BEARER_TOKEN")

      # Get Quote Posts with pagination
      for page in client.posts.get_quote_tweets(
          "1409931481552543749",
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

      // Get Quote Posts with pagination
      const paginator = client.posts.getQuoteTweets("1409931481552543749", {
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
          "id": "1495979553889697792",
          "text": "Great thread on the new API features! https://t.co/...",
          "author_id": "29757971",
          "created_at": "2022-02-22T04:31:34.000Z",
          "public_metrics": {
            "retweet_count": 5,
            "reply_count": 2,
            "like_count": 42,
            "quote_count": 1
          },
          "edit_history_tweet_ids": ["1495979553889697792"]
        }
      ],
      "includes": {
        "users": [
          {
            "id": "29757971",
            "username": "developer",
            "verified": false
          }
        ]
      },
      "meta": {
        "result_count": 1,
        "next_token": "avdjwk0udyx6"
      }
    }
    ```
  </Step>

  <Step title="Paginate through results" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-arrow-right.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=88e933002782dbdeb204043cedef033e">
    The SDKs handle pagination automatically. For cURL, use the `next_token` to get more Quote Posts:

    ```bash theme={null}
    curl "https://api.x.com/2/tweets/1409931481552543749/quote_tweets?\
    max_results=10&\
    pagination_token=avdjwk0udyx6" \
      -H "Authorization: Bearer $BEARER_TOKEN"
    ```
  </Step>
</Steps>

***

## Next steps

<CardGroup>
  <Card title="Retweets" icon="retweet" href="/x-api/posts/retweets/introduction">
    Look up Retweets
  </Card>

  <Card title="Post lookup" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-search.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=8c11ad89387b7c09ced1553d5c232834" href="/x-api/posts/lookup/introduction">
    Look up Posts by ID
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/posts/get-quoted-posts">
    Full endpoint documentation
  </Card>
</CardGroup>
