---
title: "Convert a Node.js Readable to JSON"
source: https://bun.com/docs/guides/streams/node-readable-to-json
path: docs/guides/streams/node-readable-to-json
---

To convert a Node.js `Readable` stream to a JSON object in Bun, create a [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) with the stream as the body, then call [`response.json()`](https://developer.mozilla.org/en-US/docs/Web/API/Response/json).

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
import { Readable } from "stream";
const stream = Readable.from([JSON.stringify({ hello: "world" })]);
const json = await new Response(stream).json();
console.log(json); // { hello: "world" }
```
