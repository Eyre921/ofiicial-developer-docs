---
title: "Falcon"
source: https://docs.sentry.io/platforms/python/integrations/falcon.md
path: platforms/python/integrations/falcon
---

---
title: "Falcon"
description: "Learn about using Sentry with Falcon."
url: https://docs.sentry.io/platforms/python/integrations/falcon/
---

# Falcon for Python

The Falcon integration adds support for the [Falcon web framework](https://falconframework.org/). The integration has been confirmed to work with Falcon 3.0 and later.

If you're using stream mode, this page's references to "transaction" should be applied to service spans instead. See [Streamed Spans](https://docs.sentry.io/platforms/python/tracing/streamed-spans.md) for more information.

## [Install](https://docs.sentry.io/platforms/python/integrations/falcon.md#install)

Install `sentry-sdk` from PyPI:

```bash
pip install sentry-sdk
```

*Other available variations of the above snippet: uv*

## [Configure](https://docs.sentry.io/platforms/python/integrations/falcon.md#configure)

If you have the `falcon` package in your dependencies, the Falcon integration will be enabled automatically when you initialize the Sentry SDK.

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

## [Verify](https://docs.sentry.io/platforms/python/integrations/falcon.md#verify)

```python
import falcon

sentry_sdk.init(...)  # same as above

class HelloWorldResource:
    def on_get(self, req, resp):
        message = {
            'hello': "world",
        }
        1 / 0  # raises an error
        resp.media = message

app = falcon.App()
app.add_route('/', HelloWorldResource())
```

When you point your browser to <http://localhost:8000/> a transaction will be created in the Performance section of [sentry.io](https://sentry.io). Additionally, an error event will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## [Behavior](https://docs.sentry.io/platforms/python/integrations/falcon.md#behavior)

Are you using uWSGI?

If you're using uWSGI, note that it doesn't support threads by default. This might lead to unexpected behavior when using the Sentry SDK, from features not working properly to uWSGI workers crashing.

To enable threading support in uWSGI, make sure you have both `--enable-threads` and `--py-call-uwsgi-fork-hooks` on.

Note that automatic tracing on file-like responses when `offloading` is configured is disabled (see [here](https://github.com/getsentry/sentry-python/pull/5556) for why). If you wish to enable tracing on these types of responses, you will need to [manually instrument](https://docs.sentry.io/platforms/python/tracing/instrumentation/custom-instrumentation.md) them.

* The Sentry Python SDK will install the Falcon integration for all of your apps. The integration hooks into the base `falcon.API` class via monkey patching.

* All exceptions leading to an Internal Server Error are reported.

* Request data is attached to all events: **HTTP method, URL, headers, form data, JSON payloads**. Sentry excludes raw bodies and multipart file uploads. Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you configure which categories to collect with the [`data_collection` option](https://docs.sentry.io/platforms/python/configuration/options.md#data_collection) or set `send_default_pii` to `True`. `send_default_pii` will be removed in version 3.0 of the SDK.

* Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

## [Options](https://docs.sentry.io/platforms/python/integrations/falcon.md#options)

In stream mode, these options still work as described, but apply to service spans instead of transactions.

By adding `FalconIntegration` to your `sentry_sdk.init()` call explicitly, you can set options for `FalconIntegration` to change its behavior:

```python
import sentry_sdk
from sentry_sdk.integrations.falcon import FalconIntegration

sentry_sdk.init(
    # same as above
    integrations=[
        FalconIntegration(
            transaction_style="path",
        ),
    ],
)
```

You can pass the following keyword arguments to `FalconIntegration()`:

* `transaction_style`:

  ```python
  class MessageResource:
      def on_get(self, req, resp, message_id):
          msg = database.get_message(message_id)
          resp.media = msg.as_json()

  app = falcon.API()
  app.add_route("/message/{message_id}", MessageResource())
  ```

  In the above code, you would set the transaction to:

  * `/myurl/b48a7686-ad8c-4c94-8c3b-412ec7f25db2123` if you set `transaction_style="path"`.
  * `/myurl/{message_id}` if you set `transaction_style="uri_template"`

  The default is `"uri_template"`.

## [Supported Versions](https://docs.sentry.io/platforms/python/integrations/falcon.md#supported-versions)

* Falcon:

  * 1.4+ (SDK <3.0)
  * 3.0+ (SDK 3.0+)

* Python:

  * 3.6+ (SDK <3.0)
  * 3.7+ (SDK 3.0+)

If you're looking to use Sentry with older Python or framework versions, consider using an older major version of the SDK. The minimum versions for each major version are listed above.

