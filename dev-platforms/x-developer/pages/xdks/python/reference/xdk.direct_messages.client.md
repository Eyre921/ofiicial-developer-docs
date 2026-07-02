---
title: "DirectMessagesClient"
source: https://docs.x.com/xdks/python/reference/xdk.direct_messages.client
path: xdks/python/reference/xdk.direct_messages.client
---

Reference for the direct_messages.client Python module in the X API SDK. Client class and methods for calling the direct messages endpoints of the X API v2.

## DirectMessagesClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for direct messages operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `create_by_conversation_id`

Create DM message by conversation ID
Sends a new direct message to a specific conversation by its ID.

#### Parameters

<ParamField type="str">
  The DM Conversation ID.
</ParamField>

<ParamField type="CreateByConversationIdRequest">
  Request body
</ParamField>

### `create_by_participant_id`

Create DM message by participant ID
Sends a new direct message to a specific participant by their ID.

#### Parameters

<ParamField type="Any">
  The ID of the recipient user that will receive the DM.
</ParamField>

<ParamField type="CreateByParticipantIdRequest">
  Request body
</ParamField>

### `create_conversation`

Create DM conversation
Initiates a new direct message conversation with specified participants.
body: Request body
:returns: Response data
:rtype: CreateConversationResponse

#### Parameters

<ParamField type="CreateConversationRequest" />

### `delete_events`

Delete DM event
Deletes a specific direct message event by its ID, if owned by the authenticated user.

#### Parameters

<ParamField type="Any">
  The ID of the direct-message event to delete.
</ParamField>

#### Returns

`DeleteEventsResponse` - Response data

### `get_events`

Get DM events
Retrieves a list of recent direct message events across all conversations.

#### Parameters

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get a specified ‘page’ of results.
</ParamField>

<ParamField type="List or None">
  The set of event\_types to include in the results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of DmEvent fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

#### Returns

`IteratorGetEventsResponse`

### `get_events_by_conversation_id`

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.

#### Parameters

<ParamField type="Any">
  The DM conversation ID.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get a specified ‘page’ of results.
</ParamField>

<ParamField type="List or None">
  The set of event\_types to include in the results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of DmEvent fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

#### Returns

`IteratorGetEventsByConversationIdResponse`

### `get_events_by_id`

Get DM event by ID
Retrieves details of a specific direct message event by its ID.

#### Parameters

<ParamField type="Any">
  dm event id.
</ParamField>

<ParamField type="List or None">
  A comma separated list of DmEvent fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

#### Returns

`GetEventsByIdResponse` - Response data

### `get_events_by_participant_id`

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.

#### Parameters

<ParamField type="Any">
  The ID of the participant user for the One to One DM conversation.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get a specified ‘page’ of results.
</ParamField>

<ParamField type="List or None">
  The set of event\_types to include in the results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of DmEvent fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

#### Returns

`IteratorGetEventsByParticipantIdResponse`
