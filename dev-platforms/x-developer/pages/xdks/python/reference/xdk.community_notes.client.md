---
title: "CommunityNotesClient"
source: https://docs.x.com/xdks/python/reference/xdk.community_notes.client
path: xdks/python/reference/xdk.community_notes.client
---

Reference for the community_notes.client Python module in the X API SDK. Client class and methods for calling the community notes endpoints of the X API v2.

## CommunityNotesClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for community notes operations

## Constructors

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
