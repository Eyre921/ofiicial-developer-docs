---
title: "React Native"
source: https://docs.sentry.io/platforms/react-native.md
path: platforms/react-native
---

---
title: "React Native"
description: "Learn how to set up Sentry's React Native SDK."
url: https://docs.sentry.io/platforms/react-native/
---

# React Native | Sentry for React Native

Read on to find out how to set up Sentry's React Native SDK which will automatically report errors and exceptions in your application. If you prefer to follow video instructions, see [How to Install the Sentry React Native SDK in 60 Seconds](https://vimeo.com/899369012).

If you don't already have an account and Sentry project established, head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Features](https://docs.sentry.io/platforms/react-native.md#features)

In addition to [error monitoring](https://docs.sentry.io/product/issues.md), here are some of the features you can configure when installing Sentry:

* **[Logs](https://docs.sentry.io/platforms/react-native/logs.md)**: Send, view, and query logs from your app alongside your errors to get richer context when debugging.
* **[Tracing](https://docs.sentry.io/platforms/react-native/tracing.md)**: Monitor the timing and flow of requests and operations as they happen across different systems in your application to improve performance.
* **[Session Replay](https://docs.sentry.io/platforms/react-native/session-replay.md)**: Get reproductions of user sessions to improve your app experience.
* **[Profiling](https://docs.sentry.io/platforms/react-native/profiling.md)**: Collect and analyze function-level information about your code to fine-tune performance.
* **[Application Metrics](https://docs.sentry.io/platforms/react-native/metrics.md)**: Send, view, and query counters, gauges, and measurements from your app to track health and drill down into related traces, logs, and errors.
* **[User Feedback](https://docs.sentry.io/platforms/react-native/user-feedback.md)**: Collect user feedback from anywhere inside your application at any time, without needing an error event to occur first.
* **[Size Analysis](https://docs.sentry.io/platforms/react-native/size-analysis.md)**: Monitor your mobile app's size in pre-production to prevent unexpected size increases (regressions) from reaching users.

Tracing, profiling, session replay, and logs can be added via the [Configure](https://docs.sentry.io/platforms/react-native.md#configure) section below. For the other features, refer to each product page for instructions on getting started.

## [Install](https://docs.sentry.io/platforms/react-native.md#install)

Sentry captures data by using an SDK within your application's runtime. These are platform-specific and allow Sentry to have a deep understanding of how your application works.

To install, run `@sentry/wizard`:

```bash
npx @sentry/wizard@latest -i reactNative
```

[Sentry Wizard](https://github.com/getsentry/sentry-wizard) will patch your project accordingly, though you can [set up manually](https://docs.sentry.io/platforms/react-native/manual-setup/manual-setup.md) if you prefer. You only need to patch the project once. Then you can add the patched files to your version control system.

The following tasks will be performed by the Sentry Wizard

* Install the `@sentry/react-native` package.
* Add the `@sentry/react-native/metro` to the **metro.config.js** Metro configuration.
* Add the `@sentry/react-native/expo` to the **app.json** Expo configuration.
* Enable the Sentry React Native Gradle build step for Android to auto-upload generated source maps and debug symbols.
* Wrap the *Bundle React Native code and images* Xcode project build phase script to upload generated source maps and collect bundled node modules.
* Add *Upload Debug Symbols to Sentry* Xcode project build phase.
* Run `pod install`.
* Store build credentials in **ios/sentry.properties**, **android/sentry.properties** and **.env.local**.
* Configure Sentry for the supplied DSN in your **layout.tsx**/\_*App.tsx*\_file.

If you're using Expo, [read our Expo guide](https://docs.sentry.io/platforms/react-native/guides/expo.md) to learn how to add Sentry to your Expo project. This SDK will work for both managed and bare projects.

## [Configure](https://docs.sentry.io/platforms/react-native.md#configure)

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Session Replay\[ ]Logs

To capture all errors, initialize the Sentry React Native SDK as soon as possible.

```javascript
import * as Sentry from "@sentry/react-native";

Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  // Adds more context data to events (IP address, cookies, user, etc.)
  // For more information, visit: https://docs.sentry.io/platforms/react-native/data-management/data-collected/
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance
  // Set tracesSampleRate to 1.0 to capture 100% of transactions for tracing.
  // We recommend adjusting this value in production.
  // Learn more at
  // https://docs.sentry.io/platforms/react-native/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ logs
  // Enable logs to be sent to Sentry
  // Learn more at https://docs.sentry.io/platforms/react-native/logs/
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
  // ___PRODUCT_OPTION_START___ profiling
  // profilesSampleRate is relative to tracesSampleRate.
  // Here, we'll capture profiles for 100% of transactions.
  profilesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ profiling
  // ___PRODUCT_OPTION_START___ session-replay
  // Record session replays for 100% of errors and 10% of sessions
  replaysOnErrorSampleRate: 1.0,
  replaysSessionSampleRate: 0.1,
  integrations: [Sentry.mobileReplayIntegration()],
  // ___PRODUCT_OPTION_END___ session-replay
});
```

#### [Wrap Your App](https://docs.sentry.io/platforms/react-native.md#wrap-your-app)

To automatically instrument your app with [touch event tracking](https://docs.sentry.io/platforms/react-native/configuration/touchevents.md) and [automatic tracing](https://docs.sentry.io/platforms/react-native/tracing/instrumentation/automatic-instrumentation.md), wrap it with `Sentry.wrap`:

```javascript
export default Sentry.wrap(App);
```

This is not required if your app does not have a single parent "App" component.

## [Verify](https://docs.sentry.io/platforms/react-native.md#verify)

Verify that your app is sending events to Sentry by adding the following snippet, which includes an intentional error. You should see the error reported in Sentry within a few minutes.

**Throw Error**

```javascript
throw new Error("My first Sentry error!");
```

**Native Crash**

```javascript
Sentry.nativeCrash();
```

Alternatively, you can use the [Sentry Playground](https://docs.sentry.io/platforms/react-native/manual-setup/playground.md) to interactively test your SDK setup with multiple error scenarios.

## [Next Steps](https://docs.sentry.io/platforms/react-native.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Learn about the features of Sentry's React Native SDK](https://docs.sentry.io/platforms/react-native/features.md)
* [Add readable stack traces to errors](https://docs.sentry.io/platforms/react-native/sourcemaps.md)
* [Add Apple Privacy manifest](https://docs.sentry.io/platforms/react-native/data-management/apple-privacy-manifest.md)

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
- [Agent Tracing](https://docs.sentry.io/platforms/react-native/agent-tracing.md)
- [Debug Symbols](https://docs.sentry.io/platforms/react-native/upload-debug.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/react-native/releases.md)
- [SDK Overhead](https://docs.sentry.io/platforms/react-native/overhead.md)
- [Build Distribution](https://docs.sentry.io/platforms/react-native/build-distribution.md)
- [User Feedback](https://docs.sentry.io/platforms/react-native/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/react-native/feature-flags.md)
- [Migration Guide](https://docs.sentry.io/platforms/react-native/migration.md)
- [Size Analysis](https://docs.sentry.io/platforms/react-native/size-analysis.md)
- [Troubleshooting](https://docs.sentry.io/platforms/react-native/troubleshooting.md)

