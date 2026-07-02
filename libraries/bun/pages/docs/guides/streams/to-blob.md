---
title: "Convert a ReadableStream to a Blob"
source: https://bun.com/docs/guides/streams/to-blob
path: docs/guides/streams/to-blob
---

`Bun.readableStreamToBlob` reads the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into a `Blob`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream = new ReadableStream();
const blob = await Bun.readableStreamToBlob(stream);
```

***

See [Bun's other `ReadableStream` conversion functions](/docs/runtime/utils#bun-readablestreamto).
