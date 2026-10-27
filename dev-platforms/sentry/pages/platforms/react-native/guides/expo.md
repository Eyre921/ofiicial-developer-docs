---
title: "Expo"
source: https://docs.sentry.io/platforms/react-native/guides/expo.md
path: platforms/react-native/guides/expo
---

---
title: "Expo"
description: "Learn how to set up Sentry in an Expo project and capture your first events, including Expo config plugin, Expo Router tracing, Expo Updates context, and EAS dashboard integration."
url: https://docs.sentry.io/platforms/react-native/guides/expo/
---

# Sentry for Expo

Use this guide to set up Sentry's React Native SDK in an [Expo](https://expo.dev/) project. The same `@sentry/react-native` SDK powers bare React Native and Expo apps. This guide covers Expo-specific setup, including the config plugin, Metro, and EAS.

If you don't already have an account and Sentry project, head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/react-native/guides/expo.md#install)

You need Expo SDK 50 or newer. The `@sentry/react-native` SDK requires Expo SDK 50+. On [Expo SDK 49](https://docs.expo.dev/guides/using-sentry/) or older, the deprecated `sentry-expo` package was used; [migrate to `@sentry/react-native`](https://docs.sentry.io/platforms/react-native/guides/expo/migration/sentry-expo.md) to keep receiving updates.

Use the Sentry Wizard to patch your project automatically:

```bash
npx @sentry/wizard@latest -i reactNative
```

The following tasks will be performed by the Sentry Wizard

* Install the `@sentry/react-native` package.
* Add `@sentry/react-native/metro` to the **metro.config.js** Metro configuration.
* Add `@sentry/react-native/expo` to the **app.json** Expo configuration.
* Enable the Sentry React Native Gradle build step for Android to auto-upload generated source maps and debug symbols.
* Wrap the *Bundle React Native code and images* Xcode project build phase script to upload generated source maps and collect bundled node modules.
* Add the *Upload Debug Symbols to Sentry* Xcode project build phase.
* Run `pod install`.
* Store build credentials in **ios/sentry.properties**, **android/sentry.properties**, and **.env.local**.
* Configure Sentry with the supplied DSN in your **layout.tsx** file.

You only need to patch the project once. Add the patched files to version control. If you prefer, use the [manual install](https://docs.sentry.io/platforms/react-native/guides/expo.md#manual-install) below.

### [Manual Install](https://docs.sentry.io/platforms/react-native/guides/expo.md#manual-install)

If you don't use the Wizard, install `@sentry/react-native`:

```bash
npx expo install @sentry/react-native
```

*Other available variations of the above snippet: npm, yarn, pnpm*

## [Configure](https://docs.sentry.io/platforms/react-native/guides/expo.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** need `enableLogs: true` in the initialization snippet below, and you'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/react-native/guides/expo.md#send-logs). **Application Metrics** need no extra configuration, and you'll learn how to send them in [Send Application Metrics](https://docs.sentry.io/platforms/react-native/guides/expo.md#send-application-metrics-).

This guide also enables **Tracing**, **Profiling**, **Session Replay**, and **User Feedback**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

### [Initialize the SDK](https://docs.sentry.io/platforms/react-native/guides/expo.md#initialize-the-sdk)

Import `@sentry/react-native` and initialize the SDK in your Expo Router root layout or app entry point.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/react-native/guides/expo/configuration/options.md#tracesSampleRate)
* Profiling: via `profilesSampleRate` (see [Profiling](https://docs.sentry.io/platforms/react-native/guides/expo/profiling.md))
* Session Replay: via `mobileReplayIntegration()` and the replay sample rates (see [Session Replay](https://docs.sentry.io/platforms/react-native/guides/expo/session-replay.md))
* User Feedback: via `feedbackIntegration()` (see [User Feedback](https://docs.sentry.io/platforms/react-native/guides/expo/user-feedback.md))
* Logs: via [`enableLogs`](https://docs.sentry.io/platforms/react-native/guides/expo/configuration/options.md#enableLogs)

Don't need a feature? Remove its integration and options from the snippet.

```javascript
import * as Sentry from "@sentry/react-native";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // Adds context data to events, such as IP address, cookies, and user.
  sendDefaultPii: true,

  integrations: [
    // Enables Session Replay
    Sentry.mobileReplayIntegration(),
    // Enables User Feedback. Open the form with Sentry.showFeedbackWidget().
    Sentry.feedbackIntegration(),
  ],

  // Enables Tracing.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  tracesSampleRate: 1.0,

  // Enables Profiling for 100% of sampled transactions.
  profilesSampleRate: 1.0,

  // Enables Logs to be sent to Sentry.
  enableLogs: true,

  // Capture replays for 10% of sessions and 100% of sessions with an error.
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

### [Wrap Your App](https://docs.sentry.io/platforms/react-native/guides/expo.md#wrap-your-app)

Wrap the root component of your application with `Sentry.wrap`:

```javascript
import { Stack } from "expo-router";
import * as Sentry from "@sentry/react-native";

function RootLayout() {
  return <Stack />;
}

export default Sentry.wrap(RootLayout);
```

### [Add the Sentry Expo Plugin](https://docs.sentry.io/platforms/react-native/guides/expo.md#add-the-sentry-expo-plugin)

To upload bundles and source maps automatically during native builds, add the Sentry plugin to your Expo app configuration. Add it to the `plugins` array in `app.json`, or wrap your config with `withSentry` in `app.config.js` or `app.config.ts`:

**app.json/app.config.json**

```javascript
{
  "expo": {
    "plugins": [
      [
        "@sentry/react-native/expo",
        {
          "url": "https://sentry.io/",
          "note": "Use SENTRY_AUTH_TOKEN env to authenticate with Sentry.",
          "project": "<your-project-slug>",
          "organization": "<your-org-slug>"
        }
      ]
    ]
  }
}
```

**app.config.js**

```javascript
const { withSentry } = require("@sentry/react-native/expo");

const config = {
  name: "Expo Example",
  slug: "expo-example",
};

module.exports = withSentry(config, {
  url: "https://sentry.io/",
  // Use SENTRY_AUTH_TOKEN env to authenticate with Sentry.
  project: "<your-project-slug>",
  organization: "<your-org-slug>",
});
```

**app.config.ts**

```typescript
import { ExpoConfig } from "expo/config";
import { withSentry } from "@sentry/react-native/expo";

const config: ExpoConfig = {
  name: "Expo Example",
  slug: "expo-example",
};

export default withSentry(config, {
  url: "https://sentry.io/",
  // Use SENTRY_AUTH_TOKEN env to authenticate with Sentry.
  project: "<your-project-slug>",
  organization: "<your-org-slug>",
});
```

`npx expo install` adds the bare `@sentry/react-native` to the plugins array. Both `@sentry/react-native` and `@sentry/react-native/expo` are valid plugin paths. Expo resolves them the same way.

Add your auth token to a `.env.local` file in the root of your project:

```properties
# DO NOT COMMIT YOUR AUTH TOKEN
SENTRY_AUTH_TOKEN=<your-sentry-auth-token>
```

Do not commit your auth token. Add `.env.local` to your `.gitignore`. For EAS builds, add `SENTRY_AUTH_TOKEN` as an [EAS secret](https://docs.expo.dev/eas/environment-variables/) instead of using a `.env.local` file.

### [Add the Sentry Metro Plugin](https://docs.sentry.io/platforms/react-native/guides/expo.md#add-the-sentry-metro-plugin)

Add Sentry Serializer to the Metro configuration to assign unique Debug IDs to generated bundles and source maps:

```javascript
// const { getDefaultConfig } = require("expo/metro-config");
const { getSentryExpoConfig } = require("@sentry/react-native/metro");

// const config = getDefaultConfig(__dirname);
const config = getSentryExpoConfig(__dirname);

module.exports = config;
```

### [Add the Apple Privacy Manifest](https://docs.sentry.io/platforms/react-native/guides/expo.md#add-the-apple-privacy-manifest)

The SDK needs access to some device and application information for essential functionality. Add the privacy manifest to your Xcode project to meet Apple's guidelines. See the [Apple Privacy Manifest guide](https://docs.sentry.io/platforms/react-native/guides/expo/data-management/apple-privacy-manifest.md) for the records required by the Sentry SDKs.

### [Integrate Sentry With Your EAS Dashboard](https://docs.sentry.io/platforms/react-native/guides/expo.md#integrate-sentry-with-your-eas-dashboard)

Connect Sentry to [Expo Application Services (EAS)](https://expo.dev/eas) to view crash reports and [Session Replays](https://docs.sentry.io/platforms/react-native/guides/expo/session-replay.md) for deployments in the EAS dashboard, with direct links to Sentry stack traces and debugging context.

If you change your organization slug, update the configuration for this integration. See the [troubleshooting guide](https://docs.sentry.io/integrations/troubleshooting.md).

#### [Install the Integration](https://docs.sentry.io/platforms/react-native/guides/expo.md#install-the-integration)

You need Sentry owner, manager, or admin permissions to install this integration.

1. Log in to your Expo dashboard and open **Account Settings > Overview** (`https://expo.dev/accounts/[your-account]/settings`).
2. Find **Connections** and click **Connect** next to Sentry.
3. Log in to Sentry and accept the integration into your organization. Expo will redirect you to Account Settings > Overview.

#### [Link Your Projects](https://docs.sentry.io/platforms/react-native/guides/expo.md#link-your-projects)

After connecting your accounts, link your Expo project to your Sentry project:

1. Open **Projects > \[Your Project] > Configuration > Project settings** in the Expo dashboard.
2. Click **Link** and select your Sentry project.

#### [View Sentry Data in EAS](https://docs.sentry.io/platforms/react-native/guides/expo.md#view-sentry-data-in-eas)

To see Sentry issues and replays in the Expo dashboard, create an [EAS Update channel](https://docs.expo.dev/eas-update/how-it-works/) and assign builds to it to create an [EAS deployment](https://docs.expo.dev/eas-update/deployment/). Then open **Projects > \[Your Project] > Updates > Deployments > \[Deployment]**.

### [Expo-Specific Features](https://docs.sentry.io/platforms/react-native/guides/expo.md#expo-specific-features)

* [Expo Updates](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup/expo/expo-updates.md) — Automatic OTA update context, searchable tags, performance spans for update checks and downloads, and emergency launch alerts
* [EAS Build Hooks](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup/expo/eas-build-hooks.md) — Capture build failures and lifecycle events from EAS Build
* [Sentry Android Gradle Plugin](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup/expo/gradle.md) — Advanced Android build configuration
* [Expo Router tracing](https://docs.sentry.io/platforms/react-native/guides/expo/tracing/instrumentation/expo-router.md) — Navigation transitions, performance spans, prefetch instrumentation, and per-route `ErrorBoundary` capture
* [Expo Image and Asset tracing](https://docs.sentry.io/platforms/react-native/guides/expo/tracing/instrumentation/expo-resources.md) — Automatic spans for `expo-image` and `expo-asset`
* [Upload source maps for native builds and Expo Updates](https://docs.sentry.io/platforms/react-native/guides/expo/sourcemaps/uploading/expo.md)

### [Build Notes](https://docs.sentry.io/platforms/react-native/guides/expo.md#build-notes)

* Don't commit your auth token. Store it in `.env.local` as `SENTRY_AUTH_TOKEN` for local builds, and as an [EAS secret](https://docs.expo.dev/eas/environment-variables/) for EAS builds.
* Source maps for the `Release` version of your application are uploaded automatically during the native application build.
* During development, the source code is resolved using the Metro Server and source maps aren't used. This currently doesn't work on web.

## [Send Logs](https://docs.sentry.io/platforms/react-native/guides/expo.md#send-logs)

Use `Sentry.logger` to send logs at different levels. You can include attributes to search or filter by later.

The SDK can capture `console.*` calls when Logs are enabled. See the [Console logging integration](https://docs.sentry.io/platforms/react-native/integrations/console-logging.md) for details.

```javascript
Sentry.logger.info("Order processed", { order_id: "order-123" });
Sentry.logger.warn("Slow operation detected", {
  operation: "data_fetch",
  duration_ms: 3500,
});
```

See [Set Up Logs](https://docs.sentry.io/platforms/react-native/guides/expo/logs.md) for all available logging methods and message formatting options.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/react-native/guides/expo.md#send-application-metrics-)

Application Metrics are supported in React Native SDK 7.8.0 and newer. No extra option is needed after SDK initialization. Use `Sentry.metrics` to send counters, gauges, and distributions:

```javascript
Sentry.metrics.count("checkout.failed", 1);
Sentry.metrics.gauge("active_connections", 42);
Sentry.metrics.distribution("api_latency", 187, { unit: "millisecond" });
```

See [Set Up Metrics](https://docs.sentry.io/platforms/react-native/guides/expo/metrics.md) for all available metric types and configuration options.

## [Verify Your Setup](https://docs.sentry.io/platforms/react-native/guides/expo.md#verify-your-setup)

Build the `Release` version of your application, then capture a test error:

```javascript
Sentry.captureException(new Error("First error"));
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/react-native/guides/expo.md#view-captured-data-in-sentry)

Open your project on [Sentry.io](https://sentry.io) to view the captured error.

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/react-native/guides/expo.md#next-steps)

At this point, you should have integrated Sentry into your Expo application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Configure Expo Router tracing](https://docs.sentry.io/platforms/react-native/guides/expo/tracing/instrumentation/expo-router.md)
* [Capture Expo Updates context](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup/expo/expo-updates.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/react-native/guides/expo/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/react-native/guides/expo/enriching-events.md)
- [Features](https://docs.sentry.io/platforms/react-native/guides/expo/features.md)
- [Extended Configuration](https://docs.sentry.io/platforms/react-native/guides/expo/configuration.md)
- [Manual Setup](https://docs.sentry.io/platforms/react-native/guides/expo/manual-setup.md)
- [Tracing](https://docs.sentry.io/platforms/react-native/guides/expo/tracing.md)
- [Integrations](https://docs.sentry.io/platforms/react-native/guides/expo/integrations.md)
- [Profiling](https://docs.sentry.io/platforms/react-native/guides/expo/profiling.md)
- [Data Management](https://docs.sentry.io/platforms/react-native/guides/expo/data-management.md)
- [Logs](https://docs.sentry.io/platforms/react-native/guides/expo/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/react-native/guides/expo/session-replay.md)
- [Source Maps](https://docs.sentry.io/platforms/react-native/guides/expo/sourcemaps.md)
- [Application Metrics](https://docs.sentry.io/platforms/react-native/guides/expo/metrics.md)
- [Debug Symbols](https://docs.sentry.io/platforms/react-native/guides/expo/upload-debug.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/react-native/guides/expo/releases.md)
- [SDK Overhead](https://docs.sentry.io/platforms/react-native/guides/expo/overhead.md)
- [Build Distribution](https://docs.sentry.io/platforms/react-native/guides/expo/build-distribution.md)
- [User Feedback](https://docs.sentry.io/platforms/react-native/guides/expo/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/react-native/guides/expo/feature-flags.md)
- [Migration Guide](https://docs.sentry.io/platforms/react-native/guides/expo/migration.md)
- [Size Analysis](https://docs.sentry.io/platforms/react-native/guides/expo/size-analysis.md)
- [Troubleshooting](https://docs.sentry.io/platforms/react-native/guides/expo/troubleshooting.md)

