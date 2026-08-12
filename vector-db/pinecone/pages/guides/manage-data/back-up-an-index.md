---
title: "Back up an index"
source: https://docs.pinecone.io/guides/manage-data/back-up-an-index
path: guides/manage-data/back-up-an-index
---

Create backups of serverless indexes to protect data, copy indexes, or experiment with configurations using the Pinecone SDK, API, or console.

## Create a backup

You can [create a backup from a serverless index](/reference/api/latest/control-plane/create_backup) as follows.

<Note>
  Backups are supported for indexes without a schema definition and for integrated embedding indexes that use the records API. They are not supported for full-text search indexes with document schemas that include `full_text_search` string fields, `dense_vector` fields, or `sparse_vector` fields. Indexes with document schemas also do not support `semantic_text` fields.
</Note>

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  backup = pc.create_backup(
      index_name="docs-example", 
      backup_name="example-backup", 
      description="Monthly backup of production index"
  )

  print(backup)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const backup = await pc.createBackup({
    indexName: 'docs-example',
    name: 'example-backup',
    description: 'Monthly backup of production index',
  });

  console.log(backup);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";
          String backupName = "example-backup";
          String backupDescription = "Monthly backup of production index";

          BackupModel backup = pc.createBackup(indexName,backupName, backupDescription);

          System.out.println(backup);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
      bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      indexName := "docs-example"
      backupName := "example-backup"
      backupDesc := "Monthly backup of production index"

      backup, err := pc.CreateBackup(ctx, &pinecone.CreateBackupParams{
          IndexName:   indexName,
          Name:        &backupName,
          Description: &backupDesc,
      })
      if err != nil {
          log.Fatalf("Failed to create backup: %v", err)
      }

      fmt.Printf(prettifyStruct(backup))
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="docs-example"

  curl "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -d '{
        "name": "example-backup", 
        "description": "Monthly backup of production index"
        }'
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'backup_id': '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
   'cloud': 'aws',
   'created_at': '2025-05-15T00:52:10.809305882Z',
   'description': 'Monthly backup of production index',
   'dimension': 1024,
   'name': 'example-backup',
   'namespace_count': 3,
   'record_count': 98,
   'region': 'us-east-1',
   'size_bytes': 1069169,
   'source_index_id': 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
   'source_index_name': 'docs-example',
   'status': 'Ready',
   'tags': {}}
  ```

  ```javascript JavaScript theme={null}
  {
    backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
    sourceIndexName: 'docs-example',
    sourceIndexId: 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
    name: 'example-backup',
    description: 'Monthly backup of production index',
    status: 'Ready',
    cloud: 'aws',
    region: 'us-east-1',
    dimension: 1024,
    metric: undefined,
    recordCount: 98,
    namespaceCount: 3,
    sizeBytes: 1069169,
    tags: {},
    createdAt: '2025-05-14T16:37:25.625540Z'
  }
  ```

  ```java Java theme={null}
  class BackupModel {
      backupId: 0d75b99f-be61-4a93-905e-77201286c02e
      sourceIndexName: docs-example
      sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
      name: example-backup
      description: Monthly backup of production index
      status: Initializing
      cloud: aws
      region: us-east-1
      dimension: null
      metric: null
      recordCount: null
      namespaceCount: null
      sizeBytes: null
      tags: {}
      createdAt: 2025-05-16T19:42:23.804787550Z
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "cloud": "aws",
    "created_at": "2025-05-15T00:52:10.809305882Z",
    "description": "Monthly backup of production index",
    "dimension": 1024,
    "name": "example-backup",
    "region": "us-east-1",
    "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name": "docs-example",
    "status": "Initializing",
    "tags": {}
  }
  ```

  ```json curl theme={null}
  {
    "backup_id":"8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "source_index_id":"f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name":"docs-example",
    "tags":{},
    "name":"example-backup",
    "description":"Monthly backup of production index",
    "status":"Ready",
    "cloud":"aws",
    "region":"us-east-1",
    "dimension":1024,
    "record_count":96,
    "namespace_count":3,
    "size_bytes":1069169,
    "created_at":"2025-05-14T16:37:25.625540Z"
    }
  ```
</CodeGroup>

<Tip>
  You can create a backup using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups).
</Tip>

## Describe a backup

You can [view the details of a backup](/reference/api/latest/control-plane/describe_backup) as follows.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  backup = pc.describe_backup(backup_id="8c85e612-ed1c-4f97-9f8c-8194e07bcf71")

  print(backup)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const backupDesc = await pc.describeBackup('8c85e612-ed1c-4f97-9f8c-8194e07bcf71');

  console.log(backupDesc);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          BackupModel backupModel = pc.describeBackup("8c85e612-ed1c-4f97-9f8c-8194e07bcf71");

          System.out.println(backupModel);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	backup, err := pc.DescribeBackup(ctx, "8c85e612-ed1c-4f97-9f8c-8194e07bcf71")
  	if err != nil {
  		log.Fatalf("Failed to describe backup: %v", err)
  	}
  	fmt.Printf(prettifyStruct(backup))
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="8c85e612-ed1c-4f97-9f8c-8194e07bcf71"

  curl -X GET "https://api.pinecone.io/backups/$BACKUP_ID" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -H "accept: application/json"
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  {'backup_id': '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
   'cloud': 'aws',
   'created_at': '2025-05-15T00:52:10.809354Z',
   'description': 'Monthly backup of production index',
   'dimension': 1024,
   'name': 'example-backup',
   'namespace_count': 3,
   'record_count': 98,
   'region': 'us-east-1',
   'size_bytes': 1069169,
   'source_index_id': 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
   'source_index_name': 'docs-example',
   'status': 'Ready',
   'tags': {}}
  ```

  ```javascript JavaScript theme={null}
  {
    backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
    sourceIndexName: 'docs-example',
    sourceIndexId: 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
    name: 'example-backup',
    description: 'Monthly backup of production index',
    status: 'Ready',
    cloud: 'aws',
    region: 'us-east-1',
    dimension: 1024,
    metric: undefined,
    recordCount: 98,
    namespaceCount: 3,
    sizeBytes: 1069169,
    tags: {},
    createdAt: '2025-05-14T16:37:25.625540Z'
  }
  ```

  ```java Java theme={null}
  class BackupList {
      data: [class BackupModel {
          backupId: 95707edb-e482-49cf-b5a5-312219a51a97
          sourceIndexName: docs-example
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup
          description: Monthly backup of production index
          status: Initializing
          cloud: aws
          region: us-east-1
          dimension: null
          metric: null
          recordCount: null
          namespaceCount: null
          sizeBytes: null
          tags: {}
          createdAt: 2025-05-16T19:46:26.248428Z
          additionalProperties: null
      }]
      pagination: null
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "cloud": "aws",
    "created_at": "2025-05-15T00:52:10.809354Z",
    "description": "Monthly backup of production index",
    "dimension": 1024,
    "name": "example-backup",
    "namespace_count": 3,
    "record_count": 98,
    "region": "us-east-1",
    "size_bytes": 1069169,
    "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name": "docs-example",
    "status": "Ready",
    "tags": {}
  }
  ```

  ```json curl theme={null}
  {
    "backup_id":"8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
    "source_index_id":"f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
    "source_index_name":"docs-example",
    "tags":{},
    "name":"example-backup",
    "description":"Monthly backup of production index",
    "status":"Ready",
    "cloud":"aws",
    "region":"us-east-1",
    "dimension":1024,
    "record_count":98,
    "namespace_count":3,
    "size_bytes":1069169,
    "created_at":"2025-03-11T18:29:50.549505Z"
  }
  ```
