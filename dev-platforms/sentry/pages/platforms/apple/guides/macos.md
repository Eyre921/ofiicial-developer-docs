---
title: "macOS"
source: https://docs.sentry.io/platforms/apple/guides/macos.md
path: platforms/apple/guides/macos
---

---
title: "macOS"
description: "Learn how to use the Sentry macOS SDK to automatically report errors and exceptions in your application."
url: https://docs.sentry.io/platforms/apple/guides/macos/
---

# Sentry for macOS

On this page, you'll set up Sentry's Apple SDK to report errors and exceptions in your application.

If you don't already have a Sentry account and project, [create them](https://sentry.io/signup/) before you continue.

## [Prerequisites](https://docs.sentry.io/platforms/apple/guides/macos.md#prerequisites)

The examples below use Sentry Cocoa SDK 9.27.0 or later. Minimum OS versions for SDK 9.25.0 and later are:

* macOS 12.0

If your app supports older OS versions, use a compatible earlier SDK release. See the [migration guides](https://docs.sentry.io/platforms/apple/guides/macos/migration.md) for version-specific requirements.

## [Install](https://docs.sentry.io/platforms/apple/guides/macos.md#install)

Sentry captures data by using an SDK within your application's runtime. We recommend installing the SDK with Swift Package Manager (SPM).

In Xcode, open **File > Add Package Dependencies**, then enter this repository URL:

```bash
https://github.com/getsentry/sentry-cocoa.git
```

Select a compatible SDK version and add **one** SDK product to your application target:

* **SentrySPM** builds the SDK from source and is the recommended choice.
* **Sentry** uses the prebuilt static framework.

Both products use `import Sentry`. See [Swift Package Manager](https://docs.sentry.io/platforms/apple/guides/macos/install/swift-package-manager.md) for other products, or [the installation options](https://docs.sentry.io/platforms/apple/guides/macos/install.md) for other installation methods.

## [Configure](https://docs.sentry.io/platforms/apple/guides/macos.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK.

This guide also configures **Tracing** and **Profiling**, and shows you how to send **Logs**.

**Application Metrics** are enabled by default, but aren't collected automatically. See [Send Application Metrics](https://docs.sentry.io/platforms/apple/guides/macos.md#send-application-metrics-) to record your own metrics.

The snippets set `sendDefaultPii` to include IP addresses. Remove that option if you don't want to send this data. Remove other options for features you don't need.

We recommend initializing the SDK **on the main thread**, as early as possible. See [the background-thread initialization FAQ](https://docs.sentry.io/platforms/apple/guides/macos/troubleshooting.md#can-i-initialize-the-sdk-from-a-background-thread) for details.

Set `debug` to `false` or remove it after setup, and reduce sampling rates before using the configuration in production.

### [Initialize the SDK](https://docs.sentry.io/platforms/apple/guides/macos.md#initialize-the-sdk-1)

Initialize the SDK in your app delegate's `applicationDidFinishLaunching(_:)` method or your SwiftUI `App` initializer. The snippet configures Tracing and Profiling. UI Profiling requires Sentry Cocoa SDK 8.49.0+. macOS doesn't support Session Replay.

```swift
import Sentry

SentrySDK.start { options in
    options.dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
    options.debug = true
    options.sendDefaultPii = true
    options.enableUncaughtNSExceptionReporting = true

    // Enable Tracing. Reduce this value in production.
    options.tracesSampleRate = 1.0

    // Enable Profiling.
    options.configureProfiling = {
        $0.lifecycle = .trace
        $0.sessionSampleRate = 1.0
    }
}
```

*Other available variations of the above snippet: Objective-C*

On macOS, the SDK can't capture uncaught exceptions without additional configuration. The snippets enable `enableUncaughtNSExceptionReporting`, which also sets `NSApplicationCrashOnExceptions` so the app crashes on an uncaught exception.

Don't combine this option with `SentryCrashExceptionApplication`, which can cause duplicate reports. See [capturing uncaught exceptions](https://docs.sentry.io/platforms/apple/guides/macos/usage.md#capturing-uncaught-exceptions) for details.

### [Send a Test Trace](https://docs.sentry.io/platforms/apple/guides/macos.md#send-a-test-trace)

Sampling settings determine which transactions to send; they don't create transactions. Start a transaction around an operation in your app and finish it when the operation completes:

**Swift**

```swift
let transaction = SentrySDK.startTransaction(
    name: "Example Operation",
    operation: "task",
    bindToScope: true
)

// Perform the operation you want to measure.

transaction.finish()
```

**Objective-C**

```objc
id<SentrySpan> transaction = [SentrySDK startTransactionWithName:@"Example Operation"
                                                    operation:@"task"
                                                  bindToScope:YES];

// Perform the operation you want to measure.

[transaction finish];
```

For asynchronous work, finish the transaction in the completion handler. Binding a transaction to the scope lets automatic instrumentation, such as HTTP tracing, attach child spans to it.

macOS and watchOS don't automatically create UIKit screen-load or app-start transactions. Add transactions around operations you want to measure, as shown above, or instrument your views with [SwiftUI Instrumentation](https://docs.sentry.io/platforms/apple/guides/macos/tracing/instrumentation/swiftui-instrumentation.md).

With the `.trace` profiling lifecycle used above, profiling runs while sampled root spans are active. Configure and start a transaction to collect profiles; setting a profile sample rate alone doesn't start the profiler. See [Set Up Apple Profiling](https://docs.sentry.io/platforms/apple/guides/macos/profiling.md) for other lifecycles.

## [Send Logs](https://docs.sentry.io/platforms/apple/guides/macos.md#send-logs)

Use `SentrySDK.logger` after initializing the SDK to send logs on all supported Apple platforms, including watchOS. In SDK 9.27.0+, these calls don't require an enable flag.

For SDK 9.0.0–9.26.x, set `options.enableLogs = true` during initialization. For SDK 8.55.0–8.x, use `options.experimental.enableLogs = true`. See [Set Up Logs](https://docs.sentry.io/platforms/apple/guides/macos/logs.md) for logging methods and options.

**Swift**

```swift
SentrySDK.logger.info("User example action completed")

SentrySDK.logger.warn("Slow operation detected", attributes: [
    "operation": "data_fetch",
    "duration": 3500
])
```

**Objective-C**

```objc
SentryLogger *logger = SentrySDK.logger;
[logger info:@"User example action completed"];
[logger warn:@"Slow operation detected" attributes:@{
    @"operation": @"data_fetch",
    @"duration": @3500
}];
```

To stop sending logs, remove the logging calls or filter them with [`beforeSendLog`](https://docs.sentry.io/platforms/apple/guides/macos/logs.md#beforesendlog). In SDK 9.27.0+, setting `enableLogs` to `false` doesn't drop logs sent through this API.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/apple/guides/macos.md#send-application-metrics-)

Application Metrics are enabled by default, but you must record them explicitly. In Sentry Cocoa SDK 9.12.0 and later, use `SentrySDK.metrics` to send counters, gauges, and distributions. Metrics were experimental in versions 9.2.0–9.11.x.

`SentrySDK.metrics` is a Swift API. Objective-C projects can use `SentryObjCSDK.metrics` through the separate `SentryObjC` framework, available since SDK 9.16.0. See [Set Up Metrics](https://docs.sentry.io/platforms/apple/guides/macos/metrics.md) for usage and filtering options.

```swift
SentrySDK.metrics.count(key: "checkout.failed", value: 1)

SentrySDK.metrics.gauge(key: "time_since_refresh", value: 4, unit: .hour)

SentrySDK.metrics.distribution(
    key: "api_latency",
    value: 187,
    unit: .millisecond,
    attributes: ["endpoint": "/api/orders"]
)
```

## [Upload Debug Symbols](https://docs.sentry.io/platforms/apple/guides/macos.md#upload-debug-symbols)

Upload your app's debug symbols (dSYMs) so Sentry can show function names and source locations in stack traces. Follow [Uploading Debug Symbols](https://docs.sentry.io/platforms/apple/guides/macos/dsym.md) to configure uploads for your builds.

## [Verify Your Setup](https://docs.sentry.io/platforms/apple/guides/macos.md#verify-your-setup)

Capture a handled test error after initializing the SDK. You should see it in your Sentry project's Issues page within a few minutes.

**Swift**

```swift
import Foundation
import Sentry

SentrySDK.capture(error: NSError(domain: "SentryTest", code: 1))
```

**Objective-C**

```objc
[SentrySDK captureError:[NSError errorWithDomain:@"SentryTest" code:1 userInfo:nil]];
```

This verifies handled-error delivery. To test crash reporting, run your app **without a debugger attached**, trigger a test crash, then relaunch the app so the SDK can send the report. See [Capturing Errors](https://docs.sentry.io/platforms/apple/guides/macos/usage.md) for more ways to capture events.

## [Next Steps](https://docs.sentry.io/platforms/apple/guides/macos.md#next-steps)

At this point, you've integrated Sentry into your Apple application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Explore the SDK's features and platform limitations](https://docs.sentry.io/platforms/apple/guides/macos/features.md)

## Other Apple Frameworks

- [iOS](https://docs.sentry.io/platforms/apple/guides/ios.md)
- [tvOS](https://docs.sentry.io/platforms/apple/guides/tvos.md)
- [visionOS](https://docs.sentry.io/platforms/apple/guides/visionos.md)
- [watchOS](https://docs.sentry.io/platforms/apple/guides/watchos.md)

## Topics

- [Features](https://docs.sentry.io/platforms/apple/guides/macos/features.md)
- [Installation Methods](https://docs.sentry.io/platforms/apple/guides/macos/install.md)
- [Source Context](https://docs.sentry.io/platforms/apple/guides/macos/sourcecontext.md)
- [Extended Configuration](https://docs.sentry.io/platforms/apple/guides/macos/configuration.md)
- [Application Metrics](https://docs.sentry.io/platforms/apple/guides/macos/metrics.md)
- [Capturing Errors](https://docs.sentry.io/platforms/apple/guides/macos/usage.md)
- [Uploading Debug Symbols](https://docs.sentry.io/platforms/apple/guides/macos/dsym.md)
- [Integrations](https://docs.sentry.io/platforms/apple/guides/macos/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/apple/guides/macos/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/apple/guides/macos/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/apple/guides/macos/tracing.md)
- [Snapshots](https://docs.sentry.io/platforms/apple/guides/macos/snapshots.md)
- [Profiling](https://docs.sentry.io/platforms/apple/guides/macos/profiling.md)
- [Session Replay](https://docs.sentry.io/platforms/apple/guides/macos/session-replay.md)
- [Feature Flags](https://docs.sentry.io/platforms/apple/guides/macos/feature-flags.md)
- [Logs](https://docs.sentry.io/platforms/apple/guides/macos/logs.md)
- [User Feedback](https://docs.sentry.io/platforms/apple/guides/macos/user-feedback.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/apple/guides/macos/releases.md)
- [SDK Overhead](https://docs.sentry.io/platforms/apple/guides/macos/overhead.md)
- [Migration Guide](https://docs.sentry.io/platforms/apple/guides/macos/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/apple/guides/macos/troubleshooting.md)

