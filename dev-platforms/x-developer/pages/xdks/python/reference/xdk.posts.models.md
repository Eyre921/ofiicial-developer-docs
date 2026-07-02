---
title: "Posts.Models"
source: https://docs.x.com/xdks/python/reference/xdk.posts.models
path: xdks/python/reference/xdk.posts.models
---

Reference for the posts.models Python module in the X API SDK. Pydantic request and response models for the posts endpoints of the X API v2.

This module provides Pydantic models for request and response data structures
for the posts endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

### class xdk.posts.models.CreateRequest

Request model for create

<ResponseField name="model_config" type="ConfigDict">
  Default: `{'populate_by_name': True, 'validate_by_alias': True, 'validate_by_name': True}`

  Configuration for the model, should be a dictionary conforming to \[ConfigDict]\[pydantic.config.ConfigDict].
</ResponseField>

## CreateResponse

<Badge>Class</Badge>

<Badge>Bases: BaseModel</Badge>

Response model for create

## Methods

### `class xdk.posts.models.CreateResponse`

Response model for create

### `class xdk.posts.models.DeleteResponse`

Response model for delete

### `class xdk.posts.models.GetAnalyticsResponse`

Response model for get\_analytics

### `class xdk.posts.models.GetByIdResponse`

Response model for get\_by\_id

### `class xdk.posts.models.GetByIdsResponse`

Response model for get\_by\_ids

### `class xdk.posts.models.GetCountsAllResponse`

Response model for get\_counts\_all

### `class xdk.posts.models.GetCountsRecentResponse`

Response model for get\_counts\_recent

### `class xdk.posts.models.GetInsights28hrResponse`

Response model for get\_insights28hr

### `class xdk.posts.models.GetInsightsHistoricalResponse`

Response model for get\_insights\_historical

### `class xdk.posts.models.GetLikingUsersResponse`

Response model for get\_liking\_users

### `class xdk.posts.models.GetQuotedResponse`

Response model for get\_quoted

### `class xdk.posts.models.GetRepostedByResponse`

Response model for get\_reposted\_by

### `class xdk.posts.models.GetRepostsResponse`

Response model for get\_reposts

### `class xdk.posts.models.HideReplyResponse`

Response model for hide\_reply

### `class xdk.posts.models.SearchAllResponse`

Response model for search\_all

### `class xdk.posts.models.SearchRecentResponse`

Response model for search\_recent
