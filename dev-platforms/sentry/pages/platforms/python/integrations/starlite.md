---
title: "Starlite"
source: https://docs.sentry.io/platforms/python/integrations/starlite.md
path: platforms/python/integrations/starlite
---

---
title: "Starlite"
description: "Learn about using Sentry with Starlite."
url: https://docs.sentry.io/platforms/python/integrations/starlite/
---

# Starlite for Python

The Starlite integration adds support for the [Starlite framework](https://docs.litestar.dev/1/).

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/starlite.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk uvicorn
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/starlite.md#configure)

If you have the `starlite` package in your dependencies, the Starlite integration will be enabled automatically when you initialize the Sentry SDK.

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

## [Verify](https://docs.sentry.io/platforms/python/integrations/starlite.md#verify)

```python
from starlite import Starlite, get

sentry_sdk.init(...)  # same as above

@get("/hello")
async def hello_world() -> str:
    1 / 0
    return "Hello!"

app = Starlite(route_handlers=[hello_world])
```

Save the file above as `app.py` and start the development server with:

```bash
uvicorn app:app
```

When you point your browser to <http://localhost:8000/hello> a transaction will be created in the Performance section of [sentry.io](https://sentry.io). Additionally, the `ZeroDivisionError` we've snuck into our `hello_world` handler will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/starlite.md#supported-versions)

##### Note

Starlite was renamed to Litestar with the release of version 2.0. We support different integrations for each one. This guide applies to Starlite. See [Litestar integration](https://docs.sentry.io/platforms/python/integrations/litestar.md) for the guide that applies to Litestar.

* Starlite: 1.48.0 - 1.51.14
* Python: 3.8+

