---
title: "Blazor Interactive SSR"
source: https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md
path: platforms/dotnet/guides/blazor-server
---

---
title: "Blazor Interactive SSR"
description: "Learn about Sentry's .NET integration with Blazor Interactive Server-Side Rendering."
url: https://docs.sentry.io/platforms/dotnet/guides/blazor-server/
---

# Sentry for Blazor Interactive SSR

Blazor Interactive SSR (also known as Blazor Server) runs components on the server and streams UI updates to the browser over a SignalR connection (circuit). Sentry integrates with Blazor Interactive SSR through the [Sentry.AspNetCore NuGet package](https://www.nuget.org/packages/Sentry.AspNetCore), which captures unhandled exceptions and provides optional tracing via OpenTelemetry.

## [Install](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#install)

Add the Sentry dependency to your Blazor Server application:

```shell
dotnet add package Sentry.AspNetCore -v 6.12.1
```

*Other available variations of the above snippet: Package Manager*

This package extends [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md). In addition to Blazor Server features, you'll also get the `ILogger<T>` integration and all features available in the main [Sentry](https://docs.sentry.io/platforms/dotnet.md) SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#send-application-metrics-).

This guide also enables **Tracing**.

Initialize Sentry by calling `UseSentry` on your `WebHostBuilder`:

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

builder.WebHost.UseSentry(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    // When configuring for the first time, to see what the SDK is doing:
    options.Debug = true;
    // Adds request URL and headers, IP and name for users, etc.
    options.SendDefaultPii = true;
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    options.TracesSampleRate = 0.1;
});

var app = builder.Build();

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
```

### [Limited Tracing on .NET 10 and Later](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#limited-tracing-on-net-10-and-later)

Tracing events in Blazor Server applications is challenging due to the socket based nature of communications.

However, on .NET 10 and later, Blazor emits OpenTelemetry activities for circuit lifecycle events, component navigation, and UI interactions that can be used to provide some limited tracing. The [Sentry.Samples.AspNetCore.Blazor.Server](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Blazor.Server) sample project gives an example of this.

#### [Install OpenTelemetry](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#install-opentelemetry)

See [OpenTelemetry Support](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/tracing/instrumentation/opentelemetry.md) for installation and setup instructions.

#### [Configure OpenTelemetry](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#configure-opentelemetry)

Wire up Sentry as an OpenTelemetry exporter, subscribe to the Blazor activity sources, and register helper services for circuit and breadcrumb tracking:

```csharp
using Microsoft.AspNetCore.Components.Server.Circuits;
using OpenTelemetry.Trace;
using Sentry.OpenTelemetry;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

builder.Services.AddOpenTelemetry()
    .WithTracing(tracing =>
    {
        tracing.AddSource("Microsoft.AspNetCore.Components");
        tracing.AddSource("Microsoft.AspNetCore.Components.Server.Circuits");
        tracing.AddAspNetCoreInstrumentation();
        // Export traces to Sentry
        tracing.AddSentry();
    });

builder.WebHost.UseSentry(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    options.UseOpenTelemetry();
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    options.TracesSampleRate = 0.1;
    // Rewrites /_blazor SignalR transaction names to the actual Blazor route
    options.AddEventProcessor(new BlazorEventProcessor());
});

// Track circuit lifecycle events and add navigation/UI breadcrumbs
builder.Services.AddSingleton<BlazorSentryIntegration>();
builder.Services.AddHostedService(sp => sp.GetRequiredService<BlazorSentryIntegration>());
builder.Services.AddScoped<CircuitHandler, SentryCircuitHandler>();

var app = builder.Build();

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
```

#### [Circuit Lifecycle Tracking Services](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#circuit-lifecycle-tracking-services)

The `BlazorSentryIntegration`, `SentryCircuitHandler`, and `BlazorEventProcessor` services shown above are not part of the Sentry integration. You can copy them from the [Blazor Server sample](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Blazor.Server/Services) into your application if they prove useful for your use case.

They provide the following features:

| Service                   | Purpose                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------ |
| `BlazorSentryIntegration` | Subscribes to Blazor activity sources and adds navigation/event breadcrumbs to the active Sentry scope |
| `SentryCircuitHandler`    | Hooks into circuit open/close events to track circuit lifetime and prevent memory leaks                |
| `BlazorEventProcessor`    | Rewrites uninformative SignalR transaction names (e.g. `/_blazor`) to the actual Blazor route          |

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#samples)

* This [integration with Blazor Interactive SSR](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Blazor.Server) sample demonstrates using Sentry with Blazor Server, including enhanced circuit tracking on .NET 10. (**C#**)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/blazor-server.md#next-steps)

At this point, you should have integrated Sentry into your Blazor Server application. Here's what to explore next:

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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/blazor-server/legacy-sdk.md)

