---
title: "Convert a Buffer to a blob"
source: https://bun.com/docs/guides/binary/buffer-to-blob
path: docs/guides/binary/buffer-to-blob
---

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) can be constructed from an array of "chunks", where each chunk is a string, binary data structure (including `Buffer`), or another `Blob`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const buf = Buffer.from("hello");
const blob = new Blob([buf]);
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
