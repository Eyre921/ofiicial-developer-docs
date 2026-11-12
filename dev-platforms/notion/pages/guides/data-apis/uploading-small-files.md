---
title: "Uploading small files"
source: https://developers.notion.com/guides/data-apis/uploading-small-files
path: guides/data-apis/uploading-small-files
---

Learn how to send and attach files up to 20 MB using the Notion API.

The **Direct Upload** method lets you securely upload private files to Notion-managed storage via the API. Once uploaded, these files can be reused and attached to pages, blocks, or database properties.

This guide walks you through the upload lifecycle:

**Step 1**

Create a file upload object

**Step 2**

Send the file content to Notion

**Step 3**

Attach the file to content in your workspace

> [!TIP]
>
> **Tip**:
>
> Upload once, attach many times. You can reuse the same `file_upload` ID across multiple blocks or pages.

## Before you begin

You need an integration token. Creating and sending a file upload needs either the **Insert content** or the **Update content** capability. Adding a block needs **Insert content**, setting a page cover or `files` property needs **Update content**, and checking the result needs **Read content**. Keep the token on your server. Don’t put it in browser page source, client bundles, or public repositories.

The examples upload a PNG image named `logo.png` from your working directory. They read your token and the ID of an existing page that’s shared with the integration from your shell:

```bash theme={null}
export NOTION_TOKEN="ntn_..."
export NOTION_PAGE_ID="your-page-id"
```

The Python examples run in order as one script and use the [`requests`](https://pypi.org/project/requests/) package. The JavaScript example needs Node.js 20 or later and no extra packages. Save it as an `.mjs` file.

## Step 1 - Create a File Upload object

Before uploading any content, start by creating a [File Upload object](/reference/file-upload). This returns a unique `id` and `upload_url` used to send the file.

> [!TIP]
>
> **Tip:**
>
> Save the `id` — You’ll need it to upload the file in Step 2 and attach it in Step 3.

### Example requests

This snippet sends a `POST` request to create the upload object.

```curl cURL theme={null}
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads' \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2026-03-11' \
  --data '{}'
```

```python Python theme={null}
import json
import os

import requests

NOTION_KEY = os.environ["NOTION_TOKEN"]

file_create_response = requests.post("https://api.notion.com/v1/file_uploads", json={}, headers={
    "Authorization": f"Bearer {NOTION_KEY}",
    "accept": "application/json",
    "content-type": "application/json",
    "Notion-Version": "2026-03-11"
})

if file_create_response.status_code != 200:
    raise Exception(
        f"File creation failed with status code {file_create_response.status_code}: {file_create_response.text}"
    )

file_upload_id = json.loads(file_create_response.text)['id']
print(file_upload_id)
```

Save the `id` from the response, or the ID that the Python example prints, in your shell. The JavaScript and cURL examples read it from there:

```bash theme={null}
export FILE_UPLOAD_ID="id-from-the-response"
```

### Example Response

```json JSON theme={null}
{
  "object": "file_upload",
  "id": "a3f9d3e2-1abc-42de-b904-badc0ffee000",
  "created_time": "2025-04-09T22:26:00.000Z",
  "created_by": {
    "id": "c2f20311-9e54-4d11-8c79-7398424ae41e",
    "type": "bot"
  },
  "last_edited_time": "2025-04-09T22:26:00.000Z",
  "expiry_time": "2025-04-09T23:26:00.000Z",
  "upload_url": "https://api.notion.com/v1/file_uploads/a3f9d3e2-1abc-42de-b904-badc0ffee000/send",
  "in_trash": false,
  "status": "pending",
  "filename": null,
  "content_type": null,
  "content_length": null,
  "request_id": "b7c1fd7e-2c84-4f55-877e-d3ad7db2ac4b"
}
```

## Step 2 - Upload file contents

Next, use the `upload_url` or File Upload object `id` from Step 1 to send the binary file contents to Notion.

> [!TIP]
>
> **Tips**:
>
> * The only required field is the file contents under the `file` key.
> * Unlike other Notion APIs, the Send File Upload endpoint expects a Content-Type of multipart/form-data, not application/json.
> * Include a boundary in the `Content-Type` header \[for the Send File Upload API] as described in [RFC 2388](https://datatracker.ietf.org/doc/html/rfc2388) and [RFC 1341](https://www.w3.org/Protocols/rfc1341/7_2_Multipart.html). Most HTTP clients (e.g. `fetch`, `ky`) handle this automatically if you include `FormData` with your file and don't pass an explicit `Content-Type` header.

### Example requests

This uploads the file directly from your local system.

```bash cURL theme={null}
curl --request POST \
  --url "https://api.notion.com/v1/file_uploads/$FILE_UPLOAD_ID/send" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H 'Notion-Version: 2026-03-11' \
  -F "file=@logo.png;type=image/png"
```

```javascript JavaScript expandable theme={null}
import { readFile } from 'node:fs/promises'

const notionToken = process.env.NOTION_TOKEN
const fileUploadId = process.env.FILE_UPLOAD_ID
const notionVersion = '2026-03-11'

// Read the file into a Blob with its MIME type
const fileBlob = new Blob([await readFile('logo.png')], { type: 'image/png' })

// Create form data with the (named) file contents under the `file` key.
const form = new FormData()
form.append('file', fileBlob, 'logo.png')

// HTTP POST to the Send File Upload API.
const response = await fetch(
	`https://api.notion.com/v1/file_uploads/${fileUploadId}/send`,
	{
		method: 'POST',
		body: form,
		headers: {
			'Authorization': `Bearer ${notionToken}`,
			'Notion-Version': notionVersion,
		}
	}
)

// Rescue validation errors. Possible HTTP 400 cases include:
// - content length greater than the 20MB limit
// - FileUpload not in the `pending` status (e.g. `expired`)
// - invalid or unsupported file content type
if (!response.ok) {
	const errorBody = await response.text()
	console.log('Error response body:', errorBody)
	throw new Error(`HTTP error with status: ${response.status}`)
}

const data = await response.json()
// ...
```

```python Python expandable theme={null}
file_name = "logo.png"

with open(file_name, "rb") as f:
    # Provide the MIME content type of the file as the 3rd argument.
    files = {
        "file": (file_name, f, "image/png")
    }

    response = requests.post(
        f"https://api.notion.com/v1/file_uploads/{file_upload_id}/send",
        headers={
            "Authorization": f"Bearer {NOTION_KEY}",
            "Notion-Version": "2026-03-11"
        },
        files=files
    )

    if response.status_code != 200:
        raise Exception(
            f"File upload failed with status code {response.status_code}: {response.text}")
```

### Example response

```json JSON theme={null}
{
  "object": "file_upload",
  "id": "a3f9d3e2-1abc-42de-b904-badc0ffee000",
  "created_time": "2025-04-09T22:26:00.000Z",
  "created_by": {
    "id": "c2f20311-9e54-4d11-8c79-7398424ae41e",
    "type": "bot"
  },
  "last_edited_time": "2025-04-09T22:27:00.000Z",
  "expiry_time": "2025-04-09T23:26:00.000Z",
  "in_trash": false,
  "status": "uploaded",
  "filename": "logo.png",
  "content_type": "image/png",
  "content_length": 4435,
  "request_id": "91a4ee8c-61f6-4c27-bd41-09aa35299929"
}
```

> [!NOTE]
>
> **Reminder:**
>
> Files must be attached within **1 hour** of creating the file upload or they’ll be automatically moved to an `expired` status.

## Step 3 - Attach the file to a page or block

Once the file’s `status` is `uploaded`, it can be attached to any location that supports file objects using the File Upload object `id`.

This step uses standard Notion API endpoints; there’s no special upload-specific API for attaching. Just pass a file object with a type of `file_upload` and include the `id` that you received earlier in Step 1.

You can use the file upload `id` with the following APIs:

**Step 1**

[Create a page](/reference/post-page)

* Attach files to a database property with the `files` type
* Include uploaded files in `children` blocks (e.g., file/image blocks inside a new page)

**Step 2**

[Update page](/reference/patch-page)

* Update existing `files` properties on a database page
* Set page `icon` or `cover`

**Step 3**

[Append block children](/reference/patch-block-children)

* Add a new block to a page — like a file, image, audio, video, or PDF block that uses an uploaded file

**Step 4**

[Update a block](/reference/update-a-block)

* Change the file attached to an existing file block (e.g., convert an image with an external URL to one that uses a file uploaded via the API)

### Example: add an image block to a page

This example uses the [Append block children](/reference/patch-block-children) API to create a new image block in a page and attach the uploaded file.

```bash cURL theme={null}
curl --request PATCH \
	--url "https://api.notion.com/v1/blocks/$NOTION_PAGE_ID/children" \
	-H "Authorization: Bearer $NOTION_TOKEN" \
	-H 'Content-Type: application/json' \
	-H 'Notion-Version: 2026-03-11' \
	--data '{
		"children": [
			{
				"type": "image",
				"image": {
					"caption": [],
					"type": "file_upload",
					"file_upload": {
						"id": "'"$FILE_UPLOAD_ID"'"
					}
				}
			}
		]
	}'
