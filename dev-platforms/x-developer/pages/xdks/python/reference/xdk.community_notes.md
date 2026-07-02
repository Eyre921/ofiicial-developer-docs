---
title: "CommunityNotesClient"
source: https://docs.x.com/xdks/python/reference/xdk.community_notes
path: xdks/python/reference/xdk.community_notes
---

Reference for the community_notes Python package in the X API SDK, grouping the client and Pydantic models for the community notes endpoints of the X API v2.

## Submodules

* [xdk.community\_notes.client module](/xdks/python/reference/xdk.community_notes.client)
  * [`CommunityNotesClient`](/xdks/python/reference/xdk.community_notes.client#xdk.community_notes.client.CommunityNotesClient)
    * [`CommunityNotesClient.__init__()`](/xdks/python/reference/xdk.community_notes.client#xdk.community_notes.client.CommunityNotesClient.__init__)
    * [`CommunityNotesClient.create()`](/xdks/python/reference/xdk.community_notes.client#xdk.community_notes.client.CommunityNotesClient.create)
    * [`CommunityNotesClient.delete()`](/xdks/python/reference/xdk.community_notes.client#xdk.community_notes.client.CommunityNotesClient.delete)
    * [`CommunityNotesClient.evaluate()`](/xdks/python/reference/xdk.community_notes.client#xdk.community_notes.client.CommunityNotesClient.evaluate)
    * [`CommunityNotesClient.search_eligible_posts()`](/xdks/python/reference/xdk.community_notes.client#xdk.community_notes.client.CommunityNotesClient.search_eligible_posts)
    * [`CommunityNotesClient.search_written()`](/xdks/python/reference/xdk.community_notes.client#xdk.community_notes.client.CommunityNotesClient.search_written)
* [xdk.community\_notes.models module](/xdks/python/reference/xdk.community_notes.models)
  * [`CreateRequest`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.CreateRequest)
    * [`CreateRequest.model_config`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.CreateRequest.model_config)
  * [`CreateResponse`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.CreateResponse)
    * [`CreateResponse.model_config`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.CreateResponse.model_config)
  * [`DeleteResponse`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.DeleteResponse)
    * [`DeleteResponse.model_config`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.DeleteResponse.model_config)
  * [`EvaluateRequest`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.EvaluateRequest)
    * [`EvaluateRequest.model_config`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.EvaluateRequest.model_config)
  * [`EvaluateResponse`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.EvaluateResponse)
    * [`EvaluateResponse.model_config`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.EvaluateResponse.model_config)
  * [`SearchEligiblePostsResponse`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.SearchEligiblePostsResponse)
    * [`SearchEligiblePostsResponse.model_config`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.SearchEligiblePostsResponse.model_config)
  * [`SearchWrittenResponse`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.SearchWrittenResponse)
    * [`SearchWrittenResponse.model_config`](/xdks/python/reference/xdk.community_notes.models#xdk.community_notes.models.SearchWrittenResponse.model_config)

## Module contents

This module provides access to the community notes endpoints of the X API
and serves as the main entry point for all community notes-related functionality.

### `class xdk.community_notes.CommunityNotesClient`

Client for community notes operations

#### Parameters

<ParamField type="Client" />

### `__init__`

#### Parameters

<ParamField type="Client" />

### `create`

Create a Community Note
Creates a community note endpoint for LLM use case.
body: Request body
:returns: Response data
:rtype: CreateResponse

#### Parameters

<ParamField type="CreateRequest" />

### `delete`

Delete a Community Note
Deletes a community note.

#### Parameters

<ParamField type="Any">
  The community note id to delete.
</ParamField>

#### Returns

`DeleteResponse` - Response data

### `evaluate`

Evaluate a Community Note
Endpoint to evaluate a community note.
body: Request body
:returns: Response data
:rtype: EvaluateResponse

#### Parameters

<ParamField type="EvaluateRequest" />

### `search_eligible_posts`

Search for Posts Eligible for Community Notes
Returns all the posts that are eligible for community notes.

#### Parameters

<ParamField type="bool">
  If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product.
</ParamField>

<ParamField type="str or None">
  Pagination token to get next set of posts eligible for notes.
</ParamField>

<ParamField type="int or None">
  Max results to return.
</ParamField>

<ParamField type="str or None">
  The selection of posts to return. Valid values are ‘feed\_size: small’ and ‘feed\_size: large’. Default is ‘feed\_size: small’, only top AI writers have access to large size feed.
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

`IteratorSearchEligiblePostsResponse`

### `search_written`

Search for Community Notes Written
Returns all the community notes written by the user.

#### Parameters

<ParamField type="bool">
  If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.
</ParamField>

<ParamField type="str or None">
  Pagination token to get next set of posts eligible for notes.
</ParamField>

<ParamField type="int or None">
  Max results to return.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Note fields to display.
</ParamField>

#### Returns

`IteratorSearchWrittenResponse`
