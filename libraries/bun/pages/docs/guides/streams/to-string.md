---
title: "Convert a ReadableStream to a string"
source: https://bun.com/docs/guides/streams/to-string
path: docs/guides/streams/to-string
---

`Bun.readableStreamToText` reads the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into a string.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream = new ReadableStream();
const str = await Bun.readableStreamToText(stream);
```

***

See [Bun's other `ReadableStream` conversion functions](/docs/runtime/utils#bun-readablestreamto).
