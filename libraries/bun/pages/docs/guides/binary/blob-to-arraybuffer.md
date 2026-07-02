---
title: "Convert a Blob to an ArrayBuffer"
source: https://bun.com/docs/guides/binary/blob-to-arraybuffer
path: docs/guides/binary/blob-to-arraybuffer
---

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides several methods for consuming its contents in different formats, including `.arrayBuffer()`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const blob = new Blob(["hello world"]);
const buf = await blob.arrayBuffer();
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
