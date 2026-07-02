---
title: "Convert a Buffer to a string"
source: https://bun.com/docs/guides/binary/buffer-to-string
path: docs/guides/binary/buffer-to-string
---

The [`Buffer`](https://nodejs.org/api/buffer.html) class provides a `.toString()` method that converts a `Buffer` to a string.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const buf = Buffer.from("hello");
const str = buf.toString();
// => "hello"
```

***

You can optionally specify an encoding and byte range.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const buf = Buffer.from("hello world!");
const str = buf.toString("utf8", 0, 5);
// => "hello"
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).
