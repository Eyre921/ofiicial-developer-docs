---
title: "X API"
source: https://docs.x.com/x-api/introduction
path: x-api/introduction
---

Programmatic access to X with v2 REST endpoints for Posts, users, Spaces, lists, DMs, and trends, with pay-per-use pricing and modern SDKs.

The X API gives you programmatic access to X's public conversation. Read posts, publish content, manage users, and analyze trends—all through modern REST endpoints with flexible pay-per-usage pricing.

<CardGroup>
  <Card title="Get started" icon="https://mintcdn.com/x-preview/oR-aRNyj1BKPJtxM/icons/xds/icon-rocket.svg?fit=max&auto=format&n=oR-aRNyj1BKPJtxM&q=85&s=b978d7a9225de31709efbbed5b84e92d" href="/x-api/getting-started/make-your-first-request">
    Create an app and make your first request in minutes.
  </Card>

  <Card title="API reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/posts/create-post">
    Explore all available endpoints.
  </Card>

  <Card title="SDKs" icon="cube" href="/tools-and-libraries">
    Official Python and TypeScript libraries.
  </Card>
</CardGroup>

***

## What you can build

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

## Pricing

The X API uses **pay-per-usage** pricing. No subscriptions—pay only for what you use.

<CardGroup>
  <Card title="Flexible scaling" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-bar-chart.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=e2a41caa858b122416f0005a55a8f143">
    Start small and grow. Costs scale with your actual usage.
  </Card>

  <Card title="No commitments" icon="unlock">
    No contracts or minimum spend. Stop anytime.
  </Card>

  <Card title="Real-time tracking" icon="gauge-high">
    Monitor usage and costs live in the Developer Console.
  </Card>

  <Card title="Credit-based" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-coins.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=d8b17de3fb4032d86b77606ea95fcb55">
    Purchase credits upfront. Deducted as you use the API.
  </Card>
</CardGroup>

<Tip>
  Earn free [xAI API](https://docs.x.ai) credits when you purchase X API credits—up to 20% back based on your spend. [Learn more](/x-api/getting-started/pricing#free-xai-api-credits)
</Tip>

<div>
  <Button href="/x-api/getting-started/pricing">Pricing details</Button>
  <Button href="https://console.x.com">Purchase credits</Button>
</div>

***

## Key features

<Tabs>
  <Tab title="Data access">
    ### Rich data objects

    Access detailed, structured data for posts, users, media, and more:

    * **Posts**: Full text, metrics, entities, annotations, conversation threads
    * **Users**: Profiles, follower counts, verification status
    * **Media**: Images, videos, GIFs with metadata
    * **Polls**: Options and vote counts

    Customize responses with [fields](/x-api/fundamentals/fields) and [expansions](/x-api/fundamentals/expansions) to get exactly the data you need.
  </Tab>

  <Tab title="Near real-time streaming">
    ### Filtered stream

    Get posts delivered in near real-time as they're published. Define up to 1,000 filtering rules to receive only matching posts.

    ```bash theme={null}
    # Add a rule
    curl -X POST "https://api.x.com/2/tweets/search/stream/rules" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{"add": [{"value": "from:xdevelopers"}]}'

    # Connect to stream
    curl "https://api.x.com/2/tweets/search/stream" \
      -H "Authorization: Bearer $TOKEN"
    ```

    [Learn more about filtered stream →](/x-api/posts/filtered-stream/introduction)
  </Tab>

  <Tab title="Search & analytics">
    ### Full-archive search

    Search the complete history of public posts—back to 2006. Build queries with operators for users, keywords, dates, and more.

    ```bash theme={null}
    curl "https://api.x.com/2/tweets/search/all?query=AI%20lang:en" \
      -H "Authorization: Bearer $TOKEN"
    ```

    ### Metrics

    Access engagement metrics including impressions, likes, reposts, replies, and video views.

    [Learn more about search →](/x-api/posts/search/introduction)
  </Tab>
</Tabs>

***

## Quick start

<Steps>
  <Step title="Create a developer account">
    Sign up at [console.x.com](https://console.x.com) and create an app.
  </Step>

  <Step title="Get your credentials">
    Generate your Bearer Token for app-only requests.
  </Step>

  <Step title="Make a request">
    Try looking up a user:

    ```bash theme={null}
    curl "https://api.x.com/2/users/by/username/xdevelopers" \
      -H "Authorization: Bearer $BEARER_TOKEN"
    ```
  </Step>
</Steps>

<Button href="/x-api/getting-started/make-your-first-request">Full quickstart guide</Button>

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

[Browse all libraries →](/tools-and-libraries)

***

## Support

<CardGroup>
  <Card title="Developer Forum" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-chat-unread.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=ce6313d8c0b7b4e5363f2ce80b89f7e4" href="https://devcommunity.x.com">
    Get help from the community and X team.
  </Card>

  <Card title="Support Hub" icon="circle-question" href="https://developer.x.com/en/support/twitter-api.html">
    FAQs and troubleshooting guides.
  </Card>
</CardGroup>
