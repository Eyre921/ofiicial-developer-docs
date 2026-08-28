---
title: "Advanced"
source: https://upstash.com/docs/vector/sdks/ts/advanced
path: docs/vector/sdks/ts/advanced
---

## Request Timeout

You can configure the SDK so that it will throw an error if the request takes longer than a specified time.

You can achieve this using the signal parameter like this:

```ts

const index = new Index({
  url: "<UPSTASH_VECTOR_REST_URL>",
  token: "<UPSTASH_VECTOR_REST_TOKEN>",
  // set a timeout of 1 second
  signal: () => AbortSignal.timeout(1000),
});

try {
  await index.query({ ... })
} catch (error) {
  if (error.name === "TimeoutError") {
    console.error("Request timed out");
  } else {
    console.error("An error occurred:", error);
  }
}
```

## Telemetry

This sdk sends anonymous telemetry data to help us improve your experience.
We collect the following:

* SDK version
* Platform (Cloudflare, AWS or Vercel)
* Runtime version (node@18.x)

You can opt out by setting the `UPSTASH_DISABLE_TELEMETRY` environment variable
to any truthy value.

```sh
UPSTASH_DISABLE_TELEMETRY=1
```

- [Delete](https://upstash.com/docs/vector/sdks/ts/commands/delete.md)
- [Fetch](https://upstash.com/docs/vector/sdks/ts/commands/fetch.md)
- [Info](https://upstash.com/docs/vector/sdks/ts/commands/info.md)
- [Query](https://upstash.com/docs/vector/sdks/ts/commands/query.md)
- [Range](https://upstash.com/docs/vector/sdks/ts/commands/range.md)
- [Reset](https://upstash.com/docs/vector/sdks/ts/commands/reset.md)
- [Resumable Query](https://upstash.com/docs/vector/sdks/ts/commands/resumable-query.md)
- [Upsert](https://upstash.com/docs/vector/sdks/ts/commands/upsert.md)
