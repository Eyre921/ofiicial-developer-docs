---
title: "Convert a ReadableStream to an array of chunks"
source: https://bun.com/docs/guides/streams/to-array
path: docs/guides/streams/to-array
---

`Bun.readableStreamToArray` reads the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into an array of chunks.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream = new ReadableStream();
const chunks = await Bun.readableStreamToArray(stream);
```

***

See [Bun's other `ReadableStream` conversion functions](/docs/runtime/utils#bun-readablestreamto).
