---
title: "Convert a Uint8Array to a Buffer"
source: https://bun.com/docs/guides/binary/typedarray-to-buffer
path: docs/guides/binary/typedarray-to-buffer
---

The [`Buffer`](https://nodejs.org/api/buffer.html) class extends [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) with additional methods. Use `Buffer.from()` to create a `Buffer` instance from a `Uint8Array`.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const arr: Uint8Array = ...
const buf = Buffer.from(arr);
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
