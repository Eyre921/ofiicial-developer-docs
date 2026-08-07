---
title: "Update document file"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/update-file.md
path: docs/eleven-agents/api-reference/knowledge-base/update-file
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update document file

PATCH https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/update-file
Content-Type: multipart/form-data

Update the source file of a file document. The document name, content, and metadata are updated to reflect the new file. Any manual content edits will be overwritten.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/update-file

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.

### Body (multipart/form-data)

- `file` (file, required) — Documentation that the agent will have access to in order to interact with users.

## Response

### 200

Successful Response

- `object`
  - `type`: `url`
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
        - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
    - `extracted_inner_html` (string, required)
    - `id` (string, required)
    - `metadata` (object, required)
      - `created_at_unix_secs` (integer, required)
      - `last_updated_at_unix_secs` (integer, required)
      - `size_bytes` (integer, required)
    - `name` (string, required)
    - `supported_usages` (list of enum, required)
      - Allowed values: `prompt`, `auto`
    - `url` (string, required)
    - `auto_sync_info` (object, optional)
      - `minimum_frequency_days` (integer, optional, default: 7) — Maximum number of days between automatic syncs
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional) — Unix timestamp for the next scheduled sync or None (in case of folders)
    - `content_format` (enum, optional, default: html) — Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML.
      - Allowed values: `html`, `markdown`
    - `folder_parent_id` (string, optional) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, optional)
  - `type`: `file`
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
        - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
    - `extracted_inner_html` (string, required)
    - `filename` (string, required)
    - `id` (string, required)
    - `metadata` (object, required)
      - `created_at_unix_secs` (integer, required)
      - `last_updated_at_unix_secs` (integer, required)
      - `size_bytes` (integer, required)
    - `name` (string, required)
    - `supported_usages` (list of enum, required)
      - Allowed values: `prompt`, `auto`
    - `auto_sync_info` (object, optional)
      - `minimum_frequency_days` (integer, optional, default: 7) — Maximum number of days between automatic syncs
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional) — Unix timestamp for the next scheduled sync or None (in case of folders)
    - `content_format` (enum, optional, default: html) — Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML.
      - Allowed values: `html`, `markdown`
    - `external_sync_info` (object, optional) — Tracks the link back to the original file in an external source.
      - `type` ("google_drive", required) — Provider identifier
      - `source_entity_id` (string, required) — Entity ID in the external system
      - `integration_connection_id` (string, required) — Integration connection instance ID
      - `source_parent_entity_id` (string, required) — Folder ID in the external system this file was synced from
      - `source_mime_type` (string, required) — Original MIME type in the external system
      - `source_modified_time` (datetime, required) — Last modified time from the external system
      - `root_folder_id` (string, optional) — KB folder ID of the sync root, used to query all entities under a sync tree
    - `folder_parent_id` (string, optional) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, optional)
    - `is_frozen` (boolean, optional, default: false)
    - `refresh_status` (object, optional) — In-flight or last refresh state for an externally-synced file. Used by clients to render sync progress and disable re-sync while a refresh is queued or processing.
      - `status` (enum, optional, default: queued)
        - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
      - `enqueued_at` (integer, optional)
      - `started_at` (integer, optional)
      - `completed_at` (integer, optional)
      - `last_synced_at` (integer, optional)
      - `error_message` (string, optional)
  - `type`: `text`
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
        - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
    - `extracted_inner_html` (string, required)
    - `id` (string, required)
    - `metadata` (object, required)
      - `created_at_unix_secs` (integer, required)
      - `last_updated_at_unix_secs` (integer, required)
      - `size_bytes` (integer, required)
    - `name` (string, required)
    - `supported_usages` (list of enum, required)
      - Allowed values: `prompt`, `auto`
    - `content_format` (enum, optional, default: html) — Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML.
      - Allowed values: `html`, `markdown`
    - `folder_parent_id` (string, optional) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, optional)
  - `type`: `folder`
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
        - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
    - `children_count` (integer, required)
    - `document_count` (integer, required) — Number of non-folder documents anywhere in this folder's subtree (recursive). Counting stops past 1000;
    - `id` (string, required)
    - `metadata` (object, required)
      - `created_at_unix_secs` (integer, required)
      - `last_updated_at_unix_secs` (integer, required)
      - `size_bytes` (integer, required)
    - `name` (string, required)
    - `supported_usages` (list of enum, required)
      - Allowed values: `prompt`, `auto`
    - `active_sync_job` (object, optional) — Most recent (in-flight or terminal) external sync job for this folder, if any. Used by clients to render sync progress.
      - `type` ("google_drive", required)
      - `folder_id` (string, required)
      - `integration_connection_id` (string, required)
      - `triggered_by` (enum, required)
        - Allowed values: `on_demand`, `on_connect`, `auto`
      - `updated_at` (integer, required)
      - `id` (string, required)
      - `created_at` (integer, required)
      - `status` (enum, optional, default: queued)
        - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
      - `sync_type` (enum, optional)
        - Allowed values: `full`, `incremental`
      - `items_identified` (integer, optional, default: 0)
      - `items_processed` (integer, optional, default: 0)
      - `error_message` (string, optional)
      - `started_at` (integer, optional)
      - `completed_at` (integer, optional)
    - `auto_sync_info` (object, optional)
      - `minimum_frequency_days` (integer, optional, default: 7) — Maximum number of days between automatic syncs
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional) — Unix timestamp for the next scheduled sync or None (in case of folders)
    - `external_sync_info` (object, optional) — Metadata for a KB folder that mirrors an external source folder.
      - `type` ("google_drive", required) — Provider identifier
      - `source_entity_id` (string, required) — Entity ID in the external system
      - `integration_connection_id` (string, required) — Integration connection instance ID
      - `root_folder_id` (string, optional) — KB folder ID of the sync root. None means this folder is the root.
      - `sync_cursor` (string, optional) — Opaque cursor for incremental sync, interpreted by the provider
      - `last_sync_at` (integer, optional) — Unix timestamp of last completed sync
    - `folder_parent_id` (string, optional) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, optional)
    - `is_frozen` (boolean, optional, default: false)

