---
title: ".NET for Android"
source: https://docs.sentry.io/platforms/dotnet/guides/android.md
path: platforms/dotnet/guides/android
---

---
title: ".NET for Android"
description: "Learn about Sentry's .NET integration with .NET for Android"
url: https://docs.sentry.io/platforms/dotnet/guides/android/
---

# Sentry for .NET for Android

Sentry supports [.NET for Android](https://learn.microsoft.com/dotnet/android/getting-started/installation/) directly from the [Sentry NuGet package](https://www.nuget.org/packages/Sentry).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/android.md#install)

Add the Sentry dependency to your .NET for Android application:

```shell
dotnet add package Sentry -v 6.12.1
```

*Other available variations of the above snippet: Package Manager*

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/android.md#configure)

**Error Monitoring** starts working as soon as you call `SentrySdk.Init()`. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/android.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/android.md#send-application-metrics-).

This guide also enables **Tracing** and **Session Replay** (experimental).

On .NET for Android, you also get:

* All the features of our main [.NET SDK](https://docs.sentry.io/platforms/dotnet.md), for your managed code

* LogCat logs attached to events

* Java crash reporting for Android, leveraging our [Android SDK](https://docs.sentry.io/platforms/android.md) including:

  * [Capture Application Not Responding (ANR) errors](https://docs.sentry.io/platforms/android/configuration/app-not-respond.md) when the app is unresponsive
  * Automatically [attach screenshots to Java exceptions](https://docs.sentry.io/platforms/android/enriching-events/screenshots.md)
  * Automatic breadcrumbs for Activity lifecycle, App lifecycle, System and Network events and User Interactions
  * Automatic [Activity lifecycle tracing](https://docs.sentry.io/platforms/android/tracing/instrumentation/automatic-instrumentation.md#activity-instrumentation) and [User Interaction tracing](https://docs.sentry.io/platforms/android/tracing/instrumentation/automatic-instrumentation.md#user-interaction-instrumentation)
  * Device Root checking

* Native crash reporting for Android, leveraging our [Android NDK](https://docs.sentry.io/platforms/android/configuration/using-ndk.md)

* Automatic session tracking and [release health](https://docs.sentry.io/product/releases.md)

In your `MainActivity.cs` file, call `SentrySdk.Init` in the `OnCreate` event and include any options you would like to set. The `Dsn` is the only required parameter.

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/android/configuration/options.md#TracesSampleRate)
* Session Replay: via [`Native.ExperimentalOptions.SessionReplay`](https://docs.sentry.io/platforms/dotnet/guides/android/configuration/native-options.md#session-replay)

Don't need a feature? Remove its options from the snippet.

```csharp
[Activity(Label = "@string/app_name", MainLauncher = true)]
public class MainActivity : Activity
{
    protected override void OnCreate(Bundle? savedInstanceState)
    {
        SentrySdk.Init(options =>
        {
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
            options.SendDefaultPii = true; // adds the user's IP address automatically
            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;
#if DEBUG
            // Log debug information about the Sentry SDK
            options.Debug = true;
#endif

            // Android specific .NET features are under the Android properties:
            options.Android.LogCatIntegration = LogCatIntegrationType.Errors; // Get logcat logs for both handled and unhandled errors; default is unhandled only
            options.Android.LogCatMaxLines = 1000; // Defaults to 1000

            // Native Android SDK options are available via options.Native
            options.Native.AnrEnabled = true;

            // If your app doesn't have sensitive data, you can attach screenshots automatically when a Java/native
            // error is captured.
            // https://docs.sentry.io/platforms/android/configuration/options/#attachScreenshot
            options.Native.AttachScreenshot = true;

            // Session Replay is currently available via the ExperimentalOptions
            options.Native.ExperimentalOptions.SessionReplay.OnErrorSampleRate = 1.0;
            options.Native.ExperimentalOptions.SessionReplay.SessionSampleRate = 1.0;

            options.SetBeforeSend(evt =>
            {
                if (evt.Exception?.Message.Contains("Something you don't care want logged?") ?? false)
                {
                    return null; // return null to filter out event
                }
                // or add additional data
                evt.SetTag("dotnet-Android-Native-Before", "Hello World");
                return evt;
            });
        });

        base.OnCreate(savedInstanceState);
    }
}
```

For a full list of native options, see [Android Native Options](https://docs.sentry.io/platforms/dotnet/guides/android/configuration/native-options.md).

### [Options](https://docs.sentry.io/platforms/dotnet/guides/android.md#options)

The .NET for Android integration is part of [Sentry](https://docs.sentry.io/platforms/dotnet.md). Please refer to the documentation for that package for information about platform agnostic options.

Android-specific options are described below. For configuration of the embedded Sentry Android SDK, see [Android Native Options](https://docs.sentry.io/platforms/dotnet/guides/android/configuration/native-options.md).

#### [LogCatIntegration](https://docs.sentry.io/platforms/dotnet/guides/android.md#logcatintegration)

Can be set to control whether when LogCat logs are attached to events. It can be set to one of the following values:

* `None`: The LogCat integration is disabled.
* `Unhandled`: LogCat logs are attached to events only when the event is unhandled.
* `Errors`: LogCat logs are attached to events with an exception.
* `All`: LogCat logs are attached to all events.

The default is `LogCatIntegrationType.None`

Use caution when enabling `LogCatIntegrationType.All`, as this may result in a lot of data being sent to Sentry and performance issues if the SDK generates a lot of events.

#### [LogCatMaxLines](https://docs.sentry.io/platforms/dotnet/guides/android.md#logcatmaxlines)

The maximum number of lines to read from LogCat logs.

The default value is 1000.

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/android.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/android/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/android.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/android/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/android.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

```csharp
try
{
    throw null;
}
catch (Exception ex)
{
    SentrySdk.CaptureException(ex);
}
```

*Other available variations of the above snippet: fsharp*

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/android.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/android.md#next-steps)

At this point, you should have integrated Sentry into your .NET for Android application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)
* Configure the embedded Android SDK with [Android Native Options](https://docs.sentry.io/platforms/dotnet/guides/android/configuration/native-options.md)

## Other .NET Frameworks

- [.NET for iOS, macOS, and Mac Catalyst](https://docs.sentry.io/platforms/dotnet/guides/apple.md)
- [ASP.NET](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md)
- [ASP.NET Core](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md)
- [AWS Lambda](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md)
- [Azure Functions](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md)
- [Blazor Interactive SSR](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md)
- [Blazor WebAssembly](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md)
- [Entity Framework](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md)
- [Google Cloud Functions](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md)
- [log4net](https://docs.sentry.io/platforms/dotnet/guides/log4net.md)
- [MAUI](https://docs.sentry.io/platforms/dotnet/guides/maui.md)
- [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md)
- [NLog](https://docs.sentry.io/platforms/dotnet/guides/nlog.md)
- [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/android/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/android/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/android/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/android/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/android/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/android/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/android/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/android/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/android/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/android/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/android/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/android/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/android/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/android/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/android/legacy-sdk.md)

