---
title: "Serilog"
source: https://docs.sentry.io/platforms/dotnet/guides/serilog.md
path: platforms/dotnet/guides/serilog
---

---
title: "Serilog"
description: "Learn about Sentry's .NET integration with Serilog."
url: https://docs.sentry.io/platforms/dotnet/guides/serilog/
---

# Sentry for Serilog

Sentry provides an integration with `Serilog` through the [Sentry.Serilog NuGet package](https://www.nuget.org/packages/Sentry.Serilog).

## [Overview of the features](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#overview-of-the-features)

* Store log messages as breadcrumbs
* Send events to Sentry
* Send structured logs to Sentry

Two separate settings define the minimum log level to keep the log entry as a `Breadcrumb` and to send an `Event` to Sentry. The events include any stored breadcrumb on that [scope](https://docs.sentry.io/platforms/dotnet/guides/serilog/enriching-events/scopes.md).

By default, any message with log level `Information` or higher will be kept as a `Breadcrumb`.

The default value to report a log entry as an event to Sentry is `Error`.

This means that out of the box, any `Log.Error` call will create an `Event` which will include breadcrumbs for prior log messages of level `Information`, `Warning`, `Error`, and `Fatal`.

Additionally, when enabled, log messages are sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/serilog/logs.md). You can control which logs are captured using the [Serilog MinimumLogLevel](https://github.com/serilog/serilog/wiki/Configuration-Basics#minimum-level).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.Serilog -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means that besides the logging related features, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

##### Note

The integration excludes the Sentry SDK's own logger categories to avoid capturing its diagnostic messages as events. Application categories that happen to start with `Sentry` aren't excluded solely because of that prefix.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#configure)

If another integration already initializes Sentry, configure the Serilog sink without reinitializing the SDK. Enable `EnableLogs` on the options used by that integration to send structured logs.

```csharp
using Serilog;
using Serilog.Events;

Log.Logger = new LoggerConfiguration()
  .MinimumLevel.Debug()
  .WriteTo.Sentry(o =>
  {
    o.InitializeSdk = false;
    // Debug and higher are stored as breadcrumbs (default is Information)
    o.MinimumBreadcrumbLevel = LogEventLevel.Debug;
    // Warning and higher is sent as event (default is Error)
    o.MinimumEventLevel = LogEventLevel.Warning;
  })
  .CreateLogger();
```

*Other available variations of the above snippet: json*

When Serilog owns initialization, provide the DSN and enable structured logs in the sink configuration:

```csharp
Log.Logger = new LoggerConfiguration()
  .WriteTo.Sentry(o =>
  {
    o.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    o.EnableLogs = true;
  })
  .CreateLogger();
```

*Other available variations of the above snippet: json*

Initialize the SDK once. The C# callback overload defaults `InitializeSdk` to `true` and can resolve a DSN from `SENTRY_DSN`. Set `InitializeSdk = false` when another integration or `SentrySdk.Init` owns initialization. Omitting the DSN from that callback doesn't prevent reinitialization: it uses `SENTRY_DSN` if set and replaces the existing SDK configuration, and otherwise throws because no DSN was found.

The configuration-file overload infers initialization from its `dsn` argument. In the first JSON example, Sentry must already be initialized elsewhere; supplying `dsn`, as in the second example, enables initialization through the sink.

### [Options](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#options)

#### [MinimumBreadcrumbLevel](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#minimumbreadcrumblevel)

A `LogLevel` which indicates the minimum level a log message has to be included as a breadcrumb. By default this value is `Information`.

#### [MinimumEventLevel](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#minimumeventlevel)

A `LogLevel` which indicates the minimum level a log message has to be sent to Sentry as an event. By default this value is `Error`.

#### [InitializeSdk](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#initializesdk)

Whether or not this integration should initialize the SDK. If you intend to call `SentrySdk.Init` yourself you should set this flag to `false`.

#### [RestrictedToMinimumLevel](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#restrictedtominimumlevel)

`MinimumBreadcrumbLevel` and `MinimumEventLevel` determine what the sink does with a log event, but every log event the logger captures still reaches the sink. If your logger's minimum level is verbose — for example, because another sink writes debug logs to a file — you can use Serilog's [per-sink minimum level](https://github.com/serilog/serilog/wiki/Configuration-Basics#overriding-per-sink) to stop lower-level log events from reaching Sentry entirely.

By default this value is `Verbose`, meaning no log events are filtered out. Ignored when `LevelSwitch` is set.

##### Note

This also controls which log entries are sent to Sentry as [structured logs](https://docs.sentry.io/platforms/dotnet/guides/serilog/logs.md)

#### [LevelSwitch](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#levelswitch)

An optional `LoggingLevelSwitch` that allows the sink's minimum level to be changed at runtime.

## [Verify](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#verify)

After configuring Serilog, send an informational log and an error:

```csharp
Log.Information("Sentry logging verification");
Log.Error("Sentry error-event verification");
```

With `EnableLogs = true`, the informational message appears in **Logs**. The error message also creates an event in **Issues**. Call `Log.CloseAndFlush()` when your application exits to dispose the sink and flush pending data.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#samples)

* A [simple example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.Serilog).
* An [example with ASP.NET Core](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.Serilog).

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#next-steps)

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
- [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md)
- [NLog](https://docs.sentry.io/platforms/dotnet/guides/nlog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/serilog/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/serilog/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/serilog/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/serilog/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/serilog/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/serilog/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/serilog/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/serilog/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/serilog/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/serilog/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/serilog/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/serilog/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/serilog/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/serilog/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/serilog/legacy-sdk.md)

