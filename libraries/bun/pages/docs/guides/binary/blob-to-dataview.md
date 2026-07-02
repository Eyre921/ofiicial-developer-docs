---
title: "Convert a Blob to a DataView"
source: https://bun.com/docs/guides/binary/blob-to-dataview
path: docs/guides/binary/blob-to-dataview
---

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides several methods for consuming its contents in different formats. Read the contents into an `ArrayBuffer` with `.arrayBuffer()`, then create a `DataView` from the buffer.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const blob = new Blob(["hello world"]);
const arr = new DataView(await blob.arrayBuffer());
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
