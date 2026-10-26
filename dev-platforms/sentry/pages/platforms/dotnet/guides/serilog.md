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

This means that out of the box, any `LogError` call will create an `Event` which will include breadcrumbs for all prior log messages of level `Information`, `Warning`, `Error` and `Critical`.

Additionally, when enabled, log messages are sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/serilog/logs.md). You can control which logs are captured using the [Serilog MinimumLogLevel](https://github.com/serilog/serilog/wiki/Configuration-Basics#minimum-level).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.Serilog -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means that besides the logging related features, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

##### Note

Messages logged from assemblies with the name starting with `Sentry` will not generate events.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/serilog.md#configure)

You can configure the Sentry Serilog sink as follows:

```csharp
Log.Logger = new LoggerConfiguration()
  .WriteTo.Sentry(o =>
  {
    // Debug and higher are stored as breadcrumbs (default is Information)
    o.MinimumBreadcrumbLevel = LogEventLevel.Debug;
    // Warning and higher is sent as event (default is Error)
    o.MinimumEventLevel = LogEventLevel.Warning;
  })
  .CreateLogger();
```

*Other available variations of the above snippet: json*

It's also possible to initialize the SDK through the Serilog integration. This is useful when the Serilog is the only integration being used in your application. To initialize the Sentry SDK through the Serilog integration, provide it with the DSN:

```csharp
Log.Logger = new LoggerConfiguration()
  .WriteTo.Sentry(o => o.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>")
  .CreateLogger();
```

*Other available variations of the above snippet: json*

The SDK only needs to be initialized once. If a `DSN` is made available to this integration, by default it **will** initialize the SDK. If you do not wish to initialize the SDK via this integration, set the `InitializeSdk` flag to **false**. Not providing a DSN or leaving it as `null` instructs the integration not to initialize the SDK and unless another integration initializes it or you call `SentrySdk.Init`, the SDK will stay disabled.

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

This snippet includes an intentional error, so you can test that everything is working as soon as you set it up.

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

