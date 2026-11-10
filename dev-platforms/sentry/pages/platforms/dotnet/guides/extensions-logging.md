---
title: "Microsoft.Extensions.Logging"
source: https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md
path: platforms/dotnet/guides/extensions-logging
---

---
title: "Microsoft.Extensions.Logging"
description: "Learn about Sentry's .NET integration with Microsoft.Extensions.Logging."
url: https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/
---

# Sentry for Microsoft.Extensions.Logging

Sentry has an integration with `Microsoft.Extensions.Logging` through the [Sentry.Extensions.Logging NuGet package](https://www.nuget.org/packages/Sentry.Extensions.Logging).

## [Overview of the features](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#overview-of-the-features)

* Store log messages as breadcrumbs
* Send events to Sentry
* Send structured logs to Sentry

Two separate settings define the minimum log level to keep the log entry as a `Breadcrumb` and to send an `Event` to Sentry. The events include any stored breadcrumb on that [scope](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/enriching-events/scopes.md).

By default, any message with log level `Information` or higher will be kept as a `Breadcrumb`.

The default value to report a log entry as an event to Sentry is `Error`.

This means that out of the box, any `LogError` call will create an `Event` which will include breadcrumbs for all prior log messages of level `Information`, `Warning`, `Error` and `Critical`.

Additionally, when enabled, log messages are sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/logs.md). Filtering to control the minimum log level to capture should be done [via `Microsoft.Extensions.Logging` configuration](https://learn.microsoft.com/dotnet/core/extensions/logging/overview?tabs=command-line#how-filtering-rules-are-applied).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.Extensions.Logging -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means that besides the logging related features, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

The integration excludes the Sentry SDK's own logger categories to avoid capturing its diagnostic messages as events. Application categories that happen to start with `Sentry` aren't excluded solely because of that prefix.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#configure)

Call `AddSentry` on an `ILoggingBuilder`, either through a generic host or `LoggerFactory.Create`. This registers the providers for error events, breadcrumbs, and structured logs.

The legacy `ILoggerFactory.AddSentry` extension registers only the error-event and breadcrumb provider. Use `LoggerFactory.Create` with `builder.AddSentry` to capture structured logs too. ASP.NET Core's `UseSentry` already registers the providers, so it doesn't need a separate `AddSentry` call.

### [Example configuration](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#example-configuration)

#### [Through `ILoggingBuilder`](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#through-iloggingbuilder)

This example uses a generic host from the `Microsoft.Extensions.Hosting` package:

```csharp
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

var builder = Host.CreateApplicationBuilder(args);
// Lets Sentry read the top-level "Sentry" section of appsettings.json
builder.Logging.AddConfiguration(builder.Configuration);
builder.Logging.AddSentry();

using var host = builder.Build();
await host.RunAsync();
```

The host loads `appsettings.json` and environment variables. Sentry reads its options from the `Sentry` configuration section.

With this approach, options like `Dsn`, `SendDefaultPii`, `MinimumBreadcrumbLevel`, to name a few, can be set in `appsettings.json`.

Example using `appsettings.json`:

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Debug",
      "Microsoft": "Warning"
    }
  },
  "Sentry": {
    "Dsn": "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    "EnableLogs": true,
    "SendDefaultPii": true,
    "MinimumBreadcrumbLevel": "Debug",
    "MinimumEventLevel": "Warning",
    "MaxBreadcrumbs": 50
  }
}
```

Above we set the application wide minimum log level to `Debug` and we configure a minimum log level for Microsoft specific logs to `Warning`. Sentry specific settings are set under the `Sentry` property. Options are documented below.

#### [Through `ILoggerFactory`](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#through-iloggerfactory)

```csharp
using Microsoft.Extensions.Logging;

using (var loggerFactory = LoggerFactory.Create(builder =>
{
    builder.SetMinimumLevel(LogLevel.Information);
    builder.AddSentry(options =>
    {
        options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
        options.EnableLogs = true;
    });
}))
{
    var logger = loggerFactory.CreateLogger("Example");
    logger.LogInformation("Order processed {OrderId}", "order-123");
}
```

This approach doesn't include any of the framework's configuration system. Since the DSN is being provided via parameter, the SDK will be initialized.

More settings can be passed via the callback configuring the `SentryOptions`.

## [Options and Initialization](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#options-and-initialization)

In cases where `AddSentry` is called without arguments, it's worth noting that an overload exists where `SentryOptions` can be configured just like if `SentrySdk.Init` had been called.

Initialize the SDK once. `ILoggingBuilder.AddSentry` initializes it by default and can resolve a DSN from configuration or `SENTRY_DSN`. If another integration or `SentrySdk.Init` owns initialization, set `InitializeSdk = false`. Omitting the DSN isn't a substitute for this flag: if no DSN is found, initialization throws. An explicitly empty DSN disables the SDK.

For example:

```csharp
using (var loggerFactory = LoggerFactory.Create(builder =>
    builder.AddSentry(options =>
    {
        options.InitializeSdk = false;
        options.EnableLogs = true;
    })))
{ }
```

### [Options](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#options)

#### [MinimumBreadcrumbLevel](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#minimumbreadcrumblevel)

A `LogLevel` which indicates the minimum level a log message has to be included as a breadcrumb. By default this value is `Information`.

#### [MinimumEventLevel](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#minimumeventlevel)

A `LogLevel` which indicates the minimum level a log message has to be sent to Sentry as an event. By default this value is `Error`.

#### [InitializeSdk](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#initializesdk)

Whether or not this integration should initialize the SDK. If you intend to call `SentrySdk.Init` yourself, you should set this flag to `false`.

#### [Filters](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#filters)

A list of filters which are invoked before processing log messages. This allows you to inspect the details of the log entry before they become a `Breadcrumb` or an `Event` with full access to the `Microsoft.Extensions.Logging` data.

##### Note

These filters only apply to breadcrumbs and events. They don't control which logs will be captured as structured logs in Sentry. That can be controlled independently using the [filtering capabilities built into `Microsoft.Extensions.Logging`](https://learn.microsoft.com/dotnet/core/extensions/logging/overview?tabs=command-line#how-filtering-rules-are-applied).

#### [TagFilters](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#tagfilters)

A list of filters which are invoked before processing any log message to filter out undesired tags.

For example, to remove all tags starting with `PROC_`, add a tag filter to your `SentryOptions` when initializing the SDK.

```csharp
options.TagFilters.Add("PROC_");
```

## [Verify](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#verify)

After creating a logger with one of the configurations above, send an informational log and an error to verify both providers:

```csharp
logger.LogInformation("Sentry logging verification");
logger.LogError("Sentry error-event verification");
```

Check **Logs** for the informational log and **Issues** for the error event. Run this code before disposing the host or logger factory.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#samples)

* A [simple example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.ME.Logging) using simply the `LoggerFactory`.
* An [example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.GenericHost) using the *generic host*.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

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
- [NLog](https://docs.sentry.io/platforms/dotnet/guides/nlog.md)
- [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/legacy-sdk.md)

