---
title: "List knowledge base documents"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/list.md
path: docs/api-reference/knowledge-base/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List knowledge base documents

GET https://api.elevenlabs.io/v1/convai/knowledge-base

Get a list of available knowledge base documents

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `search` (string, optional, nullable) — If specified, the endpoint returns only such knowledge base documents whose names start with this string.
- `show_only_owned_documents` (boolean, optional, default: false, deprecated) — If set to true, the endpoint will return only documents owned by you (and not shared from somebody else). Deprecated: use created_by_user_id instead.
- `created_by_user_id` (string, optional, nullable) — Filter documents by creator user ID. When set, only documents created by this user are returned. Takes precedence over show_only_owned_documents. Use '@me' to refer to the authenticated user.
- `types` (list of enum, optional, nullable) — If present, the endpoint will return only documents of the given types.
  - Allowed values: `file`, `url`, `text`, `folder`
- `parent_folder_id` (string, optional, nullable) — If set, the endpoint will return only documents that are direct children of the given folder.
- `ancestor_folder_id` (string, optional, nullable) — If set, the endpoint will return only documents that are descendants of the given folder.
- `folders_first` (boolean, optional, default: false) — Whether folders should be returned first in the list of documents.
- `sort_direction` (enum, optional) — The direction to sort the results
  - Allowed values: `asc`, `desc`
- `sort_by` (enum, optional, nullable) — The field to sort the results by
  - Allowed values: `name`, `created_at`, `updated_at`, `size`
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `documents` (list of object, required)
  - `type`: `file` (GetKnowledgeBaseSummaryFileResponseModel)
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
    - `id` (string, required)
    - `metadata` (object, required)
      - `created_at_unix_secs` (integer, required)
      - `last_updated_at_unix_secs` (integer, required)
      - `size_bytes` (integer, required)
    - `name` (string, required)
    - `supported_usages` (list of enum, required)
      - Allowed values: `prompt`, `auto`
    - `dependent_agents` (list of object, required, deprecated) — This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
      - `type`: `available` (DependentAvailableAgentIdentifier)
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `type`: `unknown` (DependentUnknownAgentIdentifier)
        - `id` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
    - `auto_sync_info` (object, optional, nullable)
      - `minimum_frequency_days` (integer, optional, default: 7) — Minimum frequency (in days) at which the document is refreshed. The actual interval may be shorter, never longer.
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional, nullable) — Unix timestamp for the next scheduled sync or None (in case of folders)
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
    - `is_frozen` (boolean, optional, default: false)
    - `refresh_status` (object, optional, nullable) — In-flight/last refresh state for an externally-synced KB file.
      - `status` (enum, optional, default: queued)
        - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
      - `enqueued_at` (integer, optional, nullable)
      - `started_at` (integer, optional, nullable)
      - `completed_at` (integer, optional, nullable)
      - `last_synced_at` (integer, optional, nullable)
      - `error_message` (string, optional, nullable)
  - `type`: `folder` (GetKnowledgeBaseSummaryFolderResponseModel)
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
    - `dependent_agents` (list of object, required, deprecated) — This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
      - `type`: `available` (DependentAvailableAgentIdentifier)
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `type`: `unknown` (DependentUnknownAgentIdentifier)
        - `id` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
    - `auto_sync_info` (object, optional, nullable)
      - `minimum_frequency_days` (integer, optional, default: 7) — Minimum frequency (in days) at which the document is refreshed. The actual interval may be shorter, never longer.
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
    - `is_frozen` (boolean, optional, default: false)
  - `type`: `text` (GetKnowledgeBaseSummaryTextResponseModel)
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
    - `id` (string, required)
    - `metadata` (object, required)
      - `created_at_unix_secs` (integer, required)
      - `last_updated_at_unix_secs` (integer, required)
      - `size_bytes` (integer, required)
    - `name` (string, required)
    - `supported_usages` (list of enum, required)
      - Allowed values: `prompt`, `auto`
    - `dependent_agents` (list of object, required, deprecated) — This field is deprecated and will be removed in the future, use the separate endpoint to get dependent agents instead.
      - `type`: `available` (DependentAvailableAgentIdentifier)
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `type`: `unknown` (DependentUnknownAgentIdentifier)
        - `id` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
    - `folder_parent_id` (string, optional, nullable) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
  - `type`: `url` (GetKnowledgeBaseSummaryURLResponseModel)
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
      - `type`: `available` (DependentAvailableAgentIdentifier)
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
      - `type`: `unknown` (DependentUnknownAgentIdentifier)
        - `id` (string, required)
        - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
    - `auto_sync_info` (object, optional, nullable)
      - `minimum_frequency_days` (integer, optional, default: 7) — Minimum frequency (in days) at which the document is refreshed. The actual interval may be shorter, never longer.
      - `auto_remove` (boolean, optional, default: false) — Whether to remove the document if the URL becomes unavailable
      - `consec_failures` (integer, optional, default: 0) — Number of consecutive sync failures
      - `next_refresh_by` (integer, optional, nullable) — Unix timestamp for the next scheduled sync or None (in case of folders)
    - `folder_parent_id` (string, optional, nullable) — The ID of the parent folder, or null if the document is at the root level.
    - `folder_path` (list of object, optional) — The folder path segments leading to this entity, from root to parent folder.
      - `id` (string, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional, nullable)

## Examples

**Response**

```json
{
  "documents": [
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
      "dependent_agents": [
        {
          "access_level": "admin",
          "created_at_unix_secs": 1,
          "id": "string",
          "name": "string",
          "referenced_resource_ids": [
            "string"
          ],
          "type": "available"
        }
      ],
      "folder_parent_id": "string",
      "folder_path": [
        {
          "id": "string"
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
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base")! as URL,
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
