---
title: "Create a file upload"
source: https://developers.notion.com/reference/create-file
path: reference/create-file
---

post /v1/file_uploads
Use this API to initiate the process of [uploading a file](/guides/data-apis/working-with-files-and-media) to your Notion workspace.

For a successful request, the response is a [File Upload](/reference/file-upload) object with a `status` of `"pending"`.

If you pass `application/octet-stream` as the `content_type` along with a `filename`, the API treats the content type as unspecified and resolves it from the filename extension instead. The same applies to the `Content-Type` header returned by an `external_url`. The request fails if the extension isn't a [supported file type](/guides/data-apis/working-with-files-and-media#supported-file-types).

The maximum allowed length of `filename` string is 900 bytes, including any file extension included in the file name or inferred based on the `content_type`. However, we recommend using shorter names for performance and easier file management and lookup using the [List file uploads](/reference/list-file-uploads) API.
