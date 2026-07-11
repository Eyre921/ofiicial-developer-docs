---
title: "Overview"
source: https://upstash.com/docs/redis/sdks/ts/overview
path: docs/redis/sdks/ts/overview
---

[@upstash/redis](https://github.com/upstash/redis-js)
is an HTTP/REST based Redis client built on top of
[Upstash REST API](/docs/redis/features/restapi).

[![Tests]()](https://github.com/upstash/redis-js/actions/workflows/tests.yaml)
![npm (scoped)]()
![npm bundle size]()

It is the only connectionless (HTTP based) Redis client and designed for:

* Serverless functions (AWS Lambda)
* Cloudflare Workers (see
  [the example](https://github.com/upstash/redis-js/tree/main/examples/cloudflare-workers))
* Fastly Compute@Edge (see
  [the example](https://github.com/upstash/redis-js/tree/main/examples/fastly))
* Next.js (see [the quickstart](/docs/redis/quickstarts/nextjs-app-router)), Jamstack
* Client side web/mobile applications
* WebAssembly
* and other environments where HTTP is preferred over TCP.

See
[the list of APIs](/docs/redis/features/restapi#rest-redis-api-compatibility)
supported by the Upstash REST API. For typed `@upstash/redis` command helpers,
see the [TypeScript SDK command reference](/docs/redis/sdks/ts/commands/overview).