</CodeGroup>

<Tip>
  You can view backup details using the [Pinecone console](https://app.pinecone.io/organizations/-/projects-/backups).
</Tip>

## List backups for an index

You can [list backups for a specific index](/reference/api/latest/control-plane/list_index_backups) as follows.

Up to 100 backups are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of backups are returned instead. Whenever there are additional backups to return, the response also includes a `pagination_token` that you can use to get the next batch of backups. When the response does not include a `pagination_token`, there are no more backups to return.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_backups = pc.list_backups(index_name="docs-example")

  print(index_backups)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const indexBackups = await pc.listBackups({ indexName: 'docs-example' });

  console.log(indexBackups);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";
          BackupList indexBackupList = pc.listIndexBackups(indexName);

          System.out.println(indexBackupList);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	indexName := "docs-example"
  	limit := 2
  	indexBackups, err := pc.ListBackups(ctx, &pinecone.ListBackupsParams{
  		Limit: &limit,
  		IndexName: &indexName,
  	})
  	if err != nil {
  		log.Fatalf("Failed to list backups: %v", err)
  	}
  	fmt.Printf(prettifyStruct(indexBackups))
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="docs-example"

  curl -X GET "https://api.pinecone.io/indexes/$INDEX_NAME/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -H "accept: application/json"
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  [{
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "source_index_name": "docs-example",
      "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "name": "example-backup",
      "description": "Monthly backup of production index",
      "dimension": 1024,
      "record_count": 98,
      "namespace_count": 3,
      "size_bytes": 1069169,
      "created_at": "2025-05-15T00:52:10.809305882Z"
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    data: [
      {
        backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
        sourceIndexName: 'docs-example',
        sourceIndexId: 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
        name: 'example-backup',
        description: 'Monthly backup of production index',
        status: 'Ready',
        cloud: 'aws',
        region: 'us-east-1',
        dimension: 1024,
        metric: undefined,
        recordCount: 98,
        namespaceCount: 3,
        sizeBytes: 1069169,
        tags: {},
        createdAt: '2025-05-14T16:37:25.625540Z'
      }
    ],
    pagination: undefined
  }
  ```

  ```java Java theme={null}
  class BackupList {
      data: [class BackupModel {
          backupId: 8c85e612-ed1c-4f97-9f8c-8194e07bcf71
          sourceIndexName: docs-example
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup
          description: Monthly backup of production index
          status: Initializing
          cloud: aws
          region: us-east-1
          dimension: null
          metric: null
          recordCount: null
          namespaceCount: null
          sizeBytes: null
          tags: {}
          createdAt: 2025-05-16T19:46:26.248428Z
          additionalProperties: null
      }]
      pagination: null
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "data": [
      {
        "backup_id": "bf2cda5d-b233-4a0a-aae9-b592780ad3ff",
        "cloud": "aws",
        "created_at": "2025-05-16T18:01:51.531129Z",
        "description": "Monthly backup of production index",
        "dimension": 0,
        "name": "example-backup",
        "namespace_count": 1,
        "record_count": 96,
        "region": "us-east-1",
        "size_bytes": 86393,
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "status": "Ready",
        "tags": {}
      },
      {
        "backup_id": "e12269b0-a29b-4af0-9729-c7771dec03e3",
        "cloud": "aws",
        "created_at": "2025-05-14T17:00:45.803146Z",
        "dimension": 0,
        "name": "example-backup2",
        "namespace_count": 1,
        "record_count": 96,
        "region": "us-east-1",
        "size_bytes": 86393,
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "status": "Ready"
      }
    ],
    "pagination": {
      "next": "eyJsaW1pdCI6Miwib2Zmc2V0IjoyfQ=="
    }
  }
  ```

  ```json curl theme={null}
  {
    "data":
    [
      {
        "backup_id":"9947520e-d5a1-4418-a78d-9f464c9969da",
        "source_index_id":"8433941a-dae7-43b5-ac2c-d3dab4a56b2b",
        "source_index_name":"docs-example",
        "tags":{},
        "name":"example-backup",
        "description":"Monthly backup of production index",
        "status":"Pending",
        "cloud":"aws",
        "region":"us-east-1",
        "dimension":1024,
        "record_count":98,
        "namespace_count":3,
        "size_bytes":1069169,
        "created_at":"2025-03-11T18:29:50.549505Z"
        }
      ],
    "pagination":null
  }
  ```
</CodeGroup>

<Tip>
  You can view the backups for a specific index from either the [Backups](https://app.pinecone.io/organizations/-/projects/-/backups) tab or the [Indexes](https://app.pinecone.io/organizations/-/projects/-/indexes) tab in the Pinecone console.
</Tip>

## List backups in a project

You can [list backups for all indexes in a project](/reference/api/latest/control-plane/list_project_backups) as follows.

Up to 100 backups are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of backups are returned instead. Whenever there are additional backups to return, the response also includes a `pagination_token` that you can use to get the next batch of backups. When the response does not include a `pagination_token`, there are no more backups to return.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  project_backups = pc.list_backups()

  print(project_backups)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const projectBackups = await pc.listBackups();

  console.log(projectBackups);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          String indexName = "docs-example";
          BackupList projectBackupList = pc.listProjectBackups();

          System.out.println(projectBackupList);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	limit := 3
  	backups, err := pc.ListBackups(ctx, &pinecone.ListBackupsParams{
  		Limit:     &limit,
  	})
  	if err != nil {
  		log.Fatalf("Failed to list backups: %v", err)
  	}
  	fmt.Printf(prettifyStruct(backups))
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -H "accept: application/json"
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```python Python theme={null}
  [{
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "source_index_name": "docs-example",
      "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "name": "example-backup",
      "description": "Monthly backup of production index",
      "dimension": 1024,
      "record_count": 98,
      "namespace_count": 3,
      "size_bytes": 1069169,
      "created_at": "2025-05-15T20:26:21.248515Z"
  }, {
      "backup_id": "95707edb-e482-49cf-b5a5-312219a51a97",
      "source_index_name": "docs-example2",
      "source_index_id": "b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "name": "example-backup2",
      "description": "Monthly backup of production index",
      "dimension": 1024,
      "record_count": 97,
      "namespace_count": 2,
      "size_bytes": 1069169,
      "created_at": "2025-05-15T00:52:10.809354Z"
  }, {
      "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
      "source_index_name": "docs-example3",
      "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
      "status": "Ready",
      "cloud": "aws",
      "region": "us-east-1",
      "tags": {},
      "name": "example-backup3",
      "description": "Monthly backup of production index",
      "dimension": 1024,
      "record_count": 98,
      "namespace_count": 3,
      "size_bytes": 1069169,
      "created_at": "2025-05-14T16:37:25.625540Z"
  }]
  ```

  ```javascript JavaScript theme={null}
  {
    data: [
      {
        backupId: 'e12269b0-a29b-4af0-9729-c7771dec03e3',
        sourceIndexName: 'docs-example',
        sourceIndexId: 'bcb5b3c9-903e-4cb6-8b37-a6072aeb874f',
        name: 'example-backup',
        description: undefined,
        status: 'Ready',
        cloud: 'aws',
        region: 'us-east-1',
        dimension: 0,
        metric: undefined,
        recordCount: 96,
        namespaceCount: 1,
        sizeBytes: 86393,
        tags: undefined,
        createdAt: '2025-05-14T17:00:45.803146Z'
      },
      {
        backupId: 'd686451d-1ede-4004-9f72-7d22cc799b6e',
        sourceIndexName: 'docs-example2',
        sourceIndexId: 'b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6',
        name: 'example-backup2',
        description: undefined,
        status: 'Ready',
        cloud: 'aws',
        region: 'us-east-1',
        dimension: 1024,
        metric: undefined,
        recordCount: 50,
        namespaceCount: 1,
        sizeBytes: 545171,
        tags: undefined,
        createdAt: '2025-05-14T17:00:34.814371Z'
      },
      {
        backupId: '8c85e612-ed1c-4f97-9f8c-8194e07bcf71',
        sourceIndexName: 'docs-example3',
        sourceIndexId: 'f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74',
        name: 'example-backup3',
        description: 'Monthly backup of production index',
        status: 'Ready',
        cloud: 'aws',
        region: 'us-east-1',
        dimension: 1024,
        metric: undefined,
        recordCount: 98,
        namespaceCount: 3,
        sizeBytes: 1069169,
        tags: {},
        createdAt: '2025-05-14T16:37:25.625540Z'
      }
    ],
    pagination: undefined
  }
  ```

  ```java Java theme={null}
  class BackupList {
      data: [class BackupModel {
          backupId: 13761d20-7a0b-4778-ac27-36dd91c4be43
          sourceIndexName: example-dense-index
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup
          description: Monthly backup of production index
          status: Initializing
          cloud: aws
          region: us-east-1
          dimension: null
          metric: null
          recordCount: null
          namespaceCount: null
          sizeBytes: null
          tags: {}
          createdAt: 2025-05-16T19:46:26.248428Z
          additionalProperties: null
      }, class BackupModel {
          backupId: 0d75b99f-be61-4a93-905e-77201286c02e
          sourceIndexName: example-dense-index
          sourceIndexId: f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74
          name: example-backup2
          description: Monthly backup of production index
          status: Initializing
          cloud: aws
          region: us-east-1
          dimension: null
          metric: null
          recordCount: null
          namespaceCount: null
          sizeBytes: null
          tags: {}
          createdAt: 2025-05-16T19:42:23.804820Z
          additionalProperties: null
      }, class BackupModel {
          backupId: bf2cda5d-b233-4a0a-aae9-b592780ad3ff
          sourceIndexName: example-sparse-index
          sourceIndexId: bcb5b3c9-903e-4cb6-8b37-a6072aeb874f
          name: example-backup3
          description: Monthly backup of production index
          status: Ready
          cloud: aws
          region: us-east-1
          dimension: 0
          metric: null
          recordCount: 96
          namespaceCount: 1
          sizeBytes: 86393
          tags: {}
          createdAt: 2025-05-16T18:01:51.531129Z
          additionalProperties: null
      }]
      pagination: null
      additionalProperties: null
  }
  ```

  ```go Go theme={null}
  {
    "data": [
      {
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "cloud": "aws",
        "created_at": "2025-05-15T00:52:10.809305882Z",
        "description": "Monthly backup of production index",
        "dimension": 1024,
        "name": "example-backup",
        "namespace_count": 3,
        "record_count": 98,
        "region": "us-east-1",
        "size_bytes": 1069169,
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "docs-example",
        "status": "Ready",
        "tags": {}
      },
      {
        "backup_id": "bf2cda5d-b233-4a0a-aae9-b592780ad3ff",
        "cloud": "aws",
        "created_at": "2025-05-15T00:52:10.809305882Z",
        "description": "Monthly backup of production index",
        "dimension": 0,
        "name": "example-backup2",
        "namespace_count": 1,
        "record_count": 96,
        "region": "us-east-1",
        "size_bytes": 86393,
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "example-sparse-index",
        "status": "Ready",
        "tags": {}
      },
      {
        "backup_id": "f73028f6-1746-410e-ab6d-9dd2519df4de",
        "cloud": "aws",
        "created_at": "2025-05-15T20:26:21.248515Z",
        "description": "Monthly backup of production index",
        "dimension": 1024,
        "name": "example-backup3",
        "namespace_count": 2,
        "record_count": 97,
        "region": "us-east-1",
        "size_bytes": 1069169,
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "example-dense-index",
        "status": "Ready",
        "tags": {}
      }
    ],
    "pagination": {
      "next": "eyJsaW1pdCI6Miwib2Zmc2V0IjoyfQ=="
    }  
  }
  ```

  ```json curl  theme={null}
  {
    "data": [
      {
        "backup_id": "e12269b0-a29b-4af0-9729-c7771dec03e3",
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "tags": null,
        "name": "example-backup",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 0,
        "record_count": 96,
        "namespace_count": 1,
        "size_bytes": 86393,
        "created_at": "2025-05-14T17:00:45.803146Z"
      },
      {
        "backup_id": "d686451d-1ede-4004-9f72-7d22cc799b6e",
        "source_index_id": "b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6",
        "source_index_name": "docs-example2",
        "tags": null,
        "name": "example-backup2",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 50,
        "namespace_count": 1,
        "size_bytes": 545171,
        "created_at": "2025-05-14T17:00:34.814371Z"
      },
      {
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "docs-example3",
        "tags": {},
        "name": "example-backup3",
        "description": "Monthly backup of production index",
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 98,
        "namespace_count": 3,
        "size_bytes": 1069169,
        "created_at": "2025-05-14T16:37:25.625540Z"
      }
    ],
    "pagination": null
  }
  ```
</CodeGroup>

<Tip>
  You can view all backups in a project using the [Pinecone console](https://app.pinecone.io/organizations/-/projects-/backups).
</Tip>

## Delete a backup

You can [delete a backup](/reference/api/latest/control-plane/delete_backup) as follows.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.delete_backup(backup_id="9947520e-d5a1-4418-a78d-9f464c9969da")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  await pc.deleteBackup('9947520e-d5a1-4418-a78d-9f464c9969da');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.*;

  public class CreateBackup {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          pc.deleteBackup("9947520e-d5a1-4418-a78d-9f464c9969da");
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"

  	"github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
  	bytes, _ := json.MarshalIndent(obj, "", "  ")
  	return string(bytes)
  }

  func main() {
  	ctx := context.Background()

  	pc, err := pinecone.NewClient(pinecone.NewClientParams{
  		ApiKey: "YOUR_API_KEY",
  	})
  	if err != nil {
  		log.Fatalf("Failed to create Client: %v", err)
  	}

  	err = pc.DeleteBackup(ctx, "8c85e612-ed1c-4f97-9f8c-8194e07bcf71")
  	if err != nil {
  		log.Fatalf("Failed to delete backup: %v", err)
  	} else {
  		fmt.Println("Backup deleted successfully")
  	}
  }
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="9947520e-d5a1-4418-a78d-9f464c9969da"

  curl -X DELETE "https://api.pinecone.io/backups/$BACKUP_ID" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

<Tip>
  You can delete a backup using the [Pinecone console](https://app.pinecone.io/organizations/-/projects-/backups).
</Tip>

## Schedule automated backups

Instead of creating backups manually, you can define a recurring schedule that automatically creates backups at a daily, weekly, or monthly frequency. Each schedule includes a retention policy that automatically deletes old backups, keeping storage costs predictable. Each index supports one active schedule at a time.

### Create a backup schedule

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups) and go to the **Backups** tab.
    2. Find your index and, in the **Schedule** column, click **add**. Alternatively, select **Schedule backups** from the actions menu of the index.
    3. In the **Add a backup schedule** modal, select a **Frequency** (daily, weekly, or monthly).
    4. Select a **Retention** period. Each backup created by the schedule is automatically deleted after this period.
    5. Click **Add schedule**.

    Pinecone names the schedule and assigns its run time automatically.
  </Tab>

  <Tab title="API">
    <Note>
      The scheduled backups API requires `X-Pinecone-API-Version: unstable`.
    </Note>

    To [create a backup schedule](/reference/api/2026-04/control-plane/create_backup_schedule):

    ```bash curl theme={null}
    curl -sS -X POST "https://api.pinecone.io/indexes/${INDEX_NAME}/backup-schedules" \
      -H "api-key: ${PINECONE_API_KEY}" \
      -H "X-Pinecone-API-Version: unstable" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "my-nightly-backup",
        "schedule": {
          "type": "time-based",
          "frequency": "daily"
        },
        "retention": {
          "expire_after_days": 7
        }
      }'
    ```

    Use `"frequency": "weekly"` or `"monthly"` as needed. The retention policy (`expire_after_days`) is required.
  </Tab>
</Tabs>

### Manage backup schedules

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/backups) and go to the **Backups** tab.
    2. Find your index and, in the **Schedule** column, click the schedule. This opens the **Scheduled backups** page for the index.

    For each schedule, the page shows the frequency, retention period, and next scheduled run time. From here, you can:

    * **Pause or resume a schedule**: Use the toggle on the schedule. An index can have up to three schedules, but only one can be enabled at a time.
    * **Edit a schedule**: Expand the schedule, change the **Frequency** or **Retention**, and click **Update**.
    * **Delete a schedule**: Select **Delete** from the actions menu of the schedule.
  </Tab>

  <Tab title="API">
    <Note>
      The scheduled backups API requires `X-Pinecone-API-Version: unstable`.
    </Note>

    You can [list schedules](/reference/api/2026-04/control-plane/list_backup_schedules), [update a schedule](/reference/api/2026-04/control-plane/update_backup_schedule) (e.g., to pause it or change the frequency), [delete a schedule](/reference/api/2026-04/control-plane/delete_backup_schedule), and [view the backup history](/reference/api/2026-04/control-plane/list_backup_schedule_history) for a schedule.
  </Tab>
</Tabs>

Deleting a schedule does not delete any backups that were previously created by it. For more details, see [Scheduled backups](/guides/manage-data/backups-overview#scheduled-backups).
