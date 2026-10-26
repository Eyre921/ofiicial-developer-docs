---
title: "Bottle"
source: https://docs.sentry.io/platforms/python/integrations/bottle.md
path: platforms/python/integrations/bottle
---

---
title: "Bottle"
description: "Learn about using Sentry with Bottle."
url: https://docs.sentry.io/platforms/python/integrations/bottle/
---

# Bottle for Python

The Bottle integration adds support for the [Bottle web framework](https://bottlepy.org/).

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/bottle.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/bottle.md#configure)

If you have the `bottle` package in your dependencies, the Bottle integration will be enabled automatically when you initialize the Sentry SDK.

Error Monitoring\[ ]Tracing\[ ]Profiling

```python
import sentry_sdk

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

## [Verify](https://docs.sentry.io/platforms/python/integrations/bottle.md#verify)

```python
from bottle import Bottle, run

sentry_sdk.init(...)  # same as above

app = Bottle()

@app.route('/')
def hello():
    1 / 0
    return "Hello World!"

run(app, host='localhost', port=8000)
```

When you point your browser to <http://localhost:8000/> a transaction in the Performance section of [sentry.io](https://sentry.io) will be created. Additionally, an error event will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## [Behavior](https://docs.sentry.io/platforms/python/integrations/bottle.md#behavior)

Are you using uWSGI?

If you're using uWSGI, note that it doesn't support threads by default. This might lead to unexpected behavior when using the Sentry SDK, from features not working properly to uWSGI workers crashing.

To enable threading support in uWSGI, make sure you have both `--enable-threads` and `--py-call-uwsgi-fork-hooks` on.

Note that automatic tracing on file-like responses when `offloading` is configured is disabled (see [here](https://github.com/getsentry/sentry-python/pull/5556) for why). If you wish to enable tracing on these types of responses, you will need to [manually instrument](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md) them.

* The Sentry Python SDK will install the Bottle integration for all of your apps. The integration hooks into base Bottle class.

* All exceptions leading to an Internal Server Error are reported.

* Request data is attached to all events: **HTTP method, URL, headers, form data, JSON payloads**. Sentry excludes raw bodies and multipart file uploads. Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

* Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

## [Options](https://docs.sentry.io/platforms/python/integrations/bottle.md#options)

In stream mode, these options still work as described, but apply to service spans instead of transactions.

If you add `BottleIntegration` explicitly to your `sentry_sdk.init()` call you can set options for `BottleIntegration` to change its behavior:

```python
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    # same as above
    integrations=[
        BottleIntegration(
            transaction_style="endpoint",
            failed_request_status_codes={*range(500, 600)},
        ),
    ],
)
```

Each of the following options are supported as keyword arguments to `BottleIntegration()`.

### [`transaction_style`](https://docs.sentry.io/platforms/python/integrations/bottle.md#transaction_style)

The `transaction_style` option specifies how the transaction name is generated. You can set the option to `"endpoint"` (the default) or `"url"`.

For example, given the following route:

```python
@app.route("/myurl/<foo>")
def myendpoint():
    return "ok"
```

* If you set `transaction_style="endpoint"`, the transaction name will be `"myendpoint"`, since that is the route handler function's name.
* If you set `transaction_style="url"`, the transaction name will be `"/myurl/<foo>"`, since that is the URL path.

### [`failed_request_status_codes`](https://docs.sentry.io/platforms/python/integrations/bottle.md#failed_request_status_codes)

A `set` of integers that will determine when an [`HTTPResponse`](https://bottlepy.org/docs/dev/api.html#bottle.HTTPResponse), which is raised or returned by the request handler, should be reported to Sentry. The `HTTPResponse` is reported to Sentry if its status code is contained in the `failed_request_status_codes` set.

Examples of valid values for `failed_request_status_codes`:

* `{500}` will only report `HTTPResponse` with status 500.
* `{400, *range(500, 600)}` will report `HTTPResponse` with status 400 as well as those in the 5xx range.
* `set()` (the empty set) will not report any `HTTPResponse` to Sentry.

The default is `{*range(500, 600)}`, meaning that any `HTTPResponse` with a status in the 5xx range is reported to Sentry.

Regardless of how `failed_request_status_codes` is configured, any non-`HTTPResponse` exceptions raised by the handler are reported to Sentry. For example, if your request handler raises an unhandled `AttributeError`, the `AttributeError` gets reported to Sentry, even if you have set `failed_request_status_codes=set()`.

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/bottle.md#supported-versions)

* Bottle: 0.12+

* Python:

  * 3.6+ (SDK <3.0)
  * 3.7+ (SDK 3.0+)

If you're looking to use Sentry with older Python or framework versions, consider using an older major version of the SDK. The minimum versions for each major version are listed above.

