---
title: "DelayedJob"
source: https://docs.sentry.io/platforms/ruby/guides/delayed_job.md
path: platforms/ruby/guides/delayed_job
---

---
title: "DelayedJob"
description: "Learn how to set up Sentry in your app, capture your first errors and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/ruby/guides/delayed_job/
---

# Sentry for DelayedJob

##### Using a framework?

Check out the other SDKs we support in the left-hand dropdown.

## [Prerequisites](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Ruby `2.4+` or any of the most recent JRuby versions

## [Install](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#install)

Installing the Sentry SDK enables core features such as **Error Monitoring** and **Application Metrics** by default. We'll show you how to send metrics in [Verify Your Setup](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#verify-your-setup).

Choose additional features you want to configure, and this guide will show you how to get set up:

Error Monitoring\[ ]Tracing\[ ]Profiling

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Install the Sentry SDK](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#install-the-sentry-sdk)

Add the `sentry-ruby` and `sentry-delayed_job` gems to your `Gemfile`:

```ruby
gem "sentry-ruby"
gem "sentry-delayed_job"
```

Add the `sentry-ruby`, `sentry-delayed_job` and `stackprof` gems to your `Gemfile`:

```ruby
gem "stackprof"
gem "sentry-ruby"
gem "sentry-delayed_job"
```

## [Configure](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#configure)

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#initialize-the-sentry-sdk)

Configuration should happen as early as possible in your application's lifecycle.

Import and initialize the SDK in your app's entry point:

```ruby
require 'sentry-ruby'

Sentry.init do |config|
  config.dsn = 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>'

  # Get breadcrumbs from logs
  # Learn more at
  # https://docs.sentry.io/platforms/ruby/configuration/options/#breadcrumbs_logger
  config.breadcrumbs_logger = [:sentry_logger, :http_logger]
  # ___PRODUCT_OPTION_START___ performance

  # Set tracesSampleRate to 1.0 to capture 100%
  # of transactions for tracing.
  # We recommend adjusting this value in production
  # Learn more at
  # https://docs.sentry.io/platforms/ruby/configuration/options/#traces_sample_rate
  config.traces_sample_rate = 1.0
  # ___PRODUCT_OPTION_END___ performance
  # ___PRODUCT_OPTION_START___ profiling

  # Enable profiling for a percentage of sessions relative to traces_sample_rate.
  # Learn more at
  # https://docs.sentry.io/platforms/ruby/configuration/options/#profiles_sample_rate
  config.profiles_sample_rate = 1.0
  # ___PRODUCT_OPTION_END___ profiling
end
```

### [Control the Data You Send to Sentry (Optional)](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#control-the-data-you-send-to-sentry-optional)

By default, the SDK does **not** send user identity data (IP address, ID, and similar) or other data like HTTP bodies and URL query parameters.

To opt in and get richer debugging context, turn on individual categories using the `data_collection` option. For the full list of categories and their defaults, [see the `data_collection` options](https://docs.sentry.io/platforms/ruby/guides/delayed_job/configuration/options.md#data_collection).

```ruby
require 'sentry-ruby'

Sentry.init do |config|
  config.dsn = 'https://<key>@o<orgId>.ingest.sentry.io/<projectId>'

  config.data_collection.user_info = true
  config.data_collection.http_bodies = [:incoming_request, :outgoing_request]
  # other categories
end
```

## [Verify Your Setup](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

### [Issues](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#issues)

To verify that Sentry captures errors and creates issues in your Sentry project, add this intentional error to your application:

```ruby

begin
  1 / 0
rescue ZeroDivisionError => exception
  Sentry.capture_exception(exception)
end
```

### [Tracing](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#tracing)

To test your tracing configuration, create a custom transaction and span:

```ruby

Sentry.start_transaction(op: "task", name: "Transaction Name") do |transaction|
  Sentry.get_current_scope.set_span(transaction)

  Sentry.with_child_span(description: "Custom Span Name") do |span|
    # your instrumented code here
  end
end
```

### [Metrics NEW](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#metrics-)

Send test metrics from your app to verify that metrics are arriving in Sentry using the `Sentry.metrics` APIs.

You can also send Yabeda metrics to Sentry automatically using our [Yabeda integration](https://docs.sentry.io/platforms/ruby/guides/delayed_job/integrations/yabeda.md).

```ruby

Sentry.metrics.count("checkout.failed", 1)
Sentry.metrics.gauge("queue.depth", 42)
Sentry.metrics.distribution("cart.amount_usd", 187.5)
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page, select a transaction, and then a profile ID to view its flame graph. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/ruby/guides/delayed_job.md#next-steps)

At this point, you should have integrated Sentry into your application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Continue to [customize your configuration](https://docs.sentry.io/platforms/ruby/guides/delayed_job/configuration.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/ruby/guides/delayed_job/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Other Ruby Frameworks

- [Rack Middleware](https://docs.sentry.io/platforms/ruby/guides/rack.md)
- [Rails](https://docs.sentry.io/platforms/ruby/guides/rails.md)
- [Resque](https://docs.sentry.io/platforms/ruby/guides/resque.md)
- [Sidekiq](https://docs.sentry.io/platforms/ruby/guides/sidekiq.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/ruby/guides/delayed_job/usage.md)
- [Tracing](https://docs.sentry.io/platforms/ruby/guides/delayed_job/tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/ruby/guides/delayed_job/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/ruby/guides/delayed_job/profiling.md)
- [Crons](https://docs.sentry.io/platforms/ruby/guides/delayed_job/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/ruby/guides/delayed_job/user-feedback.md)
- [Enriching Events](https://docs.sentry.io/platforms/ruby/guides/delayed_job/enriching-events.md)
- [Extended Configuration](https://docs.sentry.io/platforms/ruby/guides/delayed_job/configuration.md)
- [Integrations](https://docs.sentry.io/platforms/ruby/guides/delayed_job/integrations.md)
- [Data Management](https://docs.sentry.io/platforms/ruby/guides/delayed_job/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/ruby/guides/delayed_job/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/ruby/guides/delayed_job/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/ruby/guides/delayed_job/troubleshooting.md)

