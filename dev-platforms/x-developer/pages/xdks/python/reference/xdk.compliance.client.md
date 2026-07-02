---
title: "ComplianceClient"
source: https://docs.x.com/xdks/python/reference/xdk.compliance.client
path: xdks/python/reference/xdk.compliance.client
---

Reference for the compliance.client Python module in the X API SDK. Client class and methods for calling the compliance endpoints of the X API v2.

## ComplianceClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for compliance operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `create_jobs`

Create Compliance Job
Creates a new Compliance Job for the specified job type.
body: Request body
:returns: Response data
:rtype: CreateJobsResponse

#### Parameters

<ParamField type="CreateJobsRequest" />

### `get_jobs`

Get Compliance Jobs
Retrieves a list of Compliance Jobs filtered by job type and optional status.

#### Parameters

<ParamField type="str">
  Type of Compliance Job to list.
</ParamField>

<ParamField type="str or None">
  Status of Compliance Job to list.
</ParamField>

<ParamField type="List or None">
  A comma separated list of ComplianceJob fields to display.
</ParamField>

#### Returns

`GetJobsResponse` - Response data

### `get_jobs_by_id`

Get Compliance Job by ID
Retrieves details of a specific Compliance Job by its ID.

#### Parameters

<ParamField type="Any">
  The ID of the Compliance Job to retrieve.
</ParamField>

<ParamField type="List or None">
  A comma separated list of ComplianceJob fields to display.
</ParamField>

#### Returns

`GetJobsByIdResponse` - Response data
