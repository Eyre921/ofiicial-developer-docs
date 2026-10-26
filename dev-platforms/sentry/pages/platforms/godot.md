---
title: "Godot Engine"
source: https://docs.sentry.io/platforms/godot.md
path: platforms/godot
---

---
title: "Godot Engine"
description: "Learn how to set up Sentry's Godot Engine SDK for error monitoring and performance tracking."
url: https://docs.sentry.io/platforms/godot/
---

# Sentry for Godot Engine

Our SDK for Godot Engine builds on top of existing Sentry SDKs, extending them with Godot-specific features. It gives developers helpful hints for where and why an error or performance issue might have occurred.

**Features:**

* Native support for automatic crash and error reporting for:

  * Windows and Linux using the [Native SDK](https://docs.sentry.io/platforms/native.md) to support C and C++ with minidumps
  * macOS 12 Monterey or later using the [macOS SDK](https://docs.sentry.io/platforms/apple/guides/macos.md) to support Objective-C, Swift, C and C++
  * iOS 15 or later using the [iOS SDK](https://docs.sentry.io/platforms/apple/guides/ios.md) to support Objective-C, Swift, C and C++
  * Android using the [Android SDK](https://docs.sentry.io/platforms/android.md) to support Java, Kotlin, C and C++
  * Web using the [JavaScript SDK](https://docs.sentry.io/platforms/javascript.md) to support WebAssembly and JavaScript

* Automatically capture Godot runtime errors, such as script and shader errors

* Capture errors from [C# (.NET) code](https://docs.sentry.io/platforms/godot/dotnet.md), with scope and traces shared across both languages

* GDScript stack traces with optional [local and member variable](https://docs.sentry.io/platforms/godot/configuration/options.md#godot_logger.include_variables) information

* Include surrounding script source code with events when available at runtime

* [Structured Logs](https://docs.sentry.io/platforms/godot/logs.md) with searchable attributes that connect to your traces, plus optional capture of Godot log output like `print()` statements

* [Enrich events](https://docs.sentry.io/platforms/godot/enriching-events.md) with tags, breadcrumbs, contexts, and attachments

* Information about user configuration like GPU, CPU, platform and such

* [Filter and customize events](https://docs.sentry.io/platforms/godot/data-management/sensitive-data.md#scrubbing-data) in `before_send` callback

* [Log-file attachments](https://docs.sentry.io/platforms/godot/configuration/options.md#attach_log) for events

* [Scene tree data attachments](https://docs.sentry.io/platforms/godot/enriching-events/view-hierarchy.md) for events

* [Screenshot attachments](https://docs.sentry.io/platforms/godot/enriching-events/screenshots.md) for events (experimental)

* [Release Health](https://docs.sentry.io/platforms/godot/configuration/releases.md) to keep track of crash-free users and sessions

* [Event throttling](https://docs.sentry.io/platforms/godot/configuration/options.md#godot_logger.limits) to handle spammy errors

On this page, we get you up and running with Sentry's SDK.

Don't already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

## [Install](https://docs.sentry.io/platforms/godot.md#install)

Sentry captures data through our addon for Godot Engine which you can install in your project.

Download the latest stable version `2.4.0` from [GitHub Releases](https://github.com/getsentry/sentry-godot/releases/). Extract the `addons/sentry` folder from the archive into your project.

Ensure that the addon is placed in the `addons/sentry` folder, preserving the exact casing.

A separate **demo project** archive is also available on the releases page. It contains a ready-to-run Godot project with examples of common features like error capturing, breadcrumbs, and user feedback. To use it, enter your DSN in **Project Settings > Sentry > Options**.

## [Configure](https://docs.sentry.io/platforms/godot.md#configure)

**Error Monitoring** starts working as soon as you set your DSN: the SDK automatically captures crashes and Godot runtime errors, such as script and shader errors. **Logs** and **Application Metrics** are enabled by default in SDK 2.0.0 and later, and you'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/godot.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/godot.md#send-application-metrics-). This guide also enables **Tracing**, which requires SDK 2.2.0 or later. To collect **User Feedback** from players, add the SDK's [feedback form or use the feedback API](https://docs.sentry.io/platforms/godot/user-feedback.md).

### [Initialize the SDK](https://docs.sentry.io/platforms/godot.md#initialize-the-sdk)

The minimum configuration required is the [DSN](https://docs.sentry.io/concepts/key-terms/dsn-explainer.md) to your project.

To access the project settings in Godot Engine, navigate to **Project > Project Settings...**, then scroll down the sections list on the left until you find the **Sentry** section. Enter your DSN in **Sentry > Options > DSN**.

Your configuration is saved in the `project.godot` file along with other project settings. With **Auto Init** turned on (the default), the SDK initializes automatically when your game starts, before any scenes load or scripts run.

To configure the SDK in code instead, for example to define a [`before_send`](https://docs.sentry.io/platforms/godot/configuration/options.md#before_send) callback, turn off **Auto Init** in **Project Settings > Sentry > Options** and call `init()` from a script that extends `SceneTree`. Then enter the script's class name in **Project Settings > Application > Run > Main Loop Type**. A single `init()` call from either GDScript or C# initializes the SDK for both languages. See [Programmatic Configuration](https://docs.sentry.io/platforms/godot/configuration/options.md#programmatic-configuration) for details.

The snippet also turns on:

* Tracing: via [`traces_sample_rate`](https://docs.sentry.io/platforms/godot/configuration/options.md#traces_sample_rate), or **Sentry > Options > Tracing > Traces Sample Rate** in Project Settings (turn on **Advanced Settings** to see it). Add spans around operations like level loads with [instrumentation](https://docs.sentry.io/platforms/godot/tracing/instrumentation.md). For C#, use the [Sentry .NET tracing API](https://docs.sentry.io/platforms/dotnet/tracing.md).
* Scene tree attachments: via [`attach_scene_tree`](https://docs.sentry.io/platforms/godot/configuration/options.md#attach_scene_tree), or **Sentry > Options > Attach Scene Tree** in Project Settings. See [Scene Tree](https://docs.sentry.io/platforms/godot/enriching-events/view-hierarchy.md) for details.

Don't need a feature? Remove its options.

**\[GDScript] ProjectMainLoop.gd**

```gdscript
class_name ProjectMainLoop
extends SceneTree

func _initialize() -> void:
	SentrySDK.init(func(options: SentryOptions) -> void:
		options.dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
		# Enables Tracing.
		# Set to 1.0 to capture 100% of traces.
		# We recommend reducing this value in production.
		options.traces_sample_rate = 1.0
		# Attaches scene tree data to events.
		options.attach_scene_tree = true
	)
```

**\[C#] ProjectMainLoop.cs**

```csharp
using Godot;
using Sentry;
using Sentry.Godot;

[GlobalClass]
public partial class ProjectMainLoop : SceneTree
{
    public override void _Initialize()
    {
        SentrySdk.Init(options =>
        {
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
            // Enables Tracing.
            // Set to 1.0 to capture 100% of traces.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;
            // Attaches scene tree data to events.
            options.AttachSceneTree = true;
        });
    }
}
```

### [Get Readable Stack Traces](https://docs.sentry.io/platforms/godot.md#get-readable-stack-traces)

The official Godot Engine builds only provide export templates without debug information. To get function names, file paths, and line numbers for native crashes, export your game with [export templates that contain debug symbols](https://docs.sentry.io/platforms/godot/configuration/stack-traces.md) and [upload the debug symbols](https://docs.sentry.io/platforms/godot/configuration/stack-traces.md#uploading-debug-symbols) to Sentry.

To see GDScript source code around stack trace frames in exported games, set up [Source Context](https://docs.sentry.io/platforms/godot/configuration/source-context.md).

### [Export for Android](https://docs.sentry.io/platforms/godot.md#export-for-android)

Exporting for Android with the Sentry SDK requires Godot's Gradle build. Install the Android build template with **Project > Install Android Build Template...**, then turn on **Use Gradle Build** in your Android export preset. See [Exporting for Android](https://docs.sentry.io/platforms/godot/configuration/android.md) for the full setup.

### [Capture Errors From C# Code](https://docs.sentry.io/platforms/godot.md#capture-errors-from-c-code)

C# support requires SDK 2.0.0 or later and the .NET build of Godot Engine 4.5 or later. The addon ships the .NET libraries and adds them to your project's `.csproj` file when you open the project in the editor. Build your project to restore the NuGet package. See [C#/.NET Support](https://docs.sentry.io/platforms/godot/dotnet.md) for details.

## [Send Logs](https://docs.sentry.io/platforms/godot.md#send-logs)

Use `SentrySDK.logger` to send logs at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later. Logs are generally available in SDK 1.2.0 and later and enabled by default starting with SDK 2.0.0.

To also capture Godot's own log output, such as engine errors and `print()` statements, set [`godot_logger.log_mask`](https://docs.sentry.io/platforms/godot/configuration/options.md#godot_logger.log_mask). It's empty by default.

See [Set Up Logs](https://docs.sentry.io/platforms/godot/logs.md) for all available logging methods and configuration options.

**GDScript**

```gdscript
SentrySDK.logger.info("Level loaded successfully")

SentrySDK.logger.warn("Item configuration not found")

SentrySDK.logger.debug("Spawning %s with %d units", ["enemies", 5], {
	"current_scene": get_tree().current_scene.scene_file_path,
	"wave_id": "main_wave_3"
})
```

**C#**

```csharp
SentrySdk.Logger.LogInfo("Level loaded successfully");

SentrySdk.Logger.LogWarning("Item configuration not found");

SentrySdk.Logger.LogDebug(
    log =>
    {
        log.SetAttribute("current_scene", GetTree().CurrentScene.SceneFilePath);
        log.SetAttribute("wave_id", "main_wave_3");
    },
    "Spawning {0} with {1} units", "enemies", 5);
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/godot.md#send-application-metrics-)

Use `SentrySDK.metrics` to send counters, gauges, and distributions from your game to Sentry. You can pass any attributes you want and search or filter by them later. Metrics require SDK 2.0.0 or later, where they're enabled by default.

See [Set Up Metrics](https://docs.sentry.io/platforms/godot/metrics.md) for all available metric types and configuration options.

**GDScript**

```gdscript
SentrySDK.metrics.count("match_started")

SentrySDK.metrics.gauge("players_online", lobby.get_player_count())

SentrySDK.metrics.distribution("level_load_time", load_time, SentryUnit.millisecond, {
	"scene": get_tree().current_scene.name
})
```

**C#**

```csharp
SentrySdk.Metrics.EmitCounter("match_started", 1);

SentrySdk.Metrics.EmitGauge("players_online", lobby.GetPlayerCount());

SentrySdk.Metrics.EmitDistribution("level_load_time", loadTime, MeasurementUnit.Duration.Millisecond, new Dictionary<string, object>
{
    ["scene"] = GetTree().CurrentScene.Name.ToString(),
});
```

## [Verify Your Setup](https://docs.sentry.io/platforms/godot.md#verify-your-setup)

Add a `Node` to your test scene and attach a script with the following content, then run the scene. The script captures a message, so you can confirm that Sentry receives events from your game.

**GDScript**

```gdscript
extends Node

func _ready():
	SentrySDK.add_breadcrumb(SentryBreadcrumb.create("Just about to welcome the World."))
	SentrySDK.capture_message("Hello, World!")
```

**C#**

```csharp
using Godot;

public partial class SentryTest : Node
{
    public override void _Ready()
    {
        SentrySdk.AddBreadcrumb("Just about to welcome the World.");
        SentrySdk.CaptureMessage("Hello, World!");
    }
}
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/godot.md#view-captured-data-in-sentry)

To view and resolve the recorded message, log into [sentry.io](https://sentry.io) and select your project. Select **Issues** in the sidebar, then select the message's title to open a page where you can see detailed information and mark it as resolved.

## [Next Steps](https://docs.sentry.io/platforms/godot.md#next-steps)

At this point, you should have integrated Sentry into your Godot Engine game. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup.
* Learn how to [manually capture errors and messages](https://docs.sentry.io/platforms/godot/usage.md).
* Add tags, breadcrumbs, context, and attachments, such as [screenshots](https://docs.sentry.io/platforms/godot/enriching-events/screenshots.md), to [enrich your events](https://docs.sentry.io/platforms/godot/enriching-events.md).
* Track crash-free users and sessions with [Releases & Health](https://docs.sentry.io/platforms/godot/configuration/releases.md).

## Topics

- [Configuration](https://docs.sentry.io/platforms/godot/configuration.md)
- [Usage](https://docs.sentry.io/platforms/godot/usage.md)
- [C#/.NET](https://docs.sentry.io/platforms/godot/dotnet.md)
- [Enriching Events](https://docs.sentry.io/platforms/godot/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/godot/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/godot/tracing.md)
- [Logs](https://docs.sentry.io/platforms/godot/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/godot/metrics.md)
- [User Feedback](https://docs.sentry.io/platforms/godot/user-feedback.md)
- [Migration Guide](https://docs.sentry.io/platforms/godot/migration.md)

