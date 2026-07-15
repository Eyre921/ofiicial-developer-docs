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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/{documentation_id}:
    patch:
      operationId: update
      summary: Update Document
      description: Update the name and/or content of a document.
      tags:
        - documents
      parameters:
        - name: documentation_id
          in: path
          description: >-
            The id of a document from the knowledge base. This is returned on
            document addition.
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/conversational_ai_knowledge_base_documents_update_Response_200
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Update_document_v1_convai_knowledge_base__documentation_id__patch
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    Body_Update_document_v1_convai_knowledge_base__documentation_id__patch:
      type: object
      properties:
        name:
          type:
            - string
            - 'null'
          description: A custom, human-readable name for the document.
        content:
          type:
            - string
            - 'null'
          description: >-
            Updated content for the document. Only supported for text documents,
            URL documents with auto-sync disabled, and file documents.
      title: Body_Update_document_v1_convai_knowledge_base__documentation_id__patch
    KnowledgeBaseDocumentMetadataResponseModel:
      type: object
      properties:
        created_at_unix_secs:
          type: integer
        last_updated_at_unix_secs:
          type: integer
        size_bytes:
          type: integer
      required:
        - created_at_unix_secs
        - last_updated_at_unix_secs
        - size_bytes
      title: KnowledgeBaseDocumentMetadataResponseModel
    DocumentUsageModeEnum:
      type: string
      enum:
        - prompt
        - auto
      default: auto
      title: DocumentUsageModeEnum
    ResourceAccessInfoRole:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The role of the user making the request
      title: ResourceAccessInfoRole
    ResourceAccessInfoAnonymousAccessLevelOverride:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: >-
        The access level for anonymous users. If None, the resource is not
        shared publicly.
      title: ResourceAccessInfoAnonymousAccessLevelOverride
    ResourceAccessInfoAccessSource:
      type: string
      enum:
        - creator
        - explicit
        - workspace_admin
        - workspace_default
      description: >-
        Why the requesting user has access to this resource. 'creator' = caller
        is the owner. 'explicit' = caller (or one of their workspace groups) is
        listed in role_to_group_ids beyond the workspace-wide everyone group.
        'workspace_default' = the workspace-wide everyone group is listed in
        role_to_group_ids (every non-anon workspace member, including admins,
        sees this resource). 'workspace_admin' = caller is a workspace admin and
        the admin seat is the *only* path to access; reserved for docs nobody
        else can see. Lets the UI disclose why an admin-bypass viewer sees a doc
        that wasn't explicitly shared with them.
      title: ResourceAccessInfoAccessSource
    ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
          description: Whether the user making the request is the creator of the agent
        creator_name:
          type: string
          description: Name of the agent's creator
        creator_email:
          type: string
          description: Email of the agent's creator
        role:
          $ref: '#/components/schemas/ResourceAccessInfoRole'
          description: The role of the user making the request
        anonymous_access_level_override:
          oneOf:
            - $ref: >-
                #/components/schemas/ResourceAccessInfoAnonymousAccessLevelOverride
            - type: 'null'
          description: >-
            The access level for anonymous users. If None, the resource is not
            shared publicly.
        access_source:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfoAccessSource'
            - type: 'null'
          description: >-
            Why the requesting user has access to this resource. 'creator' =
            caller is the owner. 'explicit' = caller (or one of their workspace
            groups) is listed in role_to_group_ids beyond the workspace-wide
            everyone group. 'workspace_default' = the workspace-wide everyone
            group is listed in role_to_group_ids (every non-anon workspace
            member, including admins, sees this resource). 'workspace_admin' =
            caller is a workspace admin and the admin seat is the *only* path to
            access; reserved for docs nobody else can see. Lets the UI disclose
            why an admin-bypass viewer sees a doc that wasn't explicitly shared
            with them.
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
      title: ResourceAccessInfo
    KnowledgeBaseFolderPathSegmentResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type:
            - string
            - 'null'
      required:
        - id
        - name
      title: KnowledgeBaseFolderPathSegmentResponseModel
    ContentFormat:
      type: string
      enum:
        - html
        - markdown
      default: html
      description: >-
        Canonical representation of a knowledge base document's stored content.


        HTML is the legacy default; documents created before this field existed
        are

        interpreted as HTML.
      title: ContentFormat
    AutoSyncInfo:
      type: object
      properties:
        minimum_frequency_days:
          type: integer
          default: 7
          description: Maximum number of days between automatic syncs
        auto_remove:
          type: boolean
          default: false
          description: Whether to remove the document if the URL becomes unavailable
        consec_failures:
          type: integer
          default: 0
          description: Number of consecutive sync failures
        next_refresh_by:
          type:
            - integer
            - 'null'
          description: >-
            Unix timestamp for the next scheduled sync or None (in case of
            folders)
      title: AutoSyncInfo
    ExternalSyncProvider:
      type: string
      enum:
        - google_drive
      title: ExternalSyncProvider
    ExternalFileSyncInfo:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ExternalSyncProvider'
          description: Provider identifier
        source_entity_id:
          type: string
          description: Entity ID in the external system
        integration_connection_id:
          type: string
          description: Integration connection instance ID
        source_parent_entity_id:
          type: string
          description: Folder ID in the external system this file was synced from
        source_mime_type:
          type: string
          description: Original MIME type in the external system
        source_modified_time:
          type: string
          format: date-time
          description: Last modified time from the external system
        root_folder_id:
          type:
            - string
            - 'null'
          description: >-
            KB folder ID of the sync root, used to query all entities under a
            sync tree
      required:
        - type
        - source_entity_id
        - integration_connection_id
        - source_parent_entity_id
        - source_mime_type
        - source_modified_time
      description: Tracks the link back to the original file in an external source.
      title: ExternalFileSyncInfo
    ExternalFolderSyncInfo:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ExternalSyncProvider'
          description: Provider identifier
        source_entity_id:
          type: string
          description: Entity ID in the external system
        integration_connection_id:
          type: string
          description: Integration connection instance ID
        root_folder_id:
          type:
            - string
            - 'null'
          description: KB folder ID of the sync root. None means this folder is the root.
        sync_cursor:
          type:
            - string
            - 'null'
          description: Opaque cursor for incremental sync, interpreted by the provider
        last_sync_at:
          type:
            - integer
            - 'null'
          description: Unix timestamp of last completed sync
      required:
        - type
        - source_entity_id
        - integration_connection_id
      description: Metadata for a KB folder that mirrors an external source folder.
      title: ExternalFolderSyncInfo
    ExternalSyncJobTrigger:
      type: string
      enum:
        - on_demand
        - on_connect
        - auto
      title: ExternalSyncJobTrigger
    CrawlStatus:
      type: string
      enum:
        - queued
        - processing
        - succeeded
        - failed
        - skipped
        - cancelled
      default: queued
      title: CrawlStatus
    ExternalSyncJobType:
      type: string
      enum:
        - full
        - incremental
      title: ExternalSyncJobType
    KbExternalSyncJob:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ExternalSyncProvider'
        folder_id:
          type: string
        integration_connection_id:
          type: string
        triggered_by:
          $ref: '#/components/schemas/ExternalSyncJobTrigger'
        status:
          $ref: '#/components/schemas/CrawlStatus'
          default: queued
        sync_type:
          oneOf:
            - $ref: '#/components/schemas/ExternalSyncJobType'
            - type: 'null'
        items_identified:
          type: integer
          default: 0
        items_processed:
          type: integer
          default: 0
        error_message:
          type:
            - string
            - 'null'
        started_at:
          type:
            - integer
            - 'null'
        completed_at:
          type:
            - integer
            - 'null'
        updated_at:
          type: integer
        id:
          type: string
        created_at:
          type: integer
      required:
        - type
        - folder_id
        - integration_connection_id
        - triggered_by
        - updated_at
        - id
        - created_at
      title: KbExternalSyncJob
    conversational_ai_knowledge_base_documents_update_Response_200:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - url
              description: 'Discriminator value: url'
            id:
              type: string
            name:
              type: string
            metadata:
              $ref: '#/components/schemas/KnowledgeBaseDocumentMetadataResponseModel'
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/ResourceAccessInfo'
            folder_parent_id:
              type:
                - string
                - 'null'
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            url:
              type: string
            extracted_inner_html:
              type: string
            content_format:
              $ref: '#/components/schemas/ContentFormat'
              default: html
            auto_sync_info:
              oneOf:
                - $ref: '#/components/schemas/AutoSyncInfo'
                - type: 'null'
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - url
            - extracted_inner_html
          description: GetKnowledgeBaseURLResponseModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - file
              description: 'Discriminator value: file'
            id:
              type: string
            name:
              type: string
            metadata:
              $ref: '#/components/schemas/KnowledgeBaseDocumentMetadataResponseModel'
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/ResourceAccessInfo'
            folder_parent_id:
              type:
                - string
                - 'null'
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            extracted_inner_html:
              type: string
            content_format:
              $ref: '#/components/schemas/ContentFormat'
              default: html
            filename:
              type: string
            external_sync_info:
              oneOf:
                - $ref: '#/components/schemas/ExternalFileSyncInfo'
                - type: 'null'
            is_frozen:
              type: boolean
              default: false
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - extracted_inner_html
            - filename
          description: GetKnowledgeBaseFileResponseModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
              description: 'Discriminator value: text'
            id:
              type: string
            name:
              type: string
            metadata:
              $ref: '#/components/schemas/KnowledgeBaseDocumentMetadataResponseModel'
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/ResourceAccessInfo'
            folder_parent_id:
              type:
                - string
                - 'null'
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            extracted_inner_html:
              type: string
            content_format:
              $ref: '#/components/schemas/ContentFormat'
              default: html
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - extracted_inner_html
          description: GetKnowledgeBaseTextResponseModel variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - folder
              description: 'Discriminator value: folder'
            id:
              type: string
            name:
              type: string
            metadata:
              $ref: '#/components/schemas/KnowledgeBaseDocumentMetadataResponseModel'
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/ResourceAccessInfo'
            folder_parent_id:
              type:
                - string
                - 'null'
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            children_count:
              type: integer
            auto_sync_info:
              oneOf:
                - $ref: '#/components/schemas/AutoSyncInfo'
                - type: 'null'
            external_sync_info:
              oneOf:
                - $ref: '#/components/schemas/ExternalFolderSyncInfo'
                - type: 'null'
            is_frozen:
              type: boolean
              default: false
            active_sync_job:
              oneOf:
                - $ref: '#/components/schemas/KbExternalSyncJob'
                - type: 'null'
              description: >-
                Most recent (in-flight or terminal) external sync job for this
                folder, if any. Used by clients to render sync progress.
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - children_count
          description: GetKnowledgeBaseFolderResponseModel variant
      discriminator:
        propertyName: type
      title: conversational_ai_knowledge_base_documents_update_Response_200
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
