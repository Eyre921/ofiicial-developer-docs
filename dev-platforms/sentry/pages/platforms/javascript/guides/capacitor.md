---
title: "Capacitor"
source: https://docs.sentry.io/platforms/javascript/guides/capacitor.md
path: platforms/javascript/guides/capacitor
---

---
title: "Capacitor"
description: "Learn how to set up Sentry in your Capacitor application, capture your first events and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/javascript/guides/capacitor/
---

# Sentry for Capacitor

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

This guide will show you setup instructions for Angular, React, Vue, and Nuxt. If you use any other JavaScript framework (or none at all) with Capacitor, follow the vanilla instructions outlined under "Other".

## [Install](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#install-the-sentry-sdk)

Run the command for your preferred package manager to add Sentry's Capacitor SDK and the SDK for the framework you're using to your application:

**Angular**

```bash
# npm
npm install @sentry/capacitor @sentry/angular --save

# yarn
yarn add @sentry/capacitor @sentry/angular

# pnpm
pnpm add @sentry/capacitor @sentry/angular
```

**React**

```bash
# npm
npm install @sentry/capacitor @sentry/react --save

# yarn
yarn add @sentry/capacitor @sentry/react

# pnpm
pnpm add @sentry/capacitor @sentry/react
```

**Vue**

```bash
# npm
npm install @sentry/capacitor @sentry/vue --save

# yarn
yarn add @sentry/capacitor @sentry/vue

# pnpm
pnpm add @sentry/capacitor @sentry/vue
```

**Nuxt**

```bash
# npm
npm install @sentry/capacitor @sentry/nuxt --save

# yarn
yarn add @sentry/capacitor @sentry/nuxt

# pnpm
pnpm add @sentry/capacitor @sentry/nuxt
```

**Other**

```bash
# npm
npm install @sentry/capacitor @sentry/browser --save

# yarn
yarn add @sentry/capacitor @sentry/browser

# pnpm
pnpm add @sentry/capacitor @sentry/browser
```

Notes on framework compatibility

#### [Angular](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#angular)

Currently, the Sentry Capacitor SDK only supports Angular 14 and newer. If you're using an older version of Angular, you also need to use an older version of the SDK. See this table for compatibility guidance:

| Angular version | Recommended Sentry SDK                            |
| --------------- | ------------------------------------------------- |
| 14 and newer    | `@sentry/capacitor` `@sentry/angular`             |
| 12 or 13        | `@sentry/capacitor^0` `@sentry/angular-ivy@^7` \* |
| 10 or 11        | `@sentry/capacitor^0` `@sentry/angular@^7` \*     |

\* These versions of the SDK are no longer maintained or tested. Version 0 might still receive bug fixes, but we don't guarantee support.

### [React and Vue](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#react-and-vue)

Both frameworks are fully compatible with the current and beta versions of Sentry Capacitor.

## [Configure](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** need no extra configuration, and you'll learn how to send them in step [#3](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#send-logs). This guide also enables **Tracing**, **Session Replay**, and **User Feedback**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#initialize-the-sentry-sdk)

Initialize Sentry as early as possible in your application's lifecycle.

