---
title: "visionOS"
source: https://docs.sentry.io/platforms/apple/guides/visionos.md
path: platforms/apple/guides/visionos
---

---
title: "visionOS"
description: "Learn how to use the Sentry visionOS SDK to automatically report errors and exceptions in your application."
url: https://docs.sentry.io/platforms/apple/guides/visionos/
---

# Sentry for visionOS

On this page, we get you up and running with Sentry's Apple SDK, which will automatically report errors and exceptions in your application.

If you don't already have an account and Sentry project established, head over to [sentry.io](https://sentry.io/signup/), then return to this page.

##### Experimental Support

The support for [visionOS](https://developer.apple.com/visionos/) is currently experimental, which means it may have bugs. We recognize the irony.

## [Features](https://docs.sentry.io/platforms/apple/guides/visionos.md#features)

In addition to capturing errors, you can monitor interactions between multiple services or applications by [enabling tracing](https://docs.sentry.io/concepts/key-terms/tracing.md).

Select which Sentry features you'd like to install in addition to Error Monitoring to get the corresponding installation and configuration instructions below.

## [Install](https://docs.sentry.io/platforms/apple/guides/visionos.md#install)

Error Monitoring\[ ]Tracing\[ ]Logs

Sentry captures data by using an SDK within your application's runtime. These are platform-specific and allow Sentry to have a deep understanding of how your application works.

We recommend installing the SDK with Swift Package Manager (SPM), but we also support alternate [installation methods](https://docs.sentry.io/platforms/apple/guides/visionos/install.md). To integrate Sentry into your Xcode project, open your App in Xcode and open **File > Add Packages**. Then add the SDK by entering the git repo url in the top right search field:

```bash
https://github.com/getsentry/sentry-cocoa.git
```

## [Configure](https://docs.sentry.io/platforms/apple/guides/visionos.md#configure)

To capture all errors, we recommend to initialize the SDK on the main thread as soon as possible, such as in your `AppDelegate` `application:didFinishLaunchingWithOptions` method:

**Swift**

```swift
import Sentry

func application(_ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    SentrySDK.start { options in
        options.dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
        options.debug = true // Enabled debug when first installing is always helpful

        // Adds IP for users.
        // For more information, visit: https://docs.sentry.io/platforms/apple/data-management/data-collected/
        options.sendDefaultPii = true
        // ___PRODUCT_OPTION_START___ performance

        // Set tracesSampleRate to 1 to capture 100% of transactions for performance monitoring.
        // We recommend adjusting this value in production.
        options.tracesSampleRate = 1
        // ___PRODUCT_OPTION_END___ performance
        // ___PRODUCT_OPTION_START___ profiling

        options.configureProfiling = {
            $0.lifecycle = .trace
            $0.sessionSampleRate = 1
        }
        // ___PRODUCT_OPTION_END___ profiling
        // ___PRODUCT_OPTION_START___ logs

        // Enable logs to be sent to Sentry
        options.enableLogs = true
        // ___PRODUCT_OPTION_END___ logs
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
        options.debug = YES; // Enabled debug when first installing is always helpful

        // Adds IP for users.
        // For more information, visit: https://docs.sentry.io/platforms/apple/data-management/data-collected/
        options.sendDefaultPii = YES;

        // ___PRODUCT_OPTION_START___ performance
        // Set tracesSampleRate to 1.0 to capture 100% of transactions for performance monitoring.
        // We recommend adjusting this value in production.
        options.tracesSampleRate = @1.f;
        // ___PRODUCT_OPTION_END___ performance

        // ___PRODUCT_OPTION_START___ profiling
        options.configureProfiling = ^(SentryProfileOptions *profiling) {
            profiling.lifecycle = SentryProfileLifecycleTrace;
            profiling.sessionSampleRate = 1.f;
        };
        // ___PRODUCT_OPTION_END___ profiling
        // ___PRODUCT_OPTION_START___ logs

        // Enable logs to be sent to Sentry
        options.enableLogs = YES;
        // ___PRODUCT_OPTION_END___ logs
    }];

    return YES;
}
```

**SwiftUI with App conformer**

```swift
import Sentry

@main
struct SwiftUIApp: App {
    init() {
        SentrySDK.start { options in
            options.dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
            options.debug = true // Enabled debug when first installing is always helpful

            // Adds IP for users.
            // For more information, visit: https://docs.sentry.io/platforms/apple/data-management/data-collected/
            options.sendDefaultPii = true
            // ___PRODUCT_OPTION_START___ performance

            // Set tracesSampleRate to 1 to capture 100% of transactions for performance monitoring.
            // We recommend adjusting this value in production.
            options.tracesSampleRate = 1
            // ___PRODUCT_OPTION_END___ performance
            // ___PRODUCT_OPTION_START___ profiling

            options.configureProfiling = {
                $0.lifecycle = .trace
                $0.sessionSampleRate = 1
            }
            // ___PRODUCT_OPTION_END___ profiling
            // ___PRODUCT_OPTION_START___ logs

            // Enable logs to be sent to Sentry
            options.enableLogs = true
            // ___PRODUCT_OPTION_END___ logs
        }
    }
}
```

## [Verify](https://docs.sentry.io/platforms/apple/guides/visionos.md#verify)

Verify that your app is sending events to Sentry by adding the following snippet, which includes an intentional error. You should see the error reported in Sentry within a few minutes.

To verify crashes, ensure you run your application without a debugger attached. Otherwise, the SDK won't capture the crash.

**Swift**

```swift
import Sentry

do {
    try aMethodThatMightFail()
} catch {
    SentrySDK.capture(error: error)
}
```

**Objective-C**

```objc
@import Sentry;

NSError *error = nil;
[self aMethodThatMightFail:&error]

if (error) {
    [SentrySDK captureError:error];
}
```

## [Next Steps](https://docs.sentry.io/platforms/apple/guides/visionos.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Learn more about Sentry's Apple SDK features](https://docs.sentry.io/platforms/apple/guides/visionos/features.md)
* [Add readable stack traces to errors](https://docs.sentry.io/platforms/apple/guides/visionos/dsym.md)
* [Add Apple Privacy manifest](https://docs.sentry.io/platforms/apple/guides/visionos/data-management/apple-privacy-manifest.md)

## [FAQ](https://docs.sentry.io/platforms/apple/guides/visionos.md#faq)

Can I initialize the SDK from a background thread?

Yes, you can initialize the SDK from a background thread, but this is **not recommended**. Some initialization steps, like collecting view hierarchy information, must still run on the main thread. Initializing on the main thread also ensures reliable detection of app launch crashes.

## Other Apple Frameworks

- [iOS](https://docs.sentry.io/platforms/apple/guides/ios.md)
- [macOS](https://docs.sentry.io/platforms/apple/guides/macos.md)
- [tvOS](https://docs.sentry.io/platforms/apple/guides/tvos.md)
- [watchOS](https://docs.sentry.io/platforms/apple/guides/watchos.md)

## Topics

- [Features](https://docs.sentry.io/platforms/apple/guides/visionos/features.md)
- [Installation Methods](https://docs.sentry.io/platforms/apple/guides/visionos/install.md)
- [Source Context](https://docs.sentry.io/platforms/apple/guides/visionos/sourcecontext.md)
- [Extended Configuration](https://docs.sentry.io/platforms/apple/guides/visionos/configuration.md)
- [Application Metrics](https://docs.sentry.io/platforms/apple/guides/visionos/metrics.md)
- [Capturing Errors](https://docs.sentry.io/platforms/apple/guides/visionos/usage.md)
- [Uploading Debug Symbols](https://docs.sentry.io/platforms/apple/guides/visionos/dsym.md)
- [Integrations](https://docs.sentry.io/platforms/apple/guides/visionos/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/apple/guides/visionos/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/apple/guides/visionos/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/apple/guides/visionos/tracing.md)
- [Snapshots](https://docs.sentry.io/platforms/apple/guides/visionos/snapshots.md)
- [Session Replay](https://docs.sentry.io/platforms/apple/guides/visionos/session-replay.md)
- [Feature Flags](https://docs.sentry.io/platforms/apple/guides/visionos/feature-flags.md)
- [Logs](https://docs.sentry.io/platforms/apple/guides/visionos/logs.md)
- [User Feedback](https://docs.sentry.io/platforms/apple/guides/visionos/user-feedback.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/apple/guides/visionos/releases.md)
- [SDK Overhead](https://docs.sentry.io/platforms/apple/guides/visionos/overhead.md)
- [Migration Guide](https://docs.sentry.io/platforms/apple/guides/visionos/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/apple/guides/visionos/troubleshooting.md)

