---
title: "AWS Lambda"
source: https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md
path: platforms/dotnet/guides/aws-lambda
---

---
title: "AWS Lambda"
description: "Learn about Sentry's .NET integration with AWS Lambda and ASP.NET Core."
url: https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/
---

# Sentry for AWS Lambda (.NET)

Sentry provides an integration with AWS Lambda ASP.NET Core Server through the [Sentry.AspNetCore NuGet package](https://www.nuget.org/packages/Sentry.AspNetCore).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.AspNetCore -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

You can combine this integration with a logging library like `log4net`, `NLog`, or `Serilog` to include both request data as well as your logs as breadcrumbs. The logging ingrations also capture events when an error is logged.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `Microsoft.Extensions.Logging` need `EnableLogs = true`, and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#send-application-metrics-).

This guide also enables **Tracing**.

All `ASP.NET Core` configurations are valid here. But one configuration in particular is relevant.

`FlushOnCompletedRequest` ensures all events are flushed out. This is because the general ASP.NET Core hooks for when the process is exiting are not guaranteed to run in a serverless environment. This setting ensures that no event is lost if AWS recycles the process.

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/configuration/options.md#TracesSampleRate)
* Logs: via [`EnableLogs`](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/logs.md#enablelogs)

Don't need a feature? Remove its options from the snippet.

```csharp
public class LambdaEntryPoint : Amazon.Lambda.AspNetCoreServer.APIGatewayProxyFunction
{
    protected override void Init(IWebHostBuilder builder)
    {
        builder
            // Add Sentry
            .UseSentry(options =>
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
                options.TracesSampleRate = 1.0;
                // Required in Serverless environments
                options.FlushOnCompletedRequest = true;
            })
            .UseStartup<Startup>();
    }
}
```

Check out the [Sentry ASP.NET Core](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md) documentation for the complete set of options.

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#send-logs)

Use `Microsoft.Extensions.Logging` to send structured logs from your application. Set `EnableLogs = true` in your Sentry initialization.

See [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) for setup details.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/logs.md) for all available logging methods and formatting options.

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

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#samples)

* Our [samples on GitHub](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.Aws.Lambda.AspNetCoreServer) demonstrate Sentry on AWS Lambda. (**C#**)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda.md#next-steps)

At this point, you should have integrated Sentry into your AWS Lambda application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)

## Other .NET Frameworks

- [.NET for Android](https://docs.sentry.io/platforms/dotnet/guides/android.md)
- [.NET for iOS, macOS, and Mac Catalyst](https://docs.sentry.io/platforms/dotnet/guides/apple.md)
- [ASP.NET](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md)
- [ASP.NET Core](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/migration.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/aws-lambda/legacy-sdk.md)

