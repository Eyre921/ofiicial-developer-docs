---
title: "Rack Middleware"
source: https://docs.sentry.io/platforms/ruby/guides/rack.md
path: platforms/ruby/guides/rack
---

---
title: "Rack Middleware"
description: "Learn how to set up Sentry in your app, capture your first events, and view them in Sentry."
url: https://docs.sentry.io/platforms/ruby/guides/rack/
---

# Sentry for Rack Middleware

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

## [Prerequisites](https://docs.sentry.io/platforms/ruby/guides/rack.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Ruby `2.4+` or any of the most recent JRuby versions

## [Install](https://docs.sentry.io/platforms/ruby/guides/rack.md#install)

### [Install the Sentry SDK](https://docs.sentry.io/platforms/ruby/guides/rack.md#install-the-sentry-sdk)

Add the `sentry-ruby` and `stackprof` gems to your `Gemfile` to enable Profiling. Keep `stackprof` before `sentry-ruby` so it loads first:

```ruby
gem "stackprof"
gem "sentry-ruby"
```

## [Configure](https://docs.sentry.io/platforms/ruby/guides/rack.md#configure)

**Error Monitoring** starts working as soon as you call `Sentry.init`. **Application Metrics** need no extra configuration, and you'll learn how to send them in step [#3](https://docs.sentry.io/platforms/ruby/guides/rack.md#send-application-metrics-). This guide also enables **Tracing** and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/ruby/guides/rack.md#initialize-the-sentry-sdk)

#### [With Rackup](https://docs.sentry.io/platforms/ruby/guides/rack.md#with-rackup)

Import and initialize the SDK and add `use Sentry::Rack::CaptureExceptions` to your `config.ru` or other rackup file.

The snippet also turns on:

