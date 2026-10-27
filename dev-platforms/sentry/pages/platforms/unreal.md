---
title: "Unreal Engine"
source: https://docs.sentry.io/platforms/unreal.md
path: platforms/unreal
---

---
title: "Unreal Engine"
description: "Learn how to set up Sentry's Unreal Engine SDK and capture your first events."
url: https://docs.sentry.io/platforms/unreal/
---

# Sentry for Unreal Engine

The Unreal Engine SDK builds on top of other Sentry SDKs and extends them with Unreal Engine-specific features. It gives developers helpful hints for where and why an error or performance issue might have occurred.

On this page, we get you up and running with Sentry's SDK.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/unreal.md#install)

Sentry captures data by using an SDK within your application’s runtime.

The Unreal Engine (UE) SDK is officially supported for the three latest UE versions. However, it is likely to be compatible with older engine versions as well depending on the specific features and functionality that you need.

We recommend downloading the latest plugin sources from the [GitHub Releases page](https://github.com/getsentry/sentry-unreal/releases), but we also support [alternate installation methods](https://docs.sentry.io/platforms/unreal/install.md).

To integrate Sentry into your Unreal Engine project using the GitHub package, select the artifact that matches your Unreal Engine version. Place the extracted files in your project's `Plugins` directory. On the next project launch, UE will prompt you to build the Sentry and SentryEditor modules.

Currently, this method is available only for C++ UE projects. Blueprint projects can be converted to a C++ one by adding an empty class using the editor.

To make sure the Sentry plugin has been enabled after installation has been completed, go to the editor and navigate to the **Settings > Plugins > Code Plugins** menu and check for the installation.

To access the plugin API from within C++, add `Sentry` support to the build script (`MyProject.build.cs`):

```csharp
PublicDependencyModuleNames.AddRange(new string[] { ..., "Sentry" });
```

On arm64 architecture, Linux is supported with UE 5.0+ and Windows with UE 5.2+.

## [Configure](https://docs.sentry.io/platforms/unreal.md#configure)

**Error Monitoring**, including automatic crash capture, starts working as soon as the SDK initializes with your [DSN](https://docs.sentry.io/concepts/key-terms/dsn-explainer.md). **Release Health** session tracking is on by default. **Logs** and **Application Metrics** need no extra configuration, and you'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/unreal.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/unreal.md#send-application-metrics-).

This guide also enables **Tracing**. The Unreal Engine SDK also supports **Session Replay** (experimental) to capture gameplay video of the moments before a crash, and **User Feedback**; see [Set Up Session Replay](https://docs.sentry.io/platforms/unreal/session-replay.md) and [Set Up User Feedback](https://docs.sentry.io/platforms/unreal/user-feedback.md).

Configure the SDK in the editor under **Project Settings > Plugins > Sentry**. The editor saves these settings to your project's `Config/DefaultEngine.ini` file, so you can also add them there directly.

The snippet also turns on:

* Tracing: via **Enable tracing** (`EnableTracing`) and [`TracesSampleRate`](https://docs.sentry.io/platforms/unreal/configuration/options.md#TracesSampleRate). Tracing captures the transactions you create with [custom instrumentation](https://docs.sentry.io/platforms/unreal/tracing/instrumentation/custom-instrumentation.md).
* User IP address and device name collection: via [`SendDefaultPii`](https://docs.sentry.io/platforms/unreal/configuration/options.md#SendDefaultPii). Review the data your game sends before enabling this in production.
* Screenshots on crash and ensure events (not supported on Android): via [`AttachScreenshot`](https://docs.sentry.io/platforms/unreal/configuration/options.md#AttachScreenshot). Only enable this if your game doesn't render sensitive data on screen.

Don't need a feature? Remove its options from the snippet.

```ini
[/Script/Sentry.SentrySettings]
; Required: set your Sentry project identifier (DSN)
Dsn="https://<key>@o<orgId>.ingest.sentry.io/<projectId>"

; Enables Tracing.
; Set to 1.0 to capture 100% of transactions for tracing.
; We recommend reducing this value in production.
EnableTracing=True
TracesSampleRate=1.0

; Adds data like the user's IP address and device name.
SendDefaultPii=True

; Attaches a screenshot to crash and ensure events.
AttachScreenshot=True
```

If you are logged in, you can also go to your [project settings](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/:projectId/keys/) and copy its DSN directly from there.

### [Initialize the SDK](https://docs.sentry.io/platforms/unreal.md#initialize-the-sdk)

By default, the SDK is automatically initialized on application startup. Alternatively, the **Initialize SDK automatically** option can be disabled and in this case, explicit SDK initialization is required.

To override SDK settings at runtime, use the `InitializeWithSettings` method of the `SentrySubsystem` class. See [Options](https://docs.sentry.io/platforms/unreal/configuration/options.md) for all available settings.

```cpp
#include "SentrySubsystem.h"

USentrySubsystem* SentrySubsystem = GEngine->GetEngineSubsystem<USentrySubsystem>();

SentrySubsystem->InitializeWithSettings(FConfigureSettingsNativeDelegate::CreateLambda([=](USentrySettings* Settings)
{
    Settings->Dsn = TEXT("https://<key>@o<orgId>.ingest.sentry.io/<projectId>");
    Settings->EnableTracing = true;
    Settings->TracesSampleRate = 1.0f;
    Settings->SendDefaultPii = true;
    Settings->AttachScreenshot = true;
}));
```

### [Set Up Crash Reporting](https://docs.sentry.io/platforms/unreal.md#set-up-crash-reporting)

The SDK automatically captures crashes on:

* Windows (UE 5.2+) and Linux by using the [Native SDK](https://docs.sentry.io/platforms/native.md) to support C and C++ with minidumps
* macOS by using the [macOS SDK](https://docs.sentry.io/platforms/apple/guides/macos.md) to support Objective-C, Swift, C and C++
* iOS by using the [iOS SDK](https://docs.sentry.io/platforms/apple/guides/ios.md) to support Objective-C, Swift, C and C++
* Android by using the [Android SDK](https://docs.sentry.io/platforms/android.md) to support Java, Kotlin, C and C++

To automatically capture crashes on Windows with UE 5.1 or older, you have to configure the [Crash Reporter Client](https://docs.sentry.io/platforms/unreal/configuration/crash-reporter/crash-reporter-client.md). Starting from UE 5.2, the provided API allows you to switch between default (CRC) and third-party (Sentry) crash-handling solutions, so the CRC configuration step isn't required. The two are mutually exclusive and can't be used simultaneously.

To collect feedback from players after a crash, use the [Sentry Crash Reporter](https://docs.sentry.io/platforms/unreal/configuration/crash-reporter/sentry-crash-reporter.md), a standalone app supported on Windows and Linux. For PlayStation, Xbox, and Nintendo Switch, see [Game Consoles](https://docs.sentry.io/platforms/unreal/game-consoles.md).

### [Upload Debug Symbols](https://docs.sentry.io/platforms/unreal.md#upload-debug-symbols)

Sentry requires [debug information files](https://docs.sentry.io/platforms/unreal/data-management/debug-files.md) to symbolicate crashes. The automated debug symbols upload is disabled by default. To turn it on, go to **Project Settings > Plugins > Sentry**, enable **Upload debug symbols automatically**, and enter your [Auth Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/), Organization Slug, and Project Name.

See [Debug Symbols Uploading](https://docs.sentry.io/platforms/unreal/configuration/debug-symbols.md) for environment variable configuration, manual upload with `sentry-cli`, and macOS and iOS setup.

### [Store Minidumps as Attachments](https://docs.sentry.io/platforms/unreal.md#store-minidumps-as-attachments)

By default, Sentry only uses minidump files to create events and immediately drops them, because [minidumps](https://docs.sentry.io/platforms/native/guides/minidumps.md#what-is-a-minidump) may contain sensitive information about the target system. To keep them, enable *Store Minidumps As Attachments* in your [organization](https://sentry.io/orgredirect/organizations/:orgslug/settings/security-and-privacy/) or [project settings](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/:projectId/security-and-privacy/) under **Security & Privacy**. This feature is supported on Windows, Linux, and Android.

See [Store Minidumps as Attachments](https://docs.sentry.io/platforms/unreal/data-management/store-minidumps-as-attachments.md) for retention and per-issue limits.

## [Send Logs](https://docs.sentry.io/platforms/unreal.md#send-logs)

Use the logging methods on the Sentry subsystem to send logs at different levels, such as `LogInfo`, `LogWarning`, or `LogError`. You can pass an optional category to organize your logs. Logs require Unreal Engine SDK version `1.2.0` or later and are enabled by default starting with version `1.11.0`.

To also forward Unreal Engine's native `UE_LOG` calls, enable the severity levels you want to send in the [Logs setup](https://docs.sentry.io/platforms/unreal/logs.md#setup).

See [Set Up Logs](https://docs.sentry.io/platforms/unreal/logs.md) for all available logging methods, attributes, and configuration options.

```cpp
#include "SentrySubsystem.h"

USentrySubsystem* SentrySubsystem = GEngine->GetEngineSubsystem<USentrySubsystem>();

SentrySubsystem->LogInfo(TEXT("User completed tutorial"));
SentrySubsystem->LogWarning(TEXT("Failed to load texture asset"), TEXT("AssetLoading"));
SentrySubsystem->LogError(TEXT("Database connection failed"), TEXT("Database"));
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/unreal.md#send-application-metrics-)

Use the Sentry subsystem to send counters, gauges, and distributions from your game to Sentry. Metrics require Unreal Engine SDK version `1.7.0` or later and are enabled by default starting with version `1.11.0`.

The SDK can also collect frame time, GC pause, game stats, and network metrics automatically. Enable them under **Project Settings > Plugins > Sentry > Metrics > Performance**, as described in [Automatic Metrics](https://docs.sentry.io/platforms/unreal/metrics.md#automatic-metrics).

See [Set Up Metrics](https://docs.sentry.io/platforms/unreal/metrics.md) for all available metric types and configuration options.

```cpp
#include "SentrySubsystem.h"

USentrySubsystem* SentrySubsystem = GEngine->GetEngineSubsystem<USentrySubsystem>();

SentrySubsystem->AddCount(TEXT("api.requests"), 1);
SentrySubsystem->AddGauge(TEXT("active_connections"), 42, USentryUnitHelper::MakeSentryUnit(ESentryUnit::None));
SentrySubsystem->AddDistribution(TEXT("response.time"), 150.5f, USentryUnitHelper::MakeSentryUnit(ESentryUnit::Millisecond));
```

## [Verify Your Setup](https://docs.sentry.io/platforms/unreal.md#verify-your-setup)

Capture a test message to confirm that Sentry is receiving data from your project:

```cpp
#include "SentrySubsystem.h"

void Verify()
{
    // Capture message
    USentrySubsystem* SentrySubsystem = GEngine->GetEngineSubsystem<USentrySubsystem>();
    SentrySubsystem->CaptureMessage(TEXT("Capture message"));
}
```

The same result can be achieved by calling the corresponding function in Blueprint:

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/unreal.md#view-captured-data-in-sentry)

To view and resolve the recorded message, log into [sentry.io](https://sentry.io) and select your project. Select **Issues** in the sidebar to find the new issue, then click its title to see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/unreal.md#next-steps)

At this point, you should have integrated Sentry into your Unreal Engine project. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors and messages](https://docs.sentry.io/platforms/unreal/usage.md)
* Instrument more operations with [custom instrumentation](https://docs.sentry.io/platforms/unreal/tracing/instrumentation/custom-instrumentation.md)
* [Set up Session Replay](https://docs.sentry.io/platforms/unreal/session-replay.md) (experimental) to capture gameplay video of the moments before a crash
* [Collect User Feedback](https://docs.sentry.io/platforms/unreal/user-feedback.md) from your players

## Topics

- [Installation Methods](https://docs.sentry.io/platforms/unreal/install.md)
- [Basic Configuration](https://docs.sentry.io/platforms/unreal/configuration.md)
- [Game Consoles](https://docs.sentry.io/platforms/unreal/game-consoles.md)
- [Usage](https://docs.sentry.io/platforms/unreal/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/unreal/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/unreal/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/unreal/tracing.md)
- [App Hangs and ANRs](https://docs.sentry.io/platforms/unreal/app-hangs.md)
- [Session Replay](https://docs.sentry.io/platforms/unreal/session-replay.md)
- [Logs](https://docs.sentry.io/platforms/unreal/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/unreal/metrics.md)
- [User Feedback](https://docs.sentry.io/platforms/unreal/user-feedback.md)
- [Migration Guide](https://docs.sentry.io/platforms/unreal/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/unreal/troubleshooting.md)

