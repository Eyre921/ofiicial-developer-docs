---
title: "Errors"
source: https://docs.pinecone.io/reference/api/errors
path: reference/api/errors
---

Look up the HTTP status codes the Pinecone API returns, plus the causes and fixes for common Pinecone API and SDK error messages.

Look up an [HTTP status code](#http-status-codes), or find an exact error message under [Index creation errors](#index-creation-errors) or [Outdated Python SDK errors](#outdated-python-sdk-errors). For handling errors in production, see [Error handling](/guides/production/error-handling).

## HTTP status codes

Pinecone uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided, and codes in the `5xx` range indicate an error with Pinecone's servers.

### 200 - OK

The request succeeded.

### 201 - CREATED

The request succeeded and a new resource was created.

### 202 - ACCEPTED

The request was accepted, but the operation isn't complete yet. For example, deleting an index returns `202` while the deletion is still in progress.

### 204 - NO CONTENT

The request succeeded, and there's no response body to return.

### 400 - INVALID ARGUMENT

The request failed due to an invalid argument.

### 401 - UNAUTHENTICATED

The request failed due to a missing or invalid [API key](/admin/projects/understanding-projects#api-keys).

### 402 - PAYMENT REQUIRED

The request failed due to delinquent payment or account deactivation for non-payment. See [Account deactivation for non-payment](/admin/billing/non-payment-account-deactivation).

### 403 - FORBIDDEN

The request failed due to an exceeded [quota](/reference/api/database-limits/object-limits) or [index deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).

### 404 - NOT FOUND

The request failed because the resource was not found.

### 409 - ALREADY EXISTS

The request failed because the resource already exists.

### 412 - FAILED PRECONDITIONS

The request failed due to preconditions not being met.

### 422 - UNPROCESSABLE ENTITY

The request failed because the server was unable to process the contained instructions.

### 429 - TOO MANY REQUESTS

The request was [rate-limited](/reference/api/database-limits/rate-limits). [Implement retry logic with exponential backoff](/guides/production/error-handling#handle-rate-limits-429) to handle this error.

### 500 - UNKNOWN

An internal server error occurred. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.

### 502 - BAD GATEWAY

The API gateway received an invalid response from a backend service. This is typically a temporary error. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.

### 503 - UNAVAILABLE

The server is currently unavailable. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.

### 504 - GATEWAY TIMEOUT

The API gateway did not receive a timely response from the backend server. This can occur due to slow requests or backend processing delays. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.

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
