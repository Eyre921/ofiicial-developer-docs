---
title: "Litestar"
source: https://docs.sentry.io/platforms/python/integrations/litestar.md
path: platforms/python/integrations/litestar
---

---
title: "Litestar"
description: "Learn about using Sentry with Litestar."
url: https://docs.sentry.io/platforms/python/integrations/litestar/
---

# Litestar for Python

The Litestar integration adds support for the [Litestar framework](https://docs.litestar.dev/2/).

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/litestar.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk uvicorn
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/litestar.md#configure)

If you have the `litestar` package in your dependencies, the Litestar integration will be enabled automatically when you initialize the Sentry SDK.

In addition to capturing errors, you can monitor interactions between multiple services or applications by [enabling tracing](https://docs.sentry.io/concepts/key-terms/tracing.md). You can also collect and analyze performance profiles from real users with [profiling](https://docs.sentry.io/product/profiling.md).

Select which Sentry features you'd like to install in addition to Error Monitoring to get the corresponding installation and configuration instructions below.

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

## [Verify](https://docs.sentry.io/platforms/python/integrations/litestar.md#verify)

```python
from litestar import Litestar, get

sentry_sdk.init(...)  # same as above

@get("/hello")
async def hello_world() -> str:
    1 / 0
    return "Hello!"

app = Litestar(route_handlers=[hello_world])
```

Save the file above as `app.py` and start the development server with:

```bash
uvicorn app:app
```

When you point your browser to <http://localhost:8000/hello> a transaction will be created in the Performance section of [sentry.io](https://sentry.io). Additionally, the `ZeroDivisionError` we've snuck into our `hello_world` handler will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## [Options](https://docs.sentry.io/platforms/python/integrations/litestar.md#options)

By adding `LitestarIntegration` to your `sentry_sdk.init()` call explicitly, you can set options for `LitestarIntegration` to change its behavior:

```python
import sentry_sdk
from sentry_sdk.integrations.litestar import LitestarIntegration

sentry_sdk.init(
    # ...
    integrations=[
        LitestarIntegration(
            failed_request_status_codes={403, *range(500, 599)},
        ),
    ],
)
```

You can pass the following keyword arguments to `LitestarIntegration()`:

### [`failed_request_status_codes`](https://docs.sentry.io/platforms/python/integrations/litestar.md#failed_request_status_codes)

A `set` of integers that will determine when an `HTTPException` should be reported to Sentry. The `HTTPException` is reported to Sentry if its status code is contained in the `failed_request_status_codes` set.

Examples of valid `failed_request_status_codes`:

* `{500}` will only report `HTTPException` with status 500.
* `{400, *range(500, 600)}` will report `HTTPException` with status 400 as well as those in the 5xx range.
* `set()` (the empty set) will not report any `HTTPException` to Sentry.

The default is `{*range(500, 600)}`, meaning that any `HTTPException` with a status in the 5xx range is reported to Sentry.

Regardless of how `failed_request_status_codes` is set, any exceptions raised by the handler, which are not of type `HTTPException` (or a subclass) are reported to Sentry. For example, if your request handler raises an unhandled `AttributeError`, the `AttributeError` gets reported to Sentry, even if you have set `failed_request_status_codes=set()`.

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/litestar.md#supported-versions)

##### Note

Litestar was renamed from Starlite with the release of version 2.0. We support different integrations for each one. This guide applies to Litestar. See [Starlite integration](https://docs.sentry.io/platforms/python/integrations/starlite.md) for the guide that applies to Starlite.

* Litestar: 2.0.0+
* Python: 3.8+

