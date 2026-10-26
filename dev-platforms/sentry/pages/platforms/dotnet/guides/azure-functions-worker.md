---
title: "Azure Functions"
source: https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md
path: platforms/dotnet/guides/azure-functions-worker
---

---
title: "Azure Functions"
description: "Learn about Sentry's .NET integration with Azure Functions."
url: https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/
---

# Sentry for Azure Functions (.NET)

Sentry provides an integration with Azure Functions through the [Sentry.Extensions.Logging](https://www.nuget.org/packages/Sentry.Extensions.Logging) and [Sentry.OpenTelemetry.Exporter](https://www.nuget.org/packages/Sentry.OpenTelemetry.Exporter) NuGet packages.

## [Install](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#install)

Add the Sentry dependencies to your Azure Functions application:

```shell
dotnet add package Sentry.Extensions.Logging -v 6.12.1
dotnet add package Sentry.OpenTelemetry.Exporter -v 6.12.1
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Instrumentation.Http
```

*Other available variations of the above snippet: Package Manager*

The [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) package also provides access to the `ILogger<T>` integration and the other core features available in the [Sentry](https://docs.sentry.io/platforms/dotnet.md) SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK by calling `AddSentry` when configuring logging. **Logs** sent through `Microsoft.Extensions.Logging` need `EnableLogs = true`, and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#send-application-metrics-).

This guide also enables **Tracing** through OpenTelemetry. Sentry's OTLP exporter is added to the OpenTelemetry `TracerProviderBuilder`, and `UseOtlp()` tells the Sentry SDK to use OpenTelemetry for tracing.

The snippet also turns on:

* Tracing: via `AddSentryOtlpExporter` and `UseOtlp()`. Don't also set `TracesSampleRate`; OpenTelemetry handles tracing. See [OpenTelemetry (OTLP)](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/tracing/instrumentation/opentelemetry-otlp.md) for sampling and trace propagation.
* Logs: via [`EnableLogs`](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/logs.md#enablelogs)

Don't need a feature? Remove its options from the snippet.

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using OpenTelemetry.Trace;

var host = new HostBuilder()
    .ConfigureFunctionsWorkerDefaults()
    .ConfigureServices(services =>
    {
        services.AddOpenTelemetry().WithTracing(builder =>
        {
            builder
                .AddSentryOtlpExporter("https://<key>@o<orgId>.ingest.sentry.io/<projectId>") // <-- Send traces to Sentry over OTLP
                .AddHttpClientInstrumentation(); // From OpenTelemetry.Instrumentation.Http, instruments outgoing HTTP requests
        });
    })
    .ConfigureLogging(logging =>
    {
        logging.AddSentry(options =>
        {
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
            options.EnableLogs = true;
            options.UseOtlp(); // <-- Configure Sentry to use OpenTelemetry for tracing
            options.Debug = true;
        });
    })
    .Build();

await host.RunAsync();
```

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#send-logs)

Use `Microsoft.Extensions.Logging` to send structured logs from your application. Set `EnableLogs = true` in your Sentry initialization.

See [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) for setup details.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/logs.md) for all available logging methods and formatting options.

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

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#samples)

* [Azure Functions Sample](https://github.com/getsentry/sentry-dotnet/blob/main/samples/Sentry.Samples.OpenTelemetry.AzureFunctions/) demonstrates Sentry with Azure Functions Isolated Worker SDK. (**C#**)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker.md#next-steps)

At this point, you should have integrated Sentry into your Azure Functions application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Learn more about [tracing with OpenTelemetry (OTLP)](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/tracing/instrumentation/opentelemetry-otlp.md)

## Other .NET Frameworks

- [.NET for Android](https://docs.sentry.io/platforms/dotnet/guides/android.md)
- [.NET for iOS, macOS, and Mac Catalyst](https://docs.sentry.io/platforms/dotnet/guides/apple.md)
- [ASP.NET](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md)
- [ASP.NET Core](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md)
- [AWS Lambda](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/migration.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/azure-functions-worker/legacy-sdk.md)

