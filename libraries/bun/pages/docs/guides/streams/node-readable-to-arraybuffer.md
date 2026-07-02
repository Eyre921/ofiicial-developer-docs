---
title: "Convert a Node.js Readable to an ArrayBuffer"
source: https://bun.com/docs/guides/streams/node-readable-to-arraybuffer
path: docs/guides/streams/node-readable-to-arraybuffer
---

To convert a Node.js `Readable` stream to an `ArrayBuffer` in Bun, create a `Response` with the stream as the body, then call `arrayBuffer()`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
import { Readable } from "stream";
const stream = Readable.from(["Hello, ", "world!"]);
const buf = await new Response(stream).arrayBuffer();
```
