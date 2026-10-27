---
title: "Flutter"
source: https://docs.sentry.io/platforms/dart/guides/flutter.md
path: platforms/dart/guides/flutter
---

---
title: "Flutter"
description: "Learn how to set up Sentry in your Flutter app, capture your first errors and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/dart/guides/flutter/
---

# Sentry for Flutter

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
$downloadUrl = "https://github.com/getsentry/sentry-wizard/releases/download/v5.1.0/sentry-wizard-win-x64.exe"
Invoke-WebRequest $downloadUrl -OutFile sentry-wizard.exe
./sentry-wizard.exe -i flutter
```

**macOS (Intel/x64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v5.1.0/sentry-wizard-darwin-x64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**macOS (Apple Silicon/arm64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v5.1.0/sentry-wizard-darwin-arm64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**Linux (x64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v5.1.0/sentry-wizard-linux-x64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**Linux (arm64)**

```bash
downloadUrl="https://github.com/getsentry/sentry-wizard/releases/download/v5.1.0/sentry-wizard-linux-arm64"
curl -L $downloadUrl -o sentry-wizard
chmod +x sentry-wizard
./sentry-wizard -i flutter
```

**npx**

```bash
npx @sentry/wizard@latest -i flutter
```

This will patch your project and configure the SDK. You only need to patch the project once, then you can add the patched files to your version control system. If you prefer, you can also [set up the SDK manually](https://docs.sentry.io/platforms/dart/guides/flutter/manual-setup.md).

The following tasks will be performed by the Sentry Wizard

* Update your `pubspec.yaml` with the `sentry_flutter` and `sentry_dart_plugin` packages.
* Create a `sentry.properties` file (gitignored) with a Sentry CLI auth token.
* Prompt you for optional features and patch `main.dart` with `SentryFlutter.init`.
* Add a sample exception that is captured when the app starts so you can verify the setup.

The wizard will prompt you to enable optional features. Select the same options here so this guide can show you how to verify them:

Error Monitoring\[ ]Tracing\[ ]Session Replay

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Session Replay**](https://docs.sentry.io/product/session-replay.md): Get to the root cause of an issue faster by viewing a video-like reproduction of what users saw in your app before, during, and after the problem.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

## [Verify Your Setup](https://docs.sentry.io/platforms/dart/guides/flutter.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

### [Issues](https://docs.sentry.io/platforms/dart/guides/flutter.md#issues)

The wizard added a sample exception to `main.dart` that is captured when the app starts. Run your app to send it to Sentry:

```bash
flutter run
```

After you've confirmed the issue in Sentry, remove the sample exception from `main.dart` so it isn't captured on every launch.

### [Tracing](https://docs.sentry.io/platforms/dart/guides/flutter.md#tracing)

To test your tracing configuration, create a custom transaction and span:

```dart
final transaction = Sentry.startTransaction('test-transaction', 'task');
final span = transaction.startChild('test-span');
await span.finish();
await transaction.finish();
```

### [Logs](https://docs.sentry.io/platforms/dart/guides/flutter.md#logs)

Logs are enabled by default. Use the Sentry logger to send structured logs from anywhere in your application:

```dart
Sentry.logger.info('User clicked checkout button');

Sentry.logger.info('Order completed', attributes: {
  'order_id': SentryAttribute.string('12345'),
  'total': SentryAttribute.double(99.99),
});

Sentry.logger.warn('Warning message');
Sentry.logger.error('Error occurred');
```

### [Metrics NEW](https://docs.sentry.io/platforms/dart/guides/flutter.md#metrics-)

Metrics are enabled by default. Send test metrics from your app to verify that metrics are arriving in Sentry:

```dart
Sentry.metrics.count('checkout.failed', 1);
Sentry.metrics.gauge('queue.depth', 42);
Sentry.metrics.distribution('cart.amount_usd', 187.5);
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dart/guides/flutter.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) page and select an entry from the list to get a detailed view where you can replay the interaction and get more information to help you troubleshoot.
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/dart/guides/flutter.md#next-steps)

At this point, you should have integrated Sentry into your Flutter application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Continue to [customize your configuration](https://docs.sentry.io/platforms/dart/guides/flutter/configuration.md)
* Add readable [stack traces](https://docs.sentry.io/platforms/dart/guides/flutter/debug-symbols.md#when-to-upload-debug-symbols) to errors
* Learn about the [features of Sentry's Flutter SDK](https://docs.sentry.io/platforms/dart/guides/flutter/features.md)
* Add [performance instrumentation to your app](https://docs.sentry.io/platforms/dart/guides/flutter/tracing/instrumentation.md)

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

