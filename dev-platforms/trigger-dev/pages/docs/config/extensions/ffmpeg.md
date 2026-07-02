---
title: "FFmpeg"
source: https://trigger.dev/docs/config/extensions/ffmpeg
path: docs/config/extensions/ffmpeg
---

Use the ffmpeg build extension to include FFmpeg in your project

You can add the `ffmpeg` build extension to your build process:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { ffmpeg } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [ffmpeg()],
  },
});
```

By default, this will install the version of `ffmpeg` that is available in the Debian package manager (via `apt`).

## FFmpeg 7.x (static build)

If you need FFmpeg 7.x, you can pass `{ version: "7" }` to the extension. This will install a static build of FFmpeg 7.x instead of using the Debian package:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { ffmpeg } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [ffmpeg({ version: "7" })],
  },
});
```

This extension will also add the `FFMPEG_PATH` and `FFPROBE_PATH` to your environment variables, making it easy to use popular ffmpeg libraries like `fluent-ffmpeg`.

Note that `fluent-ffmpeg` needs to be added to [`external`](/docs/config/config-file#external) in your `trigger.config.ts` file.

Follow [this example](/docs/guides/examples/ffmpeg-video-processing) to get setup with Trigger.dev and FFmpeg in your project.
