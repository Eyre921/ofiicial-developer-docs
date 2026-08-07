---
title: "Update knowledge base document"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/update.md
path: docs/api-reference/knowledge-base/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update knowledge base document

PATCH https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}
Content-Type: application/json

Update the name and/or content of a document.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.

### Body (application/json)

- `name` (string, optional, nullable) — A custom, human-readable name for the document.
- `content` (string, optional, nullable) — Updated content for the document. Only supported for text documents, URL documents with auto-sync disabled, and file documents.

## Response

### 200

Successful Response

- `object`
  - `type`: `url` (GetKnowledgeBaseURLResponseModel)
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
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
    - `auto_sync_info` (object, optional, nullable)
      - `minimum_frequency_days` (integer, optional, default: 7) — Maximum number of days between automatic syncs
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional, nullable) — Unix timestamp for the next scheduled sync or None (in case of folders)
    - `content_format` (enum, optional, default: html) — Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML.
      - Allowed values: `html`, `markdown`
    - `folder_parent_id` (string, optional, nullable) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, required, nullable)
  - `type`: `file` (GetKnowledgeBaseFileResponseModel)
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
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
    - `auto_sync_info` (object, optional, nullable)
      - `minimum_frequency_days` (integer, optional, default: 7) — Maximum number of days between automatic syncs
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional, nullable) — Unix timestamp for the next scheduled sync or None (in case of folders)
    - `content_format` (enum, optional, default: html) — Canonical representation of a knowledge base document's stored content. HTML is the legacy default; documents created before this field existed are interpreted as HTML.
      - Allowed values: `html`, `markdown`
    - `external_sync_info` (object, optional, nullable) — Tracks the link back to the original file in an external source.
      - `type` (enum, required) — Provider identifier
        - Allowed values: `google_drive`
      - `source_entity_id` (string, required) — Entity ID in the external system
      - `integration_connection_id` (string, required) — Integration connection instance ID
      - `source_parent_entity_id` (string, required) — Folder ID in the external system this file was synced from
      - `source_mime_type` (string, required) — Original MIME type in the external system
      - `source_modified_time` (string, required) — Last modified time from the external system
      - `root_folder_id` (string, optional, nullable) — KB folder ID of the sync root, used to query all entities under a sync tree
    - `folder_parent_id` (string, optional, nullable) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, required, nullable)
    - `is_frozen` (boolean, optional, default: false)
    - `refresh_status` (object, optional, nullable) — In-flight or last refresh state for an externally-synced file. Used by clients to render sync progress and disable re-sync while a refresh is queued or processing.
      - `status` (enum, optional, default: queued)
        - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
      - `enqueued_at` (integer, optional, nullable)
      - `started_at` (integer, optional, nullable)
      - `completed_at` (integer, optional, nullable)
      - `last_synced_at` (integer, optional, nullable)
      - `error_message` (string, optional, nullable)
  - `type`: `text` (GetKnowledgeBaseTextResponseModel)
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
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
    - `folder_parent_id` (string, optional, nullable) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, required, nullable)
  - `type`: `folder` (GetKnowledgeBaseFolderResponseModel)
    - `access_info` (object, required)
      - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
      - `creator_name` (string, required) — Name of the agent's creator
      - `creator_email` (string, required) — Email of the agent's creator
      - `role` (enum, required) — The role of the user making the request
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
        - Allowed values: `admin`, `editor`, `commenter`, `viewer`
      - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
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
    - `active_sync_job` (object, optional, nullable) — Most recent (in-flight or terminal) external sync job for this folder, if any. Used by clients to render sync progress.
      - `type` (enum, required)
        - Allowed values: `google_drive`
      - `folder_id` (string, required)
      - `integration_connection_id` (string, required)
      - `triggered_by` (enum, required)
        - Allowed values: `on_demand`, `on_connect`, `auto`
      - `updated_at` (integer, required)
      - `id` (string, required)
      - `created_at` (integer, required)
      - `status` (enum, optional, default: queued)
        - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
      - `sync_type` (enum, optional, nullable)
        - Allowed values: `full`, `incremental`
      - `items_identified` (integer, optional, default: 0)
      - `items_processed` (integer, optional, default: 0)
      - `error_message` (string, optional, nullable)
      - `started_at` (integer, optional, nullable)
      - `completed_at` (integer, optional, nullable)
    - `auto_sync_info` (object, optional, nullable)
      - `minimum_frequency_days` (integer, optional, default: 7) — Maximum number of days between automatic syncs
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional, nullable) — Unix timestamp for the next scheduled sync or None (in case of folders)
    - `external_sync_info` (object, optional, nullable) — Metadata for a KB folder that mirrors an external source folder.
      - `type` (enum, required) — Provider identifier
        - Allowed values: `google_drive`
      - `source_entity_id` (string, required) — Entity ID in the external system
      - `integration_connection_id` (string, required) — Integration connection instance ID
      - `root_folder_id` (string, optional, nullable) — KB folder ID of the sync root. None means this folder is the root.
      - `sync_cursor` (string, optional, nullable) — Opaque cursor for incremental sync, interpreted by the provider
      - `last_sync_at` (integer, optional, nullable) — Unix timestamp of last completed sync
    - `folder_parent_id` (string, optional, nullable) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
      - `name` (string, required, nullable)
    - `is_frozen` (boolean, optional, default: false)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "access_info": {
    "access_source": "creator",
    "creator_email": "john.doe@example.com",
    "creator_name": "John Doe",
    "is_creator": true,
    "role": "admin"
  },
  "auto_sync_info": {
    "auto_remove": false,
    "consec_failures": 0,
    "minimum_frequency_days": 7,
    "next_refresh_by": 1
  },
  "content_format": "html",
  "extracted_inner_html": "string",
  "folder_parent_id": "string",
  "folder_path": [
    {
      "id": "string",
      "name": "string"
    }
  ],
  "id": "string",
  "metadata": {
    "created_at_unix_secs": 1,
    "last_updated_at_unix_secs": 1,
    "size_bytes": 1
  },
  "name": "string",
  "supported_usages": [
    "auto"
  ],
  "type": "string",
  "url": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.update("documentation_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.update(
    documentation_id="documentation_id",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Content-Type", "application/json")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id")! as URL,
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
