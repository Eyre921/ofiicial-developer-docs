---
title: "React Native"
source: https://docs.sentry.io/platforms/react-native.md
path: platforms/react-native
---

---
title: "React Native"
description: "Learn how to set up Sentry's React Native SDK and capture your first events."
url: https://docs.sentry.io/platforms/react-native/
---

# Sentry for React Native

Read on to find out how to set up Sentry's React Native SDK, which automatically reports errors and exceptions in your application. If you prefer video instructions, see [How to Install the Sentry React Native SDK in 60 Seconds](https://vimeo.com/899369012).

If you don't already have an account and Sentry project, head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/react-native.md#install)

Sentry captures data by using an SDK within your application's runtime. These platform-specific SDKs give Sentry a deeper understanding of how your application works.

Run `@sentry/wizard` to install and configure the SDK:

```bash
npx @sentry/wizard@latest -i reactNative
```

[Sentry Wizard](https://github.com/getsentry/sentry-wizard) patches your project. You only need to do this once; then add the patched files to version control. If you prefer, follow the [manual setup guide](https://docs.sentry.io/platforms/react-native/manual-setup/manual-setup.md).

The following tasks will be performed by the Sentry Wizard

* Install the `@sentry/react-native` package.
* Add `@sentry/react-native/metro` to the **metro.config.js** Metro configuration.
* Add `@sentry/react-native/expo` to the **app.json** Expo configuration.
* Enable the Sentry React Native Gradle build step for Android to auto-upload generated source maps and debug symbols.
* Wrap the *Bundle React Native code and images* Xcode project build phase script to upload generated source maps and collect bundled node modules.
* Add the *Upload Debug Symbols to Sentry* Xcode project build phase.
* Run `pod install`.
* Store build credentials in **ios/sentry.properties**, **android/sentry.properties**, and **.env.local**.
* Configure Sentry with the supplied DSN in your **layout.tsx** or **App.tsx** file.

If you're using Expo, follow the [Expo guide](https://docs.sentry.io/platforms/react-native/guides/expo.md) for Expo-specific setup. The SDK works with both managed and bare projects.

## [Configure](https://docs.sentry.io/platforms/react-native.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init()`. **Logs** need `enableLogs: true` in the initialization snippet below, and you'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/react-native.md#send-logs). **Application Metrics** need no extra configuration, and you'll learn how to send them in [Send Application Metrics](https://docs.sentry.io/platforms/react-native.md#send-application-metrics-).

This guide also enables **Tracing**, **Profiling**, **Session Replay**, and **User Feedback**. **Size Analysis** uses a separate build-time setup; see [Size Analysis](https://docs.sentry.io/platforms/react-native/size-analysis.md).

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.
* [**User Feedback**](https://docs.sentry.io/product/user-feedback.md): Collect feedback directly from users when they encounter errors, allowing them to describe what happened and provide context that helps you understand and resolve issues faster.

To capture errors, initialize the Sentry React Native SDK as early as possible in your application's lifecycle.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/react-native/configuration/options.md#tracesSampleRate)
* Profiling: via `profilesSampleRate` (see [Profiling](https://docs.sentry.io/platforms/react-native/profiling.md))
* Session Replay: via `mobileReplayIntegration()` and the replay sample rates (see [Session Replay](https://docs.sentry.io/platforms/react-native/session-replay.md))
* User Feedback: via `feedbackIntegration()` (see [User Feedback](https://docs.sentry.io/platforms/react-native/user-feedback.md))
* Logs: via [`enableLogs`](https://docs.sentry.io/platforms/react-native/configuration/options.md#enableLogs)

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

### [Wrap Your App](https://docs.sentry.io/platforms/react-native.md#wrap-your-app)

To automatically instrument your app with [touch event tracking](https://docs.sentry.io/platforms/react-native/configuration/touchevents.md) and [automatic tracing](https://docs.sentry.io/platforms/react-native/tracing/instrumentation/automatic-instrumentation.md), wrap its root component with `Sentry.wrap`:

```javascript
export default Sentry.wrap(App);
```

You don't need this if your app doesn't have a single parent `App` component.

## [Send Logs](https://docs.sentry.io/platforms/react-native.md#send-logs)

Use `Sentry.logger` to send logs at different levels. You can include attributes to search or filter by later.

The SDK can capture `console.*` calls when Logs are enabled. See the [Console logging integration](https://docs.sentry.io/platforms/react-native/integrations/console-logging.md) for details.

```javascript
Sentry.logger.info("Order processed", { order_id: "order-123" });
Sentry.logger.warn("Slow operation detected", {
  operation: "data_fetch",
  duration_ms: 3500,
});
```

See [Set Up Logs](https://docs.sentry.io/platforms/react-native/logs.md) for all available logging methods and message formatting options.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/react-native.md#send-application-metrics-)

Application Metrics are supported in React Native SDK 7.8.0 and newer. No extra option is needed after SDK initialization. Use `Sentry.metrics` to send counters, gauges, and distributions:

```javascript
Sentry.metrics.count("checkout.failed", 1);
Sentry.metrics.gauge("active_connections", 42);
Sentry.metrics.distribution("api_latency", 187, { unit: "millisecond" });
```

See [Set Up Metrics](https://docs.sentry.io/platforms/react-native/metrics.md) for all available metric types and configuration options.

## [Verify Your Setup](https://docs.sentry.io/platforms/react-native.md#verify-your-setup)

Trigger a test error to confirm that Sentry is receiving events. You should see the error in Sentry within a few minutes.

**Throw Error**

```javascript
throw new Error("My first Sentry error!");
```

**Native Crash**

```javascript
Sentry.nativeCrash();
```

Alternatively, use the [Sentry Playground](https://docs.sentry.io/platforms/react-native/manual-setup/playground.md) to test your setup interactively with multiple error scenarios.

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/react-native.md#view-captured-data-in-sentry)

Head over to your project on [Sentry.io](https://sentry.io) to view the captured error.

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).
* Open the [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) page and click on individual feedback to see more details all in one view. For more information, click [here](https://docs.sentry.io/product/user-feedback.md).

## [Next Steps](https://docs.sentry.io/platforms/react-native.md#next-steps)

At this point, you should have integrated Sentry into your React Native application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Explore React Native features](https://docs.sentry.io/platforms/react-native/features.md)
* [Add readable stack traces to errors](https://docs.sentry.io/platforms/react-native/sourcemaps.md)
* [Add the Apple Privacy Manifest](https://docs.sentry.io/platforms/react-native/data-management/apple-privacy-manifest.md)
* [Troubleshoot your setup](https://docs.sentry.io/platforms/react-native/troubleshooting.md)

## Frameworks

- [Expo](https://docs.sentry.io/platforms/react-native/guides/expo.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/react-native/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/react-native/enriching-events.md)
- [Features](https://docs.sentry.io/platforms/react-native/features.md)
- [Extended Configuration](https://docs.sentry.io/platforms/react-native/configuration.md)
- [Manual Setup](https://docs.sentry.io/platforms/react-native/manual-setup.md)
- [Tracing](https://docs.sentry.io/platforms/react-native/tracing.md)
- [Integrations](https://docs.sentry.io/platforms/react-native/integrations.md)
- [Profiling](https://docs.sentry.io/platforms/react-native/profiling.md)
- [Data Management](https://docs.sentry.io/platforms/react-native/data-management.md)
- [Logs](https://docs.sentry.io/platforms/react-native/logs.md)
- [Session Replay](https://docs.sentry.io/platforms/react-native/session-replay.md)
- [Source Maps](https://docs.sentry.io/platforms/react-native/sourcemaps.md)
- [Application Metrics](https://docs.sentry.io/platforms/react-native/metrics.md)
- [Debug Symbols](https://docs.sentry.io/platforms/react-native/upload-debug.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/react-native/releases.md)
- [SDK Overhead](https://docs.sentry.io/platforms/react-native/overhead.md)
- [Build Distribution](https://docs.sentry.io/platforms/react-native/build-distribution.md)
- [User Feedback](https://docs.sentry.io/platforms/react-native/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/react-native/feature-flags.md)
- [Migration Guide](https://docs.sentry.io/platforms/react-native/migration.md)
- [Size Analysis](https://docs.sentry.io/platforms/react-native/size-analysis.md)
- [Troubleshooting](https://docs.sentry.io/platforms/react-native/troubleshooting.md)

