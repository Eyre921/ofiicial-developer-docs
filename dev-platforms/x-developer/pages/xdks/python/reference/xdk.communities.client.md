---
title: "CommunitiesClient"
source: https://docs.x.com/xdks/python/reference/xdk.communities.client
path: xdks/python/reference/xdk.communities.client
---

Reference for the communities.client Python module in the X API SDK. Client class and methods for calling the communities endpoints of the X API v2.

## CommunitiesClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for communities operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `get_by_id`

Get Community by ID
Retrieves details of a specific Community by its ID.

#### Parameters

<ParamField type="Any">
  The ID of the Community.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Community fields to display.
</ParamField>

#### Returns

`GetByIdResponse` - Response data

### `search`

Search Communities
Retrieves a list of Communities matching the specified search query.

#### Parameters

<ParamField type="str">
  Query to search communities.
</ParamField>

<ParamField type="int or None">
  The maximum number of search results to be returned by a request.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Community fields to display.
</ParamField>

#### Returns

`IteratorSearchResponse`
