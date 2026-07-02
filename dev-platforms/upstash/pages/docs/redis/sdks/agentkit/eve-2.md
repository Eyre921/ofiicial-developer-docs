---
title: "Memory, RAG, Rate Limiting & Sandboxes for the Vercel Eve Agent Framework"
source: https://upstash.com/docs/redis/sdks/agentkit/eve
path: docs/redis/sdks/agentkit/eve
---

[Upstash AgentKit](https://github.com/upstash/agentkit) builds AI agents on Upstash Redis: memory,
conversation history, caching, and RAG, with no separate vector database. The semantic features run on
[Upstash Redis Search](/docs/redis/search/introduction) and its `$smart` fuzzy operator.

`@upstash/agentkit-eve` brings AgentKit to **Eve, the Vercel agent framework**. You drop these into your
`agent/` tree:

| Import | Feature |
| --- | --- |
| `defineMemoryRecallTool` / `defineMemorySaveTool` | Long-term memory tools the model reads and writes. |
| `defineSearchTools` | `search` / `aggregate` / `count` tools over a Redis Search index (this is how you do RAG). |
| `createRateLimitAuth` | A rate-limit gate for your channel's `auth` walk. |
| `upstash` (`@upstash/agentkit-eve/sandbox`) | Upstash Box sandbox backend for `defineSandbox`. |
| `defineCachedTool` | A `defineTool` whose result is memoized in Redis. |

Start from an eve project. Scaffold one (it installs `eve` and an AI-SDK provider for you):

```bash
npx eve@latest init my-agent
# or, to start with a Next.js app:
npx eve@latest init my-agent --channel-web-nextjs
```

Then add the AgentKit packages:

```bash
npm install @upstash/agentkit-eve @upstash/redis
# only if you use the sandbox backend:
npm install @upstash/box
```

AgentKit reads `UPSTASH_REDIS_REST_URL` / `UPSTASH_REDIS_REST_TOKEN` from the environment by default.

## How to add memory tools to Vercel Eve

Long-term memory the model reads and writes itself: `recall_memory` and `save_memory`, one file each.

```ts
// agent/tools/recall_memory.ts
import { defineMemoryRecallTool } from "@upstash/agentkit-eve";

export default defineMemoryRecallTool({
  userId: (_, ctx) => ctx.session.auth.current?.principalId ?? ctx.session.id,
});
```

```ts
// agent/tools/save_memory.ts
import { defineMemorySaveTool } from "@upstash/agentkit-eve";

export default defineMemorySaveTool({
  userId: (_, ctx) => ctx.session.auth.current?.principalId ?? ctx.session.id,
});
```

<Accordion title="Options and the userId tenant boundary">
  * **`userId`** _(required)_ — a string, or `(input, ctx) => string`.
  * `topK` — max memories `recall` returns.
  * `minScore` — BM25 relevance floor.
  * `redis` — defaults to `Redis.fromEnv()`.

  `userId` is the only tenant boundary (required, non-empty, no `:`). Derive it from Eve's **verified
  session auth** — `ctx.session.auth.current?.principalId` — not from anything the client supplies.
  Configure a real authenticator (`vercelOidc()`, an OIDC/JWT provider like Clerk, …) so `principalId`
  is trustworthy; the `?? ctx.session.id` fallback only applies to unauthenticated requests. Memories
  are stored at `agentkit:memory:<userId>:<id>`.
</Accordion>

## How to add RAG to Vercel Eve

`search` / `aggregate` / `count` Eve tools over an Upstash Redis Search index. It is the counterpart to the
[AI SDK adapter's](/docs/redis/sdks/agentkit/ai-sdk#how-to-add-rag-with-the-ai-sdk)
`createSearchTools`. Descriptions are generated from your schema.

```ts
// agent/tools/search_books.ts
import { s } from "@upstash/redis";
import { defineSearchTools } from "@upstash/agentkit-eve";

export default defineSearchTools({
  schema: s.object({ title: s.string(), author: s.string().noTokenize(), year: s.number() }),
  indexName: "books",
}).search; // aggregate_books.ts → .aggregate, count_books.ts → .count
```

<Accordion title="Options and the one-file-per-tool rule">
  * **`schema`** _(required)_ — built with `s` from `@upstash/redis`.
  * `indexName` — defaults to `"agentkit:search"`; ties all three tools to one index.
  * `prefix` — key prefix for indexed JSON docs (defaults to `"<indexName>:"`).
  * `defaultLimit` — default page size for `search` (10).
  * `redis` — defaults to `Redis.fromEnv()`.

  Each tool file must be self-contained, so call `defineSearchTools` in each one and export the member
  you want — repeat the same `schema` + `indexName` across `search_books.ts` / `aggregate_books.ts` /
  `count_books.ts`. The index is created reactively on first use, and each returned tool is already
  `defineTool`-branded.
</Accordion>

## How to add rate limiting to Vercel Eve

A ready `AuthFn` that throttles inbound requests. Drop it into your channel's
[auth walk](https://eve.dev/docs/guides/auth-and-route-protection) ahead of your real authenticators.

```ts
// agent/channels/eve.ts
import { createRateLimitAuth, Ratelimit } from "@upstash/agentkit-eve";
import { localDev, vercelOidc } from "eve/channels/auth";
import { eveChannel } from "eve/channels/eve";

export default eveChannel({
  auth: [
    createRateLimitAuth({
      limiter: Ratelimit.slidingWindow(20, "1 m"),
      identifier: (req) => req.headers.get("x-forwarded-for") ?? "anonymous",
    }),
    localDev(),
    vercelOidc(),
  ],
});
```

<AccordionGroup>
  <Accordion title="Options and the required identifier">
    * **`limiter`** _(required)_ — e.g. `Ratelimit.slidingWindow(20, "1 m")` or `fixedWindow(...)`.
    * **`identifier`** _(required)_ — a string, or `(request) => string`. There's no implicit `"global"`:
      one shared bucket lets a single abusive caller exhaust the window for everyone, so derive it per
      request (an auth user id, an API key, or `x-forwarded-for` for per-IP).
    * `prefix` — base key prefix; keys are `<prefix>:<identifier>` (default `agentkit:rateLimit`).
    * `message` — 403 body when over the limit.
    * `redis` — defaults to `Redis.fromEnv()`.

    It's a gate: under the limit it returns `null` to fall through to the next `AuthFn`; over it throws
    a 403.
  </Accordion>
  <Accordion title="Why only POST requests are counted">
    Eve runs each turn as two authenticated requests: the message `POST` (which invokes the model) and a
    follow-up `GET …/stream` that opens the reply stream. The auth walk runs on both, so counting both
    would charge every turn twice. `createRateLimitAuth` counts only the `POST`s, so one turn costs one
    token: a `Ratelimit.slidingWindow(20, "1 m")` allows 20 turns per minute, not 10. The session-read
    `GET`s pass through unthrottled.
  </Accordion>
</AccordionGroup>

## How to add a sandbox to Vercel Eve

A drop-in replacement for Eve's `vercel()` backend, powered by
[Upstash Box](https://github.com/upstash/box). Swap the import and keep the rest of your
[sandbox file](https://eve.dev/docs/sandbox) the same.

```ts
// agent/sandbox.ts
import { defineSandbox } from "eve/sandbox";
import { upstash } from "@upstash/agentkit-eve/sandbox"; // was: eve/sandbox/vercel

export default defineSandbox({
  backend: upstash({ runtime: "node", size: "medium" }),
  revalidationKey: () => "repo-bootstrap-v1",
  async bootstrap({ use }) {
    const sandbox = await use({ networkPolicy: "allow-all" }); // open egress to install packages
    await sandbox.run({ command: "apt-get install -y jq" });
  },
  async onSession({ use }) {
    await use(); // inherits the secure deny-all default
  },
});
```

<AccordionGroup>
  <Accordion title="Config: Box's BoxConfig">
    `upstash(config)` takes the `@upstash/box` `BoxConfig` verbatim — whatever you'd pass to
    `Box.create({...})`: `runtime`, `size`, `apiKey` (defaults to `UPSTASH_BOX_API_KEY`), `keepAlive`,
    `initCommand`, `env`, `skills`, `mcpServers`, `timeout`, … — plus an optional `redis` (defaults to
    `Redis.fromEnv()`). `networkPolicy` is **not** a config knob (see below). `@upstash/box` is an
    optional peer dependency — only needed when you import `@upstash/agentkit-eve/sandbox`.
  </Accordion>
  <Accordion title="Security: network egress is deny-all by default">
    The sandbox runs untrusted, model-generated code, so open egress would mean SSRF / data
    exfiltration / reaching your own infrastructure from inside the box. Open it per-session — in
    `bootstrap`'s `use(...)` or the session `use(...)` — never as a config knob. Note that `env` passed
    to `upstash({ env })` is readable by code running in the box; don't pass secrets you wouldn't want
    it to see.
  </Accordion>
  <Accordion title="Brokering credentials (injecting headers)">
    Box network policies are plain domain/CIDR allow-lists. Eve's per-domain firewall rules (`transform`
    header injection, `forwardURL`) have no Box equivalent, so passing them in `use({ networkPolicy })`
    **throws** rather than silently sending the request unauthenticated:

    ```ts
    // ❌ throws — Box can't inject headers via a per-session policy
    export default defineSandbox({
      backend: upstash({ runtime: "node" }),
      async onSession({ use }) {
        await use({
          networkPolicy: {
            allow: { "api.example.com": [{ transform: [{ headers: { authorization: "Bearer …" } }] }] },
          },
        });
      },
    });
    ```

    Broker credentials with Box's `attachHeaders` instead (set at backend creation; a proxy on the box
    injects them), and open the domain with a plain allow-list:

    ```ts
    // ✅ headers injected at the firewall; the secret never enters the box
    export default defineSandbox({
      backend: upstash({
        runtime: "node",
        attachHeaders: { "api.example.com": { Authorization: "Bearer …" } },
      }),
      async onSession({ use }) {
        await use({ networkPolicy: { allow: ["api.example.com"] } });
      },
    });
    ```
  </Accordion>
  <Accordion title="Lifecycle: one box per conversation">
    **Reuse** — Eve re-opens a session several times per turn; the backend reattaches to the same Box
    instead of creating a new one each time. Boxes default to Box's pause-based idle lifecycle
    (`keepAlive: false`) — auto-paused when idle, resumed on reattach, reaped by Box. Pass
    `keepAlive: true` only for an always-running box you manage yourself.

    **Template registry** — Eve builds your template (seed files + `bootstrap`) at build/startup, but
    session creation runs per request in a different process, so the snapshot id is stored in a durable
    Redis registry (`redis`, defaulting to `Redis.fromEnv()`). Eve roots its tools at `/workspace` while
    a Box session lives at `/workspace/home`; the backend bridges the two automatically.
  </Accordion>
</AccordionGroup>

## How to cache tools in Vercel Eve

Like Eve's `defineTool`, but the `execute` result is memoized in Redis.

```ts
// agent/tools/get_weather.ts
import { z } from "zod";
import { defineCachedTool } from "@upstash/agentkit-eve";

export default defineCachedTool({
  description: "Get the current weather for a city.",
  inputSchema: z.object({ city: z.string() }),
  execute: async ({ city }) => fetchWeather(city),
  toolName: "get_weather",
  userId: (_, ctx) => ctx.session.auth.current?.principalId ?? ctx.session.id,
});
```

<Accordion title="Options">
  * `description` / `inputSchema` / `execute` — the usual `defineTool` fields; `execute`'s result is memoized.
  * **`toolName`** _(required)_ — the tool segment of the cache key.
  * **`userId`** _(required)_ — a string, or `(input, ctx) => string`; scopes the cache per user.
  * `ttlSeconds` — per-result TTL (default: no expiry).
  * `redis` — defaults to `Redis.fromEnv()`.

  Keys are `agentkit:toolCache:<userId>:<toolName>:<hash>`.
</Accordion>

## Working with Eve's `agent/` files

Eve's runtime snapshots each tool/channel/hook file and resolves only **package** imports from it — it
does **not** include shared `agent/`-source modules (e.g. a `agent/lib/redis.ts`). So inside `agent/`:

* Import only from packages, never from other `agent/` files.
* Lean on the defaults — **`redis` defaults to `Redis.fromEnv()`** in every helper, so you almost never pass it.
* Repeat config (schema, names) per file rather than sharing a module.

Shared app code (e.g. a seeder a page calls) lives in your project `lib/`, imported by the app — not by
`agent/` files.

## How to run the Vercel Eve example app

A complete `eve` agent app (memory, search, cached tools, a rate-limit gate, and an Upstash Box sandbox,
with a chat UI that renders tool calls inline) lives in
[`examples/eve-demo`](https://github.com/upstash/agentkit/tree/main/examples/eve-demo).

<CardGroup cols={2}>
  <Card title="AgentKit on GitHub" icon="github" href="https://github.com/upstash/agentkit">
    Source, packages, and the full example apps.
  </Card>
  <Card title="Eve" icon="up-right-from-square" href="https://eve.dev">
    The Vercel agent framework this adapter targets.
  </Card>
</CardGroup>

- [ECHO](https://upstash.com/docs/redis/sdks/py/commands/auth/echo.md)
- [PING](https://upstash.com/docs/redis/sdks/py/commands/auth/ping.md): Send a ping to the server and get a response if the server is alive.
- [BITCOUNT](https://upstash.com/docs/redis/sdks/py/commands/bitmap/bitcount.md): Count the number of set bits.
- [BITFIELD](https://upstash.com/docs/redis/sdks/py/commands/bitmap/bitfield.md): Sets or gets parts of a bitfield
- [BITOP](https://upstash.com/docs/redis/sdks/py/commands/bitmap/bitop.md): Perform bitwise operations between strings.
- [BITPOS](https://upstash.com/docs/redis/sdks/py/commands/bitmap/bitpos.md): Find the position of the first set or clear bit (bit with a value of 1 or 0) in a Redis string key.
- [GETBIT](https://upstash.com/docs/redis/sdks/py/commands/bitmap/getbit.md): Retrieve a single bit.
- [SETBIT](https://upstash.com/docs/redis/sdks/py/commands/bitmap/setbit.md): Set a single bit in a string.
- [CLIENT SETINFO](https://upstash.com/docs/redis/sdks/py/commands/connection/client_setinfo.md): Set client library name and version information.
- [DEL](https://upstash.com/docs/redis/sdks/py/commands/generic/del.md): Removes the specified keys. A key is ignored if it does not exist.
- [EXISTS](https://upstash.com/docs/redis/sdks/py/commands/generic/exists.md): Check if a key exists.
- [EXPIRE](https://upstash.com/docs/redis/sdks/py/commands/generic/expire.md): Sets a timeout on key. The key will automatically be deleted.
- [EXPIREAT](https://upstash.com/docs/redis/sdks/py/commands/generic/expireat.md): Sets a timeout on key. The key will automatically be deleted.
- [KEYS](https://upstash.com/docs/redis/sdks/py/commands/generic/keys.md): Returns all keys matching pattern.
- [PERSIST](https://upstash.com/docs/redis/sdks/py/commands/generic/persist.md): Remove any timeout set on the key.
- [PEXPIRE](https://upstash.com/docs/redis/sdks/py/commands/generic/pexpire.md): Sets a timeout on key. After the timeout has expired, the key will automatically be deleted.
- [PEXPIREAT](https://upstash.com/docs/redis/sdks/py/commands/generic/pexpireat.md): Sets a timeout on key. After the timeout has expired, the key will automatically be deleted.
- [PTTL](https://upstash.com/docs/redis/sdks/py/commands/generic/pttl.md): Return the expiration in milliseconds of a key.
- [RANDOMKEY](https://upstash.com/docs/redis/sdks/py/commands/generic/randomkey.md): Returns a random key from database
- [RENAME](https://upstash.com/docs/redis/sdks/py/commands/generic/rename.md): Rename a key
- [RENAMENX](https://upstash.com/docs/redis/sdks/py/commands/generic/renamenx.md): Rename a key if it does not already exist.
- [SCAN](https://upstash.com/docs/redis/sdks/py/commands/generic/scan.md): Scan the database for keys.
- [TOUCH](https://upstash.com/docs/redis/sdks/py/commands/generic/touch.md): Alters the last access time of one or more keys
- [TTL](https://upstash.com/docs/redis/sdks/py/commands/generic/ttl.md): Return the expiration in seconds of a key.
- [TYPE](https://upstash.com/docs/redis/sdks/py/commands/generic/type.md): Get the type of a key.
- [UNLINK](https://upstash.com/docs/redis/sdks/py/commands/generic/unlink.md): Removes the specified keys. A key is ignored if it does not exist.
- [HDEL](https://upstash.com/docs/redis/sdks/py/commands/hash/hdel.md): Deletes one or more hash fields.
- [HEXISTS](https://upstash.com/docs/redis/sdks/py/commands/hash/hexists.md): Checks if a field exists in a hash.
- [HEXPIRE](https://upstash.com/docs/redis/sdks/py/commands/hash/hexpire.md): Set a timeout on a hash field in seconds.
- [HEXPIREAT](https://upstash.com/docs/redis/sdks/py/commands/hash/hexpireat.md): Sets an expiration time for field(s) in a hash in seconds since the Unix epoch.
- [HEXPIRETIME](https://upstash.com/docs/redis/sdks/py/commands/hash/hexpiretime.md): Retrieves the expiration time of field(s) in a hash in seconds.
- [HGET](https://upstash.com/docs/redis/sdks/py/commands/hash/hget.md): Retrieves the value of a hash field.
- [HGETALL](https://upstash.com/docs/redis/sdks/py/commands/hash/hgetall.md): Retrieves all fields from a hash.
- [HGETDEL](https://upstash.com/docs/redis/sdks/py/commands/hash/hgetdel.md): Get and delete hash fields atomically.
- [HGETEX](https://upstash.com/docs/redis/sdks/py/commands/hash/hgetex.md): Get hash fields with expiration support.
- [HINCRBY](https://upstash.com/docs/redis/sdks/py/commands/hash/hincrby.md): Increments the value of a hash field by a given amount
- [HINCRBYFLOAT](https://upstash.com/docs/redis/sdks/py/commands/hash/hincrbyfloat.md): Increments the value of a hash field by a given float value.
- [HKEYS](https://upstash.com/docs/redis/sdks/py/commands/hash/hkeys.md): Return all field names in the hash stored at key.
- [HLEN](https://upstash.com/docs/redis/sdks/py/commands/hash/hlen.md): Returns the number of fields contained in the hash stored at key.
- [HMGET](https://upstash.com/docs/redis/sdks/py/commands/hash/hmget.md): Return the requested fields and their values.
- [HMSET](https://upstash.com/docs/redis/sdks/py/commands/hash/hmset.md): Write multiple fields to a hash.
- [HPERSIST](https://upstash.com/docs/redis/sdks/py/commands/hash/hpersist.md): Remove the expiration from one or more hash fields.
- [HPEXPIRE](https://upstash.com/docs/redis/sdks/py/commands/hash/hpexpire.md): Set a timeout on a hash field in milliseconds.
- [HPEXPIREAT](https://upstash.com/docs/redis/sdks/py/commands/hash/hpexpireat.md): Sets an expiration time for field(s) in a hash in milliseconds since the Unix epoch.
- [HPEXPIRETIME](https://upstash.com/docs/redis/sdks/py/commands/hash/hpexpiretime.md): Retrieves the expiration time of a field in a hash in milliseconds.
- [HPTTL](https://upstash.com/docs/redis/sdks/py/commands/hash/hpttl.md): Retrieves the remaining time-to-live (TTL) for field(s) in a hash in milliseconds.
- [HRANDFIELD](https://upstash.com/docs/redis/sdks/py/commands/hash/hrandfield.md): Return a random field from a hash
- [HSCAN](https://upstash.com/docs/redis/sdks/py/commands/hash/hscan.md): Scan a hash for fields.
- [HSET](https://upstash.com/docs/redis/sdks/py/commands/hash/hset.md): Write one or more fields to a hash.
- [HSETEX](https://upstash.com/docs/redis/sdks/py/commands/hash/hsetex.md): Set hash fields with expiration support.
- [HSETNX](https://upstash.com/docs/redis/sdks/py/commands/hash/hsetnx.md): Write a field to a hash but only if the field does not exist.
- [HSTRLEN](https://upstash.com/docs/redis/sdks/py/commands/hash/hstrlen.md): Returns the string length of a value in a hash.
- [HTTL](https://upstash.com/docs/redis/sdks/py/commands/hash/httl.md): Retrieves the remaining time-to-live (TTL) for field(s) in a hash in seconds.
- [HVALS](https://upstash.com/docs/redis/sdks/py/commands/hash/hvals.md): Returns all values in the hash stored at key.
- [JSON.ARRAPPEND](https://upstash.com/docs/redis/sdks/py/commands/json/arrappend.md): Append values to the array at path in the JSON document at key.
- [JSON.ARRINDEX](https://upstash.com/docs/redis/sdks/py/commands/json/arrindex.md): Search for the first occurrence of a JSON value in an array.
- [JSON.ARRINSERT](https://upstash.com/docs/redis/sdks/py/commands/json/arrinsert.md): Insert the json values into the array at path before the index (shifts to the right).
- [JSON.ARRLEN](https://upstash.com/docs/redis/sdks/py/commands/json/arrlen.md): Report the length of the JSON array at `path` in `key`.
- [JSON.ARRPOP](https://upstash.com/docs/redis/sdks/py/commands/json/arrpop.md): Remove and return an element from the index in the array. By default the last element from an array is popped.
- [JSON.ARRTRIM](https://upstash.com/docs/redis/sdks/py/commands/json/arrtrim.md): Trim an array so that it contains only the specified inclusive range of elements.
- [JSON.CLEAR](https://upstash.com/docs/redis/sdks/py/commands/json/clear.md): Clear container values (arrays/objects) and set numeric values to 0.
- [JSON.DEL](https://upstash.com/docs/redis/sdks/py/commands/json/del.md): Delete a key from a JSON document.
- [JSON.FORGET](https://upstash.com/docs/redis/sdks/py/commands/json/forget.md): Delete a key from a JSON document.
- [JSON.GET](https://upstash.com/docs/redis/sdks/py/commands/json/get.md): Get a single value from a JSON document.
- [JSON.MERGE](https://upstash.com/docs/redis/sdks/py/commands/json/merge.md): Merges the JSON value at path in key with the provided value.
- [JSON.MGET](https://upstash.com/docs/redis/sdks/py/commands/json/mget.md): Get the same path from multiple JSON documents.
- [JSON.MSET](https://upstash.com/docs/redis/sdks/py/commands/json/mset.md): Sets multiple JSON values at multiple paths in multiple keys.
- [JSON.NUMINCRBY](https://upstash.com/docs/redis/sdks/py/commands/json/numincrby.md): Increment the number value stored at `path` by number.
- [JSON.NUMMULTBY](https://upstash.com/docs/redis/sdks/py/commands/json/nummultby.md): Multiply the number value stored at `path` by number.
- [JSON.OBJKEYS](https://upstash.com/docs/redis/sdks/py/commands/json/objkeys.md): Return the keys in the object that`s referenced by path.
- [JSON.OBJLEN](https://upstash.com/docs/redis/sdks/py/commands/json/objlen.md): Report the number of keys in the JSON object at `path` in `key`.
- [JSON.RESP](https://upstash.com/docs/redis/sdks/py/commands/json/resp.md): Return the value at the path in Redis serialization protocol format.
- [JSON.SET](https://upstash.com/docs/redis/sdks/py/commands/json/set.md): Set the JSON value at path in key.
- [JSON.STRAPPEND](https://upstash.com/docs/redis/sdks/py/commands/json/strappend.md): Append the json-string values to the string at path.
- [JSON.STRLEN](https://upstash.com/docs/redis/sdks/py/commands/json/strlen.md): Report the length of the JSON String at path in key
- [JSON.TOGGLE](https://upstash.com/docs/redis/sdks/py/commands/json/toggle.md): Toggle a boolean value stored at `path`.
- [JSON.TYPE](https://upstash.com/docs/redis/sdks/py/commands/json/type.md): Report the type of JSON value at `path`.
- [LINDEX](https://upstash.com/docs/redis/sdks/py/commands/list/lindex.md): Returns the element at index index in the list stored at key.
- [LINSERT](https://upstash.com/docs/redis/sdks/py/commands/list/linsert.md): Insert an element before or after another element in a list
- [LLEN](https://upstash.com/docs/redis/sdks/py/commands/list/llen.md): Returns the length of the list stored at key.
- [LMOVE](https://upstash.com/docs/redis/sdks/py/commands/list/lmove.md): Move an element from one list to another.
- [LPOP](https://upstash.com/docs/redis/sdks/py/commands/list/lpop.md): Remove and return the first element(s) of a list
- [LPOS](https://upstash.com/docs/redis/sdks/py/commands/list/lpos.md): Returns the index of matching elements inside a list.
- [LPUSH](https://upstash.com/docs/redis/sdks/py/commands/list/lpush.md): Push an element at the head of the list.
- [LPUSHX](https://upstash.com/docs/redis/sdks/py/commands/list/lpushx.md): Push an element at the head of the list only if the list exists.
- [LRANGE](https://upstash.com/docs/redis/sdks/py/commands/list/lrange.md): Returns the specified elements of the list stored at key.
- [LREM](https://upstash.com/docs/redis/sdks/py/commands/list/lrem.md): Remove the first `count` occurrences of an element from a list.
- [LSET](https://upstash.com/docs/redis/sdks/py/commands/list/lset.md): Set a value at a specific index.
- [LTRIM](https://upstash.com/docs/redis/sdks/py/commands/list/ltrim.md): Trim a list to the specified range
- [RPOP](https://upstash.com/docs/redis/sdks/py/commands/list/rpop.md): Remove and return the last element(s) of a list
- [RPUSH](https://upstash.com/docs/redis/sdks/py/commands/list/rpush.md): Push an element at the end of the list.
- [RPUSHX](https://upstash.com/docs/redis/sdks/py/commands/list/rpushx.md): Push an element at the end of the list only if the list exists.
- [Overview](https://upstash.com/docs/redis/sdks/py/commands/overview.md): Available Commands in upstash-redis
- [PUBLISH](https://upstash.com/docs/redis/sdks/py/commands/pubsub/publish.md): Publish a message to a channel
- [EVAL](https://upstash.com/docs/redis/sdks/py/commands/scripts/eval.md): Evaluate a Lua script server side.
- [EVAL_RO](https://upstash.com/docs/redis/sdks/py/commands/scripts/eval_ro.md): Evaluate a read-only Lua script server side.
- [EVALSHA](https://upstash.com/docs/redis/sdks/py/commands/scripts/evalsha.md): Evaluate a cached Lua script server side.
- [EVALSHA_RO](https://upstash.com/docs/redis/sdks/py/commands/scripts/evalsha_ro.md): Evaluate a cached read-only Lua script server side.
- [SCRIPT EXISTS](https://upstash.com/docs/redis/sdks/py/commands/scripts/script_exists.md): Check if scripts exist in the script cache.
- [SCRIPT FLUSH](https://upstash.com/docs/redis/sdks/py/commands/scripts/script_flush.md): Removes all scripts from the script cache.
- [SCRIPT LOAD](https://upstash.com/docs/redis/sdks/py/commands/scripts/script_load.md): Load the specified Lua script into the script cache.
- [DBSIZE](https://upstash.com/docs/redis/sdks/py/commands/server/dbsize.md): Count the number of keys in the database.
- [FLUSHALL](https://upstash.com/docs/redis/sdks/py/commands/server/flushall.md)
- [FLUSHDB](https://upstash.com/docs/redis/sdks/py/commands/server/flushdb.md)
- [SADD](https://upstash.com/docs/redis/sdks/py/commands/set/sadd.md): Adds one or more members to a set.
- [SCARD](https://upstash.com/docs/redis/sdks/py/commands/set/scard.md): Return how many members are in a set
- [SDIFF](https://upstash.com/docs/redis/sdks/py/commands/set/sdiff.md): Return the difference between sets
- [SDIFFSTORE](https://upstash.com/docs/redis/sdks/py/commands/set/sdiffstore.md): Write the difference between sets to a new set
- [SINTER](https://upstash.com/docs/redis/sdks/py/commands/set/sinter.md): Return the intersection between sets
- [SINTER](https://upstash.com/docs/redis/sdks/py/commands/set/sinterstore.md): Return the intersection between sets and store the resulting set in a key
- [SISMEMBER](https://upstash.com/docs/redis/sdks/py/commands/set/sismember.md): Check if a member exists in a set
- [SMEMBERS](https://upstash.com/docs/redis/sdks/py/commands/set/smembers.md): Return all the members of a set
- [SMISMEMBER](https://upstash.com/docs/redis/sdks/py/commands/set/smismember.md): Check if multiple members exist in a set
- [SMOVE](https://upstash.com/docs/redis/sdks/py/commands/set/smove.md): Move a member from one set to another
- [SPOP](https://upstash.com/docs/redis/sdks/py/commands/set/spop.md): Removes and returns one or more random members from a set.
- [SRANDMEMBER](https://upstash.com/docs/redis/sdks/py/commands/set/srandmember.md): Returns one or more random members from a set.
- [SREM](https://upstash.com/docs/redis/sdks/py/commands/set/srem.md): Remove one or more members from a set
- [SSCAN](https://upstash.com/docs/redis/sdks/py/commands/set/sscan.md): Scan a set
- [SUNION](https://upstash.com/docs/redis/sdks/py/commands/set/sunion.md): Return the union between sets
- [SUNIONSTORE](https://upstash.com/docs/redis/sdks/py/commands/set/sunionstore.md): Return the union between sets and store the resulting set in a key
- [XACK](https://upstash.com/docs/redis/sdks/py/commands/stream/xack.md): Removes one or multiple messages from the pending entries list of a stream consumer group.
- [XACKDEL](https://upstash.com/docs/redis/sdks/py/commands/stream/xackdel.md): Acknowledge and delete stream entries atomically.
- [XADD](https://upstash.com/docs/redis/sdks/py/commands/stream/xadd.md): Appends one or more new entries to a stream.
- [XAUTOCLAIM](https://upstash.com/docs/redis/sdks/py/commands/stream/xautoclaim.md): Changes the ownership of pending messages from one consumer to another in a stream consumer group automatically.
- [XCLAIM](https://upstash.com/docs/redis/sdks/py/commands/stream/xclaim.md): Changes the ownership of pending messages from one consumer to another in a stream consumer group.
- [XDEL](https://upstash.com/docs/redis/sdks/py/commands/stream/xdel.md): Removes the specified entries from a stream, and returns the number of entries deleted.
- [XDELEX](https://upstash.com/docs/redis/sdks/py/commands/stream/xdelex.md): Extended delete for streams with reference control.
- [XGROUP CREATE](https://upstash.com/docs/redis/sdks/py/commands/stream/xgroup_create.md): Create a new consumer group for a Redis stream.
- [XGROUP CREATECONSUMER](https://upstash.com/docs/redis/sdks/py/commands/stream/xgroup_createconsumer.md): Create a new consumer in an existing consumer group.
- [XGROUP DELCONSUMER](https://upstash.com/docs/redis/sdks/py/commands/stream/xgroup_delconsumer.md): Delete a consumer from a consumer group.
- [XGROUP DESTROY](https://upstash.com/docs/redis/sdks/py/commands/stream/xgroup_destroy.md): Delete an entire consumer group.
- [XGROUP SETID](https://upstash.com/docs/redis/sdks/py/commands/stream/xgroup_setid.md): Set the last delivered ID for a consumer group.
- [XINFO CONSUMERS](https://upstash.com/docs/redis/sdks/py/commands/stream/xinfo_consumers.md): List all consumers in a consumer group.
- [XINFO GROUPS](https://upstash.com/docs/redis/sdks/py/commands/stream/xinfo_groups.md): List all consumer groups for a stream.
- [XLEN](https://upstash.com/docs/redis/sdks/py/commands/stream/xlen.md): Returns the number of entries inside a stream.
- [XPENDING](https://upstash.com/docs/redis/sdks/py/commands/stream/xpending.md): Returns information about pending messages in a stream consumer group.
- [XRANGE](https://upstash.com/docs/redis/sdks/py/commands/stream/xrange.md): Returns stream entries matching a given range of IDs.
- [XREAD](https://upstash.com/docs/redis/sdks/py/commands/stream/xread.md): Reads data from one or multiple streams, starting from the specified IDs.
- [XREADGROUP](https://upstash.com/docs/redis/sdks/py/commands/stream/xreadgroup.md): Reads data from a stream as part of a consumer group.
- [XREVRANGE](https://upstash.com/docs/redis/sdks/py/commands/stream/xrevrange.md): Returns stream entries matching a given range of IDs in reverse order.
- [XTRIM](https://upstash.com/docs/redis/sdks/py/commands/stream/xtrim.md): Trims the stream by removing entries to keep it at a reasonable size.
- [APPEND](https://upstash.com/docs/redis/sdks/py/commands/string/append.md): Append a value to a string stored at key.
- [DECR](https://upstash.com/docs/redis/sdks/py/commands/string/decr.md): Decrement the integer value of a key by one
- [DECRBY](https://upstash.com/docs/redis/sdks/py/commands/string/decrby.md): Decrement the integer value of a key by a given number.
- [GET](https://upstash.com/docs/redis/sdks/py/commands/string/get.md): Return the value of the specified key or `None` if the key doesn't exist.
- [GETDEL](https://upstash.com/docs/redis/sdks/py/commands/string/getdel.md): Return the value of the specified key and delete the key.
- [GETRANGE](https://upstash.com/docs/redis/sdks/py/commands/string/getrange.md): Return a substring of value at the specified key.
- [GETSET](https://upstash.com/docs/redis/sdks/py/commands/string/getset.md): Return the value of the specified key and replace it with a new value.
- [INCR](https://upstash.com/docs/redis/sdks/py/commands/string/incr.md): Increment the integer value of a key by one
- [INCRBY](https://upstash.com/docs/redis/sdks/py/commands/string/incrby.md): Increment the integer value of a key by a given number.
- [INCRBYFLOAT](https://upstash.com/docs/redis/sdks/py/commands/string/incrbyfloat.md): Increment the float value of a key by a given number.
- [MGET](https://upstash.com/docs/redis/sdks/py/commands/string/mget.md): Load multiple keys from Redis in one go.
- [MSET](https://upstash.com/docs/redis/sdks/py/commands/string/mset.md): Set multiple keys in one go.
- [MSETNX](https://upstash.com/docs/redis/sdks/py/commands/string/msetnx.md): Set multiple keys in one go unless they exist already.
- [SET](https://upstash.com/docs/redis/sdks/py/commands/string/set.md): Set a key to hold a string value.
- [SETRANGE](https://upstash.com/docs/redis/sdks/py/commands/string/setrange.md): Writes the value of key at offset.
- [STRLEN](https://upstash.com/docs/redis/sdks/py/commands/string/strlen.md): Return the length of a string stored at a key.
- [ZADD](https://upstash.com/docs/redis/sdks/py/commands/zset/zadd.md): Add a member to a sorted set, or update its score if it already exists.
- [ZCARD](https://upstash.com/docs/redis/sdks/py/commands/zset/zcard.md): Returns the number of elements in the sorted set stored at key.
- [ZCOUNT](https://upstash.com/docs/redis/sdks/py/commands/zset/zcount.md): Returns the number of elements in the sorted set stored at key filterd by score.
- [ZDIFF](https://upstash.com/docs/redis/sdks/py/commands/zset/zdiff.md): Returns the difference between sets.
- [ZDIFFSTORE](https://upstash.com/docs/redis/sdks/py/commands/zset/zdiffstore.md): Writes the difference between sets to a new key.
- [ZINCRBY](https://upstash.com/docs/redis/sdks/py/commands/zset/zincrby.md): Increment the score of a member.
- [ZINTER](https://upstash.com/docs/redis/sdks/py/commands/zset/zinter.md): Returns the intersection between sets.
- [ZINTERSTORE](https://upstash.com/docs/redis/sdks/py/commands/zset/zinterstore.md): Calculates the intersection of sets and stores the result in a key
- [ZLEXCOUNT](https://upstash.com/docs/redis/sdks/py/commands/zset/zlexcount.md): Returns the number of elements in the sorted set stored at key filterd by lex.
- [ZMSCORE](https://upstash.com/docs/redis/sdks/py/commands/zset/zmscore.md): Returns the scores of multiple members.
- [ZPOPMAX](https://upstash.com/docs/redis/sdks/py/commands/zset/zpopmax.md): Removes and returns up to count members with the highest scores in the sorted set stored at key.
- [ZPOPMIN](https://upstash.com/docs/redis/sdks/py/commands/zset/zpopmin.md): Removes and returns up to count members with the lowest scores in the sorted set stored at key.
- [ZRANDMEMBER](https://upstash.com/docs/redis/sdks/py/commands/zset/zrandmember.md): Returns one or more random members from a sorted set, optionally with their scores.
- [ZRANGE](https://upstash.com/docs/redis/sdks/py/commands/zset/zrange.md): Returns the specified range of elements in the sorted set stored at key.
- [ZRANK](https://upstash.com/docs/redis/sdks/py/commands/zset/zrank.md): Returns the rank of a member
- [ZREM](https://upstash.com/docs/redis/sdks/py/commands/zset/zrem.md): Remove one or more members from a sorted set
- [ZREMRANGEBYLEX](https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebylex.md): Remove all members in a sorted set between the given lexicographical range.
- [ZREMRANGEBYRANK](https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyrank.md): Remove all members in a sorted set between the given ranks.
- [ZREMRANGEBYSCORE](https://upstash.com/docs/redis/sdks/py/commands/zset/zremrangebyscore.md): Remove all members in a sorted set between the given scores.
- [ZREVRANK](https://upstash.com/docs/redis/sdks/py/commands/zset/zrevrank.md): Returns the rank of a member in a sorted set, with scores ordered from high to low.
- [ZSCAN](https://upstash.com/docs/redis/sdks/py/commands/zset/zscan.md): Scan a sorted set
- [ZSCORE](https://upstash.com/docs/redis/sdks/py/commands/zset/zscore.md): Returns the scores of a member.
- [ZINTER](https://upstash.com/docs/redis/sdks/py/commands/zset/zunion.md): Returns the intersection between sets.
- [ZUNIONSTORE](https://upstash.com/docs/redis/sdks/py/commands/zset/zunionstore.md): Writes the union between sets to a new key.
