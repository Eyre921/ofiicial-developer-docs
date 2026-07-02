---
title: "TrendsClient"
source: https://docs.x.com/xdks/python/reference/xdk.trends.client
path: xdks/python/reference/xdk.trends.client
---

Reference for the trends.client Python module in the X API SDK. Client class and methods for calling the trends endpoints of the X API v2.

## TrendsClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for trends operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `get_ai`

Get AI Trends by ID
Retrieves an AI trend by its ID.

#### Parameters

<ParamField type="Any">
  The ID of the ai trend.
</ParamField>

<ParamField type="List or None">
  A comma separated list of News fields to display.
</ParamField>

#### Returns

`GetAiResponse` - Response data

### `get_by_woeid`

Get Trends by WOEID
Retrieves trending topics for a specific location identified by its WOEID.

#### Parameters

<ParamField type="int">
  The WOEID of the place to lookup a trend for.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Trend fields to display.
</ParamField>

#### Returns

`GetByWoeidResponse` - Response data

### `get_personalized`

Get personalized Trends
Retrieves personalized trending topics for the authenticated user.

#### Parameters

<ParamField type="List or None">
  A comma separated list of PersonalizedTrend fields to display.
</ParamField>

#### Returns

`GetPersonalizedResponse` - Response data
