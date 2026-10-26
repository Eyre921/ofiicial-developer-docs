---
title: "Angular"
source: https://docs.sentry.io/platforms/javascript/guides/angular.md
path: platforms/javascript/guides/angular
---

---
title: "Angular"
description: "Learn how to set up Sentry in your Angular application and capture your first errors."
url: https://docs.sentry.io/platforms/javascript/guides/angular/
---

# Sentry for Angular

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/angular.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Angular version `17.0.0` or above

Are you using Angular 16 or older?

If you're using Angular 16 or older, install and [Set Up the SDK Manually](https://docs.sentry.io/platforms/javascript/guides/angular/manual-setup.md). The Sentry Angular SDK still works for Angular versions 14 and newer but the installation wizards requires at least Angular 17.

## [Install](https://docs.sentry.io/platforms/javascript/guides/angular.md#install)

Run the Sentry wizard to automatically configure Sentry in your Angular application. It will then guide you through the setup process, asking you to enable additional (optional) Sentry features for your application beyond error monitoring.

```bash
npx @sentry/wizard@latest -i angular
```

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay/web.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what was happening in the user's browser before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

This guide assumes that you enable all features and allow the wizard to add an example component to your application. You can add or remove features at any time, but setting them up now will save you the effort of configuring them manually later.

Prefer to set things up yourself? Check out the [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/angular/manual-setup.md) guide.

What does the installation wizard change inside your application?

* Adds a `Sentry.init()` call into your `main.ts` file
* Registers the Sentry `ErrorHandler` and `TraceService` in your `app.config.ts` file
* Creates `.sentryclirc` with an auth token to upload source maps (this file is automatically added to `.gitignore`)
* Walks you through enabling source maps upload when making a production build, locally as well as in CI
* Adds an example component to your application to help verify your Sentry setup

## [Avoid Ad Blockers With Tunneling (Optional)](https://docs.sentry.io/platforms/javascript/guides/angular.md#avoid-ad-blockers-with-tunneling-optional)

You can prevent ad blockers from blocking Sentry events using tunneling. Use the `tunnel` option in `Sentry.init` to add an API endpoint in your application that forwards Sentry events to Sentry servers.

This will send all events to the `tunnel` endpoint. However, the events need to be parsed and redirected to Sentry, so you'll need to do additional configuration on the server. You can find a detailed explanation on how to do this on our [Troubleshooting page](https://docs.sentry.io/platforms/javascript/guides/angular/troubleshooting.md#using-the-tunnel-option).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  tunnel: "/tunnel",
});
```

## [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/angular.md#control-the-data-you-send-to-sentry-optional)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data like HTTP bodies and URL query parameters. This will give you rich debugging context.

The SDK always filters sensitive values whose keys match a built-in denylist, such as `auth` or `password`, and sends `[Filtered]` instead.

To send less data, turn off the categories you don't need in the `dataCollection` option. For the full list of categories and their defaults, [see the `dataCollection` options](https://docs.sentry.io/platforms/javascript/guides/angular/configuration/options.md#dataCollection).

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  dataCollection: {
    userInfo: false,
    // other categories
  },
});
```

## [Verify](https://docs.sentry.io/platforms/javascript/guides/angular.md#verify)

If you haven't tested your Sentry configuration yet, let's do it now. You can confirm that the Sentry SDK is sending data to your Sentry project by using the example component created by the installation wizard:

1. Open the page you added the example component to in your browser.
2. Click the "Throw error" button. This triggers an error.

Sentry captures this error for you. Additionally, the button click starts a trace to measure the time it takes for the error to be thrown.

##### Tip

Don't forget to explore the example component's code in your project to understand what's happening after your button click.

### [Verify Additional Features](https://docs.sentry.io/platforms/javascript/guides/angular.md#verify-additional-features)

**Logs** (enabled by default)

See structured log entries from your application. You can send logs from anywhere:

```typescript
Sentry.logger.info("User action", { userId: "123" });
Sentry.logger.warn("Slow response", { duration: 5000 });
Sentry.logger.error("Operation failed", { reason: "timeout" });
```

Learn more about [Logs configuration](https://docs.sentry.io/platforms/javascript/guides/angular/logs.md).

**Application Metrics** (enabled by default) NEW

Track and analyze custom application metrics to understand trends and patterns in your app's performance and behavior over time:

```typescript
Sentry.metrics.count("checkout.failed", 1);
Sentry.metrics.gauge("queue.depth", 42);
Sentry.metrics.distribution("api_latency", 187, {
  unit: "millisecond",
});
```

Learn more about [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/angular/metrics.md).

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/angular.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

##### Important

Errors triggered from within your browser's developer tools (like the browser console) are sandboxed, so they will not trigger Sentry's error monitoring.

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/angular.md#next-steps)

At this point, you should have integrated Sentry into Angular application and should already be sending error and tracing data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Extend Sentry to your backend using one of our [SDKs](https://docs.sentry.io/.md)
* Continue to [customize your configuration](https://docs.sentry.io/platforms/javascript/guides/angular/configuration.md)
* Make use of [Angular-specific features](https://docs.sentry.io/platforms/javascript/guides/angular/features.md)
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/javascript/guides/angular/usage.md)

Are you having problems setting up the SDK?

* If you encountered issues with our installation wizard, try [setting up Sentry manually](https://docs.sentry.io/platforms/javascript/guides/angular/manual-setup.md)
* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/angular/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
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

- [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/angular/manual-setup.md)
- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/angular/usage.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/angular/sourcemaps.md)
- [Logs](https://docs.sentry.io/platforms/javascript/guides/angular/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/javascript/guides/angular/session-replay.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/angular/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/javascript/guides/angular/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/javascript/guides/angular/profiling.md)
- [User Feedback](https://docs.sentry.io/platforms/javascript/guides/angular/user-feedback.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/angular/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/angular/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/angular/configuration.md)
- [Feature Flags](https://docs.sentry.io/platforms/javascript/guides/angular/feature-flags.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/angular/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/javascript/guides/angular/security-policy-reporting.md)
- [Special Use Cases](https://docs.sentry.io/platforms/javascript/guides/angular/best-practices.md)
- [Migration Guide](https://docs.sentry.io/platforms/javascript/guides/angular/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/angular/troubleshooting.md)
- [Angular Features](https://docs.sentry.io/platforms/javascript/guides/angular/features.md)
- [AngularJS 1.x](https://docs.sentry.io/platforms/javascript/guides/angular/angular1.md)

