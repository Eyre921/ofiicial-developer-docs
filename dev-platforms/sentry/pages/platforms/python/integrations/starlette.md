---
title: "Starlette"
source: https://docs.sentry.io/platforms/python/integrations/starlette.md
path: platforms/python/integrations/starlette
---

---
title: "Starlette"
description: "Learn how to set up Sentry in your Starlette app, capture your first errors and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/python/integrations/starlette/
---

# Starlette for Python

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Prerequisites](https://docs.sentry.io/platforms/python/integrations/starlette.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)

* Your application up and running

* Starlette:

  * `0.16+` (SDK <3.0)
  * `0.20+` (SDK 3.0+)

* Python: `3.7+`

## [Install](https://docs.sentry.io/platforms/python/integrations/starlette.md#install)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
pip install "sentry-sdk"
```

*Other available variations of the above snippet: uv, poetry*

## [Configure](https://docs.sentry.io/platforms/python/integrations/starlette.md#configure)

Choose the features you want to configure, and this guide will show you how:

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Logs\[ ]Metrics

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/python/integrations/starlette.md#initialize-the-sentry-sdk)

Configuration should happen as **early as possible** in your application's lifecycle.

If you have the `starlette` package in your dependencies, the Sentry Starlette integration will be enabled automatically when you initialize the Sentry SDK.

Import and initialize the SDK in your app's entry point:

```python
import sentry_sdk
# ___PRODUCT_OPTION_START___ metrics
from sentry_sdk import metrics
# ___PRODUCT_OPTION_END___ metrics

sentry_sdk.init(
    dsn="https://<key>@o<orgId>.ingest.sentry.io/<projectId>",
    # Check https://docs.sentry.io/platforms/python/data-management/data-collected/ to configure what data is collected
    data_collection={
        "user_info": True,
    },
    # ___PRODUCT_OPTION_START___ performance
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # ___PRODUCT_OPTION_END___ performance
    # ___PRODUCT_OPTION_START___ profiling
    # To collect profiles for all profile sessions,
    # set `profile_session_sample_rate` to 1.0.
    profile_session_sample_rate=1.0,
    # Profiles will be automatically collected while
    # there is an active span.
    profile_lifecycle="trace",
    # ___PRODUCT_OPTION_END___ profiling
)
```

To further customize your setup, review the [Options section](https://docs.sentry.io/platforms/python/integrations/starlette.md#options) below.

### [Capturing Errors](https://docs.sentry.io/platforms/python/integrations/starlette.md#capturing-errors)

Sentry automatically captures errors and reports issues for you. You can also expect the following for your Starlette project:

* By default, all exceptions leading to an Internal Server Error are reported. The HTTP status codes to report on are configurable via the `failed_request_status_codes` [option](https://docs.sentry.io/platforms/python/integrations/starlette.md#options).
* Request data will be attached to all events: HTTP method, URL, headers, form data, JSON payloads. Sentry excludes raw bodies and multipart file uploads.
* Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

To learn how to manually report issues, see [Capturing Errors](https://docs.sentry.io/platforms/python/usage.md).

## [Verify Your Setup](https://docs.sentry.io/platforms/python/integrations/starlette.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

### [Issues](https://docs.sentry.io/platforms/python/integrations/starlette.md#issues)

To verify that Sentry captures errors and creates issues in your Sentry project, add this intentional error to your application:

```python
from starlette.applications import Starlette
from starlette.routing import Route

sentry_sdk.init(...)  # same as above

async def trigger_error(request):
    division_by_zero = 1 / 0

app = Starlette(routes=[
    Route("/sentry-debug", trigger_error),
])
```

Point your browser to <http://localhost:8000/sentry-debug> to trigger the error which will be sent to Sentry.

### [Tracing](https://docs.sentry.io/platforms/python/integrations/starlette.md#tracing)

To test your tracing configuration, create a custom transaction and span:

```py
import sentry_sdk

with sentry_sdk.start_transaction(op="task", name="Transaction Name"):
    span = sentry_sdk.start_span(name="Custom Span Name")
    span.finish()
```

*Other available variations of the above snippet: Stream Mode*

### [Logs](https://docs.sentry.io/platforms/python/integrations/starlette.md#logs)

To verify that Sentry catches your logs (which are enabled by default), add some log statements to your application:

```python
import sentry_sdk

sentry_sdk.logger.info("This is an info log message")
sentry_sdk.logger.warning("This is a warning message")
sentry_sdk.logger.error("This is an error message")
```

### [Application Metrics NEW](https://docs.sentry.io/platforms/python/integrations/starlette.md#application-metrics-)

Send test metrics from your app to verify that metrics are arriving in Sentry:

```py
from sentry_sdk import metrics

metrics.count("checkout.failed", 1)
metrics.gauge("queue.depth", 42)
metrics.distribution("cart.amount_usd", 187.5)
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/python/integrations/starlette.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page, select a transaction, and then a profile ID to view its flame graph. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Options](https://docs.sentry.io/platforms/python/integrations/starlette.md#options)

In stream mode, these options still work as described, but apply to service spans instead of transactions.

Add `StarletteIntegration` to your `sentry_sdk.init()` call to set options for `StarletteIntegration` to change its behavior.

```python
from sentry_sdk.integrations.starlette import StarletteIntegration

sentry_sdk.init(
    # ...
    integrations=[
        StarletteIntegration(
            transaction_style="endpoint",
            failed_request_status_codes={403, *range(500, 599)},
            middleware_spans=False,
            http_methods_to_capture=("GET",),
        )
    ],
)
```

You can pass the following keyword arguments to `StarletteIntegration()`:

### [transaction\_style](https://docs.sentry.io/platforms/python/integrations/starlette.md#transaction_style)

| Type    | `string` |
| ------- | -------- |
| Default | `"url"`  |

How to name transactions that show up in Sentry tracing. The default is `"url"`.

In the code example, the transaction name will be:

* `"/catalog/product/{product_id}"` if you set `transaction_style="url"`.
* `"product_detail"` if you set `transaction_style="endpoint"`

```python
  async def product_detail(request):
      return JSONResponse({...})

  app = Starlette(routes=[
      Route('/catalog/product/{product_id}', product_detail),
  ])
```

### [failed\_request\_status\_codes](https://docs.sentry.io/platforms/python/integrations/starlette.md#failed_request_status_codes)

| Type    | `set[int]`           |
| ------- | -------------------- |
| Default | `{*range(500, 600)}` |

A `set` of integers that will determine which status codes should be reported to Sentry.

The `failed_request_status_codes` option determines whether [`HTTPException`](https://starlette.dev/exceptions/#httpexception) exceptions should be reported to Sentry. Unhandled exceptions that don't have a `status_code` attribute will always be reported to Sentry.

Examples of valid `failed_request_status_codes`:

* `{500}` will only send events on HTTP 500.
* `{400, *range(500, 600)}` will send events on HTTP 400 as well as the 5xx range.
* `{500, 503}` will send events on HTTP 500 and 503.
* `set()` (the empty set) will not send events for any HTTP status code.

The default is `{*range(500, 600)}`, meaning that all 5xx status codes are reported to Sentry.

### [middleware\_spans](https://docs.sentry.io/platforms/python/integrations/starlette.md#middleware_spans)

| Type    | `bool`  |
| ------- | ------- |
| Default | `False` |

Create spans and track performance of all middleware layers in your project. Set to `True` to enable. The default is `False`.

### [http\_methods\_to\_capture](https://docs.sentry.io/platforms/python/integrations/starlette.md#http_methods_to_capture)

| Available since | `2.15.0`                                                         |
| --------------- | ---------------------------------------------------------------- |
| Type            | `Tuple[str, ...]`                                                |
| Default         | `("CONNECT", "DELETE", "GET", "PATCH", "POST", "PUT", "TRACE",)` |

A tuple containing all the HTTP methods (as uppercase strings) that should create a transaction in Sentry. The default is `("CONNECT", "DELETE", "GET", "PATCH", "POST", "PUT", "TRACE",)`.

Note that `OPTIONS` and `HEAD` are excluded by default.

## [Next Steps](https://docs.sentry.io/platforms/python/integrations/starlette.md#next-steps)

At this point, you should have integrated Sentry into your application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Continue to [customize your configuration](https://docs.sentry.io/platforms/python/configuration.md)
* Learn more about [manually capturing errors or messages](https://docs.sentry.io/platforms/python/usage.md)
* Dive straight into the API with our [API docs](https://getsentry.github.io/sentry-python/)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/python/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

