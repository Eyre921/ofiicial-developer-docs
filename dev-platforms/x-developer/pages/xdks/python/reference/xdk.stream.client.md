---
title: "StreamClient"
source: https://docs.x.com/xdks/python/reference/xdk.stream.client
path: xdks/python/reference/xdk.stream.client
---

Reference for the stream.client Python module in the X API SDK. Client class and methods for calling the stream endpoints of the X API v2.

This module provides a client for interacting with the stream endpoints of the X API.
Real-time streaming operations return generators that yield data as it arrives.
Streaming connections are automatically managed with exponential backoff retry logic for robust handling.

## StreamClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Streaming Client for stream operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `get_rule_counts`

Get stream rule counts
Retrieves the count of rules in the active rule set for the filtered stream.

#### Parameters

<ParamField type="List or None">
  A comma separated list of RulesCount fields to display.
</ParamField>

#### Returns

`GetRuleCountsResponse` - Response data

### `get_rules`

Get stream rules
Retrieves the active rule set or a subset of rules for the filtered stream.

#### Parameters

<ParamField type="List or None">
  A comma-separated list of Rule IDs.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="str or None">
  This value is populated by passing the ‘next\_token’ returned in a request to paginate through results.
</ParamField>

#### Returns

`IteratorGetRulesResponse`

### `labels_compliance`

Stream Post labels (Streaming)
Streams all labeling events applied to Posts.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `likes_compliance`

Stream Likes compliance data (Streaming)
Streams all compliance data related to Likes for Users.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `likes_firehose`

Stream all Likes (Streaming)
Streams all public Likes in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of LikeWithTweetAuthor fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `likes_sample10`

Stream sampled Likes (Streaming)
Streams a 10% sample of public Likes in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of LikeWithTweetAuthor fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts`

Stream filtered Posts (Streaming)
Streams Posts in real-time matching the active rule set.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_compliance`

Stream Posts compliance data (Streaming)
Streams all compliance data related to Posts.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_firehose`

Stream all Posts (Streaming)
Streams all public Posts in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_firehose_en`

Stream English Posts (Streaming)
Streams all public English-language Posts in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_firehose_ja`

Stream Japanese Posts (Streaming)
Streams all public Japanese-language Posts in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_firehose_ko`

Stream Korean Posts (Streaming)
Streams all public Korean-language Posts in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_firehose_pt`

Stream Portuguese Posts (Streaming)
Streams all public Portuguese-language Posts in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_sample`

Stream sampled Posts (Streaming)
Streams a 1% sample of public Posts in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `posts_sample10`

Stream 10% sampled Posts (Streaming)
Streams a 10% sample of public Posts in real-time.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Poll fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Place fields to display.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>

### `update_rules`

Update stream rules
Adds or deletes rules from the active rule set for the filtered stream.

#### Parameters

<ParamField type="UpdateRulesRequest">
  Request body
</ParamField>

### `users_compliance`

Stream Users compliance data (Streaming)
Streams all compliance data related to Users.
This is a streaming endpoint that yields data in real-time as it becomes available.
Each yielded item represents a single data point from the stream.
The connection is automatically managed with exponential backoff retry logic.
If the stream disconnects, the SDK will automatically reconnect without client intervention.

#### Parameters

<ParamField type="int">
  The partition number.
</ParamField>

<ParamField type="int or None">
  The number of minutes of backfill requested.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.
</ParamField>

<ParamField type="StreamConfig">
  Optional StreamConfig for customizing retry behavior, timeouts, and callbacks.
</ParamField>
