---
title: "ASP.NET Core"
source: https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md
path: platforms/dotnet/guides/aspnetcore
---

---
title: "ASP.NET Core"
description: "Learn about Sentry's .NET integration with ASP.NET Core."
url: https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/
---

# Sentry for ASP.NET Core

Sentry provides an integration with ASP.NET Core through the [Sentry.AspNetCore](https://www.nuget.org/packages/Sentry.AspNetCore) NuGet package.

## [Install](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.AspNetCore -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI, Paket CLI*

This package extends [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md). This means that besides the ASP.NET Core related features, through this package you'll also get access to all the framework's logging integration and also the features available in the main [Sentry](https://docs.sentry.io/platforms/dotnet.md) SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `Microsoft.Extensions.Logging` need `EnableLogs = true`, and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#send-application-metrics-).

This guide also enables **Tracing**.

The simplest way to initialize Sentry in ASP.NET Core is by using the `UseSentry` extension method from the `Sentry.AspNetCore` package in conjunction with the [framework configuration system](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-7.0).

Call `UseSentry` with your DSN and the options you want. The SDK provides this as extension methods to support ASP.NET Core `2.X`, `3.X`, and `5.X` and later.

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/configuration/options.md#TracesSampleRate)
* Logs: via [`EnableLogs`](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/logs.md#enablelogs)

Don't need a feature? Remove its options from the snippet.

**WebApplication**

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.WebHost.UseSentry(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    options.EnableLogs = true;
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    options.TracesSampleRate = 1.0;
});
```

**IHostBuilder**

```csharp
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseSentry(options =>
            {
                options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
                options.EnableLogs = true;
                // Enables Tracing.
                // Set to 1.0 to capture 100% of spans for tracing.
                // We recommend reducing this value in production.
                options.TracesSampleRate = 1.0;
            });
        });
```

**IWebHost**

```csharp
public static IWebHost BuildWebHost(string[] args) =>
    WebHost.CreateDefaultBuilder(args)
        .UseSentry(options =>
        {
            options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
            options.EnableLogs = true;
            // Enables Tracing.
            // Set to 1.0 to capture 100% of spans for tracing.
            // We recommend reducing this value in production.
            options.TracesSampleRate = 1.0;
        })
```

### [Additional configuration](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#additional-configuration)

The framework takes configuration settings from `appsettings.json`, environment variables, or from code. These settings get applied to `Sentry.AspNetCore.SentryAspNetCoreOptions`, which extends `Sentry.Extensions.Logging.SentryLoggingOptions`, which in turn extends `Sentry.SentryOptions`. This means options for `Sentry.AspNetCore` as well as all the inner packages are available to be configured through the configuration system.

### [appsettings.json](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#appsettingsjson)

An example of some of the options that can be configured via `appsettings.json`:

```json
{
  "Sentry": {
    "Dsn": "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    "SendDefaultPii": true,
    "MaxRequestBodySize": "Always",
    "MinimumBreadcrumbLevel": "Debug",
    "MinimumEventLevel": "Warning",
    "AttachStackTrace": true,
    "Debug": true,
    "DiagnosticLevel": "Error"
  }
}
```

### [Environment variables](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#environment-variables)

It's also possible to bind properties to the SDK via environment variables, like:

**Windows**

```shell
set Sentry__Debug=true
```

**Linux or macOS**

```shell
export Sentry__Debug=true
```

ASP.NET Core will automatically read this environment variable and bind it to the SDK configuration object.

### [Using code](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#using-code)

Finally, any settings that can be configured via `appsettings.json` or environment variables can also be configured via code. Some settings can only be configured in code, such as the `BeforeSend` callback:

```csharp
.UseSentry(options =>
{
    options.SendDefaultPii = true; // Adds request URL and headers, IP and name for users, etc.
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    options.TracesSampleRate = 1.0;
    options.SetBeforeSend((@event, hint) =>
    {
        // Never report server names
        @event.ServerName = null;
        return @event;
    });
})
```

*Other available variations of the above snippet: fsharp*

> Example modifying all events before they are sent to avoid server names being reported.

### [Dependency Injection](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#dependency-injection)

Much of the behavior of the ASP.NET Core integration with Sentry can be customized by using the frameworks dependency injection system. That is done by registering your own implementation of some of the exposed abstraction.

#### [Lifetimes](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#lifetimes)

The lifetime used will be respected by the SDK. For example, when registering a `Transient` dependency, a new instance of the processor is created for each event sent out to Sentry. This allows the use of non thread-safe event processors.

#### [Capturing the affected user](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#capturing-the-affected-user)

When opting-in to [SendDefaultPii](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#senddefaultpii), the SDK will automatically read the user from the request by inspecting `HttpContext.User`. Default claim values like `NameIdentifier` for the *Id* will be used.

If you wish to change the behavior of how to read the user from the request, you can register a new `ISentryUserFactory` into the container:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddSingleton<ISentryUserFactory, MyUserFactory>();
}
```

*Other available variations of the above snippet: fsharp*

#### [Adding event and exception processors](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#adding-event-and-exception-processors)

