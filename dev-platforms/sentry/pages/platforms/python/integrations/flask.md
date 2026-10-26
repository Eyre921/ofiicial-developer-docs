---
title: "Flask"
source: https://docs.sentry.io/platforms/python/integrations/flask.md
path: platforms/python/integrations/flask
---

---
title: "Flask"
description: "Learn how to set up Sentry in your Flask app, capture your first errors and traces, and view them in Sentry."
url: https://docs.sentry.io/platforms/python/integrations/flask/
---

# Flask for Python

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Prerequisites](https://docs.sentry.io/platforms/python/integrations/flask.md#prerequisites)

You need:

* A Sentry [account](https://sentry.io/signup/) and [project](https://docs.sentry.io/product/projects.md)

* Your application up and running

* Flask:

  * `1.1.4+` (SDK <3.0)
  * `2.0.0+` (SDK 3.0+)

* Python:

  * `3.6+` (SDK <3.0)
  * `3.7+` (SDK 3.0+)

## [Install](https://docs.sentry.io/platforms/python/integrations/flask.md#install)

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash
pip install "sentry-sdk"
```

*Other available variations of the above snippet: uv, poetry*

## [Configure](https://docs.sentry.io/platforms/python/integrations/flask.md#configure)

Choose the features you want to configure, and this guide will show you how:

Error Monitoring\[ ]Tracing\[ ]Profiling\[ ]Logs\[ ]Metrics

Want to learn more about these features?

* [**Issues**](https://docs.sentry.io/product/issues.md) (always enabled): Sentry's core error monitoring product that automatically reports errors, uncaught exceptions, and unhandled rejections. If you have something that looks like an exception, Sentry can capture it.
* [**Tracing**](https://docs.sentry.io/product/tracing.md): Track software performance while seeing the impact of errors across multiple systems. For example, distributed tracing allows you to follow a request from the frontend to the backend and back.
* [**Profiling**](https://docs.sentry.io/product/profiling.md): Gain deeper insight than traditional tracing without custom instrumentation, letting you discover slow-to-execute or resource-intensive functions in your app.
* [**Logs**](https://docs.sentry.io/product/logs.md): Centralize and analyze your application logs to correlate them with errors and performance issues. Search, filter, and visualize log data to understand what's happening in your applications.
* [**Application Metrics**](https://docs.sentry.io/product/metrics.md) (always enabled): Track and analyze custom application metrics, such as response times and database query durations, to understand trends and patterns in your application's performance and behavior over time.

### [Initialize the Sentry SDK](https://docs.sentry.io/platforms/python/integrations/flask.md#initialize-the-sentry-sdk)

Configuration should happen as **early as possible** in your application's lifecycle.

If you have the `flask` package in your dependencies, the Flask integration will be enabled and installed for all your apps automatically when you initialize the Sentry SDK. The SDK hooks into Flask's signals, not anything on the app object.

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

To further customize your setup, review the [Options section](https://docs.sentry.io/platforms/python/integrations/flask.md#options) below.

### [Capturing Errors](https://docs.sentry.io/platforms/python/integrations/flask.md#capturing-errors)

Sentry automatically captures errors and reports issues for you. You can also expect the following for your Flask app:

* If you use `flask-login`, and you've either enabled `user_info` in the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii=True` in your call to `init`, user data (such as current user ID, email address, username) will be attached to error events. `send_default_pii` will be removed in version 3.0 of the SDK.
* Request data will be attached to all events: HTTP method, URL, headers, form data, JSON payloads. Sentry excludes raw bodies and multipart file uploads.
* Logs emitted by any `app.logger` or *any* logger will be recorded by the [Logging](https://docs.sentry.io/platforms/python/integrations/logging.md) integration (this integration is enabled by default).

Are you using uWSGI?

If you're using uWSGI, note that it doesn't support threads by default. This might lead to unexpected behavior when using the Sentry SDK, from features not working properly to uWSGI workers crashing.

To enable threading support in uWSGI, make sure you have both `--enable-threads` and `--py-call-uwsgi-fork-hooks` on.

Note that automatic tracing on file-like responses when `offloading` is configured is disabled (see [here](https://github.com/getsentry/sentry-python/pull/5556) for why). If you wish to enable tracing on these types of responses, you will need to [manually instrument](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md) them.

## [Verify Your Setup](https://docs.sentry.io/platforms/python/integrations/flask.md#verify-your-setup)

Let's test your setup and confirm that data reaches your Sentry project.

Errors triggered from a Python shell like IPython will not trigger Sentry's error monitoring. Make sure you're running the examples from a file instead.

### [Issues](https://docs.sentry.io/platforms/python/integrations/flask.md#issues)

To verify that Sentry captures errors and creates issues in your Sentry project, add this intentional error to your application:

```python
import sentry_sdk
from flask import Flask

sentry_sdk.init(...)  # same as above

app = Flask(__name__)

@app.route("/")
def hello_world():
    1 / 0  # raises an error
    return "<p>Hello, World!</p>"
```

### [Tracing](https://docs.sentry.io/platforms/python/integrations/flask.md#tracing)

To test your tracing configuration, create a custom transaction and span:

```py
import sentry_sdk

with sentry_sdk.start_transaction(op="task", name="Transaction Name"):
    span = sentry_sdk.start_span(name="Custom Span Name")
    span.finish()
```

*Other available variations of the above snippet: Stream Mode*

### [Logs](https://docs.sentry.io/platforms/python/integrations/flask.md#logs)

To verify that Sentry catches your logs (which are enabled by default), add some log statements to your application:

```python
import sentry_sdk

sentry_sdk.logger.info("This is an info log message")
sentry_sdk.logger.warning("This is a warning message")
sentry_sdk.logger.error("This is an error message")
```

### [Application Metrics NEW](https://docs.sentry.io/platforms/python/integrations/flask.md#application-metrics-)

Send test metrics from your app to verify that metrics are arriving in Sentry:

```py
from sentry_sdk import metrics

metrics.count("checkout.failed", 1)
metrics.gauge("queue.depth", 42)
metrics.distribution("cart.amount_usd", 187.5)
```

### [View Captured Data in Sentry](https://docs.sentry.io/platforms/python/integrations/flask.md#view-captured-data-in-sentry)

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

Need help locating captured data in your Sentry project?

* Open the [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) page and select an error from the issues list to view the full details and context of this error. For more details, see the [Issue Details documentation](https://docs.sentry.io/product/issues/issue-details.md).
* Open the [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) page and select a trace to reveal more information about each span, its duration, and any errors. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/sentry-basics/getting-started-tutorial/generate-first-error.md#ui-walkthrough).
* Open the [**Profiles**](https://sentry.io/orgredirect/organizations/:orgslug/profiling/) page, select a transaction, and then a profile ID to view its flame graph. For more information, click [here](https://docs.sentry.io/product/profiling/profile-details.md).
* Open the [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) page and filter by service, environment, or search keywords to view log entries from your application. For an interactive UI walkthrough, click [here](https://docs.sentry.io/product/logs.md#overview).
* Open the [**Application Metrics**](https://sentry.io/orgredirect/organizations/:orgslug/explore/metrics) page to view and analyze your metrics. For more details, see this [interactive walkthrough](https://docs.sentry.io/product/metrics.md#overview).

## [Options](https://docs.sentry.io/platforms/python/integrations/flask.md#options)

In stream mode, these options still work as described, but apply to service spans instead of transactions.

Add `FlaskIntegration` explicitly to your `sentry_sdk.init()` call to set options for `FlaskIntegration` to change its behavior:

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    # ...
    integrations = [
        FlaskIntegration(
            transaction_style="url",
            http_methods_to_capture=("GET",),
        ),
    ],
)
```

You can pass the following keyword arguments to `FlaskIntegration()`:

### [transaction\_style](https://docs.sentry.io/platforms/python/integrations/flask.md#transaction_style)

| Type    | `string`     |
| ------- | ------------ |
| Default | `"endpoint"` |

How to name transactions that show up in Sentry tracing. The default is `"endpoint"`.

In the code example, the transaction name will be:

* `/myurl/<foo>` if you set `transaction_style="url"`
* `myendpoint` if you set `transaction_style="endpoint"`

```python
    @app.route("/myurl/<foo>")
    def myendpoint():
        return "<p>Hello, World!</p>"
```

### [http\_methods\_to\_capture](https://docs.sentry.io/platforms/python/integrations/flask.md#http_methods_to_capture)

| Available since | `2.15.0`                                                         |
| --------------- | ---------------------------------------------------------------- |
| Type            | `Tuple[str, ...]`                                                |
| Default         | `("CONNECT", "DELETE", "GET", "PATCH", "POST", "PUT", "TRACE",)` |

A tuple containing all the HTTP methods (as uppercase strings) that should create a transaction in Sentry. The default is `("CONNECT", "DELETE", "GET", "PATCH", "POST", "PUT", "TRACE",)`.

Note that `OPTIONS` and `HEAD` are excluded by default.

## [Next Steps](https://docs.sentry.io/platforms/python/integrations/flask.md#next-steps)

At this point, you should have integrated Sentry into your application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

* Explore [practical guides](https://docs.sentry.io/get-started/guides.md) on what to monitor, log, track, and investigate after setup
* Continue to [customize your configuration](https://docs.sentry.io/platforms/python/configuration.md)
* Learn more about [manually capturing errors or messages](https://docs.sentry.io/platforms/python/usage.md)
* Dive straight into the API with our [API docs](https://getsentry.github.io/sentry-python/)

Are you having problems setting up the SDK?

* Find various topics in [Troubleshooting](https://docs.sentry.io/platforms/python/troubleshooting.md)
* [Get support](https://www.sentry.help/en/)

