---
title: "About the X API"
source: https://docs.x.com/x-api/getting-started/about-x-api
path: x-api/getting-started/about-x-api
---

High-level overview of the X API covering capabilities, v2 versus v1.1 versions, available resources, pricing tiers, and how to start building.

The X API provides programmatic access to X's public conversation. Retrieve posts, analyze trends, build integrations, and create new experiences on the platform.

***

## What you can do

| Capability             | Description                                      |
| :--------------------- | :----------------------------------------------- |
| **Read posts**         | Search, look up, and stream posts in real-time   |
| **Publish content**    | Create posts, replies, and threads               |
| **Manage users**       | Look up users, manage follows, blocks, and mutes |
| **Analyze data**       | Access metrics, trends, and engagement analytics |
| **Build integrations** | Send DMs, manage lists, and interact with Spaces |

***

## API versions

<Tabs>
  <Tab title="X API v2 (Recommended)">
    The current version of the X API with modern features and flexible pricing.

    **Why use v2:**

    * Pay-per-usage pricing
    * Modern JSON response format
    * Flexible [fields](/x-api/fundamentals/fields) and [expansions](/x-api/fundamentals/expansions)
    * Advanced features: annotations, conversation tracking, edit history
    * All new endpoints and features

    **Getting started:**

    1. Sign up at [console.x.com](https://console.x.com)
    2. Create an app and get credentials
    3. [Make your first request](/x-api/getting-started/make-your-first-request)
  </Tab>

  <Tab title="X API v1.1 (Legacy)">
    The previous version of the X API. Limited support; use v2 for new projects.

    **Still available:**

    * Some media upload endpoints
    * Legacy streaming (deprecated)
    * Some specialized endpoints

    **Migrating to v2:**
    See the [migration guide](/x-api/migrate/overview) for endpoint mapping and data format changes.
  </Tab>
</Tabs>

***

## Available resources

The X API provides access to these resource types:

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

## v2 highlights

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
  Access public metrics (likes, reposts, replies) and private metrics (impressions, clicks) for your own posts.

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

X API v2 uses **pay-per-usage** pricing:

| Benefit                | Description                                                    |
| :--------------------- | :------------------------------------------------------------- |
| **No subscriptions**   | Pay only for what you use                                      |
| **Credit-based**       | Purchase credits, deducted per request                         |
| **Real-time tracking** | Monitor usage in the Developer Console                         |
| **Deduplication**      | Same resource requested twice in 24 hours is only charged once |

[View pricing details →](/x-api/getting-started/pricing)

***

## Next steps

<CardGroup>
  <Card title="Get access" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-key.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=de93497af2dde62afd3a06e896d330f5" href="/x-api/getting-started/getting-access">
    Sign up and create your first app.
  </Card>

  <Card title="Make your first request" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/getting-started/make-your-first-request">
    Call the API in minutes.
  </Card>
</CardGroup>
