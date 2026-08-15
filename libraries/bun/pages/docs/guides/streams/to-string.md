---
title: "Convert a ReadableStream to a string"
source: https://bun.com/docs/guides/streams/to-string
path: docs/guides/streams/to-string
---

Bun provides several conveniences for reading the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into other formats. To read a stream into a string, call its `text()` method.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream = new ReadableStream();
const str = await stream.text();
```

`Bun.readableStreamToText(stream)` does the same thing, but is deprecated in favor of `stream.text()`.

***

See [Bun's other `ReadableStream` conversion functions](/docs/runtime/utils#bun-readablestreamto).
