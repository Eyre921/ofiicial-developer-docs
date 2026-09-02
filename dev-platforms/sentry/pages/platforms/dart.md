---
title: "Dart"
source: https://docs.sentry.io/platforms/dart.md
path: platforms/dart
---

---
title: "Dart"
description: "Learn how to set up Sentry in your Dart app, capture your first errors and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/dart/
---

# Dart | Sentry for Dart

##### Using Flutter?

This guide focuses on plain Dart. If you're building a Flutter app, use the dedicated [Flutter SDK](https://docs.sentry.io/platforms/dart/guides/flutter.md) instead.

## [Prerequisites](https://docs.sentry.io/platforms/dart.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running

## [Install](https://docs.sentry.io/platforms/dart.md#install)

Add the Sentry Dart SDK to your `pubspec.yaml`:

```yml
dependencies:
  sentry: ^9.28.0
```

## [Configure](https://docs.sentry.io/platforms/dart.md#configure)

Choose the features you want to configure, and this guide will show you how:

Error Monitoring\[ ]Tracing

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/dart.md#initialize-the-sentry-sdk)

Configuration should happen as **early as possible** in your application's lifecycle.

Import and initialize the SDK in your app's entry point:

```dart
import 'package:sentry/sentry.dart';

Future<void> main() async {
  await Sentry.init((options) {
    options.dsn = 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>';
    // Adds request headers and IP for users, for more info visit:
    // https://docs.sentry.io/platforms/dart/data-management/data-collected/
    options.sendDefaultPii = true;
    // ___PRODUCT_OPTION_START___ performance
    // Set tracesSampleRate to 1.0 to capture 100% of transactions for tracing.
    // We recommend adjusting this value in production.
    options.tracesSampleRate = 1.0;
    // ___PRODUCT_OPTION_END___ performance
  });

  // you can also configure SENTRY_DSN, SENTRY_RELEASE, SENTRY_DIST, and
  // SENTRY_ENVIRONMENT via Dart environment variable (--dart-define)
}
```

## [Verify Your Setup](https://docs.sentry.io/platforms/dart.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

### [Issues](https://docs.sentry.io/platforms/dart.md#issues)

To verify that Sentry captures errors and creates issues in your Sentry project, add this intentional error to your application:

```dart
import 'package:sentry/sentry.dart';

try {
  throw StateError('Sentry Test Error');
} catch (exception, stackTrace) {
  await Sentry.captureException(
    exception,
    stackTrace: stackTrace,
  );
}
```

### [Tracing](https://docs.sentry.io/platforms/dart.md#tracing)

To test your tracing configuration, create a custom transaction and span:

```dart
final transaction = Sentry.startTransaction('test-transaction', 'task');
final span = transaction.startChild('test-span');
await span.finish();
await transaction.finish();
```

### [Logs](https://docs.sentry.io/platforms/dart.md#logs)

Logs are enabled by default. Use the Sentry logger to send structured logs from anywhere in your application:

```dart
Sentry.logger.info('User clicked checkout button');

Sentry.logger.info('Order completed', attributes: {
  'order_id': SentryAttribute.string('12345'),
  'total': SentryAttribute.double(99.99),
});

Sentry.logger.warning('Warning message');
Sentry.logger.error('Error occurred');
```

### [Metrics NEW](https://docs.sentry.io/platforms/dart.md#metrics-)

Metrics are enabled by default. Send test metrics from your app to verify that metrics are arriving in Sentry:

```dart
Sentry.metrics.count('checkout.failed', 1);
Sentry.metrics.gauge('queue.depth', 42);
Sentry.metrics.distribution('cart.amount_usd', 187.5);
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/dart.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating the captured errors in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/dart.md#next-steps)

At this point, you should have integrated Sentry into your Dart application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/guides.md) on what to monitor, log, track, and investigate after setup
* Continue to [customize your configuration](https://docs.sentry.io/platforms/dart/configuration.md)
* Learn more about [manually capturing errors or messages](https://docs.sentry.io/platforms/dart/usage.md)
* Learn about the [features of Sentry's Dart SDK](https://docs.sentry.io/platforms/dart/features.md)
* Add [performance instrumentation to your app](https://docs.sentry.io/platforms/dart/tracing/instrumentation.md)

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

