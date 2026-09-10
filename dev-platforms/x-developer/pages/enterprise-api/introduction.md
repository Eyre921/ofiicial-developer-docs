---
title: "X Enterprise API introduction and product overview"
source: https://docs.x.com/enterprise-api/introduction
path: enterprise-api/introduction
---

Enterprise-grade access to the X firehose, volume streams, full-archive search, and PowerTrack with dedicated technical support and custom pricing.

The X API Enterprise plan provides the highest level of access to X data. Get complete firehose coverage, volume streams, semantic embedding operators for Filtered Stream, dedicated account management, and custom rate limits designed for organizations that depend on X data at scale.

<CardGroup>
  <Card title="Request access" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/forms/enterprise-api-interest">
    Apply for Enterprise access with a dedicated account team.
  </Card>

  <Card title="API reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/posts/create-post">
    Explore all available endpoints, including Enterprise-exclusive ones.
  </Card>

  <Card title="SDKs" icon="cube" href="/tools-and-libraries">
    Official Python and TypeScript libraries.
  </Card>
</CardGroup>

***

## Why Enterprise?

Enterprise access includes everything in the pay-per-use X API plus exclusive high-volume endpoints, dedicated support, and custom packages tailored to your needs.

<CardGroup>
  <Card title="Complete firehose access" icon="fire">
    Stream 100% of public posts in real-time. No sampling, no limits. Get every post as it happens.
  </Card>

  <Card title="Volume streams" icon="wave-pulse">
    Access full-volume and language-specific streams, including English, Japanese, Korean, and Portuguese firehoses.
  </Card>

  <Card title="Dedicated support" icon="headset">
    Get a dedicated account manager, personalized technical support, and priority issue resolution.
  </Card>

  <Card title="Custom rate limits" icon="gauge-high">
    Higher rate limits and custom-tailored packages to match your throughput requirements.
  </Card>

  <Card title="Engagement metrics at scale" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bar-chart.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=e2a41caa858b122416f0005a55a8f143">
    Access post and media analytics endpoints for deep engagement insights across large datasets.
  </Card>

  <Card title="Compliance streams" icon="https://mintcdn.com/x-preview/cfyQtgCdwk8p69aa/icons/xds/icon-shield-check.svg?fit=max&auto=format&n=cfyQtgCdwk8p69aa&q=85&s=768533bde161ac68862de87449f011c3">
    Stay compliant with real-time compliance event streams for posts, users, and likes.
  </Card>

  <Card title="Semantic embedding for Filtered Stream" icon="brain">
    Match posts by conceptual meaning — not just keywords — using the `embedding:` operator in Filtered Stream (requires Embedding tier).
  </Card>
</CardGroup>

***

## Enterprise-exclusive endpoints

These endpoints are only available on Enterprise plans:

<CardGroup>
  <Card title="Volume Streams" icon="satellite-dish" href="/x-api/posts/volume-streams/introduction">
    Full firehose, language-specific streams, and sampled streams.
  </Card>

  <Card title="Likes Streams" icon="https://mintcdn.com/x-preview/szd6PKNMlRQoyyAo/icons/xds/icon-heart.svg?fit=max&auto=format&n=szd6PKNMlRQoyyAo&q=85&s=3a435e6393c019d681c6f1a0737e21a8" href="/x-api/stream/likes-streams-introduction">
    Stream all likes or sampled likes in real-time.
  </Card>

  <Card title="Powerstream" icon="bolt" href="/x-api/powerstream/introduction">
    High-performance filtered streaming with low latency (keyword operators).
  </Card>

  <Card title="Engagement Metrics" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bar-chart.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=e2a41caa858b122416f0005a55a8f143" href="/x-api/posts/get-post-analytics">
    Deep analytics for post and media engagement.
  </Card>

  <Card title="Account Activity" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bell.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=5e0b3dcfbb39ba3d4619931d7cd927d1" href="/x-api/account-activity/introduction">
    Subscribe to real-time user activity events including posts, DMs, likes, and follows.
  </Card>

  <Card title="Stream Webhooks" icon="webhook" href="/x-api/webhooks/stream/introduction">
    Receive filtered stream data via webhooks instead of persistent connections.
  </Card>
</CardGroup>

***

## What you can build

Enterprise access powers the most demanding use cases on X.

<CardGroup>
  <Card title="Posts" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=9fde7d51b4f18c96d3a38a81d519761f" href="/x-api/posts/lookup/introduction">
    Search, retrieve, and publish posts. Access timelines, threads, and quote posts.
  </Card>

  <Card title="Users" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-person.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=507a4bbcdcf5744bd18781508002e305" href="/x-api/users/lookup/introduction">
    Look up users, manage follows, blocks, and mutes.
  </Card>

  <Card title="Spaces" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-microphone.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=84616ff8f3d942047a71ee5e0a5adab9" href="/x-api/spaces/lookup/introduction">
    Find live audio conversations and their participants.
  </Card>

  <Card title="Direct Messages" icon="https://mintcdn.com/x-preview/UIyI4eSwiP2OpODQ/icons/xds/icon-envelope.svg?fit=max&auto=format&n=UIyI4eSwiP2OpODQ&q=85&s=fbd38dbcd64d8688d3c9912ac30c4621" href="/x-api/direct-messages/lookup/introduction">
    Send and receive private messages.
  </Card>

  <Card title="Lists" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5" href="/x-api/lists/list-lookup/introduction">
    Create and manage curated lists of accounts.
  </Card>

  <Card title="Trends" icon="https://mintcdn.com/x-preview/UIyI4eSwiP2OpODQ/icons/xds/icon-feather-chart-line.svg?fit=max&auto=format&n=UIyI4eSwiP2OpODQ&q=85&s=185e7e1271f798947403bb3f0c44f294" href="/x-api/trends/trends-by-woeid/introduction">
    Access trending topics by location.
  </Card>
