---
title: "Blazor WebAssembly"
source: https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md
path: platforms/dotnet/guides/blazor-webassembly
---

---
title: "Blazor WebAssembly"
description: "Learn about Sentry's .NET integration with Blazor WebAssembly."
url: https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/
---

# Sentry for Blazor WebAssembly

Sentry provides an integration with Blazor WebAssembly through the [Sentry.AspNetCore.Blazor.WebAssembly NuGet package](https://www.nuget.org/packages/Sentry.AspNetCore.Blazor.WebAssembly).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#install)

Add the Sentry dependency to your Blazor WebAssembly application:

```shell
dotnet add package Sentry.AspNetCore.Blazor.WebAssembly -v 6.12.1
```

*Other available variations of the above snippet: Package Manager*

This package extends [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md). This means that in addition to the related Blazor WebAssembly features, you'll also get access to the `ILogger<T>` integration and other features available in the main [Sentry](https://docs.sentry.io/platforms/dotnet.md) SDK through this package.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `Microsoft.Extensions.Logging` need `EnableLogs = true`, and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#send-application-metrics-).

This guide also enables **Tracing**.

Sentry integration with Blazor WebAssembly is done by calling `.UseSentry()` and specifying the options, for example:

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/configuration/options.md#TracesSampleRate)
* Logs: via [`EnableLogs`](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/logs.md#enablelogs)

Don't need a feature? Remove its options from the snippet.

```csharp
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using Microsoft.Extensions.Logging;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.UseSentry(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    options.EnableLogs = true;
    // When configuring for the first time, to see what the SDK is doing:
    options.Debug = true;
    // Adds request URL and headers, IP and name for users, etc.
    options.SendDefaultPii = true;
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    options.TracesSampleRate = 0.1;
});

// Captures logError and higher as events
builder.Logging.AddSentry(o => o.InitializeSdk = false);

await builder.Build().RunAsync();
```

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#send-logs)

Use `Microsoft.Extensions.Logging` to send structured logs from your application. Set `EnableLogs = true` in your Sentry initialization.

See [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) for setup details.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/logs.md) for all available logging methods and formatting options.

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

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#samples)

* This [integration with Blazor WebAssembly](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Blazor.Wasm) sample demonstrates using Sentry with Blazor WebAssembly. (**C#**)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly.md#next-steps)

At this point, you should have integrated Sentry into your Blazor WebAssembly application. Here's what to explore next:

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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/migration.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/blazor-webassembly/legacy-sdk.md)

