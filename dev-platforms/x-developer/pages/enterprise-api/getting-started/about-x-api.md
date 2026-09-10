---
title: "About the Enterprise API — firehose, streams, and webhooks"
source: https://docs.x.com/enterprise-api/getting-started/about-x-api
path: enterprise-api/getting-started/about-x-api
---

Overview of the X Enterprise API, including full firehose access, volume and likes streams, account activity webhooks, custom rate limits, and support.

The Enterprise API provides the highest tier of access to X data. It includes everything available in the standard X API plus exclusive high-volume endpoints, semantic embedding operators for Filtered Stream, custom rate limits, and dedicated account management for organizations that need X data at scale.

***

## What you can do

Everything in the standard X API, plus:

| Capability                       | Description                                                                                                    |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **Stream the full firehose**     | Access 100% of public posts in real-time with volume streams                                                   |
| **Stream all likes**             | Full and sampled likes streams in real-time                                                                    |
| **Advanced filtered streaming**  | Powerstream (low-latency keyword filtering)                                                                    |
| **Semantic embedding operators** | Match posts by meaning (not just keywords) using `embedding:` on Filtered Stream (Enterprise + Embedding tier) |
| **Deep engagement analytics**    | Post and media engagement metrics at scale                                                                     |
| **Account activity events**      | Real-time subscriptions for user events (posts, DMs, likes, follows)                                           |
| **Webhook delivery**             | Receive filtered stream data via webhooks                                                                      |
| **Custom rate limits**           | Elevated limits tailored to your throughput needs                                                              |
| **Dedicated support**            | Named account manager and priority issue resolution                                                            |

***

## Enterprise-exclusive endpoints

These endpoints are only available with Enterprise access:

<CardGroup>
  <Card title="Volume Streams" icon="satellite-dish" href="/x-api/posts/volume-streams/introduction">
    Full firehose and language-specific streams for complete real-time coverage.
  </Card>

  <Card title="Likes Streams" icon="https://mintcdn.com/x-preview/szd6PKNMlRQoyyAo/icons/xds/icon-heart.svg?fit=max&auto=format&n=szd6PKNMlRQoyyAo&q=85&s=3a435e6393c019d681c6f1a0737e21a8" href="/x-api/stream/likes-streams-introduction">
    Stream all likes or sampled likes across the platform.
  </Card>

  <Card title="Powerstream" icon="bolt" href="/x-api/powerstream/introduction">
    High-performance filtered streaming with advanced operators.
  </Card>

  <Card title="Engagement Metrics" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bar-chart.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=e2a41caa858b122416f0005a55a8f143" href="/x-api/posts/get-post-analytics">
    Post and media analytics for deep engagement insights.
  </Card>

  <Card title="Account Activity" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bell.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=5e0b3dcfbb39ba3d4619931d7cd927d1" href="/x-api/account-activity/introduction">
    Real-time event subscriptions for user activity.
  </Card>

  <Card title="Stream Webhooks" icon="webhook" href="/x-api/webhooks/stream/introduction">
    Filtered stream delivery via webhooks.
  </Card>
</CardGroup>

***

## All available resources

Enterprise access includes the full set of X API resources:

<CardGroup>
  <Card title="Posts" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=9fde7d51b4f18c96d3a38a81d519761f">
    Search, retrieve, create, and delete posts. Access timelines, threads, and quote posts.
  </Card>

  <Card title="Users" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305">
    Look up profiles, manage relationships, and access follower data.
  </Card>

  <Card title="Spaces" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-microphone.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=84616ff8f3d942047a71ee5e0a5adab9">
    Discover live audio conversations and participants.
  </Card>

  <Card title="Direct Messages" icon="https://mintcdn.com/x-preview/UIyI4eSwiP2OpODQ/icons/xds/icon-envelope.svg?fit=max&auto=format&n=UIyI4eSwiP2OpODQ&q=85&s=fbd38dbcd64d8688d3c9912ac30c4621">
    Send and receive private messages between users.
  </Card>

  <Card title="Lists" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5">
    Create and manage curated lists of accounts.
  </Card>

  <Card title="Trends" icon="https://mintcdn.com/x-preview/UIyI4eSwiP2OpODQ/icons/xds/icon-feather-chart-line.svg?fit=max&auto=format&n=UIyI4eSwiP2OpODQ&q=85&s=185e7e1271f798947403bb3f0c44f294">
    Access trending topics by location.
  </Card>
</CardGroup>

***

## API highlights

<Accordion title="Fields and expansions">
  Request only the data you need. Use `fields` parameters to select specific attributes and `expansions` to include related objects.

  ```bash theme={null}
  curl "https://api.x.com/2/tweets/123?tweet.fields=created_at,public_metrics&expansions=author_id&user.fields=username" \
    -H "Authorization: Bearer $TOKEN"
  ```

  [Learn more about fields →](/x-api/fundamentals/fields)
</Accordion>

<Accordion title="Post annotations">
  Posts include semantic annotations identifying people, places, products, and topics. Filter streams and searches by topic.

  [Learn more about annotations →](/x-api/fundamentals/post-annotations)
</Accordion>

<Accordion title="Engagement metrics">
  Enterprise customers get access to dedicated engagement metrics endpoints for both posts and media, providing deep analytics at scale beyond what standard public metrics offer.

  [Learn more about metrics →](/x-api/fundamentals/metrics)
</Accordion>

<Accordion title="Conversation tracking">
  Reconstruct entire conversation threads using `conversation_id`. Track replies across the full thread.

  [Learn more about conversation tracking →](/x-api/fundamentals/conversation-id)
</Accordion>

<Accordion title="Edit history">
  Access the edit history of posts, including all previous versions and edit metadata.

  [Learn more about edit posts →](/x-api/fundamentals/edit-posts)
</Accordion>

***

## Pricing

Enterprise plans are custom-tailored to your organization's needs. Pricing is based on your data volume, endpoint usage, and support requirements.

| Feature                   | Details                                             |
| :------------------------ | :-------------------------------------------------- |
| **Custom packages**       | Tailored to your specific data and throughput needs |
| **Longer-term contracts** | Predictable pricing with committed usage agreements |
| **No post read cap**      | Custom or unlimited post read volumes               |
| **Dedicated support**     | Included with all Enterprise plans                  |

[Contact sales for pricing](/forms/enterprise-api-interest)

***

## Next steps

<CardGroup>
  <Card title="Apply for access" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-key.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=de93497af2dde62afd3a06e896d330f5" href="/forms/enterprise-api-interest">
    Contact our sales team to discuss your needs.
  </Card>

  <Card title="Explore endpoints" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/posts/create-post">
    Browse all available endpoints including Enterprise-exclusive ones.
  </Card>
</CardGroup>
