---
title: "iOS"
source: https://docs.sentry.io/platforms/apple/guides/ios.md
path: platforms/apple/guides/ios
---

---
title: "iOS"
description: "Learn how to use Sentry's Apple SDK to automatically report errors, crashes, watchdog terminations, and app hangs in your application."
url: https://docs.sentry.io/platforms/apple/guides/ios/
---

# Sentry for iOS

On this page, you'll set up Sentry's Apple SDK to report errors and exceptions in your application.

If you don't already have a Sentry account and project, [create them](https://sentry.io/signup/) before you continue.

## [Prerequisites](https://docs.sentry.io/platforms/apple/guides/ios.md#prerequisites)

The examples below use Sentry Cocoa SDK 9.27.0 or later. Minimum OS versions for SDK 9.25.0 and later are:

* iOS 15.0

If your app supports older OS versions, use a compatible earlier SDK release. See the [migration guides](https://docs.sentry.io/platforms/apple/guides/ios/migration.md) for version-specific requirements.

## [Install](https://docs.sentry.io/platforms/apple/guides/ios.md#install)

Sentry captures data by using an SDK within your application's runtime. We recommend installing the SDK with Swift Package Manager (SPM).

### [Automatic Install](https://docs.sentry.io/platforms/apple/guides/ios.md#automatic-install)

The [Sentry Wizard](https://github.com/getsentry/sentry-wizard) installs the SDK and adds an initial configuration. Run this command from your project directory:

```bash
brew install getsentry/tools/sentry-wizard && sentry-wizard -i ios
```

Review and commit the files the wizard modifies.

The following tasks will be performed by the Sentry Wizard

* Install the Sentry SDK with Swift Package Manager
* Update your `AppDelegate` or SwiftUI app initializer with the initial Sentry configuration and an example message
* Add an `Upload Debug Symbols` build phase to your Xcode target
* Create `.sentryclirc` with an auth token for uploading debug symbols (the file is added to `.gitignore`)
* Add a Fastlane lane for uploading debug symbols if you're using Fastlane

**Return to this guide after running the wizard to complete setup.** The wizard doesn't configure Session Replay, instrument your SwiftUI views, or add application-specific logs and metrics.

Continue with [Configure](https://docs.sentry.io/platforms/apple/guides/ios.md#configure), merge the settings into the existing `SentrySDK.start` call, and follow the remaining steps to send and verify your data.

Wizard 9.0.0 also needs these corrections when used with the SDK versions in this guide:

* Remove `options.experimental.enableLogs` if the wizard adds it. SDK 9.27.0+ sends logs through `SentrySDK.logger` without an enable flag.
* In Objective-C, replace `SentryProfilingLifecycleTrace` with `SentryProfileLifecycleTrace`.

### [Manual Install](https://docs.sentry.io/platforms/apple/guides/ios.md#manual-install)

To install without the wizard, follow the SPM instructions below. If you used the wizard, skip to [Configure](https://docs.sentry.io/platforms/apple/guides/ios.md#configure). For more detail, see [Manual Setup](https://docs.sentry.io/platforms/apple/guides/ios/manual-setup.md).

In Xcode, open **File > Add Package Dependencies**, then enter this repository URL:

```bash
https://github.com/getsentry/sentry-cocoa.git
```

Select a compatible SDK version and add **one** SDK product to your application target:

* **SentrySPM** builds the SDK from source and is the recommended choice.
* **Sentry** uses the prebuilt static framework.

Both products use `import Sentry`. See [Swift Package Manager](https://docs.sentry.io/platforms/apple/guides/ios/install/swift-package-manager.md) for other products, or [the installation options](https://docs.sentry.io/platforms/apple/guides/ios/install.md) for other installation methods.

## [Configure](https://docs.sentry.io/platforms/apple/guides/ios.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK.

This guide also configures **Tracing**, **Profiling**, and **Session Replay**, and shows you how to send **Logs**.

**Application Metrics** are enabled by default, but aren't collected automatically. See [Send Application Metrics](https://docs.sentry.io/platforms/apple/guides/ios.md#send-application-metrics-) to record your own metrics.

The snippets set `sendDefaultPii` to include IP addresses. Remove that option if you don't want to send this data. Remove other options for features you don't need.

We recommend initializing the SDK **on the main thread**, as early as possible. See [the background-thread initialization FAQ](https://docs.sentry.io/platforms/apple/guides/ios/troubleshooting.md#can-i-initialize-the-sdk-from-a-background-thread) for details.

Set `debug` to `false` or remove it after setup, and reduce sampling rates before using the configuration in production.

### [Initialize the SDK](https://docs.sentry.io/platforms/apple/guides/ios.md#initialize-the-sdk)

Initialize the SDK in your app delegate's `application(_:didFinishLaunchingWithOptions:)` method or your SwiftUI `App` initializer. Session Replay requires Sentry Cocoa SDK 8.31.1+ and supports the iOS versions supported by that SDK; it doesn't require iOS 16. UI Profiling requires SDK 8.49.0+.

**Swift**

```swift
import Sentry

func application(_ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    SentrySDK.start { options in
        options.dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
        options.debug = true
        options.sendDefaultPii = true

        // Enable Tracing. Reduce this value in production.
        options.tracesSampleRate = 1.0

        // Enable Profiling.
        options.configureProfiling = {
            $0.lifecycle = .trace
            $0.sessionSampleRate = 1.0
        }

        // Enable Session Replay.
        options.sessionReplay.onErrorSampleRate = 1.0
        options.sessionReplay.sessionSampleRate = 0.1
    }
    return true
}
```

**Objective-C**

```objc
@import Sentry;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
        options.dsn = @"https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
        options.debug = YES;
        options.sendDefaultPii = YES;

        // Enable Tracing. Reduce this value in production.
        options.tracesSampleRate = @1.0;

        // Enable Profiling.
        options.configureProfiling = ^(SentryProfileOptions *profiling) {
            profiling.lifecycle = SentryProfileLifecycleTrace;
            profiling.sessionSampleRate = 1.0;
        };

        // Enable Session Replay.
        options.sessionReplay.onErrorSampleRate = 1.0;
        options.sessionReplay.sessionSampleRate = 0.1;
    }];
    return YES;
}
```

**SwiftUI with App conformer**

```swift
import Sentry
import SwiftUI

@main
struct ExampleApp: App {
    init() {
        SentrySDK.start { options in
            options.dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
            options.debug = true
            options.sendDefaultPii = true
            options.tracesSampleRate = 1.0
            options.configureProfiling = {
                $0.lifecycle = .trace
                $0.sessionSampleRate = 1.0
            }
            options.sessionReplay.onErrorSampleRate = 1.0
            options.sessionReplay.sessionSampleRate = 0.1
        }
    }

    var body: some Scene {
        WindowGroup {
            SentryTracedView("Home") {
                Text("Hello, world!")
            }
        }
    }
}
```

For SwiftUI, keep your existing app content inside `WindowGroup` and wrap the views you want to measure with `SentryTracedView`, as shown above. See [SwiftUI Instrumentation](https://docs.sentry.io/platforms/apple/guides/ios/tracing/instrumentation/swiftui-instrumentation.md) for more options.

### [Send a Test Trace](https://docs.sentry.io/platforms/apple/guides/ios.md#send-a-test-trace)

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

With the `.trace` profiling lifecycle used above, profiling runs while sampled root spans are active. Configure and start a transaction to collect profiles; setting a profile sample rate alone doesn't start the profiler. See [Set Up Apple Profiling](https://docs.sentry.io/platforms/apple/guides/ios/profiling.md) for other lifecycles.

## [Send Logs](https://docs.sentry.io/platforms/apple/guides/ios.md#send-logs)

Use `SentrySDK.logger` after initializing the SDK to send logs on all supported Apple platforms, including watchOS. In SDK 9.27.0+, these calls don't require an enable flag.

For SDK 9.0.0–9.26.x, set `options.enableLogs = true` during initialization. For SDK 8.55.0–8.x, use `options.experimental.enableLogs = true`. See [Set Up Logs](https://docs.sentry.io/platforms/apple/guides/ios/logs.md) for logging methods and options.

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

To stop sending logs, remove the logging calls or filter them with [`beforeSendLog`](https://docs.sentry.io/platforms/apple/guides/ios/logs.md#beforesendlog). In SDK 9.27.0+, setting `enableLogs` to `false` doesn't drop logs sent through this API.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/apple/guides/ios.md#send-application-metrics-)

Application Metrics are enabled by default, but you must record them explicitly. In Sentry Cocoa SDK 9.12.0 and later, use `SentrySDK.metrics` to send counters, gauges, and distributions. Metrics were experimental in versions 9.2.0–9.11.x.

`SentrySDK.metrics` is a Swift API. Objective-C projects can use `SentryObjCSDK.metrics` through the separate `SentryObjC` framework, available since SDK 9.16.0. See [Set Up Metrics](https://docs.sentry.io/platforms/apple/guides/ios/metrics.md) for usage and filtering options.

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

## [Upload Debug Symbols](https://docs.sentry.io/platforms/apple/guides/ios.md#upload-debug-symbols)

Upload your app's debug symbols (dSYMs) so Sentry can show function names and source locations in stack traces. Follow [Uploading Debug Symbols](https://docs.sentry.io/platforms/apple/guides/ios/dsym.md) to configure uploads for your builds.

If you used the wizard, it already added an upload build phase. Check that uploads succeed, and set `SENTRY_AUTH_TOKEN` in your CI environment so CI builds can upload symbols too.

## [Verify Your Setup](https://docs.sentry.io/platforms/apple/guides/ios.md#verify-your-setup)

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

This verifies handled-error delivery. To test crash reporting, run your app **without a debugger attached**, trigger a test crash, then relaunch the app so the SDK can send the report. See [Capturing Errors](https://docs.sentry.io/platforms/apple/guides/ios/usage.md) for more ways to capture events.

## [Next Steps](https://docs.sentry.io/platforms/apple/guides/ios.md#next-steps)

At this point, you've integrated Sentry into your Apple application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Explore the SDK's features and platform limitations](https://docs.sentry.io/platforms/apple/guides/ios/features.md)

## Other Apple Frameworks

- [macOS](https://docs.sentry.io/platforms/apple/guides/macos.md)
- [tvOS](https://docs.sentry.io/platforms/apple/guides/tvos.md)
- [visionOS](https://docs.sentry.io/platforms/apple/guides/visionos.md)
- [watchOS](https://docs.sentry.io/platforms/apple/guides/watchos.md)

## Topics

- [Features](https://docs.sentry.io/platforms/apple/guides/ios/features.md)
- [Installation Methods](https://docs.sentry.io/platforms/apple/guides/ios/install.md)
- [Manual Setup](https://docs.sentry.io/platforms/apple/guides/ios/manual-setup.md)
- [Source Context](https://docs.sentry.io/platforms/apple/guides/ios/sourcecontext.md)
- [Extended Configuration](https://docs.sentry.io/platforms/apple/guides/ios/configuration.md)
- [Application Metrics](https://docs.sentry.io/platforms/apple/guides/ios/metrics.md)
- [Capturing Errors](https://docs.sentry.io/platforms/apple/guides/ios/usage.md)
- [Uploading Debug Symbols](https://docs.sentry.io/platforms/apple/guides/ios/dsym.md)
- [Integrations](https://docs.sentry.io/platforms/apple/guides/ios/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/apple/guides/ios/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/apple/guides/ios/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/apple/guides/ios/tracing.md)
- [Size Analysis](https://docs.sentry.io/platforms/apple/guides/ios/size-analysis.md)
- [Build Distribution](https://docs.sentry.io/platforms/apple/guides/ios/build-distribution.md)
- [Snapshots](https://docs.sentry.io/platforms/apple/guides/ios/snapshots.md)
- [Profiling](https://docs.sentry.io/platforms/apple/guides/ios/profiling.md)
- [Session Replay](https://docs.sentry.io/platforms/apple/guides/ios/session-replay.md)
- [Feature Flags](https://docs.sentry.io/platforms/apple/guides/ios/feature-flags.md)
- [Logs](https://docs.sentry.io/platforms/apple/guides/ios/logs.md)
- [User Feedback](https://docs.sentry.io/platforms/apple/guides/ios/user-feedback.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/apple/guides/ios/releases.md)
- [SDK Overhead](https://docs.sentry.io/platforms/apple/guides/ios/overhead.md)
- [Migration Guide](https://docs.sentry.io/platforms/apple/guides/ios/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/apple/guides/ios/troubleshooting.md)

