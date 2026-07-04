---
title: "Get knowledge base summaries"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-summaries.md
path: docs/eleven-agents/api-reference/knowledge-base/get-summaries
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get knowledge base summaries

GET https://api.elevenlabs.io/v1/convai/knowledge-base/summaries

Gets multiple knowledge base document summaries by their IDs.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-summaries

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/summaries:
    get:
      operationId: get
      summary: Get Knowledge Base Summaries By Ids
      description: Gets multiple knowledge base document summaries by their IDs.
      tags:
        - summaries
      parameters:
        - name: document_ids
          in: query
          description: The ids of knowledge base documents.
          required: false
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
                type: object
                additionalProperties:
                  $ref: >-
                    #/components/schemas/type_conversationalAi/knowledgeBase/documents/summaries:SummariesGetResponseValue
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:KnowledgeBaseFolderPathSegmentSummaryResponseModel:
      type: object
      properties:
        id:
          type: string
      required:
        - id
      title: KnowledgeBaseFolderPathSegmentSummaryResponseModel
    type_:DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableAgentIdentifierAccessLevel
    type_:GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/type_:DependentAvailableAgentIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
          required:
            - type
            - id
      discriminator:
        propertyName: type
      title: GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
    type_:ExternalSyncType:
      type: string
      enum:
        - google_drive
      title: ExternalSyncType
    type_:ExternalFileSyncInfo:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ExternalSyncType'
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
    type_:GetKnowledgeBaseSummaryFolderResponseModelDependentAgentsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/type_:DependentAvailableAgentIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
          required:
            - type
            - id
      discriminator:
        propertyName: type
      title: GetKnowledgeBaseSummaryFolderResponseModelDependentAgentsItem
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
    type_:ExternalFolderSyncInfo:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:ExternalSyncType'
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
    type_:GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/type_:DependentAvailableAgentIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
          required:
            - type
            - id
      discriminator:
        propertyName: type
      title: GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
    type_:GetKnowledgeBaseSummaryUrlResponseModelDependentAgentsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/type_:DependentAvailableAgentIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
          required:
            - type
            - id
      discriminator:
        propertyName: type
      title: GetKnowledgeBaseSummaryUrlResponseModelDependentAgentsItem
    type_:KnowledgeBaseSummaryBatchSuccessfulResponseModelData:
      oneOf:
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
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentSummaryResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            dependent_agents:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:GetKnowledgeBaseSummaryFileResponseModelDependentAgentsItem
              description: >-
                This field is deprecated and will be removed in the future, use
                the separate endpoint to get dependent agents instead.
            external_sync_info:
              $ref: '#/components/schemas/type_:ExternalFileSyncInfo'
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
            - dependent_agents
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
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentSummaryResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            dependent_agents:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:GetKnowledgeBaseSummaryFolderResponseModelDependentAgentsItem
              description: >-
                This field is deprecated and will be removed in the future, use
                the separate endpoint to get dependent agents instead.
            children_count:
              type: integer
            auto_sync_info:
              $ref: '#/components/schemas/type_:AutoSyncInfo'
            external_sync_info:
              $ref: '#/components/schemas/type_:ExternalFolderSyncInfo'
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
            - dependent_agents
            - children_count
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
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentSummaryResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            dependent_agents:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:GetKnowledgeBaseSummaryTextResponseModelDependentAgentsItem
              description: >-
                This field is deprecated and will be removed in the future, use
                the separate endpoint to get dependent agents instead.
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - dependent_agents
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
                  #/components/schemas/type_:KnowledgeBaseFolderPathSegmentSummaryResponseModel
              description: >-
                The folder path segments leading to this entity, from root to
                parent folder.
            dependent_agents:
              type: array
              items:
                $ref: >-
                  #/components/schemas/type_:GetKnowledgeBaseSummaryUrlResponseModelDependentAgentsItem
              description: >-
                This field is deprecated and will be removed in the future, use
                the separate endpoint to get dependent agents instead.
            url:
              type: string
            auto_sync_info:
              $ref: '#/components/schemas/type_:AutoSyncInfo'
          required:
            - type
            - id
            - name
            - metadata
            - supported_usages
            - access_info
            - dependent_agents
            - url
      discriminator:
        propertyName: type
      title: KnowledgeBaseSummaryBatchSuccessfulResponseModelData
    type_conversationalAi/knowledgeBase/documents/summaries:SummariesGetResponseValue:
      oneOf:
        - type: object
          properties:
            status:
              type: string
              enum:
                - success
              description: 'Discriminator value: success'
            data:
              $ref: >-
                #/components/schemas/type_:KnowledgeBaseSummaryBatchSuccessfulResponseModelData
          required:
            - status
            - data
        - type: object
          properties:
            status:
              type: string
              enum:
                - failure
              description: 'Discriminator value: failure'
            error_code:
              type: integer
            error_status:
              type: string
            error_message:
              type: string
          required:
            - status
            - error_code
            - error_status
            - error_message
      discriminator:
        propertyName: status
      title: SummariesGetResponseValue
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

**Response**

```json
{
  "key": {
    "status": "success",
    "data": {
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
      ],
      "external_sync_info": {
        "type": "google_drive",
        "source_entity_id": "source_entity_id",
        "integration_connection_id": "integration_connection_id",
        "source_parent_entity_id": "source_parent_entity_id",
        "source_mime_type": "source_mime_type",
        "source_modified_time": "2024-01-15T09:30:00Z"
      },
      "folder_parent_id": "folder_parent_id",
      "folder_path": [
        {
          "id": "id"
        }
      ],
      "is_frozen": true
    }
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.summaries.get({
        documentIds: [
            "21m00Tcm4TlvDq8ikWAM",
            "31n11Udm5UmwEr9jkXBN",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.summaries.get(
    document_ids=[
        "21m00Tcm4TlvDq8ikWAM",
        "31n11Udm5UmwEr9jkXBN"
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%2221m00Tcm4TlvDq8ikWAM%22%2C%2231n11Udm5UmwEr9jkXBN%22%5D"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%2221m00Tcm4TlvDq8ikWAM%22%2C%2231n11Udm5UmwEr9jkXBN%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%2221m00Tcm4TlvDq8ikWAM%22%2C%2231n11Udm5UmwEr9jkXBN%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%2221m00Tcm4TlvDq8ikWAM%22%2C%2231n11Udm5UmwEr9jkXBN%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%2221m00Tcm4TlvDq8ikWAM%22%2C%2231n11Udm5UmwEr9jkXBN%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%2221m00Tcm4TlvDq8ikWAM%22%2C%2231n11Udm5UmwEr9jkXBN%22%5D")! as URL,
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
