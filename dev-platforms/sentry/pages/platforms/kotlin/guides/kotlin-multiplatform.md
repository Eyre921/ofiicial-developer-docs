---
title: "Kotlin Multiplatform"
source: https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform.md
path: platforms/kotlin/guides/kotlin-multiplatform
---

---
title: "Kotlin Multiplatform"
url: https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/
---

# Sentry for Kotlin Multiplatform

Kotlin Multiplatform lets you write code once and use it on various platforms. It makes building apps easier and more efficient by sharing common code, while still benefitting from native capabilities.

Sentry's Kotlin Multiplatform SDK builds on top of multiple Sentry SDKs, allowing developers to share code between platforms while being able to integrate Sentry's features into their applications. Installing this SDK will enable native crash reporting and automatic breadcrumbs for app lifecycle and UI events.

## [Prerequisites](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform.md#prerequisites)

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

Xcode 16 support starts with Sentry Cocoa SDK version `8.36.0` or higher.

Starting May 1, 2024, Apple requires all apps submitted to the App Store to provide a list of privacy-related APIs they use. Use Sentry Cocoa SDK version `8.25.0` or higher to ensure compliance with these requirements. Follow our [Apple Privacy Manifest](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/data-management/apple-privacy-manifest.md) guide to learn more.

## [Install](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform.md#install)

Sentry captures data by using an SDK within your application's runtime.

To install the Kotlin Multiplatform SDK, you need to add the following to your `build.gradle.kts` file in your shared module:

```kotlin
plugins {
  id("io.sentry.kotlin.multiplatform.gradle") version "0.29.0"
}
```

The plugin does the following:

* Automatically installs the Sentry KMP dependency to `commonMain`.
* Installs the Sentry Cocoa dependency for Apple targets with Swift Package Manager (SwiftPM), using Kotlin's official SwiftPM import on Kotlin 2.4 and newer, or the [spm4Kmp](https://github.com/frankois944/spm4Kmp) plugin if you've applied it.
* If you added Sentry Cocoa to your Xcode project yourself, set the Apple provider to `NONE` to avoid installing it twice. The plugin then links your existing framework. Learn more in [Install the Sentry Cocoa SDK Yourself](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/configuration/gradle.md#install-the-sentry-cocoa-sdk-yourself).

If you use Kotlin's official SwiftPM import, run Kotlin's one-time [Xcode linkage package setup](https://kotlinlang.org/docs/multiplatform/multiplatform-spm-import.html#run-the-swiftpm-integration-task) so Xcode links Sentry Cocoa into your app.

If you use spm4Kmp, apply the Sentry Gradle plugin before spm4Kmp in the `plugins` block.

Starting with version `0.28.0`, the SDK requires iOS 15, tvOS 15, macOS 12, or watchOS 9 or newer, and no longer supports installing Sentry Cocoa with CocoaPods. Learn more in the [CocoaPods migration guide](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/configuration/gradle.md#migrate-from-cocoapods).

## [Configure](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform.md#configure)

Configuration should happen as early as possible in your application's lifecycle.

**\[commonMain] SentrySetup.kt**

```kotlin
import io.sentry.kotlin.multiplatform.Sentry

fun initializeSentry() {
  Sentry.init { options ->
    options.dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
    // Adds request headers and IP for users, for more info visit:
    // https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/data-management/data-collected/
    options.sendDefaultPii = true
  }
}
```

**iosApp**

```swift
import shared

func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    SentrySetupKt.initializeSentry()
    return true
}

// OR if you're using SwiftUI:

@main
struct SwiftUIApp: App {
    init() {
        SentrySetupKt.initializeSentry()
    }
}
```

**\[androidApp] MainActivity.kt**

```kotlin
import your.kmp.app.initializeSentry

class YourApplication : Application() {
  override fun onCreate() {
    super.onCreate()
      initializeSentry()
   }
}
```

## [Verify](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform.md#verify)

This snippet includes an intentional error, so you can test that everything is working as soon as you set it up.

```kotlin
import io.sentry.kotlin.multiplatform.Sentry

fun captureError() {
  try {
    throw Exception("This is a test.")
  } catch (e: Exception) {
    Sentry.captureException(e)
  }
}
```

Learn more about manually capturing an error or message in our [Usage documentation](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/usage.md).

To view and resolve the recorded error, log into [sentry.io](https://sentry.io) and select your project. Clicking on the error's title will open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Learn more about Sentry's Kotlin Multiplatform SDK features](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/features.md)
* [Learn about different ways to initialize the SDK](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/initialization-strategies.md)
* [See configuration options for the Kotlin Multiplatform Gradle Plugin](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/configuration/gradle.md)
* [Add readable stack traces to your errors](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/debug-symbols.md)

## Other Kotlin Frameworks

- [Compose Multiplatform](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md)

## Topics

- [Features](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/features.md)
- [Initialization Options](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/initialization-strategies.md)
- [Manual Setup](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/manual-setup.md)
- [Native Access to the SDK](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/native-access-sdk.md)
- [Usage](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/usage.md)
- [Upload Debug Symbols](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/debug-symbols.md)
- [Basic Configuration](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/configuration.md)
- [Enriching Events](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/data-management.md)
- [Size Analysis](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/size-analysis.md)
- [Snapshots](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/snapshots.md)
- [Session Replay](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/session-replay.md)
- [Logs](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/logs.md)
- [Set Up User Feedback](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/user-feedback.md)
- [Troubleshooting](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/troubleshooting.md)

