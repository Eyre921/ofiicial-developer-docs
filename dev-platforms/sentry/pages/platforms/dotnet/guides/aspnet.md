---
title: "ASP.NET"
source: https://docs.sentry.io/platforms/dotnet/guides/aspnet.md
path: platforms/dotnet/guides/aspnet
---

---
title: "ASP.NET"
description: "Learn about Sentry's .NET integration with ASP.NET."
url: https://docs.sentry.io/platforms/dotnet/guides/aspnet/
---

# Sentry for ASP.NET

Sentry provides an integration with ASP.NET through the [Sentry.AspNet NuGet package](https://www.nuget.org/packages/Sentry.AspNet).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.AspNet -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

You can combine this integration with a logging library like `log4net`, `NLog` or `Serilog` to include both request data as well as your logs as breadcrumbs. The logging integrations also capture events when an error is logged.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#send-application-metrics-).

This guide also enables **Tracing**.

You configure the SDK in the `Global.asax.cs`:

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/aspnet/configuration/options.md#TracesSampleRate)
* Logs from logging integrations: via [`EnableLogs`](https://docs.sentry.io/platforms/dotnet/guides/aspnet/logs.md#enablelogs)

Don't need a feature? Remove its options from the snippet.

```csharp
using System;
using System.Web;
using Sentry.AspNet;
using Sentry.EntityFramework; // If you also installed Sentry.EntityFramework
using Sentry.Extensibility;

public class MvcApplication : HttpApplication
{
    private IDisposable _sentry;

    protected void Application_Start()
    {
        // Initialize Sentry to capture AppDomain unhandled exceptions and more.
        _sentry = SentrySdk.Init(options =>
        {
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
            // When configuring for the first time, to see what the SDK is doing:
            options.Debug = true;
            // Adds request URL and headers, IP and name for users, etc.
            options.SendDefaultPii = true;
            options.EnableLogs = true;
            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;

            // If you also installed the Sentry.EntityFramework package
            options.AddEntityFramework();
            options.AddAspNet();
        });
    }

    // Global error catcher
    protected void Application_Error() => Server.CaptureLastError();
    protected void Application_BeginRequest()
    {
        Context.StartSentryTransaction();
    }

    protected void Application_EndRequest()
    {
        Context.FinishSentryTransaction();
    }

    protected void Application_End()
    {
        // Flushes out events before shutting down.
        _sentry?.Dispose();
    }
}
```

### [Capturing the affected user](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#capturing-the-affected-user)

When opting-in to [SendDefaultPii](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#senddefaultpii), the SDK will automatically read the user from the request by inspecting `HttpContext.User`. Default claim values like `NameIdentifier` for the *Id* will be used.

```csharp
options.AddAspNet();
options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
// Opt-in to send things like UserId and UserName if a user is logged-in
options.SendDefaultPii = true;
```

### [SendDefaultPii](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#senddefaultpii)

Although this setting is part of the [Sentry](https://docs.sentry.io/platforms/dotnet.md) package, in the context of ASP.NET Core, it means reporting the user by reading the frameworks `HttpContext.User`. The strategy to create the `SentryUser` can be customized.

### [IncludeRequestPayload](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#includerequestpayload)

It's helpful to troubleshoot a problem in the API when the payload that hit the endpoint is logged. Opt-in to send the request body to Sentry:

```csharp
options.AddAspNet(RequestSize.Always);
```

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels without an additional option. If you also send logs through an integration, set `EnableLogs = true` in the initialization snippet.

If you use Serilog, NLog, or log4net, see the documented [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md), [NLog](https://docs.sentry.io/platforms/dotnet/guides/nlog.md), and [log4net](https://docs.sentry.io/platforms/dotnet/guides/log4net.md) integrations.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnet/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/aspnet/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#troubleshooting)

For information about Troubleshooting, please visit the [troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/aspnet/troubleshooting.md) page.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#samples)

* A [sample with ASP.NET and EF 6](https://github.com/getsentry/examples/tree/master/dotnet/AspNetMvc5Ef6) and additional samples of the [.NET SDKs](https://github.com/getsentry/examples/tree/master/dotnet)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md#next-steps)

At this point, you should have integrated Sentry into your ASP.NET application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)

## Other .NET Frameworks

- [.NET for Android](https://docs.sentry.io/platforms/dotnet/guides/android.md)
- [.NET for iOS, macOS, and Mac Catalyst](https://docs.sentry.io/platforms/dotnet/guides/apple.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/aspnet/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/aspnet/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/aspnet/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnet/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/aspnet/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/aspnet/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/aspnet/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/aspnet/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/aspnet/migration.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/aspnet/crons.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/aspnet/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/aspnet/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/aspnet/legacy-sdk.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/aspnet/troubleshooting.md)