</CardGroup>

***

## Key features

<Tabs>
  <Tab title="Full firehose">
    ### Complete real-time coverage

    Stream 100% of public posts as they happen. No sampling, no gaps. Enterprise firehose access gives you the complete picture of public conversation on X.

    Available streams:

    * **All posts** - Every public post in real-time
    * **English posts** - All English-language posts
    * **Japanese posts** - All Japanese-language posts
    * **Korean posts** - All Korean-language posts
    * **Portuguese posts** - All Portuguese-language posts
    * **Sampled streams** - 1% and 10% random samples

    [Learn more about volume streams](/x-api/posts/volume-streams/introduction)
  </Tab>

  <Tab title="Data access">
    ### Rich data objects

    Access detailed, structured data for posts, users, media, and more:

    * **Posts**: Full text, metrics, entities, annotations, conversation threads
    * **Users**: Profiles, follower counts, verification status
    * **Media**: Images, videos, GIFs with metadata
    * **Polls**: Options and vote counts

    Customize responses with [fields](/x-api/fundamentals/fields) and [expansions](/x-api/fundamentals/expansions) to get exactly the data you need.
  </Tab>

  <Tab title="Streaming">
    ### Filtered stream

    Get posts delivered in real-time as they're published. Enterprise adds higher rule limits and the semantic `embedding:` operator (in Filtered Stream only) to match posts by meaning (not just keywords).

    ```bash theme={null}
    # Add a rule
    curl -X POST "https://api.x.com/2/tweets/search/stream/rules" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{"add": [{"value": "from:xdevelopers"}]}'

    # Connect to stream
    curl "https://api.x.com/2/tweets/search/stream" \
      -H "Authorization: Bearer $TOKEN"
    ```

    [Learn more about filtered stream](/x-api/posts/filtered-stream/introduction)
  </Tab>

  <Tab title="Search & analytics">
    ### Full-archive search

    Search the complete history of public posts back to 2006. Build queries with operators for users, keywords, dates, and more.

    ```bash theme={null}
    curl "https://api.x.com/2/tweets/search/all?query=AI%20lang:en" \
      -H "Authorization: Bearer $TOKEN"
    ```

    ### Engagement metrics

    Access deep engagement analytics including impressions, likes, reposts, replies, video views, and media-level metrics.

    [Learn more about search](/x-api/posts/search/introduction)
  </Tab>
</Tabs>

***

## Enterprise vs. pay-per-use

| Feature                | Pay-per-use             | Enterprise                                                            |
| :--------------------- | :---------------------- | :-------------------------------------------------------------------- |
| **Post search**        | Recent and full-archive | Recent and full-archive                                               |
| **Filtered stream**    | Up to 1,000 rules       | 5,000+ rules + semantic `embedding:` operators (Filtered Stream only) |
| **Volume streams**     | -                       | Full firehose and language streams                                    |
| **Likes streams**      | -                       | Full and sampled likes                                                |
| **Powerstream**        | -                       | Advanced filtered streaming                                           |
| **Engagement metrics** | -                       | Post and media analytics                                              |
| **Account Activity**   | -                       | Real-time user event subscriptions                                    |
| **Monthly post cap**   | 3 million reads         | Custom / unlimited                                                    |
| **Rate limits**        | Standard                | Custom / elevated                                                     |
| **Support**            | Community forum         | Dedicated account manager                                             |

***

## Get started

<Steps>
  <Step title="Apply for Enterprise access">
    [Contact our sales team](/forms/enterprise-api-interest) to discuss your needs and get a custom package.
  </Step>

  <Step title="Get onboarded">
    Your dedicated account manager will help you set up credentials and configure your access.
  </Step>

  <Step title="Start building">
    Use the same modern v2 API endpoints plus Enterprise-exclusive endpoints for your integration.

    ```bash theme={null}
    curl "https://api.x.com/2/users/by/username/xdevelopers" \
      -H "Authorization: Bearer $BEARER_TOKEN"
    ```
  </Step>
</Steps>

<Button href="/forms/enterprise-api-interest">Apply for Enterprise access</Button>

***

## Tools & libraries

<CardGroup>
  <Card title="Python SDK" icon="python" href="/xdks/python/overview">
    Official Python library with async support.
  </Card>

  <Card title="TypeScript SDK" icon="js" href="/xdks/typescript/overview">
    Official TypeScript/JavaScript library.
  </Card>

  <Card title="Postman" icon="server" href="https://www.postman.com/xapidevelopers/x-api-public-workspace/collection/34902927-2efc5689-99c6-4ab6-8091-996f35c2fd80">
    Interactive API explorer.
  </Card>
</CardGroup>

[Browse all libraries](/tools-and-libraries)

***

## Support

<CardGroup>
  <Card title="Dedicated Account Manager" icon="headset">
    Enterprise customers get a dedicated point of contact for technical and account support.
  </Card>

  <Card title="Developer Forum" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat-unread.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=ce6313d8c0b7b4e5363f2ce80b89f7e4" href="https://devcommunity.x.com">
    Get help from the community and X team.
  </Card>
</CardGroup>
