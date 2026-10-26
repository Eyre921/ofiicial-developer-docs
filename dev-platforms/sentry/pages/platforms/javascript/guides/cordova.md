---
title: "Cordova"
source: https://docs.sentry.io/platforms/javascript/guides/cordova.md
path: platforms/javascript/guides/cordova
---

---
title: "Cordova"
description: "Learn how to manually set up Sentry in your Cordova app and capture your first errors."
url: https://docs.sentry.io/platforms/javascript/guides/cordova/
---

# Sentry for Cordova

##### Deprecation Notice

Cordova is being superseded by modern alternatives like [Capacitor](https://ionic.io/resources/articles/capacitor-vs-cordova-modern-hybrid-app-development). This SDK is no longer maintained by Sentry. If you are starting a new project or planning a [migration](https://capacitorjs.com/docs/cordova/migration-strategy), consider using [Sentry Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md), [Sentry React Native](https://docs.sentry.io/platforms/react-native.md), or [Sentry Flutter](https://docs.sentry.io/platforms/dart/guides/flutter.md) instead.

The Cordova SDK uses a native extension for iOS and Android, but will fall back to a pure JavaScript version (`@sentry/browser`) if needed.

Features

* Automatic Native crash [error tracking](https://docs.sentry.io/product/issues.md) using both [iOS](https://docs.sentry.io/platforms/apple/guides/ios.md) and [Android](https://docs.sentry.io/platforms/android.md) supports
  * [Release health](https://docs.sentry.io/product/releases/health.md) to track crash-free users and sessions

* Offline storage of events

  * Android: Offline caching when a device is offline; we send a report once the application is restarted
  * iOS: Offline caching when a device is unable to connect; we send a report once we receive another event

* Events [enriched](https://docs.sentry.io/platforms/javascript/guides/cordova/enriching-events/context.md) with device data

* [Breadcrumbs](https://docs.sentry.io/platforms/javascript/guides/cordova/enriching-events/breadcrumbs.md) created for location changes, outgoing HTTP requests with XHR and Fetch, console logs, and HTML touch events

* On-device symbolication for JavaScript (in `Debug` mode)

* [Ionic support](https://docs.sentry.io/platforms/javascript/guides/cordova/ionic.md)

* Under the hood, the SDK relies on our [JavaScript SDK](https://docs.sentry.io/platforms/javascript.md), which makes all functions available for JavaScript also available in this SDK ,including:
  * [Tracing](https://docs.sentry.io/platforms/javascript/guides/cordova/performance/instrumentation/custom-instrumentation.md) to create transactions

## [Prerequisites](https://docs.sentry.io/platforms/javascript/guides/cordova.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

## [Install](https://docs.sentry.io/platforms/javascript/guides/cordova.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/cordova.md#install-the-sentry-sdk)

Run this `cordova` command to add the Sentry SDK to your application:

This command starts the Sentry Wizard, which will patch your project (you need to do this only once). The wizard helps configure your project by:

* Linking your Sentry account and project
* Adding a build step to Xcode to upload debug symbols for iOS crashes
* Configuring [source map uploads](https://docs.sentry.io/platforms/javascript/guides/cordova/sourcemaps.md) so you can see your original JavaScript code in Sentry instead of minified production code

```bash
cordova plugin add sentry-cordova
```

## [Configure](https://docs.sentry.io/platforms/javascript/guides/cordova.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/javascript/guides/cordova.md#initialize-the-sentry-sdk)

Initialize Sentry as early as possible in your application. For this, `init` the SDK in the `deviceready` event:

```javascript
onDeviceReady: function() {
  var Sentry = cordova.require("sentry-cordova.Sentry");
  Sentry.init({
    dsn: 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>',
  });
}
```

### [Allow the Sentry Domain](https://docs.sentry.io/platforms/javascript/guides/cordova.md#allow-the-sentry-domain)

Make sure your app can talk to Sentry by adding this to your `config.xml`:

```xml
<access origin="https://*.sentry.io" />
```

### [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/javascript/guides/cordova.md#control-the-data-you-send-to-sentry-optional)

See [Data Collected](https://docs.sentry.io/platforms/javascript/guides/cordova/data-management/data-collected.md) for the data the SDK sends by default, and [Scrubbing Sensitive Data](https://docs.sentry.io/platforms/javascript/guides/cordova/data-management/sensitive-data.md) to learn how to remove data before it's sent.

## [Verify Your Setup](https://docs.sentry.io/platforms/javascript/guides/cordova.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

This snippet includes an intentional error, so you can test that everything is working as soon as you set it up.

```javascript
throw new Error("My first Sentry error!");
```

Or, try a native crash:

```javascript
Sentry.nativeCrash();
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/javascript/guides/cordova.md#view-captured-data-in-sentry)

To view and resolve the recorded error, log in to [sentry.io](https://sentry.io) and select your project. Clicking the error's title opens a page where you can view detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/javascript/guides/cordova.md#next-steps)

At this point, you should have integrated Sentry into your Cordova application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Continue to [customize your configuration](https://docs.sentry.io/platforms/javascript/guides/cordova/configuration.md)
* Learn how to [upload debug symbols](https://docs.sentry.io/platforms/javascript/guides/cordova/upload-debug.md) to make sure your native stack traces are readable
* Check our [Ionic support guide](https://docs.sentry.io/platforms/javascript/guides/cordova/ionic.md)
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/javascript/guides/cordova/usage.md)

Are you having problems setting up the SDK?

* If you are experiencing errors and want to remove unused architectures from your binary when submitting the build to iTunes Connect, you can use the scripts provided in [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/cordova/troubleshooting.md).
* [Get support](https://www.sentry.help/en/)

## Other JavaScript Frameworks

- [Angular](https://docs.sentry.io/platforms/javascript/guides/angular.md)
- [Astro](https://docs.sentry.io/platforms/javascript/guides/astro.md)
- [AWS Lambda](https://docs.sentry.io/platforms/javascript/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/javascript/guides/azure-functions.md)
- [Bun](https://docs.sentry.io/platforms/javascript/guides/bun.md)
- [Capacitor](https://docs.sentry.io/platforms/javascript/guides/capacitor.md)
- [Cloud Functions for Firebase](https://docs.sentry.io/platforms/javascript/guides/firebase.md)
- [Cloudflare](https://docs.sentry.io/platforms/javascript/guides/cloudflare.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/javascript/guides/cordova/usage.md)
- [Debug Information](https://docs.sentry.io/platforms/javascript/guides/cordova/upload-debug.md)
- [Source Maps](https://docs.sentry.io/platforms/javascript/guides/cordova/sourcemaps.md)
- [Tracing](https://docs.sentry.io/platforms/javascript/guides/cordova/tracing.md)
- [Sampling](https://docs.sentry.io/platforms/javascript/guides/cordova/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/javascript/guides/cordova/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/javascript/guides/cordova/configuration.md)
- [Data Management](https://docs.sentry.io/platforms/javascript/guides/cordova/data-management.md)
- [Ionic](https://docs.sentry.io/platforms/javascript/guides/cordova/ionic.md)
- [Troubleshooting](https://docs.sentry.io/platforms/javascript/guides/cordova/troubleshooting.md)

