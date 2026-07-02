---
title: "streaming"
source: https://docs.x.com/xdks/python/reference/xdk.streaming
path: xdks/python/reference/xdk.streaming
---

Reference for the streaming Python package in the X API SDK, grouping the client and Pydantic models for the streaming endpoints of the X API v2.

Robust streaming utilities for the X API SDK.

This module provides streaming connection handling with automatic reconnection,
exponential backoff, and comprehensive error handling. Clients can consume
streaming endpoints without worrying about connection management - the SDK
handles all recovery automatically.

### `class xdk.streaming.StreamConfig`

Configuration for streaming connections with retry behavior.

#### Parameters

<ParamField type="int" />

<ParamField type="float" />

<ParamField type="float" />

<ParamField type="float" />

<ParamField type="bool" />

<ParamField type="float or None" />

<ParamField type="int" />

<ParamField type="Callable[[], None] or None" />

<ParamField type="Callable[[Exception or None], None] or None" />

<ParamField type="Callable[[int, float], None] or None" />

<ParamField type="Callable[[[StreamError" />

### `__init__`

#### Parameters

<ParamField type="int" />

<ParamField type="float" />

<ParamField type="float" />

<ParamField type="float" />

<ParamField type="bool" />

<ParamField type="float or None" />

<ParamField type="int" />

<ParamField type="Callable[[], None] or None" />

<ParamField type="Callable[[Exception or None], None] or None" />

<ParamField type="Callable[[int, float], None] or None" />

<ParamField type="Callable[[[StreamError" />

### `on_error : Callable[[[StreamError]`

### `exception xdk.streaming.StreamError`

Exception raised for streaming errors with classification.

#### Parameters

<ParamField type="str" />

<ParamField type="StreamErrorType" />

### `__init__`

#### Parameters

<ParamField type="str" />

<ParamField type="StreamErrorType" />

### `class xdk.streaming.StreamErrorType`

Classification of streaming errors for retry decisions.

#### Parameters

<ParamField type="Any" />

### `class xdk.streaming.StreamState`

Internal state for a streaming connection.

#### Parameters

<ParamField type="int" />

<ParamField type="float" />

<ParamField type="bool" />

<ParamField type="int" />

<ParamField type="StreamError" />

### `__init__`

#### Parameters

<ParamField type="int" />

<ParamField type="float" />

<ParamField type="bool" />

<ParamField type="int" />

<ParamField type="StreamError" />

### `last_error : [StreamError]`

### `xdk.streaming.stream_with_retry`

Stream data from an endpoint with automatic reconnection and exponential backoff.
This function handles all connection management, including:

* Automatic reconnection on disconnects
* Exponential backoff with jitter for retry delays
* Classification of errors as retryable vs fatal
* Lifecycle callbacks for monitoring connection state

#### Parameters

<ParamField type="Session">
  The requests Session to use for HTTP calls.
</ParamField>

<ParamField type="str">
  HTTP method (typically “get”).
</ParamField>

<ParamField type="str">
  The full URL to stream from.
</ParamField>

<ParamField type="StreamConfig">
  StreamConfig with retry and callback settings.
</ParamField>
