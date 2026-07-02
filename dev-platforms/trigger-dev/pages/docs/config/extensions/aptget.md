---
title: "apt-get"
source: https://trigger.dev/docs/config/extensions/aptGet
path: docs/config/extensions/aptget
---

Use the aptGet build extension to install system packages into the deployed image

You can install system packages into the deployed image using the `aptGet` extension:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { aptGet } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [aptGet({ packages: ["ffmpeg"] })],
  },
});
```

If you want to install a specific version of a package, you can specify the version like this:

```ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [aptGet({ packages: ["ffmpeg=6.0-4"] })],
  },
});
```
