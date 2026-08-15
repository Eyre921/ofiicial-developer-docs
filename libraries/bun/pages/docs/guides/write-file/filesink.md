---
title: "Write a file incrementally"
source: https://bun.com/docs/guides/write-file/filesink
path: docs/guides/write-file/filesink
---

Bun provides an API for incrementally writing to a file. Use it for large files, or when writing to a file over a long period of time.

Call `.writer()` on a `BunFile` to retrieve a `FileSink` instance. The `FileSink` buffers data. Call `.flush()` to write the buffer to disk. You can write & flush many times.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
const file = Bun.file("/path/to/file.txt");
const writer = file.writer();

writer.write("lorem");
writer.write("ipsum");
writer.write("dolor");

writer.flush();

// continue writing & flushing
```

***

The `.write()` method accepts strings or binary data.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
writer.write("hello");
writer.write(Buffer.from("there"));
writer.write(new Uint8Array([0, 255, 128]));
writer.flush();
```

***

The `FileSink` also auto-flushes when its internal buffer is full.

***

When you're done writing, call `.end()` to flush the buffer and close the file.

```ts theme={"theme":{"light":"github-light","dark":"dracula"}}
writer.end();
```

***

Full documentation: [FileSink](/docs/runtime/file-io#incremental-writing-with-filesink).
