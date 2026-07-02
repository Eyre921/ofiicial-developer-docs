---
title: "UsageClient"
source: https://docs.x.com/xdks/python/reference/xdk.usage.client
path: xdks/python/reference/xdk.usage.client
---

Reference for the usage.client Python module in the X API SDK. Client class and methods for calling the usage endpoints of the X API v2.

## UsageClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for usage operations

## Constructors

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
