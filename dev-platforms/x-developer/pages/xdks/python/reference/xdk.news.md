---
title: "NewsClient"
source: https://docs.x.com/xdks/python/reference/xdk.news
path: xdks/python/reference/xdk.news
---

Reference for the news Python package in the X API SDK, grouping the client and Pydantic models for the news endpoints of the X API v2.

## Submodules

* [xdk.news.client module](/xdks/python/reference/xdk.news.client)
  * [`NewsClient`](/xdks/python/reference/xdk.news.client#xdk.news.client.NewsClient)
    * [`NewsClient.__init__()`](/xdks/python/reference/xdk.news.client#xdk.news.client.NewsClient.__init__)
    * [`NewsClient.get()`](/xdks/python/reference/xdk.news.client#xdk.news.client.NewsClient.get)
    * [`NewsClient.search()`](/xdks/python/reference/xdk.news.client#xdk.news.client.NewsClient.search)
* [xdk.news.models module](/xdks/python/reference/xdk.news.models)
  * [`GetResponse`](/xdks/python/reference/xdk.news.models#xdk.news.models.GetResponse)
    * [`GetResponse.model_config`](/xdks/python/reference/xdk.news.models#xdk.news.models.GetResponse.model_config)
  * [`SearchResponse`](/xdks/python/reference/xdk.news.models#xdk.news.models.SearchResponse)
    * [`SearchResponse.model_config`](/xdks/python/reference/xdk.news.models#xdk.news.models.SearchResponse.model_config)

## Module contents

This module provides access to the news endpoints of the X API
and serves as the main entry point for all news-related functionality.

### `class xdk.news.NewsClient`

Client for news operations

#### Parameters

<ParamField type="Client" />

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