The snippets also turn on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/javascript/guides/capacitor/configuration/options.md#tracesSampleRate)
* Session Replay: via `replayIntegration()`, sampled with [`replaysSessionSampleRate`](https://docs.sentry.io/platforms/javascript/guides/capacitor/configuration/options.md#replaysSessionSampleRate) and [`replaysOnErrorSampleRate`](https://docs.sentry.io/platforms/javascript/guides/capacitor/configuration/options.md#replaysOnErrorSampleRate)
* User Feedback: via [`feedbackIntegration()`](https://docs.sentry.io/platforms/javascript/guides/capacitor/user-feedback/configuration.md)

Don't need a feature? Remove its integration and options from the snippet.

If you're using Angular, React, Vue, or Nuxt, make sure to forward the `init` method from the framework's Sentry SDK, as you can see in these code snippets. If you're following the vanilla setup, you don't need to do this.

**\[Angular 14+] app.module.ts**

```typescript
import * as Sentry from "@sentry/capacitor";
import * as SentryAngular from "@sentry/angular";

Sentry.init(
  {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Set your release version, such as "getsentry@1.0.0"
    release: "my-project-name@<release-name>",
    // Set your dist version, such as "1"
    dist: "<dist>",
    integrations: [
      // Enables automatic instrumentation
      Sentry.browserTracingIntegration(),
      // enables Session Replay
      Sentry.replayIntegration(),
      // enables User Feedback
      Sentry.feedbackIntegration({
        // Additional integration configuration goes in here
        colorScheme: "system",
      }),
    ],

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,

    // Limit which URLs receive trace propagation
    tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],

    // Capture replays for 10% of all sessions,
    // plus for 100% of sessions with an error
    // Requires Sentry.replayIntegration()
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
  },
  // Forward the init method from @sentry/angular
  SentryAngular.init
);

@NgModule({
  providers: [
    {
      provide: ErrorHandler,
      // Attach the Sentry ErrorHandler
      useValue: SentryAngular.createErrorHandler(),
    },
    {
      provide: SentryAngular.TraceService,
      deps: [Router],
    },
    {
      provide: APP_INITIALIZER,
      useFactory: () => () => {},
      deps: [SentryAngular.TraceService],
      multi: true,
    },
  ],
})
```

**\[Angular 12, 13] app.module.ts**

```typescript
// Requires @sentry/capacitor V0.
import * as Sentry from "@sentry/capacitor";
import * as SentryAngular from "@sentry/angular-ivy";

Sentry.init(
  {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Set your release version, such as "getsentry@1.0.0"
    release: "my-project-name@<release-name>",
    // Set your dist version, such as "1"
    dist: "<dist>",
    integrations: [
      // Enables automatic instrumentation
      new Sentry.BrowserTracing(),
      // enables Session Replay
      new Sentry.Replay(),
      // enables User Feedback
      Sentry.feedbackIntegration({
        // Additional integration configuration goes in here
        colorScheme: "system",
      }),
    ],
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,

    // Limit which URLs receive trace propagation
    tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],

    // Capture replays for 10% of all sessions,
    // plus for 100% of sessions with an error
    // Requires Sentry.replayIntegration()
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
  },
  // Forward the init method from @sentry/angular
  SentryAngular.init
);

@NgModule({
  providers: [
    {
      provide: ErrorHandler,
      // Attach the Sentry ErrorHandler
      useValue: SentryAngular.createErrorHandler(),
    },
    {
      provide: SentryAngular.TraceService,
      deps: [Router],
    },
    {
      provide: APP_INITIALIZER,
      useFactory: () => () => {},
      deps: [SentryAngular.TraceService],
      multi: true,
    },
  ],
})
```

**\[React] index.tsx**

```typescript
import * as Sentry from "@sentry/capacitor";
import * as SentryReact from "@sentry/react";

Sentry.init(
  {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Set your release version, such as "getsentry@1.0.0"
    release: "my-project-name@<release-name>",
    // Set your dist version, such as "1"
    dist: "<dist>",
    integrations: [
      // Enables automatic instrumentation
      Sentry.browserTracingIntegration(),
      // enables Session Replay
      Sentry.replayIntegration(),
      // enables User Feedback
      Sentry.feedbackIntegration({
        // Additional integration configuration goes in here
        colorScheme: "system",
      }),
    ],

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,

    // Limit which URLs receive trace propagation
    tracePropagationTargets: [
      "localhost",
      /^https:\/\/yourserver\.io\/api/,
    ],

    // Capture replays for 10% of all sessions,
    // plus for 100% of sessions with an error
    // Requires Sentry.replayIntegration()
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
  },
  // Forward the init method from @sentry/react
  SentryReact.init,
);
```

**\[Vue] main.ts**

```typescript
import * as Sentry from "@sentry/capacitor";
import * as SentryVue from "@sentry/vue";
import { createApp } from "vue";

const app = createApp(App);

Sentry.init(
  {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    // Vue specific settings.
    siblingOptions: {
      vueOptions: {
        app: app,
        attachErrorHandler: false,
        attachProps: true,
      },
    },

    // Set your release version, such as "getsentry@1.0.0"
    release: "my-project-name@<release-name>",
    // Set your dist version, such as "1"
    dist: "<dist>",
    integrations: [
      // Enables automatic instrumentation
      Sentry.browserTracingIntegration(),
      // enables Session Replay
      Sentry.replayIntegration(),
      // enables User Feedback
      Sentry.feedbackIntegration({
        // Additional integration configuration goes in here
        colorScheme: "system",
      }),
    ],

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,

    // Limit which URLs receive trace propagation
    tracePropagationTargets: [
      "localhost",
      /^https:\/\/yourserver\.io\/api/,
    ],

    // Capture replays for 10% of all sessions,
    // plus for 100% of sessions with an error
    // Requires Sentry.replayIntegration()
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
  },

  // Forward the init method from @sentry/vue
  SentryVue.init,
);
```

**\[Nuxt] sentry.client.config.ts**

```typescript
import * as Sentry from "@sentry/capacitor";
import * as SentryNuxt from "@sentry/nuxt";

Sentry.init(
  {
    dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    // Set your release version, such as "getsentry@1.0.0"
    release: "my-project-name@<release-name>",
    // Set your dist version, such as "1"
    dist: "<dist>",
    integrations: [
      // Enables automatic instrumentation
      Sentry.browserTracingIntegration(),
      // enables Session Replay
      Sentry.replayIntegration(),
      // enables User Feedback
      Sentry.feedbackIntegration({
        // Additional integration configuration goes in here
        colorScheme: "system",
      }),
    ],

    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    tracesSampleRate: 1.0,

    // Limit which URLs receive trace propagation
    tracePropagationTargets: [
      "localhost",
      /^https:\/\/yourserver\.io\/api/,
    ],

    // Capture replays for 10% of all sessions,
    // plus for 100% of sessions with an error
    // Requires Sentry.replayIntegration()
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
  },

  // Forward the init method from @sentry/nuxt
  SentryNuxt.init,
);
```

**\[Other] main.(ts|js)**

```javascript
import * as Sentry from "@sentry/capacitor";
import { feedbackIntegration } from "@sentry/browser";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

  // Set your release version, such as "getsentry@1.0.0"
  release: "my-project-name@<release-name>",
  // Set your dist version, such as "1"
  dist: "<dist>",
  integrations: [
    // Enables automatic instrumentation
    Sentry.browserTracingIntegration(),
    // enables Session Replay
    Sentry.replayIntegration(),
    // enables User Feedback
    feedbackIntegration({
      // Additional integration configuration goes in here
      colorScheme: "system",
    }),
  ],

  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,

  // Limit which URLs receive trace propagation
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],

  // Capture replays for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Requires Sentry.replayIntegration()
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

### [Add Readable Stack Traces With Source Maps](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#add-readable-stack-traces-with-source-maps)

The stack traces in your Sentry errors probably won't look like your actual code without unminifying them. To fix this, upload your source maps to Sentry. The easiest way to do this is by using the Sentry Wizard.

Alternatively, take a look at our [Uploading Source Maps](https://docs.sentry.io/platforms/javascript/guides/capacitor/sourcemaps/uploading.md) documentation.

```bash
npx @sentry/wizard@latest -i sourcemaps
```

### [Provide Native Debug Information for iOS](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#provide-native-debug-information-for-ios)

You need to provide debug information to Sentry to make the stack-trace information for native crashes on iOS easier to understand. You can provide debug information by [uploading dSYM files](https://docs.sentry.io/platforms/javascript/guides/capacitor/dsym.md).

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/capacitor/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Send Logs](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#send-logs)

Use `Sentry.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. See [Set Up Logs](https://docs.sentry.io/platforms/javascript/guides/capacitor/logs.md) for all available logging methods and the syntax for formatting messages.

```javascript
Sentry.logger.info("User example action completed");

Sentry.logger.warn("Slow operation detected", {
  operation: "data_fetch",
  duration: 3500,
});

Sentry.logger.error("Validation failed", {
  form_field: "email",
  reason: "Invalid email",
});
```

If you already use `console`, capture those calls as Sentry Logs with [`consoleLoggingIntegration`](https://docs.sentry.io/platforms/javascript/guides/capacitor/logs.md#console-integration).

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add a test button to an existing page. Clicking it throws an error that Sentry captures:

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

```html
<button type="button" id="test-sentry-error">Test Sentry Error</button>

<script type="module">
  document
    .getElementById("test-sentry-error")
    .addEventListener("click", () => {
      throw new Error("Sentry Test Error");
    });
</script>
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/capacitor.md#next-steps)

At this point, you should have integrated Sentry into your Capacitor application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [use Sentry with Ionic](https://docs.sentry.io/platforms/javascript/guides/capacitor/ionic.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/capacitor/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/capacitor/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/capacitor/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/capacitor/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/capacitor/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/capacitor/tracing.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/capacitor/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/capacitor/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/capacitor/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/capacitor/configuration.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/capacitor/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/capacitor/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/capacitor/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/capacitor/best-practices.md)
- [Uploading Debug Symbols (iOS)](https://docs.sentry.io/platforms/javascript/guides/capacitor/dsym.md)
- [Ionic](https://docs.sentry.io/platforms/javascript/guides/capacitor/ionic.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/capacitor/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/capacitor/troubleshooting.md)

