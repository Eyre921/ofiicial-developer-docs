---
title: "Upstash Redis Use Cases"
source: https://upstash.com/docs/redis/overall/usecases
path: docs/redis/overall/usecases
---

The data store behind Upstash is [compatible](/docs/redis/overall/compatibility)
with almost all Redis® API. So you can use Upstash for the Redis®' popular use
cases such as:

* General caching
* Session caching
* Rate limiting (see [`@upstash/ratelimit`](https://github.com/upstash/ratelimit))
* Queues and background jobs (works with [Sidekiq](/docs/redis/integrations/sidekiq), [BullMQ](/docs/redis/integrations/bullmq), [effect-mq](/docs/redis/integrations/effect-mq), [Celery](/docs/redis/integrations/celery))
* Distributed locking
* Pub/Sub
* Feature flags
* Full-text search inside Redis with [Upstash Redis Search](/docs/redis/search/introduction) (auto-synced, works with JSON, Hashes, and Strings out of the box)
* Leaderboards
* Recommendations
* Usage metering (counting)
* Content filtering
* LLM response caching, chat history, and agent memory for AI applications

Upstash runs anywhere your application runs: traditional servers and containers (EC2, Render, Fly.io, Railway, Kubernetes) over native Redis TCP, serverless functions (AWS Lambda, Vercel Functions, Google Cloud Functions) over TCP or REST, and edge runtimes (Cloudflare Workers, Vercel Edge, Deno Deploy) over the REST API.

Check Salvatore's [blog](http://antirez.com/post/take-advantage-of-redis-adding-it-to-your-stack.html) post. You can find lots of similar articles about the common use cases of Redis.

## Key Value Store and Caching for Next.js Application

Next.js is increasingly becoming the preferred method for developing dynamic and fast web applications in an agile manner. It owes its popularity to its server-side rendering capabilities and API routes supported by serverless functions, including Vercel serverless and edge functions. Upstash Redis is a great fit with Next.js applications due to its serverless model and its REST-based APIs. The REST API plays a critical role in enabling access from edge functions while also addressing connection issues in serverless functions.

Check the blog post:
[Speed up your Next.js application with Redis](https://upstash.com/blog/nextjs-caching-with-redis)

## Redis for Vercel Functions

Vercel stands out as one of the most popular cloud platform for web developers, offering continuous integration, deployment, CDN and serverless functions. However, when it comes to databases, you'll need to rely on external data services to support dynamic applications.

That's where Upstash comes into play as one of the most favored data solutions within the Vercel platform. Here are some reasons that contribute to Upstash's popularity in the Vercel ecosystem:

* No connection problems thanks to
  [Upstash SDK](https://github.com/upstash/upstash-redis) built on Upstash REST
  API.
* Edge runtime does not allow TCP based connections. You can not use regular
  Redis clients. [Upstash SDK](https://github.com/upstash/upstash-redis) works
  on edge runtimes without a problem.
* Upstash has a [Vercel add on](https://vercel.com/integrations/upstash) where
  you can easily integrate Upstash to your Vercel projects.

## Storage For Lambda Functions (FaaS)

People use Lambda functions for various reasons, with one of the primary advantages being their cost-effectiveness – you only pay for what you actually use, which is great. However, when it comes to needing a storage layer, AWS recommends DynamoDB. DynamoDB does offer a serverless mode, which sounds promising until you encounter its latency when connecting and operating within Lambda Functions. Unfortunately, DynamoDB's latency may not be ideal for Lambda Functions, where every second of latency can have a significant impact on costs. At this point, AWS suggests using ElastiCache for low-latency data storage, which is also a Redis® cache as a service – a positive aspect. However, it's worth noting that ElastiCache is not serverless, and you have to pay based on what you provision, rather than what you use. To be honest, the pricing may not be the most budget-friendly option. This leaves you with two alternatives:

* DynamoDB: Serverless but high latency
* ElastiCache: Low latency but not serverless.

Until you meet the Upstash. Our sole mission is to provide a Redis® API
compatible database that you love in the serverless model. In Upstash, you pay
per the number of requests you have sent to your database. So if you are not
using the database you pay almost nothing. (Almost, because we charge for the
storage. It is a very low amount but still it is there.)

We believe that Upstash is the best storage for your Lambda Functions because:

* Serverless just like Lambda functions itself
* Designed for low latency data access
* The lovely simple Redis® API

## Detailed Tutorials

<CardGroup cols={2}>
  <Card
    title="Building Analytics with Redis"
    icon="chart-line"
    href="https://upstash.com/blog/building-analytics-with-redis"
  >
    Count and query events with counters, bitmaps, and Redis Search
  </Card>
  <Card
    title="Agent Memory with Redis Search"
    icon="brain"
    href="/redis/tutorials/agent_memory"
  >
    Short-term and long-term memory for AI agents on Upstash Redis
  </Card>
  <Card
    title="Caching in Laravel with Redis"
    icon="laravel"
    href="/redis/tutorials/laravel_caching"
  >
    Speed up your Laravel application with Upstash Redis caching
  </Card>
  <Card
    title="Cloudflare Workers with Websockets and Redis"
    icon="cloudflare"
    href="/redis/tutorials/cloudflare_websockets_redis"
  >
    Build realtime apps on Cloudflare Workers backed by Upstash Redis
  </Card>
</CardGroup>

- [Upstash Redis with AWS Lambda (TypeScript)](https://upstash.com/docs/redis/quickstarts/aws-lambda.md): Deploy a TypeScript AWS Lambda function with the AWS CDK that uses Upstash Redis through @upstash/redis to keep a counter.
- [Upstash Redis with Azure Functions](https://upstash.com/docs/redis/quickstarts/azure-functions.md): Create a TypeScript Azure Functions app that uses Upstash Redis with @upstash/redis, set up resources with the Azure CLI, and deploy with Azure Functions Core Tools.
- [Upstash Redis with Cloudflare Workers](https://upstash.com/docs/redis/quickstarts/cloudflareworkers.md): Create a Cloudflare Workers app with C3 that connects to Upstash Redis over HTTP with @upstash/redis, then deploy it to Cloudflare.
- [Upstash Redis with Deno Deploy](https://upstash.com/docs/redis/quickstarts/deno-deploy.md): Build a view counter on Deno Deploy that stores its count in Upstash Redis using @upstash/redis.
- [Upstash Redis with DigitalOcean](https://upstash.com/docs/redis/quickstarts/digitalocean.md): Connect DigitalOcean App Platform apps and Droplets to a standard Upstash Redis database with REDIS_URL, and migrate from the deprecated Marketplace add-on (shut down August 31, 2026).
- [Upstash Redis with Django](https://upstash.com/docs/redis/quickstarts/django.md): Build a Django app that uses Upstash Redis through upstash-redis to count homepage visits.
- [Upstash Redis with Elixir](https://upstash.com/docs/redis/quickstarts/elixir.md): Tutorial on Using Upstash Redis In Your Phoenix App and Deploying it on Fly.
- [Upstash Redis with Express (Node.js)](https://upstash.com/docs/redis/quickstarts/express.md): Add a Redis cache to an Express app with ioredis, run it locally, then deploy it to any host (Render, Railway, Fly.io, DigitalOcean, a VPS or Docker) by setting REDIS_URL.
- [Upstash Redis with FastAPI](https://upstash.com/docs/redis/quickstarts/fastapi.md): Build a FastAPI app that uses Upstash Redis through upstash-redis to count requests.
- [Upstash Redis with Fastly Compute](https://upstash.com/docs/redis/quickstarts/fastlycompute.md): Connect a Fastly Compute app to a global Upstash Redis database with @upstash/redis to serve data from the edge.
- [Upstash Redis with Flask](https://upstash.com/docs/redis/quickstarts/flask.md): Build a Flask app that uses Upstash Redis through upstash-redis to count homepage visits.
- [Upstash Redis with Fly.io](https://upstash.com/docs/redis/quickstarts/fly.md): Connect an app running on Fly.io to Upstash Redis, either through Fly's native Upstash integration or a standard Upstash database.
- [Upstash Redis with Google Cloud Run functions](https://upstash.com/docs/redis/quickstarts/google-cloud-functions.md): Deploy a Google Cloud Run function that connects to Upstash Redis with @upstash/redis and increments a counter on every request.
- [Upstash Redis with Koyeb](https://upstash.com/docs/redis/quickstarts/koyeb.md): Connect a Node.js Express app on Koyeb to Upstash Redis with @upstash/redis, then deploy it from a Git repository or a Docker container.
- [Upstash Redis with Laravel](https://upstash.com/docs/redis/quickstarts/laravel.md): Use Upstash Redis in a Laravel app with Predis or PhpRedis, including the Redis facade and Laravel's cache, session and queue drivers.
- [Upstash Redis with Netlify](https://upstash.com/docs/redis/quickstarts/netlify.md): Use Upstash Redis from Netlify Functions and Netlify Edge Functions with the HTTP-based @upstash/redis SDK and environment variables set in Netlify.
- [Upstash Redis with Next.js (App Router)](https://upstash.com/docs/redis/quickstarts/nextjs-app-router.md): Use Upstash Redis in a Next.js App Router project with @upstash/redis: add your credentials, create a client, and build a simple counter.
- [Upstash Redis with Next.js (Pages Router)](https://upstash.com/docs/redis/quickstarts/nextjs-pages-router.md): Use Upstash Redis in a Next.js Pages Router project with @upstash/redis: create a database, connect over HTTP, and build a simple counter.
- [Upstash Redis with AWS Lambda (Python)](https://upstash.com/docs/redis/quickstarts/python-aws-lambda.md): Deploy a Python AWS Lambda function with the AWS CDK that uses Upstash Redis through upstash-redis to keep a counter.
- [Upstash Redis with Render](https://upstash.com/docs/redis/quickstarts/render.md): Connect a Render Web Service, Background Worker or Cron Job to Upstash Redis with any standard Redis client by setting REDIS_URL.
- [Upstash Redis with SST](https://upstash.com/docs/redis/quickstarts/sst.md): Deploy an SST app on AWS that connects to Upstash Redis with @upstash/redis and keeps a counter.
- [Upstash Redis with Supabase Edge Functions](https://upstash.com/docs/redis/quickstarts/supabase.md): Use Upstash Redis from Supabase Edge Functions to keep a hash of function invocation counts per region.
- [Upstash Redis with Vercel Functions (App Router)](https://upstash.com/docs/redis/quickstarts/vercel-functions-app-router.md): Connect Vercel Functions in a Next.js App Router project to Upstash Redis with @upstash/redis, then deploy the counter example to Vercel.
- [Upstash Redis with Vercel Functions (Pages Router)](https://upstash.com/docs/redis/quickstarts/vercel-functions-pages-router.md): Connect Vercel Functions in a Next.js Pages Router project to Upstash Redis with @upstash/redis, then deploy the counter example to Vercel.
- [Upstash Redis with the Vercel Python Runtime](https://upstash.com/docs/redis/quickstarts/vercel-python-runtime.md): Use Upstash Redis from the Vercel Python runtime with upstash-redis, using a Django counter app that you can adapt to Flask or FastAPI.
