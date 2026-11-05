---
title: "Python SDK"
source: https://docs.fireworks.ai/tools-sdks/python-sdk
path: tools-sdks/python-sdk
---

Overview of the Fireworks Python SDK, including installation, authentication, and calling chat and completion endpoints from a Python project.

The official Python SDK for the Fireworks AI API is available on [GitHub](https://github.com/fw-ai-external/python-sdk) and [PyPI](https://pypi.org/project/fireworks-ai/).

## Fireworks vs. OpenAI SDK

Fireworks is [OpenAI-compatible](/tools-sdks/openai-compatibility), so you can use the OpenAI SDK with Fireworks. The Fireworks SDK offers additional benefits:

* **Better concurrency defaults** — Optimized connection pooling for high-throughput workloads
* **Fireworks-exclusive features** — Access parameters and response fields not available in the OpenAI API
* **Platform automation** — Manage datasets, evals, training, and deployments programmatically

## Installation

Requires Python 3.9+ and an API key. See [Getting your API key](/api-reference/introduction#getting-your-api-key) for instructions.

```bash pip theme={null}
python -m pip install --upgrade fireworks-ai
```

```bash poetry theme={null}
poetry add fireworks-ai
```

```bash uv theme={null}
uv add fireworks-ai
```

For Training API recipes and utilities, install `fireworks-training-cookbook` on Python 3.11 or newer. See [Cookbook installation](/fine-tuning/training-api/cookbook/overview#installation) for PyPI releases and editable source checkouts. To use the Training API SDK directly, install `fireworks-ai[training]`.

For detailed usage instructions, see the
[README.md](https://github.com/fw-ai-external/python-sdk#readme). To quickly get
started with serverless, see our [Serverless
Quickstart](/getting-started/quickstart).
