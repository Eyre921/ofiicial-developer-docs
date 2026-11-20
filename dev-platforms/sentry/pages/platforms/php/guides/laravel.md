---
title: "Laravel"
source: https://docs.sentry.io/platforms/php/guides/laravel.md
path: platforms/php/guides/laravel
---

---
title: "Laravel"
description: "Learn how to set up Sentry in your Laravel application and capture your first events."
url: https://docs.sentry.io/platforms/php/guides/laravel/
---

# Sentry for Laravel

## [Prerequisites](https://docs.sentry.io/platforms/php/guides/laravel.md#prerequisites)

You need:

* a [Sentry account](https://sentry.io/signup/) and project
* an application running on PHP `7.2` or later
* Laravel version `11.x`+
* [Composer](https://getcomposer.org/)

Read one of these guides if you use an [older Laravel version](https://docs.sentry.io/platforms/php/guides/laravel/other-versions.md) or need [Lumen-specific instructions](https://docs.sentry.io/platforms/php/guides/laravel/other-versions/lumen.md).

Deploying with Forge?

If you use Laravel Forge to provision and deploy your PHP application, you can create a Sentry organization through [Forge](https://forge.laravel.com/docs/integrations/sentry).

## [Install](https://docs.sentry.io/platforms/php/guides/laravel.md#install)

Install the latest `sentry/sentry-laravel` package:

```bash
composer require sentry/sentry-laravel
```

### [Install Excimer for Profiling](https://docs.sentry.io/platforms/php/guides/laravel.md#install-excimer-for-profiling)

Profiling requires the Excimer PHP extension. Install it with PECL:

```bash
pecl install excimer
```

Excimer supports PHP `7.2`+, and requires Linux or macOS. It doesn't support Windows. For other installation methods, see the [Excimer installation guide](https://docs.sentry.io/platforms/php/guides/laravel/profiling.md#installation).

Depending on your PHP installation, you may also need to enable `extension=excimer.so` in the `php.ini` used by your application and restart your PHP workers or web server. Confirm that Excimer is loaded in the PHP runtime serving your application.

## [Configure](https://docs.sentry.io/platforms/php/guides/laravel.md#configure)

**Error Monitoring** starts working as soon as you initialize Sentry. **Application Metrics** need no extra configuration and you'll learn how to send them in step [#4](https://docs.sentry.io/platforms/php/guides/laravel.md#send-application-metrics-). This guide also enables **Tracing**, **Profiling**, and **Logs**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/php/guides/laravel.md#initialize-the-sentry-sdk)

Publish the Sentry config file and set your DSN:

```shell
php artisan sentry:publish --dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>
```

This creates the config file `config/sentry.php` and adds your DSN, along with any options you confirm at the prompts, to your `.env` file.

The snippet shown below also configures:

* Tracing: via [`traces_sample_rate`](https://docs.sentry.io/platforms/php/guides/laravel/configuration/options.md#traces_sample_rate)
* Profiling: via [`profiles_sample_rate`](https://docs.sentry.io/platforms/php/guides/laravel/configuration/options.md#profiles_sample_rate)
* Logs: via the [`sentry_logs`](https://docs.sentry.io/platforms/php/guides/laravel/logs.md) channel in `LOG_STACK`

Don't need a feature? Remove its lines from your `.env` file.

```shell
SENTRY_LARAVEL_DSN=https://<key>@o<orgId>.ingest.sentry.io/<projectId>

# Enables Tracing.
# Set to 1.0 to capture 100% of spans for tracing.
# We recommend reducing this value in production.
SENTRY_TRACES_SAMPLE_RATE=1.0

# Enables Profiling.
# Profiles are sampled relative to SENTRY_TRACES_SAMPLE_RATE.
SENTRY_PROFILES_SAMPLE_RATE=1.0

# Sends Laravel logs to Sentry through the sentry_logs channel.
LOG_CHANNEL=stack
LOG_STACK=single,sentry_logs
```

##### Capture stack trace arguments

To receive stack trace arguments in your errors, set `zend.exception_ignore_args = Off` in your `php.ini`.

### [Disable Sentry During Local Development and Testing](https://docs.sentry.io/platforms/php/guides/laravel.md#disable-sentry-during-local-development-and-testing)

When Sentry is installed in your application, it's also active when you're developing or running tests. This can send unwanted events to Sentry and slow down your application or test suite.

To stop sending events to Sentry, leave `SENTRY_LARAVEL_DSN` out of your `.env` file or set it to `SENTRY_LARAVEL_DSN=null`.

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/php/guides/laravel.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data (HTTP bodies, URL query parameters, etc.), with sensitive values scrubbed.

To opt out of individual categories use the `data_collection` option. For the full list of categories and their defaults, [see the `data_collection` options](https://docs.sentry.io/platforms/php/guides/laravel/configuration/options.md#data_collection).

```php
'data_collection' => [
    // opt out of collecting user info
    'user_info' => false,
    // opt out of collecting cookies
    'cookies' => ['mode' => 'off'],
    // other categories
],
```

### [Report Unhandled Exceptions](https://docs.sentry.io/platforms/php/guides/laravel.md#report-unhandled-exceptions)

Enable capturing unhandled exceptions to report to Sentry by making the following change to your `bootstrap/app.php`:

```php
<?php

use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;
use Sentry\Laravel\Integration;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',
    )
    ->withMiddleware(function (Middleware $middleware) {
        //
    })
    ->withExceptions(function (Exceptions $exceptions) {
        Integration::handles($exceptions);
    })
    ->create();
```

## [Send Logs](https://docs.sentry.io/platforms/php/guides/laravel.md#send-logs)

Once the `sentry_logs` channel is in your log stack, Laravel's `Log` facade sends logs to Sentry. Laravel flushes logs automatically when a request, command, or job finishes.

See [Set Up Logs](https://docs.sentry.io/platforms/php/guides/laravel/logs.md) for all available logging methods and formatting options.

```php
use Illuminate\Support\Facades\Log;

Log::info('This is an info message');
Log::warning('User {id} failed to login.', ['id' => $user->id]);
Log::error('Something went wrong', [
    'user_id' => auth()->id(),
    'action' => 'update_profile',
    'additional_data' => $data,
]);
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/php/guides/laravel.md#send-application-metrics-)

Use `\Sentry\traceMetrics()` to send counters, gauges, and distributions from your app. Add attributes to search and filter metrics later. Laravel flushes metrics automatically at the end of each request or command.

See [Set Up Metrics](https://docs.sentry.io/platforms/php/guides/laravel/metrics.md) for all available metric types and configuration options.

```php
use \Sentry\Metrics\Unit;

\Sentry\traceMetrics()->count('button-click', 5, ['browser' => 'Firefox', 'app_version' => '1.0.0']);
\Sentry\traceMetrics()->distribution('page-load', 15.0, ['page' => '/home'], Unit::millisecond());
```

## [Verify Your Setup](https://docs.sentry.io/platforms/php/guides/laravel.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

### [Verify With Artisan](https://docs.sentry.io/platforms/php/guides/laravel.md#verify-with-artisan)

You can test your configuration using the `sentry:test` artisan command:

```shell
php artisan sentry:test
```

### [Verify With Code](https://docs.sentry.io/platforms/php/guides/laravel.md#verify-with-code)

Add a route that throws an exception, then visit it:

```php
Route::get('/debug-sentry', function () {
    throw new Exception('My first Sentry error!');
});
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/php/guides/laravel.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/php/guides/laravel.md#next-steps)

At this point, you should have integrated Sentry into your Laravel application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Monitor and debug your Laravel agents with [Agent Tracing](https://docs.sentry.io/platforms/php/guides/laravel/agent-tracing.md)
* Learn how to use [Crons](https://docs.sentry.io/platforms/php/guides/laravel/crons.md) and [Feature Flags](https://docs.sentry.io/platforms/php/guides/laravel/feature-flags.md)
* Collect user feedback via the [Crash-Report Modal](https://docs.sentry.io/platforms/php/guides/laravel/user-feedback.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/php/guides/laravel/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other PHP Frameworks

- [Symfony](https://docs.sentry.io/platforms/php/guides/symfony.md)
- [Bref](https://docs.sentry.io/platforms/php/guides/bref.md)

## Topics

- [Enriching Events](https://docs.sentry.io/platforms/php/guides/laravel/enriching-events.md)
- [Profiling](https://docs.sentry.io/platforms/php/guides/laravel/profiling.md)
- [Tracing](https://docs.sentry.io/platforms/php/guides/laravel/tracing.md)
- [Configuration](https://docs.sentry.io/platforms/php/guides/laravel/configuration.md)
- [Logs](https://docs.sentry.io/platforms/php/guides/laravel/logs.md)
- [Integrations](https://docs.sentry.io/platforms/php/guides/laravel/integrations.md)
- [Usage](https://docs.sentry.io/platforms/php/guides/laravel/usage.md)
- [Troubleshooting](https://docs.sentry.io/platforms/php/guides/laravel/troubleshooting.md)
- [Crons](https://docs.sentry.io/platforms/php/guides/laravel/crons.md)
- [Data Management](https://docs.sentry.io/platforms/php/guides/laravel/data-management.md)
- [Agent Tracing](https://docs.sentry.io/platforms/php/guides/laravel/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/php/guides/laravel/metrics.md)
- [Other Versions](https://docs.sentry.io/platforms/php/guides/laravel/other-versions.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/php/guides/laravel/security-policy-reporting.md)
- [User Feedback](https://docs.sentry.io/platforms/php/guides/laravel/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/php/guides/laravel/feature-flags.md)