```

```python Python theme={null}
# Append image to desired block (this could be a page,
# or a block within a page)
append_block_id = os.environ["NOTION_PAGE_ID"]
url = f"https://api.notion.com/v1/blocks/{append_block_id}/children"

payload = {
    "children": [
        {
            "object": "block",
            "type": "image",
            "image": {
                "type": "file_upload",
                "file_upload": {
                    "id": file_upload_id
                }
            }
        }
    ]
}

response = requests.patch(url, headers={
    "Authorization": f"Bearer {NOTION_KEY}",
    "accept": "application/json",
    "content-type": "application/json",
    "Notion-Version": "2026-03-11"
}, data=json.dumps(payload))

if response.status_code != 200:
    raise Exception(
        f"Block append failed with status code {response.status_code}: {response.text}")

print(response.json()["results"][0]["id"])
```

### Example: add a file block to a page

example uses the [Append block children](/reference/patch-block-children) API to create a new file block in a page and attach the uploaded file.

```bash cURL expandable theme={null}
curl --request PATCH \
  --url "https://api.notion.com/v1/blocks/$NOTION_PAGE_ID/children" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2026-03-11' \
  --data '{
	  "children": [
		  {
			  "type": "file",
			  "file": {
				  "type": "file_upload",
				  "file_upload": {
					  "id": "'"$FILE_UPLOAD_ID"'"
				  }
			  }
		  }
	  ]
  }'
```

### Example: attach a file property to a page in a database

This example uses the [Update page](/reference/patch-page) API to add the uploaded file to a `files` property on a page that lives in a Notion database. Set `DATABASE_PAGE_ID` to a page in a database with a `files` property named `Attachments`.

```bash cURL expandable theme={null}
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$DATABASE_PAGE_ID" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2026-03-11' \
  --data '{
    "properties": {
      "Attachments": {
        "type": "files",
        "files": [
          {
            "type": "file_upload",
            "file_upload": { "id": "'"$FILE_UPLOAD_ID"'" },
            "name": "logo.png"
          }
        ]
      }
    }
  }'
```

### Example: Set a page cover

This example uses the [Update page](/reference/patch-page) API to add the uploaded file as a page cover.

```bash cURL theme={null}
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$NOTION_PAGE_ID" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2026-03-11' \
  --data '{
	  "cover": {
		  "type": "file_upload",
		  "file_upload": {
			  "id": "'"$FILE_UPLOAD_ID"'"
		  }
	  }
  }'
```

### Check the attachment

[Retrieve the file upload](/reference/retrieve-file-upload). After the first attachment, its `status` stays `uploaded` and its `expiry_time` is `null`.

```bash theme={null}
curl --url "https://api.notion.com/v1/file_uploads/$FILE_UPLOAD_ID" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H 'Notion-Version: 2026-03-11'
```

The append response lists the new block, and the Python example prints its ID. Save that `id` as `BLOCK_ID` and [retrieve the block](/reference/retrieve-a-block). An image block has an `image.type` of `file` and a temporary download URL in `image.file.url`.

```bash theme={null}
curl --url "https://api.notion.com/v1/blocks/$BLOCK_ID" \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H 'Notion-Version: 2026-03-11'
```

> [!TIP]
>
> **You’ve successfully uploaded and attached a file using Notion’s Direct Upload method.**

## File lifecycle and reuse

When a file is first uploaded, it has an `expiry_time`, one hour from the time of creation, during which it must be attached.

Once attached to any page, block, or database in your workspace:

* The `expiry_time` becomes `null`.
* The file becomes a permanent part of your workspace.
* The `status` remains `uploaded`.

Even if the original content is deleted, the `file_upload` ID remains valid and can be reused to attach the file again.

Currently, there is no way to delete or revoke a file upload after it has been created.

## Downloading an uploaded file

Attaching a file upload gives you access to a temporary download URL via the Notion API.

These URLs expire after 1 hour.

To refresh access, re-fetch the page, block, or database where the file is attached.

> [!TIP]
>
> **Tip:**
>
> A file becomes persistent and reusable after the first successful attachment — no need to re-upload.

## Tips and troubleshooting

* **URL expiration**: Notion-hosted files expire after 1 hour. Always re-fetch file objects to refresh links.
* **Attachment deadline**: Files must be attached within 1 hour of upload, or they’ll expire.
* **Size limit**: This guide only supports files up to 20 MB. Larger files require a [multi-part upload](/guides/data-apis/sending-larger-files).
* **Block type compatibility**: Files can be attached to image, file, video, audio, or pdf blocks — and to `files` properties on pages.

**What’s Next**

Now that you know how to upload a file, let’s walk through how to retrieve a file via the API:
