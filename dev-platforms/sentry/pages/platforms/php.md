---
title: "PHP"
source: https://docs.sentry.io/platforms/php.md
path: platforms/php
---

---
title: "PHP"
description: "Learn how to set up Sentry in your PHP application and capture your first events."
url: https://docs.sentry.io/platforms/php/
---

# Sentry for PHP

## Set up with Sentry CLI

Set up the Sentry PHP SDK with the Sentry CLI. Install the CLI with one of these commands, then follow the Sentry CLI docs to finish setup.

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

##### Using a framework?

This guide focuses on plain PHP. Read one of these other guides if you use [Laravel](https://docs.sentry.io/platforms/php/guides/laravel.md) or [Symfony](https://docs.sentry.io/platforms/php/guides/symfony.md).

## [Prerequisites](https://docs.sentry.io/platforms/php.md#prerequisites)

You need:

* a [Sentry account](https://sentry.io/signup/) and project
* an application running on PHP `7.2` or later
* [Composer](https://getcomposer.org/)

Deploying with Forge?

If you use Laravel Forge to provision and deploy your PHP application, you can create a Sentry organization through [Forge](https://forge.laravel.com/docs/integrations/sentry).

## [Install](https://docs.sentry.io/platforms/php.md#install)

Install the Sentry PHP SDK using Composer:

```bash
composer require "sentry/sentry:^4.31"
```

### [Install Excimer for Profiling](https://docs.sentry.io/platforms/php.md#install-excimer-for-profiling)

Profiling requires the Excimer PHP extension. Install it with PECL:

```bash
pecl install excimer
```

Excimer supports PHP `7.2`+, and requires Linux or macOS. It doesn't support Windows. For other installation methods, see the [Excimer installation guide](https://docs.sentry.io/platforms/php/profiling.md#installation).

Depending on your PHP installation, you may also need to enable `extension=excimer.so` in the `php.ini` used by your application and restart your PHP workers or web server. Confirm that Excimer is loaded in the PHP runtime serving your application.

## [Configure](https://docs.sentry.io/platforms/php.md#configure)

**Error Monitoring** starts working as soon as you call `\Sentry\init()`. **Logs** and **Application Metrics** need no extra configuration as of SDK version `4.31.0`, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/php.md#send-logs) and [#4](https://docs.sentry.io/platforms/php.md#send-application-metrics-). This guide also configures **Tracing** and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/php.md#initialize-the-sentry-sdk)

To capture errors that occur during startup, initialize the Sentry PHP SDK as early as possible in your application's lifecycle, after loading Composer's autoloader. The example below assumes your entry point is in the project root.

The snippet configures:

* Tracing: via [`traces_sample_rate`](https://docs.sentry.io/platforms/php/configuration/options.md#traces_sample_rate)
* Profiling: via [`profiles_sample_rate`](https://docs.sentry.io/platforms/php/configuration/options.md#profiles_sample_rate)

Don't need a feature? Remove its options from the snippet.

```php
require_once __DIR__ . '/vendor/autoload.php';

\Sentry\init([
  'dsn' => 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>',

  // Configures sampling for transactions you create below.
  // Set to 1.0 to capture 100% of spans for tracing.
  // We recommend reducing this value in production.
  'traces_sample_rate' => 1.0,

  // Enables Profiling.
  // Profiles are sampled relative to traces_sample_rate.
  'profiles_sample_rate' => 1.0,
]);
```

##### Capture stack trace arguments

To receive stack trace arguments in your errors, set `zend.exception_ignore_args = Off` in your `php.ini`.

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/php.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data (HTTP bodies, URL query parameters, etc.), with sensitive values scrubbed.

To opt out of individual categories use the `data_collection` option. For the full list of categories and their defaults, [see the `data_collection` options](https://docs.sentry.io/platforms/php/configuration/options.md#data_collection).

```php
\Sentry\init([
    'dsn' => 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>',
    'data_collection' => [
        // opt out of collecting user info
        'user_info' => false,
        // opt out of collecting cookies
        'cookies' => ['mode' => 'off'],
        // other categories
    ],
]);
```

### [Start a Transaction](https://docs.sentry.io/platforms/php.md#start-a-transaction)

In plain PHP, the tracing and profiling sampling options don't create transactions automatically. Start a transaction around the work you want to trace and profile, and finish it to send the data to Sentry:

```php
$transactionContext = \Sentry\Tracing\TransactionContext::make()
    ->setName('Example transaction')
    ->setOp('task');

$transaction = \Sentry\startTransaction($transactionContext);
\Sentry\SentrySdk::getCurrentHub()->setSpan($transaction);

try {
    // Run the application code you want to trace and profile.
} finally {
    $transaction->finish();
    \Sentry\SentrySdk::getCurrentHub()->setSpan(null);
}
```

See [Custom Instrumentation](https://docs.sentry.io/platforms/php/tracing/instrumentation/custom-instrumentation.md) to add child spans and instrument more of your application.

## [Send Logs](https://docs.sentry.io/platforms/php.md#send-logs)

Use `\Sentry\logger()` to send logs at different levels, such as `info`, `warn`, or `error`.

In standalone PHP applications, explicitly flush buffered logs before the request or script ends. In long-running processes, flush periodically. Laravel and Symfony provide lifecycle-based flushing.

See [Set Up Logs](https://docs.sentry.io/platforms/php/logs.md) for all available logging methods and formatting options.

```php
\Sentry\logger()->info('Checkout completed');
\Sentry\logger()->warn('This is a warning log with attributes.', attributes: [
  'attribute1' => 'string',
  'attribute2' => 1,
  'attribute3' => 1.0,
  'attribute4' => true,
]);

\Sentry\logger()->flush();
```

If you already use Monolog, its [Sentry LogsHandler](https://docs.sentry.io/platforms/php/integrations/monolog.md#logs) can send messages to Sentry.

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/php.md#send-application-metrics-)

Use `\Sentry\traceMetrics()` to send counters, gauges, and distributions from your app. Add attributes to search and filter metrics later. Flush collected metrics before the request or script ends, or periodically in long-running processes.

See [Set Up Metrics](https://docs.sentry.io/platforms/php/metrics.md) for all available metric types and configuration options.

```php
use \Sentry\Metrics\Unit;

\Sentry\traceMetrics()->count('button-click', 5, ['browser' => 'Firefox', 'app_version' => '1.0.0']);
\Sentry\traceMetrics()->distribution('page-load', 15.0, ['page' => '/home'], Unit::millisecond());

\Sentry\traceMetrics()->flush();
```

## [Verify Your Setup](https://docs.sentry.io/platforms/php.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Add an uncaught exception to a route or test script and run it:

```php
throw new \RuntimeException('Sentry test exception');
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/php.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/php.md#next-steps)

At this point, you should have integrated Sentry into your PHP application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Learn how to use [Crons](https://docs.sentry.io/platforms/php/crons.md) and [Feature Flags](https://docs.sentry.io/platforms/php/feature-flags.md)
* Collect user feedback via the [Crash-Report Modal](https://docs.sentry.io/platforms/php/user-feedback.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/php/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Frameworks

- [Laravel](https://docs.sentry.io/platforms/php/guides/laravel.md)
- [Symfony](https://docs.sentry.io/platforms/php/guides/symfony.md)
- [Bref](https://docs.sentry.io/platforms/php/guides/bref.md)

## Topics

- [Enriching Events](https://docs.sentry.io/platforms/php/enriching-events.md)
- [Tracing](https://docs.sentry.io/platforms/php/tracing.md)
- [Configuration](https://docs.sentry.io/platforms/php/configuration.md)
- [Profiling](https://docs.sentry.io/platforms/php/profiling.md)
- [Integrations](https://docs.sentry.io/platforms/php/integrations.md)
- [Logs](https://docs.sentry.io/platforms/php/logs.md)
- [Troubleshooting](https://docs.sentry.io/platforms/php/troubleshooting.md)
- [Sidecar SDK Transport](https://docs.sentry.io/platforms/php/agent.md)
- [Crons](https://docs.sentry.io/platforms/php/crons.md)
- [Data Management](https://docs.sentry.io/platforms/php/data-management.md)
- [Application Metrics](https://docs.sentry.io/platforms/php/metrics.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/php/security-policy-reporting.md)
- [User Feedback](https://docs.sentry.io/platforms/php/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/php/feature-flags.md)
- [Usage](https://docs.sentry.io/platforms/php/usage.md)
- [Legacy SDK](https://docs.sentry.io/platforms/php/legacy-sdk.md)

