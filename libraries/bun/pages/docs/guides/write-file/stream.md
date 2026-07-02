---
title: "Write a ReadableStream to a file"
source: https://bun.com/docs/guides/write-file/stream
path: docs/guides/write-file/stream
---

To write a `ReadableStream` to disk, create a `Response` from the stream and pass it to [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write).

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream: ReadableStream = ...;
const path = "./file.txt";
const response = new Response(stream);

await Bun.write(path, response);
```

***

See [`Bun.write()`](/docs/runtime/file-io#writing-files-bun-write).
