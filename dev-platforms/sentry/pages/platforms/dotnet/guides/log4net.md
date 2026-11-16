---
title: "log4net"
source: https://docs.sentry.io/platforms/dotnet/guides/log4net.md
path: platforms/dotnet/guides/log4net
---

---
title: "log4net"
description: "Learn about Sentry's .NET integration with log4net."
url: https://docs.sentry.io/platforms/dotnet/guides/log4net/
---

# Sentry for log4net

Sentry provides an integration with log4net through the [Sentry.Log4Net NuGet package](https://www.nuget.org/packages/Sentry.Log4Net).

The `SentryAppender` captures log events as Sentry events and breadcrumbs, including additional properties like `Exception` data and more.

Log messages are also sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/log4net/logs.md).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.Log4Net -Version 7.0.0
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means besides the log4net `Appender`, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#configure)

Initialize Sentry first, with `SentrySdk.Init` or a host integration such as [ASP.NET Core](https://docs.sentry.io/platforms/dotnet/guides/aspnetcore.md):

```csharp
SentrySdk.Init(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
});
```

Then add the appender to your log4net configuration. This can be done, for example, via the `app.config` for console and desktop apps or `web.config` in case of ASP.NET.

```xml
<appender
  name="SentryAppender"
  type="Sentry.Log4Net.SentryAppender, Sentry.Log4Net"
>
    <!--Sends the log event Identity value as the user-->
    <SendIdentity value="true" />
    <!--Sends Error and higher as events, and adds lower levels as breadcrumbs-->
    <MinimumEventLevel value="ERROR" />
    <threshold value="INFO" />
  </appender>
```

Other [SDK options](https://docs.sentry.io/platforms/dotnet/guides/log4net/configuration/options.md) can also be configured when calling `SentrySdk.Init`.

The appender drops log events while Sentry isn't initialized. If a DSN can be found anyway, for example in the `SENTRY_DSN` environment variable, the appender also writes a warning to standard error the first time it drops an event. To fix it, initialize Sentry at startup as shown above.

### [Apps That Call UseSentry](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#apps-that-call-usesentry)

If an app that calls `UseSentry` also sends `ILogger` entries to log4net, for example with `AddLog4Net()` from the `Microsoft.Extensions.Logging.Log4Net.AspNetCore` package, both the appender and the `ILogger` integration that `UseSentry` adds capture each entry. Turn off events and breadcrumbs from the `ILogger` integration and leave `EnableLogs` off, so each entry reaches Sentry once, through the appender:

```csharp
builder.UseSentry(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    options.MinimumBreadcrumbLevel = LogLevel.None;
    options.MinimumEventLevel = LogLevel.None;
});
```

### [Capturing Startup Crashes](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#capturing-startup-crashes)

`UseSentry` starts Sentry when the host is built or, in ASP.NET Core, when the app starts running. If the app crashes before then, the appender drops the crash.

To send these crashes, also call `SentrySdk.Init` before you create the builder, and log the crash if startup fails:

```csharp
using log4net;

using var sentry = SentrySdk.Init(options =>
{
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
});

var logger = LogManager.GetLogger(typeof(Program));

try
{
    var builder = WebApplication.CreateBuilder(args);
    builder.UseSentry(options =>
    {
        options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    });

    var app = builder.Build();
    app.Run();
}
catch (Exception ex)
{
    logger.Fatal("Application terminated unexpectedly", ex);
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

### [SendIdentity](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#sendidentity)

In the example above, the `SendIdentity` flag was switched on. The SDK then will take the log4net `Identity` value and report to Sentry as the user's id.

## [Verify](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#verify)

Ensure log4net loads your configuration and the appender is referenced by a logger. For example, add this inside your `<log4net>` element alongside the appender:

```xml
<root>
  <level value="INFO" />
  <appender-ref ref="SentryAppender" />
</root>
```

After initializing Sentry, run this code to verify error capture:

```csharp
using System;
using log4net;
using log4net.Config;
using Sentry;

XmlConfigurator.Configure();
var logger = LogManager.GetLogger("SentryVerification");

try
{
    throw new InvalidOperationException("Sentry log4net verification");
}
catch (Exception exception)
{
    logger.Error("Sentry error-event verification", exception);
}

SentrySdk.FlushAsync().GetAwaiter().GetResult();
```

Check **Issues** for the error event and **Logs** for the log entry.

## [Sample](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#sample)

For a [sample app.config](https://github.com/getsentry/sentry-dotnet/blob/main/samples/Sentry.Samples.Log4Net/app.config) or a complete working [sample](https://github.com/getsentry/sentry-dotnet/tree/main/samples/Sentry.Samples.Log4Net) to see it in action.

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#next-steps)

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
- [MAUI](https://docs.sentry.io/platforms/dotnet/guides/maui.md)
- [Microsoft.Extensions.Logging](https://docs.sentry.io/platforms/dotnet/guides/extensions-logging.md)
- [NLog](https://docs.sentry.io/platforms/dotnet/guides/nlog.md)
- [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/log4net/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/log4net/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/log4net/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/log4net/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/log4net/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/log4net/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/log4net/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/log4net/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/log4net/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/log4net/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/log4net/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/log4net/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/log4net/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/log4net/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/log4net/legacy-sdk.md)

