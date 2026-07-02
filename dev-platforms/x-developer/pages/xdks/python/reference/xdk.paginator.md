---
title: "paginator"
source: https://docs.x.com/xdks/python/reference/xdk.paginator
path: xdks/python/reference/xdk.paginator
---

Reference for the paginator Python package in the X API SDK, grouping the client and Pydantic models for the paginator endpoints of the X API v2.

Cursor-based pagination utilities for the X API SDK.

This module provides a Cursor class for elegant pagination support across
all API clients. The Cursor enables easy iteration over paginated results
using both .pages() and .items() methods with proper type safety.

### `class xdk.paginator.Cursor`

\[`ResponseType`]

#### Parameters

<ParamField type="PaginatableMethod" />

### `__init__`

Initialize the cursor.

#### Parameters

<ParamField type="PaginatableMethod">
  The API method to call for each page (must support pagination)
</ParamField>

### `items`

Iterate over individual items from paginated responses.

#### Parameters

<ParamField type="int or None">
  Maximum number of items to return (None for unlimited)
</ParamField>

#### Returns

`IteratorAny`

### `pages`

Iterate over pages of responses.

#### Parameters

<ParamField type="int or None">
  Maximum number of pages to return (None for unlimited)
</ParamField>

#### Returns

`IteratorResponseType`

### `class xdk.paginator.PaginatableMethod`

\[`ResponseType`]

### `__init__`

### `xdk.paginator.cursor`

Create a cursor with proper type inference and validation.
This factory function helps with type inference so you get proper
type hints for the response type, and validates that the method
supports pagination at both static analysis and runtime.

#### Parameters

<ParamField type="PaginatableMethod">
  The API method to wrap (must support pagination)
</ParamField>
