---
title: "MAUI"
source: https://docs.sentry.io/platforms/dotnet/guides/maui.md
path: platforms/dotnet/guides/maui
---

---
title: "MAUI"
description: "Learn about Sentry's .NET integration with .NET Multi-platform App UI (MAUI)."
url: https://docs.sentry.io/platforms/dotnet/guides/maui/
---

# Sentry for MAUI

Sentry has an integration for the [.NET Multi-platform App UI (MAUI)](https://dotnet.microsoft.com/apps/maui) through the [Sentry.Maui NuGet package](https://www.nuget.org/packages/Sentry.Maui).

**Overview of the features**

* Easy MAUI integration by calling `UseSentry` on your `MauiAppBuilder`
* All the features of our main [.NET SDK](https://docs.sentry.io/platforms/dotnet.md), for your managed code
* Native crash reporting for Android, leveraging our [Android SDK](https://docs.sentry.io/platforms/android.md)
* Native crash reporting for iOS and Mac Catalyst, leveraging our [Cocoa SDK for iOS](https://docs.sentry.io/platforms/apple/guides/ios.md)
* Managed crash reporting (unhandled exceptions), on all MAUI platforms (iOS, Android, Windows, Mac Catalyst, and Tizen)
* Line numbers for your .NET stack traces when PDBs are uploaded to Sentry
* Automatic breadcrumbs for MAUI app lifecycle and UI events
* Detailed device and runtime information passed on every event
* Automatic session tracking enabled, to support [release health](https://docs.sentry.io/product/releases.md)

## [Install](https://docs.sentry.io/platforms/dotnet/guides/maui.md#install)

Add the Sentry dependency to your .NET MAUI application:

```shell
dotnet add package Sentry.Maui -v 6.12.1
```

*Other available variations of the above snippet: Package Manager*

This package extends [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md). This means that besides the MAUI related features, through this package you'll also get access to all the framework's logging integration and also the features available in the main [Sentry](https://docs.sentry.io/platforms/dotnet.md) SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/maui.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `Microsoft.Extensions.Logging` need `EnableLogs = true`, and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/maui.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/maui.md#send-application-metrics-).

This guide also enables **Tracing**.

In your `MauiProgram.cs` file, call `UseSentry` on your `MauiAppBuilder`, and include any options you would like to set. The `Dsn` is the only required parameter.

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/maui/configuration/options.md#TracesSampleRate)
* Logs: via [`EnableLogs`](https://docs.sentry.io/platforms/dotnet/guides/maui/logs.md#enablelogs)

Don't need a feature? Remove its options from the snippet.

```csharp
public static MauiApp CreateMauiApp()
{
    var builder = MauiApp.CreateBuilder();
    builder
        .UseMauiApp<App>()

        // Add this section anywhere on the builder:
        .UseSentry(options =>
        {
            // The DSN is the only required setting.
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
            options.EnableLogs = true;

            // Use debug mode if you want to see what the SDK is doing.
            // Debug messages are written to stdout with Console.Writeline,
            // and are viewable in your IDE's debug console or with 'adb logcat', etc.
            // This option is not recommended when deploying your application.
            options.Debug = true;

            // Adds request URL and headers, IP and name for users, etc.
            options.SendDefaultPii = true;
            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;

            // If your app doesn't have sensitive data, you can get screenshots on error events automatically
            options.AttachScreenshot = true;

            // Other Sentry options can be set here.
        })

        // ... the remainder of your MAUI app setup

    return builder.Build();
}
```

### [Options](https://docs.sentry.io/platforms/dotnet/guides/maui.md#options)

As previously mentioned, this package is a wrapper around [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) and [Sentry](https://docs.sentry.io/platforms/dotnet.md). Please refer to the documentation of these packages to get the options that are defined at those levels.

When targeting Android or Apple platforms, the embedded native SDKs can be configured via `options.Native`. See the platform-specific native options reference:

* [Android Native Options](https://docs.sentry.io/platforms/dotnet/guides/android/configuration/native-options.md)
* [Apple Native Options](https://docs.sentry.io/platforms/dotnet/guides/apple/configuration/native-options.md)

Below, the options that are specific to `Sentry.Maui` will be described.

#### [IncludeTextInBreadcrumbs](https://docs.sentry.io/platforms/dotnet/guides/maui.md#includetextinbreadcrumbs)

This option controls whether elements that implement the `IText` interface (such as `Button`, `Label`, `Entry`, and others) will have their text included on breadcrumbs. This option is disabled by default.

Use caution when enabling, as such values may contain personally identifiable information (PII).

#### [IncludeTitleInBreadcrumbs](https://docs.sentry.io/platforms/dotnet/guides/maui.md#includetitleinbreadcrumbs)

This option controls whether elements that implement the `ITitledElement` interface (such as `Window`, `Page`, and others) will have their titles included on breadcrumbs. This option is disabled by default.

Use caution when enabling, as such values may contain personally identifiable information (PII).

#### [IncludeBackgroundingStateInBreadcrumbs](https://docs.sentry.io/platforms/dotnet/guides/maui.md#includebackgroundingstateinbreadcrumbs)

Controls whether the breadcrumb sent for the `Window.Backgrounding` event will include state data from `BackgroundingEventArgs.State`. This option is disabled by default.

Use caution when enabling, as such values may contain personally identifiable information (PII).

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/maui.md#send-logs)

Use `Microsoft.Extensions.Logging` to send structured logs from your application. Set `EnableLogs = true` in your Sentry initialization.

See [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) for setup details.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/maui/logs.md) for all available logging methods and formatting options.

```csharp
using Microsoft.Extensions.Logging;

public sealed class OrderService
{
    private readonly ILogger<OrderService> _logger;

    public OrderService(ILogger<OrderService> logger) => _logger = logger;

    public void Process()
    {
        _logger.LogInformation("Order processed {OrderId}", "order-123");
        _logger.LogWarning("Rate limit reached for {Endpoint}", "/api/orders");
    }
}
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/maui.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/maui/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/maui.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/maui.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/maui.md#next-steps)

At this point, you should have integrated Sentry into your .NET MAUI application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)

## Other .NET Frameworks

- [.NET for Android](https://docs.sentry.io/platforms/dotnet/guides/android.md)
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
- [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md)
- [NLog](https://docs.sentry.io/platforms/dotnet/guides/nlog.md)
- [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/maui/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/maui/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/maui/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/maui/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/maui/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/maui/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/maui/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/maui/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/maui/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/maui/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/maui/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/maui/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/maui/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/maui/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/maui/legacy-sdk.md)

