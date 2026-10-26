---
title: "Compose Multiplatform"
source: https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md
path: platforms/kotlin/guides/compose-multiplatform
---

---
title: "Compose Multiplatform"
description: "Learn how to integrate Sentry's Kotlin Multiplatform SDK into your Compose Multiplatform project for cross-platform error tracking."
url: https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform/
---

# Sentry for Compose Multiplatform

##### Experimental Support

While Sentry's Kotlin Multiplatform SDK works in Compose Multiplatform (CMP) projects, it isn't natively supported or fully tested for CMP. Some features may behave unexpectedly or provide incomplete data. Use with caution in production environments and report any issues you encounter.

## [Overview](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#overview)

**Compose Multiplatform** is JetBrains' declarative UI framework that allows you to build native user interfaces for desktop, web, and mobile platforms using a single Kotlin codebase. It extends Jetpack Compose beyond Android to create multiplatform applications.

You need to use the [Sentry Kotlin Multiplatform SDK](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform.md) which provides error tracking across multiple Kotlin targets. While the SDK functions in Compose Multiplatform projects use the same APIs as pure KMP setups, it's important to note a few differences:

* **Experimental support**: The KMP SDK works in CMP projects and currently supports capturing crashes and errors as well as other basic features that are available through the Sentry KMP SDK.
* **Not CMP-native**: No specific CMP optimizations or testing.
* **Untested edge cases**: Some platform-specific behaviors may be incomplete.

## [Installation](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#installation)

Sentry captures data by using an SDK within your application's runtime.

To install the Kotlin Multiplatform SDK in your Compose Multiplatform project, you need to add the following to your `build.gradle.kts` file in your shared module:

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

## [Configure](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#configure)

Configuration should happen as early as possible in your application's lifecycle to ensure a working instrumentation. Configure with the following steps:

1. Add a function to initialize Sentry to your shared module (`commonMain`).
2. Call the function in your iOS and Android app modules.

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
import ComposeApp // Replace this with the name of the shared framework

@main
struct iOSApp: App {
    init() {
        SentrySetupKt.initializeSentry()
    }
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

// OR alternatively in AppDelegate:


func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    SentrySetupKt.initializeSentry()
    return true
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

## [Verify](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#verify)

This snippet includes an intentional error, so you can test that everything is working as soon as you set it up.

```kotlin
import io.sentry.kotlin.multiplatform.Sentry

// Add the following button to your Compose UI and click it to trigger an error
Button(onClick = {
    try {
        throw Exception("Sentry works!")
    } catch (e: Exception) {
        Sentry.captureException(e)
    }
}) {
    Text("Send an error to Sentry")
}
```

## [Supported Platforms](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#supported-platforms)

For a complete list of supported platforms and target presets, see the [Kotlin Multiplatform features documentation](https://docs.sentry.io/platforms/kotlin/guides/kotlin-multiplatform/features.md#supported-platforms).

## [Debug Symbols](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#debug-symbols)

Error stack traces in your app might appear unreadable or obfuscated, making it hard to debug issues. To make stack traces clear and human-readable in Sentry, you need to upload your app's debug symbols.

### [Android](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#android)

For Android applications, you need to manually upload ProGuard mapping files using the `sentry-cli`. Follow the [ProGuard Mapping Upload guide](https://docs.sentry.io/cli/dif.md#proguard-mapping-upload) for detailed instructions.

### [iOS](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#ios)

For iOS applications, follow the [Uploading Debug Symbols guide](https://docs.sentry.io/platforms/apple/guides/ios/dsym.md) to set up debug symbols upload.

## [Next Steps](https://docs.sentry.io/platforms/kotlin/guides/compose-multiplatform.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

