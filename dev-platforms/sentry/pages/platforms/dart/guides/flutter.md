---
title: "Flutter"
source: https://docs.sentry.io/platforms/dart/guides/flutter.md
path: platforms/dart/guides/flutter
---

---
title: "Flutter"
description: "Learn how to set up Sentry in your Flutter app, capture your first events, and view them in Sentry."
url: https://docs.sentry.io/platforms/dart/guides/flutter/
---

# Sentry for Flutter

## Set up with Sentry CLI

Set up the Sentry Flutter SDK with the Sentry CLI. Install the CLI with one of these commands, then follow the Sentry CLI docs to finish setup.

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

## [Prerequisites](https://docs.sentry.io/platforms/dart/guides/flutter.md#prerequisites)

These instructions use Sentry Flutter SDK v10. You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* A Flutter application using **Flutter 3.44.0** and **Dart 3.12.0** or later
* **Android API 26** or later for Android apps. Set your app's `minSdk` to `26` or higher.
* **iOS 15.0** or **macOS 12.0** or later for Apple apps, with Swift Package Manager enabled

For an existing Sentry integration, review the [migration guide](https://docs.sentry.io/platforms/dart/guides/flutter/migration.md) before upgrading to v10.

## [Install](https://docs.sentry.io/platforms/dart/guides/flutter.md#install)

Sentry captures data by using an SDK within your application's runtime.

We recommend installing the SDK through our [Sentry Wizard](https://github.com/getsentry/sentry-wizard). Run one of the following commands inside your project directory:

**brew**

```bash
brew install getsentry/tools/sentry-wizard && sentry-wizard -i flutter
```

**Windows**

```powershell
$downloadUrl = "https://github.com/getsentry/sentry-wizard/releases/download/v9.1.0/sentry-wizard-win-x64.exe"
Invoke-WebRequest $downloadUrl -OutFile sentry-wizard.exe
./sentry-wizard.exe -i flutter
```

**macOS (Intel/x64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.1.0/sentry-wizard-darwin-x64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**macOS (Apple Silicon/arm64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.1.0/sentry-wizard-darwin-arm64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**Linux (x64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.1.0/sentry-wizard-linux-x64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**Linux (arm64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v9.1.0/sentry-wizard-linux-arm64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**npx**

```bash
npx @sentry/wizard@latest -i flutter
```

This will patch your project and configure the SDK. **Logs** and **Application Metrics** are enabled by default in SDK v10, and you'll learn how to send them in steps [#2](https://docs.sentry.io/platforms/dart/guides/flutter.md#send-logs) and [#3](https://docs.sentry.io/platforms/dart/guides/flutter.md#send-application-metrics-). You only need to patch the project once, then you can add the patched files to your version control system. If you prefer, you can also [set up the SDK manually](https://docs.sentry.io/platforms/dart/guides/flutter/manual-setup.md).

The following tasks will be performed by the Sentry Wizard

* Update your `pubspec.yaml` with the `sentry_flutter` and `sentry_dart_plugin` packages.
* Create a `sentry.properties` file (gitignored) with a Sentry CLI auth token.
* Prompt you for optional features and patch `main.dart` with `SentryFlutter.init`.
* Add a sample exception that is captured when the app starts so you can verify the setup.

## [Send Logs](https://docs.sentry.io/platforms/dart/guides/flutter.md#send-logs)

Call `Sentry.logger` from your application code after initialization to send structured logs at different levels. You can add attributes to make logs easier to search and filter.

See [Set Up Logs](https://docs.sentry.io/platforms/dart/guides/flutter/logs.md) for all available logging methods and message formatting.

```dart
Sentry.logger.info('Order completed', attributes: {
  'order_id': SentryAttribute.string('12345'),
  'total': SentryAttribute.double(99.99),
});

Sentry.logger.warn('Slow operation detected');
Sentry.logger.error('Validation failed');
```

If you use the Dart `logging` package, add the [`sentry_logging` integration](https://docs.sentry.io/platforms/dart/guides/flutter/integrations/logging.md) to send its records to Sentry.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dart/guides/flutter.md#send-application-metrics-)

Call `Sentry.metrics` from your application code after initialization to send counters, gauges, and distributions. Add attributes to filter and group metrics in Sentry.

See [Set Up Metrics](https://docs.sentry.io/platforms/dart/guides/flutter/metrics.md) for metric types, attributes, and configuration options.

```dart
Sentry.metrics.count('checkout.failed', 1);
Sentry.metrics.gauge('queue.depth', 42);
Sentry.metrics.distribution('api_latency', 187, unit: 'millisecond');
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dart/guides/flutter.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

The wizard added a sample exception to main.dart that is captured when the app starts. Run your app to send it to Sentry:

```bash
flutter run
```

After you've confirmed the issue in Sentry, remove the sample exception from `main.dart` so it isn't captured on every launch.

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dart/guides/flutter.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/dart/guides/flutter.md#next-steps)

At this point, you should have integrated Sentry into your Flutter application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Upload [debug symbols and source maps](https://docs.sentry.io/platforms/dart/guides/flutter/debug-symbols.md) for readable production stack traces. The wizard configures `sentry_dart_plugin`; run `dart run sentry_dart_plugin` after each production build to upload the files. In CI, provide `SENTRY_AUTH_TOKEN` to the upload step.
* Learn about [Session Replay](https://docs.sentry.io/platforms/dart/guides/flutter/session-replay.md) and its privacy controls
* Add [performance instrumentation](https://docs.sentry.io/platforms/dart/guides/flutter/tracing/instrumentation.md) to your app

Are you having problems setting up the SDK?

* If you encountered issues with the installation wizard, try [setting up Sentry manually](https://docs.sentry.io/platforms/dart/guides/flutter/manual-setup.md)
* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/dart/guides/flutter/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Topics

- [Features](https://docs.sentry.io/platforms/dart/guides/flutter/features.md)
- [Manual Setup](https://docs.sentry.io/platforms/dart/guides/flutter/manual-setup.md)
- [Basic Configuration](https://docs.sentry.io/platforms/dart/guides/flutter/configuration.md)
- [Usage](https://docs.sentry.io/platforms/dart/guides/flutter/usage.md)
- [Native Initialization](https://docs.sentry.io/platforms/dart/guides/flutter/native-init.md)
- [Integrations](https://docs.sentry.io/platforms/dart/guides/flutter/integrations.md)
- [Debug Symbols](https://docs.sentry.io/platforms/dart/guides/flutter/debug-symbols.md)
- [Enriching Events](https://docs.sentry.io/platforms/dart/guides/flutter/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/dart/guides/flutter/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/dart/guides/flutter/tracing.md)
- [Size Analysis](https://docs.sentry.io/platforms/dart/guides/flutter/size-analysis.md)
- [Build Distribution](https://docs.sentry.io/platforms/dart/guides/flutter/build-distribution.md)
- [Snapshots](https://docs.sentry.io/platforms/dart/guides/flutter/snapshots.md)
- [Session Replay](https://docs.sentry.io/platforms/dart/guides/flutter/session-replay.md)
- [Logs](https://docs.sentry.io/platforms/dart/guides/flutter/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dart/guides/flutter/metrics.md)
- [User Feedback](https://docs.sentry.io/platforms/dart/guides/flutter/user-feedback.md)
- [Mobile SDK Releases](https://docs.sentry.io/platforms/dart/guides/flutter/releases.md)
- [Set Up Feature Flags](https://docs.sentry.io/platforms/dart/guides/flutter/feature-flags.md)
- [SDK Overhead](https://docs.sentry.io/platforms/dart/guides/flutter/overhead.md)
- [Migration Guide](https://docs.sentry.io/platforms/dart/guides/flutter/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/dart/guides/flutter/troubleshooting.md)

