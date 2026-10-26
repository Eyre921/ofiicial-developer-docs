---
title: "AIOHTTP"
source: https://docs.sentry.io/platforms/python/integrations/aiohttp.md
path: platforms/python/integrations/aiohttp
---

---
title: "AIOHTTP"
description: "Learn about using Sentry with AIOHTTP."
url: https://docs.sentry.io/platforms/python/integrations/aiohttp/
---

# AIOHTTP for Python

The AIOHTTP integration adds support for the [AIOHTTP server web framework](https://docs.aiohttp.org/en/stable/web.html).

If you use AIOHTTP as your HTTP client and want to instrument outgoing HTTP requests, have a look at the [AIOHTTP client documentation](https://docs.sentry.io/platforms/python/integrations/aiohttp/aiohttp-client.md).

## [Install](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#configure)

If you have the `aiohttp` package in your dependencies, the AIOHTTP integration will be enabled automatically when you initialize the Sentry SDK.

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

## [Verify](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#verify)

```python
from aiohttp import web

sentry_sdk.init(...)  # same as above

async def hello(request):
    1 / 0  # raises an error
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app)
```

When you point your browser to <http://localhost:8080/> a transaction will be created in the Performance section of [sentry.io](https://sentry.io). Additionally, an error event will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## [Behavior](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#behavior)

* The Sentry Python SDK will install the AIOHTTP integration for all of your apps.
* All exceptions leading to an Internal Server Error are reported.
* *The AIOHTTP integration currently does not attach the request body*, see [GitHub issue](https://github.com/getsentry/sentry-python/issues/220).
* Logging with any logger will create breadcrumbs when the [Logging](https://docs.sentry.io/platforms/python/integrations/logging.md) integration is enabled (done by default).

## [Options](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#options)

In stream mode, these options still work as described, but apply to service spans instead of transactions.

By adding `AioHttpIntegration` to your `sentry_sdk.init()` call explicitly, you can set options for `AioHttpIntegration` to change its behavior:

```python
import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

sentry_sdk.init(
    # same as above
    integrations=[
        AioHttpIntegration(
            transaction_style="...",  # type: str
            failed_request_status_codes={...}  # type: collections.abc.Set[int]
        ),
    ],
)
```

You can pass the following keyword arguments to `AioHttpIntegration()`:

### [`transaction_style`](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#transaction_style)

Configure the way Sentry names transactions:

* `GET /path/{id}` if you set `transaction_style="method_and_path_pattern"`
* `<module_name>.hello` if you set `transaction_style="handler_name"`

The default is `"handler_name"`.

### [`failed_request_status_codes`](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#failed_request_status_codes)

A `set` of integers that will determine when an `HTTPException` should be reported to Sentry. The `HTTPException` is reported to Sentry if its status code is contained in the `failed_request_status_codes` set.

Examples of valid `failed_request_status_codes`:

* `{500}` will only report `HTTPException` with status 500 (i.e. `HTTPInternalServerError`).
* `{400, *range(500, 600)}` will report `HTTPException` with status 400 (i.e. `HTTPBadRequest`) as well as those in the 5xx range.
* `set()` (the empty set) will not report any `HTTPException` to Sentry.

The default is `{*range(500, 600)}`, meaning that any `HTTPException` with a status in the 5xx range is reported to Sentry.

Regardless of how `failed_request_status_codes` is set, any exceptions raised by the handler, which are not of type `HTTPException` (or a subclass) are reported to Sentry. For example, if your request handler raises an unhandled `AttributeError`, the `AttributeError` gets reported to Sentry, even if you have set `failed_request_status_codes=set()`.

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/aiohttp.md#supported-versions)

* AIOHTTP:

  * 3.4+ (SDK <3.0)
  * 3.7+ (SDK 3.0+)

* Python: 3.7+

## Pages in this section

- [AIOHTTP Client](https://docs.sentry.io/platforms/python/integrations/aiohttp/aiohttp-client.md)

