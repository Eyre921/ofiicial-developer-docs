---
title: "Convert a ReadableStream to an ArrayBuffer"
source: https://bun.com/docs/guides/streams/to-arraybuffer
path: docs/guides/streams/to-arraybuffer
---

`Bun.readableStreamToArrayBuffer` reads the contents of a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) into an `ArrayBuffer`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream = new ReadableStream();
const buf = await Bun.readableStreamToArrayBuffer(stream);
```

***

See [Bun's other `ReadableStream` conversion functions](/docs/runtime/utils#bun-readablestreamto).
