---
title: "SpacesClient"
source: https://docs.x.com/xdks/python/reference/xdk.spaces.client
path: xdks/python/reference/xdk.spaces.client
---

Reference for the spaces.client Python module in the X API SDK. Client class and methods for calling the spaces endpoints of the X API v2.

## SpacesClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for spaces operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `get_buyers`

Get Space ticket buyers
Retrieves a list of Users who purchased tickets to a specific Space by its ID.

#### Parameters

<ParamField type="str">
  The ID of the Space to be retrieved.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get a specified ‘page’ of results.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Tweet fields to display.
</ParamField>

#### Returns

`IteratorGetBuyersResponse`

### `get_by_creator_ids`

Get Spaces by creator IDs
Retrieves details of Spaces created by specified User IDs.

#### Parameters

<ParamField type="List">
  The IDs of Users to search through.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Space fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Topic fields to display.
</ParamField>

#### Returns

`GetByCreatorIdsResponse` - Response data

### `get_by_id`

Get space by ID
Retrieves details of a specific space by its ID.

#### Parameters

<ParamField type="str">
  The ID of the Space to be retrieved.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Space fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Topic fields to display.
</ParamField>

#### Returns

`GetByIdResponse` - Response data

### `get_by_ids`

Get Spaces by IDs
Retrieves details of multiple Spaces by their IDs.

#### Parameters

<ParamField type="List">
  The list of Space IDs to return.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Space fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Topic fields to display.
</ParamField>

#### Returns

`GetByIdsResponse` - Response data

### `get_posts`

Get Space Posts
Retrieves a list of Posts shared in a specific Space by its ID.

#### Parameters

<ParamField type="str">
  The ID of the Space to be retrieved.
</ParamField>

<ParamField type="int or None">
  The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100.
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

#### Returns

`GetPostsResponse` - Response data

### `search`

Search Spaces
Retrieves a list of Spaces matching the specified search query.

#### Parameters

<ParamField type="str">
  The search query.
</ParamField>

<ParamField type="str or None">
  The state of Spaces to search for.
</ParamField>

<ParamField type="int or None">
  The number of results to return.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Space fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of fields to expand.
</ParamField>

<ParamField type="List or None">
  A comma separated list of User fields to display.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Topic fields to display.
</ParamField>

#### Returns

`SearchResponse` - Response data
