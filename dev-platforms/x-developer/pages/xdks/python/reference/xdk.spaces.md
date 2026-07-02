---
title: "SpacesClient"
source: https://docs.x.com/xdks/python/reference/xdk.spaces
path: xdks/python/reference/xdk.spaces
---

Reference for the spaces Python package in the X API SDK, grouping the client and Pydantic models for the spaces endpoints of the X API v2.

## Submodules

* [xdk.spaces.client module](/xdks/python/reference/xdk.spaces.client)
  * [`SpacesClient`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient)
    * [`SpacesClient.__init__()`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient.__init__)
    * [`SpacesClient.get_buyers()`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient.get_buyers)
    * [`SpacesClient.get_by_creator_ids()`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient.get_by_creator_ids)
    * [`SpacesClient.get_by_id()`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient.get_by_id)
    * [`SpacesClient.get_by_ids()`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient.get_by_ids)
    * [`SpacesClient.get_posts()`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient.get_posts)
    * [`SpacesClient.search()`](/xdks/python/reference/xdk.spaces.client#xdk.spaces.client.SpacesClient.search)
* [xdk.spaces.models module](/xdks/python/reference/xdk.spaces.models)
  * [`GetBuyersResponse`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetBuyersResponse)
    * [`GetBuyersResponse.model_config`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetBuyersResponse.model_config)
  * [`GetByCreatorIdsResponse`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetByCreatorIdsResponse)
    * [`GetByCreatorIdsResponse.model_config`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetByCreatorIdsResponse.model_config)
  * [`GetByIdResponse`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetByIdResponse)
    * [`GetByIdResponse.model_config`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetByIdResponse.model_config)
  * [`GetByIdsResponse`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetByIdsResponse)
    * [`GetByIdsResponse.model_config`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetByIdsResponse.model_config)
  * [`GetPostsResponse`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetPostsResponse)
    * [`GetPostsResponse.model_config`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.GetPostsResponse.model_config)
  * [`SearchResponse`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.SearchResponse)
    * [`SearchResponse.model_config`](/xdks/python/reference/xdk.spaces.models#xdk.spaces.models.SearchResponse.model_config)

## Module contents

This module provides access to the spaces endpoints of the X API
and serves as the main entry point for all spaces-related functionality.

### `class xdk.spaces.SpacesClient`

Client for spaces operations

#### Parameters

<ParamField type="Client" />

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
