---
title: "Tools"
source: https://openrouter.ai/docs/client-sdks/python/sdks/tools/README.md
path: docs/client-sdks/python/sdks/tools/readme
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools

> The catalog of server tools OpenRouter runs on behalf of a model: accepted `tools[].type` spellings per API format, engines and pricing, and which endpoints run each tool natively. See https://openrouter.ai/docs/guides/features/server-tools.

## Overview

The catalog of server tools OpenRouter runs on behalf of a model: accepted `tools[].type` spellings per API format, engines and pricing, and which endpoints run each tool natively. See [https://openrouter.ai/docs/guides/features/server-tools](https://openrouter.ai/docs/guides/features/server-tools).

### Available Operations

* [list\_tools](#list_tools) - List server tools
* [get\_tool](#get_tool) - Get a server tool

## list\_tools

Lists every server tool OpenRouter can run on behalf of a model: accepted `tools[].type` spellings per API format, the engines behind it with their pricing, and how many endpoints run it natively.

### Example Usage

```python theme={null}
from openrouter import OpenRouter, operations
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
) as open_router:

    res = open_router.tools.list_tools(security=operations.ListToolsSecurity(
        bearer=os.getenv("OPENROUTER_BEARER", ""),
    ), offset=0, limit=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `security` | [operations.ListToolsSecurity](../../operations/listtoolssecurity.mdx) | :heavy\_check\_mark: | N/A | |
| `http_referer` | *Optional\[str]* | :heavy\_minus\_sign: | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br />This is used to track API usage per application.<br /> | |
| `x_open_router_title` | *Optional\[str]* | :heavy\_minus\_sign: | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br /> | |
| `x_open_router_categories` | *Optional\[str]* | :heavy\_minus\_sign: | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.<br /> | |
| `offset` | *OptionalNullable\[int]* | :heavy\_minus\_sign: | Number of records to skip for pagination. When both offset and limit are omitted, the full list is returned | 0 |
| `limit` | *Optional\[int]* | :heavy\_minus\_sign: | Maximum number of records to return (max 100). When both offset and limit are omitted, the full list is returned | 50 |
| `api_format` | [Optional\[operations.APIFormat\]](../../operations/apiformat.mdx) | :heavy\_minus\_sign: | Only tools usable on this API format | responses |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. | |

### Response

**[components.ListToolsResponse](../../components/listtoolsresponse.mdx)**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## get\_tool

One server tool by canonical name or any accepted alias, with the models that run it natively.

### Example Usage

```python theme={null}
from openrouter import OpenRouter, operations
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
) as open_router:

    res = open_router.tools.get_tool(security=operations.GetToolSecurity(
        bearer=os.getenv("OPENROUTER_BEARER", ""),
    ), name="openrouter:web_search")

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `security` | [operations.GetToolSecurity](../../operations/gettoolsecurity.mdx) | :heavy\_check\_mark: | N/A | |
| `name` | *str* | :heavy\_check\_mark: | Canonical `openrouter:*` name or any accepted `tools[].type` alias | openrouter:web\_search |
| `http_referer` | *Optional\[str]* | :heavy\_minus\_sign: | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br />This is used to track API usage per application.<br /> | |
| `x_open_router_title` | *Optional\[str]* | :heavy\_minus\_sign: | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br /> | |
| `x_open_router_categories` | *Optional\[str]* | :heavy\_minus\_sign: | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.<br /> | |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | :heavy\_minus\_sign: | Configuration to override the default retry behavior of the client. | |

### Response

**[operations.GetToolResponse](../../operations/gettoolresponse.mdx)**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

