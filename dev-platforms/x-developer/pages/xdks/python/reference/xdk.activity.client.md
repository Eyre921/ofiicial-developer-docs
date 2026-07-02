---
title: "ActivityClient"
source: https://docs.x.com/xdks/python/reference/xdk.activity.client
path: xdks/python/reference/xdk.activity.client
---

Reference for the activity.client Python module in the X API SDK. Client class and methods for calling the activity endpoints of the X API v2.

This module provides a client for interacting with the activity endpoints of the X API.
Real-time streaming operations return generators that yield data as it arrives.
Streaming connections are automatically managed with exponential backoff retry logic for robust handling.

## ActivityClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Streaming Client for activity operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `create_subscription`

Create X activity subscription
Creates a subscription for an X activity event
body: Request body
:returns: Response data
:rtype: CreateSubscriptionResponse

#### Parameters

<ParamField type="CreateSubscriptionRequest" />

### `delete_subscription`

Deletes X activity subscription
Deletes a subscription for an X activity event

#### Parameters

<ParamField type="Any">
  The ID of the subscription to delete.
</ParamField>

#### Returns

`DeleteSubscriptionResponse` - Response data

### `get_subscriptions`

Get X activity subscriptions
Get a list of active subscriptions for XAA
:returns: Response data
:rtype: GetSubscriptionsResponse

#### Returns

`GetSubscriptionsResponse`

### `stream`

Activity Stream (Streaming)
Stream of X Activities
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

### `update_subscription`

Update X activity subscription
Updates a subscription for an X activity event

#### Parameters

<ParamField type="Any">
  The ID of the subscription to update.
</ParamField>

<ParamField type="UpdateSubscriptionRequest">
  Request body
</ParamField>
