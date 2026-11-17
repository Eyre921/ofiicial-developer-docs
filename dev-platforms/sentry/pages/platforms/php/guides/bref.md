---
title: "Bref"
source: https://docs.sentry.io/platforms/php/guides/bref.md
path: platforms/php/guides/bref
---

---
title: "Bref"
description: "Monitor PHP applications running on AWS Lambda with Bref and Sentry."
url: https://docs.sentry.io/platforms/php/guides/bref/
---

# Sentry for Bref

[Bref](https://bref.sh) runs PHP applications on AWS Lambda. Some Lambda errors occur outside your application code, where the Sentry SDK alone can't capture them. The `sentry/sentry-bref` package extends the Sentry SDK for PHP, Laravel, or Symfony with support for:

* [Lambda errors](https://docs.sentry.io/platforms/php/guides/bref/usage.md) that happen outside PHP-FPM, like timeouts
* [Exceptions](https://docs.sentry.io/platforms/php/guides/bref/usage.md) and [transactions](https://docs.sentry.io/platforms/php/guides/bref/tracing/automatic-instrumentation.md) for event handlers (SQS, EventBridge, S3, and so on)
* [Cold starts](https://docs.sentry.io/platforms/php/guides/bref/tracing/automatic-instrumentation.md) in your transactions
* [AWS SDK calls](https://docs.sentry.io/platforms/php/guides/bref/tracing/aws-sdk.md) as spans and breadcrumbs

For all other SDK features and configuration, follow the [PHP](https://docs.sentry.io/platforms/php.md), [Laravel](https://docs.sentry.io/platforms/php/guides/laravel.md), or [Symfony](https://docs.sentry.io/platforms/php/guides/symfony.md) docs.

## [Prerequisites](https://docs.sentry.io/platforms/php/guides/bref.md#prerequisites)

* You need a [Sentry account](https://sentry.io/signup/) and project
* Your application needs to run on Bref 3 and PHP 8.2 or later
* Your Laravel version needs to be 12.x or higher, and your Symfony version 6.4 or higher
* Sentry needs to be set up in your application: follow the [PHP](https://docs.sentry.io/platforms/php.md), [Laravel](https://docs.sentry.io/platforms/php/guides/laravel.md), or [Symfony](https://docs.sentry.io/platforms/php/guides/symfony.md) guide first

## [Install](https://docs.sentry.io/platforms/php/guides/bref.md#install)

Install the `sentry/sentry-bref` package:

```bash
composer require sentry/sentry-bref
```

## [Configure](https://docs.sentry.io/platforms/php/guides/bref.md#configure)

Your Lambda functions need the DSN at runtime. Deploy it in your `.env` file, or set it as an environment variable in `serverless.yml`:

```yaml
provider:
  environment:
    # SENTRY_LARAVEL_DSN for Laravel
    SENTRY_DSN: https://<key>@o<orgId>.ingest.sentry.io/<projectId>
```

Transactions, cold starts, and AWS SDK spans are only sent when [tracing](https://docs.sentry.io/platforms/php/guides/bref/tracing.md) is enabled.

The integration adds the cold start to the transaction of the request. To do that, it needs to hook into your framework.

### [Laravel](https://docs.sentry.io/platforms/php/guides/bref.md#laravel)

No action is required, since Laravel discovers the integration's service provider automatically.

### [Symfony](https://docs.sentry.io/platforms/php/guides/bref.md#symfony)

Register the bundle:

```php
return [
    // ...
    Sentry\Bref\Symfony\BrefSentryBundle::class => ['all' => true],
];
```

### [Other Frameworks](https://docs.sentry.io/platforms/php/guides/bref.md#other-frameworks)

Add the `Sentry\Bref\Psr15\BrefSentryMiddleware` PSR-15 middleware to your HTTP middleware stack.

## [Verify](https://docs.sentry.io/platforms/php/guides/bref.md#verify)

Deploy your application, then run the `sentry:test` command on Lambda:

```bash
serverless bref:cli --args="sentry:test"
```

With [Bref Cloud](https://bref.sh/cloud), run `bref command "sentry:test"` instead.

The test event shows up in Sentry with the details of the Lambda function and a link to the logs of the invocation in CloudWatch.

In other applications, throw an exception in one of your routes or event handlers.

## [Next Steps](https://docs.sentry.io/platforms/php/guides/bref.md#next-steps)

* Learn what the integration reports in [Usage](https://docs.sentry.io/platforms/php/guides/bref/usage.md) and [Tracing](https://docs.sentry.io/platforms/php/guides/bref/tracing.md)
* Trace your [AWS SDK calls](https://docs.sentry.io/platforms/php/guides/bref/tracing/aws-sdk.md)
* Learn more about [Bref](https://bref.sh/docs)
* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other PHP Frameworks

- [Laravel](https://docs.sentry.io/platforms/php/guides/laravel.md)
- [Symfony](https://docs.sentry.io/platforms/php/guides/symfony.md)

## Topics

- [Tracing](https://docs.sentry.io/platforms/php/guides/bref/tracing.md)
- [Usage](https://docs.sentry.io/platforms/php/guides/bref/usage.md)

