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

Without any code change, this package is able to initialize the Sentry SDK and capture events while including additional properties like `Exception` data and more.

Additionally, when enabled, log messages are sent to Sentry as [Structured Logs](https://docs.sentry.io/platforms/dotnet/guides/log4net/logs.md).

## [Install](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#install)

Add the Sentry dependency:

```powershell
Install-Package Sentry.Log4Net -Version 6.12.1
```

*Other available variations of the above snippet: .NET Core CLI*

This package extends `Sentry` main SDK. That means besides the log4net `Appender`, through this package you'll also get access to all API and features available in the main `Sentry` SDK.

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#configure)

Once the log4net integration package is installed in your project, you can modify your configuration file to add the appender. This can be done, for example, via the `app.config` for console and desktop apps or `web.config` in case of ASP.NET.

```xml
<appender
  name="SentryAppender"
  type="Sentry.Log4Net.SentryAppender, Sentry.Log4Net"
>
    <Dsn value="https://<key>@o<orgId>.ingest.sentry.io/<projectId>" />
    <!--Sends the log event Identity value as the user-->
    <SendIdentity value="true" />
    <threshold value="INFO" />
  </appender>
```

Only a subset of the options are exposed via the log4net appender configuration. If you wish to access an [SDK option](https://docs.sentry.io/platforms/dotnet/configuration/options.md) which is not listed below, you'll need to initialize the SDK via [SentrySdk.Init](https://docs.sentry.io/platforms/dotnet.md) instead of doing it via this integration as described below.

### [SendIdentity](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#sendidentity)

In the example above, the `SendIdentity` flag was switched on. The SDK then will take the log4net `Identity` value and report to Sentry as the user's id.

### [DSN](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#dsn)

Also in the example above, you can find the DSN being set. That will instruct the `SentryAppender` to initialize the SDK.

This is only one of the ways to initialize the SDK. If you wish to configure the SDK programmatically, you could **leave the DSN out** from the appender configuration section. The SDK needs to be initialized only **once** and since other integrations (like ASP.NET) are also able to initialize the SDK, you only need to pass the DSN to one of these integrations. One common case to not add the DSN to the XML configuration file (which would initialize it via the log4net integration) is to have full access to the [SDK option](https://docs.sentry.io/platforms/dotnet/guides/log4net/configuration/options.md).

## [Verify](https://docs.sentry.io/platforms/dotnet/guides/log4net.md#verify)

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

