---
title: "Convert a Node.js Readable to a Blob"
source: https://bun.com/docs/guides/streams/node-readable-to-blob
path: docs/guides/streams/node-readable-to-blob
---

To convert a Node.js `Readable` stream to a [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) in Bun, create a [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) with the stream as the body, then call [`response.blob()`](https://developer.mozilla.org/en-US/docs/Web/API/Response/blob).

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
import { Readable } from "stream";
const stream = Readable.from(["Hello, ", "world!"]);
const blob = await new Response(stream).blob();
```
