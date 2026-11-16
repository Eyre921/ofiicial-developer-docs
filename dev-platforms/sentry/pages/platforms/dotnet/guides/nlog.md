---
title: "NLog"
source: https://docs.sentry.io/platforms/dotnet/guides/nlog.md
path: platforms/dotnet/guides/nlog
---

---
title: "NLog"
description: "Learn about Sentry's .NET integration with NLog."
url: https://docs.sentry.io/platforms/dotnet/guides/nlog/
---

# Sentry for NLog

Sentry provides an integration with `NLog` through the [Sentry.NLog NuGet package](https://www.nuget.org/packages/Sentry.NLog).

## [Overview of the features](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#overview-of-the-features)

* Store log messages as breadcrumbs
* Send events to Sentry
* Send structured logs to Sentry

Two separate settings define the minimum log level to keep the log entry as a `Breadcrumb` and to send an `Event` to Sentry. The events include any stored breadcrumb on that [scope](https://docs.sentry.io/platforms/dotnet/guides/nlog/enriching-events/scopes.md).

By default, Sentry will keep any message with log level `Info` or higher as a `Breadcrumb`.

The default value to report a log entry as an event to Sentry is `Error`.

This means that out of the box, any `Error` call will create an `Event` which will include all log messages of level `Info`, `Warn`, `Error`, and `Fatal` stored as breadcrumbs.

Log messages at `Info` or higher are also sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/nlog/logs.md). Set [`MinimumLogLevel`](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimumloglevel) to change that level.

## [Install](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.NLog -Version 7.0.0
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means that besides the logging related features, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#configure)

##### NLog Layouts

For more information on how to dynamically set event data via `NLog.config`, see NLog's [layout renderer documentation](https://nlog-project.org/config/?tab=layout-renderers).

Initialize Sentry first, with `SentrySdk.Init` or a host integration such as [ASP.NET Core](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md), then add the target. You can add it in code:

```csharp
using NLog;
using NLog.Config;

SentrySdk.Init(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
});

var config = new LoggingConfiguration();
config.AddSentry(options =>
{
    // Optionally specify a separate format for message
    options.Layout = "${message}";
    // Optionally specify a separate format for breadcrumbs
    options.BreadcrumbLayout = "${logger}: ${message}";

    // Debug and higher are stored as breadcrumbs (default is Info)
    options.MinimumBreadcrumbLevel = LogLevel.Debug;
    // Error and higher is sent as event (default is Error)
    options.MinimumEventLevel = LogLevel.Error;
    // Info and higher are sent as logs (default is Info)
    options.MinimumLogLevel = LogLevel.Info;

    // Send the logger name as a tag
    options.AddTag("logger", "${logger}");
});
LogManager.Configuration = config;
```

The target drops log events while Sentry isn't initialized. If a DSN can be found anyway, for example in the `SENTRY_DSN` environment variable, the target also writes a warning to standard error the first time it drops an event. To fix it, initialize Sentry at startup as shown above.

### [Minimum log level](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimum-log-level)

Three log levels configure this integration. See [Options](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#options) below. `MinimumEventLevel` is the lowest level for a log message to become an event sent to Sentry. `MinimumBreadcrumbLevel` is the lowest level for a message to become a breadcrumb. `MinimumLogLevel` is the lowest level for a message to be sent as a structured log. Breadcrumbs are kept in memory, by default the last 100 records, and are sent with events. For example, by default, if you log 100 entries with `logger.Info` or `logger.Warn`, no event is sent to Sentry. If you then log with `logger.Error`, an event is sent to Sentry which includes those 100 `Info` or `Warn` messages. For this to work, `SentryTarget` needs to receive **all** log entries in order to decide what to keep as breadcrumb or sent as event. `AddSentry` adds a rule that passes the target every entry at the lowest of the three levels or higher. If you write the rule yourself, for example in `NLog.config`, make sure its minimum level isn't higher than `MinimumBreadcrumbLevel`, `MinimumEventLevel` or `MinimumLogLevel`, so `SentryTarget` receives these log messages.

The target can also be configured in an `NLog.config` XML file:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<nlog
  xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>
  <extensions>
    <add assembly="Sentry.NLog" />
  </extensions>

  <targets>
    <target
      xsi:type="Sentry"
      name="sentry"
      layout="${message}"
      breadcrumbLayout="${message}"
      minimumBreadcrumbLevel="Debug"
      minimumEventLevel="Error"
      minimumLogLevel="Info"
      includeEventDataOnBreadcrumbs="true"
    >

      <!--Optionally add any desired additional Tags that will be sent with every message -->
      <tag
        name="exception"
        layout="${exception:format=shorttype}"
        includeEmptyValue="false"
      />

      <!--Optionally add any desired additional Data that will be sent with every message -->
      <contextproperty
        name="threadid"
        layout="${threadid}"
        includeEmptyValue="true"
      />
    </target>
  </targets>

  <rules>
    <logger name="*" writeTo="sentry" />
  </rules>
</nlog>
```

### [Apps That Call UseSentry](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#apps-that-call-usesentry)

In an app that calls `UseSentry`, add NLog with `AddNLog` from the `NLog.Extensions.Logging` package, and set `ReplaceLoggerFactory`:

```csharp
using NLog;
using NLog.Config;
using NLog.Extensions.Logging;

var config = new LoggingConfiguration();
config.AddSentry();
LogManager.Configuration = config;

builder.Logging.AddNLog(new NLogProviderOptions { ReplaceLoggerFactory = true });
builder.UseSentry(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
});
```

`ReplaceLoggerFactory` replaces the app's `ILogger` factory with NLog's, so each `ILogger` entry reaches Sentry once, through the target. Without it, NLog runs alongside the `ILogger` integration that `UseSentry` adds, and Sentry receives every entry twice. NLog's rules then decide which entries are logged, instead of the `Logging` section of your configuration. The target sends entries at `Info` or higher to Sentry as logs. To change that level, set [`MinimumLogLevel`](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimumloglevel). In ASP.NET Core, `UseNLog` from the `NLog.Web.AspNetCore` package takes the same option.

### [Capturing Startup Crashes](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#capturing-startup-crashes)

`UseSentry` starts Sentry when the host is built or, in ASP.NET Core, when the app starts running. If the app crashes before then, for example while it reads configuration or registers services, the crash isn't sent.

To send these crashes, also call `SentrySdk.Init` before you create the builder, and log the crash if startup fails:

```csharp
using NLog;
using NLog.Config;
using NLog.Extensions.Logging;

using var sentry = SentrySdk.Init(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
});

