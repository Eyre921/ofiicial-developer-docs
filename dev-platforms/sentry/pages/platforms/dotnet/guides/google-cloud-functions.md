---
title: "Google Cloud Functions"
source: https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md
path: platforms/dotnet/guides/google-cloud-functions
---

---
title: "Google Cloud Functions"
description: "Learn about Sentry's .NET integration with Google Cloud Functions."
url: https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/
---

# Sentry for Google Cloud Functions (.NET)

Sentry provides an integration with `Google Cloud Functions` through the [Sentry.Google.Cloud.Functions NuGet package](https://www.nuget.org/packages/sentry.google.cloud.functions).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.Google.Cloud.Functions -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

Or, manually add the Sentry dependency into your csproj file:

```xml
  <ItemGroup>
    <PackageReference Include="Sentry.Google.Cloud.Functions" Version="6.12.1"/>
  </ItemGroup>
```

This package extends `Sentry.AspNetCore`, which in turn extends `Sentry`'s main SDK. That means that besides the logging-related features, through this package you'll also get access to all API and features available in those packages.

Messages logged from assemblies with the name starting with `Sentry` will not generate events.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#send-application-metrics-).

This guide also enables **Tracing**.

The `Sentry.Google.Cloud.Functions` integration also gives you:

* Easy Google Cloud Functions integration, single line: `[assembly: FunctionsStartup(typeof(SentryStartup))]`
* Captures unhandled exceptions in the middleware pipeline
* Captures exceptions handled by the framework `UseExceptionHandler`
* Captures process-wide unhandled exceptions (AppDomain)
* Captures `LogError` or `LogCritical`
* Any event sent will include relevant application log messages
* RequestId as tag
* URL as tag
* Environment is automatically set (IHostingEnvironment)
* Request payload can be captured if opt-in
* Support for EventProcessors registered with DI
* Support for ExceptionProcessors registered with DI
* Supports configuration system (bind to `SentryAspNetCoreOptions`)
* Server OS info sent
* Server Runtime info sent
* Request headers sent
* HTTP Proxy configuration
* Request body compressed
* Event flooding protection (429 retry-after and internal bound queue)
* Assembly Strong named

The simplest way to configure the `Sentry.Google.Cloud.Functions` package is by setting up your Sentry configuration into `appsettings.json` using the assembly method `FunctionsStartup` to include the type `SentryStartup`.

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```json
{
  "Sentry": {
    "Dsn": "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    "MaxRequestBodySize": "Always",
    "SendDefaultPii": true,
    "MinimumBreadcrumbLevel": "Debug",
    "MinimumEventLevel": "Warning",
    "AttachStackTrace": true,
    "Debug": true,
    "DiagnosticLevel": "Error",
    "TracesSampleRate": 1.0
  }
}
```

> An example of some of the options that can be configured via `appsettings.json`.

Setting `TracesSampleRate` to `1.0` captures 100% of spans. We recommend reducing this value in production.

To load the configurations, you will need to use the assembly `[assembly: FunctionsStartup(typeof(SentryStartup))]`. After being initialized, the framework automatically loads `appsettings.json` and environment variables, binding to `SentryAspNetCoreOptions`.

```csharp
using System.Threading.Tasks;
using Google.Cloud.Functions.Framework;
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Http;

[assembly: FunctionsStartup(typeof(SentryStartup))]

public class Function : IHttpFunction
{
}
```

Some of the settings require actual code. For those, like the `BeforeSend` callback, you will need to create a new class implementing the abstract class `FunctionsStartup` to set it up:

```csharp
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Sentry.AspNetCore;

[assembly: FunctionsStartup(typeof(CustomOptions))]

public class CustomOptions : FunctionsStartup
{
    public override void ConfigureServices(WebHostBuilderContext context, IServiceCollection services)
    {
        base.ConfigureServices(context, services);
        services.Configure<SentryAspNetCoreOptions>(options =>
        {
            options.SetBeforeSend(@event =>
            {
                @event.ServerName = null;
                return @event;
            });
        });
    }
}
```

> Example modifying all events before they are sent to avoid server names being reported.

### [Dependency Injection](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#dependency-injection)

Much of the behavior of the Google cloud functions integration with Sentry can be customized by using the frameworks dependency injection system. That is done by registering your own implementation of some of the exposed abstraction inside of `FunctionsStartup`.

#### [Capturing the Affected User](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#capturing-the-affected-user)

When opting in to `SendDefaultPii`, the SDK will automatically read the user from the request by inspecting `HttpContext.User`. Default claim values like `NameIdentifier` for the *Id* will be used.

If you wish to change the behavior of how to read the user from the request, you can register a new `IUserFactory` into the container:

```csharp
using Google.Cloud.Functions.Hosting;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Sentry.AspNetCore;

[assembly: FunctionsStartup(typeof(UserFactoryStartup))]

public class UserFactoryStartup : FunctionsStartup
{
    public override void ConfigureServices(WebHostBuilderContext context, IServiceCollection services)
    {
        base.ConfigureServices(context, services);
        services.AddSingleton<IUserFactory, MyUserFactory>();
    }
}
```

### [Options and Initialization](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#options-and-initialization)

As previously mentioned, this package is a wrapper around [Sentry.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md), [Sentry.AspNetCore](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md) and [Sentry](https://docs.sentry.io/platforms/dotnet.md). Please refer to the documentation of these packages to get the options that are defined at those levels.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions.md#next-steps)

At this point, you should have integrated Sentry into your Google Cloud Functions application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)
* Check out the [Google Cloud Functions sample](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.Google.Cloud.Functions), or browse [more samples](https://github.com/getsentry/sentry-dotnet-samples) of the .NET SDKs

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

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/configuration.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/migration.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/google-cloud-functions/legacy-sdk.md)