* Tracing: via [`traces_sample_rate`](https://docs.sentry.io/platforms/ruby/guides/rack/configuration/options.md#traces_sample_rate)
* Profiling: via [`profiles_sample_rate`](https://docs.sentry.io/platforms/ruby/guides/rack/configuration/options.md#profiles_sample_rate) (requires the `stackprof` gem from the Install step)
* Breadcrumbs from logs: via [`breadcrumbs_logger`](https://docs.sentry.io/platforms/ruby/guides/rack/configuration/options.md#breadcrumbs_logger)

Don't need a feature? Remove its options from the snippet.

```ruby
require 'sentry-ruby'

Sentry.init do |config|
  config.dsn = 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>'

  # Add breadcrumbs from logs
  config.breadcrumbs_logger = [:sentry_logger, :http_logger]

  # Enables Tracing.
  # Set to 1.0 to capture 100% of transactions for tracing.
  # We recommend reducing this value in production.
  config.traces_sample_rate = 1.0

  # Enables Profiling for a percentage of sampled transactions.
  # Requires the stackprof gem.
  config.profiles_sample_rate = 1.0
end

use Sentry::Rack::CaptureExceptions
```

#### [Without Rackup](https://docs.sentry.io/platforms/ruby/guides/rack.md#without-rackup)

If you're not using Rackup to run your app, you have to place Sentry's initialization code **before** your code requires Sinatra.

The snippet also turns on:

* Tracing: via [`traces_sample_rate`](https://docs.sentry.io/platforms/ruby/guides/rack/configuration/options.md#traces_sample_rate)
* Profiling: via [`profiles_sample_rate`](https://docs.sentry.io/platforms/ruby/guides/rack/configuration/options.md#profiles_sample_rate) (requires the `stackprof` gem from the Install step)
* Breadcrumbs from logs: via [`breadcrumbs_logger`](https://docs.sentry.io/platforms/ruby/guides/rack/configuration/options.md#breadcrumbs_logger)

Don't need a feature? Remove its options from the snippet.

```ruby
require 'sentry-ruby'

Sentry.init do |config|
  config.dsn = 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>'

  # Add breadcrumbs from logs
  config.breadcrumbs_logger = [:sentry_logger, :http_logger]

  # Enables Tracing.
  # Set to 1.0 to capture 100% of transactions for tracing.
  # We recommend reducing this value in production.
  config.traces_sample_rate = 1.0

  # Enables Profiling for a percentage of sampled transactions.
  # Requires the stackprof gem.
  config.profiles_sample_rate = 1.0
end

# in a non-rackup environment you must initialize the Sentry SDK before requiring sinatra
require 'sinatra'
use Sentry::Rack::CaptureExceptions

get "/" do
  raise "foo"
end
```

### [Control the Data You Send to Sentry](https://docs.sentry.io/platforms/ruby/guides/rack.md#control-the-data-you-send-to-sentry)

By default, the SDK does **not** send user identity data (IP address, ID, and similar) or other data like HTTP bodies and URL query parameters.

To opt in and get richer debugging context, turn on individual categories using the `data_collection` option. For the full list of categories and their defaults, [see the `data_collection` options](https://docs.sentry.io/platforms/ruby/guides/rack/configuration/options.md#data_collection).

```ruby
require 'sentry-ruby'

Sentry.init do |config|
  config.dsn = 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>'

  config.data_collection.user_info = true
  config.data_collection.http_bodies = [:incoming_request, :outgoing_request]
  # other categories
end
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/ruby/guides/rack.md#send-application-metrics-)

Use `Sentry.metrics` to send counters, gauges, and distributions from your app. Add attributes to search and filter metrics later.

See [Set Up Metrics](https://docs.sentry.io/platforms/ruby/guides/rack/metrics.md) for all available metric types and configuration options.

```ruby
Sentry.metrics.count("checkout.failed", value: 1)

Sentry.metrics.gauge(
  "queue.depth",
  42,
  attributes: { queue: "payments" }
)

Sentry.metrics.distribution(
  "api_latency",
  187,
  unit: "millisecond",
  attributes: { endpoint: "/api/orders" }
)
```

If you're using Yabeda, you can use the [`sentry-yabeda` integration](https://docs.sentry.io/platforms/ruby/guides/rack/integrations/yabeda.md) to automatically send Yabeda metrics to Sentry.

## [Verify Your Setup](https://docs.sentry.io/platforms/ruby/guides/rack.md#verify-your-setup)

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

Trigger and capture a test error in your application:

```ruby
begin
  1 / 0
rescue ZeroDivisionError => exception
  Sentry.capture_exception(exception)
end
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/ruby/guides/rack.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/ruby/guides/rack.md#next-steps)

At this point, you should have integrated Sentry into your Ruby application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set Up Tracing](https://docs.sentry.io/platforms/ruby/guides/rack/tracing.md) to learn more about tracing and sampling
* [Set Up Profiling](https://docs.sentry.io/platforms/ruby/guides/rack/profiling.md) to learn how to collect and analyze profiles

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/ruby/guides/rack/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other Ruby Frameworks

- [DelayedJob](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md)
- [Rails](https://docs.sentry.io/platforms/ruby/guides/rails.md)
- [Resque](https://docs.sentry.io/platforms/ruby/guides/resque.md)
- [Sidekiq](https://docs.sentry.io/platforms/ruby/guides/sidekiq.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/ruby/guides/rack/usage.md)
- [Tracing](https://docs.sentry.io/platforms/ruby/guides/rack/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/ruby/guides/rack/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/ruby/guides/rack/profiling.md)
- [Crons](https://docs.sentry.io/platforms/ruby/guides/rack/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/ruby/guides/rack/user-feedback.md)
- [Enriching Events](https://docs.sentry.io/platforms/ruby/guides/rack/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/ruby/guides/rack/configuration.md)
- [Integrations](https://docs.sentry.io/platforms/ruby/guides/rack/integrations.md)
- [Data Management](https://docs.sentry.io/platforms/ruby/guides/rack/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/ruby/guides/rack/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/ruby/guides/rack/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/ruby/guides/rack/troubleshooting.md)

