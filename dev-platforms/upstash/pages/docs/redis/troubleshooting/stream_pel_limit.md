---
title: "ERR XReadGroup is cancelled"
source: https://upstash.com/docs/redis/troubleshooting/stream_pel_limit
path: docs/redis/troubleshooting/stream_pel_limit
---

### Symptom

The client gets an exception similar to:

```
ReplyError: ERR XReadGroup is cancelled. Pending Entries List limit per consumer is about to be reached. Limit: 1000, Current PEL size: 90, Requested Read: 20, Key: mstream, Group: group1, Consumer: consumer1.
```

### Diagnosis

Pending Entries List of the stream for the consumer is full. For each consumer
in a consumer group, there is a pending entries list. This list keeps the
messages that are delivered to a consumer but not yet acknowledged via
[XACK](https://redis.io/commands/xack/). This list is populated via
[XREADGROUP](https://redis.io/commands/xreadgroup/).

### Solution

Acknowledge the consumed messages via [XACK](https://redis.io/commands/xack/)
from the list of the associated group and consumer.

- [Agent Memory with Redis Search](https://upstash.com/docs/redis/tutorials/agent_memory.md): Build short-term and long-term memory for AI agents on Upstash Redis. Store working memory with TTLs and recall long-term memories with Redis Search full-text queries.
- [Deploy a Serverless API with AWS CDK and AWS Lambda](https://upstash.com/docs/redis/tutorials/api_with_cdk.md)
- [Autocomplete API with Serverless Redis](https://upstash.com/docs/redis/tutorials/auto_complete_with_serverless_redis.md)
- [Build Stateful Applications with AWS App Runner and Serverless Redis](https://upstash.com/docs/redis/tutorials/aws_app_runner_with_redis.md): This tutorial shows how to create a serverless and stateful application using AWS App Runner and Redis
- [Session Management on Google Cloud Run with Serverless Redis](https://upstash.com/docs/redis/tutorials/cloud_run_sessions.md): This tutorial shows how to manage user sessions on Google Cloud Run using Serverless Redis.
- [Cloudflare Workers with Websockets and Redis](https://upstash.com/docs/redis/tutorials/cloudflare_websockets_redis.md)
- [Use Redis in Cloudflare Workers](https://upstash.com/docs/redis/tutorials/cloudflare_workers_with_redis.md)
- [Backendless Coin Price List with GraphQL API, Serverless Redis and Next.JS](https://upstash.com/docs/redis/tutorials/coin_price_list.md)
- [Build a Leaderboard API At Edge using Cloudflare Workers and Redis](https://upstash.com/docs/redis/tutorials/edge_leaderboard.md): This tutorial shows how to build a Leaderboard API At Edge using Cloudflare Workers and Redis.
- [Express Session with Serverless Redis](https://upstash.com/docs/redis/tutorials/express_session.md): This tutorial shows how to use Upstash as the session storage of your Express application.
- [Serverless Golang API with Redis](https://upstash.com/docs/redis/tutorials/goapi.md)
- [Build a Serverless Histogram API with Redis](https://upstash.com/docs/redis/tutorials/histogram.md): This tutorial shows how to build a histogram API with Redis.
- [Job Processing and Event Queue with Serverless Redis](https://upstash.com/docs/redis/tutorials/job_processing.md): This tutorial shows how to use Upstash Redis for job/task processing.
- [Caching in Laravel with Redis](https://upstash.com/docs/redis/tutorials/laravel_caching.md)
- [Next.js with Redis](https://upstash.com/docs/redis/tutorials/nextjs_with_redis.md)
- [Building a Serverless Notification API for Your Web Application with Redis](https://upstash.com/docs/redis/tutorials/notification.md): This tutorial shows how to create a Serverless Notification API for Your Web Application with Redis.
- [Nuxt with Redis](https://upstash.com/docs/redis/tutorials/nuxtjs_with_redis.md): This tutorial shows how to use Upstash inside your Nuxt application.
- [Redis as a Cache for Your FastAPI App](https://upstash.com/docs/redis/tutorials/python_fastapi_caching.md)
- [Multithreaded Web Scraping with Redis Caching](https://upstash.com/docs/redis/tutorials/python_multithreading.md)
- [Rate Limiting for Your FastAPI App](https://upstash.com/docs/redis/tutorials/python_rate_limiting.md)
- [Build a Real-Time Chat Application with Serverless Redis](https://upstash.com/docs/redis/tutorials/python_realtime_chat.md)
- [Manage Sessions in Python with Serverless Redis](https://upstash.com/docs/redis/tutorials/python_session.md)
- [Building a URL Shortener with Redis](https://upstash.com/docs/redis/tutorials/python_url_shortener.md)
- [Serverless Python API with Redis](https://upstash.com/docs/redis/tutorials/pythonapi.md)
- [AWS Lambda Rate Limiting with Serverless Redis](https://upstash.com/docs/redis/tutorials/rate-limiting.md)
- [Redis Queue: From FIFO Lists to a Job Queue](https://upstash.com/docs/redis/tutorials/redis_queue.md): How to build FIFO, reliable, and blocking queues on Upstash Redis, then a delayed and prioritized job queue with a dead-letter queue.
- [Serverless Redisson](https://upstash.com/docs/redis/tutorials/redisson.md): This tutorial shows how to use Upstash with Redisson client.
- [Roadmap Voting App with Serverless Redis](https://upstash.com/docs/redis/tutorials/roadmapvotingapp.md): This is a single page application powered by upstash and next.js.
- [Serverless API with Java and Redis](https://upstash.com/docs/redis/tutorials/serverless_java_redis.md)
- [TanStack AI Chat Persistance](https://upstash.com/docs/redis/tutorials/tanstack_chat_persistence.md): Use Upstash Redis to persist TanStack AI chat histories across reloads, navigation, and devices with a simple adapter.
- [Using AWS SAM](https://upstash.com/docs/redis/tutorials/using_aws_sam.md)
- [Serverless Redis on Google Cloud Functions](https://upstash.com/docs/redis/tutorials/using_google_cloud_functions.md)
- [Using Serverless Framework](https://upstash.com/docs/redis/tutorials/using_serverless_framework.md)
