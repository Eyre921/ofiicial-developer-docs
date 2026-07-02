---
title: "NewsClient"
source: https://docs.x.com/xdks/python/reference/xdk.news.client
path: xdks/python/reference/xdk.news.client
---

Reference for the news.client Python module in the X API SDK. Client class and methods for calling the news endpoints of the X API v2.

## NewsClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for news operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `get`

Get news stories by ID
Retrieves news story by its ID.

#### Parameters

<ParamField type="Any">
  The ID of the news story.
</ParamField>

<ParamField type="List or None">
  A comma separated list of News fields to display.
</ParamField>

#### Returns

`GetResponse` - Response data

### `search`

Search News
Retrieves a list of News stories matching the specified search query.

#### Parameters

<ParamField type="str">
  The search query.
</ParamField>

<ParamField type="int or None">
  The number of results to return.
</ParamField>

<ParamField type="int or None">
  The maximum age of the News story to search for.
</ParamField>

<ParamField type="List or None">
  A comma separated list of News fields to display.
</ParamField>

#### Returns

`SearchResponse` - Response data
