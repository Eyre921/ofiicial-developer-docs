---
title: "FastAPI"
source: https://docs.sentry.io/platforms/python/integrations/fastapi.md
path: platforms/python/integrations/fastapi
---

---
title: "FastAPI"
description: "Learn how to set up Sentry in your FastAPI app, capture your first events and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/python/integrations/fastapi/
---

# FastAPI for Python

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Prerequisites](https://docs.sentry.io/platforms/python/integrations/fastapi.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)

* Your application up and running

* FastAPI:

  * `0.79.0+` (SDK <3.0)
  * `0.85.0+` (SDK 3.0+)

* Python `3.7+`

## [Install](https://docs.sentry.io/platforms/python/integrations/fastapi.md#install)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
pip install "sentry-sdk"
```

*Other available variations of the above snippet: uv, poetry*

This guide requires `sentry-sdk` version 2.70.0 or later. If you already have the SDK installed, upgrade it with `pip install --upgrade sentry-sdk`.

## [Configure](https://docs.sentry.io/platforms/python/integrations/fastapi.md#configure)

**Error Monitoring** starts working as soon as you call `sentry_sdk.init()`. **Logs** and **Application Metrics** need no extra configuration when using `sentry_sdk.logger` and `sentry_sdk.metrics`, and you'll learn how to send them in steps [#3](https://docs.sentry.io/platforms/python/integrations/fastapi.md#send-logs) and [#4](https://docs.sentry.io/platforms/python/integrations/fastapi.md#send-application-metrics-). This guide also enables **Tracing** and **Profiling**.

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and crashes. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/python/integrations/fastapi.md#initialize-the-sentry-sdk)

Configuration should happen as **early as possible** in your application's lifecycle.

If you have the `fastapi` package in your dependencies, the Sentry FastAPI integration will be enabled automatically when you initialize the Sentry SDK.

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

To further customize your setup, review the [Options section](https://docs.sentry.io/platforms/python/integrations/fastapi.md#options) below.

### [Capturing Errors](https://docs.sentry.io/platforms/python/integrations/fastapi.md#capturing-errors)

Sentry automatically captures errors and reports issues for you. You can also expect the following for your FastAPI project:

* By default, all exceptions leading to an Internal Server Error are captured and reported. The HTTP status codes to report on are configurable via the `failed_request_status_codes` [option](https://docs.sentry.io/platforms/python/integrations/fastapi.md#options).
* Request data will be attached to all events: HTTP method, URL, headers, form data, JSON payloads. Sentry excludes raw bodies and multipart file uploads.
* Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

To learn how to manually report issues, see [Capturing Errors](https://docs.sentry.io/platforms/python/usage.md).

### [Instrumenting Your App](https://docs.sentry.io/platforms/python/integrations/fastapi.md#instrumenting-your-app)

The Sentry SDK automatically monitors the following parts of your FastAPI project:

* Middleware stack
* Middleware `send` and `receive` callbacks
* Database queries
* Redis commands

You can also manually capture performance data – see [Custom Instrumentation](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md) to learn more.

## [Send Logs](https://docs.sentry.io/platforms/python/integrations/fastapi.md#send-logs)

Use `sentry_sdk.logger` to send structured logs at different levels. You can include searchable attributes with each message.

To capture records from Python's standard-library `logging` module or Loguru, configure `capture_sentry_logs=True` on the corresponding integration. See the [standard logging](https://docs.sentry.io/platforms/python/integrations/logging.md) and [Loguru](https://docs.sentry.io/platforms/python/integrations/loguru.md) integration guides.

See [Set Up Logs](https://docs.sentry.io/platforms/python/logs.md) for all available logging methods and formatting options.

```python
import sentry_sdk

sentry_sdk.logger.info("Order processed {order_id}", order_id="order-123")
sentry_sdk.logger.warning("Rate limit reached", attributes={"endpoint": "/api/orders"})
```

## [Send Application Metrics NEW](https://docs.sentry.io/platforms/python/integrations/fastapi.md#send-application-metrics-)

Use `sentry_sdk.metrics` to send counters, gauges, and distributions from your app. Metrics are enabled by default after you initialize the SDK.

See [Set Up Metrics](https://docs.sentry.io/platforms/python/metrics.md) for all available metric types and configuration options.

```python
import sentry_sdk

sentry_sdk.metrics.count("checkout.failed", 1)
sentry_sdk.metrics.gauge("active_connections", 42)
sentry_sdk.metrics.distribution("api_latency", 187, unit="millisecond")
```

## [Verify Your Setup](https://docs.sentry.io/platforms/python/integrations/fastapi.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

Add this route to your FastAPI app, then request `/sentry-debug`:

```python
@app.get("/sentry-debug")
async def trigger_error():
    1 / 0
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/python/integrations/fastapi.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page to see your slowest functions and an aggregate flame graph of your most frequent code paths. If tracing is enabled, select a transaction to see the flame graph for that part of your app. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Options](https://docs.sentry.io/platforms/python/integrations/fastapi.md#options)

In stream mode, these options still work as described, but apply to service spans instead of transactions.

Add `FastApiIntegration` to your `sentry_sdk.init()` call to set options for `FastApiIntegration` to change its behavior.

Because FastAPI is based on the Starlette framework, both integrations, `StarletteIntegration` and `FastApiIntegration`, must be instantiated.

```python
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    # same as above
    integrations=[
        StarletteIntegration(
            transaction_style="endpoint",
            failed_request_status_codes={403, *range(500, 599)},
            http_methods_to_capture=("GET",),
        ),
        FastApiIntegration(
            transaction_style="endpoint",
            failed_request_status_codes={403, *range(500, 599)},
            http_methods_to_capture=("GET",),
        ),
    ]
)
```

You can pass the following keyword arguments to `StarletteIntegration()` and `FastApiIntegration()`:

### [transaction\_style](https://docs.sentry.io/platforms/python/integrations/fastapi.md#transaction_style)

| Type    | `string` |
| ------- | -------- |
| Default | `"url"`  |

How to name transactions that show up in Sentry tracing. The default is `"url"`.

In the code example, the transaction name will be:

* `"/catalog/product/{product_id}"` if you set `transaction_style="url"`
* `"product_detail"` if you set `transaction_style="endpoint"`

```python
  import sentry_sdk
  from sentry_sdk.integrations.starlette import StarletteIntegration
  from sentry_sdk.integrations.fastapi import FastApiIntegration

  sentry_sdk.init(
      # ...
      integrations=[
          StarletteIntegration(
              transaction_style="endpoint",
          ),
          FastApiIntegration(
              transaction_style="endpoint",
          ),
      ],
  )

  app = FastAPI()

  @app.get("/catalog/product/{product_id}")
  async def product_detail(product_id):
      return {...}
```

### [failed\_request\_status\_codes](https://docs.sentry.io/platforms/python/integrations/fastapi.md#failed_request_status_codes)

| Type    | `set[int]`           |
| ------- | -------------------- |
| Default | `{*range(500, 600)}` |

A `set` of integers that determine which status codes should be reported to Sentry.

The `failed_request_status_codes` option determines whether [`HTTPException`](https://fastapi.tiangolo.com/reference/exceptions/?h=httpexception) exceptions should be reported to Sentry. Unhandled exceptions that don't have a `status_code` attribute will always be reported to Sentry.

Examples of valid `failed_request_status_codes`:

* `{500}` will only send events on HTTP 500.
* `{400, *range(500, 600)}` will send events on HTTP 400 as well as the 5xx range.
* `{500, 503}` will send events on HTTP 500 and 503.
* `set()` (the empty set) will not send events for any HTTP status code.

The default is `{*range(500, 600)}`, meaning that all 5xx status codes are reported to Sentry.

### [middleware\_spans](https://docs.sentry.io/platforms/python/integrations/fastapi.md#middleware_spans)

| Type    | `bool`  |
| ------- | ------- |
| Default | `False` |

Create spans and track performance of all middleware layers in your FastAPI project. Set to `True` to enable. The default is `False`.

### [http\_methods\_to\_capture](https://docs.sentry.io/platforms/python/integrations/fastapi.md#http_methods_to_capture)

| Available since | `2.15.0`                                                         |
| --------------- | ---------------------------------------------------------------- |
| Type            | `Tuple[str, ...]`                                                |
| Default         | `("CONNECT", "DELETE", "GET", "PATCH", "POST", "PUT", "TRACE",)` |

A tuple containing all the HTTP methods (as uppercase strings) that should create a transaction in Sentry. The default is `("CONNECT", "DELETE", "GET", "PATCH", "POST", "PUT", "TRACE",)`.

Note that `OPTIONS` and `HEAD` are excluded by default.

## [Next Steps](https://docs.sentry.io/platforms/python/integrations/fastapi.md#next-steps)

At this point, you should have integrated Sentry into your FastAPI application. Here's what to explore next:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* [Set up Agent Tracing](https://docs.sentry.io/platforms/python/agent-tracing.md) to monitor your AI systems
* Learn how to [manually capture errors](https://docs.sentry.io/platforms/python/usage.md)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/python/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

