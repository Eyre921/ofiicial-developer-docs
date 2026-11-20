---
title: "Android"
source: https://docs.sentry.io/platforms/android.md
path: platforms/android
---

---
title: "Android"
description: "Learn how to set up Sentry's Android SDK, capture your first events, and monitor performance."
url: https://docs.sentry.io/platforms/android/
---

# Sentry for Android

## Set up with Sentry CLI

Set up the Sentry Android SDK with the Sentry CLI. Install the CLI with one of these commands, then follow the Sentry CLI docs to finish setup.

**cURL**

```bash
curl https://cli.sentry.dev/install -fsS | bash
```

**PowerShell**

```powershell
irm https://cli.sentry.dev/install.ps1 | iex
```

**Homebrew**

```bash
brew install getsentry/tools/sentry
```

**npx**

```bash
npx sentry@latest
```

[Learn more about the Sentry CLI](https://cli.sentry.dev/)

## [Prerequisites](https://docs.sentry.io/platforms/android.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Android 5.0 (API level 21) or higher
  * Session Replay requires at least Android 8.0 (API level 26)

## [Install](https://docs.sentry.io/platforms/android.md#install)

We recommend installing the SDK through our [Sentry Wizard](https://github.com/getsentry/sentry-wizard) by running one of the following commands inside your project directory:

**brew**

```bash
brew install getsentry/tools/sentry-wizard && sentry-wizard -i android
```

**npx**

```bash
npx @sentry/wizard@latest -i android
```

**macOS (Intel/x64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.0.0/sentry-wizard-darwin-x64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i android
```

**macOS (Apple Silicon/arm64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.0.0/sentry-wizard-darwin-arm64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i android
```

**Linux (x64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.0.0/sentry-wizard-linux-x64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i android
```

**Linux (arm64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.0.0/sentry-wizard-linux-arm64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i android
```

**Windows**

```powershell
$downloadUrl = "https://github.com/getsentry/sentry-wizard/releases/download/v9.0.0/sentry-wizard-win-x64.exe"
Invoke-WebRequest $downloadUrl -OutFile sentry-wizard.exe
./sentry-wizard.exe -i android
```

This will patch your project and configure the SDK. You only need to patch the project once, then you can add the patched files to your version control system.

Prefer to set things up yourself? Check out the [Manual Setup guide](https://docs.sentry.io/platforms/android/manual-setup.md).

The following tasks will be performed by the Sentry Wizard

The wizard will prompt you to log in to Sentry. It'll then automatically do the following steps for you:

* Update your app's `build.gradle` file with the Sentry Gradle plugin and configure it
* Update your `AndroidManifest.xml` with your DSN, tracing, user-interaction tracing, screenshots, view hierarchies, and default PII collection
* Ask whether to enable automatic Logs collection
* Create `sentry.properties` with an auth token to upload proguard mappings (this file is automatically added to `.gitignore`)
* Add an example error to your app's Main Activity to verify your Sentry setup

The wizard does not enable Profiling or Session Replay. Follow [Additional Configuration](https://docs.sentry.io/platforms/android.md#additional-configuration) to add them and adjust the generated configuration, including [data collection](https://docs.sentry.io/platforms/android/data-management/data-collected.md).

## [Additional Configuration](https://docs.sentry.io/platforms/android.md#additional-configuration)

**Error Monitoring** starts working as soon as you initialize the SDK. You can also send **Logs** and **Application Metrics** after initialization, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/android.md#send-logs) and [#4](https://docs.sentry.io/platforms/android.md#send-application-metrics-). The configuration below also enables **Tracing**, **Profiling**, and **Session Replay**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

- [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
- [**Tracing**](https://docs.sentry.io/product/tracing.md): Follow app starts, screen loads, and requests to see where they fail or slow down.
- [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
- [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
- [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
- [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

Use SDK version **8.58.0 or later** for the full configuration below.

The SDK initializes automatically using your application's `AndroidManifest.xml`. If you ran the wizard, update the existing Sentry entries and add the missing options from the snippet below. Keep a single `io.sentry.dsn` entry.

The snippet also turns on:

* Data Collection: via [`data-collection`](https://docs.sentry.io/platforms/android/configuration/options.md#dataCollection)
* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/android/configuration/options.md#tracesSampleRate)
* Profiling: via [`profileSessionSampleRate`](https://docs.sentry.io/platforms/android/configuration/options.md#profileSessionSampleRate) and [`profileLifecycle`](https://docs.sentry.io/platforms/android/configuration/options.md#profileLifecycle)
* Session Replay: via `sessionSampleRate` and `onErrorSampleRate` in the [Session Replay configuration](https://docs.sentry.io/platforms/android/session-replay/configuration.md#general-configuration)
* Logs: via [`logs.enabled`](https://docs.sentry.io/platforms/android/logs.md)

Don't need a feature? Remove its options from your app's manifest. The `trace` profiling lifecycle requires tracing: if you disable tracing, also remove the profiling options or [configure manual profiling](https://docs.sentry.io/platforms/android/profiling.md#enabling-manual-lifecycle-ui-profiling).

```xml
<application>
  <!-- Required: set your sentry.io project identifier (DSN) -->
  <meta-data
    android:name="io.sentry.dsn"
    android:value="https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
  />
  <!-- Use Data Collection defaults but don't collect automatic user information. -->
  <meta-data
    android:name="io.sentry.data-collection.user-info"
    android:value="false"
  />

  <!-- Enables Tracing. -->
  <!-- Set to 1.0 to capture 100% of transactions. -->
  <!-- We recommend reducing this value in production. -->
  <meta-data
    android:name="io.sentry.traces.sample-rate"
    android:value="1.0"
  />

  <!-- Enables Profiling while sampled traces are active. -->
  <!-- Sampling is evaluated once per session. Reduce this value in production. -->
  <meta-data
    android:name="io.sentry.traces.profiling.session-sample-rate"
    android:value="1.0"
  />
  <meta-data
    android:name="io.sentry.traces.profiling.lifecycle"
    android:value="trace"
  />

  <!-- Captures replays for 10% of sessions and 100% of sessions with errors. -->
  <meta-data
    android:name="io.sentry.session-replay.on-error-sample-rate"
    android:value="1.0"
  />
  <meta-data
    android:name="io.sentry.session-replay.session-sample-rate"
    android:value="0.1"
  />

  <!-- Enables automatic Logs collection through Timber and Logcat integrations. -->
  <meta-data android:name="io.sentry.logs.enabled" android:value="true" />
</application>
```

##### A note on Profiling

Starting with SDK version 8.51.0, profiling on Android 15 (API level 35) and higher uses the Android [ProfilingManager](https://developer.android.com/reference/android/os/ProfilingManager) to capture [Perfetto](https://perfetto.dev/) traces. On older devices, the SDK automatically falls back to the [legacy profiler](https://docs.sentry.io/platforms/android/profiling/legacy.md).

### [Configure the Sentry Android Gradle Plugin](https://docs.sentry.io/platforms/android.md#configure-the-sentry-android-gradle-plugin)

The Sentry Wizard configures the Gradle plugin, which supports automatic tracing instrumentation and uploads ProGuard/R8 mappings and source context. For manual setup, see the [Gradle plugin](https://docs.sentry.io/platforms/android/configuration/gradle.md), [ProGuard/R8](https://docs.sentry.io/platforms/android/enhance-errors/proguard.md), and [source context](https://docs.sentry.io/platforms/android/enhance-errors/source-context.md) guides.

## [Send Logs](https://docs.sentry.io/platforms/android.md#send-logs)

After SDK initialization, use `Sentry.logger()` to send log messages at different levels, such as `info`, `warn`, or `error`. You can pass any attributes you want and search or filter by them later.

See [Set Up Logs](https://docs.sentry.io/platforms/android/logs.md) for all available logging methods and configuration options.

```java
import io.sentry.Sentry;
import io.sentry.SentryAttribute;
import io.sentry.SentryAttributes;
import io.sentry.SentryLogLevel;
import io.sentry.logger.SentryLogParameters;

Sentry.logger().info("Order processed");
Sentry.logger().error("Payment failed");

Sentry.logger().log(
    SentryLogLevel.FATAL,
    SentryLogParameters.create(
        SentryAttributes.of(
            SentryAttribute.stringAttribute("my.string-attribute", "some-value"),
            SentryAttribute.named("my.attribute", new Point(1, 2))
        )
    ),
    "log message %s",
    "param1"
);
```

*Other available variations of the above snippet: Kotlin*

We also provide integrations for:

* [Timber](https://docs.sentry.io/platforms/android/integrations/timber.md)
* [Logcat](https://docs.sentry.io/platforms/android/integrations/logcat.md)

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/android.md#send-application-metrics-)

Use `Sentry.metrics()` to send counters, gauges, and distributions from your app. Add attributes to search and filter metrics later.

See [Set Up Metrics](https://docs.sentry.io/platforms/android/metrics.md) for all available metric types and configuration options.

```java
import io.sentry.Sentry;
import io.sentry.SentryAttribute;
import io.sentry.SentryAttributes;
import io.sentry.metrics.MetricsUnit;
import io.sentry.metrics.SentryMetricsParameters;

Sentry.metrics().count("button_click", 1.0);
Sentry.metrics().gauge("queue_depth", 42.0);

Sentry.metrics().distribution(
  "response_time",
  1.0,
  MetricsUnit.Duration.MILLISECOND,
  SentryMetricsParameters.create(
    SentryAttributes.of(
      SentryAttribute.stringAttribute("browser", "Firefox")
    )
  )
);
```

*Other available variations of the above snippet: Kotlin*

## [Verify Your Setup](https://docs.sentry.io/platforms/android.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Trigger and capture a test error in your application:

```java
import io.sentry.Sentry;

Sentry.captureException(new Exception("This is a test."));
```

*Other available variations of the above snippet: Kotlin*

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/android.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

- [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
- [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
- [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
- [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
- [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
- [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

## [Next Steps](https://docs.sentry.io/platforms/android.md#next-steps)

At this point, you should have integrated Sentry into your Android application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Enhance stack traces](https://docs.sentry.io/platforms/android/enhance-errors.md) to make error details more readable
* [Collect User Feedback](https://docs.sentry.io/platforms/android/user-feedback.md) from your users

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/android/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Topics

- [Features](https://docs.sentry.io/platforms/android/features.md)
- [Manual Setup](https://docs.sentry.io/platforms/android/manual-setup.md)
- [Extended Configuration](https://docs.sentry.io/platforms/android/configuration.md)
- [Capturing Errors](https://docs.sentry.io/platforms/android/usage.md)
- [Enhance Error Reporting](https://docs.sentry.io/platforms/android/enhance-errors.md)
- [Integrations](https://docs.sentry.io/platforms/android/integrations.md)
- [Enriching Events](https://docs.sentry.io/platforms/android/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/android/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/android/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/android/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/android/profiling.md)
- [Size Analysis](https://docs.sentry.io/platforms/android/size-analysis.md)
- [Build Distribution](https://docs.sentry.io/platforms/android/build-distribution.md)
- [Snapshots](https://docs.sentry.io/platforms/android/snapshots.md)
- [Session Replay](https://docs.sentry.io/platforms/android/session-replay.md)
- [Logs](https://docs.sentry.io/platforms/android/logs.md)
- [User Feedback](https://docs.sentry.io/platforms/android/user-feedback.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/android/releases.md)
- [Feature Flags](https://docs.sentry.io/platforms/android/feature-flags.md)
- [SDK Overhead](https://docs.sentry.io/platforms/android/overhead.md)
- [Migration Guide](https://docs.sentry.io/platforms/android/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/android/troubleshooting.md)

