---
title: "PostsClient"
source: https://docs.x.com/xdks/python/reference/xdk.posts.client
path: xdks/python/reference/xdk.posts.client
---

Reference for the posts.client Python module in the X API SDK. Client class and methods for calling the posts endpoints of the X API v2.

## PostsClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for posts operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `create`

Create or Edit Post
Creates a new Post for the authenticated user, or edits an existing Post when edit\_options are provided.
body: Request body
:returns: Response data
:rtype: CreateResponse

#### Parameters

<ParamField type="CreateRequest" />

### `delete`

Delete Post
Deletes a specific Post by its ID, if owned by the authenticated user.

#### Parameters

<ParamField type="Any">
  The ID of the Post to be deleted.
</ParamField>

#### Returns

`DeleteResponse` - Response data

### `get_analytics`

Get Post analytics
Retrieves analytics data for specified Posts within a defined time range.

#### Parameters

<ParamField type="List">
  A comma separated list of Post IDs. Up to 100 are allowed in a single request.
</ParamField>

<ParamField type="str">
  YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
</ParamField>

<ParamField type="str">
  YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
</ParamField>

<ParamField type="str">
  The granularity for the search counts results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Analytics fields to display.
</ParamField>

#### Returns

`GetAnalyticsResponse` - Response data

### `get_by_id`

Get Post by ID
Retrieves details of a specific Post by its ID.

#### Parameters

<ParamField type="Any">
  A single Post ID.
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

`GetByIdResponse` - Response data

### `get_by_ids`

Get Posts by IDs
Retrieves details of multiple Posts by their IDs.

#### Parameters

<ParamField type="List">
  A comma separated list of Post IDs. Up to 100 are allowed in a single request.
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

`GetByIdsResponse` - Response data

### `get_counts_all`

Get count of all Posts
Retrieves the count of Posts matching a search query from the full archive.

#### Parameters

<ParamField type="str">
  One query/rule/filter for matching Posts. Refer to [https://t.co/rulelength](https://t.co/rulelength) to identify the max query length.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID greater than (that is, more recent than) the specified ID.
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID less than (that is, older than) the specified ID.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
</ParamField>

<ParamField type="str or None">
  The granularity for the search counts results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of SearchCount fields to display.
</ParamField>

#### Returns

`IteratorGetCountsAllResponse`

### `get_counts_recent`

Get count of recent Posts
Retrieves the count of Posts from the last 7 days matching a search query.

#### Parameters

<ParamField type="str">
  One query/rule/filter for matching Posts. Refer to [https://t.co/rulelength](https://t.co/rulelength) to identify the max query length.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID greater than (that is, more recent than) the specified ID.
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID less than (that is, older than) the specified ID.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
</ParamField>

<ParamField type="str or None">
  The granularity for the search counts results.
</ParamField>

<ParamField type="List or None">
  A comma separated list of SearchCount fields to display.
</ParamField>

#### Returns

`IteratorGetCountsRecentResponse`

### `get_insights28hr`

Get 28-hour Post insights
Retrieves engagement metrics for specified Posts over the last 28 hours.

#### Parameters

<ParamField type="List">
  List of PostIds for 28hr metrics.
</ParamField>

<ParamField type="str">
  granularity of metrics response.
</ParamField>

<ParamField type="List">
  request metrics for historical request.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Engagement fields to display.
</ParamField>

#### Returns

`GetInsights28hrResponse` - Response data

### `get_insights_historical`

Get historical Post insights
Retrieves historical engagement metrics for specified Posts within a defined time range.

#### Parameters

<ParamField type="List">
  List of PostIds for historical metrics.
</ParamField>

<ParamField type="str">
  YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
</ParamField>

<ParamField type="str">
  YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
</ParamField>

<ParamField type="str">
  granularity of metrics response.
</ParamField>

<ParamField type="List">
  request metrics for historical request.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Engagement fields to display.
</ParamField>

#### Returns

`GetInsightsHistoricalResponse` - Response data

### `get_liking_users`

Get Liking Users
Retrieves a list of Users who liked a specific Post by its ID.

#### Parameters

<ParamField type="Any">
  A single Post ID.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results.
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

`IteratorGetLikingUsersResponse`

### `get_quoted`

Get Quoted Posts
Retrieves a list of Posts that quote a specific Post by its ID.

#### Parameters

<ParamField type="Any">
  A single Post ID.
</ParamField>

<ParamField type="int or None">
  The maximum number of results to be returned.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get a specified ‘page’ of results.
</ParamField>

<ParamField type="List or None">
  The set of entities to exclude (e.g. ‘replies’ or ‘retweets’).
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

`IteratorGetQuotedResponse`

### `get_reposted_by`

Get Reposted by
Retrieves a list of Users who reposted a specific Post by its ID.

#### Parameters

<ParamField type="Any">
  A single Post ID.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results.
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

`IteratorGetRepostedByResponse`

### `get_reposts`

Get Reposts
Retrieves a list of Posts that repost a specific Post by its ID.

#### Parameters

<ParamField type="Any">
  A single Post ID.
</ParamField>

<ParamField type="int or None">
  The maximum number of results.
</ParamField>

<ParamField type="Any or None">
  This parameter is used to get the next ‘page’ of results.
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

`IteratorGetRepostsResponse`

### `hide_reply`

Hide reply
Hides or unhides a reply to a conversation owned by the authenticated user.

#### Parameters

<ParamField type="Any">
  The ID of the reply that you want to hide or unhide.
</ParamField>

<ParamField type="HideReplyRequest">
  Request body
</ParamField>

### `search_all`

Search all Posts
Retrieves Posts from the full archive matching a search query.

#### Parameters

<ParamField type="str">
  One query/rule/filter for matching Posts. Refer to [https://t.co/rulelength](https://t.co/rulelength) to identify the max query length.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID greater than (that is, more recent than) the specified ID.
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID less than (that is, older than) the specified ID.
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

<ParamField type="str or None">
  This order in which to return results.
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

`IteratorSearchAllResponse`

### `search_recent`

Search recent Posts
Retrieves Posts from the last 7 days matching a search query.

#### Parameters

<ParamField type="str">
  One query/rule/filter for matching Posts. Refer to [https://t.co/rulelength](https://t.co/rulelength) to identify the max query length.
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
</ParamField>

<ParamField type="str or None">
  YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID greater than (that is, more recent than) the specified ID.
</ParamField>

<ParamField type="Any or None">
  Returns results with a Post ID less than (that is, older than) the specified ID.
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

<ParamField type="str or None">
  This order in which to return results.
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

`IteratorSearchRecentResponse`
