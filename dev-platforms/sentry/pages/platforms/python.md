---
title: "Python"
source: https://docs.sentry.io/platforms/python.md
path: platforms/python
---

---
title: "Python"
description: "Learn how to set up Sentry in your Python app, capture your first events and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/python/
---

# Sentry for Python

##### Using a framework?

This guide focuses on plain Python. If you're working with Django, FastAPI, Starlette, or any other web framework, choose the respective guide from the list of supported [frameworks](https://docs.sentry.io/platforms/python/integrations.md#web-frameworks).

## [Prerequisites](https://docs.sentry.io/platforms/python.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)
* Your application up and running
* Python `3.6` or above

## [Install](https://docs.sentry.io/platforms/python.md#install)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
pip install "sentry-sdk"
```

*Other available variations of the above snippet: uv, poetry*

This guide requires `sentry-sdk` version 2.70.0 or later. If you already have the SDK installed, upgrade it with `pip install --upgrade sentry-sdk`.

## [Configure](https://docs.sentry.io/platforms/python.md#configure)

**Error Monitoring** starts working as soon as you call `sentry_sdk.init()`. **Logs** and **Application Metrics** need no extra configuration when using `sentry_sdk.logger` and `sentry_sdk.metrics`, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/python.md#send-logs) and [#4](https://docs.sentry.io/platforms/python.md#send-application-metrics-). This guide also enables **Tracing** and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/python.md#initialize-the-sentry-sdk)

Configuration should happen as **early as possible** in your application's lifecycle.

Import and initialize the SDK in your app's entry point:

The snippet also turns on:

* Collection of user data, such as the user's IP address: via [`data_collection`](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection)
* Tracing: via [`traces_sample_rate`](https://docs.sentry.io/platforms/python/configuration/options.md#traces_sample_rate)
* Profiling: via [`profile_session_sample_rate`](https://docs.sentry.io/platforms/python/configuration/options.md#profile_session_sample_rate) and [`profile_lifecycle`](https://docs.sentry.io/platforms/python/configuration/options.md#profile_lifecycle)

Don't need a feature? Remove its options from the snippet.

```python
import sentry_sdk
sentry_sdk.init(
    dsn="https://<key>@o<orgId>.ingest.sentry.io/<projectId>",

    # Check https://docs.sentry.io/platforms/python/data-management/data-collected/ to configure what data is collected
    data_collection={
        "user_info": True,
    },

    # Enables Tracing.
    # Set to 1.0 to capture 100% of spans for tracing.
    # We recommend reducing this value in production.
    traces_sample_rate=1.0,

    # Enables Profiling.
    # Set to 1.0 to profile 100% of sessions.
    profile_session_sample_rate=1.0,
    # Profiles are collected while a transaction is active.
    profile_lifecycle="trace",
)
```

In async programs, add the [`AsyncioIntegration`](https://docs.sentry.io/platforms/python/integrations/asyncio.md) to instrument your async code. This integration isn't enabled by default. Call `sentry_sdk.init()` at the beginning of the first `async` function you call:

```python
import asyncio
import sentry_sdk
from sentry_sdk.integrations.asyncio import AsyncioIntegration

async def main():
    sentry_sdk.init(
        ...,  # same options as above
        integrations=[AsyncioIntegration()],
    )

asyncio.run(main())
```

### [Instrumenting Your App](https://docs.sentry.io/platforms/python.md#instrumenting-your-app)

The Sentry SDK automatically enables integrations for [many popular libraries](https://docs.sentry.io/platforms/python/tracing/instrumentation/automatic-instrumentation.md), so operations like HTTP requests or database queries made with supported libraries will be captured as spans automatically.

However, spans are only created within an existing transaction. If you're not using a supported framework that creates transactions automatically, you'll need to create them manually using `sentry_sdk.start_transaction()`.

See [Custom Instrumentation](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md) for more info.

```python
import sentry_sdk

def some_function():
    with sentry_sdk.start_transaction(op="task", name="Test Transaction"):
        ...
```

## [Send Logs](https://docs.sentry.io/platforms/python.md#send-logs)

Use `sentry_sdk.logger` to send structured logs at different levels. You can include searchable attributes with each message.

To capture records from Python's standard-library `logging` module or Loguru, configure `capture_sentry_logs=True` on the corresponding integration. See the [standard logging](https://docs.sentry.io/platforms/python/integrations/logging.md) and [Loguru](https://docs.sentry.io/platforms/python/integrations/loguru.md) integration guides.

See [Set Up Logs](https://docs.sentry.io/platforms/python/logs.md) for all available logging methods and formatting options.

```python
import sentry_sdk

