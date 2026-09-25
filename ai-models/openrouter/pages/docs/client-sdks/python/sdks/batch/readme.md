---
title: "Batch"
source: https://openrouter.ai/docs/client-sdks/python/sdks/batch/README.md
path: docs/client-sdks/python/sdks/batch/readme
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch

> Submit, list, poll, and delete asynchronous batches of inference requests. See https://openrouter.ai/docs/batch-quickstart.

## Overview

Submit, list, poll, and delete asynchronous batches of inference requests. See [https://openrouter.ai/docs/batch-quickstart](https://openrouter.ai/docs/batch-quickstart).

### Available Operations

* [list](#list) - List batches
* [create\_batches](#create_batches) - Create a batch
* [delete](#delete) - Delete a batch
* [get\_batches](#get_batches) - Get a batch

## list

Lists batches in the workspace of the authenticating API key, newest first. To fetch the next page, pass the previous page's `last_id` as `after`. List items omit `results`. Use `GET /batches/{id}` to get them. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).

### Example Usage

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.batch.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                  | Type                                                                                 | Required             | Description                                                                                                                                                 | Example                                   |
| -------------------------- | ------------------------------------------------------------------------------------ | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `http_referer`             | *Optional\[str]*                                                                     | :heavy\_minus\_sign: | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br />This is used to track API usage per application.<br /> |                                           |
| `x_open_router_title`      | *Optional\[str]*                                                                     | :heavy\_minus\_sign: | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br />                                                          |                                           |
| `x_open_router_categories` | *Optional\[str]*                                                                     | :heavy\_minus\_sign: | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.<br />                                                 |                                           |
| `limit`                    | *Optional\[int]*                                                                     | :heavy\_minus\_sign: | Maximum number of batches to return, from 1 through 100.                                                                                                    | 20                                        |
| `after`                    | *Optional\[str]*                                                                     | :heavy\_minus\_sign: | Batch id from the previous page's `last_id`.                                                                                                                | batch\_7a4b02                             |
| `status`                   | List\[[components.BatchListStatus](../../components/batchliststatus.mdx)]            | :heavy\_minus\_sign: | Repeat this parameter to include more than one status.                                                                                                      | \[<br />"completed",<br />"failed"<br />] |
| `created_after`            | [Optional\[components.BatchListTimestamp\]](../../components/batchlisttimestamp.mdx) | :heavy\_minus\_sign: | Only include batches created strictly after this timestamp.                                                                                                 | 2026-08-20T00:00:00Z                      |
| `created_before`           | [Optional\[components.BatchListTimestamp\]](../../components/batchlisttimestamp.mdx) | :heavy\_minus\_sign: | Only include batches created strictly before this timestamp.                                                                                                | 2026-08-20T00:00:00Z                      |
| `retries`                  | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx)                  | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client.                                                                                         |                                           |

### Response

**[operations.ListBatchesResponse](../../operations/listbatchesresponse.mdx)**

### Errors

| Error Type                    | Status Code   | Content Type     |
| ----------------------------- | ------------- | ---------------- |
| errors.BatchErrorResponse     | 400, 401, 429 | application/json |
| errors.BatchErrorResponse     | 500, 502      | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX      | \*/\*            |

## create\_batches

Creates a batch of requests that run asynchronously against a single endpoint (`/v1/chat/completions`, `/v1/responses`, `/v1/messages`, `/v1/embeddings`). Returns `202` with `status: "validating"`. Poll `GET /batches/{id}` for progress and results. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).

### Example Usage: chatCompletions

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.batch.create_batches(endpoint="/v1/chat/completions", model="openai/gpt-4o", requests=[
        {
            "body": {
                "messages": [
                    {
                        "content": "Summarize ...",
                        "role": "user",
                    },
                ],
                "model": "openai/gpt-4o",
            },
            "custom_id": "req-0001",
        },
    ], completion_window="24h")

    # Handle response
    print(res)

```

### Example Usage: messages

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.batch.create_batches(endpoint="/v1/messages", model="openai/gpt-5-nano", requests=[
        {
            "body": {
                "max_tokens": 1024,
                "messages": [
                    {
                        "content": "Summarize ...",
                        "role": "user",
                    },
                ],
                "model": "openai/gpt-5-nano",
            },
            "custom_id": "req-0001",
        },
    ], completion_window="24h")

    # Handle response
    print(res)

```

### Example Usage: providerPinned

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.batch.create_batches(endpoint="/v1/chat/completions", model="google/gemini-3.6-flash", requests=[
        {
            "body": {
                "messages": [
                    {
                        "content": "Summarize ...",
                        "role": "user",
                    },
                ],
                "model": "google/gemini-3.6-flash",
            },
            "custom_id": "req-0001",
        },
    ], completion_window="24h")

    # Handle response
    print(res)

```

### Example Usage: responses

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.batch.create_batches(endpoint="/v1/responses", model="openai/gpt-4o", requests=[
        {
            "body": {
                "input": [
                    {
                        "content": [
                            {
                                "text": "Summarize ...",
                                "type": "input_text",
                            },
                        ],
                        "role": "user",
                    },
                ],
                "model": "openai/gpt-4o",
            },
            "custom_id": "req-0001",
        },
    ], completion_window="24h")

    # Handle response
    print(res)

```

### Parameters

| Parameter                  | Type                                                                                                           | Required             | Description                                                                                                                                                 | Example                                               |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `endpoint`                 | [components.Endpoint](../../components/endpoint.mdx)                                                           | :heavy\_check\_mark: | N/A                                                                                                                                                         |                                                       |
| `model`                    | *str*                                                                                                          | :heavy\_check\_mark: | N/A                                                                                                                                                         |                                                       |
| `requests`                 | List\[[components.Request](../../components/request.mdx)]                                                      | :heavy\_check\_mark: | N/A                                                                                                                                                         |                                                       |
| `http_referer`             | *Optional\[str]*                                                                                               | :heavy\_minus\_sign: | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br />This is used to track API usage per application.<br /> |                                                       |
| `x_open_router_title`      | *Optional\[str]*                                                                                               | :heavy\_minus\_sign: | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br />                                                          |                                                       |
| `x_open_router_categories` | *Optional\[str]*                                                                                               | :heavy\_minus\_sign: | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.<br />                                                 |                                                       |
| `completion_window`        | [Optional\[components.BatchSubmitBodyCompletionWindow\]](../../components/batchsubmitbodycompletionwindow.mdx) | :heavy\_minus\_sign: | N/A                                                                                                                                                         |                                                       |
| `provider`                 | [OptionalNullable\[components.BatchProviderPreferences\]](../../components/batchproviderpreferences.mdx)       | :heavy\_minus\_sign: | Batch provider routing preferences. Only `provider.only` is supported.                                                                                      | \{<br />"only": \[<br />"google-vertex"<br />]<br />} |
| `retries`                  | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx)                                            | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client.                                                                                         |                                                       |

### Response

**[components.BatchObject](../../components/batchobject.mdx)**

### Errors

| Error Type                    | Status Code                            | Content Type     |
| ----------------------------- | -------------------------------------- | ---------------- |
| errors.BatchErrorResponse     | 400, 401, 402, 403, 404, 413, 422, 429 | application/json |
| errors.BatchErrorResponse     | 500, 502                               | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX                               | \*/\*            |

## delete

Deletes a batch in a terminal status (`completed`, `failed`, `expired`, or `cancelled`) and its stored requests and results. Batches still in progress return `409`. Billing and usage records are kept. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).

### Example Usage

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.batch.delete(id="batch_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                  | Type                                                                | Required             | Description                                                                                                                                                 | Example       |
| -------------------------- | ------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `id`                       | *str*                                                               | :heavy\_check\_mark: | The batch job id returned from submit.                                                                                                                      | batch\_abc123 |
| `http_referer`             | *Optional\[str]*                                                    | :heavy\_minus\_sign: | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br />This is used to track API usage per application.<br /> |               |
| `x_open_router_title`      | *Optional\[str]*                                                    | :heavy\_minus\_sign: | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br />                                                          |               |
| `x_open_router_categories` | *Optional\[str]*                                                    | :heavy\_minus\_sign: | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.<br />                                                 |               |
| `retries`                  | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client.                                                                                         |               |

### Response

**[components.BatchDeletedObject](../../components/batchdeletedobject.mdx)**

### Errors

| Error Type                    | Status Code        | Content Type     |
| ----------------------------- | ------------------ | ---------------- |
| errors.BatchErrorResponse     | 401, 404, 409, 429 | application/json |
| errors.BatchErrorResponse     | 500, 502           | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX           | \*/\*            |

## get\_batches

Returns a batch with its status and request counts. Batches in a terminal status include `results`. Failed batches report the reason in `error.message`. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).

### Example Usage

```python theme={null}
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.batch.get_batches(id="batch_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                  | Type                                                                | Required             | Description                                                                                                                                                 | Example       |
| -------------------------- | ------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `id`                       | *str*                                                               | :heavy\_check\_mark: | The batch job id returned from submit.                                                                                                                      | batch\_abc123 |
| `http_referer`             | *Optional\[str]*                                                    | :heavy\_minus\_sign: | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br />This is used to track API usage per application.<br /> |               |
| `x_open_router_title`      | *Optional\[str]*                                                    | :heavy\_minus\_sign: | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br />                                                          |               |
| `x_open_router_categories` | *Optional\[str]*                                                    | :heavy\_minus\_sign: | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.<br />                                                 |               |
| `retries`                  | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client.                                                                                         |               |

### Response

**[components.BatchObject](../../components/batchobject.mdx)**

### Errors

| Error Type                               | Status Code   | Content Type     |
| ---------------------------------------- | ------------- | ---------------- |
| errors.BatchPaymentRequiredResponseError | 402           | application/json |
| errors.BatchErrorResponse                | 401, 404, 429 | application/json |
| errors.BatchErrorResponse                | 500, 502      | application/json |
| errors.OpenRouterDefaultError            | 4XX, 5XX      | \*/\*            |

