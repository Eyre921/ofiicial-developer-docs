---
title: "Puppeteer build extension"
source: https://trigger.dev/docs/config/extensions/puppeteer
path: docs/config/extensions/puppeteer
---

Use the puppeteer build extension to enable support for Puppeteer in your project

> [!WARNING]
>
> **WEB SCRAPING:** When web scraping, you MUST use a proxy to comply with our terms of service. Direct scraping of third-party websites without the site owner's permission using Trigger.dev Cloud is prohibited and will result in account suspension. See [this example](/docs/guides/examples/puppeteer#scrape-content-from-a-web-page) which uses a proxy.

To use Puppeteer in your project, add these build settings to your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { puppeteer } from "@trigger.dev/build/extensions/puppeteer";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [puppeteer()],
  },
});
```

The extension installs Chrome and sets `PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable` for deployed builds automatically, so you do not need to set it. Don't set it in your Dev environment: the extension does nothing in Dev, and locally Puppeteer uses the browser it downloads on install.

Follow [this example](/docs/guides/examples/puppeteer) to get setup with Trigger.dev and Puppeteer in your project.