var config = new LoggingConfiguration();
config.AddSentry();
LogManager.Configuration = config;
var logger = LogManager.GetCurrentClassLogger();

try
{
    var builder = WebApplication.CreateBuilder(args);
    builder.Logging.AddNLog(new NLogProviderOptions { ReplaceLoggerFactory = true });
    builder.UseSentry(options =>
    {
        options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    });

    var app = builder.Build();
    app.Run();
}
catch (Exception ex)
{
    logger.Fatal(ex, "Application terminated unexpectedly");
    throw;
}
finally
{
    LogManager.Shutdown();
}
```

The two initializations don't share anything:

* `SentrySdk.Init` runs before the app reads `appsettings.json`, so set its DSN in code or with the `SENTRY_DSN` environment variable.
* `UseSentry` doesn't reuse those options. Give it a DSN as well, in its callback or the `Sentry` section.
* Once `UseSentry` starts Sentry, it replaces the first initialization. Crashes before then are sent with the first initialization's options, such as its release and environment. Breadcrumbs logged before then aren't carried over.
* Crashes after then, such as a port that's already in use, are sent by `UseSentry`. `logger.Fatal` doesn't send them a second time.

### [Options](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#options)

#### [MinimumBreadcrumbLevel](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimumbreadcrumblevel)

A `LogLevel` that indicates the minimum level a log message needs to be in order to become a breadcrumb. By default, this value is `Info`.

#### [MinimumEventLevel](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimumeventlevel)

A `LogLevel` which indicates the minimum level a log message has to be sent to Sentry as an event. By default this value is `Error`.

#### [MinimumLogLevel](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimumloglevel)

A `LogLevel` which indicates the minimum level a log message needs to be sent to Sentry as a structured log. By default this value is `Info`. Set it to `Off` to send no logs.

#### [IgnoreEventsWithNoException](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#ignoreeventswithnoexception)

To ignore log messages that don't contain an exception.

#### [IncludeEventProperties](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#includeeventproperties)

Determines whether event-level properties will be sent to Sentry as additional data. Defaults to true.

#### [IncludeEventPropertiesAsTags](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#includeeventpropertiesastags)

Determines whether event properties will be sent to Sentry as Tags or not. Defaults to false.

#### [IncludeEventDataOnBreadcrumbs](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#includeeventdataonbreadcrumbs)

Determines whether or not to include event-level data as data in breadcrumbs for future errors. Defaults to false.

#### [BreadcrumbLayout](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#breadcrumblayout)

Custom layout for breadcrumbs. See [NLog layout renderers](https://nlog-project.org/config/?tab=layout-renderers) for more.

#### [Layout](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#layout)

Layout used to render the message of events sent to Sentry. Defaults to `${message}`.

#### [Tags](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#tags)

Any additional tags to apply to each logged message. Tag values can use NLog layouts.

#### [User](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#user)

You can provide a `user` entry matching the following example user. See [Identify Users](https://docs.sentry.io/platforms/dotnet/guides/nlog/enriching-events/identify-user.md) for more information.

```xml
<user
  id="sample_id"
  username="sample_username"
  email="sample@email.com"
  ipAddress="127.0.0.1"
>
 <other name="mood" layout="joyous" />
</user>
```

## [Verify](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#verify)

After configuring NLog, send an informational log and an error:

```csharp
var logger = LogManager.GetCurrentClassLogger();
logger.Info("Sentry logging verification");
logger.Error("Sentry error-event verification");
LogManager.Flush();
```

The informational message appears in **Logs**. The error message also creates an event in **Issues**. Call `LogManager.Shutdown()` when your application exits to dispose the target and flush pending data.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#samples)

* A [simple example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.NLog).
* An [example with ASP.NET Core](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.AspNetCore.NLog).
* Example of [advanced configuration](https://docs.sentry.io/platforms/dotnet/guides/nlog/configuration/advanced-configuration-example.md)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#next-steps)

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
- [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md)
- [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/nlog/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/nlog/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/nlog/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/nlog/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/nlog/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/nlog/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/nlog/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/nlog/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/nlog/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/nlog/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/nlog/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/nlog/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/nlog/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/nlog/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/nlog/legacy-sdk.md)

