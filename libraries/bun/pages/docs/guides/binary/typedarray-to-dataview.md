---
title: "Convert a Uint8Array to a DataView"
source: https://bun.com/docs/guides/binary/typedarray-to-dataview
path: docs/guides/binary/typedarray-to-dataview
---

A [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) is a *typed array*, a view over data in an underlying `ArrayBuffer`. To convert it to a `DataView`, create one over the same range of data.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const arr: Uint8Array = ...
const dv = new DataView(arr.buffer, arr.byteOffset, arr.byteLength);
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
