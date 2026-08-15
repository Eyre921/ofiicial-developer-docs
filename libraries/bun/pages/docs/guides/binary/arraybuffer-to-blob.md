---
title: "Convert an ArrayBuffer to a Blob"
source: https://bun.com/docs/guides/binary/arraybuffer-to-blob
path: docs/guides/binary/arraybuffer-to-blob
---

You can construct a [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) from an array of "chunks", where each chunk is a string, binary data structure, or another `Blob`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const buf = new ArrayBuffer(64);
const blob = new Blob([buf]);
```

***

By default the `type` of the resulting `Blob` is unset. Set it with the `type` option.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const buf = new ArrayBuffer(64);
const blob = new Blob([buf], { type: "application/octet-stream" });
blob.type; // => "application/octet-stream"
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
