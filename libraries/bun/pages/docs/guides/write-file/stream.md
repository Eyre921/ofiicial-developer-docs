---
title: "Write a ReadableStream to a file"
source: https://bun.com/docs/guides/write-file/stream
path: docs/guides/write-file/stream
---

To write a `ReadableStream` to disk, call `.writer()` on a `BunFile` to get a [`FileSink`](/docs/runtime/file-io#incremental-writing-with-filesink). The stream is an async iterable, so write each of its chunks to the `FileSink` with `for await`. Then call `.end()` to flush the buffer and close the file.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const stream: ReadableStream = ...;
const path = "./file.txt";
const writer = Bun.file(path).writer();

for await (const chunk of stream) {
  writer.write(chunk);
}

await writer.end();
```

***

`.writer()` creates the file if it doesn't exist, but does not truncate an existing file. If the file may already exist, delete it first.

***

See [`FileSink`](/docs/runtime/file-io#incremental-writing-with-filesink).
