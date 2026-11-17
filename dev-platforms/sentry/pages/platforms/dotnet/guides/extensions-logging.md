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

Log messages are also sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/logs.md). Filtering to control the minimum log level to capture should be done [via `Microsoft.Extensions.Logging` configuration](https://learn.microsoft.com/dotnet/core/extensions/logging/overview?tabs=command-line#how-filtering-rules-are-applied).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.Extensions.Logging -Version 7.0.1
```

*Other available variations of the above snippet: .NET Core CLI*

On .NET Framework, also install the `Microsoft.Extensions.Logging` package. The examples on this page need it.

This package extends `Sentry` main SDK. That means that besides the logging related features, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

Generic host apps install the `Sentry.Extensions.Hosting` package instead, which depends on this one. See the [Generic Host](https://docs.sentry.io/platforms/dotnet/guides/extensions-hosting.md) guide.

The integration excludes the Sentry SDK's own logger categories to avoid capturing its diagnostic messages as events. Application categories that happen to start with `Sentry` aren't excluded solely because of that prefix.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#configure)

If your app uses one of these integrations, skip this setup. Call that integration's `UseSentry` instead, which initializes Sentry and adds this logging integration for you:

* [Generic Host](https://docs.sentry.io/platforms/dotnet/guides/extensions-hosting.md), for worker services, Windows services and console apps that call `Host.CreateApplicationBuilder` or `Host.CreateDefaultBuilder`. Before 7.0.0, these apps initialized Sentry with `builder.Logging.AddSentry(...)` from this page.
* [ASP.NET Core](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md)
* [MAUI](https://docs.sentry.io/platforms/dotnet/guides/maui.md)

.NET Framework apps that call `Host.CreateApplicationBuilder()` can't use the Generic Host integration's `UseSentry`. See [.NET Framework](https://docs.sentry.io/platforms/dotnet/guides/extensions-hosting.md#net-framework) in the Generic Host guide.

Apps without a host initialize Sentry with `SentrySdk.Init`, then add the integration with `AddSentry()`:

```csharp
using Microsoft.Extensions.Logging;

using var sentry = SentrySdk.Init(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
});

using var loggerFactory = LoggerFactory.Create(builder => builder.AddSentry());
var logger = loggerFactory.CreateLogger<Program>();
```

*Other available variations of the above snippet: ServiceCollection*

Set other [SDK options](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/configuration/options.md) in `SentrySdk.Init` too. Disposing the object it returns sends any pending events before your app exits.

Every `ILogger` entry that passes your `Microsoft.Extensions.Logging` filters is also sent as a structured log. To send fewer, set `LogLevel` under `Logging:Sentry`, as shown in [Logging Configuration](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#logging-configuration), or return `null` from `SetBeforeSendLog`.

`AddSentry()` doesn't register `IHub`, `ISentryClient` or `Func<IHub>`. If your services inject them, register them with `HubAdapter.Instance`. Otherwise resolving those services fails with `Unable to resolve service for type 'Sentry.IHub'`:

```csharp
using Sentry.Extensibility;

services.AddSingleton<IHub>(HubAdapter.Instance);
services.AddSingleton<ISentryClient>(HubAdapter.Instance);
services.AddSingleton<Func<IHub>>(() => HubAdapter.Instance);
```

You only need the lines for the types your services inject.

##### Changed in Version 7.0.0

Prior to version 7.0.0, `AddSentry` could also initialize the SDK itself, registered `IHub` and `ISentryClient`, and only sent log entries as structured logs when `EnableLogs` was `true`. On those versions, set the DSN in `AddSentry(options => ...)` instead of calling `SentrySdk.Init`. To upgrade, see [Migrate from 6.x to 7.x](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/migration/v6-to-v7.md).

### [Logging Configuration](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#logging-configuration)

If you add your configuration to the logging builder, for example with `builder.AddConfiguration(configuration.GetSection("Logging"))`, the integration reads its settings from the `Logging:Sentry` section:

```json
{
  "Logging": {
    "Sentry": {
      "LogLevel": {
        "Default": "Information"
      },
      "MinimumBreadcrumbLevel": "Debug",
      "MinimumEventLevel": "Warning"
    }
  }
}
```

`LogLevel` controls which entries are sent as [structured logs](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging/logs.md). `MinimumBreadcrumbLevel` and `MinimumEventLevel` are described under [Options](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#options).

The `Logging:Sentry` section only accepts these three keys. Any other key, such as `Dsn` or `EnableLogs`, makes the app fail at startup. Set SDK options in `SentrySdk.Init`.

### [Options](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#options)

Set these in `AddSentry(options => ...)`. You can also set the two levels in the `Logging:Sentry` configuration section.

#### [MinimumBreadcrumbLevel](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#minimumbreadcrumblevel)

A `LogLevel` which indicates the minimum level a log message has to be included as a breadcrumb. By default this value is `Information`.

#### [MinimumEventLevel](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#minimumeventlevel)

A `LogLevel` which indicates the minimum level a log message has to be sent to Sentry as an event. By default this value is `Error`.

#### [Log Entry Filters](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#log-entry-filters)

Filters run before a log entry is processed. They get the entry's `Microsoft.Extensions.Logging` data, so you can drop the entry before it becomes a `Breadcrumb` or an `Event`. Return `true` to drop it:

```csharp
using Microsoft.Extensions.Logging;
using Sentry.Extensions.Logging;

using var loggerFactory = LoggerFactory.Create(builder => builder.AddSentry(options =>
{
    options.AddLogEntryFilter((category, level, eventId, exception) =>
        level < LogLevel.Critical && exception is DivideByZeroException);
}));
```

With a host integration, call `AddLogEntryFilter` on the options you pass to `UseSentry` instead.

##### Note

These filters only apply to breadcrumbs and events. They don't control which logs will be captured as structured logs in Sentry. That can be controlled independently using the [filtering capabilities built into `Microsoft.Extensions.Logging`](https://learn.microsoft.com/dotnet/core/extensions/logging/overview?tabs=command-line#how-filtering-rules-are-applied).

### [TagFilters](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#tagfilters)

`TagFilters` is an SDK option, so set it in `SentrySdk.Init`. It drops any tag set on the scope whose key contains one of its entries, including the tags this integration adds from `BeginScope` state. An entry can also be a `Regex`, such as `new Regex("^PROC_")` to match only keys that start with `PROC_`. For example, to drop tags whose key contains `PROC_`:

```csharp
options.TagFilters.Add("PROC_");
```

## [Verify](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#verify)

After creating a logger with one of the configurations above, send an informational log and an error to verify both providers:

```csharp
logger.LogInformation("Sentry logging verification");
logger.LogError("Sentry error-event verification");
```

Check **Logs** for the informational log and **Issues** for the error event. Run this code before disposing the logger factory or service provider.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md#samples)

* A [simple example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.ME.Logging) using simply the `LoggerFactory`.

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
- [Generic Host](https://docs.sentry.io/platforms/dotnet/guides/extensions-hosting.md)
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

