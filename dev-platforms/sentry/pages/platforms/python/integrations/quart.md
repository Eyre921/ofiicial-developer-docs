---
title: "Quart"
source: https://docs.sentry.io/platforms/python/integrations/quart.md
path: platforms/python/integrations/quart
---

---
title: "Quart"
description: "Learn about using Sentry with Quart."
url: https://docs.sentry.io/platforms/python/integrations/quart/
---

# Quart for Python

The Quart integration adds support for the [Quart Web Framework](https://gitlab.com/pgjones/quart).

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/quart.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/quart.md#configure)

If you have the `quart` package in your dependencies, the Quart integration will be enabled automatically when you initialize the Sentry SDK.

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

# [Verify](https://docs.sentry.io/platforms/python/integrations/quart.md#verify)

```python
from quart import Quart

sentry_sdk.init(...)  # same as above

app = Quart(__name__)

@app.route("/")
async def hello():
    1/0  # raises an error
    return {"hello": "world"}

app.run()
```

When you point your browser to <http://localhost:5000/> a transaction in the Performance section of [sentry.io](https://sentry.io) will be created. Additionally, an error event will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## [Behavior](https://docs.sentry.io/platforms/python/integrations/quart.md#behavior)

* The Sentry Python SDK will install the Quart integration for all of your apps.

* All exceptions leading to an Internal Server Error, from before/after serving functions, and background tasks are reported.

* Request data is attached to all events: **HTTP method, URL, headers**. Sentry also excludes personally identifiable information (such as user IDs, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

* Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

* Logging with any logger will create breadcrumbs when the [Logging](https://docs.sentry.io/platforms/python/integrations/logging.md) integration is enabled (done by default).

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/quart.md#supported-versions)

* Quart:

  * 0.16.0+ (SDK <3.0)
  * 0.19.0+ (SDK 3.0+)

* Python: 3.7+

