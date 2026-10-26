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

On this page, we get you up and running with Sentry's Apple SDK, which will automatically report errors and exceptions in your application.

If you don't already have an account and Sentry project established, head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Features](https://docs.sentry.io/platforms/apple/guides/ios.md#features)

In addition to capturing errors, you can monitor interactions between multiple services or applications by [enabling tracing](https://docs.sentry.io/concepts/key-terms/tracing.md). You can also collect and analyze performance profiles from real users with [profiling](https://docs.sentry.io/product/profiling.md).

Select which Sentry features you'd like to install in addition to Error Monitoring to get the corresponding installation and configuration instructions below.

## [Install](https://docs.sentry.io/platforms/apple/guides/ios.md#install)

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Session Replay\[ ]Logs

Sentry captures data by using an SDK within your application's runtime. These are platform-specific and allow Sentry to have a deep understanding of how your application works.

We recommend installing the SDK through our [Sentry Wizard](https://github.com/getsentry/sentry-wizard) by running the following command inside your project directory:

```bash
brew install getsentry/tools/sentry-wizard && sentry-wizard -i ios
```

This will patch your project and configure the SDK. You'll only need to patch the project once, then you'll be able to add the patched files to your version control system. If you prefer, you can also [set up the SDK manually](https://docs.sentry.io/platforms/apple/guides/ios/manual-setup.md) or follow the instructions below to adapt the [configuration](https://docs.sentry.io/platforms/apple/guides/ios.md#configure).

The following tasks will be performed by the Sentry Wizard

* Install the Sentry SDK via Swift Package Manager
* Update your `AppDelegate` or SwiftUI App Initializer with the default Sentry configuration and an example error
* Add a new `Upload Debug Symbols` phase to your `xcodebuild` build script
* Create `.sentryclirc` with an auth token to upload debug symbols (this file is automatically added to `.gitignore`)
* If you're using Fastlane, a lane for uploading debug symbols to Sentry will be added

## [Configure](https://docs.sentry.io/platforms/apple/guides/ios.md#configure)

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
        // ___PRODUCT_OPTION_START___ session-replay

        // Record session replays for 100% of errors and 10% of sessions
        options.sessionReplay.onErrorSampleRate = 1.0
        options.sessionReplay.sessionSampleRate = 0.1
        // ___PRODUCT_OPTION_END___ session-replay
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
        // ___PRODUCT_OPTION_START___ session-replay

        // Record session replays for 100% of errors and 10% of sessions
        options.sessionReplay.onErrorSampleRate = 1.0;
        options.sessionReplay.sessionSampleRate = 0.1;
        // ___PRODUCT_OPTION_END___ session-replay
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
            // ___PRODUCT_OPTION_START___ session-replay
            // Record session replays for 100% of errors and 10% of sessions
            options.sessionReplay.onErrorSampleRate = 1.0
            options.sessionReplay.sessionSampleRate = 0.1
            // ___PRODUCT_OPTION_END___ session-replay

            // ___PRODUCT_OPTION_START___ logs
            // Enable logs to be sent to Sentry
            options.enableLogs = true
            // ___PRODUCT_OPTION_END___ logs
        }
    }
}
```

## [Verify](https://docs.sentry.io/platforms/apple/guides/ios.md#verify)

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

## [Next Steps](https://docs.sentry.io/platforms/apple/guides/ios.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Learn more about Sentry's Apple SDK features](https://docs.sentry.io/platforms/apple/guides/ios/features.md)
* [Add readable stack traces to errors](https://docs.sentry.io/platforms/apple/guides/ios/dsym.md)
* [Add Apple Privacy manifest](https://docs.sentry.io/platforms/apple/guides/ios/data-management/apple-privacy-manifest.md)

## [FAQ](https://docs.sentry.io/platforms/apple/guides/ios.md#faq)

Can I initialize the SDK from a background thread?

Yes, you can initialize the SDK from a background thread, but this is **not recommended**. Some initialization steps, like collecting view hierarchy information, must still run on the main thread. Initializing on the main thread also ensures reliable detection of app launch crashes.

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

