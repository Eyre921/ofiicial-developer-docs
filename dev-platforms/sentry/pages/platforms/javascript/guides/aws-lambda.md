---
title: "AWS Lambda"
source: https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md
path: platforms/javascript/guides/aws-lambda
---

---
title: "AWS Lambda"
description: "AWS Lambda is a serverless compute service offered as part of Amazon Web Services. Learn how to set it up with Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/aws-lambda/
---

# Sentry for AWS Lambda (JavaScript)

Looking for instructions on how to add Sentry without modifying your code? [Check out these docs instead](https://docs.sentry.io/integrations/cloud-monitoring/aws-lambda.md).

On this page you'll get an overview how to install, configure and use Sentry in your AWS Lambda functions. Once set up, our SDK will automatically report error and performance data from your Lambda Functions. Issues in Sentry will automatically include cloudwatch data, function details and execution time measurements.

## [Installation](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md#installation)

Depending on your preferences, you can install Sentry in your Lambda functions using the [Sentry AWS Lambda Layer](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/install/layer.md) (recommended) or the [Sentry AWS NPM package](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/install/npm.md).

### [Should I use the Lambda Layer or the NPM package?](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md#should-i-use-the-lambda-layer-or-the-npm-package)

We generally recommend using the Lambda layer as it doesn't require you to deploy any Sentry dependency alongside your function. With the layer, you can achieve the same level of customization as with the NPM package. There are two reasons why you still might want to use the NPM package instead:

1. You want to minimize lambda function size and tree-shake parts of the SDK code that you don't need. A related reason might be because you're transpiling your code and want to transpile your dependencies as well.
2. You already use NPM packages and deploy `node_modules` with your function and you don't want to add a (or another) Lambda layer to your functions.

## [Configuration](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md#configuration)

After installing the SDK, you might want to configure some parameters. Besides the [common SDK configuration](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/configuration.md), you can also [configure Sentry's Lambda Function handler wrapper](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/configuration/lambda-wrapper.md) to optimize function runtime overhead and timeout warnings.

## [Verify](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md#verify)

Once set up, verify that Sentry is reporting errors correctly by throwing a sample error in one of your functions:

**\[CommonJS] index.js**

```javascript
exports.handler = async (event, context) => {
  throw new Error("This is a test error");
};
```

**\[ESM] index.mjs**

```javascript
import * as Sentry from "@sentry/aws-serverless";

export const handler = Sentry.wrapHandler(async (event, context) => {
  throw new Error("This is a test error");
});
```

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
- [Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md)
- [Cloud Functions for Firebase](https://docs.sentry.io/platforms/javascript/guides/firebase.md)
- [Cloudflare](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md)
- [Cordova](https://docs.sentry.io/platforms/javascript/guides/cordova.md)
- [Deno](https://docs.sentry.io/platforms/javascript/guides/deno.md)
- [Effect](https://docs.sentry.io/platforms/javascript/guides/effect.md)
- [Electron](https://docs.sentry.io/platforms/javascript/guides/electron.md)
- [Elysia](https://docs.sentry.io/platforms/javascript/guides/elysia.md)
- [Ember](https://docs.sentry.io/platforms/javascript/guides/ember.md)
- [Eve](https://docs.sentry.io/platforms/javascript/guides/eve.md)
- [Express](https://docs.sentry.io/platforms/javascript/guides/express.md)
- [Fastify](https://docs.sentry.io/platforms/javascript/guides/fastify.md)
- [Flue](https://docs.sentry.io/platforms/javascript/guides/flue.md)
- [Gatsby](https://docs.sentry.io/platforms/javascript/guides/gatsby.md)
- [Google Cloud Functions](https://docs.sentry.io/platforms/javascript/guides/gcp-functions.md)
- [Hapi](https://docs.sentry.io/platforms/javascript/guides/hapi.md)
- [Hono](https://docs.sentry.io/platforms/javascript/guides/hono.md)
- [Koa](https://docs.sentry.io/platforms/javascript/guides/koa.md)
- [Mastra](https://docs.sentry.io/platforms/javascript/guides/mastra.md)
- [Nest.js](https://docs.sentry.io/platforms/javascript/guides/nestjs.md)
- [Next.js](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)
- [Nitro](https://docs.sentry.io/platforms/javascript/guides/nitro.md)
- [Node.js](https://docs.sentry.io/platforms/javascript/guides/node.md)
- [Nuxt](https://docs.sentry.io/platforms/javascript/guides/nuxt.md)
- [Pi Durable](https://docs.sentry.io/platforms/javascript/guides/pi-durable.md)
- [React](https://docs.sentry.io/platforms/javascript/guides/react.md)
- [React Router Framework](https://docs.sentry.io/platforms/javascript/guides/react-router.md)
- [Remix](https://docs.sentry.io/platforms/javascript/guides/remix.md)
- [Solid](https://docs.sentry.io/platforms/javascript/guides/solid.md)
- [SolidStart](https://docs.sentry.io/platforms/javascript/guides/solidstart.md)
- [Svelte](https://docs.sentry.io/platforms/javascript/guides/svelte.md)
- [SvelteKit](https://docs.sentry.io/platforms/javascript/guides/sveltekit.md)
- [TanStack Start React](https://docs.sentry.io/platforms/javascript/guides/tanstackstart-react.md)
- [Vue](https://docs.sentry.io/platforms/javascript/guides/vue.md)
- [Wasm](https://docs.sentry.io/platforms/javascript/guides/wasm.md)

## Topics

- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/install.md)
- [Installation Methods](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/install__v9.x.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/logs.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/metrics.md)
- [MCP Monitoring](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/mcp-monitoring.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/profiling.md)
- [Crons](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/configuration.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/opentelemetry.md)
- [OpenTelemetry Support](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/opentelemetry__v10.x.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/data-management.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/aws-lambda/troubleshooting.md)

