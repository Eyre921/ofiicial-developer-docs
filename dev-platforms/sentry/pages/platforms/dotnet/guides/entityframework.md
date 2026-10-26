---
title: "Entity Framework"
source: https://docs.sentry.io/platforms/dotnet/guides/entityframework.md
path: platforms/dotnet/guides/entityframework
---

---
title: "Entity Framework"
description: "Learn about Sentry's .NET integration with Entity Framework."
url: https://docs.sentry.io/platforms/dotnet/guides/entityframework/
---

# Sentry for Entity Framework

Sentry provides an integration with `EntityFramework` through the of the [Sentry.EntityFramework NuGet package](https://www.nuget.org/packages/Sentry.EntityFramework).

> Looking for `EntityFramework Core`? If you're targeting .NET Core 3.1 or newer, that's already built in to the main Sentry .NET SDK. It's also enabled by default for our ASP.NET or ASP.NET Core integrations, even for older targets. For other scenarios, you may need to add the `Sentry.DiagnosticSource` package and call `AddDiagnosticSourceIntegration`, [as described here](https://docs.sentry.io/platforms/dotnet/tracing/instrumentation/automatic-instrumentation.md#diagnosticsource-integration). (The rest of this page describes our EF6 integration, not EFCore.)

**Overview of the features**

* Queries as breadcrumbs
* Validation errors

All queries executed are added as breadcrumbs and are sent with any event which happens on the same [scope](https://docs.sentry.io/platforms/dotnet/guides/entityframework/enriching-events/scopes.md). Besides that, validation errors are also included as `Extra`.

## [Install](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#install)

```powershell
Install-Package Sentry.EntityFramework -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means that besides the EF features, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#send-application-metrics-).

This guide also enables **Tracing**.

Add the Entity Framework 6 support to your project in one step:

* When initializing the SDK, call the extension method `AddEntityFramework()` on `SentryOptions`. This will register all error processors to extract extra data, such as validation errors, from the exceptions thrown by Entity Framework.

### [Example configuration](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#example-configuration)

For example, configuring an ASP.NET app with *global.asax*:

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/entityframework/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```csharp
using System;
using System.Configuration;
using Sentry.AspNet;

public class MvcApplication : System.Web.HttpApplication
{
    private IDisposable _sentrySdk;

    protected void Application_Start()
    {
        _sentrySdk = SentrySdk.Init(options =>
        {
            // We store the DSN inside Web.config
            options.Dsn = ConfigurationManager.AppSettings["SentryDsn"];
            // Adds request URL and headers, IP and name for users, etc.
            options.SendDefaultPii = true;
            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;
            // Add the EntityFramework integration
            options.AddEntityFramework();
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
    public override void Dispose()
    {
        _sentrySdk.Dispose();
        base.Dispose();
    }
}
```

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/entityframework/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/entityframework/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Sample](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#sample)

Check out a complete working [sample](https://github.com/getsentry/sentry-dotnet-ef/tree/master/samples/Sentry.Samples.AspNet.Mvc) to see it in action.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/entityframework.md#next-steps)

At this point, you should have integrated Sentry into your Entity Framework application. Here's what to explore next:

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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/entityframework/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/entityframework/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/entityframework/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/entityframework/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/entityframework/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/entityframework/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/entityframework/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/entityframework/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/entityframework/migration.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/entityframework/crons.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/entityframework/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/entityframework/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/entityframework/legacy-sdk.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/entityframework/troubleshooting.md)

