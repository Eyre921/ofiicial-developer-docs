---
title: "OpenLLMetry"
source: https://docs.trychroma.com/integrations/frameworks/openllmetry
path: integrations/frameworks/openllmetry
---

[OpenLLMetry](https://www.traceloop.com/openllmetry) provides observability for systems using Chroma. It allows tracing calls to Chroma, OpenAI, and other services.
It gives visibility to query and index calls as well as LLM prompts and completions.
For more information on how to use OpenLLMetry, see the [OpenLLMetry docs](https://www.traceloop.com/docs/openllmetry).

![](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/openllmetry.png?fit=max\&auto=format\&n=N-xA4EbmHOvIcCcs\&q=85\&s=b5fe7744ed8fda703db34aa15c234fe7)

### Example

Install OpenLLMetry SDK by running:

```bash theme={null}
pip install traceloop-sdk
```

Then, initialize the SDK in your application:

```python theme={null}
from traceloop.sdk import Traceloop

Traceloop.init()
```

### Configuration

OpenLLMetry can be configured to send traces to any observability platform that supports OpenTelemetry - Datadog, Honeycomb, Dynatrace, New Relic, etc. See the [OpenLLMetry docs](https://www.traceloop.com/openllmetry/provider/chroma) for more information.
