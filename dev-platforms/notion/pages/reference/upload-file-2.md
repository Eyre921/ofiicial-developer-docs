---
title: "Send a file upload"
source: https://developers.notion.com/reference/upload-file
path: reference/upload-file
---

post /v1/file_uploads/{file_upload_id}/send
Use this API to transmit file contents to Notion for a [file upload](/reference/file-upload).

For this endpoint, use a `Content-Type` of `multipart/form-data`, and provide your file contents under the `file` key.

<Info>
  The use of multipart form data is unique to this endpoint. Other Notion APIs, including [Create a file upload](/reference/create-file) and [Complete a file upload](/reference/complete-file-upload), use JSON parameters.

  Include a `boundary` with the `Content-Type` header of your request as per [RFC 2388](https://datatracker.ietf.org/doc/html/rfc2388). Most request libraries (e.g. `fetch`, `ky`) automatically handle this as long as you provide a form data object but don't overwrite the `Content-Type` explicitly.

  For more tips and examples, view the [file upload guide](/guides/data-apis/uploading-small-files#step-2-upload-file-contents).
</Info>

When `mode=multi_part`, each part must include a form field `part_number` to indicate which part is being sent. Parts may be sent concurrently up to standard Notion API [rate limits](/reference/request-limits), and may be sent out of order as long as all parts (1, ..., `part_number`) are successfully sent before calling the [complete file upload API](/reference/complete-file-upload).

The maximum allowed length of a file name is 900 bytes, including any file extension included in the file name or inferred based on the `content_type`. However, we recommend using shorter names for performance and easier file management and lookup using the [List file uploads](/reference/list-file-uploads) API.
