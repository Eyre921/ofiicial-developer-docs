---
title: "Lists.Models"
source: https://docs.x.com/xdks/python/reference/xdk.lists.models
path: xdks/python/reference/xdk.lists.models
---

Reference for the lists.models Python module in the X API SDK. Pydantic request and response models for the lists endpoints of the X API v2.

This module provides Pydantic models for request and response data structures
for the lists endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

### class xdk.lists.models.AddMemberRequest

Request model for add\_member

<ResponseField name="model_config" type="ConfigDict">
  Default: `{'populate_by_name': True, 'validate_by_alias': True, 'validate_by_name': True}`

  Configuration for the model, should be a dictionary conforming to \[ConfigDict]\[pydantic.config.ConfigDict].
</ResponseField>

## AddMemberResponse

<Badge>Class</Badge>

<Badge>Bases: BaseModel</Badge>

Response model for add\_member

## Methods

### `class xdk.lists.models.AddMemberResponse`

Response model for add\_member

### `class xdk.lists.models.CreateResponse`

Response model for create

### `class xdk.lists.models.DeleteResponse`

Response model for delete

### `class xdk.lists.models.GetByIdResponse`

Response model for get\_by\_id

### `class xdk.lists.models.GetFollowersResponse`

Response model for get\_followers

### `class xdk.lists.models.GetMembersResponse`

Response model for get\_members

### `class xdk.lists.models.GetPostsResponse`

Response model for get\_posts

### `class xdk.lists.models.RemoveMemberByUserIdResponse`

Response model for remove\_member\_by\_user\_id

### `class xdk.lists.models.UpdateResponse`

Response model for update
