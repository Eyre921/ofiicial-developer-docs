---
title: "Dart"
source: https://docs.sentry.io/platforms/dart.md
path: platforms/dart
---

---
title: "Dart"
description: "Learn how to set up Sentry in your Dart app, capture your first events, and view them in Sentry."
url: https://docs.sentry.io/platforms/dart/
---

# Sentry for Dart

##### Using Flutter?

This guide focuses on plain Dart. If you're building a Flutter app, use the dedicated [Flutter SDK](https://docs.sentry.io/platforms/dart/guides/flutter.md) instead.

## [Prerequisites](https://docs.sentry.io/platforms/dart.md#prerequisites)

These instructions use Sentry Dart SDK v10. You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* An application using **Dart 3.12.0** or later

For an existing Sentry integration, review the [v10 breaking changes](https://github.com/getsentry/sentry-dart/releases/tag/10.0.0) before upgrading.

## [Install](https://docs.sentry.io/platforms/dart.md#install)

Add the Sentry Dart SDK to your `pubspec.yaml`:

```yml
dependencies:
  sentry: ^10.3.0
```

## [Configure](https://docs.sentry.io/platforms/dart.md#configure)

Initialize **Error Monitoring** with `Sentry.init()` and run your application in its `appRunner` callback to capture uncaught exceptions and unhandled asynchronous errors. **Logs** and **Application Metrics** are enabled by default in SDK v10, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/dart.md#send-logs) and [#4](https://docs.sentry.io/platforms/dart.md#send-application-metrics-). This guide also enables **Tracing**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Capture uncaught exceptions and unhandled asynchronous errors in your application's guarded error zone. Report handled errors with Sentry.captureException.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/dart.md#initialize-the-sentry-sdk)

Configuration should happen as **early as possible** in your application's lifecycle.

Import and initialize the SDK in your app's entry point as shown in the code snippet below.

The snippet also turns on:

* Tracing: via [`tracesSampleRate`](https://docs.sentry.io/platforms/dart/configuration/options.md#tracesSampleRate)
* Additional user and request data: via [`sendDefaultPii`](https://docs.sentry.io/platforms/dart/configuration/options.md#sendDefaultPii)

To skip tracing, omit `tracesSampleRate`. To discard logs or metrics, return `null` from [`beforeSendLog`](https://docs.sentry.io/platforms/dart/logs.md#beforesendlog) or [`beforeSendMetric`](https://docs.sentry.io/platforms/dart/metrics.md#beforesendmetric).

```dart
import 'package:sentry/sentry.dart';

Future<void> main() async {
  await Sentry.init(
    (options) {
      options.dsn = 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>';

      // Allows sending default personal data, such as IP addresses,
      // when available from the SDK's integrations.
      options.sendDefaultPii = true;

      // Enables Tracing.
      // Set to 1.0 to capture 100% of spans for tracing.
      // We recommend reducing this value in production.
      options.tracesSampleRate = 1.0;
    },
    appRunner: () async {
      // Start your application here.
    },
  );

  // You can also configure SENTRY_DSN, SENTRY_RELEASE, SENTRY_DIST, and
  // SENTRY_ENVIRONMENT via Dart environment variables (--dart-define).
}
```

The `appRunner` callback runs in a guarded error zone. This is required for automatic error capture on Dart web, where isolate error listeners are unavailable. For additional isolates, register an error listener with [`addSentryErrorListener`](https://pub.dev/documentation/sentry/latest/sentry_io/SentryIsolateExtension/addSentryErrorListener.html) from `package:sentry/sentry_io.dart`.

For finite command-line applications, call `await Sentry.close()` after all awaited application work finishes to flush buffered telemetry and close SDK resources, including the isolate error-listener port.

## [Send Logs](https://docs.sentry.io/platforms/dart.md#send-logs)

Call `Sentry.logger` from your application code after initialization to send structured logs at different levels. You can add attributes to make logs easier to search and filter.

See [Set Up Logs](https://docs.sentry.io/platforms/dart/logs.md) for all available logging methods and message formatting.

```dart
Sentry.logger.info('Order completed', attributes: {
  'order_id': SentryAttribute.string('12345'),
  'total': SentryAttribute.double(99.99),
});

Sentry.logger.warn('Slow operation detected');
Sentry.logger.error('Validation failed');
```

If you use the Dart `logging` package, add the [`sentry_logging` integration](https://docs.sentry.io/platforms/dart/integrations/logging.md) to send its records to Sentry.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/dart.md#send-application-metrics-)

Call `Sentry.metrics` from your application code after initialization to send counters, gauges, and distributions. Add attributes to filter and group metrics in Sentry.

See [Set Up Metrics](https://docs.sentry.io/platforms/dart/metrics.md) for metric types, attributes, and configuration options.

```dart
Sentry.metrics.count('checkout.failed', 1);
Sentry.metrics.gauge('queue.depth', 42);
Sentry.metrics.distribution('api_latency', 187, unit: 'millisecond');
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dart.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

Add this inside the async `appRunner` callback to trigger and capture a test error:

```dart
try {
  throw StateError('Sentry Test Error');
} catch (exception, stackTrace) {
  await Sentry.captureException(
    exception,
    stackTrace: stackTrace,
  );
}
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dart.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/dart.md#next-steps)

At this point, you should have integrated Sentry into your Dart application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn more about [manually capturing errors or messages](https://docs.sentry.io/platforms/dart/usage.md)
* Add [performance instrumentation](https://docs.sentry.io/platforms/dart/tracing/instrumentation.md) to your app

Are you having problems setting up the SDK?

* [Get support](https://www.sentry.help/en/)

## Frameworks

- [Flutter](https://docs.sentry.io/platforms/dart/guides/flutter.md)

## Topics

- [Features](https://docs.sentry.io/platforms/dart/features.md)
- [Basic Configuration](https://docs.sentry.io/platforms/dart/configuration.md)
- [Integrations](https://docs.sentry.io/platforms/dart/integrations.md)
- [Usage](https://docs.sentry.io/platforms/dart/usage.md)
- [Debug Symbols](https://docs.sentry.io/platforms/dart/debug-symbols.md)
- [Enriching Events](https://docs.sentry.io/platforms/dart/enriching-events.md)
- [Data Management](https://docs.sentry.io/platforms/dart/data-management.md)
- [Tracing](https://docs.sentry.io/platforms/dart/tracing.md)
- [Logs](https://docs.sentry.io/platforms/dart/logs.md)
- [Application Metrics](https://docs.sentry.io/platforms/dart/metrics.md)
- [User Feedback](https://docs.sentry.io/platforms/dart/user-feedback.md)
- [Set Up Feature Flags](https://docs.sentry.io/platforms/dart/feature-flags.md)
- [SDK Overhead](https://docs.sentry.io/platforms/dart/overhead.md)
- [Migration Guide](https://docs.sentry.io/platforms/dart/migration.md)

