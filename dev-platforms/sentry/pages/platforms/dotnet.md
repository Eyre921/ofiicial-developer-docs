---
title: ".NET"
source: https://docs.sentry.io/platforms/dotnet.md
path: platforms/dotnet
---

---
title: ".NET"
description: "Learn how to set up and run Sentry's .NET SDK, which will automatically report errors and exceptions in your application."
url: https://docs.sentry.io/platforms/dotnet/
---

# Sentry for .NET

If you don't already have an account and Sentry project established, head over to [sentry.io](https://sentry.io/signup/), then return to this page.

You can use these instructions to run Sentry in an app running on:

* Windows
* macOS
* Linux
* Android
* iOS

If you're using a framework, such as ASP.NET Core or MAUI, please select the framework on the drop down on the top left.

## [Install](https://docs.sentry.io/platforms/dotnet.md#install)

Install the `Sentry` NuGet package to add the SDK:

```shell
dotnet add package Sentry -v 6.12.1
```

*Other available variations of the above snippet: Package Manager*

## [Configure](https://docs.sentry.io/platforms/dotnet.md#configure)

**Error Monitoring** starts working as soon as you call `SentrySdk.Init()`. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet.md#send-application-metrics-).

This guide also enables **Tracing**. **Profiling** is in Alpha and needs .NET 8 or later, so it's a separate step: see [Enable Profiling on .NET 8 and Later](https://docs.sentry.io/platforms/dotnet.md#enable-profiling-on-net-8-and-later).

To capture all errors, even the one during the startup of your application, you should initialize the Sentry .NET SDK as soon as possible.

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```csharp
SentrySdk.Init(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    options.Debug = true;
    // Adds request URL and headers, IP and name for users, etc.
    options.SendDefaultPii = true;
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    options.TracesSampleRate = 1.0f;
});
```

### [Enable Profiling on .NET 8 and Later](https://docs.sentry.io/platforms/dotnet.md#enable-profiling-on-net-8-and-later)

Profiling for .NET is in Alpha and needs .NET 8 or later. On .NET Framework, `Sentry.Profiling` installs without a warning, but `AddProfilingIntegration()` doesn't compile.

To profile your app, install the `Sentry.Profiling` package:

```shell
dotnet add package Sentry.Profiling -v 6.12.1
```

*Other available variations of the above snippet: Package Manager*

Then add these options to `SentrySdk.Init()`:

```csharp
// Enables Profiling for 100% of sampled transactions.
options.ProfilesSampleRate = 1.0f;
options.AddProfilingIntegration();
```

See [Set Up Profiling](https://docs.sentry.io/platforms/dotnet/profiling.md) for supported platforms and options.

## [Send Logs](https://docs.sentry.io/platforms/dotnet.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Next Steps](https://docs.sentry.io/platforms/dotnet.md#next-steps)

At this point, you should have integrated Sentry into your .NET application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)

## Frameworks

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
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/legacy-sdk.md)

