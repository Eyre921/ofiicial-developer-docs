---
title: "Symfony"
source: https://docs.sentry.io/platforms/php/guides/symfony.md
path: platforms/php/guides/symfony
---

---
title: "Symfony"
description: "Symfony is a set of reusable PHP components and a PHP framework to build web applications and services. Learn how to set it up with Sentry."
url: https://docs.sentry.io/platforms/php/guides/symfony/
---

# Sentry for Symfony

## [Prerequisites](https://docs.sentry.io/platforms/php/guides/symfony.md#prerequisites)

* You need a [Sentry account](https://sentry.io/signup/) and project
* Your Symfony application needs to run on PHP 7.2 or later

## [Install](https://docs.sentry.io/platforms/php/guides/symfony.md#install)

Install the `sentry/sentry-symfony` bundle:

```bash
composer require sentry/sentry-symfony
```

If you're already using [Monolog](https://github.com/Seldaek/monolog), see the [Monolog integration docs](https://docs.sentry.io/platforms/php/guides/symfony/integrations/monolog.md) for Monolog-related configuration.

## [Configure](https://docs.sentry.io/platforms/php/guides/symfony.md#configure)

Add your DSN to your `.env` file:

```plain
###> sentry/sentry-symfony ###
SENTRY_DSN="https://<key>@o<orgId>.ingest.sentry.io/<projectId>"
###< sentry/sentry-symfony ###
```

When using Symfony Flex, the Sentry bundle is configured to be enabled in the `prod` environment only by default. You can change this behaviour in your `config/packages/sentry.yaml` and `config/bundles.php` files.

In order to receive stack trace arguments in your errors, make sure to set `zend.exception_ignore_args: Off` in your php.ini

## [Verify](https://docs.sentry.io/platforms/php/guides/symfony.md#verify)

To test that Sentry is capturing unhandled exceptions, you can create the following controller:

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

After you visit the `/_sentry-test` page, you can view and resolve the recorded error by logging into [sentry.io](https://sentry.io) and opening your project.

## [Next Steps](https://docs.sentry.io/platforms/php/guides/symfony.md#next-steps)

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup

## Other PHP Frameworks

- [Laravel](https://docs.sentry.io/platforms/php/guides/laravel.md)

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

