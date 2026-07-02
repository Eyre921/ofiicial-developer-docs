---
title: "Manage Retweets"
source: https://docs.x.com/x-api/posts/retweets/migrate/manage-retweets-standard-to-twitter-api-v2
path: x-api/posts/retweets/migrate/manage-retweets-standard-to-twitter-api-v2
---

If you have been working with the standard v1.1 POST statuses/retweet/:id, and POST. Reference for the X API v2 standard tier covering migrate.

### Manage Retweets: Standard v1.1 compared to X API v2

If you have been working with the standard v1.1 [POST statuses/retweet/:id](https://developer.x.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id), and [POST statuses/unretweet/:id](https://developer.x.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id)  endpoints, the goal of this guide is to help you understand the similarities and differences between the standard and X API v2 Retweets endpoints.

* **Similarities**
  * Authentication
* **Differences**
  * Endpoint URLs and HTTP methods
  * Request limitations
  * App and Project requirements
  * Request parameters

#### Similarities

**Authentication**

Both the standard v1.1 and X API v2 manage Retweets ([POST statuses/retweet/:id](https://developer.x.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id), and [POST statuses/unretweet/:id](https://developer.x.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id)) endpoints use [OAuth 1.0a User Context](https://developer.x.com/content/developer-twitter/resources/fundamentals/authentication). Therefore, if you were previously using one of the standard v1.1 Retweets lookup endpoints, you can continue using the same authentication method if you migrate to the X API v2 version. 

#### Differences

**Endpoint URLs and HTTP methods**

* Standard v1.1 endpoints:
  * [https://api.x.com/1.1/statuses/retweet/:id.json](https://api.x.com/1.1/statuses/retweet/:id.json)
    (Retweets a Post. Returns the original Post with Retweet details embedded)
  * [https://api.x.com/1.1/statuses/unretweet/:id.json](https://api.x.com/1.1/statuses/unretweet/:id.json)
    (Undo a Retweet. Returns the original Post with Retweet details embedded)
* X API v2 endpoint:
