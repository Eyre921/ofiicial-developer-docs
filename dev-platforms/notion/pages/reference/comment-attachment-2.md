---
title: "Comment attachment"
source: https://developers.notion.com/reference/comment-attachment
path: reference/comment-attachment
---

The Comment Attachment object represents [files](/reference/file-object) that have been attached to a [Comment](/reference/comment-object).

<Note>
  Comments can currently support up to 3 attachments.
</Note>

## Request format (input)

### Object properties

After following the [Working with files and media](/guides/data-apis/working-with-files-and-media) guide, provide an array of objects under the `attachments` parameter in the [Create comment](/reference/create-a-comment) API, each containing the following properties:

| Parameter        | Type                | Description                                                                 | Example value                            |
| :--------------- | :------------------ | :-------------------------------------------------------------------------- | :--------------------------------------- |
| `file_upload_id` | `string` (UUID)     | ID of a [File Upload](/reference/file-upload) with a status of `"uploaded"` | `"2e2cdb8b-9897-4a6c-a935-82922b1cfb87"` |
| `type`           | `string` (optional) | Possible type values are:`"file_upload"`                                    | `"file_upload"`                          |

Example Create Comment request:

<CodeGroup>
  ```json API request theme={null}
  {
    "parent": {
      "page_id": "d0a1ffaf-a4d8-4acf-a1ed-abae6e110418"
    },
    "rich_text": [
      {
        "text": {"content": "Thanks for the helpful page!"}
      },
    ],
    "attachments": {
      "file_upload_id": "2e2cdb8b-9897-4a6c-a935-82922b1cfb87"
    }
  }
  ```
</CodeGroup>

In the Notion app, when viewing a comment uploaded using the API, the user experience is automatically customized based on the detected category of the file upload. For example, uploading a `.png` file displays your attachment as an inline image instead of a regular file download block.

## Response format (output)

### Object properties

The response of Comment APIs like [Create comment](/reference/create-a-comment) contains `attachments` with the following fields:

| Field      | Type            | Description                                                                                                               | Example value                                                                                    |
| :--------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------- |
| `category` | `string` (enum) | The category of this attachment. Possible type values are: `"audio"`, `"image"`, `"pdf"`, `"productivity"`, and `"video"` | `"audio"`                                                                                        |
| `file`     | `object`        | A [file object](/reference/file-object#notion-hosted-files-type-file) containing type-specific configuration.             | `{"url": "<https://s3.us-west-2.amazonaws.com/...">, "expiry_time": "2025-06-10T21:26:03.070Z"}` |

Example attachment object in Create Comment response:

<CodeGroup>
  ```json Comment Attachment Response theme={null}
  {
    "category": "video",
    "file": {
      "url": "https://s3.us-west-2.amazonaws.com/...",
      "expiry_time": "2025-06-10T21:26:03.070Z"
    }
  }
  ```
</CodeGroup>

The `file.url` is a temporary download link generated at the time of retrieving a comment. See the guide on [Retrieving existing files](/guides/data-apis/retrieving-files) to learn more about accessing the files you upload.
