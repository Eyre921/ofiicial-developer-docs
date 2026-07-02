---
title: "MediaClient"
source: https://docs.x.com/xdks/python/reference/xdk.media.client
path: xdks/python/reference/xdk.media.client
---

Reference for the media.client Python module in the X API SDK. Client class and methods for calling the media endpoints of the X API v2.

## MediaClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for media operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `append_upload`

Append Media upload
Appends data to a Media upload request.

#### Parameters

<ParamField type="Any">
  The media identifier for the media to perform the append operation.
</ParamField>

<ParamField type="AppendUploadRequest">
  Request body
</ParamField>

### `create_metadata`

Create Media metadata
Creates metadata for a Media file.
body: Request body
:returns: Response data
:rtype: CreateMetadataResponse

#### Parameters

<ParamField type="CreateMetadataRequest" />

### `create_subtitles`

Create Media subtitles
Creates subtitles for a specific Media file.
body: Request body
:returns: Response data
:rtype: CreateSubtitlesResponse

#### Parameters

<ParamField type="CreateSubtitlesRequest" />

### `delete_subtitles`

Delete Media subtitles
Deletes subtitles for a specific Media file.
body: Request body
:returns: Response data
:rtype: DeleteSubtitlesResponse

#### Parameters

<ParamField type="DeleteSubtitlesRequest" />

### `finalize_upload`

Finalize Media upload
Finalizes a Media upload request.

#### Parameters

<ParamField type="Any">
  The media id of the targeted media to finalize.
</ParamField>

#### Returns

`FinalizeUploadResponse` - Response data

### `get_analytics`

Get Media analytics
Retrieves analytics data for media.

#### Parameters

<ParamField type="List">
  A comma separated list of Media Keys. Up to 100 are allowed in a single request.
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
  A comma separated list of MediaAnalytics fields to display.
</ParamField>

#### Returns

`GetAnalyticsResponse` - Response data

### `get_by_key`

Get Media by media key
Retrieves details of a specific Media file by its media key.

#### Parameters

<ParamField type="Any">
  A single Media Key.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

#### Returns

`GetByKeyResponse` - Response data

### `get_by_keys`

Get Media by media keys
Retrieves details of Media files by their media keys.

#### Parameters

<ParamField type="List">
  A comma separated list of Media Keys. Up to 100 are allowed in a single request.
</ParamField>

<ParamField type="List or None">
  A comma separated list of Media fields to display.
</ParamField>

#### Returns

`GetByKeysResponse` - Response data

### `get_upload_status`

Get Media upload status
Retrieves the status of a Media upload by its ID.

#### Parameters

<ParamField type="Any">
  Media id for the requested media upload status.
</ParamField>

<ParamField type="str or None">
  The command for the media upload request.
</ParamField>

#### Returns

`GetUploadStatusResponse` - Response data

### `initialize_upload`

Initialize media upload
Initializes a media upload.
body: Request body
:returns: Response data
:rtype: InitializeUploadResponse

#### Parameters

<ParamField type="InitializeUploadRequest" />

### `upload`

Upload media
Uploads a media file for use in posts or other content.
body: Request body
:returns: Response data
:rtype: UploadResponse

#### Parameters

<ParamField type="UploadRequest" />