sentry_sdk.logger.info("Order processed {order_id}", order_id="order-123")
sentry_sdk.logger.warning("Rate limit reached", attributes={"endpoint": "/api/orders"})
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/python.md#send-application-metrics-)

Use `sentry_sdk.metrics` to send counters, gauges, and distributions from your app. Metrics are enabled by default after you initialize the SDK.

See [Set Up Metrics](https://docs.sentry.io/platforms/python/metrics.md) for all available metric types and configuration options.

```python
import sentry_sdk

sentry_sdk.metrics.count("checkout.failed", 1)
sentry_sdk.metrics.gauge("active_connections", 42)
sentry_sdk.metrics.distribution("api_latency", 187, unit="millisecond")
```

## [Verify Your Setup](https://docs.sentry.io/platforms/python.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

Run this code after `sentry_sdk.init()` to send a test error, along with a trace, a log, and a metric:

```python
import sentry_sdk

with sentry_sdk.start_transaction(op="test", name="Verify Sentry setup"):
    sentry_sdk.logger.info("Sentry verification log")
    sentry_sdk.metrics.count("sentry.verification", 1)
    1 / 0
```

The SDK sends profiles after a transaction finishes, so a script that exits right away, like the one above, might not send a profile. Profiles appear for applications that keep running after their transactions complete.

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/python.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Next Steps](https://docs.sentry.io/platforms/python.md#next-steps)

At this point, you should have integrated Sentry into your Python application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/python/agent-tracing.md) to monitor your AI systems
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/python/usage.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/python/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

## Frameworks

- [Django](https://docs.sentry.io/platforms/python/integrations/django.md)
- [Flask](https://docs.sentry.io/platforms/python/integrations/flask.md)
- [FastAPI](https://docs.sentry.io/platforms/python/integrations/fastapi.md)
- [AIOHTTP](https://docs.sentry.io/platforms/python/integrations/aiohttp.md)
- [Bottle](https://docs.sentry.io/platforms/python/integrations/bottle.md)
- [Falcon](https://docs.sentry.io/platforms/python/integrations/falcon.md)
- [Pyramid](https://docs.sentry.io/platforms/python/integrations/pyramid.md)
- [Quart](https://docs.sentry.io/platforms/python/integrations/quart.md)
- [Sanic](https://docs.sentry.io/platforms/python/integrations/sanic.md)
- [Starlette](https://docs.sentry.io/platforms/python/integrations/starlette.md)
- [Starlite](https://docs.sentry.io/platforms/python/integrations/starlite.md)
- [Litestar](https://docs.sentry.io/platforms/python/integrations/litestar.md)
- [Tornado](https://docs.sentry.io/platforms/python/integrations/tornado.md)

## Topics

- [Capturing Errors](https://docs.sentry.io/platforms/python/usage.md)
- [Logs](https://docs.sentry.io/platforms/python/logs.md)
- [Tracing](https://docs.sentry.io/platforms/python/tracing.md)
- [Agent Tracing](https://docs.sentry.io/platforms/python/agent-tracing.md)
- [Application Metrics](https://docs.sentry.io/platforms/python/metrics.md)
- [Profiling](https://docs.sentry.io/platforms/python/profiling.md)
- [Crons](https://docs.sentry.io/platforms/python/crons.md)
- [User Feedback](https://docs.sentry.io/platforms/python/user-feedback.md)
- [Feature Flags](https://docs.sentry.io/platforms/python/feature-flags.md)
- [Sampling](https://docs.sentry.io/platforms/python/sampling.md)
- [Enriching Events](https://docs.sentry.io/platforms/python/enriching-events.md)
- [Legacy SDK](https://docs.sentry.io/platforms/python/legacy-sdk.md)
- [Extended Configuration](https://docs.sentry.io/platforms/python/configuration.md)
- [Integrations](https://docs.sentry.io/platforms/python/integrations.md)
- [Integrations](https://docs.sentry.io/platforms/python/integrations__v2.x.md)
- [Data Management](https://docs.sentry.io/platforms/python/data-management.md)
- [Security Policy Reporting](https://docs.sentry.io/platforms/python/security-policy-reporting.md)
- [Migration Guide](https://docs.sentry.io/platforms/python/migration.md)
- [Troubleshooting](https://docs.sentry.io/platforms/python/troubleshooting.md)

