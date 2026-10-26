---
title: "WPF"
source: https://docs.sentry.io/platforms/dotnet/guides/wpf.md
path: platforms/dotnet/guides/wpf
---

---
title: "WPF"
description: "Learn more about how Sentry's .NET SDK works with Windows Presentation Foundation (WPF) applications."
url: https://docs.sentry.io/platforms/dotnet/guides/wpf/
---

# Sentry for WPF

Sentry's .NET SDK works with Windows Presentation Foundation applications through the [Sentry NuGet package](https://www.nuget.org/packages/Sentry). It works with WPF apps running on .NET Framework 4.6.2, .NET Core 3.0 or higher.

## [Install](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#install)

Install the **NuGet** package to add the Sentry dependency:

```shell
dotnet add package Sentry -v 6.12.1
```

*Other available variations of the above snippet: Package Manager, Paket CLI*

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#send-application-metrics-).

This guide also enables **Tracing**.

In addition to [initializing the SDK with `SentrySdk.Init`](https://docs.sentry.io/platforms/dotnet.md), you must configure the WPF specific error handler.

The SDK automatically handles `AppDomain.UnhandledException`. On WPF, for production apps (when no debugger is attached), WPF catches exception to show the dialog to the user. You can also configure your app to capture those exceptions before the dialog shows up:

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/wpf/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```csharp
using System.Windows;

public partial class App : Application
{
    public App()
    {
        SentrySdk.Init(options =>
        {
            // Tells which project in Sentry to send events to:
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";

            // When configuring for the first time, to see what the SDK is doing:
            options.Debug = true;

            // Adds request URL and headers, IP and name for users, etc.
            options.SendDefaultPii = true;
            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;
            // Enable Global Mode since this is a client app
            options.IsGlobalModeEnabled = true;

            //TODO: any other options you need go here
        });
        DispatcherUnhandledException += App_DispatcherUnhandledException;
    }

    void App_DispatcherUnhandledException(object sender, DispatcherUnhandledExceptionEventArgs e)
    {
        SentrySdk.CaptureException(e.Exception);

        // If you want to avoid the application from crashing:
        e.Handled = true;
    }
}
```

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/wpf/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/wpf/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/wpf.md#next-steps)

At this point, you should have integrated Sentry into your WPF application. Here's what to explore next:

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
- [MAUI](https://docs.sentry.io/platforms/dotnet/guides/maui.md)
- [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md)
- [NLog](https://docs.sentry.io/platforms/dotnet/guides/nlog.md)
- [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/wpf/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/wpf/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/wpf/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/wpf/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/wpf/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/wpf/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/wpf/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/wpf/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/wpf/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/wpf/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/wpf/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/wpf/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/wpf/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/wpf/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/wpf/legacy-sdk.md)

