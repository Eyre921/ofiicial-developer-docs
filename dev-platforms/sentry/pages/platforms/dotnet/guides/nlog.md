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

This means that out of the box, any `Error` call will create an `Event` which will include all log messages of level `Info`, `Warn` and also `Error` and `Critical`.

Additionally, when enabled, log messages are sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/nlog/logs.md).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.NLog -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means that besides the logging related features, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

##### Note

Messages logged from assemblies with the name starting with `Sentry` will not generate events.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#configure)

##### NLog Layouts

For more information on how to dynamically set event data via `NLog.config`, see NLog's [layout renderer documentation](https://nlog-project.org/config/?tab=layout-renderers).

You can configure the Sentry NLog target via code as follows:

```csharp
LogManager.Configuration = new LoggingConfiguration();
LogManager.Configuration
    .AddSentry(options =>
    {
        // Optionally specify a separate format for message
        options.Layout = "${message}";
        // Optionally specify a separate format for breadcrumbs
        options.BreadcrumbLayout = "${logger}: ${message}";

        // Debug and higher are stored as breadcrumbs (default is Info)
        options.MinimumBreadcrumbLevel = LogLevel.Debug;
        // Error and higher is sent as event (default is Error)
        options.MinimumEventLevel = LogLevel.Error;

        // Send the logger name as a tag
        options.AddTag("logger", "${logger}");

        // All Sentry Options are accessible here.
    });
```

It's also possible to initialize the SDK through the NLog integration (as opposed to using `SentrySdk.Init`). This is useful when NLog is the only integration being used in your application. To initialize the Sentry SDK through the NLog integration, provide it with the DSN:

```csharp
LogManager.Configuration = new LoggingConfiguration();
LogManager.Configuration
    .AddSentry(o =>
    {
        // The NLog integration will initialize the SDK if DSN is set:
        o.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    });
```

##### Note

The SDK needs to be initialized only once. If a `DSN` is made available to this integration, by default it **will** initialize the SDK. If you do not wish to initialize the SDK via this integration, set the `InitializeSdk` flag to **false**. Not providing a DSN or leaving it as `null` instructs the integration not to initialize the SDK and unless another integration initializes it or you call `SentrySdk.Init`, the SDK will stay disabled.

### [Minimum log level](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimum-log-level)

Two log levels are used to configure this integration (see options below). One will configure the lowest level required for a log message to become an event (`MinimumEventLevel`) sent to Sentry. The other option (`MinimumBreadcrumbLevel`) configures the lowest level a message has to be to become a breadcrumb. Breadcrumbs are kept in memory (by default the last 100 records) and are sent with events. For example, by default, if you log 100 entries with `logger.Info` or `logger.Warn`, no event is sent to Sentry. If you then log with `logger.Error`, an event is sent to Sentry which includes those 100 `Info` or `Warn` messages. For this to work, `SentryTarget` needs to receive **all** log entries in order to decide what to keep as breadcrumb or sent as event. Make sure to set the `NLog` `LogLevel` configuration to a value lower than what you set for the `MinimumBreadcrumbLevel` and `MinimumEventLevel` to make sure `SentryTarget` receives these log messages.

The SDK can also be configured via `NLog.config` XML file:

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
      dsn="https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
      layout="${message}"
      environment="Development"
      breadcrumbLayout="${message}"
      minimumBreadcrumbLevel="Debug"
      minimumEventLevel="Error"
    >

      <!-- Advanced options can be configured here-->
      <options
        sendDefaultPii="true"
        attachStacktrace="false"
        shutdownTimeoutSeconds="5"
        debug="false"
      >
        <!--Advanced options can be specified as attributes or elements-->
        <includeEventDataOnBreadcrumbs>true</includeEventDataOnBreadcrumbs>
      </options>

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

### [Options](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#options)

#### [MinimumBreadcrumbLevel](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimumbreadcrumblevel)

A `LogLevel` that indicates the minimum level a log message needs to be in order to become a breadcrumb. By default, this value is `Info`.

#### [MinimumEventLevel](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#minimumeventlevel)

A `LogLevel` which indicates the minimum level a log message has to be sent to Sentry as an event. By default this value is `Error`.

#### [InitializeSdk](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#initializesdk)

Whether or not this integration should initialize the SDK. If you intend to call `SentrySdk.Init` yourself you should set this flag to `false`.

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

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/nlog.md#samples)

* A [simple example](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.NLog).
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

