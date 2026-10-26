---
title: "WinUI"
source: https://docs.sentry.io/platforms/dotnet/guides/winui.md
path: platforms/dotnet/guides/winui
---

---
title: "WinUI"
description: "Learn about using Sentry's .NET SDK with the Windows UI Library"
url: https://docs.sentry.io/platforms/dotnet/guides/winui/
---

# Sentry for WinUI

Sentry's .NET SDK works with Windows UI Library applications through the [Sentry NuGet package](https://www.nuget.org/packages/Sentry).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/winui.md#install)

Install the **NuGet** package to add the Sentry dependency:

```shell
dotnet add package Sentry -v 6.12.1
```

*Other available variations of the above snippet: Package Manager, Paket CLI*

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/winui.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/winui.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/winui.md#send-application-metrics-).

This guide also enables **Tracing**.

If you don't have [Trimming](https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/trimming-options?pivots=dotnet-8-0) enabled when publishing your application then all you need to do is [initialize the SDK with `SentrySdk.Init`](https://docs.sentry.io/platforms/dotnet.md) in the constructor of your application class (usually `App.xaml.cs`). Sentry's integration for WinUI will automatically capture any unhandled exceptions in your application and send these to Sentry.

Do not initialize the SDK in the `OnLaunched` event of the application or the `Hub` will not be initialized correctly.

In addition to capturing errors, you can monitor interactions between multiple services or applications by [enabling tracing](https://docs.sentry.io/concepts/key-terms/tracing.md).

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/winui/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```csharp
using Sentry.Protocol;

sealed partial class App : Application
{
    public App()
    {
        // Initialize Sentry in the App constructor before any other code, to ensure you capture all possible exceptions.
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

            // Enable Global Mode since this is a client app.
            options.IsGlobalModeEnabled = true;

            // TODO:Any other Sentry options you need go here.
        });

        // Initialize the app component, and hook the Suspending event.
        this.InitializeComponent();

        // Add any other code you may need last.
    }
}
```

### [Configure With Trimming](https://docs.sentry.io/platforms/dotnet/guides/winui.md#configure-with-trimming)

If you have [Trimming](https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/trimming-options?pivots=dotnet-8-0) enabled when publishing your application then, in addition to [initializing the SDK with `SentrySdk.Init`](https://docs.sentry.io/platforms/dotnet.md), you must also configure an UnhandledException handler in the constructor of your application class (usually `App.xaml.cs`).

Do not initialize the SDK in the `OnLaunched` event of the application or the `Hub` will not be initialized correctly.

```csharp
// Add these to your existing using statements.
using Sentry.Protocol;
using UnhandledExceptionEventArgs = Microsoft.UI.Xaml.UnhandledExceptionEventArgs;

sealed partial class App : Application
{
    public App()
    {
        // Initialize Sentry in the App constructor before any other code, to ensure you capture all possible exceptions.
        SentrySdk.Init(o =>
        {
            // Tells which project in Sentry to send events to:
            o.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";

            // When configuring for the first time, to see what the SDK is doing:
            o.Debug = true;

            // Adds request URL and headers, IP and name for users, etc.
            o.SendDefaultPii = true;

            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            o.TracesSampleRate = 1.0;

            // Enable Global Mode since this is a client app.
            o.IsGlobalModeEnabled = true;

            // Disable Sentry's built in UnhandledException handler as this won't work with AOT compilation
            o.DisableWinUiUnhandledExceptionIntegration();

            // TODO:Any other Sentry options you need go here.
        });

        // Hook up the WinUI UnhandledException event before initializing the app component.
        this.UnhandledException += OnUnhandledException;

        // Initialize the app component, and hook the Suspending event.
        this.InitializeComponent();

        // Add any other code you may need last.
    }

    // Add this OnUnhandledException handler.

    // Use this attribute to ensure all types of exceptions are handled.
    [SecurityCritical]
    private void OnUnhandledException(object sender, UnhandledExceptionEventArgs e)
    {
        // Get a reference to the exception, because the Exception property is cleared when accessed.
        var exception = e.Exception;
        if (exception != null)
        {
            // Tell Sentry this was an unhandled exception
            exception.Data[Mechanism.HandledKey] = false;
            exception.Data[Mechanism.MechanismKey] = "Application.UnhandledException";

            // Capture the exception
            SentrySdk.CaptureException(exception);

            // Flush the event immediately
            SentrySdk.FlushAsync(TimeSpan.FromSeconds(2)).GetAwaiter().GetResult();
        }
    }
}
```

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/winui.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/winui/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/winui.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/winui/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/winui.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/winui.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/winui.md#next-steps)

At this point, you should have integrated Sentry into your WinUI application. Here's what to explore next:

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
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/winui/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/winui/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/winui/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/winui/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/winui/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/winui/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/winui/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/winui/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/winui/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/winui/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/winui/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/winui/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/winui/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/winui/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/winui/legacy-sdk.md)

