---
title: "Windows Forms"
source: https://docs.sentry.io/platforms/dotnet/guides/winforms.md
path: platforms/dotnet/guides/winforms
---

---
title: "Windows Forms"
description: "Learn how Sentry's .NET SDK works with WinForms applications."
url: https://docs.sentry.io/platforms/dotnet/guides/winforms/
---

# Sentry for Windows Forms

Sentry's .NET SDK works with WinForms applications through the [Sentry NuGet package](https://www.nuget.org/packages/Sentry). It works with WinForms apps running on .NET Framework 4.6.2, .NET Core 3.0, or higher.

## [Install](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#install)

Install the **NuGet** package to add the Sentry dependency:

```shell
dotnet add package Sentry -v 6.12.1
```

*Other available variations of the above snippet: Package Manager, Paket CLI*

## [Configure](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#configure)

**Error Monitoring** starts working as soon as you initialize the SDK. **Logs** sent through `SentrySdk.Logger` and **Application Metrics** need no extra configuration. You'll learn how to send them in [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#send-logs) and [Send Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#send-application-metrics-).

This guide also enables **Tracing**.

After adding the NuGet package, the SDK should be initialized in the program's main entry point, before launching any forms or performing significant work. The options for initialization vary by language.

### [C# Initialization](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#c-initialization)

A C# Windows Forms application will have a `Program.cs` file. You should initialize Sentry in this file.

You should also set `Application.SetUnhandledExceptionMode(UnhandledExceptionMode.ThrowException)` so Sentry can capture unhandled exceptions.

A complete example of the recommended startup is as follows:

The snippet also turns on:

