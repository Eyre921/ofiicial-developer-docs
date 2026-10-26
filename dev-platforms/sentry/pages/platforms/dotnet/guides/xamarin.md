---
title: "Xamarin"
source: https://docs.sentry.io/platforms/dotnet/guides/xamarin.md
path: platforms/dotnet/guides/xamarin
---

---
title: "Xamarin"
description: "Learn more about how Sentry's .NET SDK works with Xamarin applications."
url: https://docs.sentry.io/platforms/dotnet/guides/xamarin/
---

# Sentry for Xamarin

Sentry's .NET SDK works with Xamarin applications through the [Sentry Xamarin NuGet package](https://www.nuget.org/packages/Sentry.Xamarin) and Xamarin Forms with the [Sentry Xamarin Forms NuGet package](https://www.nuget.org/packages/Sentry.Xamarin.Forms).

The SDK is compatible with the following versions or higher:

* Xamarin.Android 9.0
* Xamarin.iOS 10.14
* Universal Windows Platform 10.0.16299
* Tizen 4.0

## [Install](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#install)

Install the **NuGet** package:

```shell
# For Xamarin.Forms
Install-Package Sentry.Xamarin.Forms -Version 2.1.0

# If you are not using Xamarin.Forms, but only Xamarin:
Install-Package Sentry.Xamarin -Version 2.1.0
```

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK.

This guide also enables **Tracing**.

After you've completed setting up a project in Sentry, Sentry will give you a value which we call a DSN or Data Source Name. It looks a lot like a standard URL, but it's just a representation of the configuration required by the Sentry SDK. It consists of a few pieces, including the protocol, public key, the server address, and the project identifier. You should initialize the SDK as early as possible, for an example, the start of OnCreate on MainActivity for Android, and, the top of FinishedLaunching on AppDelegate for iOS).

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/xamarin/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```csharp
SentryXamarin.Init(options =>
{
    options.AddXamarinFormsIntegration();
    // Tells which project in Sentry to send events to:
    options.Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>";
    // When configuring for the first time, to see what the SDK is doing:
    options.Debug = true;
    // Adds request URL and headers, IP and name for users, etc.
    options.SendDefaultPii = true;
    // Enables Tracing.
    // Set to 1.0 to capture 100% of spans for tracing.
    // We recommend reducing this value in production.
    options.TracesSampleRate = 1.0;
});
// App code
```

### [Xamarin Options](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#xamarin-options)

The following options are only going to be valid during the SDK initialization.

#### [DisableNativeIntegration](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#disablenativeintegration)

Disable the native event processor for Android,iOS,UWP

#### [DisableOfflineCaching](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#disableofflinecaching)

By calling it, the SDK will not automatically Cache your events and they might be lost if a hard crash happens or no connectivity is available during the transport of the event.

#### [AttachScreenshots](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#attachscreenshots)

Automatically attaches a screenshot of the app at the time of the event capture. By default, it is set to false.

##### Note

Note that personally identifiable information (PII) might be included in the screenshot when you activate this feature.

### [Xamarin Forms Options](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#xamarin-forms-options)

#### [DisableXamarinWarningsBreadcrumbs](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#disablexamarinwarningsbreadcrumbs)

Disables the automatic Logging of internal Warnings that comes from Xamarin Forms.

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

You can verify Sentry is capturing unhandled exceptions by raising an exception. For example, you can use the following snippet to raise a `NullReferenceException`:

```csharp
throw null;
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#troubleshooting)

For information about Troubleshooting, please visit the [troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/xamarin/troubleshooting.md) page.

## [Samples](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#samples)

* An [example](https://github.com/getsentry/sentry-xamarin/tree/main/Samples) using Xamarin Forms and most of the SDK features. (**Android, iOS, UWP**)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md#next-steps)

At this point, you should have integrated Sentry into your Xamarin application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/dotnet/usage.md)
* Explore [Tracing](https://docs.sentry.io/platforms/dotnet/tracing.md)

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
- [Serilog](https://docs.sentry.io/platforms/dotnet/guides/serilog.md)
- [Windows Forms](https://docs.sentry.io/platforms/dotnet/guides/winforms.md)
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/xamarin/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/xamarin/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/xamarin/configuration.md)
- [Ignoring Exceptions](https://docs.sentry.io/platforms/dotnet/guides/xamarin/ignoring-exceptions.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/xamarin/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/xamarin/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/xamarin/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/xamarin/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/xamarin/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/xamarin/crons.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/xamarin/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/xamarin/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/xamarin/legacy-sdk.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/xamarin/troubleshooting.md)

