---
title: "Convert a Buffer to an ArrayBuffer"
source: https://bun.com/docs/guides/binary/buffer-to-arraybuffer
path: docs/guides/binary/buffer-to-arraybuffer
---

The Node.js [`Buffer`](https://nodejs.org/api/buffer.html) class views and manipulates data in an underlying `ArrayBuffer`. The `buffer` property returns that `ArrayBuffer`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const nodeBuf = Buffer.alloc(64);
const arrBuf = nodeBuf.buffer;
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