* Tracing: via [`TracesSampleRate`](https://docs.sentry.io/platforms/dotnet/guides/winforms/configuration/options.md#TracesSampleRate)

Don't need a feature? Remove its options from the snippet.

```csharp
using System;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {

            // These WinForms options are usually set by default
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            // Add this so Sentry can catch unhandled exceptions
            Application.SetUnhandledExceptionMode(UnhandledExceptionMode.ThrowException);

            // Configure the options for Sentry
            var sentryOptions = new SentryOptions
            {
                // Tells which project in Sentry to send events to:
                Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

                // When configuring for the first time, to see what the SDK is doing:
                Debug = true,

                // Adds request URL and headers, IP and name for users, etc.
                SendDefaultPii = true,
                // Enables Tracing.
                // Set to 1.0 to capture 100% of spans for tracing.
                // We recommend reducing this value in production.
                TracesSampleRate = 1.0,
                // Enable Global Mode since this is a client app
                IsGlobalModeEnabled = true,

                //TODO: any other options you need go here
            };

            // Initialize Sentry and run the main form of the application
            using (SentrySdk.Init(sentryOptions))
            {
                Application.Run(new YourMainApplicationForm());
            }
        }
    }
}
```

### [Visual Basic Initialization](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#visual-basic-initialization)

Windows Forms applications written in VB have two different initialization options. Pick one of them (not both).

#### [Option 1](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#option-1)

You can initialize Sentry in a similar approach as shown above for C#.

First, modify the settings on the project properties page as follows:

* Clear the "Enable application framework" checkbox.
* Set the "Startup object" to "Sub Main".

Then, add the following file as `Program.vb`:

```vb
Imports Sentry

Module Program

    ''' <summary>
    ''' The main entry point for the application.
    ''' </summary>
    <STAThread>
    Sub Main()

        ' These WinForms options are usually set by default
        Application.EnableVisualStyles()
        Application.SetCompatibleTextRenderingDefault(False)

        ' Add this so Sentry can catch unhandled exceptions
        Application.SetUnhandledExceptionMode(UnhandledExceptionMode.ThrowException)

        ' Configure the options for Sentry
        Dim sentryOptions = New SentryOptions With
        {
            .Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

            ' Adds request URL and headers, IP and name for users, etc.
            .SendDefaultPii = True,

            ' Enable Global Mode since this is a client app
            .IsGlobalModeEnabled = True,

            ' any other options you need go here
        }

        ' Initialize Sentry and run the main form of the application
        Using SentrySdk.Init(sentryOptions)
            Application.Run(New YourMainApplicationForm)
        End Using
    End Sub

End Module
```

#### [Option 2](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#option-2)

If you prefer to keep the WinForms "Application Framework" feature enabled, then you can initialize Sentry in the "Application Events".

First, ensure the settings on the project properties page are as follows:

* The "Enable application framework" checkbox should be checked.
* The "Startup object" should be set to the name of your main form.

Next, you will need to modify the `ApplicationEvents.vb` file.

* If you are using .NET Framework, clicking the "View Application Events" button will create and open the `ApplicationEvents.vb` file.
* If you are using .NET Core, you will need to add the file manually.
* If you are using .NET 5 or higher, the file should already be present. If not, you can add it manually.

Once you have the file created:

* Initialize Sentry in the `Startup` event, and retain the result.
* Dispose Sentry in the `Shutdown` event, using the result from initialization.
* Use the `UnhandledException` event to send unhandled exceptions to sentry.

See the following complete example:

```vb
Imports Microsoft.VisualBasic.ApplicationServices
Imports Sentry
Imports Sentry.Protocol

Namespace My
    Partial Friend Class MyApplication

        Private _sentry As IDisposable

        Private Sub MyApplication_Startup(sender As Object, e As StartupEventArgs) Handles Me.Startup

            ' Configure the options for Sentry
            Dim sentryOptions = New SentryOptions With
            {
                .Dsn = "https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

                ' Adds request URL and headers, IP and name for users, etc.
                .SendDefaultPii = True,

                ' Enable Global Mode since this is a client app
                .IsGlobalModeEnabled = True,

                ' any other options you need go here
            }

            ' Initialize Sentry
            _sentry = SentrySdk.Init(sentryOptions)

        End Sub

        Private Sub MyApplication_Shutdown(sender As Object, e As EventArgs) Handles Me.Shutdown

            ' Dispose the Sentry SDK to ensure events are flushed and sent to Sentry
            _sentry.Dispose()

        End Sub

        Private Sub MyApplication_UnhandledException(sender As Object, e As UnhandledExceptionEventArgs) Handles Me.UnhandledException

            ' Set some additional data on the exception for Sentry to recognize this exception as unhandled
            Dim ex = e.Exception
            ex.Data(Mechanism.HandledKey) = False
            ex.Data(Mechanism.MechanismKey) = "WindowsFormsApplicationBase.UnhandledException"

            ' Capture the exception with Sentry
            SentrySdk.CaptureException(ex)

        End Sub

    End Class
End Namespace
```

## [Send Logs](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#send-logs)

Use `SentrySdk.Logger` to send logs at different levels. These logs are sent without an additional option.

See [Set Up Logs](https://docs.sentry.io/platforms/dotnet/guides/winforms/logs.md) for all available logging methods and formatting options.

```csharp
SentrySdk.Logger.LogInfo("Order processed");
SentrySdk.Logger.LogWarning("Rate limit reached for /api/orders");
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#send-application-metrics-)

Metrics are enabled by default in Sentry .NET SDK 6.1.0 and later. Use `SentrySdk.Metrics` to send counters, gauges, and distributions from your app.

See [Set Up Metrics](https://docs.sentry.io/platforms/dotnet/guides/winforms/metrics.md) for all available metric types and configuration options.

```csharp
SentrySdk.Metrics.EmitCounter("button_click", 5,
    new Dictionary<string, object> { ["browser"] = "Firefox" });
SentrySdk.Metrics.EmitGauge("page_load", 15.0, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["page"] = "/home" });
SentrySdk.Metrics.EmitDistribution("api_latency", 187, MeasurementUnit.Duration.Millisecond,
    new Dictionary<string, object> { ["endpoint"] = "/api/orders" });
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#verify-your-setup)

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

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#view-captured-data-in-sentry)

Open your Sentry project to view the captured event.

## [Resources](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#resources)

[Discussion on GitHub `Application.SetUnhandledExceptionMode`](https://github.com/getsentry/sentry-dotnet/issues/176)

## [Next Steps](https://docs.sentry.io/platforms/dotnet/guides/winforms.md#next-steps)

At this point, you should have integrated Sentry into your WinForms application. Here's what to explore next:

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
- [WinUI](https://docs.sentry.io/platforms/dotnet/guides/winui.md)
- [WPF](https://docs.sentry.io/platforms/dotnet/guides/wpf.md)
- [Xamarin](https://docs.sentry.io/platforms/dotnet/guides/xamarin.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/dotnet/guides/winforms/usage.md)
- [Enriching Events](https://docs.sentry.io/platforms/dotnet/guides/winforms/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/dotnet/guides/winforms/configuration.md)
- [Logs](https://docs.sentry.io/platforms/dotnet/guides/winforms/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dotnet/guides/winforms/metrics.md)
- [Data Management](https://docs.sentry.io/platforms/dotnet/guides/winforms/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/dotnet/guides/winforms/security-policy-reporting.md)
- [Tracing](https://docs.sentry.io/platforms/dotnet/guides/winforms/tracing.md)
- [Migration Guide](https://docs.sentry.io/platforms/dotnet/guides/winforms/migration.md)
- [Profiling](https://docs.sentry.io/platforms/dotnet/guides/winforms/profiling.md)
- [Crons](https://docs.sentry.io/platforms/dotnet/guides/winforms/crons.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dotnet/guides/winforms/troubleshooting.md)
- [Unit Testing](https://docs.sentry.io/platforms/dotnet/guides/winforms/unit-testing.md)
- [User Feedback](https://docs.sentry.io/platforms/dotnet/guides/winforms/user-feedback.md)
- [Legacy SDK](https://docs.sentry.io/platforms/dotnet/guides/winforms/legacy-sdk.md)

