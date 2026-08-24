---
title: "Search knowledge base"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/search.md
path: docs/eleven-agents/api-reference/knowledge-base/search
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Search knowledge base

GET https://api.elevenlabs.io/v1/convai/knowledge-base/search

Fuzzy text search over knowledge base document content

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/search

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `query` (string, required) — The search query text
- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `types` (enum, optional) — If present, the endpoint will return only documents of the given types.
  - Allowed values: `file`, `url`, `text`, `folder`
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `results` (list of object, required)
  - `document` (object, required)
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
      - `id` (string, required)
      - `metadata` (object, required)
        - `created_at_unix_secs` (integer, required)
        - `last_updated_at_unix_secs` (integer, required)
        - `size_bytes` (integer, required)
      - `name` (string, required)
      - `supported_usages` (list of enum, required)
        - Allowed values: `prompt`, `auto`
      - `dependent_agents` (list of object, required, deprecated) — This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
        - `type`: `available`
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
        - `type`: `unknown`
          - `id` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `auto_sync_info` (object, optional)
        - `minimum_frequency_days` (integer, optional, default: 7) — Minimum frequency (in days) at which the document is refreshed. The actual interval may be shorter, never longer.
        - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
        - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
        - `next_refresh_by` (integer, optional) — Unix timestamp for the next scheduled sync or None (in case of folders)
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
      - `is_frozen` (boolean, optional, default: false)
      - `refresh_status` (object, optional) — In-flight/last refresh state for an externally-synced KB file.
        - `status` (enum, optional, default: queued)
          - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
        - `enqueued_at` (integer, optional)
        - `started_at` (integer, optional)
        - `completed_at` (integer, optional)
        - `last_synced_at` (integer, optional)
        - `error_message` (string, optional)
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
      - `dependent_agents` (list of object, required, deprecated) — This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
        - `type`: `available`
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
        - `type`: `unknown`
          - `id` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `auto_sync_info` (object, optional)
        - `minimum_frequency_days` (integer, optional, default: 7) — Minimum frequency (in days) at which the document is refreshed. The actual interval may be shorter, never longer.
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
      - `is_frozen` (boolean, optional, default: false)
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
      - `id` (string, required)
      - `metadata` (object, required)
        - `created_at_unix_secs` (integer, required)
        - `last_updated_at_unix_secs` (integer, required)
        - `size_bytes` (integer, required)
      - `name` (string, required)
      - `supported_usages` (list of enum, required)
        - Allowed values: `prompt`, `auto`
      - `dependent_agents` (list of object, required, deprecated) — This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
        - `type`: `available`
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
        - `type`: `unknown`
          - `id` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `folder_parent_id` (string, optional) — The ID of the parent folder, or null if the document is at the root level.
      - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
        - `id` (string, required)
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
      - `id` (string, required)
      - `metadata` (object, required)
        - `created_at_unix_secs` (integer, required)
        - `last_updated_at_unix_secs` (integer, required)
        - `size_bytes` (integer, required)
      - `name` (string, required)
      - `supported_usages` (list of enum, required)
        - Allowed values: `prompt`, `auto`
      - `url` (string, required)
      - `dependent_agents` (list of object, required, deprecated) — This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
        - `type`: `available`
          - `access_level` (enum, required)
            - Allowed values: `admin`, `editor`, `commenter`, `viewer`
          - `created_at_unix_secs` (integer, required)
          - `id` (string, required)
          - `name` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
        - `type`: `unknown`
          - `id` (string, required)
          - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `auto_sync_info` (object, optional)
        - `minimum_frequency_days` (integer, optional, default: 7) — Minimum frequency (in days) at which the document is refreshed. The actual interval may be shorter, never longer.
        - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
        - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
        - `next_refresh_by` (integer, optional) — Unix timestamp for the next scheduled sync or None (in case of folders)
      - `folder_parent_id` (string, optional) — The ID of the parent folder, or null if the document is at the root level.
      - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
        - `id` (string, required)
  - `score` (double, required)
  - `search_snippet` (list of object, optional)
    - `value` (string, required)
    - `is_hit` (boolean, required)
- `next_cursor` (string, optional)

## Examples

**Response**

```json
{
  "results": [
    {
      "document": {
        "type": "file",
        "access_info": {
          "is_creator": true,
          "creator_name": "John Doe",
          "creator_email": "john.doe@example.com",
          "role": "admin",
          "access_source": "creator"
        },
        "id": "id",
        "metadata": {
          "created_at_unix_secs": 1,
          "last_updated_at_unix_secs": 1,
          "size_bytes": 1
        },
        "name": "name",
        "supported_usages": [
          "prompt"
        ],
        "dependent_agents": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1,
            "id": "id",
            "name": "name"
          }
        ]
      },
      "score": 1.1,
      "search_snippet": [
        {
          "value": "value",
          "is_hit": true
        }
      ]
    }
  ],
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.search({
        cursor: "cursor",
        pageSize: 1,
        query: "query",
        types: [
            "file",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.search(
    cursor="cursor",
    page_size=1,
    query="query",
    types=[
        "file"
    ],
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/search?cursor=cursor&page_size=1&query=query&types=%5B%22file%22%5D"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/search?cursor=cursor&page_size=1&query=query&types=%5B%22file%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/search?cursor=cursor&page_size=1&query=query&types=%5B%22file%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/search?cursor=cursor&page_size=1&query=query&types=%5B%22file%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/search?cursor=cursor&page_size=1&query=query&types=%5B%22file%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/search?cursor=cursor&page_size=1&query=query&types=%5B%22file%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
