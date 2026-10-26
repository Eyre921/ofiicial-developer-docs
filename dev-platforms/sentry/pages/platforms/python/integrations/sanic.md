---
title: "Sanic"
source: https://docs.sentry.io/platforms/python/integrations/sanic.md
path: platforms/python/integrations/sanic
---

---
title: "Sanic"
description: "Learn about using Sentry with Sanic."
url: https://docs.sentry.io/platforms/python/integrations/sanic/
---

# Sanic for Python

The Sanic integration adds support for the [Sanic Web Framework](https://sanic.dev/).

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/sanic.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/sanic.md#configure)

If you have the `sanic` package in your dependencies, the Sanic integration will be enabled automatically when you initialize the Sentry SDK.

To ensure that errors occurring in background tasks get reported to Sentry, we always recommend enabling the [`AsyncioIntegration`](https://docs.sentry.io/platforms/python/integrations/asyncio.md) when you are using the `SanicIntegration`. To enable the `AsyncioIntegration`, you must explicitly add the `AsyncioIntegration` to the `integrations` list and initialize the SDK within a `before_server_start` listener.

The example below demonstrates the simplest recommended setup.

In addition to capturing errors, you can monitor interactions between multiple services or applications by [enabling tracing](https://docs.sentry.io/concepts/key-terms/tracing.md). You can also collect and analyze performance profiles from real users with [profiling](https://docs.sentry.io/product/profiling.md).

Select which Sentry features you'd like to install in addition to Error Monitoring to get the corresponding installation and configuration instructions below.

Error Monitoring\[ ]Tracing\[ ]Profiling

```python
from sanic import Sanic
import sentry_sdk
from sentry_sdk.integrations.asyncio import AsyncioIntegration

app = Sanic(__main__)

@app.listener("before_server_start")
async def init_sentry(_):
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
        integrations=[AsyncioIntegration()],
    )
```

### [Configuration options](https://docs.sentry.io/platforms/python/integrations/sanic.md#configuration-options)

If you're using tracing, you can configure the Sanic integration to not send transactions for requests that resulted in certain HTTP statuses using the `unsampled_statuses` option.

By default, the Sanic integration generates transactions for all requests, except requests that result in a 404 HTTP status. To generate transactions for all HTTP statuses, including 404, or change which HTTP statuses don't generate transactions, you can manually instantiate the Sanic integration when initializing the Sentry SDK, like so:

```python
from sanic import Sanic
import sentry_sdk
from sentry_sdk.integrations.asyncio import AsyncioIntegration
from sentry_sdk.integrations.sanic import SanicIntegration

@app.listener("before_server_start")
async def init_sentry(_):
    sentry_sdk.init(
        # ...
        integrations=[
            AsyncioIntegration(),
            SanicIntegration(
                # Configure the Sanic integration so that we generate
                # transactions for all HTTP status codes, including 404
                unsampled_statuses=None,
            ),
        ],
    )
```

To specify a different set of HTTP statuses for which no transactions should be generated, set `unsampled_statuses` to a set containing the HTTP statuses that don't generate transactions. For example, if you wish to have no transactions for requests resulting in a 200 or 404 HTTP status, use `SanicIntegration(unsampled_statuses={200, 400})`.

## [Verify](https://docs.sentry.io/platforms/python/integrations/sanic.md#verify)

```python
from sanic import Sanic
from sanic.response import text
import sentry_sdk
from sentry_sdk.integrations.asyncio import AsyncioIntegration

app = Sanic(__name__)

@app.listener("before_server_start")
async def init_sentry(_):
    sentry_sdk.init(...)  # same as above

@app.get("/")
async def hello_world(request):
    1 / 0  # raises an error
    return text("Hello, world.")`
```

When you point your browser to <http://localhost:8000/> an error event will be sent to [sentry.io](https://sentry.io).

## [Behavior](https://docs.sentry.io/platforms/python/integrations/sanic.md#behavior)

* The Sentry Python SDK will install the Sanic integration for all of your apps.

* All exceptions leading to an Internal Server Error are reported.

* Request data is attached to all events: **HTTP method, URL, headers, form data, JSON payloads**. Sentry excludes raw bodies and multipart file uploads. Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

* Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

* Logging with any logger will create breadcrumbs when the [Logging](https://docs.sentry.io/platforms/python/integrations/logging.md) integration is enabled (done by default).

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/sanic.md#supported-versions)

* Sanic:

  * 0.8+ (SDK <3.0)
  * 22.0+ (SDK 3.0+)

* Python:

  * 3.6+ (SDK <3.0)
  * 3.7+ (SDK 3.0+)

