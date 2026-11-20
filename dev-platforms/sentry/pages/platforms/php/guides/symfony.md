---
title: "Symfony"
source: https://docs.sentry.io/platforms/php/guides/symfony.md
path: platforms/php/guides/symfony
---

---
title: "Symfony"
description: "Learn how to set up Sentry in your Symfony application and capture your first events."
url: https://docs.sentry.io/platforms/php/guides/symfony/
---

# Sentry for Symfony

## [Prerequisites](https://docs.sentry.io/platforms/php/guides/symfony.md#prerequisites)

You need:

* a [Sentry account](https://sentry.io/signup/) and project
* a Symfony app running on PHP `7.2` or later
* [Composer](https://getcomposer.org/)

## [Install](https://docs.sentry.io/platforms/php/guides/symfony.md#install)

Install the latest `sentry/sentry-symfony` bundle:

```bash
composer require sentry/sentry-symfony
```

### [Install Monolog for Logs](https://docs.sentry.io/platforms/php/guides/symfony.md#install-monolog-for-logs)

The logging configuration below also requires MonologBundle. If it isn't already installed, add it:

```bash
composer require symfony/monolog-bundle
```

### [Install Excimer for Profiling](https://docs.sentry.io/platforms/php/guides/symfony.md#install-excimer-for-profiling)

Profiling requires the Excimer PHP extension. Install it with PECL:

```bash
pecl install excimer
```

Excimer supports PHP `7.2`+, and requires Linux or macOS. It doesn't support Windows. For other installation methods, see the [Excimer installation guide](https://docs.sentry.io/platforms/php/guides/symfony/profiling.md#installation).

Depending on your PHP installation, you may also need to enable `extension=excimer.so` in the `php.ini` used by your application and restart your PHP workers or web server. Confirm that Excimer is loaded in the PHP runtime serving your application.

## [Configure](https://docs.sentry.io/platforms/php/guides/symfony.md#configure)

**Error Monitoring** starts working as soon as the bundle is enabled and your DSN is set. **Application Metrics** need no extra configuration and you'll learn how to send them in step [#4](https://docs.sentry.io/platforms/php/guides/symfony.md#send-application-metrics-). This guide also enables **Tracing**, **Profiling**, and **Logs**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/php/guides/symfony.md#initialize-the-sentry-sdk)

Add your Sentry DSN to your `.env` file:

```plain
###> sentry/sentry-symfony ###
SENTRY_DSN="https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
###< sentry/sentry-symfony ###
```

Then configure the bundle in `config/packages/sentry.yaml` as shown in the snippet below.

The snippet also turns on:

* Tracing: via [`traces_sample_rate`](https://docs.sentry.io/platforms/php/guides/symfony/configuration/options.md#traces_sample_rate)
* Profiling: via [`profiles_sample_rate`](https://docs.sentry.io/platforms/php/guides/symfony/configuration/options.md#profiles_sample_rate)
* Logs: via the [`sentry_logs` Monolog handler](https://docs.sentry.io/platforms/php/guides/symfony/logs.md)

Don't need a feature? Remove its options from the snippet.

```yaml
when@prod:
  sentry:
    dsn: "%env(SENTRY_DSN)%"
    options:
      # Enables Tracing.
      # Set to 1.0 to capture 100% of spans for tracing.
      # We recommend reducing this value in production.
      traces_sample_rate: 1.0

      # Enables Profiling.
      # Profiles are sampled relative to traces_sample_rate.
      profiles_sample_rate: 1.0

  # Sends Monolog records to Sentry as Logs.
  monolog:
    handlers:
      sentry_logs:
        type: service
        id: Sentry\SentryBundle\Monolog\LogsHandler

  services:
    Sentry\SentryBundle\Monolog\LogsHandler:
      arguments:
        # The minimum level of logs to send to Sentry.
        - !php/const Monolog\Logger::INFO
```

##### Capture stack trace arguments

To receive stack trace arguments in your errors, set `zend.exception_ignore_args = Off` in your `php.ini`.

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/php/guides/symfony.md#control-the-data-you-send-to-sentry)

By default, the SDK sends user identity data (IP address, ID, and similar) and other data (HTTP bodies, URL query parameters, etc.), with sensitive values scrubbed.

To opt out of individual categories use the `data_collection` option. For the full list of categories and their defaults, [see the `data_collection` options](https://docs.sentry.io/platforms/php/guides/symfony/configuration/options.md#data_collection).

```yaml
when@prod:
    sentry:
        options:
            data_collection:
                # opt out of collecting user info
                user_info: false
                # opt out of collecting cookies
                cookies:
                    mode: "off"
                # other categories
            # your other Sentry options
],
```

### [Enable Sentry in Other Environments](https://docs.sentry.io/platforms/php/guides/symfony.md#enable-sentry-in-other-environments)

When using Symfony Flex, the Sentry bundle is enabled in the `prod` environment only by default, which is why the snippet uses `when@prod`. To use Sentry in other environments, update `config/packages/sentry.yaml` and the Sentry bundle entry in `config/bundles.php`.

## [Send Logs](https://docs.sentry.io/platforms/php/guides/symfony.md#send-logs)

Once the `sentry_logs` handler is registered, you can use you regular `LoggerInterface` to send logs to Sentry. Symfony flushes logs automatically when a request or command finishes.

See [Set Up Logs](https://docs.sentry.io/platforms/php/guides/symfony/logs.md) for all available logging methods and formatting options.

```php
$this->logger->info("This is an info message");
$this->logger->warning('User {id} failed to login.', ['id' => $user->id]);

$this->logger->error('Something went wrong', [
    'user_id' => $userId,
    'action' => 'update_profile',
    'additional_data' => $data,
]);
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/php/guides/symfony.md#send-application-metrics-)

Use `\Sentry\traceMetrics()` to send counters, gauges, and distributions from your app. Add attributes to search and filter metrics later. Symfony flushes metrics automatically at the end of each request or command.

See [Set Up Metrics](https://docs.sentry.io/platforms/php/guides/symfony/metrics.md) for all available metric types and configuration options.

```php
use \Sentry\Metrics\Unit;

\Sentry\traceMetrics()->count('button-click', 5, ['browser' => 'Firefox', 'app_version' => '1.0.0']);
\Sentry\traceMetrics()->distribution('page-load', 15.0, ['page' => '/home'], Unit::millisecond());
```

## [Verify Your Setup](https://docs.sentry.io/platforms/php/guides/symfony.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Create the following controller, then visit `/_sentry-test` in an environment where Sentry is enabled:

```php
<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Routing\Attribute\Route;

class SentryTestController extends AbstractController
{
    #[Route('/_sentry-test', name: 'sentry_test')]
    public function testException()
    {
        throw new \RuntimeException('Example exception.');
    }
}
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/php/guides/symfony.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/php/guides/symfony.md#next-steps)

At this point, you should have integrated Sentry into your Symfony application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after Setup
* Learn how to use [Crons](https://docs.sentry.io/platforms/php/guides/symfony/crons.md) and [Feature Flags](https://docs.sentry.io/platforms/php/guides/symfony/feature-flags.md)
* Collect user feedback via the [Crash-Report Modal](https://docs.sentry.io/platforms/php/guides/symfony/user-feedback.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/php/guides/symfony/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other PHP Frameworks

- [Laravel](https://docs.sentry.io/platforms/php/guides/laravel.md)
- [Bref](https://docs.sentry.io/platforms/php/guides/bref.md)

## Topics

- [Enriching Events](https://docs.sentry.io/platforms/php/guides/symfony/enriching-events.md)
- [Profiling](https://docs.sentry.io/platforms/php/guides/symfony/profiling.md)
- [Tracing](https://docs.sentry.io/platforms/php/guides/symfony/tracing.md)
- [Configuration](https://docs.sentry.io/platforms/php/guides/symfony/configuration.md)
- [Logs](https://docs.sentry.io/platforms/php/guides/symfony/logs.md)
- [Integrations](https://docs.sentry.io/platforms/php/guides/symfony/integrations.md)
- [Troubleshooting](https://docs.sentry.io/platforms/php/guides/symfony/troubleshooting.md)
- [Crons](https://docs.sentry.io/platforms/php/guides/symfony/crons.md)
- [Data Management](https://docs.sentry.io/platforms/php/guides/symfony/data-management.md)
- [Application Metrics](https://docs.sentry.io/platforms/php/guides/symfony/metrics.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/php/guides/symfony/security-policy-reporting.md)
- [User Feedback](https://docs.sentry.io/platforms/php/guides/symfony/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/php/guides/symfony/feature-flags.md)
- [Usage](https://docs.sentry.io/platforms/php/guides/symfony/usage.md)

