---
title: "Pyramid"
source: https://docs.sentry.io/platforms/python/integrations/pyramid.md
path: platforms/python/integrations/pyramid
---

---
title: "Pyramid"
description: "Learn about using Sentry with Pyramid."
url: https://docs.sentry.io/platforms/python/integrations/pyramid/
---

# Pyramid for Python

The Pyramid integration adds support for the [Pyramid Web Framework](https://trypyramid.com/).

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/pyramid.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install "sentry-sdk"
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/pyramid.md#configure)

If you have the `pyramid` package in your dependencies, the Pyramid integration will be enabled automatically when you initialize the Sentry SDK.

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

## [Verify](https://docs.sentry.io/platforms/python/integrations/pyramid.md#verify)

```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

sentry_sdk.init(...)  # same as above

def hello_world(request):
    1 / 0  # raises an error
    return Response('Hello World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
```

When you point your browser to <http://localhost:6543/> an error event will be sent to [sentry.io](https://sentry.io).

## [Behavior](https://docs.sentry.io/platforms/python/integrations/pyramid.md#behavior)

Are you using uWSGI?

If you're using uWSGI, note that it doesn't support threads by default. This might lead to unexpected behavior when using the Sentry SDK, from features not working properly to uWSGI workers crashing.

To enable threading support in uWSGI, make sure you have both `--enable-threads` and `--py-call-uwsgi-fork-hooks` on.

Note that automatic tracing on file-like responses when `offloading` is configured is disabled (see [here](https://github.com/getsentry/sentry-python/pull/5556) for why). If you wish to enable tracing on these types of responses, you will need to [manually instrument](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md) them.

* The Sentry Python SDK will install the Pyramid integration for all of your apps. The integration hooks into Pyramid itself, not any of your apps specifically.

* The SDK will report all exceptions leading to an Internal Server Error. These two kinds of exceptions are:

  * exceptions that are not handled by any exception view
  * exceptions whose exception view returns a status code of 500

* Request data is attached to all events: **HTTP method, URL, headers, form data, JSON payloads**. Sentry excludes raw bodies and multipart file uploads. Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

* Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

* Logging with *any* logger will create breadcrumbs when the [Logging](https://docs.sentry.io/platforms/python/integrations/logging.md) integration is enabled (done by default).

## [Options](https://docs.sentry.io/platforms/python/integrations/pyramid.md#options)

In stream mode, these options still work as described, but apply to service spans instead of transactions.

By adding `PyramidIntegration` to your `sentry_sdk.init()` call explicitly, you can set options for `PyramidIntegration` to change its behavior:

```python
import sentry_sdk
from sentry_sdk.integrations.pyramid import PyramidIntegration

sentry_sdk.init(
    # ...
    integrations=[
        PyramidIntegration(
            transaction_style="route_pattern",
        )
    ]
)
```

You can pass the following keyword arguments to `PyramidIntegration()`:

* `transaction_style`:

  ```python
  config.add_route("myroute", "/myurl/{id}")
  config.add_view(myfunction, route_name="myroute")
  ```

  In the above code, you can set the transaction to:

  * `/myurl/{id}` if you set `transaction_style="route_pattern"`
  * `myroute` if you set `transaction_style="route_name"`

  The default is `"route_name"`.

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/pyramid.md#supported-versions)

* Pyramid:

  * 1.6+ (SDK <3.0)
  * 2.0+ (SDK 3.0+)

* Python:

  * 3.6+ (SDK <3.0)
  * 3.7+ (SDK 3.0+)

If you're looking to use Sentry with older Python or framework versions, consider using an older major version of the SDK. The minimum versions for each major version are listed above.

