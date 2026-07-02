---
title: "Send emails with PHP"
source: https://resend.com/docs/send-with-php
path: docs/send-with-php
---

Learn how to send your first email using the Resend PHP SDK.

## Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

Prefer watching a video? Check out this video walkthrough below.

<YouTube />

## 1. Install

Get the Resend PHP SDK.

```bash Composer theme={"theme":{"light":"github-light","dark":"vesper"}}
composer require resend/resend-php
```

## 2. Send email using HTML

The easiest way to send an email is by using the `html` parameter.

```php index.php theme={"theme":{"light":"github-light","dark":"vesper"}}
<?php

require __DIR__ . '/vendor/autoload.php';

$resend = Resend::client('re_xxxxxxxxx');

$resend->emails->send([
  'from' => 'Acme <onboarding@resend.dev>',
  'to' => ['delivered@resend.dev'],
  'subject' => 'hello world',
  'html' => '<strong>it works!</strong>',
]);
```

## 3. Try it yourself

<CardGroup>
  <Card title="Basic Send" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/send">
    Basic, batch, and prevent-threading send
  </Card>

  <Card title="Attachments" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/attachments">
    File attachments and inline images (CID)
  </Card>

  <Card title="Scheduling" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/scheduling">
    Schedule emails for future delivery
  </Card>

  <Card title="Templates" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/templates">
    Send emails using Resend hosted templates
  </Card>

  <Card title="Double Opt-in" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/double-optin">
    Double opt-in subscription flow
  </Card>

  <Card title="Inbound Webhooks" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/inbound">
    Receive and process inbound emails
  </Card>

  <Card title="Audiences" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/audiences">
    Manage contacts and audiences
  </Card>

  <Card title="Domains" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/src/domains">
    Create and manage sending domains
  </Card>

  <Card title="Symfony App" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/php-resend-examples/symfony_app">
    Full Symfony web application
  </Card>
</CardGroup>
