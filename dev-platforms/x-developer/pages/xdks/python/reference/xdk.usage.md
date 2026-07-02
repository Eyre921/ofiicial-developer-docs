---
title: "UsageClient"
source: https://docs.x.com/xdks/python/reference/xdk.usage
path: xdks/python/reference/xdk.usage
---

Reference for the usage Python package in the X API SDK, grouping the client and Pydantic models for the usage endpoints of the X API v2.

## Submodules

* [xdk.usage.client module](/xdks/python/reference/xdk.usage.client)
  * [`UsageClient`](/xdks/python/reference/xdk.usage.client#xdk.usage.client.UsageClient)
    * [`UsageClient.__init__()`](/xdks/python/reference/xdk.usage.client#xdk.usage.client.UsageClient.__init__)
    * [`UsageClient.get()`](/xdks/python/reference/xdk.usage.client#xdk.usage.client.UsageClient.get)
* [xdk.usage.models module](/xdks/python/reference/xdk.usage.models)
  * [`GetResponse`](/xdks/python/reference/xdk.usage.models#xdk.usage.models.GetResponse)
    * [`GetResponse.model_config`](/xdks/python/reference/xdk.usage.models#xdk.usage.models.GetResponse.model_config)

## Module contents

This module provides access to the usage endpoints of the X API
and serves as the main entry point for all usage-related functionality.

### `class xdk.usage.UsageClient`

Client for usage operations

#### Parameters

<ParamField type="Client" />

### `__init__`

#### Parameters

<ParamField type="Client" />

### `get`

Get usage
Retrieves usage statistics for Posts over a specified number of days.

#### Parameters

<ParamField type="int or None">
  The number of days for which you need usage for.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Usage fields to display.
</ParamField>

#### Returns

`GetResponse` - Response data
