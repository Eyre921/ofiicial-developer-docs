---
title: "ExternalUsers"
source: https://openrouter.ai/docs/client-sdks/python/sdks/externalusers/README.md
path: docs/client-sdks/python/sdks/externalusers/readme
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ExternalUsers

## Overview

### Available Operations

* [list](#list) - List registered external users
* [create](#create) - Register an external user
* [delete](#delete) - Deactivate a registered external user
* [get](#get) - Get a registered external user
* [update](#update) - Update a registered external user

## list

List registrations belonging to the authenticated organization. Inactive registrations are excluded by default. [Management key](https://openrouter.ai/docs/client-sdks/python/docs/guides/overview/auth/management-api-keys) required.

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

    res = open_router.external_users.list(offset=0, limit=50, include_inactive=False)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `http_referer` | *Optional\[str]* | ➖ | The app identifier should be your app's URL and is used as the primary identifier for rankings. This is used to track API usage per application.  | |
| `x_open_router_title` | *Optional\[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter's dashboard.  | |
| `x_open_router_categories` | *Optional\[str]* | ➖ | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.  | |
| `offset` | *OptionalNullable\[int]* | ➖ | Number of records to skip for pagination | 0 |
| `limit` | *Optional\[int]* | ➖ | Maximum number of records to return (max 100) | 50 |
| `user` | *Optional\[str]* | ➖ | Immutable case-sensitive tracking string supplied as user on inference requests or as external.user on API keys: 1 to 512 characters, well-formed Unicode, no NUL, no surrounding whitespace. URL-encode it in resource paths; an ID of `.` or `..` cannot be addressed by path, so look it up with the list filter. | employee\_123 |
| `include_inactive` | *Optional\[bool]* | ➖ | Include deactivated registrations. | false |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | ➖ | Configuration to override the default retry behavior of the client. | |

### Response

**[operations.ListExternalUsersResponse](../../operations/listexternalusersresponse.mdx)**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## create

Register a caller-supplied tracking ID under the authenticated organization. No login account, policy, or credentials are created. [Management key](https://openrouter.ai/docs/client-sdks/python/docs/guides/overview/auth/management-api-keys) required.

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

    res = open_router.external_users.create(user="employee_123")

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `user` | *str* | ✔️ | Immutable case-sensitive tracking string supplied as user on inference requests or as external.user on API keys: 1 to 512 characters, well-formed Unicode, no NUL, no surrounding whitespace. URL-encode it in resource paths; an ID of `.` or `..` cannot be addressed by path, so look it up with the list filter. | employee\_123 |
| `http_referer` | *Optional\[str]* | ➖ | The app identifier should be your app's URL and is used as the primary identifier for rankings. This is used to track API usage per application.  | |
| `x_open_router_title` | *Optional\[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter's dashboard.  | |
| `x_open_router_categories` | *Optional\[str]* | ➖ | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.  | |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | ➖ | Configuration to override the default retry behavior of the client. | |

### Response

**[components.ExternalUserResponse](../../components/externaluserresponse.mdx)**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.ConflictResponseError | 409 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## delete

Soft-deactivate a registration while retaining its tracking ID. Repeat deactivation succeeds. This does not block inference; reactivate through PATCH. [Management key](https://openrouter.ai/docs/client-sdks/python/docs/guides/overview/auth/management-api-keys) required.

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

    open_router.external_users.delete(user="employee_123")

    # Use the SDK ...

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `user` | *str* | ✔️ | Immutable case-sensitive tracking string supplied as user on inference requests or as external.user on API keys: 1 to 512 characters, well-formed Unicode, no NUL, no surrounding whitespace. URL-encode it in resource paths; an ID of `.` or `..` cannot be addressed by path, so look it up with the list filter. | employee\_123 |
| `http_referer` | *Optional\[str]* | ➖ | The app identifier should be your app's URL and is used as the primary identifier for rankings. This is used to track API usage per application.  | |
| `x_open_router_title` | *Optional\[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter's dashboard.  | |
| `x_open_router_categories` | *Optional\[str]* | ➖ | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.  | |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | ➖ | Configuration to override the default retry behavior of the client. | |

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## get

Retrieve an active or inactive registration by its URL-encoded, caller-supplied tracking ID. [Management key](https://openrouter.ai/docs/client-sdks/python/docs/guides/overview/auth/management-api-keys) required.

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

    res = open_router.external_users.get(user="employee_123")

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `user` | *str* | ✔️ | Immutable case-sensitive tracking string supplied as user on inference requests or as external.user on API keys: 1 to 512 characters, well-formed Unicode, no NUL, no surrounding whitespace. URL-encode it in resource paths; an ID of `.` or `..` cannot be addressed by path, so look it up with the list filter. | employee\_123 |
| `http_referer` | *Optional\[str]* | ➖ | The app identifier should be your app's URL and is used as the primary identifier for rankings. This is used to track API usage per application.  | |
| `x_open_router_title` | *Optional\[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter's dashboard.  | |
| `x_open_router_categories` | *Optional\[str]* | ➖ | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.  | |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | ➖ | Configuration to override the default retry behavior of the client. | |

### Response

**[components.ExternalUserResponse](../../components/externaluserresponse.mdx)**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## update

Update registration state without changing identity. State changes do not enforce inference access. [Management key](https://openrouter.ai/docs/client-sdks/python/docs/guides/overview/auth/management-api-keys) required.

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

    res = open_router.external_users.update(user="employee_123", is_active=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `user` | *str* | ✔️ | Immutable case-sensitive tracking string supplied as user on inference requests or as external.user on API keys: 1 to 512 characters, well-formed Unicode, no NUL, no surrounding whitespace. URL-encode it in resource paths; an ID of `.` or `..` cannot be addressed by path, so look it up with the list filter. | employee\_123 |
| `is_active` | *bool* | ✔️ | Registration state only; does not enforce inference access. | true |
| `http_referer` | *Optional\[str]* | ➖ | The app identifier should be your app's URL and is used as the primary identifier for rankings. This is used to track API usage per application.  | |
| `x_open_router_title` | *Optional\[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter's dashboard.  | |
| `x_open_router_categories` | *Optional\[str]* | ➖ | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.  | |
| `retries` | [Optional\[utils.RetryConfig\]](../../models/utils/retryconfig.mdx) | ➖ | Configuration to override the default retry behavior of the client. | |

### Response

**[components.ExternalUserResponse](../../components/externaluserresponse.mdx)**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