Event processors and exception processors can be added via DI:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddTransient<ISentryEventProcessor, MyEventProcessor>();
    services.AddScoped<ISentryEventExceptionProcessor, MyExceptionProcessor>();
}
```

*Other available variations of the above snippet: fsharp*

### [Options and Initialization](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#options-and-initialization)

As previously mentioned, this package is a wrapper around [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) and [Sentry](https://docs.sentry.io/platforms/dotnet.md). Please refer to the documentation of these packages to get the options that are defined at those levels.

Below, the options that are specific to `Sentry.AspNetCore` will be described.

#### [SendDefaultPii](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#senddefaultpii)

Although this setting is part of the [Sentry](https://docs.sentry.io/platforms/dotnet.md) package, in the context of ASP.NET Core, it means reporting the user by reading the frameworks `HttpContext.User`. The strategy to create the `SentryUser` can be customized. Please read [retrieving user info](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#capturing-the-affected-user) for more.

#### [Environment](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#environment)

The environment name is automatically populated by reading the frameworks `IHostingEnvironment` value.

This option is part of the [Sentry](https://docs.sentry.io/platforms/dotnet.md) package. The value of `IHostingEnvironment` will only be used if **no other method was used**.

Methods that take precedence over `IHostingEnvironment` are:

* Programmatically: `options.Environment`
* Environment variable *SENTRY\_ENVIRONMENT*
* Configuration system like `appsettings.json`

#### [MaxRequestBodySize](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#maxrequestbodysize)

This parameter controls whether integrations should capture HTTP request bodies. It can be set to one of the following values:

* `None`: Request bodies are never sent.
* `Small`: Only small request bodies will be captured (typically 4KB).
* `Medium`: Medium and small requests will be captured (typically 10KB).
* `Always`: The SDK will always capture the request body as long as Sentry can make sense of it.

If the request bodies should be captured, all requests will have the `EnableRewind` method invoked. This is done so that the request data can be read later, in case an error happens while processing the request.

#### [CaptureBlockingCalls](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#captureblockingcalls)

When set to `true`, the SDK will detect blocking calls in async methods (like `Task.Wait()` and `Task.Result`) and report these to Sentry as errors. Blocking calls can lead to [Threadpool starvation](https://learn.microsoft.com/en-nz/archive/blogs/vancem/diagnosing-net-core-threadpool-starvation-with-perfview-why-my-service-is-not-saturating-all-cores-or-seems-to-stall).

Check out the MVC Sample for an example of [how to use this feature](https://github.com/getsentry/sentry-dotnet/blob/d1e5efcdf3af763ad49f11cd2426cc14a315a901/samples/Sentry.Samples.AspNetCore.Mvc/Controllers/HomeController.cs#L17-L36).

In that sample you can also see an example of [how to suppress blocking detection](https://github.com/getsentry/sentry-dotnet/blob/d1e5efcdf3af763ad49f11cd2426cc14a315a901/samples/Sentry.Samples.AspNetCore.Mvc/Controllers/HomeController.cs#L45-L48) for specific code blocks.

This feature makes use of the `Ben.BlockingDetector` library and so has [the same caveats](https://github.com/getsentry/Ben.BlockingDetector?tab=readme-ov-file#caveats):

> 1. For async methods with occurrences of **`.ConfigureAwait(false)`**, detection won't alert for blocking Monitor calls after occurrences in the case where the returned Task wasn't already completed
> 2. Won't alert for blocking calls that don't block, like on precompleted Tasks (such as a single small `Body.Write`)
> 3. Won't alert for blocking that happens in syscalls (like `File.Read(...)` and `Thread.Sleep`)
>
> It will detect CLR-initiated waits lock, `ManualResetEventSlim`, `Semaphore\{Slim\}`, `Task.Wait`, `Task.Result` etc. if they do block.

#### [IncludeActivityData](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#includeactivitydata)

Opt-in to capture values from [System.Diagnostic.Activity](https://github.com/dotnet/runtime/blob/master/src/libraries/System.Diagnostics.DiagnosticSource/src/ActivityUserGuide.md) if one exists.

### [Tunnel](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#tunnel)

If events are being logged to Sentry from the client-side, then you should use a [tunnel](https://docs.sentry.io/platforms/javascript/troubleshooting.md#using-the-tunnel-option).

A tunnel is an HTTP endpoint that acts as a proxy between Sentry and your application. Because you control this server, there is no risk of any requests sent to it being blocked.

#### [Usage](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#usage)

* Add to the container by calling `AddSentryTunneling();` on `IServiceCollection`.
* Add the web app by calling `UseSentryTunneling();` on `IApplicationBuilder`.
* In the client-side JavaScript configuration, ensure the tunnel option is used:

```javascript
Sentry.init({
  dsn: "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
  sendDefaultPii: true,
  tunnel: "/tunnel",
});
```

The [AspNetCore.Mvc sample](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Mvc) uses this approach.

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#send-logs)

Use `Microsoft.Extensions.Logging` to send structured logs from your application. Set `EnableLogs = true` in your Sentry initialization.

See [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md) for setup details.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/logs.md) for all available logging methods and formatting options.

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

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#samples)

* A [simple example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Basic) without MVC. (**C#**)
* An [example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Mvc) using MVC and most of the SDK features. (**C#**)
* An [example](https://github.com/sentry-demos/giraffe) using Giraffe on top of ASP.NET Core with a basic overview of available features. (**F#**)
* For [more samples](https://github.com/getsentry/sentry-dotnet-samples) of the .NET SDKs.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md#next-steps)

At this point, you should have integrated Sentry into your ASP.NET Core application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)

## Other .NET Frameworks

- [.NET for Android](https://docs.sentry.io/platforms/dotnet/guides/android.md)
- [.NET for iOS, macOS, and Mac Catalyst](https://docs.sentry.io/platforms/dotnet/guides/apple.md)
- [ASP.NET](https://docs.sentry.io/platforms/dotnet/guides/aspnet.md)
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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/configuration.md)
- [Features](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/features.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/legacy-sdk.md)
- [Built-in sampling context](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore/builtin-sampling-context.md)

