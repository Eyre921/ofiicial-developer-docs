---
title: "Common error messages"
source: https://docs.pinecone.io/reference/api/error-messages
path: reference/api/error-messages
---

Look up specific Pinecone API and SDK error messages, what causes each one, and how to fix it.

For the HTTP status codes the API returns, see [Errors](/reference/api/errors).

## Index creation errors

### Missing spec argument

```console theme={null}
TypeError: Pinecone.create_index() missing 1 required positional argument: 'spec'
```

Python SDK versions 3.0.0 to 9.x require a `spec` argument in `create_index()`. Pass one to set the index's cloud and region:

```python Python theme={null}
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="YOUR_API_KEY")

pc.create_index(
    name="docs-example",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)
```

In Python SDK 10, `spec` is optional and new indexes default to AWS `us-east-1`. For current syntax, see [Create an index](/guides/index-data/create-an-index).

### Serverless index limit reached

```console theme={null}
Request failed. You've reached the max serverless indexes allowed in project PROJECT_NAME (LIMIT). Use namespaces to partition your data into logical groups, or upgrade your plan to add more serverless indexes.
```

The API returns this with status `403` when the project already has as many serverless indexes as your plan allows. For the limit on each plan, see [Object limits](/reference/api/database-limits/object-limits). To fix it, do one of the following:

* [Delete indexes](/guides/manage-data/manage-indexes#delete-an-index) you no longer need.
* Store data in [namespaces](/guides/index-data/implement-multitenancy) within one index instead of creating separate indexes.
* [Upgrade your plan](/admin/billing/upgrade-billing-plan).

## Outdated Python SDK errors

These errors come from code written for Python SDK versions earlier than 3.0.0, or from having the deprecated `pinecone-client` package installed.

### Pinecone has no attribute init

```console theme={null}
AttributeError: module 'pinecone' has no attribute 'init'
```

In Python SDK 5.0.0 and later, the message reads:

```console theme={null}
AttributeError: init is no longer a top-level attribute of the pinecone package.

Please create an instance of the Pinecone class instead.
```

The code calls `pinecone.init()`, which was removed in version 3.0.0. Create a client instance instead. It doesn't take an environment, only an API key:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")
```

The same applies to other former top-level functions, such as `pinecone.create_index()` and `pinecone.list_indexes()`. Call them on the client instance instead.

### Cannot import name Pinecone

```console theme={null}
ImportError: cannot import name 'Pinecone' from 'pinecone'
```

The installed SDK is earlier than 3.0.0, or the deprecated `pinecone-client` package is installed alongside `pinecone`. The Python SDK package was renamed from `pinecone-client` to `pinecone`, and having both installed causes conflicts. Remove the old package and upgrade:

```shell Shell theme={null}
pip uninstall pinecone-client
pip install --upgrade pinecone
```

### Controller hostname not found

```console theme={null}
Failed to resolve 'controller.us-west-2.pinecone.io'
controller.us-west-2-aws.pinecone.io not found
Request failed to reach Pinecone while calling https://controller.us-west-2.pinecone.io/actions/whoami
```

SDK versions earlier than 3.0.0 send requests to environment-specific `controller` hostnames. Current SDKs use `https://api.pinecone.io`. Upgrade the SDK, then update your code as described in [Pinecone has no attribute init](#pinecone-has-no-attribute-init):

```shell Shell theme={null}
pip install --upgrade pinecone
```
