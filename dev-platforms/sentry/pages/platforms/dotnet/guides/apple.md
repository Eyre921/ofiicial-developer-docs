---
title: ".NET for iOS, macOS, and Mac Catalyst"
source: https://docs.sentry.io/platforms/dotnet/guides/apple.md
path: platforms/dotnet/guides/apple
---

---
title: ".NET for iOS, macOS, and Mac Catalyst"
description: "Learn about Sentry's .NET integration with .NET for iOS, macOS, and Mac Catalyst"
url: https://docs.sentry.io/platforms/dotnet/guides/apple/
---

# Sentry for .NET for iOS, macOS, and Mac Catalyst

Sentry supports [.NET for iOS, macOS, and Mac Catalyst](https://learn.microsoft.com/dotnet/ios/) directly from the [Sentry NuGet package](https://www.nuget.org/packages/Sentry).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/apple.md#install)

Add the Sentry dependency to your .NET for iOS, macOS, and/or Mac Catalyst application:

```shell
dotnet add package Sentry -v 6.12.1
```

*Other available variations of the above snippet: Package Manager*

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/apple.md#configure)

**Error Monitoring** starts working as soon as you call `SentrySdk.Init()`. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/apple.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/apple.md#send-application-metrics-).

This guide also enables **Tracing**, **Profiling**, and **Session Replay** (experimental).

On .NET for iOS, macOS, and Mac Catalyst, you also get:

* All the features of our main [.NET SDK](https://docs.sentry.io/platforms/dotnet.md), for your managed code

* Native crash reporting for Apple platforms, leveraging our [Cocoa SDK](https://docs.sentry.io/platforms/apple.md) including:

  * Automatically [attach screenshots to Native exceptions](https://docs.sentry.io/platforms/apple/guides/ios/configuration/options.md#attachScreenshot)
  * Detect [App Hangs](https://docs.sentry.io/platforms/apple/configuration/app-hangs.md)
  * [Automatic performance tracing](https://docs.sentry.io/platforms/apple/tracing.md)
  * [Automatic breadcrumbs](https://docs.sentry.io/platforms/apple/enriching-events/breadcrumbs.md#automatic-breadcrumbs)
  * [Swizzling](https://docs.sentry.io/platforms/apple/configuration/swizzling.md)

* Automatic session tracking and [release health](https://docs.sentry.io/product/releases.md)

In your `AppDelegate.cs` file, call `SentrySdk.Init` in the `FinishedLaunching` event and include any options you would like to set. The `Dsn` is the only required parameter.

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/apple/configuration/options.md#TracesSampleRate)
* Profiling: via [`ProfilesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/apple/profiling.md). On iOS and Mac Catalyst, the SDK adds the native profiling integration automatically, so you don't need the `Sentry.Profiling` package.
* Session Replay: via [`Native.ExperimentalOptions.SessionReplay`](https://docs.sentry.io/platforms/dotnet/guides/apple/configuration/native-options.md#session-replay)

Don't need a feature? Remove its options from the snippet.

```csharp
[Register("AppDelegate")]
public class AppDelegate : UIApplicationDelegate
{
    public override bool FinishedLaunching(UIApplication application, NSDictionary launchOptions)
    {
        // Init the Sentry SDK
        SentrySdk.Init(options =>
        {
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
            options.SendDefaultPii = true; // adds the user's IP address automatically
            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;
            // Enables Profiling.
            // Set to 1.0 to profile 100% of captured transactions.
            options.ProfilesSampleRate = 1.0;
#if DEBUG
            // Log debug information about the Sentry SDK
            options.Debug = true;
#endif

            // Native Apple SDK options are available via options.Native
            options.Native.EnableAppHangTracking = true;

            // If your app doesn't have sensitive data, you can get screenshots on error events automatically
            // https://docs.sentry.io/platforms/apple/guides/ios/configuration/options/#attachScreenshot
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
                evt.SetTag("dotnet-iOS-Native-Before", "Hello World");
                return evt;
            });

            options.OnCrashedLastRun = e =>
            {
                Console.WriteLine(e);
            };
        });

        return true;
    }
}
```

For a full list of native options, see [Apple Native Options](https://docs.sentry.io/platforms/dotnet/guides/apple/configuration/native-options.md).

### [Options](https://docs.sentry.io/platforms/dotnet/guides/apple.md#options)

The .NET for iOS, macOS, and Mac Catalyst integration is part of [Sentry](https://docs.sentry.io/platforms/dotnet.md). Please refer to the documentation for that package for information about platform agnostic options.

For configuration of the embedded Sentry Cocoa SDK, see [Apple Native Options](https://docs.sentry.io/platforms/dotnet/guides/apple/configuration/native-options.md).

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/apple.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/apple/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/apple.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/apple/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/apple.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/apple.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/apple.md#next-steps)

At this point, you should have integrated Sentry into your .NET for iOS, macOS, or Mac Catalyst application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)
* Configure the embedded Cocoa SDK with [Apple Native Options](https://docs.sentry.io/platforms/dotnet/guides/apple/configuration/native-options.md)

## Other .NET Frameworks

- [.NET for Android](https://docs.sentry.io/platforms/dotnet/guides/android.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/apple/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/apple/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/apple/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/apple/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/apple/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/apple/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/apple/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/apple/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/apple/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/apple/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/apple/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/apple/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/apple/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/apple/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/apple/legacy-sdk.md)

