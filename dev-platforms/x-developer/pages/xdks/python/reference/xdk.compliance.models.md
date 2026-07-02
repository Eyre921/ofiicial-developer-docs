---
title: "Compliance.Models"
source: https://docs.x.com/xdks/python/reference/xdk.compliance.models
path: xdks/python/reference/xdk.compliance.models
---

Reference for the compliance.models Python module in the X API SDK. Pydantic request and response models for the compliance endpoints of the X API v2.

This module provides Pydantic models for request and response data structures
for the compliance endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

### class xdk.compliance.models.CreateJobsRequest

Request model for create\_jobs

<ResponseField name="model_config" type="ConfigDict">
  Default: `{'populate_by_name': True, 'validate_by_alias': True, 'validate_by_name': True}`

  Configuration for the model, should be a dictionary conforming to \[ConfigDict]\[pydantic.config.ConfigDict].
</ResponseField>

## CreateJobsResponse

<Badge>Class</Badge>

<Badge>Bases: BaseModel</Badge>

Response model for create\_jobs

## Methods

### `class xdk.compliance.models.CreateJobsResponse`

Response model for create\_jobs

### `class xdk.compliance.models.GetJobsByIdResponse`

Response model for get\_jobs\_by\_id

### `class xdk.compliance.models.GetJobsResponse`

Response model for get\_jobs
