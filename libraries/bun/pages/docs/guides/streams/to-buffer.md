---
title: "Convert a ReadableStream to a Buffer"
source: https://bun.com/docs/guides/streams/to-buffer
path: docs/guides/streams/to-buffer
---

To convert a [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) to a `Buffer`, read its contents into an [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) with `Bun.readableStreamToArrayBuffer`, then create a [`Buffer`](https://nodejs.org/api/buffer.html) that points to it.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream = new ReadableStream();
const arrBuf = await Bun.readableStreamToArrayBuffer(stream);
const nodeBuf = Buffer.from(arrBuf);
```

***

See [Bun's other `ReadableStream` conversion functions](/docs/runtime/utils#bun-readablestreamto).