## Examples

**Request**

```json
{
  "file": "<file: U29tZSBleGFtcGxlIGJpbmFyeSBkYXRhIGZvciB0aGUgZG9jdW1lbnQgc2VydmljZQ==>"
}
```

**Response**

```json
{
  "type": "url",
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "anonymous_access_level_override": "viewer",
    "access_source": "creator"
  },
  "extracted_inner_html": "<p>Welcome to the Q2 2024 product documentation. This document covers all updates and features released in this quarter.</p>",
  "id": "21m00Tcm4TlvDq8ikWAM",
  "metadata": {
    "created_at_unix_secs": 1685600000,
    "last_updated_at_unix_secs": 1688201600,
    "size_bytes": 2540000
  },
  "name": "Product Documentation Q2 2024",
  "supported_usages": [
    "prompt"
  ],
  "url": "https://docs.company.com/product-q2-2024.pdf",
  "auto_sync_info": {
    "minimum_frequency_days": 7,
    "auto_remove": false,
    "consec_failures": 0,
    "next_refresh_by": 1688806400
  },
  "content_format": "html",
  "folder_parent_id": "folder_9X7b2LkPq3",
  "folder_path": [
    {
      "id": "folder_root",
      "name": "Company Knowledge Base"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.document.updateFile("21m00Tcm4TlvDq8ikWAM", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.document.update_file(
    documentation_id="21m00Tcm4TlvDq8ikWAM",
    file="example_file",
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/update-file"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"U29tZSBleGFtcGxlIGJpbmFyeSBkYXRhIGZvciB0aGUgZG9jdW1lbnQgc2VydmljZQ==\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/update-file")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"U29tZSBleGFtcGxlIGJpbmFyeSBkYXRhIGZvciB0aGUgZG9jdW1lbnQgc2VydmljZQ==\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/update-file")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"U29tZSBleGFtcGxlIGJpbmFyeSBkYXRhIGZvciB0aGUgZG9jdW1lbnQgc2VydmljZQ==\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/update-file', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => 'U29tZSBleGFtcGxlIGJpbmFyeSBkYXRhIGZvciB0aGUgZG9jdW1lbnQgc2VydmljZQ==',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/update-file");
var request = new RestRequest(Method.PATCH);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"U29tZSBleGFtcGxlIGJpbmFyeSBkYXRhIGZvciB0aGUgZG9jdW1lbnQgc2VydmljZQ==\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "file",
    "fileName": "U29tZSBleGFtcGxlIGJpbmFyeSBkYXRhIGZvciB0aGUgZG9jdW1lbnQgc2VydmljZQ=="
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/update-file")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
