---
title: "Tornado"
source: https://docs.sentry.io/platforms/python/integrations/tornado.md
path: platforms/python/integrations/tornado
---

---
title: "Tornado"
description: "Learn about using Sentry with Tornado."
url: https://docs.sentry.io/platforms/python/integrations/tornado/
---

# Tornado for Python

The Tornado integration adds support for the [Tornado Web Framework](https://www.tornadoweb.org/).

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/tornado.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/tornado.md#configure)

If you have the `tornado` package in your dependencies, the Tornado integration will be enabled automatically when you initialize the Sentry SDK.

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

## [Verify](https://docs.sentry.io/platforms/python/integrations/tornado.md#verify)

```python
import asyncio
import tornado

sentry_sdk.init(...)  # same as above

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        1 / 0  # raises an error
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

asyncio.run(main())
```

When you point your browser to <http://localhost:8888/> a transaction in the Performance section of [sentry.io](https://sentry.io) will be created. Additionally, an error event will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## [Behavior](https://docs.sentry.io/platforms/python/integrations/tornado.md#behavior)

* The Tornado integration will be installed for all of your apps and handlers.

* All exceptions leading to a Internal Server Error are reported.

* Request data is attached to all events: **HTTP method, URL, headers, form data, JSON payloads**. Sentry excludes raw bodies and multipart file uploads. Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

* Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

* Logging with any logger will create breadcrumbs when the [Logging](https://docs.sentry.io/platforms/python/integrations/logging.md) integration is enabled (done by default).

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/tornado.md#supported-versions)

* Tornado: 6+
* Python: 3.8+

If you're looking to use Sentry with older Python or framework versions, consider using an older major version of the SDK. The minimum versions for each major version are listed above.

