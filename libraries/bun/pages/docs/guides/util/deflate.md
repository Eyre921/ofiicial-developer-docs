---
title: "Compress and decompress data with DEFLATE"
source: https://bun.com/docs/guides/util/deflate
path: docs/guides/util/deflate
---

Use `Bun.deflateSync()` to compress a `Uint8Array` with DEFLATE.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const data = Buffer.from("Hello, world!");
const compressed = Bun.deflateSync(data);
// => Uint8Array

const decompressed = Bun.inflateSync(compressed);
// => Uint8Array
```

***

See [Utils](/docs/runtime/utils).
