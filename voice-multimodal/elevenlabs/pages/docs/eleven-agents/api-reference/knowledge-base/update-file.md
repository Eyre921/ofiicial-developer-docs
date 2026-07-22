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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/{documentation_id}/update-file:
    patch:
      operationId: update_file
      summary: Update File Document
      description: >-
        Update the source file of a file document. The document name, content,
        and metadata are updated to reflect the new file. Any manual content
        edits will be overwritten.
      tags:
        - document
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
                  #/components/schemas/type_conversationalAi/knowledgeBase/document:DocumentUpdateFileResponse
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                  description: >-
                    Documentation that the agent will have access to in order to
                    interact with users.
              required:
                - file
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
    type_:KnowledgeBaseDocumentMetadataResponseModel:
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
    type_:DocumentUsageModeEnum:
      type: string
      enum:
        - prompt
        - auto
      default: auto
      title: DocumentUsageModeEnum
    type_:ResourceAccessInfoRole:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The role of the user making the request
      title: ResourceAccessInfoRole
    type_:ResourceAccessInfoAnonymousAccessLevelOverride:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: ResourceAccessInfoAnonymousAccessLevelOverride
    type_:ResourceAccessInfoAccessSource:
      type: string
      enum:
        - creator
        - explicit
        - workspace_admin
        - workspace_default
      title: ResourceAccessInfoAccessSource
    type_:ResourceAccessInfo:
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
          $ref: '#/components/schemas/type_:ResourceAccessInfoRole'
          description: The role of the user making the request
        anonymous_access_level_override:
          $ref: >-
            #/components/schemas/type_:ResourceAccessInfoAnonymousAccessLevelOverride
          description: >-
            The access level for anonymous users. If None, the resource is not
            shared publicly.
        access_source:
          $ref: '#/components/schemas/type_:ResourceAccessInfoAccessSource'
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
    type_:KnowledgeBaseFolderPathSegmentResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
      required:
        - id
      title: KnowledgeBaseFolderPathSegmentResponseModel
    type_:ContentFormat:
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
    type_:AutoSyncInfo:
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
          type: integer
          description: >-
            Unix timestamp for the next scheduled sync or None (in case of
            folders)
      title: AutoSyncInfo
    type_:ExternalSyncProvider:
      type: string
      enum:
        - google_drive
      title: ExternalSyncProvider
    type_:ExternalFileSyncInfo:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ExternalSyncProvider'
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
          type: string
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
    type_:CrawlStatus:
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
    type_:FileRefreshStatus:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/type_:CrawlStatus'
        enqueued_at:
          type: integer
        started_at:
          type: integer
        completed_at:
          type: integer
        last_synced_at:
          type: integer
        error_message:
          type: string
      description: In-flight/last refresh state for an externally-synced KB file.
      title: FileRefreshStatus
    type_:ExternalFolderSyncInfo:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ExternalSyncProvider'
          description: Provider identifier
        source_entity_id:
          type: string
          description: Entity ID in the external system
        integration_connection_id:
          type: string
          description: Integration connection instance ID
        root_folder_id:
          type: string
          description: KB folder ID of the sync root. None means this folder is the root.
        sync_cursor:
          type: string
          description: Opaque cursor for incremental sync, interpreted by the provider
        last_sync_at:
          type: integer
          description: Unix timestamp of last completed sync
      required:
        - type
        - source_entity_id
        - integration_connection_id
      description: Metadata for a KB folder that mirrors an external source folder.
      title: ExternalFolderSyncInfo
    type_:ExternalSyncJobTrigger:
      type: string
      enum:
        - on_demand
        - on_connect
        - auto
      title: ExternalSyncJobTrigger
    type_:ExternalSyncJobType:
      type: string
      enum:
        - full
        - incremental
      title: ExternalSyncJobType
    type_:KbExternalSyncJob:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ExternalSyncProvider'
        folder_id:
          type: string
        integration_connection_id:
          type: string
        triggered_by:
          $ref: '#/components/schemas/type_:ExternalSyncJobTrigger'
        status:
          $ref: '#/components/schemas/type_:CrawlStatus'
        sync_type:
          $ref: '#/components/schemas/type_:ExternalSyncJobType'
        items_identified:
          type: integer
          default: 0
        items_processed:
          type: integer
          default: 0
        error_message:
          type: string
        started_at:
          type: integer
        completed_at:
          type: integer
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
    type_conversationalAi/knowledgeBase/document:DocumentUpdateFileResponse:
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
              $ref: >-
                #/components/schemas/type_:KnowledgeBaseDocumentMetadataResponseModel
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/type_:DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/type_:ResourceAccessInfo'
            folder_parent_id:
              type: string
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            url:
              type: string
            extracted_inner_html:
              type: string
            content_format:
              $ref: '#/components/schemas/type_:ContentFormat'
            auto_sync_info:
              $ref: '#/components/schemas/type_:AutoSyncInfo'
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - url
            - extracted_inner_html
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
              $ref: >-
                #/components/schemas/type_:KnowledgeBaseDocumentMetadataResponseModel
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/type_:DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/type_:ResourceAccessInfo'
            folder_parent_id:
              type: string
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            extracted_inner_html:
              type: string
            content_format:
              $ref: '#/components/schemas/type_:ContentFormat'
            filename:
              type: string
            external_sync_info:
              $ref: '#/components/schemas/type_:ExternalFileSyncInfo'
            auto_sync_info:
              $ref: '#/components/schemas/type_:AutoSyncInfo'
            refresh_status:
              $ref: '#/components/schemas/type_:FileRefreshStatus'
              description: >-
                In-flight or last refresh state for an externally-synced file.
                Used by clients to render sync progress and disable re-sync
                while a refresh is queued or processing.
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
              $ref: >-
                #/components/schemas/type_:KnowledgeBaseDocumentMetadataResponseModel
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/type_:DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/type_:ResourceAccessInfo'
            folder_parent_id:
              type: string
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            extracted_inner_html:
              type: string
            content_format:
              $ref: '#/components/schemas/type_:ContentFormat'
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - extracted_inner_html
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
              $ref: >-
                #/components/schemas/type_:KnowledgeBaseDocumentMetadataResponseModel
            supported_usages:
              type: array
              items:
                $ref: '#/components/schemas/type_:DocumentUsageModeEnum'
            access_info:
              $ref: '#/components/schemas/type_:ResourceAccessInfo'
            folder_parent_id:
              type: string
              description: >-
                The ID of the parent folder, or null if the document is at the
                root level.
            folder_path:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            children_count:
              type: integer
            document_count:
              type: integer
              description: >-
                Number of non-folder documents anywhere in this folder's subtree
                (recursive). Counting stops past 1000;
            auto_sync_info:
              $ref: '#/components/schemas/type_:AutoSyncInfo'
            external_sync_info:
              $ref: '#/components/schemas/type_:ExternalFolderSyncInfo'
            is_frozen:
              type: boolean
              default: false
            active_sync_job:
              $ref: '#/components/schemas/type_:KbExternalSyncJob'
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
            - document_count
      discriminator:
        propertyName: type
      title: DocumentUpdateFileResponse
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

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
