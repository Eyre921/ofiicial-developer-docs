---
title: "Organization"
source: https://openrouter.ai/docs/client-sdks/go/sdks/organization/README.md
path: docs/client-sdks/go/sdks/organization/readme
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization

> Organization endpoints

## Overview

Organization endpoints

### Available Operations

* [ListMembers](#listmembers) - List organization members
* [GetSettings](#getsettings) - Get organization settings
* [UpdateSettings](#updatesettings) - Update organization settings

## ListMembers

List all members of the organization associated with the authenticated management key. [Management key](/docs/client-sdks/go/docs/guides/overview/auth/management-api-keys) required.

### Example Usage

```go theme={null}
package main

import(
	"context"
	"os"
	openrouter "github.com/OpenRouterTeam/go-sdk"
	"github.com/OpenRouterTeam/go-sdk/optionalnullable"
	"log"
)

func main() {
    ctx := context.Background()

    s := openrouter.New(
        openrouter.WithSecurity(os.Getenv("OPENROUTER_API_KEY")),
    )

    res, err := s.Organization.ListMembers(ctx, optionalnullable.From(openrouter.Pointer[int64](0)), openrouter.Pointer[int64](50))
    if err != nil {
        log.Fatal(err)
    }
    if res != nil {
        for {
            // handle items

            res, err = res.Next()

            if err != nil {
                // handle error
            }

            if res == nil {
                break
            }
        }
    }
}
```

### Parameters

| Parameter | Type | Required | Description | Example |
| - | - | - | - | - |
| `ctx` | [context.Context](https://pkg.go.dev/context#Context) | :heavy\_check\_mark: | The context to use for the request. | |
| `offset` | optionalnullable.OptionalNullable\[`int64`] | :heavy\_minus\_sign: | Number of records to skip for pagination | 0 |
| `limit` | `*int64` | :heavy\_minus\_sign: | Maximum number of records to return (max 100) | 50 |
| `opts` | \[][operations.Option](../../models/operations/option.mdx) | :heavy\_minus\_sign: | The options for this request. | |

### Response

**[\*operations.ListOrganizationMembersResponse](../../models/operations/listorganizationmembersresponse.mdx), error**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| sdkerrors.UnauthorizedResponseError | 401 | application/json |
| sdkerrors.NotFoundResponseError | 404 | application/json |
| sdkerrors.InternalServerResponseError | 500 | application/json |
| sdkerrors.APIError | 4XX, 5XX | \*/\* |

## GetSettings

Get the settings of the organization associated with the authenticated management key. [Management key](/docs/client-sdks/go/docs/guides/overview/auth/management-api-keys) required.

### Example Usage

```go theme={null}
package main

import(
	"context"
	"os"
	openrouter "github.com/OpenRouterTeam/go-sdk"
	"log"
)

func main() {
    ctx := context.Background()

    s := openrouter.New(
        openrouter.WithSecurity(os.Getenv("OPENROUTER_API_KEY")),
    )

    res, err := s.Organization.GetSettings(ctx)
    if err != nil {
        log.Fatal(err)
    }
    if res != nil {
        // handle response
    }
}
```

### Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `ctx` | [context.Context](https://pkg.go.dev/context#Context) | :heavy\_check\_mark: | The context to use for the request. |
| `opts` | \[][operations.Option](../../models/operations/option.mdx) | :heavy\_minus\_sign: | The options for this request. |

### Response

**[\*operations.GetOrganizationSettingsResponse](../../models/operations/getorganizationsettingsresponse.mdx), error**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| sdkerrors.UnauthorizedResponseError | 401 | application/json |
| sdkerrors.NotFoundResponseError | 404 | application/json |
| sdkerrors.InternalServerResponseError | 500 | application/json |
| sdkerrors.APIError | 4XX, 5XX | \*/\* |

## UpdateSettings

Update the settings of the organization associated with the authenticated management key. [Management key](/docs/client-sdks/go/docs/guides/overview/auth/management-api-keys) required.

### Example Usage

```go theme={null}
package main

import(
	"context"
	"os"
	openrouter "github.com/OpenRouterTeam/go-sdk"
	"github.com/OpenRouterTeam/go-sdk/models/components"
	"log"
)

func main() {
    ctx := context.Background()

    s := openrouter.New(
        openrouter.WithSecurity(os.Getenv("OPENROUTER_API_KEY")),
    )

    res, err := s.Organization.UpdateSettings(ctx, components.UpdateOrganizationSettingsRequest{
        IsFilteredModelCatalogEnabled: true,
    })
    if err != nil {
        log.Fatal(err)
    }
    if res != nil {
        // handle response
    }
}
```

### Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `ctx` | [context.Context](https://pkg.go.dev/context#Context) | :heavy\_check\_mark: | The context to use for the request. |
| `request` | [components.UpdateOrganizationSettingsRequest](../../models/components/updateorganizationsettingsrequest.mdx) | :heavy\_check\_mark: | The request object to use for the request. |
| `opts` | \[][operations.Option](../../models/operations/option.mdx) | :heavy\_minus\_sign: | The options for this request. |

### Response

**[\*operations.UpdateOrganizationSettingsResponse](../../models/operations/updateorganizationsettingsresponse.mdx), error**

### Errors

| Error Type | Status Code | Content Type |
| - | - | - |
| sdkerrors.BadRequestResponseError | 400 | application/json |
| sdkerrors.UnauthorizedResponseError | 401 | application/json |
| sdkerrors.NotFoundResponseError | 404 | application/json |
| sdkerrors.InternalServerResponseError | 500 | application/json |
| sdkerrors.APIError | 4XX, 5XX | \*/\* |

