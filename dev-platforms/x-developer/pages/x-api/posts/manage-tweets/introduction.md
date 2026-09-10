---
title: "Manage Posts on the X API v2"
source: https://docs.x.com/x-api/posts/manage-tweets/introduction
path: x-api/posts/manage-tweets/introduction
---

Create and delete Posts on behalf of authenticated users with the X API v2 standard tier manage Posts endpoints, including request and response details.

The Manage Posts endpoints let you create and delete Posts on behalf of authenticated users. Build applications that post content, create threads, or manage user Posts.

## Overview

<CardGroup>
  <Card title="Create Post" icon="pen">
    Publish a new Post
  </Card>

  <Card title="Delete Post" icon="trash">
    Delete an existing Post
  </Card>

  <Card title="Reply" icon="reply">
    Reply to another Post
  </Card>

  <Card title="Quote" icon="quote-right">
    Quote another Post
  </Card>
</CardGroup>

***

## Endpoints

| Method | Endpoint                                    | Description       |
| :----- | :------------------------------------------ | :---------------- |
| POST   | [`/2/tweets`](/x-api/posts/create-post)     | Create a new Post |
| DELETE | [`/2/tweets/:id`](/x-api/posts/delete-post) | Delete a Post     |

***

## Creating Posts

### Basic Post

```bash theme={null}
curl -X POST "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from the API!"}'
```

<Note>
  **Self-serve customers:** Posts created via the API are limited to a maximum of 1 cashtag per post.
</Note>

### Reply to a Post

```bash theme={null}
curl -X POST "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This is a reply!",
    "reply": {
      "in_reply_to_tweet_id": "1234567890"
    }
  }'
```

<Note>
  **Self-serve customers:** Replies are only permitted if the original post's author has explicitly summoned the replying account by @mentioning them or quoting one of their posts.
</Note>

### Quote a Post

```bash theme={null}
curl -X POST "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Check this out!",
    "quote_tweet_id": "1234567890"
  }'
```

### Post with media

```bash theme={null}
curl -X POST "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Photo of the day",
    "media": {
      "media_ids": ["1234567890123456789"]
    }
  }'
```

<Note>
  Upload media first using the [chunked media upload](/x-api/media/quickstart/media-upload-chunked) endpoints (`/2/media/upload/initialize`, `/{id}/append`, `/{id}/finalize`), then reference the `media_id` in your Post.
</Note>

A Post may include **up to 4 photos**, **1 animated GIF**, or **1 video**. Video duration and file size are checked again at Post create. They follow the **posting user's** X Premium / verified status and the `media_category` used at upload:

| Posting account      | Video cap when attaching to a Post (`tweet_video` / `amplify_video`) |
| :------------------- | :------------------------------------------------------------------- |
| Default (no Premium) | 20 minutes, 8 GB                                                     |
| X Premium / verified | 125 minutes, 16 GB                                                   |

If the video is longer than that user is allowed to post, the response is **403 Forbidden**: `This user is not allowed to post a video longer than N minutes.` A successful upload does not guarantee the media can be attached. See [size and duration limits](/x-api/media/introduction#size-and-duration-limits).

### Post with poll

```bash theme={null}
curl -X POST "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "What is your favorite color?",
    "poll": {
      "options": ["Red", "Blue", "Green", "Yellow"],
      "duration_minutes": 1440
    }
  }'
```

### Post with paid partnership

Use the `paid_partnership` field when creating a Post to indicate it is a paid partnership (i.e., the author is disclosing that the Post contains paid promotion). When set to `true`, the Post will be labeled as a paid promotion.

```bash theme={null}
curl -X POST "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Excited to partner with Acme on their latest launch!",
    "paid_partnership": true
  }'
```

To retrieve the value on existing Posts (including your own), request it via the `tweet.fields` parameter:

```bash theme={null}
curl "https://api.x.com/2/tweets/1234567890?tweet.fields=paid_partnership,created_at" \
  -H "Authorization: Bearer $TOKEN"
```

***

## Deleting Posts

```bash theme={null}
curl -X DELETE "https://api.x.com/2/tweets/1234567890" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN"
```

<Warning>
  You can only delete Posts authored by the authenticated user.
</Warning>

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * User Access Tokens via [OAuth 2.0 PKCE](/resources/fundamentals/authentication#oauth-2-0-authorization-code-flow-with-pkce-2) or [3-legged OAuth](/resources/fundamentals/authentication#obtaining-access-tokens-using-3-legged-oauth-flow)
</Note>

<CardGroup>
  <Card title="Quickstart" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/posts/manage-tweets/quickstart">
    Create your first Post
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/posts/manage-tweets/integrate">
    Key concepts and best practices
  </Card>

  <Card title="Media upload" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-photo.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=d0986097dcff55478c32801b20440ecc" href="/x-api/media/quickstart/media-upload-chunked">
    Upload media for Posts
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/posts/creation-of-a-post">
    Full endpoint documentation
  </Card>
</CardGroup>
