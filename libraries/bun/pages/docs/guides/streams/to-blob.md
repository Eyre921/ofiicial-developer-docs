---
title: "Convert a ReadableStream to a Blob"
source: https://bun.com/docs/guides/streams/to-blob
path: docs/guides/streams/to-blob
---

Bun provides several conveniences for reading the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into other formats. To read a stream into a `Blob`, call its `blob()` method.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream = new ReadableStream();
const blob = await stream.blob();
```

`Bun.readableStreamToBlob(stream)` does the same thing, but is deprecated in favor of `stream.blob()`.

***

See [Bun's other `ReadableStream` conversion functions](/docs/runtime/utils#bun-readablestreamto).
