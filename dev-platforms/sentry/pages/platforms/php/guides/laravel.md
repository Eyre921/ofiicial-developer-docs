---
title: "Laravel"
source: https://docs.sentry.io/platforms/php/guides/laravel.md
path: platforms/php/guides/laravel
---

---
title: "Laravel"
description: "Laravel is a PHP web application framework with expressive, elegant syntax. Learn how to set it up with Sentry."
url: https://docs.sentry.io/platforms/php/guides/laravel/
---

# Sentry for Laravel

## [Prerequisites](https://docs.sentry.io/platforms/php/guides/laravel.md#prerequisites)

* You need a [Sentry account](https://sentry.io/signup/) and project
* Your Laravel application needs to run on PHP 7.2 or later
* Your Laravel version needs to be 11.x or higher
* Read one of these guides if you use an [older version](https://docs.sentry.io/platforms/php/guides/laravel/other-versions.md) or need [Lumen-specific instructions](https://docs.sentry.io/platforms/php/guides/laravel/other-versions/lumen.md)

## [Install](https://docs.sentry.io/platforms/php/guides/laravel.md#install)

Install the `sentry/sentry-laravel` package:

```bash
composer require sentry/sentry-laravel
```

Enable capturing unhandled exception to report to Sentry by making the following change to your `bootstrap/app.php`:

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

If you also want to send structured logs to Sentry, see the [Logs guide](https://docs.sentry.io/platforms/php/guides/laravel/logs.md).

## [Configure](https://docs.sentry.io/platforms/php/guides/laravel.md#configure)

Configure the Sentry DSN with this command:

```shell
php artisan sentry:publish --dsn=https://<key>@o<orgId>.ingest.sentry.io/<projectId>
```

It creates the config file (`config/sentry.php`) and adds the `DSN` to your `.env` file.

```shell
SENTRY_LARAVEL_DSN=https://<key>@o<orgId>.ingest.sentry.io/<projectId>
```

In order to receive stack trace arguments in your errors, make sure to set `zend.exception_ignore_args: Off` in your php.ini

## [Verify](https://docs.sentry.io/platforms/php/guides/laravel.md#verify)

### [Verify With Artisan](https://docs.sentry.io/platforms/php/guides/laravel.md#verify-with-artisan)

You can test your configuration using the provided `sentry:test` artisan command:

```shell
php artisan sentry:test
```

### [Verify With Code](https://docs.sentry.io/platforms/php/guides/laravel.md#verify-with-code)

You can verify that Sentry is capturing errors in your Laravel application by creating a route that will throw an exception:

```php
Route::get('/debug-sentry', function () {
    throw new Exception('My first Sentry error!');
});
```

Visiting this route will trigger an exception that will be captured by Sentry.

## [Tracing](https://docs.sentry.io/platforms/php/guides/laravel.md#tracing)

Set `traces_sample_rate` in `config/sentry.php` or `SENTRY_TRACES_SAMPLE_RATE` in your `.env` to a value greater than `0.0`. Setting a value greater than `0.0` will enable Tracing, `null` (the default) will disable Tracing.

```shell
# Be sure to lower this value in production otherwise you could burn through your quota quickly.
SENTRY_TRACES_SAMPLE_RATE=1.0
```

The example configuration above will transmit 100% of captured traces. Be sure to lower this value in production or you could use up your quota quickly.

You can also be more granular with the sample rate by using the `traces_sampler` option. Learn more in [Using Sampling to Filter Transaction Events](https://docs.sentry.io/platforms/php/guides/laravel/configuration/filtering.md#using-sampling-to-filter-transaction-events).

If your queued jobs generate more traces than your web requests, you can also lower the sample rate for specific jobs with `Sentry\Laravel\Jobs\Middleware\SentryTracesSampleRate`. See [Laravel Options](https://docs.sentry.io/platforms/php/guides/laravel/configuration/laravel-options.md#lower-sample-rate-for-specific-jobs).

Performance data is transmitted using a new event type called "transactions", which you can learn about in [Distributed Tracing](https://docs.sentry.io/concepts/key-terms/tracing/distributed-tracing.md#traces-transactions-and-spans).

## [Local Development and Testing](https://docs.sentry.io/platforms/php/guides/laravel.md#local-development-and-testing)

When Sentry is installed in your application, it will also be active when you are developing or running tests.

You most likely don't want errors to be sent to Sentry when you are developing or running tests. To avoid this, set the DSN value to `null` to disable sending errors to Sentry.

You can also do this by not defining `SENTRY_LARAVEL_DSN` in your `.env` or by defining it as `SENTRY_LARAVEL_DSN=null`.

If you do leave Sentry enabled when developing or running tests, it's possible for it to have a negative effect on the performance of your application or test suite.

## [Set up Sentry through Forge](https://docs.sentry.io/platforms/php/guides/laravel.md#set-up-sentry-through-forge)

If you're using Laravel's Forge platform to provision and deploy your PHP application, you can create a Sentry organization through [Forge](https://forge.laravel.com/docs/integrations/sentry).

## [Next Steps](https://docs.sentry.io/platforms/php/guides/laravel.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other PHP Frameworks

- [Symfony](https://docs.sentry.io/platforms/php/guides/symfony.md)

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

